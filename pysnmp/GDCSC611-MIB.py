# SNMP MIB module (GDCSC611-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCSC611-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:19 2024
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
_Bql2_ObjectIdentity = ObjectIdentity
bql2 = _Bql2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12)
)
_Bql611_ObjectIdentity = ObjectIdentity
bql611 = _Bql611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 2)
)


class _Bql611MIBVersion_Type(DisplayString):
    """Custom type bql611MIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Bql611MIBVersion_Type.__name__ = "DisplayString"
_Bql611MIBVersion_Object = MibScalar
bql611MIBVersion = _Bql611MIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 1),
    _Bql611MIBVersion_Type()
)
bql611MIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611MIBVersion.setStatus("mandatory")
_Bql611WhatAreYouTable_Object = MibTable
bql611WhatAreYouTable = _Bql611WhatAreYouTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2)
)
if mibBuilder.loadTexts:
    bql611WhatAreYouTable.setStatus("mandatory")
_Bql611WhatAreYouEntry_Object = MibTableRow
bql611WhatAreYouEntry = _Bql611WhatAreYouEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1)
)
bql611WhatAreYouEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611WhatAreYouIndex"),
)
if mibBuilder.loadTexts:
    bql611WhatAreYouEntry.setStatus("mandatory")
_Bql611WhatAreYouIndex_Type = SCinstance
_Bql611WhatAreYouIndex_Object = MibTableColumn
bql611WhatAreYouIndex = _Bql611WhatAreYouIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1, 1),
    _Bql611WhatAreYouIndex_Type()
)
bql611WhatAreYouIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611WhatAreYouIndex.setStatus("mandatory")


class _Bql611BaseCardType_Type(Integer32):
    """Custom type bql611BaseCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dc621", 7),
          ("sc611", 5))
    )


_Bql611BaseCardType_Type.__name__ = "Integer32"
_Bql611BaseCardType_Object = MibTableColumn
bql611BaseCardType = _Bql611BaseCardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1, 2),
    _Bql611BaseCardType_Type()
)
bql611BaseCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611BaseCardType.setStatus("mandatory")


class _Bql611OptionCard_Type(Integer32):
    """Custom type bql611OptionCard based on Integer32"""
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


_Bql611OptionCard_Type.__name__ = "Integer32"
_Bql611OptionCard_Object = MibTableColumn
bql611OptionCard = _Bql611OptionCard_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1, 3),
    _Bql611OptionCard_Type()
)
bql611OptionCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611OptionCard.setStatus("mandatory")


class _Bql611DTECardType_Type(Integer32):
    """Custom type bql611DTECardType based on Integer32"""
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


_Bql611DTECardType_Type.__name__ = "Integer32"
_Bql611DTECardType_Object = MibTableColumn
bql611DTECardType = _Bql611DTECardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1, 4),
    _Bql611DTECardType_Type()
)
bql611DTECardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611DTECardType.setStatus("mandatory")


class _Bql611CodeRev_Type(DisplayString):
    """Custom type bql611CodeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Bql611CodeRev_Type.__name__ = "DisplayString"
_Bql611CodeRev_Object = MibTableColumn
bql611CodeRev = _Bql611CodeRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1, 5),
    _Bql611CodeRev_Type()
)
bql611CodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611CodeRev.setStatus("mandatory")


class _Bql611AlarmStatus_Type(OctetString):
    """Custom type bql611AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Bql611AlarmStatus_Type.__name__ = "OctetString"
_Bql611AlarmStatus_Object = MibTableColumn
bql611AlarmStatus = _Bql611AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 2, 1, 6),
    _Bql611AlarmStatus_Type()
)
bql611AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611AlarmStatus.setStatus("mandatory")
_Bql611ConfigTable_Object = MibTable
bql611ConfigTable = _Bql611ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3)
)
if mibBuilder.loadTexts:
    bql611ConfigTable.setStatus("mandatory")
_Bql611ConfigEntry_Object = MibTableRow
bql611ConfigEntry = _Bql611ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1)
)
bql611ConfigEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611ConfigIndex"),
)
if mibBuilder.loadTexts:
    bql611ConfigEntry.setStatus("mandatory")
_Bql611ConfigIndex_Type = SCinstance
_Bql611ConfigIndex_Object = MibTableColumn
bql611ConfigIndex = _Bql611ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 1),
    _Bql611ConfigIndex_Type()
)
bql611ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611ConfigIndex.setStatus("mandatory")


class _Bql611DteRate_Type(Integer32):
    """Custom type bql611DteRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("kBps128", 10),
          ("kBps19Dot2", 4),
          ("kBps2Dot4", 1),
          ("kBps48", 6),
          ("kBps4Dot8", 2),
          ("kBps64", 9),
          ("kBps9Dot6", 3))
    )


_Bql611DteRate_Type.__name__ = "Integer32"
_Bql611DteRate_Object = MibTableColumn
bql611DteRate = _Bql611DteRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 2),
    _Bql611DteRate_Type()
)
bql611DteRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611DteRate.setStatus("mandatory")


class _Bql611RateAdaption_Type(Integer32):
    """Custom type bql611RateAdaption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x50Div2", 2),
          ("x50Div3", 1))
    )


_Bql611RateAdaption_Type.__name__ = "Integer32"
_Bql611RateAdaption_Object = MibTableColumn
bql611RateAdaption = _Bql611RateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 3),
    _Bql611RateAdaption_Type()
)
bql611RateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611RateAdaption.setStatus("mandatory")


class _Bql611DteOperation_Type(Integer32):
    """Custom type bql611DteOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1))
    )


_Bql611DteOperation_Type.__name__ = "Integer32"
_Bql611DteOperation_Object = MibTableColumn
bql611DteOperation = _Bql611DteOperation_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 4),
    _Bql611DteOperation_Type()
)
bql611DteOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611DteOperation.setStatus("mandatory")


class _Bql611TxClkSource_Type(Integer32):
    """Custom type bql611TxClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_Bql611TxClkSource_Type.__name__ = "Integer32"
_Bql611TxClkSource_Object = MibTableColumn
bql611TxClkSource = _Bql611TxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 5),
    _Bql611TxClkSource_Type()
)
bql611TxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611TxClkSource.setStatus("mandatory")


class _Bql611WordLength_Type(Integer32):
    """Custom type bql611WordLength based on Integer32"""
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
        *(("bitWord10", 3),
          ("bitWord11", 4),
          ("bitWord8", 1),
          ("bitWord9", 2))
    )


_Bql611WordLength_Type.__name__ = "Integer32"
_Bql611WordLength_Object = MibTableColumn
bql611WordLength = _Bql611WordLength_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 6),
    _Bql611WordLength_Type()
)
bql611WordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611WordLength.setStatus("mandatory")


class _Bql611OverSpeed_Type(Integer32):
    """Custom type bql611OverSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePercent", 1),
          ("twoPointThreePercent", 2))
    )


_Bql611OverSpeed_Type.__name__ = "Integer32"
_Bql611OverSpeed_Object = MibTableColumn
bql611OverSpeed = _Bql611OverSpeed_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 7),
    _Bql611OverSpeed_Type()
)
bql611OverSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611OverSpeed.setStatus("mandatory")


class _Bql611RTS_Type(Integer32):
    """Custom type bql611RTS based on Integer32"""
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


_Bql611RTS_Type.__name__ = "Integer32"
_Bql611RTS_Object = MibTableColumn
bql611RTS = _Bql611RTS_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 8),
    _Bql611RTS_Type()
)
bql611RTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611RTS.setStatus("mandatory")


class _Bql611RTSCTSDelay_Type(Integer32):
    """Custom type bql611RTSCTSDelay based on Integer32"""
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


_Bql611RTSCTSDelay_Type.__name__ = "Integer32"
_Bql611RTSCTSDelay_Object = MibTableColumn
bql611RTSCTSDelay = _Bql611RTSCTSDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 9),
    _Bql611RTSCTSDelay_Type()
)
bql611RTSCTSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611RTSCTSDelay.setStatus("mandatory")


class _Bql611DCD_Type(Integer32):
    """Custom type bql611DCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inBandRTS", 2),
          ("normal", 1))
    )


_Bql611DCD_Type.__name__ = "Integer32"
_Bql611DCD_Object = MibTableColumn
bql611DCD = _Bql611DCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 10),
    _Bql611DCD_Type()
)
bql611DCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611DCD.setStatus("mandatory")


class _Bql611RDL_Type(Integer32):
    """Custom type bql611RDL based on Integer32"""
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


_Bql611RDL_Type.__name__ = "Integer32"
_Bql611RDL_Object = MibTableColumn
bql611RDL = _Bql611RDL_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 11),
    _Bql611RDL_Type()
)
bql611RDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611RDL.setStatus("mandatory")


class _Bql611RDLMethod_Type(Integer32):
    """Custom type bql611RDLMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eocorpn127", 2),
          ("v54", 1))
    )


_Bql611RDLMethod_Type.__name__ = "Integer32"
_Bql611RDLMethod_Object = MibTableColumn
bql611RDLMethod = _Bql611RDLMethod_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 12),
    _Bql611RDLMethod_Type()
)
bql611RDLMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611RDLMethod.setStatus("mandatory")


class _Bql611RDLTimeout_Type(Integer32):
    """Custom type bql611RDLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minutes10", 2),
          ("none", 1))
    )


_Bql611RDLTimeout_Type.__name__ = "Integer32"
_Bql611RDLTimeout_Object = MibTableColumn
bql611RDLTimeout = _Bql611RDLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 13),
    _Bql611RDLTimeout_Type()
)
bql611RDLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611RDLTimeout.setStatus("mandatory")


class _Bql611TestPattern_Type(Integer32):
    """Custom type bql611TestPattern based on Integer32"""
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


_Bql611TestPattern_Type.__name__ = "Integer32"
_Bql611TestPattern_Object = MibTableColumn
bql611TestPattern = _Bql611TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 3, 1, 14),
    _Bql611TestPattern_Type()
)
bql611TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611TestPattern.setStatus("mandatory")
_Bql611DiagnosticTable_Object = MibTable
bql611DiagnosticTable = _Bql611DiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4)
)
if mibBuilder.loadTexts:
    bql611DiagnosticTable.setStatus("mandatory")
_Bql611DiagnosticEntry_Object = MibTableRow
bql611DiagnosticEntry = _Bql611DiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4, 1)
)
bql611DiagnosticEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611DiagnosticIndex"),
)
if mibBuilder.loadTexts:
    bql611DiagnosticEntry.setStatus("mandatory")
_Bql611DiagnosticIndex_Type = SCinstance
_Bql611DiagnosticIndex_Object = MibTableColumn
bql611DiagnosticIndex = _Bql611DiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4, 1, 1),
    _Bql611DiagnosticIndex_Type()
)
bql611DiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611DiagnosticIndex.setStatus("mandatory")


class _Bql611DiagnosticTest_Type(Integer32):
    """Custom type bql611DiagnosticTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Bql611DiagnosticTest_Type.__name__ = "Integer32"
_Bql611DiagnosticTest_Object = MibTableColumn
bql611DiagnosticTest = _Bql611DiagnosticTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4, 1, 2),
    _Bql611DiagnosticTest_Type()
)
bql611DiagnosticTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611DiagnosticTest.setStatus("mandatory")


class _Bql611DiagnosticActive_Type(Integer32):
    """Custom type bql611DiagnosticActive based on Integer32"""
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


_Bql611DiagnosticActive_Type.__name__ = "Integer32"
_Bql611DiagnosticActive_Object = MibTableColumn
bql611DiagnosticActive = _Bql611DiagnosticActive_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4, 1, 3),
    _Bql611DiagnosticActive_Type()
)
bql611DiagnosticActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611DiagnosticActive.setStatus("mandatory")


class _Bql611DiagnosticResults_Type(Integer32):
    """Custom type bql611DiagnosticResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Bql611DiagnosticResults_Type.__name__ = "Integer32"
_Bql611DiagnosticResults_Object = MibTableColumn
bql611DiagnosticResults = _Bql611DiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4, 1, 4),
    _Bql611DiagnosticResults_Type()
)
bql611DiagnosticResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611DiagnosticResults.setStatus("mandatory")


class _Bql611DiagnosticResetErrorCount_Type(Integer32):
    """Custom type bql611DiagnosticResetErrorCount based on Integer32"""
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


_Bql611DiagnosticResetErrorCount_Type.__name__ = "Integer32"
_Bql611DiagnosticResetErrorCount_Object = MibTableColumn
bql611DiagnosticResetErrorCount = _Bql611DiagnosticResetErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 4, 1, 5),
    _Bql611DiagnosticResetErrorCount_Type()
)
bql611DiagnosticResetErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611DiagnosticResetErrorCount.setStatus("mandatory")
_Bql611ControlTable_Object = MibTable
bql611ControlTable = _Bql611ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5)
)
if mibBuilder.loadTexts:
    bql611ControlTable.setStatus("mandatory")
_Bql611ControlEntry_Object = MibTableRow
bql611ControlEntry = _Bql611ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1)
)
bql611ControlEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611ControlIndex"),
)
if mibBuilder.loadTexts:
    bql611ControlEntry.setStatus("mandatory")
_Bql611ControlIndex_Type = SCinstance
_Bql611ControlIndex_Object = MibTableColumn
bql611ControlIndex = _Bql611ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1, 1),
    _Bql611ControlIndex_Type()
)
bql611ControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611ControlIndex.setStatus("mandatory")


class _Bql611SoftReset_Type(Integer32):
    """Custom type bql611SoftReset based on Integer32"""
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


_Bql611SoftReset_Type.__name__ = "Integer32"
_Bql611SoftReset_Object = MibTableColumn
bql611SoftReset = _Bql611SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1, 2),
    _Bql611SoftReset_Type()
)
bql611SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611SoftReset.setStatus("mandatory")


class _Bql611EraseConfig_Type(Integer32):
    """Custom type bql611EraseConfig based on Integer32"""
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


_Bql611EraseConfig_Type.__name__ = "Integer32"
_Bql611EraseConfig_Object = MibTableColumn
bql611EraseConfig = _Bql611EraseConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1, 3),
    _Bql611EraseConfig_Type()
)
bql611EraseConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611EraseConfig.setStatus("mandatory")


class _Bql611FrontPanel_Type(Integer32):
    """Custom type bql611FrontPanel based on Integer32"""
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


_Bql611FrontPanel_Type.__name__ = "Integer32"
_Bql611FrontPanel_Object = MibTableColumn
bql611FrontPanel = _Bql611FrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1, 4),
    _Bql611FrontPanel_Type()
)
bql611FrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611FrontPanel.setStatus("mandatory")


class _Bql611LEDStatus_Type(OctetString):
    """Custom type bql611LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Bql611LEDStatus_Type.__name__ = "OctetString"
_Bql611LEDStatus_Object = MibTableColumn
bql611LEDStatus = _Bql611LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1, 5),
    _Bql611LEDStatus_Type()
)
bql611LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611LEDStatus.setStatus("mandatory")


class _Bql621LEDStatus_Type(OctetString):
    """Custom type bql621LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Bql621LEDStatus_Type.__name__ = "OctetString"
_Bql621LEDStatus_Object = MibTableColumn
bql621LEDStatus = _Bql621LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 5, 1, 6),
    _Bql621LEDStatus_Type()
)
bql621LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql621LEDStatus.setStatus("mandatory")
_Bql611CurrentTable_Object = MibTable
bql611CurrentTable = _Bql611CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 6)
)
if mibBuilder.loadTexts:
    bql611CurrentTable.setStatus("mandatory")
_Bql611CurrentEntry_Object = MibTableRow
bql611CurrentEntry = _Bql611CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 6, 1)
)
bql611CurrentEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611CurrentIndex"),
)
if mibBuilder.loadTexts:
    bql611CurrentEntry.setStatus("mandatory")
_Bql611CurrentIndex_Type = SCinstance
_Bql611CurrentIndex_Object = MibTableColumn
bql611CurrentIndex = _Bql611CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 6, 1, 1),
    _Bql611CurrentIndex_Type()
)
bql611CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611CurrentIndex.setStatus("mandatory")


class _Bql611CurrentStats_Type(OctetString):
    """Custom type bql611CurrentStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Bql611CurrentStats_Type.__name__ = "OctetString"
_Bql611CurrentStats_Object = MibTableColumn
bql611CurrentStats = _Bql611CurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 6, 1, 2),
    _Bql611CurrentStats_Type()
)
bql611CurrentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611CurrentStats.setStatus("mandatory")
_Bql611IntervalTable_Object = MibTable
bql611IntervalTable = _Bql611IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 8)
)
if mibBuilder.loadTexts:
    bql611IntervalTable.setStatus("mandatory")
_Bql611IntervalEntry_Object = MibTableRow
bql611IntervalEntry = _Bql611IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 8, 1)
)
bql611IntervalEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611IntervalIndex"),
    (0, "GDCSC611-MIB", "bql611IntervalNumber"),
)
if mibBuilder.loadTexts:
    bql611IntervalEntry.setStatus("mandatory")
_Bql611IntervalIndex_Type = SCinstance
_Bql611IntervalIndex_Object = MibTableColumn
bql611IntervalIndex = _Bql611IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 8, 1, 1),
    _Bql611IntervalIndex_Type()
)
bql611IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611IntervalIndex.setStatus("mandatory")


class _Bql611IntervalNumber_Type(Integer32):
    """Custom type bql611IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Bql611IntervalNumber_Type.__name__ = "Integer32"
_Bql611IntervalNumber_Object = MibTableColumn
bql611IntervalNumber = _Bql611IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 8, 1, 2),
    _Bql611IntervalNumber_Type()
)
bql611IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611IntervalNumber.setStatus("mandatory")


class _Bql611IntervalStats_Type(OctetString):
    """Custom type bql611IntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Bql611IntervalStats_Type.__name__ = "OctetString"
_Bql611IntervalStats_Object = MibTableColumn
bql611IntervalStats = _Bql611IntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 8, 1, 3),
    _Bql611IntervalStats_Type()
)
bql611IntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611IntervalStats.setStatus("mandatory")
_Bql611TotalTable_Object = MibTable
bql611TotalTable = _Bql611TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 9)
)
if mibBuilder.loadTexts:
    bql611TotalTable.setStatus("mandatory")
_Bql611TotalEntry_Object = MibTableRow
bql611TotalEntry = _Bql611TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 9, 1)
)
bql611TotalEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611TotalIndex"),
)
if mibBuilder.loadTexts:
    bql611TotalEntry.setStatus("mandatory")
_Bql611TotalIndex_Type = SCinstance
_Bql611TotalIndex_Object = MibTableColumn
bql611TotalIndex = _Bql611TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 9, 1, 1),
    _Bql611TotalIndex_Type()
)
bql611TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611TotalIndex.setStatus("mandatory")


class _Bql611TotalStats_Type(OctetString):
    """Custom type bql611TotalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Bql611TotalStats_Type.__name__ = "OctetString"
_Bql611TotalStats_Object = MibTableColumn
bql611TotalStats = _Bql611TotalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 9, 1, 2),
    _Bql611TotalStats_Type()
)
bql611TotalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611TotalStats.setStatus("mandatory")
_Bql611IntervalMaintenanceTable_Object = MibTable
bql611IntervalMaintenanceTable = _Bql611IntervalMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10)
)
if mibBuilder.loadTexts:
    bql611IntervalMaintenanceTable.setStatus("mandatory")
_Bql611IntervalMaintenanceEntry_Object = MibTableRow
bql611IntervalMaintenanceEntry = _Bql611IntervalMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10, 1)
)
bql611IntervalMaintenanceEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611IntervalMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    bql611IntervalMaintenanceEntry.setStatus("mandatory")
_Bql611IntervalMaintenanceIndex_Type = SCinstance
_Bql611IntervalMaintenanceIndex_Object = MibTableColumn
bql611IntervalMaintenanceIndex = _Bql611IntervalMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10, 1, 1),
    _Bql611IntervalMaintenanceIndex_Type()
)
bql611IntervalMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611IntervalMaintenanceIndex.setStatus("mandatory")


class _Bql611ResetIntervals_Type(Integer32):
    """Custom type bql611ResetIntervals based on Integer32"""
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


_Bql611ResetIntervals_Type.__name__ = "Integer32"
_Bql611ResetIntervals_Object = MibTableColumn
bql611ResetIntervals = _Bql611ResetIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10, 1, 2),
    _Bql611ResetIntervals_Type()
)
bql611ResetIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611ResetIntervals.setStatus("mandatory")


class _Bql611NumberofValidIntervals_Type(Integer32):
    """Custom type bql611NumberofValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Bql611NumberofValidIntervals_Type.__name__ = "Integer32"
_Bql611NumberofValidIntervals_Object = MibTableColumn
bql611NumberofValidIntervals = _Bql611NumberofValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10, 1, 3),
    _Bql611NumberofValidIntervals_Type()
)
bql611NumberofValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611NumberofValidIntervals.setStatus("mandatory")


class _Bql611ResetMajorAlarm_Type(Integer32):
    """Custom type bql611ResetMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 2),
          ("reset", 1))
    )


_Bql611ResetMajorAlarm_Type.__name__ = "Integer32"
_Bql611ResetMajorAlarm_Object = MibTableColumn
bql611ResetMajorAlarm = _Bql611ResetMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10, 1, 4),
    _Bql611ResetMajorAlarm_Type()
)
bql611ResetMajorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611ResetMajorAlarm.setStatus("mandatory")


class _Bql611ResetMinorAlarm_Type(Integer32):
    """Custom type bql611ResetMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 2),
          ("reset", 1))
    )


_Bql611ResetMinorAlarm_Type.__name__ = "Integer32"
_Bql611ResetMinorAlarm_Object = MibTableColumn
bql611ResetMinorAlarm = _Bql611ResetMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 2, 10, 1, 5),
    _Bql611ResetMinorAlarm_Type()
)
bql611ResetMinorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611ResetMinorAlarm.setStatus("mandatory")
_Bql621_ObjectIdentity = ObjectIdentity
bql621 = _Bql621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 3)
)
_Bql611Alarm_ObjectIdentity = ObjectIdentity
bql611Alarm = _Bql611Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9)
)
_Bql611AlarmData_ObjectIdentity = ObjectIdentity
bql611AlarmData = _Bql611AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1)
)
_Bql611NoResponseAlm_ObjectIdentity = ObjectIdentity
bql611NoResponseAlm = _Bql611NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 1)
)
_Bql611DiagRxErrAlm_ObjectIdentity = ObjectIdentity
bql611DiagRxErrAlm = _Bql611DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 2)
)
_Bql611PowerUpAlm_ObjectIdentity = ObjectIdentity
bql611PowerUpAlm = _Bql611PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 3)
)
_Bql611OutofSyncAlm_ObjectIdentity = ObjectIdentity
bql611OutofSyncAlm = _Bql611OutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 4)
)
_Bql611TxClkOutOfToleranceAlm_ObjectIdentity = ObjectIdentity
bql611TxClkOutOfToleranceAlm = _Bql611TxClkOutOfToleranceAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 5)
)
_Bql611ExtClkAbsentAlm_ObjectIdentity = ObjectIdentity
bql611ExtClkAbsentAlm = _Bql611ExtClkAbsentAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 6)
)
_Bql611SealingCurrentNoContinuityAlm_ObjectIdentity = ObjectIdentity
bql611SealingCurrentNoContinuityAlm = _Bql611SealingCurrentNoContinuityAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 7)
)
_Bql611DtrNotPresentAlm_ObjectIdentity = ObjectIdentity
bql611DtrNotPresentAlm = _Bql611DtrNotPresentAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 8)
)
_Bql611MajorAlarmBERAlm_ObjectIdentity = ObjectIdentity
bql611MajorAlarmBERAlm = _Bql611MajorAlarmBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 9)
)
_Bql611MinorAlarmBERAlm_ObjectIdentity = ObjectIdentity
bql611MinorAlarmBERAlm = _Bql611MinorAlarmBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 1, 10)
)
_Bql611AlarmConfigTable_Object = MibTable
bql611AlarmConfigTable = _Bql611AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 2)
)
if mibBuilder.loadTexts:
    bql611AlarmConfigTable.setStatus("mandatory")
_Bql611AlarmConfigEntry_Object = MibTableRow
bql611AlarmConfigEntry = _Bql611AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 2, 1)
)
bql611AlarmConfigEntry.setIndexNames(
    (0, "GDCSC611-MIB", "bql611AlarmConfigIndex"),
    (0, "GDCSC611-MIB", "bql611AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    bql611AlarmConfigEntry.setStatus("mandatory")
_Bql611AlarmConfigIndex_Type = SCinstance
_Bql611AlarmConfigIndex_Object = MibTableColumn
bql611AlarmConfigIndex = _Bql611AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 2, 1, 1),
    _Bql611AlarmConfigIndex_Type()
)
bql611AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611AlarmConfigIndex.setStatus("mandatory")
_Bql611AlarmConfigIdentifier_Type = ObjectIdentifier
_Bql611AlarmConfigIdentifier_Object = MibTableColumn
bql611AlarmConfigIdentifier = _Bql611AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 2, 1, 2),
    _Bql611AlarmConfigIdentifier_Type()
)
bql611AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql611AlarmConfigIdentifier.setStatus("mandatory")


class _Bql611AlarmThreshold_Type(Integer32):
    """Custom type bql611AlarmThreshold based on Integer32"""
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
        *(("thres10E03", 1),
          ("thres10E04", 2),
          ("thres10E05", 3),
          ("thres10E06", 4))
    )


_Bql611AlarmThreshold_Type.__name__ = "Integer32"
_Bql611AlarmThreshold_Object = MibTableColumn
bql611AlarmThreshold = _Bql611AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 9, 2, 1, 3),
    _Bql611AlarmThreshold_Type()
)
bql611AlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql611AlarmThreshold.setStatus("mandatory")
_Bql621Alarm_ObjectIdentity = ObjectIdentity
bql621Alarm = _Bql621Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11)
)
_Bql621AlarmData_ObjectIdentity = ObjectIdentity
bql621AlarmData = _Bql621AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1)
)
_Bql621NoResponseAlm_ObjectIdentity = ObjectIdentity
bql621NoResponseAlm = _Bql621NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1, 1)
)
_Bql621DiagRxErrAlm_ObjectIdentity = ObjectIdentity
bql621DiagRxErrAlm = _Bql621DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1, 2)
)
_Bql621PowerUpAlm_ObjectIdentity = ObjectIdentity
bql621PowerUpAlm = _Bql621PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1, 3)
)
_Bql621DtrNotPresentAlm_ObjectIdentity = ObjectIdentity
bql621DtrNotPresentAlm = _Bql621DtrNotPresentAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1, 4)
)
_Bql621MajorAlarmBERAlm_ObjectIdentity = ObjectIdentity
bql621MajorAlarmBERAlm = _Bql621MajorAlarmBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1, 5)
)
_Bql621MinorAlarmBERAlm_ObjectIdentity = ObjectIdentity
bql621MinorAlarmBERAlm = _Bql621MinorAlarmBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 11, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCSC611-MIB",
    **{"gdc": gdc,
       "bql2": bql2,
       "bql611": bql611,
       "bql611MIBVersion": bql611MIBVersion,
       "bql611WhatAreYouTable": bql611WhatAreYouTable,
       "bql611WhatAreYouEntry": bql611WhatAreYouEntry,
       "bql611WhatAreYouIndex": bql611WhatAreYouIndex,
       "bql611BaseCardType": bql611BaseCardType,
       "bql611OptionCard": bql611OptionCard,
       "bql611DTECardType": bql611DTECardType,
       "bql611CodeRev": bql611CodeRev,
       "bql611AlarmStatus": bql611AlarmStatus,
       "bql611ConfigTable": bql611ConfigTable,
       "bql611ConfigEntry": bql611ConfigEntry,
       "bql611ConfigIndex": bql611ConfigIndex,
       "bql611DteRate": bql611DteRate,
       "bql611RateAdaption": bql611RateAdaption,
       "bql611DteOperation": bql611DteOperation,
       "bql611TxClkSource": bql611TxClkSource,
       "bql611WordLength": bql611WordLength,
       "bql611OverSpeed": bql611OverSpeed,
       "bql611RTS": bql611RTS,
       "bql611RTSCTSDelay": bql611RTSCTSDelay,
       "bql611DCD": bql611DCD,
       "bql611RDL": bql611RDL,
       "bql611RDLMethod": bql611RDLMethod,
       "bql611RDLTimeout": bql611RDLTimeout,
       "bql611TestPattern": bql611TestPattern,
       "bql611DiagnosticTable": bql611DiagnosticTable,
       "bql611DiagnosticEntry": bql611DiagnosticEntry,
       "bql611DiagnosticIndex": bql611DiagnosticIndex,
       "bql611DiagnosticTest": bql611DiagnosticTest,
       "bql611DiagnosticActive": bql611DiagnosticActive,
       "bql611DiagnosticResults": bql611DiagnosticResults,
       "bql611DiagnosticResetErrorCount": bql611DiagnosticResetErrorCount,
       "bql611ControlTable": bql611ControlTable,
       "bql611ControlEntry": bql611ControlEntry,
       "bql611ControlIndex": bql611ControlIndex,
       "bql611SoftReset": bql611SoftReset,
       "bql611EraseConfig": bql611EraseConfig,
       "bql611FrontPanel": bql611FrontPanel,
       "bql611LEDStatus": bql611LEDStatus,
       "bql621LEDStatus": bql621LEDStatus,
       "bql611CurrentTable": bql611CurrentTable,
       "bql611CurrentEntry": bql611CurrentEntry,
       "bql611CurrentIndex": bql611CurrentIndex,
       "bql611CurrentStats": bql611CurrentStats,
       "bql611IntervalTable": bql611IntervalTable,
       "bql611IntervalEntry": bql611IntervalEntry,
       "bql611IntervalIndex": bql611IntervalIndex,
       "bql611IntervalNumber": bql611IntervalNumber,
       "bql611IntervalStats": bql611IntervalStats,
       "bql611TotalTable": bql611TotalTable,
       "bql611TotalEntry": bql611TotalEntry,
       "bql611TotalIndex": bql611TotalIndex,
       "bql611TotalStats": bql611TotalStats,
       "bql611IntervalMaintenanceTable": bql611IntervalMaintenanceTable,
       "bql611IntervalMaintenanceEntry": bql611IntervalMaintenanceEntry,
       "bql611IntervalMaintenanceIndex": bql611IntervalMaintenanceIndex,
       "bql611ResetIntervals": bql611ResetIntervals,
       "bql611NumberofValidIntervals": bql611NumberofValidIntervals,
       "bql611ResetMajorAlarm": bql611ResetMajorAlarm,
       "bql611ResetMinorAlarm": bql611ResetMinorAlarm,
       "bql621": bql621,
       "bql611Alarm": bql611Alarm,
       "bql611AlarmData": bql611AlarmData,
       "bql611NoResponseAlm": bql611NoResponseAlm,
       "bql611DiagRxErrAlm": bql611DiagRxErrAlm,
       "bql611PowerUpAlm": bql611PowerUpAlm,
       "bql611OutofSyncAlm": bql611OutofSyncAlm,
       "bql611TxClkOutOfToleranceAlm": bql611TxClkOutOfToleranceAlm,
       "bql611ExtClkAbsentAlm": bql611ExtClkAbsentAlm,
       "bql611SealingCurrentNoContinuityAlm": bql611SealingCurrentNoContinuityAlm,
       "bql611DtrNotPresentAlm": bql611DtrNotPresentAlm,
       "bql611MajorAlarmBERAlm": bql611MajorAlarmBERAlm,
       "bql611MinorAlarmBERAlm": bql611MinorAlarmBERAlm,
       "bql611AlarmConfigTable": bql611AlarmConfigTable,
       "bql611AlarmConfigEntry": bql611AlarmConfigEntry,
       "bql611AlarmConfigIndex": bql611AlarmConfigIndex,
       "bql611AlarmConfigIdentifier": bql611AlarmConfigIdentifier,
       "bql611AlarmThreshold": bql611AlarmThreshold,
       "bql621Alarm": bql621Alarm,
       "bql621AlarmData": bql621AlarmData,
       "bql621NoResponseAlm": bql621NoResponseAlm,
       "bql621DiagRxErrAlm": bql621DiagRxErrAlm,
       "bql621PowerUpAlm": bql621PowerUpAlm,
       "bql621DtrNotPresentAlm": bql621DtrNotPresentAlm,
       "bql621MajorAlarmBERAlm": bql621MajorAlarmBERAlm,
       "bql621MinorAlarmBERAlm": bql621MinorAlarmBERAlm}
)
