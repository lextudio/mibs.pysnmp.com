# SNMP MIB module (CADANT-CMTS-DOWNCHANNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-DOWNCHANNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:27 2024
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

(TenthdBmV,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cadDownchannelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2)
)
cadDownchannelMib.setRevisions(
        ("2015-10-27 00:00",
         "2015-10-07 00:00",
         "2015-09-30 00:00",
         "2015-09-08 00:00",
         "2015-08-19 00:00",
         "2015-08-12 00:00",
         "2015-06-23 00:00",
         "2015-05-01 00:00",
         "2015-04-27 00:00",
         "2015-03-04 00:00",
         "2015-02-18 00:00",
         "2015-02-17 00:00",
         "2015-02-13 00:00",
         "2015-02-06 00:00",
         "2015-01-16 00:00",
         "2014-11-26 00:00",
         "2014-11-17 00:00",
         "2014-05-20 00:00",
         "2014-04-03 00:00",
         "2014-01-16 00:00",
         "2013-10-13 00:00",
         "2013-03-15 00:00",
         "2013-02-26 00:00",
         "2013-01-14 00:00",
         "2012-10-17 00:00",
         "2012-10-15 00:00",
         "2011-09-27 00:00",
         "2011-08-30 00:00",
         "2010-06-10 00:00",
         "2010-05-03 00:00",
         "2010-04-01 00:00",
         "2009-12-16 00:00",
         "2008-04-03 00:00",
         "2007-10-09 00:00",
         "2007-09-28 00:00",
         "2007-02-07 00:00",
         "2007-01-22 00:00",
         "2006-11-01 00:00",
         "2006-08-30 00:00",
         "2006-08-28 00:00",
         "2006-02-24 00:00",
         "2005-06-21 00:00",
         "2004-12-03 00:00",
         "2004-03-04 00:00",
         "2003-07-03 00:00",
         "2002-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OfdmProfileId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
        ValueRangeConstraint(256, 256),
    )



class CerOfdmModType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
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
        *(("qam0", 0),
          ("qam1024", 10),
          ("qam128", 7),
          ("qam16", 4),
          ("qam16384", 14),
          ("qam2048", 11),
          ("qam256", 8),
          ("qam4096", 12),
          ("qam512", 9),
          ("qam64", 6),
          ("qam8192", 13),
          ("qpsk", 2))
    )



class CerOfdmModBitsType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CadIfDownstreamChannelTable_Object = MibTable
cadIfDownstreamChannelTable = _CadIfDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    cadIfDownstreamChannelTable.setStatus("current")
_CadIfDownstreamChannelEntry_Object = MibTableRow
cadIfDownstreamChannelEntry = _CadIfDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1)
)
cadIfDownstreamChannelEntry.setIndexNames(
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDownChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadIfDownstreamChannelEntry.setStatus("current")


class _CadIfDownChannelId_Type(Integer32):
    """Custom type cadIfDownChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CadIfDownChannelId_Type.__name__ = "Integer32"
_CadIfDownChannelId_Object = MibTableColumn
cadIfDownChannelId = _CadIfDownChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 1),
    _CadIfDownChannelId_Type()
)
cadIfDownChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDownChannelId.setStatus("current")


class _CadIfDownChannelFrequency_Type(Integer32):
    """Custom type cadIfDownChannelFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CadIfDownChannelFrequency_Type.__name__ = "Integer32"
_CadIfDownChannelFrequency_Object = MibTableColumn
cadIfDownChannelFrequency = _CadIfDownChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 2),
    _CadIfDownChannelFrequency_Type()
)
cadIfDownChannelFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelFrequency.setUnits("hertz")


class _CadIfDownChannelWidth_Type(Integer32):
    """Custom type cadIfDownChannelWidth based on Integer32"""
    defaultValue = 6000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_CadIfDownChannelWidth_Type.__name__ = "Integer32"
_CadIfDownChannelWidth_Object = MibTableColumn
cadIfDownChannelWidth = _CadIfDownChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 3),
    _CadIfDownChannelWidth_Type()
)
cadIfDownChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelWidth.setUnits("hertz")


class _CadIfDownChannelModulation_Type(Integer32):
    """Custom type cadIfDownChannelModulation based on Integer32"""
    defaultValue = 4

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
        *(("other", 2),
          ("qam256", 4),
          ("qam64", 3),
          ("unknown", 1))
    )


_CadIfDownChannelModulation_Type.__name__ = "Integer32"
_CadIfDownChannelModulation_Object = MibTableColumn
cadIfDownChannelModulation = _CadIfDownChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 4),
    _CadIfDownChannelModulation_Type()
)
cadIfDownChannelModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelModulation.setStatus("current")


class _CadIfDownChannelInterleave_Type(Integer32):
    """Custom type cadIfDownChannelInterleave based on Integer32"""
    defaultValue = 5

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("taps128Increment1", 7),
          ("taps128increment2", 9),
          ("taps128increment3", 10),
          ("taps128increment4", 11),
          ("taps128increment5", 12),
          ("taps128increment6", 13),
          ("taps128increment7", 14),
          ("taps128increment8", 15),
          ("taps12increment17", 8),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps8Increment16", 3),
          ("unknown", 1))
    )


_CadIfDownChannelInterleave_Type.__name__ = "Integer32"
_CadIfDownChannelInterleave_Object = MibTableColumn
cadIfDownChannelInterleave = _CadIfDownChannelInterleave_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 5),
    _CadIfDownChannelInterleave_Type()
)
cadIfDownChannelInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelInterleave.setStatus("current")


class _CadIfDownChannelPower_Type(TenthdBmV):
    """Custom type cadIfDownChannelPower based on TenthdBmV"""
    defaultValue = 380

    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(250, 600),
    )


_CadIfDownChannelPower_Type.__name__ = "TenthdBmV"
_CadIfDownChannelPower_Object = MibTableColumn
cadIfDownChannelPower = _CadIfDownChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 6),
    _CadIfDownChannelPower_Type()
)
cadIfDownChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPower.setUnits("dBmV")


class _CadIfDownChannelPowerFineAdj_Type(Integer32):
    """Custom type cadIfDownChannelPowerFineAdj based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 0),
    )


_CadIfDownChannelPowerFineAdj_Type.__name__ = "Integer32"
_CadIfDownChannelPowerFineAdj_Object = MibTableColumn
cadIfDownChannelPowerFineAdj = _CadIfDownChannelPowerFineAdj_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 7),
    _CadIfDownChannelPowerFineAdj_Type()
)
cadIfDownChannelPowerFineAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPowerFineAdj.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPowerFineAdj.setUnits("Steps")
_CadIfCmtsCardNumber_Type = CardId
_CadIfCmtsCardNumber_Object = MibTableColumn
cadIfCmtsCardNumber = _CadIfCmtsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 19),
    _CadIfCmtsCardNumber_Type()
)
cadIfCmtsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCardNumber.setStatus("current")


class _CadIfDownChannelCACL1Threshold_Type(Integer32):
    """Custom type cadIfDownChannelCACL1Threshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadIfDownChannelCACL1Threshold_Type.__name__ = "Integer32"
_CadIfDownChannelCACL1Threshold_Object = MibTableColumn
cadIfDownChannelCACL1Threshold = _CadIfDownChannelCACL1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 21),
    _CadIfDownChannelCACL1Threshold_Type()
)
cadIfDownChannelCACL1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelCACL1Threshold.setStatus("current")


class _CadIfDownChannelCACL2Threshold_Type(Integer32):
    """Custom type cadIfDownChannelCACL2Threshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadIfDownChannelCACL2Threshold_Type.__name__ = "Integer32"
_CadIfDownChannelCACL2Threshold_Object = MibTableColumn
cadIfDownChannelCACL2Threshold = _CadIfDownChannelCACL2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 22),
    _CadIfDownChannelCACL2Threshold_Type()
)
cadIfDownChannelCACL2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelCACL2Threshold.setStatus("current")


class _CadIfDownChannelCACL3Threshold_Type(Integer32):
    """Custom type cadIfDownChannelCACL3Threshold based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadIfDownChannelCACL3Threshold_Type.__name__ = "Integer32"
_CadIfDownChannelCACL3Threshold_Object = MibTableColumn
cadIfDownChannelCACL3Threshold = _CadIfDownChannelCACL3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 23),
    _CadIfDownChannelCACL3Threshold_Type()
)
cadIfDownChannelCACL3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelCACL3Threshold.setStatus("current")


class _CadIfDownChannelMaxRoundTripDelay_Type(Integer32):
    """Custom type cadIfDownChannelMaxRoundTripDelay based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1600),
    )


_CadIfDownChannelMaxRoundTripDelay_Type.__name__ = "Integer32"
_CadIfDownChannelMaxRoundTripDelay_Object = MibTableColumn
cadIfDownChannelMaxRoundTripDelay = _CadIfDownChannelMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 24),
    _CadIfDownChannelMaxRoundTripDelay_Type()
)
cadIfDownChannelMaxRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelMaxRoundTripDelay.setUnits("Microseconds")


class _CadIfDownChannelAnnex_Type(Integer32):
    """Custom type cadIfDownChannelAnnex based on Integer32"""
    defaultValue = 4

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
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_CadIfDownChannelAnnex_Type.__name__ = "Integer32"
_CadIfDownChannelAnnex_Object = MibTableColumn
cadIfDownChannelAnnex = _CadIfDownChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 26),
    _CadIfDownChannelAnnex_Type()
)
cadIfDownChannelAnnex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelAnnex.setStatus("current")


class _CadIfDownChannelPCNormAllowedUsage_Type(Integer32):
    """Custom type cadIfDownChannelPCNormAllowedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDownChannelPCNormAllowedUsage_Type.__name__ = "Integer32"
_CadIfDownChannelPCNormAllowedUsage_Object = MibTableColumn
cadIfDownChannelPCNormAllowedUsage = _CadIfDownChannelPCNormAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 27),
    _CadIfDownChannelPCNormAllowedUsage_Type()
)
cadIfDownChannelPCNormAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPCNormAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPCNormAllowedUsage.setUnits("percent")


class _CadIfDownChannelPCNormResUsage_Type(Integer32):
    """Custom type cadIfDownChannelPCNormResUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDownChannelPCNormResUsage_Type.__name__ = "Integer32"
_CadIfDownChannelPCNormResUsage_Object = MibTableColumn
cadIfDownChannelPCNormResUsage = _CadIfDownChannelPCNormResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 28),
    _CadIfDownChannelPCNormResUsage_Type()
)
cadIfDownChannelPCNormResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPCNormResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPCNormResUsage.setUnits("percent")


class _CadIfDownChannelPCEmerAllowedUsage_Type(Integer32):
    """Custom type cadIfDownChannelPCEmerAllowedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDownChannelPCEmerAllowedUsage_Type.__name__ = "Integer32"
_CadIfDownChannelPCEmerAllowedUsage_Object = MibTableColumn
cadIfDownChannelPCEmerAllowedUsage = _CadIfDownChannelPCEmerAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 29),
    _CadIfDownChannelPCEmerAllowedUsage_Type()
)
cadIfDownChannelPCEmerAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPCEmerAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPCEmerAllowedUsage.setUnits("percent")


class _CadIfDownChannelPCEmerResUsage_Type(Integer32):
    """Custom type cadIfDownChannelPCEmerResUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDownChannelPCEmerResUsage_Type.__name__ = "Integer32"
_CadIfDownChannelPCEmerResUsage_Object = MibTableColumn
cadIfDownChannelPCEmerResUsage = _CadIfDownChannelPCEmerResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 30),
    _CadIfDownChannelPCEmerResUsage_Type()
)
cadIfDownChannelPCEmerResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPCEmerResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPCEmerResUsage.setUnits("percent")


class _CadIfDownChannelPCTotalAllowedUsage_Type(Integer32):
    """Custom type cadIfDownChannelPCTotalAllowedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDownChannelPCTotalAllowedUsage_Type.__name__ = "Integer32"
_CadIfDownChannelPCTotalAllowedUsage_Object = MibTableColumn
cadIfDownChannelPCTotalAllowedUsage = _CadIfDownChannelPCTotalAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 31),
    _CadIfDownChannelPCTotalAllowedUsage_Type()
)
cadIfDownChannelPCTotalAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPCTotalAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDownChannelPCTotalAllowedUsage.setUnits("percent")
_CadIfDownChannelPCPreemptionAllowed_Type = TruthValue
_CadIfDownChannelPCPreemptionAllowed_Object = MibTableColumn
cadIfDownChannelPCPreemptionAllowed = _CadIfDownChannelPCPreemptionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 32),
    _CadIfDownChannelPCPreemptionAllowed_Type()
)
cadIfDownChannelPCPreemptionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPCPreemptionAllowed.setStatus("current")
_CadIfDownChannelIfIndex_Type = InterfaceIndex
_CadIfDownChannelIfIndex_Object = MibTableColumn
cadIfDownChannelIfIndex = _CadIfDownChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 37),
    _CadIfDownChannelIfIndex_Type()
)
cadIfDownChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDownChannelIfIndex.setStatus("current")


class _CadIfDownChannelPrimaryCapable_Type(TruthValue):
    """Custom type cadIfDownChannelPrimaryCapable based on TruthValue"""


_CadIfDownChannelPrimaryCapable_Object = MibTableColumn
cadIfDownChannelPrimaryCapable = _CadIfDownChannelPrimaryCapable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 38),
    _CadIfDownChannelPrimaryCapable_Type()
)
cadIfDownChannelPrimaryCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownChannelPrimaryCapable.setStatus("current")


class _CadIfDownSpectralInversion_Type(TruthValue):
    """Custom type cadIfDownSpectralInversion based on TruthValue"""


_CadIfDownSpectralInversion_Object = MibTableColumn
cadIfDownSpectralInversion = _CadIfDownSpectralInversion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 39),
    _CadIfDownSpectralInversion_Type()
)
cadIfDownSpectralInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDownSpectralInversion.setStatus("current")
_CadDownChannelParams_ObjectIdentity = ObjectIdentity
cadDownChannelParams = _CadDownChannelParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2)
)


class _CadDownChannelMaxFrequency_Type(Integer32):
    """Custom type cadDownChannelMaxFrequency based on Integer32"""
    defaultValue = 867000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(858000000, 858000000),
        ValueRangeConstraint(867000000, 867000000),
        ValueRangeConstraint(999000000, 999000000),
    )


_CadDownChannelMaxFrequency_Type.__name__ = "Integer32"
_CadDownChannelMaxFrequency_Object = MibScalar
cadDownChannelMaxFrequency = _CadDownChannelMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 1),
    _CadDownChannelMaxFrequency_Type()
)
cadDownChannelMaxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelMaxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadDownChannelMaxFrequency.setUnits("hertz")


class _CadDownChannelMinFrequency_Type(Integer32):
    """Custom type cadDownChannelMinFrequency based on Integer32"""
    defaultValue = 91000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57000000, 57000000),
        ValueRangeConstraint(85000000, 85000000),
        ValueRangeConstraint(91000000, 91000000),
        ValueRangeConstraint(112000000, 112000000),
    )


_CadDownChannelMinFrequency_Type.__name__ = "Integer32"
_CadDownChannelMinFrequency_Object = MibScalar
cadDownChannelMinFrequency = _CadDownChannelMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 2),
    _CadDownChannelMinFrequency_Type()
)
cadDownChannelMinFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelMinFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadDownChannelMinFrequency.setUnits("hertz")


class _CadDownChannelAgcEnable_Type(TruthValue):
    """Custom type cadDownChannelAgcEnable based on TruthValue"""


_CadDownChannelAgcEnable_Object = MibScalar
cadDownChannelAgcEnable = _CadDownChannelAgcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 3),
    _CadDownChannelAgcEnable_Type()
)
cadDownChannelAgcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelAgcEnable.setStatus("current")


class _CadDownChannelOorRecoveryEnable_Type(TruthValue):
    """Custom type cadDownChannelOorRecoveryEnable based on TruthValue"""


_CadDownChannelOorRecoveryEnable_Object = MibScalar
cadDownChannelOorRecoveryEnable = _CadDownChannelOorRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 4),
    _CadDownChannelOorRecoveryEnable_Type()
)
cadDownChannelOorRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelOorRecoveryEnable.setStatus("current")


class _CadDsOfdmOcdDpdPlcInterval_Type(Integer32):
    """Custom type cadDsOfdmOcdDpdPlcInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 250),
    )


_CadDsOfdmOcdDpdPlcInterval_Type.__name__ = "Integer32"
_CadDsOfdmOcdDpdPlcInterval_Object = MibScalar
cadDsOfdmOcdDpdPlcInterval = _CadDsOfdmOcdDpdPlcInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 5),
    _CadDsOfdmOcdDpdPlcInterval_Type()
)
cadDsOfdmOcdDpdPlcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDsOfdmOcdDpdPlcInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadDsOfdmOcdDpdPlcInterval.setUnits("milliseconds")


class _CadDsOfdmDpdProfAInterval_Type(Integer32):
    """Custom type cadDsOfdmDpdProfAInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 600),
    )


_CadDsOfdmDpdProfAInterval_Type.__name__ = "Integer32"
_CadDsOfdmDpdProfAInterval_Object = MibScalar
cadDsOfdmDpdProfAInterval = _CadDsOfdmDpdProfAInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 6),
    _CadDsOfdmDpdProfAInterval_Type()
)
cadDsOfdmDpdProfAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDsOfdmDpdProfAInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadDsOfdmDpdProfAInterval.setUnits("milliseconds")


class _CadDownChannelLsredMinThresh_Type(Integer32):
    """Custom type cadDownChannelLsredMinThresh based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_CadDownChannelLsredMinThresh_Type.__name__ = "Integer32"
_CadDownChannelLsredMinThresh_Object = MibScalar
cadDownChannelLsredMinThresh = _CadDownChannelLsredMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 7),
    _CadDownChannelLsredMinThresh_Type()
)
cadDownChannelLsredMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelLsredMinThresh.setStatus("current")
if mibBuilder.loadTexts:
    cadDownChannelLsredMinThresh.setUnits("milliseconds")


class _CadDownChannelLsredMaxThresh_Type(Integer32):
    """Custom type cadDownChannelLsredMaxThresh based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2500),
    )


_CadDownChannelLsredMaxThresh_Type.__name__ = "Integer32"
_CadDownChannelLsredMaxThresh_Object = MibScalar
cadDownChannelLsredMaxThresh = _CadDownChannelLsredMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 8),
    _CadDownChannelLsredMaxThresh_Type()
)
cadDownChannelLsredMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelLsredMaxThresh.setStatus("current")
if mibBuilder.loadTexts:
    cadDownChannelLsredMaxThresh.setUnits("milliseconds")


class _CadDownChannelLsredMaxProb_Type(Integer32):
    """Custom type cadDownChannelLsredMaxProb based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadDownChannelLsredMaxProb_Type.__name__ = "Integer32"
_CadDownChannelLsredMaxProb_Object = MibScalar
cadDownChannelLsredMaxProb = _CadDownChannelLsredMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 9),
    _CadDownChannelLsredMaxProb_Type()
)
cadDownChannelLsredMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelLsredMaxProb.setStatus("current")
if mibBuilder.loadTexts:
    cadDownChannelLsredMaxProb.setUnits("0.01%")


class _CadDownChannelVoiceShaping_Type(TruthValue):
    """Custom type cadDownChannelVoiceShaping based on TruthValue"""


_CadDownChannelVoiceShaping_Object = MibScalar
cadDownChannelVoiceShaping = _CadDownChannelVoiceShaping_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 10),
    _CadDownChannelVoiceShaping_Type()
)
cadDownChannelVoiceShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDownChannelVoiceShaping.setStatus("current")
_CadIfDsOfdmPowerTable_Object = MibTable
cadIfDsOfdmPowerTable = _CadIfDsOfdmPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerTable.setStatus("current")
_CadIfDsOfdmPowerEntry_Object = MibTableRow
cadIfDsOfdmPowerEntry = _CadIfDsOfdmPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1)
)
cadIfDsOfdmPowerEntry.setIndexNames(
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmPowerIfIndex"),
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmPowerFrequency"),
)
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerEntry.setStatus("current")
_CadIfDsOfdmPowerIfIndex_Type = InterfaceIndex
_CadIfDsOfdmPowerIfIndex_Object = MibTableColumn
cadIfDsOfdmPowerIfIndex = _CadIfDsOfdmPowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 1),
    _CadIfDsOfdmPowerIfIndex_Type()
)
cadIfDsOfdmPowerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerIfIndex.setStatus("current")


class _CadIfDsOfdmPowerFrequency_Type(Integer32):
    """Custom type cadIfDsOfdmPowerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_CadIfDsOfdmPowerFrequency_Type.__name__ = "Integer32"
_CadIfDsOfdmPowerFrequency_Object = MibTableColumn
cadIfDsOfdmPowerFrequency = _CadIfDsOfdmPowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 2),
    _CadIfDsOfdmPowerFrequency_Type()
)
cadIfDsOfdmPowerFrequency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerFrequency.setUnits("MHz")


class _CadIfDsOfdmPowerFineAdjustment_Type(TenthdBmV):
    """Custom type cadIfDsOfdmPowerFineAdjustment based on TenthdBmV"""
    defaultValue = 0

    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 0),
    )


_CadIfDsOfdmPowerFineAdjustment_Type.__name__ = "TenthdBmV"
_CadIfDsOfdmPowerFineAdjustment_Object = MibTableColumn
cadIfDsOfdmPowerFineAdjustment = _CadIfDsOfdmPowerFineAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 3),
    _CadIfDsOfdmPowerFineAdjustment_Type()
)
cadIfDsOfdmPowerFineAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerFineAdjustment.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerFineAdjustment.setUnits("dBmVtenths")


class _CadIfDsOfdmPowerCurrLevel_Type(TenthdBmV):
    """Custom type cadIfDsOfdmPowerCurrLevel based on TenthdBmV"""
    defaultValue = 0


_CadIfDsOfdmPowerCurrLevel_Object = MibTableColumn
cadIfDsOfdmPowerCurrLevel = _CadIfDsOfdmPowerCurrLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 4),
    _CadIfDsOfdmPowerCurrLevel_Type()
)
cadIfDsOfdmPowerCurrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerCurrLevel.setStatus("current")


class _CadIfDsOfdmPowerMinLevel_Type(TenthdBmV):
    """Custom type cadIfDsOfdmPowerMinLevel based on TenthdBmV"""
    defaultValue = 0


_CadIfDsOfdmPowerMinLevel_Object = MibTableColumn
cadIfDsOfdmPowerMinLevel = _CadIfDsOfdmPowerMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 5),
    _CadIfDsOfdmPowerMinLevel_Type()
)
cadIfDsOfdmPowerMinLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerMinLevel.setStatus("current")


class _CadIfDsOfdmPowerMaxLevel_Type(TenthdBmV):
    """Custom type cadIfDsOfdmPowerMaxLevel based on TenthdBmV"""
    defaultValue = 0


_CadIfDsOfdmPowerMaxLevel_Object = MibTableColumn
cadIfDsOfdmPowerMaxLevel = _CadIfDsOfdmPowerMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 6),
    _CadIfDsOfdmPowerMaxLevel_Type()
)
cadIfDsOfdmPowerMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmPowerMaxLevel.setStatus("current")
_CadIfDsOfdmChlTable_Object = MibTable
cadIfDsOfdmChlTable = _CadIfDsOfdmChlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5)
)
if mibBuilder.loadTexts:
    cadIfDsOfdmChlTable.setStatus("current")
_CadIfDsOfdmChlEntry_Object = MibTableRow
cadIfDsOfdmChlEntry = _CadIfDsOfdmChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1)
)
cadIfDsOfdmChlEntry.setIndexNames(
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmChlIfIndex"),
)
if mibBuilder.loadTexts:
    cadIfDsOfdmChlEntry.setStatus("current")
_CadIfDsOfdmChlIfIndex_Type = InterfaceIndex
_CadIfDsOfdmChlIfIndex_Object = MibTableColumn
cadIfDsOfdmChlIfIndex = _CadIfDsOfdmChlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 1),
    _CadIfDsOfdmChlIfIndex_Type()
)
cadIfDsOfdmChlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlIfIndex.setStatus("current")


class _CadIfDsOfdmChlLowFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlLowFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(108000000, 1770000000),
    )


_CadIfDsOfdmChlLowFreq_Type.__name__ = "Integer32"
_CadIfDsOfdmChlLowFreq_Object = MibTableColumn
cadIfDsOfdmChlLowFreq = _CadIfDsOfdmChlLowFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 2),
    _CadIfDsOfdmChlLowFreq_Type()
)
cadIfDsOfdmChlLowFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlLowFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlLowFreq.setUnits("hertz")


class _CadIfDsOfdmChlHighFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlHighFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(132000000, 1794000000),
    )


_CadIfDsOfdmChlHighFreq_Type.__name__ = "Integer32"
_CadIfDsOfdmChlHighFreq_Object = MibTableColumn
cadIfDsOfdmChlHighFreq = _CadIfDsOfdmChlHighFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 3),
    _CadIfDsOfdmChlHighFreq_Type()
)
cadIfDsOfdmChlHighFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlHighFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlHighFreq.setUnits("hertz")


class _CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlPlcBlkLowSubcCentFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(108000000, 1788000000),
    )


_CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Type.__name__ = "Integer32"
_CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Object = MibTableColumn
cadIfDsOfdmChlPlcBlkLowSubcCentFreq = _CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 4),
    _CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Type()
)
cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setUnits("hertz")


class _CadIfDsOfdmChlCyclicPrefix_Type(Integer32):
    """Custom type cadIfDsOfdmChlCyclicPrefix based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(768, 768),
        ValueRangeConstraint(1024, 1024),
    )


_CadIfDsOfdmChlCyclicPrefix_Type.__name__ = "Integer32"
_CadIfDsOfdmChlCyclicPrefix_Object = MibTableColumn
cadIfDsOfdmChlCyclicPrefix = _CadIfDsOfdmChlCyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 5),
    _CadIfDsOfdmChlCyclicPrefix_Type()
)
cadIfDsOfdmChlCyclicPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlCyclicPrefix.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlCyclicPrefix.setUnits("samples")


class _CadIfDsOfdmChlRolloffPeriod_Type(Integer32):
    """Custom type cadIfDsOfdmChlRolloffPeriod based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(256, 256),
    )


_CadIfDsOfdmChlRolloffPeriod_Type.__name__ = "Integer32"
_CadIfDsOfdmChlRolloffPeriod_Object = MibTableColumn
cadIfDsOfdmChlRolloffPeriod = _CadIfDsOfdmChlRolloffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 6),
    _CadIfDsOfdmChlRolloffPeriod_Type()
)
cadIfDsOfdmChlRolloffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlRolloffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlRolloffPeriod.setUnits("samples")


class _CadIfDsOfdmChlTimeIntlvrDepth_Type(Integer32):
    """Custom type cadIfDsOfdmChlTimeIntlvrDepth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CadIfDsOfdmChlTimeIntlvrDepth_Type.__name__ = "Integer32"
_CadIfDsOfdmChlTimeIntlvrDepth_Object = MibTableColumn
cadIfDsOfdmChlTimeIntlvrDepth = _CadIfDsOfdmChlTimeIntlvrDepth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 7),
    _CadIfDsOfdmChlTimeIntlvrDepth_Type()
)
cadIfDsOfdmChlTimeIntlvrDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlTimeIntlvrDepth.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlTimeIntlvrDepth.setUnits("symbols")


class _CadIfDsOfdmChlSubcSpacing_Type(Integer32):
    """Custom type cadIfDsOfdmChlSubcSpacing based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25000, 25000),
        ValueRangeConstraint(50000, 50000),
    )


_CadIfDsOfdmChlSubcSpacing_Type.__name__ = "Integer32"
_CadIfDsOfdmChlSubcSpacing_Object = MibTableColumn
cadIfDsOfdmChlSubcSpacing = _CadIfDsOfdmChlSubcSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 8),
    _CadIfDsOfdmChlSubcSpacing_Type()
)
cadIfDsOfdmChlSubcSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlSubcSpacing.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlSubcSpacing.setUnits("hertz")


class _CadIfDsOfdmChlContPilotScaleFactor_Type(Integer32):
    """Custom type cadIfDsOfdmChlContPilotScaleFactor based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 120),
    )


_CadIfDsOfdmChlContPilotScaleFactor_Type.__name__ = "Integer32"
_CadIfDsOfdmChlContPilotScaleFactor_Object = MibTableColumn
cadIfDsOfdmChlContPilotScaleFactor = _CadIfDsOfdmChlContPilotScaleFactor_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 9),
    _CadIfDsOfdmChlContPilotScaleFactor_Type()
)
cadIfDsOfdmChlContPilotScaleFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlContPilotScaleFactor.setStatus("current")


class _CadIfDsOfdmChlMaxRoundTripDelay_Type(Integer32):
    """Custom type cadIfDsOfdmChlMaxRoundTripDelay based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1600),
    )


_CadIfDsOfdmChlMaxRoundTripDelay_Type.__name__ = "Integer32"
_CadIfDsOfdmChlMaxRoundTripDelay_Object = MibTableColumn
cadIfDsOfdmChlMaxRoundTripDelay = _CadIfDsOfdmChlMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 10),
    _CadIfDsOfdmChlMaxRoundTripDelay_Type()
)
cadIfDsOfdmChlMaxRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlMaxRoundTripDelay.setUnits("Microseconds")


class _CadIfDsOfdmChlPCNormAllowedUsage_Type(Integer32):
    """Custom type cadIfDsOfdmChlPCNormAllowedUsage based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDsOfdmChlPCNormAllowedUsage_Type.__name__ = "Integer32"
_CadIfDsOfdmChlPCNormAllowedUsage_Object = MibTableColumn
cadIfDsOfdmChlPCNormAllowedUsage = _CadIfDsOfdmChlPCNormAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 11),
    _CadIfDsOfdmChlPCNormAllowedUsage_Type()
)
cadIfDsOfdmChlPCNormAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCNormAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCNormAllowedUsage.setUnits("percent")


class _CadIfDsOfdmChlPCNormResUsage_Type(Integer32):
    """Custom type cadIfDsOfdmChlPCNormResUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDsOfdmChlPCNormResUsage_Type.__name__ = "Integer32"
_CadIfDsOfdmChlPCNormResUsage_Object = MibTableColumn
cadIfDsOfdmChlPCNormResUsage = _CadIfDsOfdmChlPCNormResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 12),
    _CadIfDsOfdmChlPCNormResUsage_Type()
)
cadIfDsOfdmChlPCNormResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCNormResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCNormResUsage.setUnits("percent")


class _CadIfDsOfdmChlPCEmerAllowedUsage_Type(Integer32):
    """Custom type cadIfDsOfdmChlPCEmerAllowedUsage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDsOfdmChlPCEmerAllowedUsage_Type.__name__ = "Integer32"
_CadIfDsOfdmChlPCEmerAllowedUsage_Object = MibTableColumn
cadIfDsOfdmChlPCEmerAllowedUsage = _CadIfDsOfdmChlPCEmerAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 13),
    _CadIfDsOfdmChlPCEmerAllowedUsage_Type()
)
cadIfDsOfdmChlPCEmerAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCEmerAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCEmerAllowedUsage.setUnits("percent")


class _CadIfDsOfdmChlPCEmerResUsage_Type(Integer32):
    """Custom type cadIfDsOfdmChlPCEmerResUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDsOfdmChlPCEmerResUsage_Type.__name__ = "Integer32"
_CadIfDsOfdmChlPCEmerResUsage_Object = MibTableColumn
cadIfDsOfdmChlPCEmerResUsage = _CadIfDsOfdmChlPCEmerResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 14),
    _CadIfDsOfdmChlPCEmerResUsage_Type()
)
cadIfDsOfdmChlPCEmerResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCEmerResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCEmerResUsage.setUnits("percent")


class _CadIfDsOfdmChlPCTotalAllowedUsage_Type(Integer32):
    """Custom type cadIfDsOfdmChlPCTotalAllowedUsage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfDsOfdmChlPCTotalAllowedUsage_Type.__name__ = "Integer32"
_CadIfDsOfdmChlPCTotalAllowedUsage_Object = MibTableColumn
cadIfDsOfdmChlPCTotalAllowedUsage = _CadIfDsOfdmChlPCTotalAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 15),
    _CadIfDsOfdmChlPCTotalAllowedUsage_Type()
)
cadIfDsOfdmChlPCTotalAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCTotalAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCTotalAllowedUsage.setUnits("percent")


class _CadIfDsOfdmChlPCPreemptionAllowed_Type(TruthValue):
    """Custom type cadIfDsOfdmChlPCPreemptionAllowed based on TruthValue"""


_CadIfDsOfdmChlPCPreemptionAllowed_Object = MibTableColumn
cadIfDsOfdmChlPCPreemptionAllowed = _CadIfDsOfdmChlPCPreemptionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 16),
    _CadIfDsOfdmChlPCPreemptionAllowed_Type()
)
cadIfDsOfdmChlPCPreemptionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPCPreemptionAllowed.setStatus("current")


class _CadIfDsOfdmChlRfPortBasePower_Type(TenthdBmV):
    """Custom type cadIfDsOfdmChlRfPortBasePower based on TenthdBmV"""
    defaultValue = 380

    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 600),
    )


_CadIfDsOfdmChlRfPortBasePower_Type.__name__ = "TenthdBmV"
_CadIfDsOfdmChlRfPortBasePower_Object = MibTableColumn
cadIfDsOfdmChlRfPortBasePower = _CadIfDsOfdmChlRfPortBasePower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 17),
    _CadIfDsOfdmChlRfPortBasePower_Type()
)
cadIfDsOfdmChlRfPortBasePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlRfPortBasePower.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlRfPortBasePower.setUnits("dBmV")


class _CadIfDsOfdmChlSubcZeroCentFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlSubcZeroCentFreq based on Integer32"""
    defaultValue = 0


_CadIfDsOfdmChlSubcZeroCentFreq_Object = MibTableColumn
cadIfDsOfdmChlSubcZeroCentFreq = _CadIfDsOfdmChlSubcZeroCentFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 18),
    _CadIfDsOfdmChlSubcZeroCentFreq_Type()
)
cadIfDsOfdmChlSubcZeroCentFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlSubcZeroCentFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlSubcZeroCentFreq.setUnits("hertz")


class _CadIfDsOfdmChlLowActSubcCentFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlLowActSubcCentFreq based on Integer32"""
    defaultValue = 0


_CadIfDsOfdmChlLowActSubcCentFreq_Object = MibTableColumn
cadIfDsOfdmChlLowActSubcCentFreq = _CadIfDsOfdmChlLowActSubcCentFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 19),
    _CadIfDsOfdmChlLowActSubcCentFreq_Type()
)
cadIfDsOfdmChlLowActSubcCentFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlLowActSubcCentFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlLowActSubcCentFreq.setUnits("hertz")


class _CadIfDsOfdmChlHighActSubcCentFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlHighActSubcCentFreq based on Integer32"""
    defaultValue = 0


_CadIfDsOfdmChlHighActSubcCentFreq_Object = MibTableColumn
cadIfDsOfdmChlHighActSubcCentFreq = _CadIfDsOfdmChlHighActSubcCentFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 20),
    _CadIfDsOfdmChlHighActSubcCentFreq_Type()
)
cadIfDsOfdmChlHighActSubcCentFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlHighActSubcCentFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlHighActSubcCentFreq.setUnits("hertz")


class _CadIfDsOfdmChlPlcLowSubcCentFreq_Type(Integer32):
    """Custom type cadIfDsOfdmChlPlcLowSubcCentFreq based on Integer32"""
    defaultValue = 0


_CadIfDsOfdmChlPlcLowSubcCentFreq_Object = MibTableColumn
cadIfDsOfdmChlPlcLowSubcCentFreq = _CadIfDsOfdmChlPlcLowSubcCentFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 21),
    _CadIfDsOfdmChlPlcLowSubcCentFreq_Type()
)
cadIfDsOfdmChlPlcLowSubcCentFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPlcLowSubcCentFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlPlcLowSubcCentFreq.setUnits("hertz")


class _CadIfDsOfdmChlNumActSubc_Type(Integer32):
    """Custom type cadIfDsOfdmChlNumActSubc based on Integer32"""
    defaultValue = 0


_CadIfDsOfdmChlNumActSubc_Object = MibTableColumn
cadIfDsOfdmChlNumActSubc = _CadIfDsOfdmChlNumActSubc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 22),
    _CadIfDsOfdmChlNumActSubc_Type()
)
cadIfDsOfdmChlNumActSubc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlNumActSubc.setStatus("current")
_CadIfDsOfdmChlDataTable_Object = MibTable
cadIfDsOfdmChlDataTable = _CadIfDsOfdmChlDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6)
)
if mibBuilder.loadTexts:
    cadIfDsOfdmChlDataTable.setStatus("current")
_CadIfDsOfdmChlDataEntry_Object = MibTableRow
cadIfDsOfdmChlDataEntry = _CadIfDsOfdmChlDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cadIfDsOfdmChlDataEntry.setStatus("current")


class _CadIfDsOfdmChlDataNumActSubcarriers_Type(Integer32):
    """Custom type cadIfDsOfdmChlDataNumActSubcarriers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(200, 7600),
    )


_CadIfDsOfdmChlDataNumActSubcarriers_Type.__name__ = "Integer32"
_CadIfDsOfdmChlDataNumActSubcarriers_Object = MibTableColumn
cadIfDsOfdmChlDataNumActSubcarriers = _CadIfDsOfdmChlDataNumActSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6, 1, 1),
    _CadIfDsOfdmChlDataNumActSubcarriers_Type()
)
cadIfDsOfdmChlDataNumActSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlDataNumActSubcarriers.setStatus("current")


class _CadIfDsOfdmChlDataNumContPilots_Type(Integer32):
    """Custom type cadIfDsOfdmChlDataNumContPilots based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 128),
    )


_CadIfDsOfdmChlDataNumContPilots_Type.__name__ = "Integer32"
_CadIfDsOfdmChlDataNumContPilots_Object = MibTableColumn
cadIfDsOfdmChlDataNumContPilots = _CadIfDsOfdmChlDataNumContPilots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6, 1, 2),
    _CadIfDsOfdmChlDataNumContPilots_Type()
)
cadIfDsOfdmChlDataNumContPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfDsOfdmChlDataNumContPilots.setStatus("current")
_CadDsOfdmProfileTable_Object = MibTable
cadDsOfdmProfileTable = _CadDsOfdmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8)
)
if mibBuilder.loadTexts:
    cadDsOfdmProfileTable.setStatus("current")
_CadDsOfdmProfileEntry_Object = MibTableRow
cadDsOfdmProfileEntry = _CadDsOfdmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1)
)
cadDsOfdmProfileEntry.setIndexNames(
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfileIfIndex"),
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfileId"),
)
if mibBuilder.loadTexts:
    cadDsOfdmProfileEntry.setStatus("current")
_CadDsOfdmProfileIfIndex_Type = InterfaceIndex
_CadDsOfdmProfileIfIndex_Object = MibTableColumn
cadDsOfdmProfileIfIndex = _CadDsOfdmProfileIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 1),
    _CadDsOfdmProfileIfIndex_Type()
)
cadDsOfdmProfileIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfileIfIndex.setStatus("current")
_CadDsOfdmProfileId_Type = OfdmProfileId
_CadDsOfdmProfileId_Object = MibTableColumn
cadDsOfdmProfileId = _CadDsOfdmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 2),
    _CadDsOfdmProfileId_Type()
)
cadDsOfdmProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfileId.setStatus("current")


class _CadDsOfdmProfileDefBitload_Type(CerOfdmModType):
    """Custom type cadDsOfdmProfileDefBitload based on CerOfdmModType"""


_CadDsOfdmProfileDefBitload_Object = MibTableColumn
cadDsOfdmProfileDefBitload = _CadDsOfdmProfileDefBitload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 3),
    _CadDsOfdmProfileDefBitload_Type()
)
cadDsOfdmProfileDefBitload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfileDefBitload.setStatus("current")
_CadDsOfdmProfileRowStatus_Type = RowStatus
_CadDsOfdmProfileRowStatus_Object = MibTableColumn
cadDsOfdmProfileRowStatus = _CadDsOfdmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 4),
    _CadDsOfdmProfileRowStatus_Type()
)
cadDsOfdmProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfileRowStatus.setStatus("current")
_CadDsOfdmProfStatTable_Object = MibTable
cadDsOfdmProfStatTable = _CadDsOfdmProfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9)
)
if mibBuilder.loadTexts:
    cadDsOfdmProfStatTable.setStatus("current")
_CadDsOfdmProfStatEntry_Object = MibTableRow
cadDsOfdmProfStatEntry = _CadDsOfdmProfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1)
)
cadDsOfdmProfStatEntry.setIndexNames(
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfStatIfIndex"),
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfStatProfId"),
)
if mibBuilder.loadTexts:
    cadDsOfdmProfStatEntry.setStatus("current")
_CadDsOfdmProfStatIfIndex_Type = InterfaceIndex
_CadDsOfdmProfStatIfIndex_Object = MibTableColumn
cadDsOfdmProfStatIfIndex = _CadDsOfdmProfStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 1),
    _CadDsOfdmProfStatIfIndex_Type()
)
cadDsOfdmProfStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatIfIndex.setStatus("current")
_CadDsOfdmProfStatProfId_Type = OfdmProfileId
_CadDsOfdmProfStatProfId_Object = MibTableColumn
cadDsOfdmProfStatProfId = _CadDsOfdmProfStatProfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 2),
    _CadDsOfdmProfStatProfId_Type()
)
cadDsOfdmProfStatProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatProfId.setStatus("current")
_CadDsOfdmProfStatAvgBitsPerSubc_Type = Unsigned32
_CadDsOfdmProfStatAvgBitsPerSubc_Object = MibTableColumn
cadDsOfdmProfStatAvgBitsPerSubc = _CadDsOfdmProfStatAvgBitsPerSubc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 3),
    _CadDsOfdmProfStatAvgBitsPerSubc_Type()
)
cadDsOfdmProfStatAvgBitsPerSubc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatAvgBitsPerSubc.setStatus("current")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatAvgBitsPerSubc.setUnits("HundredthBit")
_CadDsOfdmProfStatReqMods_Type = CerOfdmModBitsType
_CadDsOfdmProfStatReqMods_Object = MibTableColumn
cadDsOfdmProfStatReqMods = _CadDsOfdmProfStatReqMods_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 4),
    _CadDsOfdmProfStatReqMods_Type()
)
cadDsOfdmProfStatReqMods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatReqMods.setStatus("current")
_CadDsOfdmProfStatEtherFrameBytes_Type = Counter64
_CadDsOfdmProfStatEtherFrameBytes_Object = MibTableColumn
cadDsOfdmProfStatEtherFrameBytes = _CadDsOfdmProfStatEtherFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 5),
    _CadDsOfdmProfStatEtherFrameBytes_Type()
)
cadDsOfdmProfStatEtherFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatEtherFrameBytes.setStatus("current")
_CadDsOfdmProfStatTotalCodewords_Type = Counter64
_CadDsOfdmProfStatTotalCodewords_Object = MibTableColumn
cadDsOfdmProfStatTotalCodewords = _CadDsOfdmProfStatTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 6),
    _CadDsOfdmProfStatTotalCodewords_Type()
)
cadDsOfdmProfStatTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsOfdmProfStatTotalCodewords.setStatus("current")


class _CadDsOfdmProfStat30SecCwUtil_Type(Unsigned32):
    """Custom type cadDsOfdmProfStat30SecCwUtil based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadDsOfdmProfStat30SecCwUtil_Type.__name__ = "Unsigned32"
_CadDsOfdmProfStat30SecCwUtil_Object = MibTableColumn
cadDsOfdmProfStat30SecCwUtil = _CadDsOfdmProfStat30SecCwUtil_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 7),
    _CadDsOfdmProfStat30SecCwUtil_Type()
)
cadDsOfdmProfStat30SecCwUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsOfdmProfStat30SecCwUtil.setStatus("current")


class _CadDsOfdmProfStat30SecCwEff_Type(Unsigned32):
    """Custom type cadDsOfdmProfStat30SecCwEff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadDsOfdmProfStat30SecCwEff_Type.__name__ = "Unsigned32"
_CadDsOfdmProfStat30SecCwEff_Object = MibTableColumn
cadDsOfdmProfStat30SecCwEff = _CadDsOfdmProfStat30SecCwEff_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 8),
    _CadDsOfdmProfStat30SecCwEff_Type()
)
cadDsOfdmProfStat30SecCwEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsOfdmProfStat30SecCwEff.setStatus("current")
_CadDsOfdmProfExceptionTable_Object = MibTable
cadDsOfdmProfExceptionTable = _CadDsOfdmProfExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11)
)
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionTable.setStatus("current")
_CadDsOfdmProfExceptionEntry_Object = MibTableRow
cadDsOfdmProfExceptionEntry = _CadDsOfdmProfExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1)
)
cadDsOfdmProfExceptionEntry.setIndexNames(
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfExceptionIfIndex"),
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfExceptionProfId"),
    (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfExceptionLowFreq"),
)
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionEntry.setStatus("current")
_CadDsOfdmProfExceptionIfIndex_Type = InterfaceIndex
_CadDsOfdmProfExceptionIfIndex_Object = MibTableColumn
cadDsOfdmProfExceptionIfIndex = _CadDsOfdmProfExceptionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 1),
    _CadDsOfdmProfExceptionIfIndex_Type()
)
cadDsOfdmProfExceptionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionIfIndex.setStatus("current")
_CadDsOfdmProfExceptionProfId_Type = OfdmProfileId
_CadDsOfdmProfExceptionProfId_Object = MibTableColumn
cadDsOfdmProfExceptionProfId = _CadDsOfdmProfExceptionProfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 2),
    _CadDsOfdmProfExceptionProfId_Type()
)
cadDsOfdmProfExceptionProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionProfId.setStatus("current")


class _CadDsOfdmProfExceptionLowFreq_Type(Integer32):
    """Custom type cadDsOfdmProfExceptionLowFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(108000000, 1770000000),
    )


_CadDsOfdmProfExceptionLowFreq_Type.__name__ = "Integer32"
_CadDsOfdmProfExceptionLowFreq_Object = MibTableColumn
cadDsOfdmProfExceptionLowFreq = _CadDsOfdmProfExceptionLowFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 3),
    _CadDsOfdmProfExceptionLowFreq_Type()
)
cadDsOfdmProfExceptionLowFreq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionLowFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionLowFreq.setUnits("hertz")


class _CadDsOfdmProfExceptionHighFreq_Type(Integer32):
    """Custom type cadDsOfdmProfExceptionHighFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(108000000, 1770000000),
    )


_CadDsOfdmProfExceptionHighFreq_Type.__name__ = "Integer32"
_CadDsOfdmProfExceptionHighFreq_Object = MibTableColumn
cadDsOfdmProfExceptionHighFreq = _CadDsOfdmProfExceptionHighFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 4),
    _CadDsOfdmProfExceptionHighFreq_Type()
)
cadDsOfdmProfExceptionHighFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionHighFreq.setStatus("current")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionHighFreq.setUnits("hertz")


class _CadDsOfdmProfExceptionSkip_Type(TruthValue):
    """Custom type cadDsOfdmProfExceptionSkip based on TruthValue"""


_CadDsOfdmProfExceptionSkip_Object = MibTableColumn
cadDsOfdmProfExceptionSkip = _CadDsOfdmProfExceptionSkip_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 5),
    _CadDsOfdmProfExceptionSkip_Type()
)
cadDsOfdmProfExceptionSkip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionSkip.setStatus("current")


class _CadDsOfdmProfExceptionMainBitload_Type(CerOfdmModType):
    """Custom type cadDsOfdmProfExceptionMainBitload based on CerOfdmModType"""


_CadDsOfdmProfExceptionMainBitload_Object = MibTableColumn
cadDsOfdmProfExceptionMainBitload = _CadDsOfdmProfExceptionMainBitload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 6),
    _CadDsOfdmProfExceptionMainBitload_Type()
)
cadDsOfdmProfExceptionMainBitload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionMainBitload.setStatus("current")


class _CadDsOfdmProfExceptionOddBitload_Type(CerOfdmModType):
    """Custom type cadDsOfdmProfExceptionOddBitload based on CerOfdmModType"""


_CadDsOfdmProfExceptionOddBitload_Object = MibTableColumn
cadDsOfdmProfExceptionOddBitload = _CadDsOfdmProfExceptionOddBitload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 7),
    _CadDsOfdmProfExceptionOddBitload_Type()
)
cadDsOfdmProfExceptionOddBitload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionOddBitload.setStatus("current")
_CadDsOfdmProfExceptionRowStatus_Type = RowStatus
_CadDsOfdmProfExceptionRowStatus_Object = MibTableColumn
cadDsOfdmProfExceptionRowStatus = _CadDsOfdmProfExceptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 8),
    _CadDsOfdmProfExceptionRowStatus_Type()
)
cadDsOfdmProfExceptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsOfdmProfExceptionRowStatus.setStatus("current")
cadIfDsOfdmChlEntry.registerAugmentions(
    ("CADANT-CMTS-DOWNCHANNEL-MIB",
     "cadIfDsOfdmChlDataEntry")
)
cadIfDsOfdmChlDataEntry.setIndexNames(*cadIfDsOfdmChlEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-DOWNCHANNEL-MIB",
    **{"OfdmProfileId": OfdmProfileId,
       "CerOfdmModType": CerOfdmModType,
       "CerOfdmModBitsType": CerOfdmModBitsType,
       "cadDownchannelMib": cadDownchannelMib,
       "cadIfDownstreamChannelTable": cadIfDownstreamChannelTable,
       "cadIfDownstreamChannelEntry": cadIfDownstreamChannelEntry,
       "cadIfDownChannelId": cadIfDownChannelId,
       "cadIfDownChannelFrequency": cadIfDownChannelFrequency,
       "cadIfDownChannelWidth": cadIfDownChannelWidth,
       "cadIfDownChannelModulation": cadIfDownChannelModulation,
       "cadIfDownChannelInterleave": cadIfDownChannelInterleave,
       "cadIfDownChannelPower": cadIfDownChannelPower,
       "cadIfDownChannelPowerFineAdj": cadIfDownChannelPowerFineAdj,
       "cadIfCmtsCardNumber": cadIfCmtsCardNumber,
       "cadIfDownChannelCACL1Threshold": cadIfDownChannelCACL1Threshold,
       "cadIfDownChannelCACL2Threshold": cadIfDownChannelCACL2Threshold,
       "cadIfDownChannelCACL3Threshold": cadIfDownChannelCACL3Threshold,
       "cadIfDownChannelMaxRoundTripDelay": cadIfDownChannelMaxRoundTripDelay,
       "cadIfDownChannelAnnex": cadIfDownChannelAnnex,
       "cadIfDownChannelPCNormAllowedUsage": cadIfDownChannelPCNormAllowedUsage,
       "cadIfDownChannelPCNormResUsage": cadIfDownChannelPCNormResUsage,
       "cadIfDownChannelPCEmerAllowedUsage": cadIfDownChannelPCEmerAllowedUsage,
       "cadIfDownChannelPCEmerResUsage": cadIfDownChannelPCEmerResUsage,
       "cadIfDownChannelPCTotalAllowedUsage": cadIfDownChannelPCTotalAllowedUsage,
       "cadIfDownChannelPCPreemptionAllowed": cadIfDownChannelPCPreemptionAllowed,
       "cadIfDownChannelIfIndex": cadIfDownChannelIfIndex,
       "cadIfDownChannelPrimaryCapable": cadIfDownChannelPrimaryCapable,
       "cadIfDownSpectralInversion": cadIfDownSpectralInversion,
       "cadDownChannelParams": cadDownChannelParams,
       "cadDownChannelMaxFrequency": cadDownChannelMaxFrequency,
       "cadDownChannelMinFrequency": cadDownChannelMinFrequency,
       "cadDownChannelAgcEnable": cadDownChannelAgcEnable,
       "cadDownChannelOorRecoveryEnable": cadDownChannelOorRecoveryEnable,
       "cadDsOfdmOcdDpdPlcInterval": cadDsOfdmOcdDpdPlcInterval,
       "cadDsOfdmDpdProfAInterval": cadDsOfdmDpdProfAInterval,
       "cadDownChannelLsredMinThresh": cadDownChannelLsredMinThresh,
       "cadDownChannelLsredMaxThresh": cadDownChannelLsredMaxThresh,
       "cadDownChannelLsredMaxProb": cadDownChannelLsredMaxProb,
       "cadDownChannelVoiceShaping": cadDownChannelVoiceShaping,
       "cadIfDsOfdmPowerTable": cadIfDsOfdmPowerTable,
       "cadIfDsOfdmPowerEntry": cadIfDsOfdmPowerEntry,
       "cadIfDsOfdmPowerIfIndex": cadIfDsOfdmPowerIfIndex,
       "cadIfDsOfdmPowerFrequency": cadIfDsOfdmPowerFrequency,
       "cadIfDsOfdmPowerFineAdjustment": cadIfDsOfdmPowerFineAdjustment,
       "cadIfDsOfdmPowerCurrLevel": cadIfDsOfdmPowerCurrLevel,
       "cadIfDsOfdmPowerMinLevel": cadIfDsOfdmPowerMinLevel,
       "cadIfDsOfdmPowerMaxLevel": cadIfDsOfdmPowerMaxLevel,
       "cadIfDsOfdmChlTable": cadIfDsOfdmChlTable,
       "cadIfDsOfdmChlEntry": cadIfDsOfdmChlEntry,
       "cadIfDsOfdmChlIfIndex": cadIfDsOfdmChlIfIndex,
       "cadIfDsOfdmChlLowFreq": cadIfDsOfdmChlLowFreq,
       "cadIfDsOfdmChlHighFreq": cadIfDsOfdmChlHighFreq,
       "cadIfDsOfdmChlPlcBlkLowSubcCentFreq": cadIfDsOfdmChlPlcBlkLowSubcCentFreq,
       "cadIfDsOfdmChlCyclicPrefix": cadIfDsOfdmChlCyclicPrefix,
       "cadIfDsOfdmChlRolloffPeriod": cadIfDsOfdmChlRolloffPeriod,
       "cadIfDsOfdmChlTimeIntlvrDepth": cadIfDsOfdmChlTimeIntlvrDepth,
       "cadIfDsOfdmChlSubcSpacing": cadIfDsOfdmChlSubcSpacing,
       "cadIfDsOfdmChlContPilotScaleFactor": cadIfDsOfdmChlContPilotScaleFactor,
       "cadIfDsOfdmChlMaxRoundTripDelay": cadIfDsOfdmChlMaxRoundTripDelay,
       "cadIfDsOfdmChlPCNormAllowedUsage": cadIfDsOfdmChlPCNormAllowedUsage,
       "cadIfDsOfdmChlPCNormResUsage": cadIfDsOfdmChlPCNormResUsage,
       "cadIfDsOfdmChlPCEmerAllowedUsage": cadIfDsOfdmChlPCEmerAllowedUsage,
       "cadIfDsOfdmChlPCEmerResUsage": cadIfDsOfdmChlPCEmerResUsage,
       "cadIfDsOfdmChlPCTotalAllowedUsage": cadIfDsOfdmChlPCTotalAllowedUsage,
       "cadIfDsOfdmChlPCPreemptionAllowed": cadIfDsOfdmChlPCPreemptionAllowed,
       "cadIfDsOfdmChlRfPortBasePower": cadIfDsOfdmChlRfPortBasePower,
       "cadIfDsOfdmChlSubcZeroCentFreq": cadIfDsOfdmChlSubcZeroCentFreq,
       "cadIfDsOfdmChlLowActSubcCentFreq": cadIfDsOfdmChlLowActSubcCentFreq,
       "cadIfDsOfdmChlHighActSubcCentFreq": cadIfDsOfdmChlHighActSubcCentFreq,
       "cadIfDsOfdmChlPlcLowSubcCentFreq": cadIfDsOfdmChlPlcLowSubcCentFreq,
       "cadIfDsOfdmChlNumActSubc": cadIfDsOfdmChlNumActSubc,
       "cadIfDsOfdmChlDataTable": cadIfDsOfdmChlDataTable,
       "cadIfDsOfdmChlDataEntry": cadIfDsOfdmChlDataEntry,
       "cadIfDsOfdmChlDataNumActSubcarriers": cadIfDsOfdmChlDataNumActSubcarriers,
       "cadIfDsOfdmChlDataNumContPilots": cadIfDsOfdmChlDataNumContPilots,
       "cadDsOfdmProfileTable": cadDsOfdmProfileTable,
       "cadDsOfdmProfileEntry": cadDsOfdmProfileEntry,
       "cadDsOfdmProfileIfIndex": cadDsOfdmProfileIfIndex,
       "cadDsOfdmProfileId": cadDsOfdmProfileId,
       "cadDsOfdmProfileDefBitload": cadDsOfdmProfileDefBitload,
       "cadDsOfdmProfileRowStatus": cadDsOfdmProfileRowStatus,
       "cadDsOfdmProfStatTable": cadDsOfdmProfStatTable,
       "cadDsOfdmProfStatEntry": cadDsOfdmProfStatEntry,
       "cadDsOfdmProfStatIfIndex": cadDsOfdmProfStatIfIndex,
       "cadDsOfdmProfStatProfId": cadDsOfdmProfStatProfId,
       "cadDsOfdmProfStatAvgBitsPerSubc": cadDsOfdmProfStatAvgBitsPerSubc,
       "cadDsOfdmProfStatReqMods": cadDsOfdmProfStatReqMods,
       "cadDsOfdmProfStatEtherFrameBytes": cadDsOfdmProfStatEtherFrameBytes,
       "cadDsOfdmProfStatTotalCodewords": cadDsOfdmProfStatTotalCodewords,
       "cadDsOfdmProfStat30SecCwUtil": cadDsOfdmProfStat30SecCwUtil,
       "cadDsOfdmProfStat30SecCwEff": cadDsOfdmProfStat30SecCwEff,
       "cadDsOfdmProfExceptionTable": cadDsOfdmProfExceptionTable,
       "cadDsOfdmProfExceptionEntry": cadDsOfdmProfExceptionEntry,
       "cadDsOfdmProfExceptionIfIndex": cadDsOfdmProfExceptionIfIndex,
       "cadDsOfdmProfExceptionProfId": cadDsOfdmProfExceptionProfId,
       "cadDsOfdmProfExceptionLowFreq": cadDsOfdmProfExceptionLowFreq,
       "cadDsOfdmProfExceptionHighFreq": cadDsOfdmProfExceptionHighFreq,
       "cadDsOfdmProfExceptionSkip": cadDsOfdmProfExceptionSkip,
       "cadDsOfdmProfExceptionMainBitload": cadDsOfdmProfExceptionMainBitload,
       "cadDsOfdmProfExceptionOddBitload": cadDsOfdmProfExceptionOddBitload,
       "cadDsOfdmProfExceptionRowStatus": cadDsOfdmProfExceptionRowStatus}
)
