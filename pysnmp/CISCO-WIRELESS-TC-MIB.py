# SNMP MIB module (CISCO-WIRELESS-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:34 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWirelessTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 137)
)
ciscoWirelessTextualConventions.setRevisions(
        ("2000-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CwrRFZeroIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



class CwrCwErrorFreeSecond(Gauge32, TextualConvention):
    status = "current"


class CwrCwErroredSecond(Gauge32, TextualConvention):
    status = "current"


class CwrCwSeverelyErroredSecond(Gauge32, TextualConvention):
    status = "current"


class CwrCwConsecutiveSevErrSecond(Gauge32, TextualConvention):
    status = "current"


class CwrCwDegradedSecond(Gauge32, TextualConvention):
    status = "current"


class CwrCwDegradedMinute(Gauge32, TextualConvention):
    status = "current"


class CwrCollectionAction(Integer32, TextualConvention):
    status = "current"
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
        *(("actionClear", 3),
          ("actionRestart", 4),
          ("actionStart", 2),
          ("actionStop", 1))
    )



class CwrCollectionStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("statusCaptured", 4),
          ("statusIdle", 1),
          ("statusInProgress", 2),
          ("statusStopped", 3))
    )



class CwrdBm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 33),
    )



class CwrdB(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class CwrThreshLimitType(Integer32, TextualConvention):
    status = "current"
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
        *(("downChange", 2),
          ("highThresh", 3),
          ("lowLimit", 6),
          ("lowThresh", 4),
          ("upChange", 1),
          ("upLimit", 5))
    )



class CwrRadioSignalAttribute(Integer32, TextualConvention):
    status = "current"
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
        *(("rsaConstellationVariance", 3),
          ("rsaFreqOffset", 8),
          ("rsaGainSettingsIF", 6),
          ("rsaGainSettingsRF", 7),
          ("rsaIN", 1),
          ("rsaINR", 2),
          ("rsaReceivedPower", 5),
          ("rsaSyncStatus", 10),
          ("rsaTimingOffset", 4),
          ("rsaTotalGain", 9))
    )



class CwrOscState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("osccillatorBad", 2),
          ("oscillatorOk", 1))
    )



class P2mpRadioSignalAttribute(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rsaChDelaySpreadDiversityAnt", 8),
          ("rsaChDelaySpreadMainAnt", 7),
          ("rsaHeAmbientNoise", 9),
          ("rsaRxPowerDiversityAnt", 6),
          ("rsaRxPowerMainAnt", 5),
          ("rsaSinrDiversityAnt", 2),
          ("rsaSinrMainAnt", 1),
          ("rsaSinrRatio", 3),
          ("rsaSuRxPowerDeltaDiversityAnt", 11),
          ("rsaSuRxPowerDeltaMainAnt", 10),
          ("rsaSuTotalTxPower", 12),
          ("rsaTimingOffset", 4))
    )



class CwrRfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 1),
          ("main", 0))
    )



class CwrFixedPointScale(Integer32, TextualConvention):
    status = "current"
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("atto", 3),
          ("exa", 14),
          ("femto", 4),
          ("giga", 12),
          ("kilo", 10),
          ("mega", 11),
          ("micro", 7),
          ("milli", 8),
          ("nano", 6),
          ("peta", 15),
          ("pico", 5),
          ("tera", 13),
          ("units", 9),
          ("yocto", 1),
          ("yotta", 17),
          ("zepto", 2),
          ("zetta", 16))
    )



class CwrFixedPointPrecision(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )



class CwrFixedPointValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class P2mpSnapshotAttribute(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class CwrPercentageValue(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )



class CwrUpdateTime(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CwrRfFreqRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )



class WirelessGauge64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-TC-MIB",
    **{"CwrRFZeroIndex": CwrRFZeroIndex,
       "CwrCwErrorFreeSecond": CwrCwErrorFreeSecond,
       "CwrCwErroredSecond": CwrCwErroredSecond,
       "CwrCwSeverelyErroredSecond": CwrCwSeverelyErroredSecond,
       "CwrCwConsecutiveSevErrSecond": CwrCwConsecutiveSevErrSecond,
       "CwrCwDegradedSecond": CwrCwDegradedSecond,
       "CwrCwDegradedMinute": CwrCwDegradedMinute,
       "CwrCollectionAction": CwrCollectionAction,
       "CwrCollectionStatus": CwrCollectionStatus,
       "CwrdBm": CwrdBm,
       "CwrdB": CwrdB,
       "CwrThreshLimitType": CwrThreshLimitType,
       "CwrRadioSignalAttribute": CwrRadioSignalAttribute,
       "CwrOscState": CwrOscState,
       "P2mpRadioSignalAttribute": P2mpRadioSignalAttribute,
       "CwrRfType": CwrRfType,
       "CwrFixedPointScale": CwrFixedPointScale,
       "CwrFixedPointPrecision": CwrFixedPointPrecision,
       "CwrFixedPointValue": CwrFixedPointValue,
       "P2mpSnapshotAttribute": P2mpSnapshotAttribute,
       "CwrPercentageValue": CwrPercentageValue,
       "CwrUpdateTime": CwrUpdateTime,
       "CwrRfFreqRange": CwrRfFreqRange,
       "WirelessGauge64": WirelessGauge64,
       "ciscoWirelessTextualConventions": ciscoWirelessTextualConventions}
)
