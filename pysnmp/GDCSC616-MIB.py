# SNMP MIB module (GDCSC616-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCSC616-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:21 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Bql_ObjectIdentity = ObjectIdentity
bql = _Bql_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10)
)


class _BqlMIBVersion_Type(DisplayString):
    """Custom type bqlMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_BqlMIBVersion_Type.__name__ = "DisplayString"
_BqlMIBVersion_Object = MibScalar
bqlMIBVersion = _BqlMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 1),
    _BqlMIBVersion_Type()
)
bqlMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlMIBVersion.setStatus("mandatory")
_BqlWhatAreYouTable_Object = MibTable
bqlWhatAreYouTable = _BqlWhatAreYouTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2)
)
if mibBuilder.loadTexts:
    bqlWhatAreYouTable.setStatus("mandatory")
_BqlWhatAreYouEntry_Object = MibTableRow
bqlWhatAreYouEntry = _BqlWhatAreYouEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1)
)
bqlWhatAreYouEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlWhatAreYouIndex"),
)
if mibBuilder.loadTexts:
    bqlWhatAreYouEntry.setStatus("mandatory")
_BqlWhatAreYouIndex_Type = SCinstance
_BqlWhatAreYouIndex_Object = MibTableColumn
bqlWhatAreYouIndex = _BqlWhatAreYouIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 1),
    _BqlWhatAreYouIndex_Type()
)
bqlWhatAreYouIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlWhatAreYouIndex.setStatus("mandatory")


class _BqlBaseCardType_Type(Integer32):
    """Custom type bqlBaseCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dc610", 2),
          ("dc612", 4),
          ("gt128", 9),
          ("gt128NZ", 10),
          ("sc616", 5))
    )


_BqlBaseCardType_Type.__name__ = "Integer32"
_BqlBaseCardType_Object = MibTableColumn
bqlBaseCardType = _BqlBaseCardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 2),
    _BqlBaseCardType_Type()
)
bqlBaseCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlBaseCardType.setStatus("mandatory")


class _BqlOptionCard_Type(Integer32):
    """Custom type bqlOptionCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_BqlOptionCard_Type.__name__ = "Integer32"
_BqlOptionCard_Object = MibTableColumn
bqlOptionCard = _BqlOptionCard_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 3),
    _BqlOptionCard_Type()
)
bqlOptionCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlOptionCard.setStatus("mandatory")


class _BqlDTE2CardType_Type(Integer32):
    """Custom type bqlDTE2CardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eia530", 1),
          ("none", 7),
          ("x21", 2))
    )


_BqlDTE2CardType_Type.__name__ = "Integer32"
_BqlDTE2CardType_Object = MibTableColumn
bqlDTE2CardType = _BqlDTE2CardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 4),
    _BqlDTE2CardType_Type()
)
bqlDTE2CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDTE2CardType.setStatus("mandatory")


class _BqlDTE1CardType_Type(Integer32):
    """Custom type bqlDTE1CardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eia530", 1),
          ("none", 7),
          ("v35", 3),
          ("x21", 2))
    )


_BqlDTE1CardType_Type.__name__ = "Integer32"
_BqlDTE1CardType_Object = MibTableColumn
bqlDTE1CardType = _BqlDTE1CardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 5),
    _BqlDTE1CardType_Type()
)
bqlDTE1CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDTE1CardType.setStatus("mandatory")


class _BqlCodeRev_Type(DisplayString):
    """Custom type bqlCodeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BqlCodeRev_Type.__name__ = "DisplayString"
_BqlCodeRev_Object = MibTableColumn
bqlCodeRev = _BqlCodeRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 6),
    _BqlCodeRev_Type()
)
bqlCodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCodeRev.setStatus("mandatory")


class _BqlAlarmStatus_Type(OctetString):
    """Custom type bqlAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_BqlAlarmStatus_Type.__name__ = "OctetString"
_BqlAlarmStatus_Object = MibTableColumn
bqlAlarmStatus = _BqlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 2, 1, 7),
    _BqlAlarmStatus_Type()
)
bqlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlAlarmStatus.setStatus("mandatory")
_BqlConfigTable_Object = MibTable
bqlConfigTable = _BqlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3)
)
if mibBuilder.loadTexts:
    bqlConfigTable.setStatus("mandatory")
_BqlConfigEntry_Object = MibTableRow
bqlConfigEntry = _BqlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1)
)
bqlConfigEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlConfigIndex"),
    (0, "GDCSC616-MIB", "bqlConfigChnlIndex"),
)
if mibBuilder.loadTexts:
    bqlConfigEntry.setStatus("mandatory")
_BqlConfigIndex_Type = SCinstance
_BqlConfigIndex_Object = MibTableColumn
bqlConfigIndex = _BqlConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 1),
    _BqlConfigIndex_Type()
)
bqlConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlConfigIndex.setStatus("mandatory")


class _BqlConfigChnlIndex_Type(Integer32):
    """Custom type bqlConfigChnlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_BqlConfigChnlIndex_Type.__name__ = "Integer32"
_BqlConfigChnlIndex_Object = MibTableColumn
bqlConfigChnlIndex = _BqlConfigChnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 2),
    _BqlConfigChnlIndex_Type()
)
bqlConfigChnlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlConfigChnlIndex.setStatus("mandatory")


class _BqlTestPattern_Type(Integer32):
    """Custom type bqlTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pattern2047", 1),
          ("pattern511", 2))
    )


_BqlTestPattern_Type.__name__ = "Integer32"
_BqlTestPattern_Object = MibTableColumn
bqlTestPattern = _BqlTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 3),
    _BqlTestPattern_Type()
)
bqlTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlTestPattern.setStatus("mandatory")


class _BqlRLTimeout_Type(Integer32):
    """Custom type bqlRLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTimeout", 1),
          ("timeoutAfter10Min", 2))
    )


_BqlRLTimeout_Type.__name__ = "Integer32"
_BqlRLTimeout_Object = MibTableColumn
bqlRLTimeout = _BqlRLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 4),
    _BqlRLTimeout_Type()
)
bqlRLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlRLTimeout.setStatus("mandatory")


class _BqlRespRL_Type(Integer32):
    """Custom type bqlRespRL based on Integer32"""
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


_BqlRespRL_Type.__name__ = "Integer32"
_BqlRespRL_Object = MibTableColumn
bqlRespRL = _BqlRespRL_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 5),
    _BqlRespRL_Type()
)
bqlRespRL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlRespRL.setStatus("mandatory")


class _BqlRLType_Type(Integer32):
    """Custom type bqlRLType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pn127", 2),
          ("v54", 1))
    )


_BqlRLType_Type.__name__ = "Integer32"
_BqlRLType_Object = MibTableColumn
bqlRLType = _BqlRLType_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 6),
    _BqlRLType_Type()
)
bqlRLType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlRLType.setStatus("mandatory")


class _BqlBilateralRL_Type(Integer32):
    """Custom type bqlBilateralRL based on Integer32"""
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


_BqlBilateralRL_Type.__name__ = "Integer32"
_BqlBilateralRL_Object = MibTableColumn
bqlBilateralRL = _BqlBilateralRL_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 7),
    _BqlBilateralRL_Type()
)
bqlBilateralRL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlBilateralRL.setStatus("mandatory")


class _BqlInbandRTSDCD_Type(Integer32):
    """Custom type bqlInbandRTSDCD based on Integer32"""
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


_BqlInbandRTSDCD_Type.__name__ = "Integer32"
_BqlInbandRTSDCD_Object = MibTableColumn
bqlInbandRTSDCD = _BqlInbandRTSDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 8),
    _BqlInbandRTSDCD_Type()
)
bqlInbandRTSDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlInbandRTSDCD.setStatus("mandatory")


class _BqlRTS_Type(Integer32):
    """Custom type bqlRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 2),
          ("normal", 1))
    )


_BqlRTS_Type.__name__ = "Integer32"
_BqlRTS_Object = MibTableColumn
bqlRTS = _BqlRTS_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 9),
    _BqlRTS_Type()
)
bqlRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlRTS.setStatus("mandatory")


class _BqlRTSCTSDelay_Type(Integer32):
    """Custom type bqlRTSCTSDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 2),
          ("noDelay", 1))
    )


_BqlRTSCTSDelay_Type.__name__ = "Integer32"
_BqlRTSCTSDelay_Object = MibTableColumn
bqlRTSCTSDelay = _BqlRTSCTSDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 10),
    _BqlRTSCTSDelay_Type()
)
bqlRTSCTSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlRTSCTSDelay.setStatus("mandatory")


class _BqlAntiStream_Type(Integer32):
    """Custom type bqlAntiStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("antistream", 2),
          ("noAntistream", 1))
    )


_BqlAntiStream_Type.__name__ = "Integer32"
_BqlAntiStream_Object = MibTableColumn
bqlAntiStream = _BqlAntiStream_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 11),
    _BqlAntiStream_Type()
)
bqlAntiStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlAntiStream.setStatus("mandatory")


class _BqlTXDataElasticBufr_Type(Integer32):
    """Custom type bqlTXDataElasticBufr based on Integer32"""
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


_BqlTXDataElasticBufr_Type.__name__ = "Integer32"
_BqlTXDataElasticBufr_Object = MibTableColumn
bqlTXDataElasticBufr = _BqlTXDataElasticBufr_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 12),
    _BqlTXDataElasticBufr_Type()
)
bqlTXDataElasticBufr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlTXDataElasticBufr.setStatus("mandatory")


class _BqlRTSCTSDelayTime_Type(Integer32):
    """Custom type bqlRTSCTSDelayTime based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("ms0", 1),
          ("ms10", 3),
          ("ms15", 4),
          ("ms20", 5),
          ("ms25", 6),
          ("ms30", 7),
          ("ms35", 8),
          ("ms40", 9),
          ("ms45", 10),
          ("ms5", 2),
          ("ms50", 11),
          ("ms55", 12),
          ("ms60", 13),
          ("ms65", 14),
          ("ms70", 15),
          ("ms75", 16))
    )


_BqlRTSCTSDelayTime_Type.__name__ = "Integer32"
_BqlRTSCTSDelayTime_Object = MibTableColumn
bqlRTSCTSDelayTime = _BqlRTSCTSDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 13),
    _BqlRTSCTSDelayTime_Type()
)
bqlRTSCTSDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlRTSCTSDelayTime.setStatus("mandatory")


class _BqlAntiStreamTime_Type(Integer32):
    """Custom type bqlAntiStreamTime based on Integer32"""
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
        *(("seconds0", 1),
          ("seconds10", 3),
          ("seconds15", 4),
          ("seconds20", 5),
          ("seconds25", 6),
          ("seconds30", 7),
          ("seconds35", 8),
          ("seconds5", 2))
    )


_BqlAntiStreamTime_Type.__name__ = "Integer32"
_BqlAntiStreamTime_Object = MibTableColumn
bqlAntiStreamTime = _BqlAntiStreamTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 3, 1, 14),
    _BqlAntiStreamTime_Type()
)
bqlAntiStreamTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlAntiStreamTime.setStatus("mandatory")
_BqlConfig1Table_Object = MibTable
bqlConfig1Table = _BqlConfig1Table_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 4)
)
if mibBuilder.loadTexts:
    bqlConfig1Table.setStatus("mandatory")
_BqlConfig1Entry_Object = MibTableRow
bqlConfig1Entry = _BqlConfig1Entry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 4, 1)
)
bqlConfig1Entry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlConfig1Index"),
)
if mibBuilder.loadTexts:
    bqlConfig1Entry.setStatus("mandatory")
_BqlConfig1Index_Type = SCinstance
_BqlConfig1Index_Object = MibTableColumn
bqlConfig1Index = _BqlConfig1Index_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 4, 1, 1),
    _BqlConfig1Index_Type()
)
bqlConfig1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlConfig1Index.setStatus("mandatory")


class _BqlFrontPanel_Type(Integer32):
    """Custom type bqlFrontPanel based on Integer32"""
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


_BqlFrontPanel_Type.__name__ = "Integer32"
_BqlFrontPanel_Object = MibTableColumn
bqlFrontPanel = _BqlFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 4, 1, 2),
    _BqlFrontPanel_Type()
)
bqlFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlFrontPanel.setStatus("mandatory")


class _BqlSoftHard_Type(Integer32):
    """Custom type bqlSoftHard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardmode", 1),
          ("softmode", 2))
    )


_BqlSoftHard_Type.__name__ = "Integer32"
_BqlSoftHard_Object = MibTableColumn
bqlSoftHard = _BqlSoftHard_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 4, 1, 3),
    _BqlSoftHard_Type()
)
bqlSoftHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlSoftHard.setStatus("mandatory")


class _BqlDteStatus_Type(OctetString):
    """Custom type bqlDteStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BqlDteStatus_Type.__name__ = "OctetString"
_BqlDteStatus_Object = MibTableColumn
bqlDteStatus = _BqlDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 4, 1, 4),
    _BqlDteStatus_Type()
)
bqlDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDteStatus.setStatus("mandatory")
_BqlConfig2Table_Object = MibTable
bqlConfig2Table = _BqlConfig2Table_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 5)
)
if mibBuilder.loadTexts:
    bqlConfig2Table.setStatus("mandatory")
_BqlConfig2Entry_Object = MibTableRow
bqlConfig2Entry = _BqlConfig2Entry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 5, 1)
)
bqlConfig2Entry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlConfig2Index"),
)
if mibBuilder.loadTexts:
    bqlConfig2Entry.setStatus("mandatory")
_BqlConfig2Index_Type = SCinstance
_BqlConfig2Index_Object = MibTableColumn
bqlConfig2Index = _BqlConfig2Index_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 5, 1, 1),
    _BqlConfig2Index_Type()
)
bqlConfig2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlConfig2Index.setStatus("mandatory")


class _BqlMasterTXClkSrc_Type(Integer32):
    """Custom type bqlMasterTXClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xtc1", 1),
          ("xtc2", 2))
    )


_BqlMasterTXClkSrc_Type.__name__ = "Integer32"
_BqlMasterTXClkSrc_Object = MibTableColumn
bqlMasterTXClkSrc = _BqlMasterTXClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 5, 1, 2),
    _BqlMasterTXClkSrc_Type()
)
bqlMasterTXClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlMasterTXClkSrc.setStatus("mandatory")
_BqlDiagnosticTable_Object = MibTable
bqlDiagnosticTable = _BqlDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6)
)
if mibBuilder.loadTexts:
    bqlDiagnosticTable.setStatus("mandatory")
_BqlDiagnosticEntry_Object = MibTableRow
bqlDiagnosticEntry = _BqlDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1)
)
bqlDiagnosticEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlDiagnosticIndex"),
    (0, "GDCSC616-MIB", "bqlDiagnosticChnlIndex"),
)
if mibBuilder.loadTexts:
    bqlDiagnosticEntry.setStatus("mandatory")
_BqlDiagnosticIndex_Type = SCinstance
_BqlDiagnosticIndex_Object = MibTableColumn
bqlDiagnosticIndex = _BqlDiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1, 1),
    _BqlDiagnosticIndex_Type()
)
bqlDiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDiagnosticIndex.setStatus("mandatory")


class _BqlDiagnosticChnlIndex_Type(Integer32):
    """Custom type bqlDiagnosticChnlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_BqlDiagnosticChnlIndex_Type.__name__ = "Integer32"
_BqlDiagnosticChnlIndex_Object = MibTableColumn
bqlDiagnosticChnlIndex = _BqlDiagnosticChnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1, 2),
    _BqlDiagnosticChnlIndex_Type()
)
bqlDiagnosticChnlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDiagnosticChnlIndex.setStatus("mandatory")


class _BqlDiagnosticTest_Type(Integer32):
    """Custom type bqlDiagnosticTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BqlDiagnosticTest_Type.__name__ = "Integer32"
_BqlDiagnosticTest_Object = MibTableColumn
bqlDiagnosticTest = _BqlDiagnosticTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1, 3),
    _BqlDiagnosticTest_Type()
)
bqlDiagnosticTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlDiagnosticTest.setStatus("mandatory")


class _BqlDiagnosticLength_Type(Integer32):
    """Custom type bqlDiagnosticLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BqlDiagnosticLength_Type.__name__ = "Integer32"
_BqlDiagnosticLength_Object = MibTableColumn
bqlDiagnosticLength = _BqlDiagnosticLength_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1, 4),
    _BqlDiagnosticLength_Type()
)
bqlDiagnosticLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlDiagnosticLength.setStatus("mandatory")


class _BqlDiagnosticActive_Type(Integer32):
    """Custom type bqlDiagnosticActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_BqlDiagnosticActive_Type.__name__ = "Integer32"
_BqlDiagnosticActive_Object = MibTableColumn
bqlDiagnosticActive = _BqlDiagnosticActive_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1, 5),
    _BqlDiagnosticActive_Type()
)
bqlDiagnosticActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDiagnosticActive.setStatus("mandatory")


class _BqlDiagnosticResults_Type(Integer32):
    """Custom type bqlDiagnosticResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_BqlDiagnosticResults_Type.__name__ = "Integer32"
_BqlDiagnosticResults_Object = MibTableColumn
bqlDiagnosticResults = _BqlDiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 6, 1, 6),
    _BqlDiagnosticResults_Type()
)
bqlDiagnosticResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDiagnosticResults.setStatus("mandatory")
_BqlSC616Alarm_ObjectIdentity = ObjectIdentity
bqlSC616Alarm = _BqlSC616Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7)
)
_BqlAlarmData_ObjectIdentity = ObjectIdentity
bqlAlarmData = _BqlAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1)
)
_BqlNoResponseAlm_ObjectIdentity = ObjectIdentity
bqlNoResponseAlm = _BqlNoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 1)
)
_BqlDiagRxErrAlm_ObjectIdentity = ObjectIdentity
bqlDiagRxErrAlm = _BqlDiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 2)
)
_BqlPowerUpAlm_ObjectIdentity = ObjectIdentity
bqlPowerUpAlm = _BqlPowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 3)
)
_BqlLp2B1QOutofSyncAlm_ObjectIdentity = ObjectIdentity
bqlLp2B1QOutofSyncAlm = _BqlLp2B1QOutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 4)
)
_BqlLpChn1ElasBufrOverUnderFlowAlm_ObjectIdentity = ObjectIdentity
bqlLpChn1ElasBufrOverUnderFlowAlm = _BqlLpChn1ElasBufrOverUnderFlowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 5)
)
_BqlLpChn2ElasBufrOverUnderFlowAlm_ObjectIdentity = ObjectIdentity
bqlLpChn2ElasBufrOverUnderFlowAlm = _BqlLpChn2ElasBufrOverUnderFlowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 6)
)
_BqlLpChn1ExtTxClkAlm_ObjectIdentity = ObjectIdentity
bqlLpChn1ExtTxClkAlm = _BqlLpChn1ExtTxClkAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 7)
)
_BqlLpChn2ExtTxClkAlm_ObjectIdentity = ObjectIdentity
bqlLpChn2ExtTxClkAlm = _BqlLpChn2ExtTxClkAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 8)
)
_BqlLpSealingCurrentNoContinuityAlm_ObjectIdentity = ObjectIdentity
bqlLpSealingCurrentNoContinuityAlm = _BqlLpSealingCurrentNoContinuityAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 7, 1, 9)
)
_BqlSC616LEDStatusTable_Object = MibTable
bqlSC616LEDStatusTable = _BqlSC616LEDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 8)
)
if mibBuilder.loadTexts:
    bqlSC616LEDStatusTable.setStatus("mandatory")
_BqlSC616LEDEntry_Object = MibTableRow
bqlSC616LEDEntry = _BqlSC616LEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 8, 1)
)
bqlSC616LEDEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlSC616LEDIndex"),
)
if mibBuilder.loadTexts:
    bqlSC616LEDEntry.setStatus("mandatory")
_BqlSC616LEDIndex_Type = SCinstance
_BqlSC616LEDIndex_Object = MibTableColumn
bqlSC616LEDIndex = _BqlSC616LEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 8, 1, 1),
    _BqlSC616LEDIndex_Type()
)
bqlSC616LEDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlSC616LEDIndex.setStatus("mandatory")


class _BqlSC616LEDStatus_Type(OctetString):
    """Custom type bqlSC616LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_BqlSC616LEDStatus_Type.__name__ = "OctetString"
_BqlSC616LEDStatus_Object = MibTableColumn
bqlSC616LEDStatus = _BqlSC616LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 8, 1, 2),
    _BqlSC616LEDStatus_Type()
)
bqlSC616LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlSC616LEDStatus.setStatus("mandatory")
_BqlDC610Alarm_ObjectIdentity = ObjectIdentity
bqlDC610Alarm = _BqlDC610Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 9)
)
_BqlDC610AlarmData_ObjectIdentity = ObjectIdentity
bqlDC610AlarmData = _BqlDC610AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 9, 1)
)
_BqlDC610PowerUpAlm_ObjectIdentity = ObjectIdentity
bqlDC610PowerUpAlm = _BqlDC610PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 9, 1, 1)
)
_BqlDC610Chnl1DTRAlm_ObjectIdentity = ObjectIdentity
bqlDC610Chnl1DTRAlm = _BqlDC610Chnl1DTRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 9, 1, 2)
)
_BqlDC610NoResponseAlm_ObjectIdentity = ObjectIdentity
bqlDC610NoResponseAlm = _BqlDC610NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 9, 1, 3)
)
_BqlDC610DiagRxErrAlm_ObjectIdentity = ObjectIdentity
bqlDC610DiagRxErrAlm = _BqlDC610DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 9, 1, 4)
)
_BqlDC610LEDStatusTable_Object = MibTable
bqlDC610LEDStatusTable = _BqlDC610LEDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 10)
)
if mibBuilder.loadTexts:
    bqlDC610LEDStatusTable.setStatus("mandatory")
_BqlDC610LEDEntry_Object = MibTableRow
bqlDC610LEDEntry = _BqlDC610LEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 10, 1)
)
bqlDC610LEDEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlDC610LEDIndex"),
)
if mibBuilder.loadTexts:
    bqlDC610LEDEntry.setStatus("mandatory")
_BqlDC610LEDIndex_Type = SCinstance
_BqlDC610LEDIndex_Object = MibTableColumn
bqlDC610LEDIndex = _BqlDC610LEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 10, 1, 1),
    _BqlDC610LEDIndex_Type()
)
bqlDC610LEDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDC610LEDIndex.setStatus("mandatory")


class _BqlDC610LEDStatus_Type(OctetString):
    """Custom type bqlDC610LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BqlDC610LEDStatus_Type.__name__ = "OctetString"
_BqlDC610LEDStatus_Object = MibTableColumn
bqlDC610LEDStatus = _BqlDC610LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 10, 1, 2),
    _BqlDC610LEDStatus_Type()
)
bqlDC610LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDC610LEDStatus.setStatus("mandatory")
_BqlDC612Alarm_ObjectIdentity = ObjectIdentity
bqlDC612Alarm = _BqlDC612Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11)
)
_BqlDC612AlarmData_ObjectIdentity = ObjectIdentity
bqlDC612AlarmData = _BqlDC612AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11, 1)
)
_BqlDC612PowerUpAlm_ObjectIdentity = ObjectIdentity
bqlDC612PowerUpAlm = _BqlDC612PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11, 1, 1)
)
_BqlDC612Chnl1DTRAlm_ObjectIdentity = ObjectIdentity
bqlDC612Chnl1DTRAlm = _BqlDC612Chnl1DTRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11, 1, 2)
)
_BqlDC612Chnl2DTRAlm_ObjectIdentity = ObjectIdentity
bqlDC612Chnl2DTRAlm = _BqlDC612Chnl2DTRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11, 1, 3)
)
_BqlDC612NoResponseAlm_ObjectIdentity = ObjectIdentity
bqlDC612NoResponseAlm = _BqlDC612NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11, 1, 4)
)
_BqlDC612DiagRxErrAlm_ObjectIdentity = ObjectIdentity
bqlDC612DiagRxErrAlm = _BqlDC612DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 11, 1, 5)
)
_BqlDC612LEDStatusTable_Object = MibTable
bqlDC612LEDStatusTable = _BqlDC612LEDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 12)
)
if mibBuilder.loadTexts:
    bqlDC612LEDStatusTable.setStatus("mandatory")
_BqlDC612LEDEntry_Object = MibTableRow
bqlDC612LEDEntry = _BqlDC612LEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 12, 1)
)
bqlDC612LEDEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlDC612LEDIndex"),
)
if mibBuilder.loadTexts:
    bqlDC612LEDEntry.setStatus("mandatory")
_BqlDC612LEDIndex_Type = SCinstance
_BqlDC612LEDIndex_Object = MibTableColumn
bqlDC612LEDIndex = _BqlDC612LEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 12, 1, 1),
    _BqlDC612LEDIndex_Type()
)
bqlDC612LEDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDC612LEDIndex.setStatus("mandatory")


class _BqlDC612LEDStatus_Type(OctetString):
    """Custom type bqlDC612LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_BqlDC612LEDStatus_Type.__name__ = "OctetString"
_BqlDC612LEDStatus_Object = MibTableColumn
bqlDC612LEDStatus = _BqlDC612LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 12, 1, 2),
    _BqlDC612LEDStatus_Type()
)
bqlDC612LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDC612LEDStatus.setStatus("mandatory")
_BqlControlTable_Object = MibTable
bqlControlTable = _BqlControlTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 13)
)
if mibBuilder.loadTexts:
    bqlControlTable.setStatus("mandatory")
_BqlControlEntry_Object = MibTableRow
bqlControlEntry = _BqlControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 13, 1)
)
bqlControlEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlControlIndex"),
)
if mibBuilder.loadTexts:
    bqlControlEntry.setStatus("mandatory")
_BqlControlIndex_Type = SCinstance
_BqlControlIndex_Object = MibTableColumn
bqlControlIndex = _BqlControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 13, 1, 1),
    _BqlControlIndex_Type()
)
bqlControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlControlIndex.setStatus("mandatory")


class _BqlSoftReset_Type(Integer32):
    """Custom type bqlSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_BqlSoftReset_Type.__name__ = "Integer32"
_BqlSoftReset_Object = MibTableColumn
bqlSoftReset = _BqlSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 13, 1, 2),
    _BqlSoftReset_Type()
)
bqlSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlSoftReset.setStatus("mandatory")


class _BqlEraseConfig_Type(Integer32):
    """Custom type bqlEraseConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erase", 2),
          ("normal", 1))
    )


_BqlEraseConfig_Type.__name__ = "Integer32"
_BqlEraseConfig_Object = MibTableColumn
bqlEraseConfig = _BqlEraseConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 13, 1, 3),
    _BqlEraseConfig_Type()
)
bqlEraseConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlEraseConfig.setStatus("mandatory")
_BqlCurrentTable_Object = MibTable
bqlCurrentTable = _BqlCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14)
)
if mibBuilder.loadTexts:
    bqlCurrentTable.setStatus("mandatory")
_BqlCurrentEntry_Object = MibTableRow
bqlCurrentEntry = _BqlCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1)
)
bqlCurrentEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlCurrentIndex"),
)
if mibBuilder.loadTexts:
    bqlCurrentEntry.setStatus("mandatory")
_BqlCurrentIndex_Type = SCinstance
_BqlCurrentIndex_Object = MibTableColumn
bqlCurrentIndex = _BqlCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1, 1),
    _BqlCurrentIndex_Type()
)
bqlCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCurrentIndex.setStatus("mandatory")
_BqlCurrentESs_Type = Gauge32
_BqlCurrentESs_Object = MibTableColumn
bqlCurrentESs = _BqlCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1, 2),
    _BqlCurrentESs_Type()
)
bqlCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCurrentESs.setStatus("mandatory")
_BqlCurrentBESs_Type = Gauge32
_BqlCurrentBESs_Object = MibTableColumn
bqlCurrentBESs = _BqlCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1, 3),
    _BqlCurrentBESs_Type()
)
bqlCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCurrentBESs.setStatus("mandatory")
_BqlCurrentSESs_Type = Gauge32
_BqlCurrentSESs_Object = MibTableColumn
bqlCurrentSESs = _BqlCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1, 4),
    _BqlCurrentSESs_Type()
)
bqlCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCurrentSESs.setStatus("mandatory")
_BqlCurrentUASs_Type = Gauge32
_BqlCurrentUASs_Object = MibTableColumn
bqlCurrentUASs = _BqlCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1, 5),
    _BqlCurrentUASs_Type()
)
bqlCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCurrentUASs.setStatus("mandatory")


class _BqlCurrentStats_Type(OctetString):
    """Custom type bqlCurrentStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_BqlCurrentStats_Type.__name__ = "OctetString"
_BqlCurrentStats_Object = MibTableColumn
bqlCurrentStats = _BqlCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 14, 1, 6),
    _BqlCurrentStats_Type()
)
bqlCurrentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlCurrentStats.setStatus("mandatory")
_BqlIntervalTable_Object = MibTable
bqlIntervalTable = _BqlIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15)
)
if mibBuilder.loadTexts:
    bqlIntervalTable.setStatus("mandatory")
_BqlIntervalEntry_Object = MibTableRow
bqlIntervalEntry = _BqlIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1)
)
bqlIntervalEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlIntervalIndex"),
    (0, "GDCSC616-MIB", "bqlIntervalNumber"),
)
if mibBuilder.loadTexts:
    bqlIntervalEntry.setStatus("mandatory")
_BqlIntervalIndex_Type = SCinstance
_BqlIntervalIndex_Object = MibTableColumn
bqlIntervalIndex = _BqlIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 1),
    _BqlIntervalIndex_Type()
)
bqlIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalIndex.setStatus("mandatory")


class _BqlIntervalNumber_Type(Integer32):
    """Custom type bqlIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BqlIntervalNumber_Type.__name__ = "Integer32"
_BqlIntervalNumber_Object = MibTableColumn
bqlIntervalNumber = _BqlIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 2),
    _BqlIntervalNumber_Type()
)
bqlIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalNumber.setStatus("mandatory")
_BqlIntervalESs_Type = Gauge32
_BqlIntervalESs_Object = MibTableColumn
bqlIntervalESs = _BqlIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 3),
    _BqlIntervalESs_Type()
)
bqlIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalESs.setStatus("mandatory")
_BqlIntervalBESs_Type = Gauge32
_BqlIntervalBESs_Object = MibTableColumn
bqlIntervalBESs = _BqlIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 4),
    _BqlIntervalBESs_Type()
)
bqlIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalBESs.setStatus("mandatory")
_BqlIntervalSESs_Type = Gauge32
_BqlIntervalSESs_Object = MibTableColumn
bqlIntervalSESs = _BqlIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 5),
    _BqlIntervalSESs_Type()
)
bqlIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalSESs.setStatus("mandatory")
_BqlIntervalUASs_Type = Gauge32
_BqlIntervalUASs_Object = MibTableColumn
bqlIntervalUASs = _BqlIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 6),
    _BqlIntervalUASs_Type()
)
bqlIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalUASs.setStatus("mandatory")


class _BqlIntervalStats_Type(OctetString):
    """Custom type bqlIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_BqlIntervalStats_Type.__name__ = "OctetString"
_BqlIntervalStats_Object = MibTableColumn
bqlIntervalStats = _BqlIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 15, 1, 7),
    _BqlIntervalStats_Type()
)
bqlIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalStats.setStatus("mandatory")
_BqlTotalTable_Object = MibTable
bqlTotalTable = _BqlTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16)
)
if mibBuilder.loadTexts:
    bqlTotalTable.setStatus("mandatory")
_BqlTotalEntry_Object = MibTableRow
bqlTotalEntry = _BqlTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1)
)
bqlTotalEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlTotalIndex"),
)
if mibBuilder.loadTexts:
    bqlTotalEntry.setStatus("mandatory")
_BqlTotalIndex_Type = SCinstance
_BqlTotalIndex_Object = MibTableColumn
bqlTotalIndex = _BqlTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1, 1),
    _BqlTotalIndex_Type()
)
bqlTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlTotalIndex.setStatus("mandatory")
_BqlTotalESs_Type = Gauge32
_BqlTotalESs_Object = MibTableColumn
bqlTotalESs = _BqlTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1, 2),
    _BqlTotalESs_Type()
)
bqlTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlTotalESs.setStatus("mandatory")
_BqlTotalBESs_Type = Gauge32
_BqlTotalBESs_Object = MibTableColumn
bqlTotalBESs = _BqlTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1, 3),
    _BqlTotalBESs_Type()
)
bqlTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlTotalBESs.setStatus("mandatory")
_BqlTotalSESs_Type = Gauge32
_BqlTotalSESs_Object = MibTableColumn
bqlTotalSESs = _BqlTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1, 4),
    _BqlTotalSESs_Type()
)
bqlTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlTotalSESs.setStatus("mandatory")
_BqlTotalUASs_Type = Gauge32
_BqlTotalUASs_Object = MibTableColumn
bqlTotalUASs = _BqlTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1, 5),
    _BqlTotalUASs_Type()
)
bqlTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlTotalUASs.setStatus("mandatory")


class _BqlTotalStats_Type(OctetString):
    """Custom type bqlTotalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_BqlTotalStats_Type.__name__ = "OctetString"
_BqlTotalStats_Object = MibTableColumn
bqlTotalStats = _BqlTotalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 16, 1, 6),
    _BqlTotalStats_Type()
)
bqlTotalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlTotalStats.setStatus("mandatory")
_BqlDTERateTable_Object = MibTable
bqlDTERateTable = _BqlDTERateTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17)
)
if mibBuilder.loadTexts:
    bqlDTERateTable.setStatus("mandatory")
_BqlDTEEntry_Object = MibTableRow
bqlDTEEntry = _BqlDTEEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17, 1)
)
bqlDTEEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlDTEIndex"),
)
if mibBuilder.loadTexts:
    bqlDTEEntry.setStatus("mandatory")
_BqlDTEIndex_Type = SCinstance
_BqlDTEIndex_Object = MibTableColumn
bqlDTEIndex = _BqlDTEIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17, 1, 1),
    _BqlDTEIndex_Type()
)
bqlDTEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDTEIndex.setStatus("mandatory")


class _BqlDTE2Mapped_Type(Integer32):
    """Custom type bqlDTE2Mapped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("toChannel1", 2),
          ("toChannel2", 1))
    )


_BqlDTE2Mapped_Type.__name__ = "Integer32"
_BqlDTE2Mapped_Object = MibTableColumn
bqlDTE2Mapped = _BqlDTE2Mapped_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17, 1, 2),
    _BqlDTE2Mapped_Type()
)
bqlDTE2Mapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlDTE2Mapped.setStatus("mandatory")


class _BqlDTE2DataRate_Type(Integer32):
    """Custom type bqlDTE2DataRate based on Integer32"""
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
        *(("kBps128000", 10),
          ("kBps19200", 4),
          ("kBps2400", 1),
          ("kBps38400", 5),
          ("kBps4800", 2),
          ("kBps48000", 6),
          ("kBps56000", 7),
          ("kBps57600", 8),
          ("kBps64000", 9),
          ("kBps9600", 3))
    )


_BqlDTE2DataRate_Type.__name__ = "Integer32"
_BqlDTE2DataRate_Object = MibTableColumn
bqlDTE2DataRate = _BqlDTE2DataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17, 1, 3),
    _BqlDTE2DataRate_Type()
)
bqlDTE2DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlDTE2DataRate.setStatus("mandatory")


class _BqlDTE1Mapped_Type(Integer32):
    """Custom type bqlDTE1Mapped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("toChannel1", 1),
          ("toChannel2", 2))
    )


_BqlDTE1Mapped_Type.__name__ = "Integer32"
_BqlDTE1Mapped_Object = MibTableColumn
bqlDTE1Mapped = _BqlDTE1Mapped_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17, 1, 4),
    _BqlDTE1Mapped_Type()
)
bqlDTE1Mapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlDTE1Mapped.setStatus("mandatory")


class _BqlDTE1DataRate_Type(Integer32):
    """Custom type bqlDTE1DataRate based on Integer32"""
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
        *(("kBps128000", 10),
          ("kBps19200", 4),
          ("kBps2400", 1),
          ("kBps38400", 5),
          ("kBps4800", 2),
          ("kBps48000", 6),
          ("kBps56000", 7),
          ("kBps57600", 8),
          ("kBps64000", 9),
          ("kBps9600", 3))
    )


_BqlDTE1DataRate_Type.__name__ = "Integer32"
_BqlDTE1DataRate_Object = MibTableColumn
bqlDTE1DataRate = _BqlDTE1DataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 17, 1, 5),
    _BqlDTE1DataRate_Type()
)
bqlDTE1DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlDTE1DataRate.setStatus("mandatory")
_BqlIntervalMaintenanceTable_Object = MibTable
bqlIntervalMaintenanceTable = _BqlIntervalMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 18)
)
if mibBuilder.loadTexts:
    bqlIntervalMaintenanceTable.setStatus("mandatory")
_BqlIntervalMaintenanceEntry_Object = MibTableRow
bqlIntervalMaintenanceEntry = _BqlIntervalMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 18, 1)
)
bqlIntervalMaintenanceEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlIntervalMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    bqlIntervalMaintenanceEntry.setStatus("mandatory")
_BqlIntervalMaintenanceIndex_Type = SCinstance
_BqlIntervalMaintenanceIndex_Object = MibTableColumn
bqlIntervalMaintenanceIndex = _BqlIntervalMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 18, 1, 1),
    _BqlIntervalMaintenanceIndex_Type()
)
bqlIntervalMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlIntervalMaintenanceIndex.setStatus("mandatory")


class _BqlResetIntervals_Type(Integer32):
    """Custom type bqlResetIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_BqlResetIntervals_Type.__name__ = "Integer32"
_BqlResetIntervals_Object = MibTableColumn
bqlResetIntervals = _BqlResetIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 18, 1, 2),
    _BqlResetIntervals_Type()
)
bqlResetIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bqlResetIntervals.setStatus("mandatory")


class _BqlNumberofValidIntervals_Type(Integer32):
    """Custom type bqlNumberofValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_BqlNumberofValidIntervals_Type.__name__ = "Integer32"
_BqlNumberofValidIntervals_Object = MibTableColumn
bqlNumberofValidIntervals = _BqlNumberofValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 18, 1, 3),
    _BqlNumberofValidIntervals_Type()
)
bqlNumberofValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlNumberofValidIntervals.setStatus("mandatory")
_BqlDC610LEDStatusNZTable_Object = MibTable
bqlDC610LEDStatusNZTable = _BqlDC610LEDStatusNZTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 19)
)
if mibBuilder.loadTexts:
    bqlDC610LEDStatusNZTable.setStatus("mandatory")
_BqlDC610LEDNZEntry_Object = MibTableRow
bqlDC610LEDNZEntry = _BqlDC610LEDNZEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 19, 1)
)
bqlDC610LEDNZEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlDC610LEDNZIndex"),
)
if mibBuilder.loadTexts:
    bqlDC610LEDNZEntry.setStatus("mandatory")
_BqlDC610LEDNZIndex_Type = SCinstance
_BqlDC610LEDNZIndex_Object = MibTableColumn
bqlDC610LEDNZIndex = _BqlDC610LEDNZIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 19, 1, 1),
    _BqlDC610LEDNZIndex_Type()
)
bqlDC610LEDNZIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDC610LEDNZIndex.setStatus("mandatory")


class _BqlDC610LEDNZStatus_Type(OctetString):
    """Custom type bqlDC610LEDNZStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BqlDC610LEDNZStatus_Type.__name__ = "OctetString"
_BqlDC610LEDNZStatus_Object = MibTableColumn
bqlDC610LEDNZStatus = _BqlDC610LEDNZStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 19, 1, 2),
    _BqlDC610LEDNZStatus_Type()
)
bqlDC610LEDNZStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlDC610LEDNZStatus.setStatus("mandatory")
_BqlGT128Alarm_ObjectIdentity = ObjectIdentity
bqlGT128Alarm = _BqlGT128Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 20)
)
_BqlGT128AlarmData_ObjectIdentity = ObjectIdentity
bqlGT128AlarmData = _BqlGT128AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 20, 1)
)
_BqlGT128NoResponseAlm_ObjectIdentity = ObjectIdentity
bqlGT128NoResponseAlm = _BqlGT128NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 20, 1, 1)
)
_BqlGT128DiagRxErrAlm_ObjectIdentity = ObjectIdentity
bqlGT128DiagRxErrAlm = _BqlGT128DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 20, 1, 2)
)
_BqlGT128PowerUpAlm_ObjectIdentity = ObjectIdentity
bqlGT128PowerUpAlm = _BqlGT128PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 20, 1, 3)
)
_BqlGT128Chnl1DTRAlm_ObjectIdentity = ObjectIdentity
bqlGT128Chnl1DTRAlm = _BqlGT128Chnl1DTRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 20, 1, 4)
)
_BqlGT128LEDStatusTable_Object = MibTable
bqlGT128LEDStatusTable = _BqlGT128LEDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 21)
)
if mibBuilder.loadTexts:
    bqlGT128LEDStatusTable.setStatus("mandatory")
_BqlGT128LEDEntry_Object = MibTableRow
bqlGT128LEDEntry = _BqlGT128LEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 21, 1)
)
bqlGT128LEDEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlGT128LEDIndex"),
)
if mibBuilder.loadTexts:
    bqlGT128LEDEntry.setStatus("mandatory")
_BqlGT128LEDIndex_Type = SCinstance
_BqlGT128LEDIndex_Object = MibTableColumn
bqlGT128LEDIndex = _BqlGT128LEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 21, 1, 1),
    _BqlGT128LEDIndex_Type()
)
bqlGT128LEDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlGT128LEDIndex.setStatus("mandatory")


class _BqlGT128LEDStatus_Type(OctetString):
    """Custom type bqlGT128LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BqlGT128LEDStatus_Type.__name__ = "OctetString"
_BqlGT128LEDStatus_Object = MibTableColumn
bqlGT128LEDStatus = _BqlGT128LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 21, 1, 2),
    _BqlGT128LEDStatus_Type()
)
bqlGT128LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlGT128LEDStatus.setStatus("mandatory")
_BqlGT128NZAlarm_ObjectIdentity = ObjectIdentity
bqlGT128NZAlarm = _BqlGT128NZAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 22)
)
_BqlGT128NZAlarmData_ObjectIdentity = ObjectIdentity
bqlGT128NZAlarmData = _BqlGT128NZAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 22, 1)
)
_BqlGT128NZNoResponseAlm_ObjectIdentity = ObjectIdentity
bqlGT128NZNoResponseAlm = _BqlGT128NZNoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 22, 1, 1)
)
_BqlGT128NZDiagRxErrAlm_ObjectIdentity = ObjectIdentity
bqlGT128NZDiagRxErrAlm = _BqlGT128NZDiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 22, 1, 2)
)
_BqlGT128NZPowerUpAlm_ObjectIdentity = ObjectIdentity
bqlGT128NZPowerUpAlm = _BqlGT128NZPowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 22, 1, 3)
)
_BqlGT128NZChnl1DTRAlm_ObjectIdentity = ObjectIdentity
bqlGT128NZChnl1DTRAlm = _BqlGT128NZChnl1DTRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 10, 22, 1, 4)
)
_BqlGT128LEDNZStatusTable_Object = MibTable
bqlGT128LEDNZStatusTable = _BqlGT128LEDNZStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 23)
)
if mibBuilder.loadTexts:
    bqlGT128LEDNZStatusTable.setStatus("mandatory")
_BqlGT128LEDNZEntry_Object = MibTableRow
bqlGT128LEDNZEntry = _BqlGT128LEDNZEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 23, 1)
)
bqlGT128LEDNZEntry.setIndexNames(
    (0, "GDCSC616-MIB", "bqlGT128LEDNZIndex"),
)
if mibBuilder.loadTexts:
    bqlGT128LEDNZEntry.setStatus("mandatory")
_BqlGT128LEDNZIndex_Type = SCinstance
_BqlGT128LEDNZIndex_Object = MibTableColumn
bqlGT128LEDNZIndex = _BqlGT128LEDNZIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 23, 1, 1),
    _BqlGT128LEDNZIndex_Type()
)
bqlGT128LEDNZIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlGT128LEDNZIndex.setStatus("mandatory")


class _BqlGT128LEDNZStatus_Type(OctetString):
    """Custom type bqlGT128LEDNZStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BqlGT128LEDNZStatus_Type.__name__ = "OctetString"
_BqlGT128LEDNZStatus_Object = MibTableColumn
bqlGT128LEDNZStatus = _BqlGT128LEDNZStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 10, 23, 1, 2),
    _BqlGT128LEDNZStatus_Type()
)
bqlGT128LEDNZStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bqlGT128LEDNZStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCSC616-MIB",
    **{"gdc": gdc,
       "bql": bql,
       "bqlMIBVersion": bqlMIBVersion,
       "bqlWhatAreYouTable": bqlWhatAreYouTable,
       "bqlWhatAreYouEntry": bqlWhatAreYouEntry,
       "bqlWhatAreYouIndex": bqlWhatAreYouIndex,
       "bqlBaseCardType": bqlBaseCardType,
       "bqlOptionCard": bqlOptionCard,
       "bqlDTE2CardType": bqlDTE2CardType,
       "bqlDTE1CardType": bqlDTE1CardType,
       "bqlCodeRev": bqlCodeRev,
       "bqlAlarmStatus": bqlAlarmStatus,
       "bqlConfigTable": bqlConfigTable,
       "bqlConfigEntry": bqlConfigEntry,
       "bqlConfigIndex": bqlConfigIndex,
       "bqlConfigChnlIndex": bqlConfigChnlIndex,
       "bqlTestPattern": bqlTestPattern,
       "bqlRLTimeout": bqlRLTimeout,
       "bqlRespRL": bqlRespRL,
       "bqlRLType": bqlRLType,
       "bqlBilateralRL": bqlBilateralRL,
       "bqlInbandRTSDCD": bqlInbandRTSDCD,
       "bqlRTS": bqlRTS,
       "bqlRTSCTSDelay": bqlRTSCTSDelay,
       "bqlAntiStream": bqlAntiStream,
       "bqlTXDataElasticBufr": bqlTXDataElasticBufr,
       "bqlRTSCTSDelayTime": bqlRTSCTSDelayTime,
       "bqlAntiStreamTime": bqlAntiStreamTime,
       "bqlConfig1Table": bqlConfig1Table,
       "bqlConfig1Entry": bqlConfig1Entry,
       "bqlConfig1Index": bqlConfig1Index,
       "bqlFrontPanel": bqlFrontPanel,
       "bqlSoftHard": bqlSoftHard,
       "bqlDteStatus": bqlDteStatus,
       "bqlConfig2Table": bqlConfig2Table,
       "bqlConfig2Entry": bqlConfig2Entry,
       "bqlConfig2Index": bqlConfig2Index,
       "bqlMasterTXClkSrc": bqlMasterTXClkSrc,
       "bqlDiagnosticTable": bqlDiagnosticTable,
       "bqlDiagnosticEntry": bqlDiagnosticEntry,
       "bqlDiagnosticIndex": bqlDiagnosticIndex,
       "bqlDiagnosticChnlIndex": bqlDiagnosticChnlIndex,
       "bqlDiagnosticTest": bqlDiagnosticTest,
       "bqlDiagnosticLength": bqlDiagnosticLength,
       "bqlDiagnosticActive": bqlDiagnosticActive,
       "bqlDiagnosticResults": bqlDiagnosticResults,
       "bqlSC616Alarm": bqlSC616Alarm,
       "bqlAlarmData": bqlAlarmData,
       "bqlNoResponseAlm": bqlNoResponseAlm,
       "bqlDiagRxErrAlm": bqlDiagRxErrAlm,
       "bqlPowerUpAlm": bqlPowerUpAlm,
       "bqlLp2B1QOutofSyncAlm": bqlLp2B1QOutofSyncAlm,
       "bqlLpChn1ElasBufrOverUnderFlowAlm": bqlLpChn1ElasBufrOverUnderFlowAlm,
       "bqlLpChn2ElasBufrOverUnderFlowAlm": bqlLpChn2ElasBufrOverUnderFlowAlm,
       "bqlLpChn1ExtTxClkAlm": bqlLpChn1ExtTxClkAlm,
       "bqlLpChn2ExtTxClkAlm": bqlLpChn2ExtTxClkAlm,
       "bqlLpSealingCurrentNoContinuityAlm": bqlLpSealingCurrentNoContinuityAlm,
       "bqlSC616LEDStatusTable": bqlSC616LEDStatusTable,
       "bqlSC616LEDEntry": bqlSC616LEDEntry,
       "bqlSC616LEDIndex": bqlSC616LEDIndex,
       "bqlSC616LEDStatus": bqlSC616LEDStatus,
       "bqlDC610Alarm": bqlDC610Alarm,
       "bqlDC610AlarmData": bqlDC610AlarmData,
       "bqlDC610PowerUpAlm": bqlDC610PowerUpAlm,
       "bqlDC610Chnl1DTRAlm": bqlDC610Chnl1DTRAlm,
       "bqlDC610NoResponseAlm": bqlDC610NoResponseAlm,
       "bqlDC610DiagRxErrAlm": bqlDC610DiagRxErrAlm,
       "bqlDC610LEDStatusTable": bqlDC610LEDStatusTable,
       "bqlDC610LEDEntry": bqlDC610LEDEntry,
       "bqlDC610LEDIndex": bqlDC610LEDIndex,
       "bqlDC610LEDStatus": bqlDC610LEDStatus,
       "bqlDC612Alarm": bqlDC612Alarm,
       "bqlDC612AlarmData": bqlDC612AlarmData,
       "bqlDC612PowerUpAlm": bqlDC612PowerUpAlm,
       "bqlDC612Chnl1DTRAlm": bqlDC612Chnl1DTRAlm,
       "bqlDC612Chnl2DTRAlm": bqlDC612Chnl2DTRAlm,
       "bqlDC612NoResponseAlm": bqlDC612NoResponseAlm,
       "bqlDC612DiagRxErrAlm": bqlDC612DiagRxErrAlm,
       "bqlDC612LEDStatusTable": bqlDC612LEDStatusTable,
       "bqlDC612LEDEntry": bqlDC612LEDEntry,
       "bqlDC612LEDIndex": bqlDC612LEDIndex,
       "bqlDC612LEDStatus": bqlDC612LEDStatus,
       "bqlControlTable": bqlControlTable,
       "bqlControlEntry": bqlControlEntry,
       "bqlControlIndex": bqlControlIndex,
       "bqlSoftReset": bqlSoftReset,
       "bqlEraseConfig": bqlEraseConfig,
       "bqlCurrentTable": bqlCurrentTable,
       "bqlCurrentEntry": bqlCurrentEntry,
       "bqlCurrentIndex": bqlCurrentIndex,
       "bqlCurrentESs": bqlCurrentESs,
       "bqlCurrentBESs": bqlCurrentBESs,
       "bqlCurrentSESs": bqlCurrentSESs,
       "bqlCurrentUASs": bqlCurrentUASs,
       "bqlCurrentStats": bqlCurrentStats,
       "bqlIntervalTable": bqlIntervalTable,
       "bqlIntervalEntry": bqlIntervalEntry,
       "bqlIntervalIndex": bqlIntervalIndex,
       "bqlIntervalNumber": bqlIntervalNumber,
       "bqlIntervalESs": bqlIntervalESs,
       "bqlIntervalBESs": bqlIntervalBESs,
       "bqlIntervalSESs": bqlIntervalSESs,
       "bqlIntervalUASs": bqlIntervalUASs,
       "bqlIntervalStats": bqlIntervalStats,
       "bqlTotalTable": bqlTotalTable,
       "bqlTotalEntry": bqlTotalEntry,
       "bqlTotalIndex": bqlTotalIndex,
       "bqlTotalESs": bqlTotalESs,
       "bqlTotalBESs": bqlTotalBESs,
       "bqlTotalSESs": bqlTotalSESs,
       "bqlTotalUASs": bqlTotalUASs,
       "bqlTotalStats": bqlTotalStats,
       "bqlDTERateTable": bqlDTERateTable,
       "bqlDTEEntry": bqlDTEEntry,
       "bqlDTEIndex": bqlDTEIndex,
       "bqlDTE2Mapped": bqlDTE2Mapped,
       "bqlDTE2DataRate": bqlDTE2DataRate,
       "bqlDTE1Mapped": bqlDTE1Mapped,
       "bqlDTE1DataRate": bqlDTE1DataRate,
       "bqlIntervalMaintenanceTable": bqlIntervalMaintenanceTable,
       "bqlIntervalMaintenanceEntry": bqlIntervalMaintenanceEntry,
       "bqlIntervalMaintenanceIndex": bqlIntervalMaintenanceIndex,
       "bqlResetIntervals": bqlResetIntervals,
       "bqlNumberofValidIntervals": bqlNumberofValidIntervals,
       "bqlDC610LEDStatusNZTable": bqlDC610LEDStatusNZTable,
       "bqlDC610LEDNZEntry": bqlDC610LEDNZEntry,
       "bqlDC610LEDNZIndex": bqlDC610LEDNZIndex,
       "bqlDC610LEDNZStatus": bqlDC610LEDNZStatus,
       "bqlGT128Alarm": bqlGT128Alarm,
       "bqlGT128AlarmData": bqlGT128AlarmData,
       "bqlGT128NoResponseAlm": bqlGT128NoResponseAlm,
       "bqlGT128DiagRxErrAlm": bqlGT128DiagRxErrAlm,
       "bqlGT128PowerUpAlm": bqlGT128PowerUpAlm,
       "bqlGT128Chnl1DTRAlm": bqlGT128Chnl1DTRAlm,
       "bqlGT128LEDStatusTable": bqlGT128LEDStatusTable,
       "bqlGT128LEDEntry": bqlGT128LEDEntry,
       "bqlGT128LEDIndex": bqlGT128LEDIndex,
       "bqlGT128LEDStatus": bqlGT128LEDStatus,
       "bqlGT128NZAlarm": bqlGT128NZAlarm,
       "bqlGT128NZAlarmData": bqlGT128NZAlarmData,
       "bqlGT128NZNoResponseAlm": bqlGT128NZNoResponseAlm,
       "bqlGT128NZDiagRxErrAlm": bqlGT128NZDiagRxErrAlm,
       "bqlGT128NZPowerUpAlm": bqlGT128NZPowerUpAlm,
       "bqlGT128NZChnl1DTRAlm": bqlGT128NZChnl1DTRAlm,
       "bqlGT128LEDNZStatusTable": bqlGT128LEDNZStatusTable,
       "bqlGT128LEDNZEntry": bqlGT128LEDNZEntry,
       "bqlGT128LEDNZIndex": bqlGT128LEDNZIndex,
       "bqlGT128LEDNZStatus": bqlGT128LEDNZStatus}
)
