# SNMP MIB module (CISCO-WAN-FR-X21-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FR-X21-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:06 2024
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

(frPortCnfX21PortGrp,
 x21) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "frPortCnfX21PortGrp",
    "x21")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanFrX21MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 49)
)
ciscoWanFrX21MIB.setRevisions(
        ("2002-09-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_X21CnfGrp_ObjectIdentity = ObjectIdentity
x21CnfGrp = _X21CnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1)
)
_X21CnfGrpTable_Object = MibTable
x21CnfGrpTable = _X21CnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    x21CnfGrpTable.setStatus("current")
_X21CnfGrpEntry_Object = MibTableRow
x21CnfGrpEntry = _X21CnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1)
)
x21CnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-X21-MIB", "x21LineNum"),
)
if mibBuilder.loadTexts:
    x21CnfGrpEntry.setStatus("current")


class _X21LineNum_Type(Integer32):
    """Custom type x21LineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_X21LineNum_Type.__name__ = "Integer32"
_X21LineNum_Object = MibTableColumn
x21LineNum = _X21LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 1),
    _X21LineNum_Type()
)
x21LineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LineNum.setStatus("current")


class _X21LineEnable_Type(Integer32):
    """Custom type x21LineEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("modify", 3))
    )


_X21LineEnable_Type.__name__ = "Integer32"
_X21LineEnable_Object = MibTableColumn
x21LineEnable = _X21LineEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 2),
    _X21LineEnable_Type()
)
x21LineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineEnable.setStatus("current")


class _X21LineType_Type(Integer32):
    """Custom type x21LineType based on Integer32"""
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
          ("dteST", 3))
    )


_X21LineType_Type.__name__ = "Integer32"
_X21LineType_Object = MibTableColumn
x21LineType = _X21LineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 3),
    _X21LineType_Type()
)
x21LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineType.setStatus("current")


class _X21LineRate_Type(Integer32):
    """Custom type x21LineRate based on Integer32"""
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
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("r10240Kbps", 37),
          ("r1024Kbps", 18),
          ("r10808Kbps", 61),
          ("r10890Kbps", 38),
          ("r11060Kbps", 39),
          ("r112Kbps", 4),
          ("r12288Kbps", 89),
          ("r12352Kbps", 62),
          ("r12390Kbps", 40),
          ("r12630Kbps", 41),
          ("r128Kbps", 5),
          ("r13896Kbps", 63),
          ("r13900Kbps", 42),
          ("r14220Kbps", 43),
          ("r14336Kbps", 90),
          ("r14340Kbps", 44),
          ("r1536Kbps", 19),
          ("r15440Kbps", 64),
          ("r1544Kbps", 20),
          ("r15490Kbps", 45),
          ("r15800Kbps", 46),
          ("r16380Kbps", 47),
          ("r16384Kbps", 91),
          ("r168Kbps", 6),
          ("r16984Kbps", 65),
          ("r17370Kbps", 51),
          ("r1792Kbps", 21),
          ("r18432Kbps", 92),
          ("r18528Kbps", 66),
          ("r18950Kbps", 52),
          ("r1920Kbps", 22),
          ("r192Kbps", 7),
          ("r1984Kbps", 23),
          ("r20030Kbps", 48),
          ("r20072Kbps", 67),
          ("r20480Kbps", 93),
          ("r2048Kbps", 24),
          ("r20530Kbps", 53),
          ("r21616Kbps", 68),
          ("r22100Kbps", 54),
          ("r224Kbps", 8),
          ("r22528Kbps", 94),
          ("r23160Kbps", 69),
          ("r23680Kbps", 55),
          ("r24576Kbps", 95),
          ("r24704Kbps", 70),
          ("r24990Kbps", 49),
          ("r256Kbps", 9),
          ("r26248Kbps", 71),
          ("r26624Kbps", 96),
          ("r27792Kbps", 72),
          ("r280Kbps", 10),
          ("r28672Kbps", 97),
          ("r29336Kbps", 73),
          ("r30720Kbps", 98),
          ("r30880Kbps", 74),
          ("r3088Kbps", 56),
          ("r3097Kbps", 25),
          ("r3157Kbps", 26),
          ("r320Kbps", 11),
          ("r32424Kbps", 75),
          ("r32768Kbps", 99),
          ("r336Kbps", 12),
          ("r33968Kbps", 76),
          ("r34816Kbps", 100),
          ("r35512Kbps", 77),
          ("r36864Kbps", 101),
          ("r37056Kbps", 78),
          ("r384Kbps", 13),
          ("r38600Kbps", 79),
          ("r38912Kbps", 102),
          ("r392Kbps", 14),
          ("r40144Kbps", 80),
          ("r40960Kbps", 103),
          ("r4096Kbps", 27),
          ("r41688Kbps", 81),
          ("r43008Kbps", 104),
          ("r43232Kbps", 82),
          ("r44776Kbps", 83),
          ("r448Kbps", 15),
          ("r45056Kbps", 105),
          ("r46320Kbps", 84),
          ("r4632Kbps", 57),
          ("r4645Kbps", 28),
          ("r47104Kbps", 106),
          ("r4736Kbps", 29),
          ("r47864Kbps", 85),
          ("r48Kbps", 1),
          ("r49152Kbps", 107),
          ("r49408Kbps", 86),
          ("r50952Kbps", 87),
          ("r51200Kbps", 108),
          ("r512Kbps", 16),
          ("r52Mbps", 50),
          ("r56Kbps", 2),
          ("r6144Kbps", 88),
          ("r6176Kbps", 58),
          ("r6195Kbps", 30),
          ("r6315Kbps", 31),
          ("r64Kbps", 3),
          ("r768Kbps", 17),
          ("r7720Kbps", 59),
          ("r7744Kbps", 32),
          ("r7899Kbps", 33),
          ("r8192Kbps", 34),
          ("r9264Kbps", 60),
          ("r9289Kbps", 35),
          ("r9472Kbps", 36))
    )


_X21LineRate_Type.__name__ = "Integer32"
_X21LineRate_Object = MibTableColumn
x21LineRate = _X21LineRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 4),
    _X21LineRate_Type()
)
x21LineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineRate.setStatus("current")


class _X21LineLoopbackCommand_Type(Integer32):
    """Custom type x21LineLoopbackCommand based on Integer32"""
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
        *(("v35MetallicLoop", 5),
          ("x21DiagnosticFrontcardLoop", 3),
          ("x21DiagnosticMetallicLoop", 2),
          ("x21NoLoop", 1),
          ("x21RemoteLoop", 4))
    )


_X21LineLoopbackCommand_Type.__name__ = "Integer32"
_X21LineLoopbackCommand_Object = MibTableColumn
x21LineLoopbackCommand = _X21LineLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 5),
    _X21LineLoopbackCommand_Type()
)
x21LineLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineLoopbackCommand.setStatus("current")


class _X21LineSendCode_Type(Integer32):
    """Custom type x21LineSendCode based on Integer32"""
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
        *(("x21NoCode", 1),
          ("x21SendLocalLoopCode", 4),
          ("x21SendLoopACode", 2),
          ("x21SendLoopBCode", 3),
          ("x21SendRemoteLoopCode", 5),
          ("x21SendUnLoopCode", 6))
    )


_X21LineSendCode_Type.__name__ = "Integer32"
_X21LineSendCode_Object = MibTableColumn
x21LineSendCode = _X21LineSendCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 6),
    _X21LineSendCode_Type()
)
x21LineSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineSendCode.setStatus("current")


class _X21LineLoopbackCodeDetection_Type(Integer32):
    """Custom type x21LineLoopbackCodeDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("codeDetectDisabled", 1),
          ("codeDetectEnabled", 2))
    )


_X21LineLoopbackCodeDetection_Type.__name__ = "Integer32"
_X21LineLoopbackCodeDetection_Object = MibTableColumn
x21LineLoopbackCodeDetection = _X21LineLoopbackCodeDetection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 7),
    _X21LineLoopbackCodeDetection_Type()
)
x21LineLoopbackCodeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineLoopbackCodeDetection.setStatus("current")


class _X21ConnectorType_Type(Integer32):
    """Custom type x21ConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hssiBackcard", 2),
          ("v35Backcard", 3),
          ("x21Backcard", 1))
    )


_X21ConnectorType_Type.__name__ = "Integer32"
_X21ConnectorType_Object = MibTableColumn
x21ConnectorType = _X21ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 8),
    _X21ConnectorType_Type()
)
x21ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21ConnectorType.setStatus("current")


class _X21InvertClock_Type(Integer32):
    """Custom type x21InvertClock based on Integer32"""
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
        *(("invertedAndLooped", 4),
          ("invertedAndNotLooped", 2),
          ("nonInvertedAndLooped", 3),
          ("nonInvertedAndNotLooped", 1))
    )


_X21InvertClock_Type.__name__ = "Integer32"
_X21InvertClock_Object = MibTableColumn
x21InvertClock = _X21InvertClock_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 9),
    _X21InvertClock_Type()
)
x21InvertClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21InvertClock.setStatus("current")


class _X21LineInterfaceType_Type(Integer32):
    """Custom type x21LineInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hssi", 1),
          ("v35", 3),
          ("x21", 2))
    )


_X21LineInterfaceType_Type.__name__ = "Integer32"
_X21LineInterfaceType_Object = MibTableColumn
x21LineInterfaceType = _X21LineInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 10),
    _X21LineInterfaceType_Type()
)
x21LineInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LineInterfaceType.setStatus("current")


class _X21ClkFrequencyThreshold_Type(Integer32):
    """Custom type x21ClkFrequencyThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_X21ClkFrequencyThreshold_Type.__name__ = "Integer32"
_X21ClkFrequencyThreshold_Object = MibTableColumn
x21ClkFrequencyThreshold = _X21ClkFrequencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 11),
    _X21ClkFrequencyThreshold_Type()
)
x21ClkFrequencyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21ClkFrequencyThreshold.setStatus("current")


class _SerialLineRate_Type(Integer32):
    """Custom type serialLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48000, 51840000),
    )


_SerialLineRate_Type.__name__ = "Integer32"
_SerialLineRate_Object = MibTableColumn
serialLineRate = _SerialLineRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 12),
    _SerialLineRate_Type()
)
serialLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialLineRate.setStatus("current")


class _SerialLineRateVariation_Type(Integer32):
    """Custom type serialLineRateVariation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SerialLineRateVariation_Type.__name__ = "Integer32"
_SerialLineRateVariation_Object = MibTableColumn
serialLineRateVariation = _SerialLineRateVariation_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 13),
    _SerialLineRateVariation_Type()
)
serialLineRateVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialLineRateVariation.setStatus("current")


class _X21LineNumofValidEntries_Type(Integer32):
    """Custom type x21LineNumofValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_X21LineNumofValidEntries_Type.__name__ = "Integer32"
_X21LineNumofValidEntries_Object = MibScalar
x21LineNumofValidEntries = _X21LineNumofValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 2),
    _X21LineNumofValidEntries_Type()
)
x21LineNumofValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LineNumofValidEntries.setStatus("current")
_X21AlmCnfGrp_ObjectIdentity = ObjectIdentity
x21AlmCnfGrp = _X21AlmCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2)
)
_X21AlmCnfGrpTable_Object = MibTable
x21AlmCnfGrpTable = _X21AlmCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    x21AlmCnfGrpTable.setStatus("current")
_X21AlmCnfGrpEntry_Object = MibTableRow
x21AlmCnfGrpEntry = _X21AlmCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1, 1)
)
x21AlmCnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-X21-MIB", "x21AlmCnfLineNum"),
)
if mibBuilder.loadTexts:
    x21AlmCnfGrpEntry.setStatus("current")


class _X21AlmCnfLineNum_Type(Integer32):
    """Custom type x21AlmCnfLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_X21AlmCnfLineNum_Type.__name__ = "Integer32"
_X21AlmCnfLineNum_Object = MibTableColumn
x21AlmCnfLineNum = _X21AlmCnfLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1, 1, 1),
    _X21AlmCnfLineNum_Type()
)
x21AlmCnfLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21AlmCnfLineNum.setStatus("current")


class _X21Severity_Type(Integer32):
    """Custom type x21Severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dontcare", 3),
          ("major", 2),
          ("minor", 1))
    )


_X21Severity_Type.__name__ = "Integer32"
_X21Severity_Object = MibTableColumn
x21Severity = _X21Severity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1, 1, 2),
    _X21Severity_Type()
)
x21Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21Severity.setStatus("current")
_X21AlmGrp_ObjectIdentity = ObjectIdentity
x21AlmGrp = _X21AlmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3)
)
_X21AlmGrpTable_Object = MibTable
x21AlmGrpTable = _X21AlmGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1)
)
if mibBuilder.loadTexts:
    x21AlmGrpTable.setStatus("current")
_X21AlmGrpEntry_Object = MibTableRow
x21AlmGrpEntry = _X21AlmGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1)
)
x21AlmGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-X21-MIB", "x21AlmLineNum"),
)
if mibBuilder.loadTexts:
    x21AlmGrpEntry.setStatus("current")


class _X21AlmLineNum_Type(Integer32):
    """Custom type x21AlmLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_X21AlmLineNum_Type.__name__ = "Integer32"
_X21AlmLineNum_Object = MibTableColumn
x21AlmLineNum = _X21AlmLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 1),
    _X21AlmLineNum_Type()
)
x21AlmLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21AlmLineNum.setStatus("current")


class _X21LineAlarmState_Type(Integer32):
    """Custom type x21LineAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X21LineAlarmState_Type.__name__ = "Integer32"
_X21LineAlarmState_Object = MibTableColumn
x21LineAlarmState = _X21LineAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 2),
    _X21LineAlarmState_Type()
)
x21LineAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LineAlarmState.setStatus("current")


class _X21LineEIAStatus_Type(Integer32):
    """Custom type x21LineEIAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_X21LineEIAStatus_Type.__name__ = "Integer32"
_X21LineEIAStatus_Object = MibTableColumn
x21LineEIAStatus = _X21LineEIAStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 3),
    _X21LineEIAStatus_Type()
)
x21LineEIAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LineEIAStatus.setStatus("current")


class _X21AlarmClrButton_Type(Integer32):
    """Custom type x21AlarmClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_X21AlarmClrButton_Type.__name__ = "Integer32"
_X21AlarmClrButton_Object = MibTableColumn
x21AlarmClrButton = _X21AlarmClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 4),
    _X21AlarmClrButton_Type()
)
x21AlarmClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21AlarmClrButton.setStatus("current")
_FrPortCnfX21PortGrpTable_Object = MibTable
frPortCnfX21PortGrpTable = _FrPortCnfX21PortGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    frPortCnfX21PortGrpTable.setStatus("current")
_FrPortCnfX21PortGrpEntry_Object = MibTableRow
frPortCnfX21PortGrpEntry = _FrPortCnfX21PortGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1)
)
frPortCnfX21PortGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-X21-MIB", "x21portNum"),
)
if mibBuilder.loadTexts:
    frPortCnfX21PortGrpEntry.setStatus("current")


class _X21portNum_Type(Integer32):
    """Custom type x21portNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_X21portNum_Type.__name__ = "Integer32"
_X21portNum_Object = MibTableColumn
x21portNum = _X21portNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 1),
    _X21portNum_Type()
)
x21portNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portNum.setStatus("current")


class _X21portLineNum_Type(Integer32):
    """Custom type x21portLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_X21portLineNum_Type.__name__ = "Integer32"
_X21portLineNum_Object = MibTableColumn
x21portLineNum = _X21portLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 2),
    _X21portLineNum_Type()
)
x21portLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portLineNum.setStatus("current")


class _X21portRowStatus_Type(Integer32):
    """Custom type x21portRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_X21portRowStatus_Type.__name__ = "Integer32"
_X21portRowStatus_Object = MibTableColumn
x21portRowStatus = _X21portRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 3),
    _X21portRowStatus_Type()
)
x21portRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portRowStatus.setStatus("current")


class _X21portFlagsBetweenFrames_Type(Integer32):
    """Custom type x21portFlagsBetweenFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_X21portFlagsBetweenFrames_Type.__name__ = "Integer32"
_X21portFlagsBetweenFrames_Object = MibTableColumn
x21portFlagsBetweenFrames = _X21portFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 4),
    _X21portFlagsBetweenFrames_Type()
)
x21portFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portFlagsBetweenFrames.setStatus("current")


class _X21portEqueueServiceRatio_Type(Integer32):
    """Custom type x21portEqueueServiceRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_X21portEqueueServiceRatio_Type.__name__ = "Integer32"
_X21portEqueueServiceRatio_Object = MibTableColumn
x21portEqueueServiceRatio = _X21portEqueueServiceRatio_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 5),
    _X21portEqueueServiceRatio_Type()
)
x21portEqueueServiceRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portEqueueServiceRatio.setStatus("current")


class _X21portSpeed_Type(Integer32):
    """Custom type x21portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_X21portSpeed_Type.__name__ = "Integer32"
_X21portSpeed_Object = MibTableColumn
x21portSpeed = _X21portSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 6),
    _X21portSpeed_Type()
)
x21portSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portSpeed.setStatus("current")


class _X21portAdmin_Type(Integer32):
    """Custom type x21portAdmin based on Integer32"""
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
          ("up", 1),
          ("write-Only", 3))
    )


_X21portAdmin_Type.__name__ = "Integer32"
_X21portAdmin_Object = MibTableColumn
x21portAdmin = _X21portAdmin_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 7),
    _X21portAdmin_Type()
)
x21portAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portAdmin.setStatus("current")


class _X21portType_Type(Integer32):
    """Custom type x21portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frFUNI", 2),
          ("frame-forward", 3),
          ("frame-relay", 1))
    )


_X21portType_Type.__name__ = "Integer32"
_X21portType_Object = MibTableColumn
x21portType = _X21portType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 8),
    _X21portType_Type()
)
x21portType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portType.setStatus("current")


class _X21portSvcStatus_Type(Integer32):
    """Custom type x21portSvcStatus based on Integer32"""
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


_X21portSvcStatus_Type.__name__ = "Integer32"
_X21portSvcStatus_Object = MibTableColumn
x21portSvcStatus = _X21portSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 9),
    _X21portSvcStatus_Type()
)
x21portSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portSvcStatus.setStatus("current")


class _X21portSvcInUse_Type(Integer32):
    """Custom type x21portSvcInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 2),
          ("not-use", 1))
    )


_X21portSvcInUse_Type.__name__ = "Integer32"
_X21portSvcInUse_Object = MibTableColumn
x21portSvcInUse = _X21portSvcInUse_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 10),
    _X21portSvcInUse_Type()
)
x21portSvcInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portSvcInUse.setStatus("current")


class _X21portSvcShareLcn_Type(Integer32):
    """Custom type x21portSvcShareLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card-based", 2),
          ("port-based", 1))
    )


_X21portSvcShareLcn_Type.__name__ = "Integer32"
_X21portSvcShareLcn_Object = MibTableColumn
x21portSvcShareLcn = _X21portSvcShareLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 11),
    _X21portSvcShareLcn_Type()
)
x21portSvcShareLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portSvcShareLcn.setStatus("current")


class _X21portSvcLcnLow_Type(Integer32):
    """Custom type x21portSvcLcnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 271),
    )


_X21portSvcLcnLow_Type.__name__ = "Integer32"
_X21portSvcLcnLow_Object = MibTableColumn
x21portSvcLcnLow = _X21portSvcLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 12),
    _X21portSvcLcnLow_Type()
)
x21portSvcLcnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portSvcLcnLow.setStatus("current")


class _X21portSvcLcnHigh_Type(Integer32):
    """Custom type x21portSvcLcnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 271),
    )


_X21portSvcLcnHigh_Type.__name__ = "Integer32"
_X21portSvcLcnHigh_Object = MibTableColumn
x21portSvcLcnHigh = _X21portSvcLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 13),
    _X21portSvcLcnHigh_Type()
)
x21portSvcLcnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portSvcLcnHigh.setStatus("current")


class _X21portSvcDlciLow_Type(Integer32):
    """Custom type x21portSvcDlciLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X21portSvcDlciLow_Type.__name__ = "Integer32"
_X21portSvcDlciLow_Object = MibTableColumn
x21portSvcDlciLow = _X21portSvcDlciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 14),
    _X21portSvcDlciLow_Type()
)
x21portSvcDlciLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portSvcDlciLow.setStatus("current")


class _X21portSvcDlciHigh_Type(Integer32):
    """Custom type x21portSvcDlciHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X21portSvcDlciHigh_Type.__name__ = "Integer32"
_X21portSvcDlciHigh_Object = MibTableColumn
x21portSvcDlciHigh = _X21portSvcDlciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 15),
    _X21portSvcDlciHigh_Type()
)
x21portSvcDlciHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portSvcDlciHigh.setStatus("current")


class _X21portDeleteSvcs_Type(Integer32):
    """Custom type x21portDeleteSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("other", 2))
    )


_X21portDeleteSvcs_Type.__name__ = "Integer32"
_X21portDeleteSvcs_Object = MibTableColumn
x21portDeleteSvcs = _X21portDeleteSvcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 16),
    _X21portDeleteSvcs_Type()
)
x21portDeleteSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21portDeleteSvcs.setStatus("current")


class _X21portIngrSvcBandW_Type(Integer32):
    """Custom type x21portIngrSvcBandW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_X21portIngrSvcBandW_Type.__name__ = "Integer32"
_X21portIngrSvcBandW_Object = MibTableColumn
x21portIngrSvcBandW = _X21portIngrSvcBandW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 17),
    _X21portIngrSvcBandW_Type()
)
x21portIngrSvcBandW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portIngrSvcBandW.setStatus("current")


class _X21portEgrSvcBandW_Type(Integer32):
    """Custom type x21portEgrSvcBandW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_X21portEgrSvcBandW_Type.__name__ = "Integer32"
_X21portEgrSvcBandW_Object = MibTableColumn
x21portEgrSvcBandW = _X21portEgrSvcBandW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 18),
    _X21portEgrSvcBandW_Type()
)
x21portEgrSvcBandW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21portEgrSvcBandW.setStatus("current")
_CwfX21MIBConformance_ObjectIdentity = ObjectIdentity
cwfX21MIBConformance = _CwfX21MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2)
)
_CwfX21MIBGroups_ObjectIdentity = ObjectIdentity
cwfX21MIBGroups = _CwfX21MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1)
)
_CwfX21MIBCompliances_ObjectIdentity = ObjectIdentity
cwfX21MIBCompliances = _CwfX21MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 2)
)

# Managed Objects groups

ciscoWanFrX21PortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 1)
)
ciscoWanFrX21PortGroup.setObjects(
      *(("CISCO-WAN-FR-X21-MIB", "x21portNum"),
        ("CISCO-WAN-FR-X21-MIB", "x21portLineNum"),
        ("CISCO-WAN-FR-X21-MIB", "x21portRowStatus"),
        ("CISCO-WAN-FR-X21-MIB", "x21portFlagsBetweenFrames"),
        ("CISCO-WAN-FR-X21-MIB", "x21portEqueueServiceRatio"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSpeed"),
        ("CISCO-WAN-FR-X21-MIB", "x21portAdmin"),
        ("CISCO-WAN-FR-X21-MIB", "x21portType"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcStatus"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcInUse"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcShareLcn"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcLcnLow"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcLcnHigh"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcDlciLow"),
        ("CISCO-WAN-FR-X21-MIB", "x21portSvcDlciHigh"),
        ("CISCO-WAN-FR-X21-MIB", "x21portDeleteSvcs"),
        ("CISCO-WAN-FR-X21-MIB", "x21portIngrSvcBandW"),
        ("CISCO-WAN-FR-X21-MIB", "x21portEgrSvcBandW"))
)
if mibBuilder.loadTexts:
    ciscoWanFrX21PortGroup.setStatus("current")

ciscoWanFrX21LineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 2)
)
ciscoWanFrX21LineGroup.setObjects(
      *(("CISCO-WAN-FR-X21-MIB", "x21LineNum"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineEnable"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineType"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineRate"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineLoopbackCommand"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineSendCode"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineLoopbackCodeDetection"),
        ("CISCO-WAN-FR-X21-MIB", "x21ConnectorType"),
        ("CISCO-WAN-FR-X21-MIB", "x21InvertClock"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineInterfaceType"),
        ("CISCO-WAN-FR-X21-MIB", "x21ClkFrequencyThreshold"),
        ("CISCO-WAN-FR-X21-MIB", "serialLineRate"),
        ("CISCO-WAN-FR-X21-MIB", "serialLineRateVariation"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineNumofValidEntries"))
)
if mibBuilder.loadTexts:
    ciscoWanFrX21LineGroup.setStatus("current")

ciscoWanFrX21AlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 3)
)
ciscoWanFrX21AlarmConfGroup.setObjects(
      *(("CISCO-WAN-FR-X21-MIB", "x21AlmCnfLineNum"),
        ("CISCO-WAN-FR-X21-MIB", "x21Severity"))
)
if mibBuilder.loadTexts:
    ciscoWanFrX21AlarmConfGroup.setStatus("current")

ciscoWanFrX21AlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 4)
)
ciscoWanFrX21AlarmGroup.setObjects(
      *(("CISCO-WAN-FR-X21-MIB", "x21AlmLineNum"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineAlarmState"),
        ("CISCO-WAN-FR-X21-MIB", "x21LineEIAStatus"),
        ("CISCO-WAN-FR-X21-MIB", "x21AlarmClrButton"))
)
if mibBuilder.loadTexts:
    ciscoWanFrX21AlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwfX21Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwfX21Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FR-X21-MIB",
    **{"x21CnfGrp": x21CnfGrp,
       "x21CnfGrpTable": x21CnfGrpTable,
       "x21CnfGrpEntry": x21CnfGrpEntry,
       "x21LineNum": x21LineNum,
       "x21LineEnable": x21LineEnable,
       "x21LineType": x21LineType,
       "x21LineRate": x21LineRate,
       "x21LineLoopbackCommand": x21LineLoopbackCommand,
       "x21LineSendCode": x21LineSendCode,
       "x21LineLoopbackCodeDetection": x21LineLoopbackCodeDetection,
       "x21ConnectorType": x21ConnectorType,
       "x21InvertClock": x21InvertClock,
       "x21LineInterfaceType": x21LineInterfaceType,
       "x21ClkFrequencyThreshold": x21ClkFrequencyThreshold,
       "serialLineRate": serialLineRate,
       "serialLineRateVariation": serialLineRateVariation,
       "x21LineNumofValidEntries": x21LineNumofValidEntries,
       "x21AlmCnfGrp": x21AlmCnfGrp,
       "x21AlmCnfGrpTable": x21AlmCnfGrpTable,
       "x21AlmCnfGrpEntry": x21AlmCnfGrpEntry,
       "x21AlmCnfLineNum": x21AlmCnfLineNum,
       "x21Severity": x21Severity,
       "x21AlmGrp": x21AlmGrp,
       "x21AlmGrpTable": x21AlmGrpTable,
       "x21AlmGrpEntry": x21AlmGrpEntry,
       "x21AlmLineNum": x21AlmLineNum,
       "x21LineAlarmState": x21LineAlarmState,
       "x21LineEIAStatus": x21LineEIAStatus,
       "x21AlarmClrButton": x21AlarmClrButton,
       "frPortCnfX21PortGrpTable": frPortCnfX21PortGrpTable,
       "frPortCnfX21PortGrpEntry": frPortCnfX21PortGrpEntry,
       "x21portNum": x21portNum,
       "x21portLineNum": x21portLineNum,
       "x21portRowStatus": x21portRowStatus,
       "x21portFlagsBetweenFrames": x21portFlagsBetweenFrames,
       "x21portEqueueServiceRatio": x21portEqueueServiceRatio,
       "x21portSpeed": x21portSpeed,
       "x21portAdmin": x21portAdmin,
       "x21portType": x21portType,
       "x21portSvcStatus": x21portSvcStatus,
       "x21portSvcInUse": x21portSvcInUse,
       "x21portSvcShareLcn": x21portSvcShareLcn,
       "x21portSvcLcnLow": x21portSvcLcnLow,
       "x21portSvcLcnHigh": x21portSvcLcnHigh,
       "x21portSvcDlciLow": x21portSvcDlciLow,
       "x21portSvcDlciHigh": x21portSvcDlciHigh,
       "x21portDeleteSvcs": x21portDeleteSvcs,
       "x21portIngrSvcBandW": x21portIngrSvcBandW,
       "x21portEgrSvcBandW": x21portEgrSvcBandW,
       "ciscoWanFrX21MIB": ciscoWanFrX21MIB,
       "cwfX21MIBConformance": cwfX21MIBConformance,
       "cwfX21MIBGroups": cwfX21MIBGroups,
       "ciscoWanFrX21PortGroup": ciscoWanFrX21PortGroup,
       "ciscoWanFrX21LineGroup": ciscoWanFrX21LineGroup,
       "ciscoWanFrX21AlarmConfGroup": ciscoWanFrX21AlarmConfGroup,
       "ciscoWanFrX21AlarmGroup": ciscoWanFrX21AlarmGroup,
       "cwfX21MIBCompliances": cwfX21MIBCompliances,
       "cwfX21Compliance": cwfX21Compliance}
)
