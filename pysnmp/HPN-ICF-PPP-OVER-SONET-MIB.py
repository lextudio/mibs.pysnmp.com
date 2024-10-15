# SNMP MIB module (HPN-ICF-PPP-OVER-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PPP-OVER-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:31 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfPos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19)
)
hpnicfPos.setRevisions(
        ("2013-10-10 17:00",
         "2010-05-19 17:00",
         "2007-07-19 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPosMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfPosMIBObjects = _HpnicfPosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1)
)
_HpnicfPosParamTable_Object = MibTable
hpnicfPosParamTable = _HpnicfPosParamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfPosParamTable.setStatus("current")
_HpnicfPosParamTableEntry_Object = MibTableRow
hpnicfPosParamTableEntry = _HpnicfPosParamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1)
)
hpnicfPosParamTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPosParamTableEntry.setStatus("current")


class _HpnicfPosCRC_Type(Integer32):
    """Custom type hpnicfPosCRC based on Integer32"""
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


_HpnicfPosCRC_Type.__name__ = "Integer32"
_HpnicfPosCRC_Object = MibTableColumn
hpnicfPosCRC = _HpnicfPosCRC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 1),
    _HpnicfPosCRC_Type()
)
hpnicfPosCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosCRC.setStatus("current")
_HpnicfPosMTU_Type = Integer32
_HpnicfPosMTU_Object = MibTableColumn
hpnicfPosMTU = _HpnicfPosMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 2),
    _HpnicfPosMTU_Type()
)
hpnicfPosMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosMTU.setStatus("current")


class _HpnicfPosScramble_Type(TruthValue):
    """Custom type hpnicfPosScramble based on TruthValue"""


_HpnicfPosScramble_Object = MibTableColumn
hpnicfPosScramble = _HpnicfPosScramble_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 3),
    _HpnicfPosScramble_Type()
)
hpnicfPosScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosScramble.setStatus("current")


class _HpnicfPosClockSource_Type(Integer32):
    """Custom type hpnicfPosClockSource based on Integer32"""
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


_HpnicfPosClockSource_Type.__name__ = "Integer32"
_HpnicfPosClockSource_Object = MibTableColumn
hpnicfPosClockSource = _HpnicfPosClockSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 4),
    _HpnicfPosClockSource_Type()
)
hpnicfPosClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosClockSource.setStatus("current")


class _HpnicfPosSdhFlagJ0_Type(DisplayString):
    """Custom type hpnicfPosSdhFlagJ0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpnicfPosSdhFlagJ0_Type.__name__ = "DisplayString"
_HpnicfPosSdhFlagJ0_Object = MibTableColumn
hpnicfPosSdhFlagJ0 = _HpnicfPosSdhFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 5),
    _HpnicfPosSdhFlagJ0_Type()
)
hpnicfPosSdhFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosSdhFlagJ0.setStatus("current")


class _HpnicfPosSdhFlagJ1_Type(DisplayString):
    """Custom type hpnicfPosSdhFlagJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpnicfPosSdhFlagJ1_Type.__name__ = "DisplayString"
_HpnicfPosSdhFlagJ1_Object = MibTableColumn
hpnicfPosSdhFlagJ1 = _HpnicfPosSdhFlagJ1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 6),
    _HpnicfPosSdhFlagJ1_Type()
)
hpnicfPosSdhFlagJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosSdhFlagJ1.setStatus("current")


class _HpnicfPosSonetFlagJ0_Type(Integer32):
    """Custom type hpnicfPosSonetFlagJ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfPosSonetFlagJ0_Type.__name__ = "Integer32"
_HpnicfPosSonetFlagJ0_Object = MibTableColumn
hpnicfPosSonetFlagJ0 = _HpnicfPosSonetFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 7),
    _HpnicfPosSonetFlagJ0_Type()
)
hpnicfPosSonetFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosSonetFlagJ0.setStatus("current")


class _HpnicfPosSonetFlagJ1_Type(DisplayString):
    """Custom type hpnicfPosSonetFlagJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_HpnicfPosSonetFlagJ1_Type.__name__ = "DisplayString"
_HpnicfPosSonetFlagJ1_Object = MibTableColumn
hpnicfPosSonetFlagJ1 = _HpnicfPosSonetFlagJ1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 8),
    _HpnicfPosSonetFlagJ1_Type()
)
hpnicfPosSonetFlagJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosSonetFlagJ1.setStatus("current")


class _HpnicfPosFlagC2_Type(Integer32):
    """Custom type hpnicfPosFlagC2 based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfPosFlagC2_Type.__name__ = "Integer32"
_HpnicfPosFlagC2_Object = MibTableColumn
hpnicfPosFlagC2 = _HpnicfPosFlagC2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 9),
    _HpnicfPosFlagC2_Type()
)
hpnicfPosFlagC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosFlagC2.setStatus("current")


class _HpnicfPosFrameType_Type(Integer32):
    """Custom type hpnicfPosFrameType based on Integer32"""
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


_HpnicfPosFrameType_Type.__name__ = "Integer32"
_HpnicfPosFrameType_Object = MibTableColumn
hpnicfPosFrameType = _HpnicfPosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 10),
    _HpnicfPosFrameType_Type()
)
hpnicfPosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosFrameType.setStatus("current")


class _HpnicfPosBindVlanId_Type(Integer32):
    """Custom type hpnicfPosBindVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HpnicfPosBindVlanId_Type.__name__ = "Integer32"
_HpnicfPosBindVlanId_Object = MibTableColumn
hpnicfPosBindVlanId = _HpnicfPosBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 11),
    _HpnicfPosBindVlanId_Type()
)
hpnicfPosBindVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosBindVlanId.setStatus("current")


class _HpnicfPosEncapsulation_Type(Integer32):
    """Custom type hpnicfPosEncapsulation based on Integer32"""
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


_HpnicfPosEncapsulation_Type.__name__ = "Integer32"
_HpnicfPosEncapsulation_Object = MibTableColumn
hpnicfPosEncapsulation = _HpnicfPosEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 12),
    _HpnicfPosEncapsulation_Type()
)
hpnicfPosEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosEncapsulation.setStatus("current")


class _HpnicfPoskeepaliveTimeout_Type(Integer32):
    """Custom type hpnicfPoskeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HpnicfPoskeepaliveTimeout_Type.__name__ = "Integer32"
_HpnicfPoskeepaliveTimeout_Object = MibTableColumn
hpnicfPoskeepaliveTimeout = _HpnicfPoskeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 13),
    _HpnicfPoskeepaliveTimeout_Type()
)
hpnicfPoskeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPoskeepaliveTimeout.setStatus("current")


class _HpnicfPosBERthresholdSF_Type(Integer32):
    """Custom type hpnicfPosBERthresholdSF based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HpnicfPosBERthresholdSF_Type.__name__ = "Integer32"
_HpnicfPosBERthresholdSF_Object = MibTableColumn
hpnicfPosBERthresholdSF = _HpnicfPosBERthresholdSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 14),
    _HpnicfPosBERthresholdSF_Type()
)
hpnicfPosBERthresholdSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosBERthresholdSF.setStatus("current")


class _HpnicfPosBERthresholdSD_Type(Integer32):
    """Custom type hpnicfPosBERthresholdSD based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HpnicfPosBERthresholdSD_Type.__name__ = "Integer32"
_HpnicfPosBERthresholdSD_Object = MibTableColumn
hpnicfPosBERthresholdSD = _HpnicfPosBERthresholdSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 15),
    _HpnicfPosBERthresholdSD_Type()
)
hpnicfPosBERthresholdSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosBERthresholdSD.setStatus("current")
_HpnicfPosB1Error_Type = Counter64
_HpnicfPosB1Error_Object = MibTableColumn
hpnicfPosB1Error = _HpnicfPosB1Error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 16),
    _HpnicfPosB1Error_Type()
)
hpnicfPosB1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosB1Error.setStatus("current")
_HpnicfPosB2Error_Type = Counter64
_HpnicfPosB2Error_Object = MibTableColumn
hpnicfPosB2Error = _HpnicfPosB2Error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 17),
    _HpnicfPosB2Error_Type()
)
hpnicfPosB2Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosB2Error.setStatus("current")
_HpnicfPosB3Error_Type = Counter64
_HpnicfPosB3Error_Object = MibTableColumn
hpnicfPosB3Error = _HpnicfPosB3Error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 18),
    _HpnicfPosB3Error_Type()
)
hpnicfPosB3Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosB3Error.setStatus("current")
_HpnicfPosM1Error_Type = Counter64
_HpnicfPosM1Error_Object = MibTableColumn
hpnicfPosM1Error = _HpnicfPosM1Error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 19),
    _HpnicfPosM1Error_Type()
)
hpnicfPosM1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosM1Error.setStatus("current")
_HpnicfPosG1Error_Type = Counter64
_HpnicfPosG1Error_Object = MibTableColumn
hpnicfPosG1Error = _HpnicfPosG1Error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 20),
    _HpnicfPosG1Error_Type()
)
hpnicfPosG1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosG1Error.setStatus("current")


class _HpnicfPosFlagJ0Type_Type(Integer32):
    """Custom type hpnicfPosFlagJ0Type based on Integer32"""
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


_HpnicfPosFlagJ0Type_Type.__name__ = "Integer32"
_HpnicfPosFlagJ0Type_Object = MibTableColumn
hpnicfPosFlagJ0Type = _HpnicfPosFlagJ0Type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 21),
    _HpnicfPosFlagJ0Type_Type()
)
hpnicfPosFlagJ0Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosFlagJ0Type.setStatus("current")


class _HpnicfPosFlagJ1Type_Type(Integer32):
    """Custom type hpnicfPosFlagJ1Type based on Integer32"""
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


_HpnicfPosFlagJ1Type_Type.__name__ = "Integer32"
_HpnicfPosFlagJ1Type_Object = MibTableColumn
hpnicfPosFlagJ1Type = _HpnicfPosFlagJ1Type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 22),
    _HpnicfPosFlagJ1Type_Type()
)
hpnicfPosFlagJ1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosFlagJ1Type.setStatus("current")


class _HpnicfPosB1TCAThreshold_Type(Integer32):
    """Custom type hpnicfPosB1TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HpnicfPosB1TCAThreshold_Type.__name__ = "Integer32"
_HpnicfPosB1TCAThreshold_Object = MibTableColumn
hpnicfPosB1TCAThreshold = _HpnicfPosB1TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 23),
    _HpnicfPosB1TCAThreshold_Type()
)
hpnicfPosB1TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosB1TCAThreshold.setStatus("current")


class _HpnicfPosB2TCAThreshold_Type(Integer32):
    """Custom type hpnicfPosB2TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HpnicfPosB2TCAThreshold_Type.__name__ = "Integer32"
_HpnicfPosB2TCAThreshold_Object = MibTableColumn
hpnicfPosB2TCAThreshold = _HpnicfPosB2TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 24),
    _HpnicfPosB2TCAThreshold_Type()
)
hpnicfPosB2TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosB2TCAThreshold.setStatus("current")


class _HpnicfPosB3TCAThreshold_Type(Integer32):
    """Custom type hpnicfPosB3TCAThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HpnicfPosB3TCAThreshold_Type.__name__ = "Integer32"
_HpnicfPosB3TCAThreshold_Object = MibTableColumn
hpnicfPosB3TCAThreshold = _HpnicfPosB3TCAThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 25),
    _HpnicfPosB3TCAThreshold_Type()
)
hpnicfPosB3TCAThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosB3TCAThreshold.setStatus("current")


class _HpnicfPosB1TCAEnable_Type(Integer32):
    """Custom type hpnicfPosB1TCAEnable based on Integer32"""
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


_HpnicfPosB1TCAEnable_Type.__name__ = "Integer32"
_HpnicfPosB1TCAEnable_Object = MibTableColumn
hpnicfPosB1TCAEnable = _HpnicfPosB1TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 26),
    _HpnicfPosB1TCAEnable_Type()
)
hpnicfPosB1TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosB1TCAEnable.setStatus("current")


class _HpnicfPosB2TCAEnable_Type(Integer32):
    """Custom type hpnicfPosB2TCAEnable based on Integer32"""
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


_HpnicfPosB2TCAEnable_Type.__name__ = "Integer32"
_HpnicfPosB2TCAEnable_Object = MibTableColumn
hpnicfPosB2TCAEnable = _HpnicfPosB2TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 27),
    _HpnicfPosB2TCAEnable_Type()
)
hpnicfPosB2TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosB2TCAEnable.setStatus("current")


class _HpnicfPosB3TCAEnable_Type(Integer32):
    """Custom type hpnicfPosB3TCAEnable based on Integer32"""
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


_HpnicfPosB3TCAEnable_Type.__name__ = "Integer32"
_HpnicfPosB3TCAEnable_Object = MibTableColumn
hpnicfPosB3TCAEnable = _HpnicfPosB3TCAEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 28),
    _HpnicfPosB3TCAEnable_Type()
)
hpnicfPosB3TCAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosB3TCAEnable.setStatus("current")
_HpnicfPosMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpnicfPosMIBNotificationsPrefix = _HpnicfPosMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2)
)
_HpnicfPosMIBNotifications_ObjectIdentity = ObjectIdentity
hpnicfPosMIBNotifications = _HpnicfPosMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfPosLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 1)
)
hpnicfPosLOSAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLOSAlarm.setStatus(
        "current"
    )

hpnicfPosLOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 2)
)
hpnicfPosLOFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLOFAlarm.setStatus(
        "current"
    )

hpnicfPosOOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 3)
)
hpnicfPosOOFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosOOFAlarm.setStatus(
        "current"
    )

hpnicfPosLAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 4)
)
hpnicfPosLAISAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLAISAlarm.setStatus(
        "current"
    )

hpnicfPosLRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 5)
)
hpnicfPosLRDIAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLRDIAlarm.setStatus(
        "current"
    )

hpnicfPosPRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 6)
)
hpnicfPosPRDIAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosPRDIAlarm.setStatus(
        "current"
    )

hpnicfPosPAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 7)
)
hpnicfPosPAISAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosPAISAlarm.setStatus(
        "current"
    )

hpnicfPosLOPAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 8)
)
hpnicfPosLOPAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLOPAlarm.setStatus(
        "current"
    )

hpnicfPosSTIMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 9)
)
hpnicfPosSTIMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosSTIMAlarm.setStatus(
        "current"
    )

hpnicfPosPTIMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 10)
)
hpnicfPosPTIMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosPTIMAlarm.setStatus(
        "current"
    )

hpnicfPosPSLMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 11)
)
hpnicfPosPSLMAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosPSLMAlarm.setStatus(
        "current"
    )

hpnicfPosLSDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 12)
)
hpnicfPosLSDAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLSDAlarm.setStatus(
        "current"
    )

hpnicfPosLSFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 13)
)
hpnicfPosLSFAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosLSFAlarm.setStatus(
        "current"
    )

hpnicfPosNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 14)
)
hpnicfPosNormalAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfPosNormalAlarm.setStatus(
        "current"
    )

hpnicfPosB1TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 15)
)
hpnicfPosB1TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPosB1TCAlarm.setStatus(
        "current"
    )

hpnicfPosB2TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 16)
)
hpnicfPosB2TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPosB2TCAlarm.setStatus(
        "current"
    )

hpnicfPosB3TCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 17)
)
hpnicfPosB3TCAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPosB3TCAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PPP-OVER-SONET-MIB",
    **{"hpnicfPos": hpnicfPos,
       "hpnicfPosMIBObjects": hpnicfPosMIBObjects,
       "hpnicfPosParamTable": hpnicfPosParamTable,
       "hpnicfPosParamTableEntry": hpnicfPosParamTableEntry,
       "hpnicfPosCRC": hpnicfPosCRC,
       "hpnicfPosMTU": hpnicfPosMTU,
       "hpnicfPosScramble": hpnicfPosScramble,
       "hpnicfPosClockSource": hpnicfPosClockSource,
       "hpnicfPosSdhFlagJ0": hpnicfPosSdhFlagJ0,
       "hpnicfPosSdhFlagJ1": hpnicfPosSdhFlagJ1,
       "hpnicfPosSonetFlagJ0": hpnicfPosSonetFlagJ0,
       "hpnicfPosSonetFlagJ1": hpnicfPosSonetFlagJ1,
       "hpnicfPosFlagC2": hpnicfPosFlagC2,
       "hpnicfPosFrameType": hpnicfPosFrameType,
       "hpnicfPosBindVlanId": hpnicfPosBindVlanId,
       "hpnicfPosEncapsulation": hpnicfPosEncapsulation,
       "hpnicfPoskeepaliveTimeout": hpnicfPoskeepaliveTimeout,
       "hpnicfPosBERthresholdSF": hpnicfPosBERthresholdSF,
       "hpnicfPosBERthresholdSD": hpnicfPosBERthresholdSD,
       "hpnicfPosB1Error": hpnicfPosB1Error,
       "hpnicfPosB2Error": hpnicfPosB2Error,
       "hpnicfPosB3Error": hpnicfPosB3Error,
       "hpnicfPosM1Error": hpnicfPosM1Error,
       "hpnicfPosG1Error": hpnicfPosG1Error,
       "hpnicfPosFlagJ0Type": hpnicfPosFlagJ0Type,
       "hpnicfPosFlagJ1Type": hpnicfPosFlagJ1Type,
       "hpnicfPosB1TCAThreshold": hpnicfPosB1TCAThreshold,
       "hpnicfPosB2TCAThreshold": hpnicfPosB2TCAThreshold,
       "hpnicfPosB3TCAThreshold": hpnicfPosB3TCAThreshold,
       "hpnicfPosB1TCAEnable": hpnicfPosB1TCAEnable,
       "hpnicfPosB2TCAEnable": hpnicfPosB2TCAEnable,
       "hpnicfPosB3TCAEnable": hpnicfPosB3TCAEnable,
       "hpnicfPosMIBNotificationsPrefix": hpnicfPosMIBNotificationsPrefix,
       "hpnicfPosMIBNotifications": hpnicfPosMIBNotifications,
       "hpnicfPosLOSAlarm": hpnicfPosLOSAlarm,
       "hpnicfPosLOFAlarm": hpnicfPosLOFAlarm,
       "hpnicfPosOOFAlarm": hpnicfPosOOFAlarm,
       "hpnicfPosLAISAlarm": hpnicfPosLAISAlarm,
       "hpnicfPosLRDIAlarm": hpnicfPosLRDIAlarm,
       "hpnicfPosPRDIAlarm": hpnicfPosPRDIAlarm,
       "hpnicfPosPAISAlarm": hpnicfPosPAISAlarm,
       "hpnicfPosLOPAlarm": hpnicfPosLOPAlarm,
       "hpnicfPosSTIMAlarm": hpnicfPosSTIMAlarm,
       "hpnicfPosPTIMAlarm": hpnicfPosPTIMAlarm,
       "hpnicfPosPSLMAlarm": hpnicfPosPSLMAlarm,
       "hpnicfPosLSDAlarm": hpnicfPosLSDAlarm,
       "hpnicfPosLSFAlarm": hpnicfPosLSFAlarm,
       "hpnicfPosNormalAlarm": hpnicfPosNormalAlarm,
       "hpnicfPosB1TCAlarm": hpnicfPosB1TCAlarm,
       "hpnicfPosB2TCAlarm": hpnicfPosB2TCAlarm,
       "hpnicfPosB3TCAlarm": hpnicfPosB3TCAlarm}
)
