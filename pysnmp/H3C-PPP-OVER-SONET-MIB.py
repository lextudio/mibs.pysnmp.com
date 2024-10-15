# SNMP MIB module (H3C-PPP-OVER-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-PPP-OVER-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:10 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cPos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19)
)
h3cPos.setRevisions(
        ("2010-05-19 17:00",
         "2007-07-19 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPosMIBObjects_ObjectIdentity = ObjectIdentity
h3cPosMIBObjects = _H3cPosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1)
)
_H3cPosParamTable_Object = MibTable
h3cPosParamTable = _H3cPosParamTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    h3cPosParamTable.setStatus("current")
_H3cPosParamTableEntry_Object = MibTableRow
h3cPosParamTableEntry = _H3cPosParamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1)
)
h3cPosParamTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cPosParamTableEntry.setStatus("current")


class _H3cPosCRC_Type(Integer32):
    """Custom type h3cPosCRC based on Integer32"""
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


_H3cPosCRC_Type.__name__ = "Integer32"
_H3cPosCRC_Object = MibTableColumn
h3cPosCRC = _H3cPosCRC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 1),
    _H3cPosCRC_Type()
)
h3cPosCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosCRC.setStatus("current")


class _H3cPosMTU_Type(Integer32):
    """Custom type h3cPosMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9192),
    )


_H3cPosMTU_Type.__name__ = "Integer32"
_H3cPosMTU_Object = MibTableColumn
h3cPosMTU = _H3cPosMTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 2),
    _H3cPosMTU_Type()
)
h3cPosMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosMTU.setStatus("current")


class _H3cPosScramble_Type(TruthValue):
    """Custom type h3cPosScramble based on TruthValue"""


_H3cPosScramble_Object = MibTableColumn
h3cPosScramble = _H3cPosScramble_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 3),
    _H3cPosScramble_Type()
)
h3cPosScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosScramble.setStatus("current")


class _H3cPosClockSource_Type(Integer32):
    """Custom type h3cPosClockSource based on Integer32"""
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


_H3cPosClockSource_Type.__name__ = "Integer32"
_H3cPosClockSource_Object = MibTableColumn
h3cPosClockSource = _H3cPosClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 4),
    _H3cPosClockSource_Type()
)
h3cPosClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosClockSource.setStatus("current")


class _H3cPosSdhFlagJ0_Type(DisplayString):
    """Custom type h3cPosSdhFlagJ0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_H3cPosSdhFlagJ0_Type.__name__ = "DisplayString"
_H3cPosSdhFlagJ0_Object = MibTableColumn
h3cPosSdhFlagJ0 = _H3cPosSdhFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 5),
    _H3cPosSdhFlagJ0_Type()
)
h3cPosSdhFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosSdhFlagJ0.setStatus("current")


class _H3cPosSdhFlagJ1_Type(DisplayString):
    """Custom type h3cPosSdhFlagJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_H3cPosSdhFlagJ1_Type.__name__ = "DisplayString"
_H3cPosSdhFlagJ1_Object = MibTableColumn
h3cPosSdhFlagJ1 = _H3cPosSdhFlagJ1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 6),
    _H3cPosSdhFlagJ1_Type()
)
h3cPosSdhFlagJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosSdhFlagJ1.setStatus("current")


class _H3cPosSonetFlagJ0_Type(Integer32):
    """Custom type h3cPosSonetFlagJ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cPosSonetFlagJ0_Type.__name__ = "Integer32"
_H3cPosSonetFlagJ0_Object = MibTableColumn
h3cPosSonetFlagJ0 = _H3cPosSonetFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 7),
    _H3cPosSonetFlagJ0_Type()
)
h3cPosSonetFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosSonetFlagJ0.setStatus("current")


class _H3cPosSonetFlagJ1_Type(DisplayString):
    """Custom type h3cPosSonetFlagJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_H3cPosSonetFlagJ1_Type.__name__ = "DisplayString"
_H3cPosSonetFlagJ1_Object = MibTableColumn
h3cPosSonetFlagJ1 = _H3cPosSonetFlagJ1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 8),
    _H3cPosSonetFlagJ1_Type()
)
h3cPosSonetFlagJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosSonetFlagJ1.setStatus("current")


class _H3cPosFlagC2_Type(Integer32):
    """Custom type h3cPosFlagC2 based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cPosFlagC2_Type.__name__ = "Integer32"
_H3cPosFlagC2_Object = MibTableColumn
h3cPosFlagC2 = _H3cPosFlagC2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 9),
    _H3cPosFlagC2_Type()
)
h3cPosFlagC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosFlagC2.setStatus("current")


class _H3cPosFrameType_Type(Integer32):
    """Custom type h3cPosFrameType based on Integer32"""
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


_H3cPosFrameType_Type.__name__ = "Integer32"
_H3cPosFrameType_Object = MibTableColumn
h3cPosFrameType = _H3cPosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 10),
    _H3cPosFrameType_Type()
)
h3cPosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosFrameType.setStatus("current")


class _H3cPosBindVlanId_Type(Integer32):
    """Custom type h3cPosBindVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_H3cPosBindVlanId_Type.__name__ = "Integer32"
_H3cPosBindVlanId_Object = MibTableColumn
h3cPosBindVlanId = _H3cPosBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 11),
    _H3cPosBindVlanId_Type()
)
h3cPosBindVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosBindVlanId.setStatus("current")


class _H3cPosEncapsulation_Type(Integer32):
    """Custom type h3cPosEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("ppp", 1))
    )


_H3cPosEncapsulation_Type.__name__ = "Integer32"
_H3cPosEncapsulation_Object = MibTableColumn
h3cPosEncapsulation = _H3cPosEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 12),
    _H3cPosEncapsulation_Type()
)
h3cPosEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosEncapsulation.setStatus("current")


class _H3cPoskeepaliveTimeout_Type(Integer32):
    """Custom type h3cPoskeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_H3cPoskeepaliveTimeout_Type.__name__ = "Integer32"
_H3cPoskeepaliveTimeout_Object = MibTableColumn
h3cPoskeepaliveTimeout = _H3cPoskeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 13),
    _H3cPoskeepaliveTimeout_Type()
)
h3cPoskeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPoskeepaliveTimeout.setStatus("current")


class _H3cPosBERthresholdSF_Type(Integer32):
    """Custom type h3cPosBERthresholdSF based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_H3cPosBERthresholdSF_Type.__name__ = "Integer32"
_H3cPosBERthresholdSF_Object = MibTableColumn
h3cPosBERthresholdSF = _H3cPosBERthresholdSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 14),
    _H3cPosBERthresholdSF_Type()
)
h3cPosBERthresholdSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosBERthresholdSF.setStatus("current")


class _H3cPosBERthresholdSD_Type(Integer32):
    """Custom type h3cPosBERthresholdSD based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_H3cPosBERthresholdSD_Type.__name__ = "Integer32"
_H3cPosBERthresholdSD_Object = MibTableColumn
h3cPosBERthresholdSD = _H3cPosBERthresholdSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 15),
    _H3cPosBERthresholdSD_Type()
)
h3cPosBERthresholdSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosBERthresholdSD.setStatus("current")
_H3cPosB1Error_Type = Counter64
_H3cPosB1Error_Object = MibTableColumn
h3cPosB1Error = _H3cPosB1Error_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 16),
    _H3cPosB1Error_Type()
)
h3cPosB1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosB1Error.setStatus("current")
_H3cPosB2Error_Type = Counter64
_H3cPosB2Error_Object = MibTableColumn
h3cPosB2Error = _H3cPosB2Error_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 17),
    _H3cPosB2Error_Type()
)
h3cPosB2Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosB2Error.setStatus("current")
_H3cPosB3Error_Type = Counter64
_H3cPosB3Error_Object = MibTableColumn
h3cPosB3Error = _H3cPosB3Error_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 18),
    _H3cPosB3Error_Type()
)
h3cPosB3Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosB3Error.setStatus("current")
_H3cPosM1Error_Type = Counter64
_H3cPosM1Error_Object = MibTableColumn
h3cPosM1Error = _H3cPosM1Error_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 19),
    _H3cPosM1Error_Type()
)
h3cPosM1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosM1Error.setStatus("current")
_H3cPosG1Error_Type = Counter64
_H3cPosG1Error_Object = MibTableColumn
h3cPosG1Error = _H3cPosG1Error_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 20),
    _H3cPosG1Error_Type()
)
h3cPosG1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosG1Error.setStatus("current")


class _H3cPosFlagJ0Type_Type(Integer32):
    """Custom type h3cPosFlagJ0Type based on Integer32"""
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


_H3cPosFlagJ0Type_Type.__name__ = "Integer32"
_H3cPosFlagJ0Type_Object = MibTableColumn
h3cPosFlagJ0Type = _H3cPosFlagJ0Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 21),
    _H3cPosFlagJ0Type_Type()
)
h3cPosFlagJ0Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosFlagJ0Type.setStatus("current")


class _H3cPosFlagJ1Type_Type(Integer32):
    """Custom type h3cPosFlagJ1Type based on Integer32"""
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


_H3cPosFlagJ1Type_Type.__name__ = "Integer32"
_H3cPosFlagJ1Type_Object = MibTableColumn
h3cPosFlagJ1Type = _H3cPosFlagJ1Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 22),
    _H3cPosFlagJ1Type_Type()
)
h3cPosFlagJ1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosFlagJ1Type.setStatus("current")


class _H3cPosB1TCAThreshold_Type(Integer32):
    """Custom type h3cPosB1TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_H3cPosB1TCAThreshold_Type.__name__ = "Integer32"
_H3cPosB1TCAThreshold_Object = MibTableColumn
h3cPosB1TCAThreshold = _H3cPosB1TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 23),
    _H3cPosB1TCAThreshold_Type()
)
h3cPosB1TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosB1TCAThreshold.setStatus("current")


class _H3cPosB2TCAThreshold_Type(Integer32):
    """Custom type h3cPosB2TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_H3cPosB2TCAThreshold_Type.__name__ = "Integer32"
_H3cPosB2TCAThreshold_Object = MibTableColumn
h3cPosB2TCAThreshold = _H3cPosB2TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 24),
    _H3cPosB2TCAThreshold_Type()
)
h3cPosB2TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosB2TCAThreshold.setStatus("current")


class _H3cPosB3TCAThreshold_Type(Integer32):
    """Custom type h3cPosB3TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_H3cPosB3TCAThreshold_Type.__name__ = "Integer32"
_H3cPosB3TCAThreshold_Object = MibTableColumn
h3cPosB3TCAThreshold = _H3cPosB3TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 25),
    _H3cPosB3TCAThreshold_Type()
)
h3cPosB3TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosB3TCAThreshold.setStatus("current")


class _H3cPosB1TCAEnable_Type(Integer32):
    """Custom type h3cPosB1TCAEnable based on Integer32"""
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


_H3cPosB1TCAEnable_Type.__name__ = "Integer32"
_H3cPosB1TCAEnable_Object = MibTableColumn
h3cPosB1TCAEnable = _H3cPosB1TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 26),
    _H3cPosB1TCAEnable_Type()
)
h3cPosB1TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosB1TCAEnable.setStatus("current")


class _H3cPosB2TCAEnable_Type(Integer32):
    """Custom type h3cPosB2TCAEnable based on Integer32"""
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


_H3cPosB2TCAEnable_Type.__name__ = "Integer32"
_H3cPosB2TCAEnable_Object = MibTableColumn
h3cPosB2TCAEnable = _H3cPosB2TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 27),
    _H3cPosB2TCAEnable_Type()
)
h3cPosB2TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosB2TCAEnable.setStatus("current")


class _H3cPosB3TCAEnable_Type(Integer32):
    """Custom type h3cPosB3TCAEnable based on Integer32"""
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


_H3cPosB3TCAEnable_Type.__name__ = "Integer32"
_H3cPosB3TCAEnable_Object = MibTableColumn
h3cPosB3TCAEnable = _H3cPosB3TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 1, 1, 1, 28),
    _H3cPosB3TCAEnable_Type()
)
h3cPosB3TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosB3TCAEnable.setStatus("current")
_H3cPosMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
h3cPosMIBNotificationsPrefix = _H3cPosMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2)
)
_H3cPosMIBNotifications_ObjectIdentity = ObjectIdentity
h3cPosMIBNotifications = _H3cPosMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cPosLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 1)
)
h3cPosLOSAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLOSAlarm.setStatus(
        "current"
    )

h3cPosLOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 2)
)
h3cPosLOFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLOFAlarm.setStatus(
        "current"
    )

h3cPosOOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 3)
)
h3cPosOOFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosOOFAlarm.setStatus(
        "current"
    )

h3cPosLAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 4)
)
h3cPosLAISAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLAISAlarm.setStatus(
        "current"
    )

h3cPosLRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 5)
)
h3cPosLRDIAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLRDIAlarm.setStatus(
        "current"
    )

h3cPosPRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 6)
)
h3cPosPRDIAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosPRDIAlarm.setStatus(
        "current"
    )

h3cPosPAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 7)
)
h3cPosPAISAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosPAISAlarm.setStatus(
        "current"
    )

h3cPosLOPAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 8)
)
h3cPosLOPAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLOPAlarm.setStatus(
        "current"
    )

h3cPosSTIMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 9)
)
h3cPosSTIMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosSTIMAlarm.setStatus(
        "current"
    )

h3cPosPTIMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 10)
)
h3cPosPTIMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosPTIMAlarm.setStatus(
        "current"
    )

h3cPosPSLMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 11)
)
h3cPosPSLMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosPSLMAlarm.setStatus(
        "current"
    )

h3cPosLSDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 12)
)
h3cPosLSDAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLSDAlarm.setStatus(
        "current"
    )

h3cPosLSFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 13)
)
h3cPosLSFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosLSFAlarm.setStatus(
        "current"
    )

h3cPosNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 14)
)
h3cPosNormalAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h3cPosNormalAlarm.setStatus(
        "current"
    )

h3cPosB1TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 15)
)
h3cPosB1TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cPosB1TCAlarm.setStatus(
        "current"
    )

h3cPosB2TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 16)
)
h3cPosB2TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cPosB2TCAlarm.setStatus(
        "current"
    )

h3cPosB3TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 19, 2, 0, 17)
)
h3cPosB3TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cPosB3TCAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PPP-OVER-SONET-MIB",
    **{"h3cPos": h3cPos,
       "h3cPosMIBObjects": h3cPosMIBObjects,
       "h3cPosParamTable": h3cPosParamTable,
       "h3cPosParamTableEntry": h3cPosParamTableEntry,
       "h3cPosCRC": h3cPosCRC,
       "h3cPosMTU": h3cPosMTU,
       "h3cPosScramble": h3cPosScramble,
       "h3cPosClockSource": h3cPosClockSource,
       "h3cPosSdhFlagJ0": h3cPosSdhFlagJ0,
       "h3cPosSdhFlagJ1": h3cPosSdhFlagJ1,
       "h3cPosSonetFlagJ0": h3cPosSonetFlagJ0,
       "h3cPosSonetFlagJ1": h3cPosSonetFlagJ1,
       "h3cPosFlagC2": h3cPosFlagC2,
       "h3cPosFrameType": h3cPosFrameType,
       "h3cPosBindVlanId": h3cPosBindVlanId,
       "h3cPosEncapsulation": h3cPosEncapsulation,
       "h3cPoskeepaliveTimeout": h3cPoskeepaliveTimeout,
       "h3cPosBERthresholdSF": h3cPosBERthresholdSF,
       "h3cPosBERthresholdSD": h3cPosBERthresholdSD,
       "h3cPosB1Error": h3cPosB1Error,
       "h3cPosB2Error": h3cPosB2Error,
       "h3cPosB3Error": h3cPosB3Error,
       "h3cPosM1Error": h3cPosM1Error,
       "h3cPosG1Error": h3cPosG1Error,
       "h3cPosFlagJ0Type": h3cPosFlagJ0Type,
       "h3cPosFlagJ1Type": h3cPosFlagJ1Type,
       "h3cPosB1TCAThreshold": h3cPosB1TCAThreshold,
       "h3cPosB2TCAThreshold": h3cPosB2TCAThreshold,
       "h3cPosB3TCAThreshold": h3cPosB3TCAThreshold,
       "h3cPosB1TCAEnable": h3cPosB1TCAEnable,
       "h3cPosB2TCAEnable": h3cPosB2TCAEnable,
       "h3cPosB3TCAEnable": h3cPosB3TCAEnable,
       "h3cPosMIBNotificationsPrefix": h3cPosMIBNotificationsPrefix,
       "h3cPosMIBNotifications": h3cPosMIBNotifications,
       "h3cPosLOSAlarm": h3cPosLOSAlarm,
       "h3cPosLOFAlarm": h3cPosLOFAlarm,
       "h3cPosOOFAlarm": h3cPosOOFAlarm,
       "h3cPosLAISAlarm": h3cPosLAISAlarm,
       "h3cPosLRDIAlarm": h3cPosLRDIAlarm,
       "h3cPosPRDIAlarm": h3cPosPRDIAlarm,
       "h3cPosPAISAlarm": h3cPosPAISAlarm,
       "h3cPosLOPAlarm": h3cPosLOPAlarm,
       "h3cPosSTIMAlarm": h3cPosSTIMAlarm,
       "h3cPosPTIMAlarm": h3cPosPTIMAlarm,
       "h3cPosPSLMAlarm": h3cPosPSLMAlarm,
       "h3cPosLSDAlarm": h3cPosLSDAlarm,
       "h3cPosLSFAlarm": h3cPosLSFAlarm,
       "h3cPosNormalAlarm": h3cPosNormalAlarm,
       "h3cPosB1TCAlarm": h3cPosB1TCAlarm,
       "h3cPosB2TCAlarm": h3cPosB2TCAlarm,
       "h3cPosB3TCAlarm": h3cPosB3TCAlarm}
)
