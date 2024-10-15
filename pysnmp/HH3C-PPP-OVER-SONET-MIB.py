# SNMP MIB module (HH3C-PPP-OVER-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PPP-OVER-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:32 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cPos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19)
)
hh3cPos.setRevisions(
        ("2013-10-10 17:00",
         "2010-05-19 17:00",
         "2007-07-19 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPosMIBObjects_ObjectIdentity = ObjectIdentity
hh3cPosMIBObjects = _Hh3cPosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1)
)
_Hh3cPosParamTable_Object = MibTable
hh3cPosParamTable = _Hh3cPosParamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cPosParamTable.setStatus("current")
_Hh3cPosParamTableEntry_Object = MibTableRow
hh3cPosParamTableEntry = _Hh3cPosParamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1)
)
hh3cPosParamTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cPosParamTableEntry.setStatus("current")


class _Hh3cPosCRC_Type(Integer32):
    """Custom type hh3cPosCRC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 2),
          ("crc32", 1))
    )


_Hh3cPosCRC_Type.__name__ = "Integer32"
_Hh3cPosCRC_Object = MibTableColumn
hh3cPosCRC = _Hh3cPosCRC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 1),
    _Hh3cPosCRC_Type()
)
hh3cPosCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosCRC.setStatus("current")
_Hh3cPosMTU_Type = Integer32
_Hh3cPosMTU_Object = MibTableColumn
hh3cPosMTU = _Hh3cPosMTU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 2),
    _Hh3cPosMTU_Type()
)
hh3cPosMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosMTU.setStatus("current")


class _Hh3cPosScramble_Type(TruthValue):
    """Custom type hh3cPosScramble based on TruthValue"""


_Hh3cPosScramble_Object = MibTableColumn
hh3cPosScramble = _Hh3cPosScramble_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 3),
    _Hh3cPosScramble_Type()
)
hh3cPosScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosScramble.setStatus("current")


class _Hh3cPosClockSource_Type(Integer32):
    """Custom type hh3cPosClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 2),
          ("system", 1))
    )


_Hh3cPosClockSource_Type.__name__ = "Integer32"
_Hh3cPosClockSource_Object = MibTableColumn
hh3cPosClockSource = _Hh3cPosClockSource_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 4),
    _Hh3cPosClockSource_Type()
)
hh3cPosClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosClockSource.setStatus("current")


class _Hh3cPosSdhFlagJ0_Type(DisplayString):
    """Custom type hh3cPosSdhFlagJ0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Hh3cPosSdhFlagJ0_Type.__name__ = "DisplayString"
_Hh3cPosSdhFlagJ0_Object = MibTableColumn
hh3cPosSdhFlagJ0 = _Hh3cPosSdhFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 5),
    _Hh3cPosSdhFlagJ0_Type()
)
hh3cPosSdhFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosSdhFlagJ0.setStatus("current")


class _Hh3cPosSdhFlagJ1_Type(DisplayString):
    """Custom type hh3cPosSdhFlagJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Hh3cPosSdhFlagJ1_Type.__name__ = "DisplayString"
_Hh3cPosSdhFlagJ1_Object = MibTableColumn
hh3cPosSdhFlagJ1 = _Hh3cPosSdhFlagJ1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 6),
    _Hh3cPosSdhFlagJ1_Type()
)
hh3cPosSdhFlagJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosSdhFlagJ1.setStatus("current")


class _Hh3cPosSonetFlagJ0_Type(Integer32):
    """Custom type hh3cPosSonetFlagJ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cPosSonetFlagJ0_Type.__name__ = "Integer32"
_Hh3cPosSonetFlagJ0_Object = MibTableColumn
hh3cPosSonetFlagJ0 = _Hh3cPosSonetFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 7),
    _Hh3cPosSonetFlagJ0_Type()
)
hh3cPosSonetFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosSonetFlagJ0.setStatus("current")


class _Hh3cPosSonetFlagJ1_Type(DisplayString):
    """Custom type hh3cPosSonetFlagJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_Hh3cPosSonetFlagJ1_Type.__name__ = "DisplayString"
_Hh3cPosSonetFlagJ1_Object = MibTableColumn
hh3cPosSonetFlagJ1 = _Hh3cPosSonetFlagJ1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 8),
    _Hh3cPosSonetFlagJ1_Type()
)
hh3cPosSonetFlagJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosSonetFlagJ1.setStatus("current")


class _Hh3cPosFlagC2_Type(Integer32):
    """Custom type hh3cPosFlagC2 based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cPosFlagC2_Type.__name__ = "Integer32"
_Hh3cPosFlagC2_Object = MibTableColumn
hh3cPosFlagC2 = _Hh3cPosFlagC2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 9),
    _Hh3cPosFlagC2_Type()
)
hh3cPosFlagC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosFlagC2.setStatus("current")


class _Hh3cPosFrameType_Type(Integer32):
    """Custom type hh3cPosFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_Hh3cPosFrameType_Type.__name__ = "Integer32"
_Hh3cPosFrameType_Object = MibTableColumn
hh3cPosFrameType = _Hh3cPosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 10),
    _Hh3cPosFrameType_Type()
)
hh3cPosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosFrameType.setStatus("current")


class _Hh3cPosBindVlanId_Type(Integer32):
    """Custom type hh3cPosBindVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hh3cPosBindVlanId_Type.__name__ = "Integer32"
_Hh3cPosBindVlanId_Object = MibTableColumn
hh3cPosBindVlanId = _Hh3cPosBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 11),
    _Hh3cPosBindVlanId_Type()
)
hh3cPosBindVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosBindVlanId.setStatus("current")


class _Hh3cPosEncapsulation_Type(Integer32):
    """Custom type hh3cPosEncapsulation based on Integer32"""
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
        *(("fr", 3),
          ("hdlc", 2),
          ("ppp", 1))
    )


_Hh3cPosEncapsulation_Type.__name__ = "Integer32"
_Hh3cPosEncapsulation_Object = MibTableColumn
hh3cPosEncapsulation = _Hh3cPosEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 12),
    _Hh3cPosEncapsulation_Type()
)
hh3cPosEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosEncapsulation.setStatus("current")


class _Hh3cPoskeepaliveTimeout_Type(Integer32):
    """Custom type hh3cPoskeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Hh3cPoskeepaliveTimeout_Type.__name__ = "Integer32"
_Hh3cPoskeepaliveTimeout_Object = MibTableColumn
hh3cPoskeepaliveTimeout = _Hh3cPoskeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 13),
    _Hh3cPoskeepaliveTimeout_Type()
)
hh3cPoskeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPoskeepaliveTimeout.setStatus("current")


class _Hh3cPosBERthresholdSF_Type(Integer32):
    """Custom type hh3cPosBERthresholdSF based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_Hh3cPosBERthresholdSF_Type.__name__ = "Integer32"
_Hh3cPosBERthresholdSF_Object = MibTableColumn
hh3cPosBERthresholdSF = _Hh3cPosBERthresholdSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 14),
    _Hh3cPosBERthresholdSF_Type()
)
hh3cPosBERthresholdSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosBERthresholdSF.setStatus("current")


class _Hh3cPosBERthresholdSD_Type(Integer32):
    """Custom type hh3cPosBERthresholdSD based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_Hh3cPosBERthresholdSD_Type.__name__ = "Integer32"
_Hh3cPosBERthresholdSD_Object = MibTableColumn
hh3cPosBERthresholdSD = _Hh3cPosBERthresholdSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 15),
    _Hh3cPosBERthresholdSD_Type()
)
hh3cPosBERthresholdSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosBERthresholdSD.setStatus("current")
_Hh3cPosB1Error_Type = Counter64
_Hh3cPosB1Error_Object = MibTableColumn
hh3cPosB1Error = _Hh3cPosB1Error_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 16),
    _Hh3cPosB1Error_Type()
)
hh3cPosB1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosB1Error.setStatus("current")
_Hh3cPosB2Error_Type = Counter64
_Hh3cPosB2Error_Object = MibTableColumn
hh3cPosB2Error = _Hh3cPosB2Error_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 17),
    _Hh3cPosB2Error_Type()
)
hh3cPosB2Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosB2Error.setStatus("current")
_Hh3cPosB3Error_Type = Counter64
_Hh3cPosB3Error_Object = MibTableColumn
hh3cPosB3Error = _Hh3cPosB3Error_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 18),
    _Hh3cPosB3Error_Type()
)
hh3cPosB3Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosB3Error.setStatus("current")
_Hh3cPosM1Error_Type = Counter64
_Hh3cPosM1Error_Object = MibTableColumn
hh3cPosM1Error = _Hh3cPosM1Error_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 19),
    _Hh3cPosM1Error_Type()
)
hh3cPosM1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosM1Error.setStatus("current")
_Hh3cPosG1Error_Type = Counter64
_Hh3cPosG1Error_Object = MibTableColumn
hh3cPosG1Error = _Hh3cPosG1Error_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 20),
    _Hh3cPosG1Error_Type()
)
hh3cPosG1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosG1Error.setStatus("current")


class _Hh3cPosFlagJ0Type_Type(Integer32):
    """Custom type hh3cPosFlagJ0Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_Hh3cPosFlagJ0Type_Type.__name__ = "Integer32"
_Hh3cPosFlagJ0Type_Object = MibTableColumn
hh3cPosFlagJ0Type = _Hh3cPosFlagJ0Type_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 21),
    _Hh3cPosFlagJ0Type_Type()
)
hh3cPosFlagJ0Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosFlagJ0Type.setStatus("current")


class _Hh3cPosFlagJ1Type_Type(Integer32):
    """Custom type hh3cPosFlagJ1Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_Hh3cPosFlagJ1Type_Type.__name__ = "Integer32"
_Hh3cPosFlagJ1Type_Object = MibTableColumn
hh3cPosFlagJ1Type = _Hh3cPosFlagJ1Type_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 22),
    _Hh3cPosFlagJ1Type_Type()
)
hh3cPosFlagJ1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosFlagJ1Type.setStatus("current")


class _Hh3cPosB1TCAThreshold_Type(Integer32):
    """Custom type hh3cPosB1TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_Hh3cPosB1TCAThreshold_Type.__name__ = "Integer32"
_Hh3cPosB1TCAThreshold_Object = MibTableColumn
hh3cPosB1TCAThreshold = _Hh3cPosB1TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 23),
    _Hh3cPosB1TCAThreshold_Type()
)
hh3cPosB1TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosB1TCAThreshold.setStatus("current")


class _Hh3cPosB2TCAThreshold_Type(Integer32):
    """Custom type hh3cPosB2TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_Hh3cPosB2TCAThreshold_Type.__name__ = "Integer32"
_Hh3cPosB2TCAThreshold_Object = MibTableColumn
hh3cPosB2TCAThreshold = _Hh3cPosB2TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 24),
    _Hh3cPosB2TCAThreshold_Type()
)
hh3cPosB2TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosB2TCAThreshold.setStatus("current")


class _Hh3cPosB3TCAThreshold_Type(Integer32):
    """Custom type hh3cPosB3TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_Hh3cPosB3TCAThreshold_Type.__name__ = "Integer32"
_Hh3cPosB3TCAThreshold_Object = MibTableColumn
hh3cPosB3TCAThreshold = _Hh3cPosB3TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 25),
    _Hh3cPosB3TCAThreshold_Type()
)
hh3cPosB3TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosB3TCAThreshold.setStatus("current")


class _Hh3cPosB1TCAEnable_Type(Integer32):
    """Custom type hh3cPosB1TCAEnable based on Integer32"""
    defaultValue = 1

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


_Hh3cPosB1TCAEnable_Type.__name__ = "Integer32"
_Hh3cPosB1TCAEnable_Object = MibTableColumn
hh3cPosB1TCAEnable = _Hh3cPosB1TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 26),
    _Hh3cPosB1TCAEnable_Type()
)
hh3cPosB1TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosB1TCAEnable.setStatus("current")


class _Hh3cPosB2TCAEnable_Type(Integer32):
    """Custom type hh3cPosB2TCAEnable based on Integer32"""
    defaultValue = 1

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


_Hh3cPosB2TCAEnable_Type.__name__ = "Integer32"
_Hh3cPosB2TCAEnable_Object = MibTableColumn
hh3cPosB2TCAEnable = _Hh3cPosB2TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 27),
    _Hh3cPosB2TCAEnable_Type()
)
hh3cPosB2TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosB2TCAEnable.setStatus("current")


class _Hh3cPosB3TCAEnable_Type(Integer32):
    """Custom type hh3cPosB3TCAEnable based on Integer32"""
    defaultValue = 1

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


_Hh3cPosB3TCAEnable_Type.__name__ = "Integer32"
_Hh3cPosB3TCAEnable_Object = MibTableColumn
hh3cPosB3TCAEnable = _Hh3cPosB3TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 28),
    _Hh3cPosB3TCAEnable_Type()
)
hh3cPosB3TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosB3TCAEnable.setStatus("current")
_Hh3cPosMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
hh3cPosMIBNotificationsPrefix = _Hh3cPosMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2)
)
_Hh3cPosMIBNotifications_ObjectIdentity = ObjectIdentity
hh3cPosMIBNotifications = _Hh3cPosMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cPosLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 1)
)
hh3cPosLOSAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLOSAlarm.setStatus(
        "current"
    )

hh3cPosLOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 2)
)
hh3cPosLOFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLOFAlarm.setStatus(
        "current"
    )

hh3cPosOOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 3)
)
hh3cPosOOFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosOOFAlarm.setStatus(
        "current"
    )

hh3cPosLAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 4)
)
hh3cPosLAISAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLAISAlarm.setStatus(
        "current"
    )

hh3cPosLRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 5)
)
hh3cPosLRDIAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLRDIAlarm.setStatus(
        "current"
    )

hh3cPosPRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 6)
)
hh3cPosPRDIAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosPRDIAlarm.setStatus(
        "current"
    )

hh3cPosPAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 7)
)
hh3cPosPAISAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosPAISAlarm.setStatus(
        "current"
    )

hh3cPosLOPAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 8)
)
hh3cPosLOPAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLOPAlarm.setStatus(
        "current"
    )

hh3cPosSTIMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 9)
)
hh3cPosSTIMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosSTIMAlarm.setStatus(
        "current"
    )

hh3cPosPTIMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 10)
)
hh3cPosPTIMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosPTIMAlarm.setStatus(
        "current"
    )

hh3cPosPSLMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 11)
)
hh3cPosPSLMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosPSLMAlarm.setStatus(
        "current"
    )

hh3cPosLSDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 12)
)
hh3cPosLSDAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLSDAlarm.setStatus(
        "current"
    )

hh3cPosLSFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 13)
)
hh3cPosLSFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosLSFAlarm.setStatus(
        "current"
    )

hh3cPosNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 14)
)
hh3cPosNormalAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cPosNormalAlarm.setStatus(
        "current"
    )

hh3cPosB1TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 15)
)
hh3cPosB1TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cPosB1TCAlarm.setStatus(
        "current"
    )

hh3cPosB2TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 16)
)
hh3cPosB2TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cPosB2TCAlarm.setStatus(
        "current"
    )

hh3cPosB3TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 17)
)
hh3cPosB3TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cPosB3TCAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PPP-OVER-SONET-MIB",
    **{"hh3cPos": hh3cPos,
       "hh3cPosMIBObjects": hh3cPosMIBObjects,
       "hh3cPosParamTable": hh3cPosParamTable,
       "hh3cPosParamTableEntry": hh3cPosParamTableEntry,
       "hh3cPosCRC": hh3cPosCRC,
       "hh3cPosMTU": hh3cPosMTU,
       "hh3cPosScramble": hh3cPosScramble,
       "hh3cPosClockSource": hh3cPosClockSource,
       "hh3cPosSdhFlagJ0": hh3cPosSdhFlagJ0,
       "hh3cPosSdhFlagJ1": hh3cPosSdhFlagJ1,
       "hh3cPosSonetFlagJ0": hh3cPosSonetFlagJ0,
       "hh3cPosSonetFlagJ1": hh3cPosSonetFlagJ1,
       "hh3cPosFlagC2": hh3cPosFlagC2,
       "hh3cPosFrameType": hh3cPosFrameType,
       "hh3cPosBindVlanId": hh3cPosBindVlanId,
       "hh3cPosEncapsulation": hh3cPosEncapsulation,
       "hh3cPoskeepaliveTimeout": hh3cPoskeepaliveTimeout,
       "hh3cPosBERthresholdSF": hh3cPosBERthresholdSF,
       "hh3cPosBERthresholdSD": hh3cPosBERthresholdSD,
       "hh3cPosB1Error": hh3cPosB1Error,
       "hh3cPosB2Error": hh3cPosB2Error,
       "hh3cPosB3Error": hh3cPosB3Error,
       "hh3cPosM1Error": hh3cPosM1Error,
       "hh3cPosG1Error": hh3cPosG1Error,
       "hh3cPosFlagJ0Type": hh3cPosFlagJ0Type,
       "hh3cPosFlagJ1Type": hh3cPosFlagJ1Type,
       "hh3cPosB1TCAThreshold": hh3cPosB1TCAThreshold,
       "hh3cPosB2TCAThreshold": hh3cPosB2TCAThreshold,
       "hh3cPosB3TCAThreshold": hh3cPosB3TCAThreshold,
       "hh3cPosB1TCAEnable": hh3cPosB1TCAEnable,
       "hh3cPosB2TCAEnable": hh3cPosB2TCAEnable,
       "hh3cPosB3TCAEnable": hh3cPosB3TCAEnable,
       "hh3cPosMIBNotificationsPrefix": hh3cPosMIBNotificationsPrefix,
       "hh3cPosMIBNotifications": hh3cPosMIBNotifications,
       "hh3cPosLOSAlarm": hh3cPosLOSAlarm,
       "hh3cPosLOFAlarm": hh3cPosLOFAlarm,
       "hh3cPosOOFAlarm": hh3cPosOOFAlarm,
       "hh3cPosLAISAlarm": hh3cPosLAISAlarm,
       "hh3cPosLRDIAlarm": hh3cPosLRDIAlarm,
       "hh3cPosPRDIAlarm": hh3cPosPRDIAlarm,
       "hh3cPosPAISAlarm": hh3cPosPAISAlarm,
       "hh3cPosLOPAlarm": hh3cPosLOPAlarm,
       "hh3cPosSTIMAlarm": hh3cPosSTIMAlarm,
       "hh3cPosPTIMAlarm": hh3cPosPTIMAlarm,
       "hh3cPosPSLMAlarm": hh3cPosPSLMAlarm,
       "hh3cPosLSDAlarm": hh3cPosLSDAlarm,
       "hh3cPosLSFAlarm": hh3cPosLSFAlarm,
       "hh3cPosNormalAlarm": hh3cPosNormalAlarm,
       "hh3cPosB1TCAlarm": hh3cPosB1TCAlarm,
       "hh3cPosB2TCAlarm": hh3cPosB2TCAlarm,
       "hh3cPosB3TCAlarm": hh3cPosB3TCAlarm}
)
