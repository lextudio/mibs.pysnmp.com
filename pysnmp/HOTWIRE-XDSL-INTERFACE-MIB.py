# SNMP MIB module (HOTWIRE-XDSL-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HOTWIRE-XDSL-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:52 2024
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

(pdnPortConfigVNID,) = mibBuilder.importSymbols(
    "HOT-DOMAIN-MIB",
    "pdnPortConfigVNID")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(xdsl,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "xdsl")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XdslDevice_ObjectIdentity = ObjectIdentity
xdslDevice = _XdslDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1)
)
_XdslDevIfStats_ObjectIdentity = ObjectIdentity
xdslDevIfStats = _XdslDevIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1)
)
_XdslDevIfIntervalStatsTable_Object = MibTable
xdslDevIfIntervalStatsTable = _XdslDevIfIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xdslDevIfIntervalStatsTable.setStatus("mandatory")
_XdslDevIfIntervalStatsEntry_Object = MibTableRow
xdslDevIfIntervalStatsEntry = _XdslDevIfIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1)
)
xdslDevIfIntervalStatsEntry.setIndexNames(
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslDevIfStatsIfIndex"),
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslDevIfStatsInterval"),
)
if mibBuilder.loadTexts:
    xdslDevIfIntervalStatsEntry.setStatus("mandatory")
_XdslDevIfStatsIfIndex_Type = Integer32
_XdslDevIfStatsIfIndex_Object = MibTableColumn
xdslDevIfStatsIfIndex = _XdslDevIfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 1),
    _XdslDevIfStatsIfIndex_Type()
)
xdslDevIfStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsIfIndex.setStatus("mandatory")


class _XdslDevIfStatsInterval_Type(Integer32):
    """Custom type xdslDevIfStatsInterval based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("current15Minutes", 6),
          ("current24Hours", 31),
          ("currentHour", 5),
          ("first15MinuteSlice", 1),
          ("fourth15MinuteSlice", 4),
          ("hour10of24hrs", 16),
          ("hour11of24hrs", 17),
          ("hour12of24hrs", 18),
          ("hour13of24hrs", 19),
          ("hour14of24hrs", 20),
          ("hour15of24hrs", 21),
          ("hour16of24hrs", 22),
          ("hour17of24hrs", 23),
          ("hour18of24hrs", 24),
          ("hour19of24hrs", 25),
          ("hour1of24hrs", 7),
          ("hour20of24hrs", 26),
          ("hour21of24hrs", 27),
          ("hour22of24hrs", 28),
          ("hour23of24hrs", 29),
          ("hour24of24hrs", 30),
          ("hour2of24hrs", 8),
          ("hour3of24hrs", 9),
          ("hour4of24hrs", 10),
          ("hour5of24hrs", 11),
          ("hour6of24hrs", 12),
          ("hour7of24hrs", 13),
          ("hour8of24hrs", 14),
          ("hour9of24hrs", 15),
          ("previousDay", 32),
          ("second15MinuteSlice", 2),
          ("third15MinuteSlice", 3))
    )


_XdslDevIfStatsInterval_Type.__name__ = "Integer32"
_XdslDevIfStatsInterval_Object = MibTableColumn
xdslDevIfStatsInterval = _XdslDevIfStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 2),
    _XdslDevIfStatsInterval_Type()
)
xdslDevIfStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsInterval.setStatus("mandatory")
_XdslDevIfStatsValid15MinuteIntervalCount_Type = Counter32
_XdslDevIfStatsValid15MinuteIntervalCount_Object = MibTableColumn
xdslDevIfStatsValid15MinuteIntervalCount = _XdslDevIfStatsValid15MinuteIntervalCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 3),
    _XdslDevIfStatsValid15MinuteIntervalCount_Type()
)
xdslDevIfStatsValid15MinuteIntervalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsValid15MinuteIntervalCount.setStatus("mandatory")
_XdslDevIfStatsElapsedTimeLinkUp_Type = Counter32
_XdslDevIfStatsElapsedTimeLinkUp_Object = MibTableColumn
xdslDevIfStatsElapsedTimeLinkUp = _XdslDevIfStatsElapsedTimeLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 4),
    _XdslDevIfStatsElapsedTimeLinkUp_Type()
)
xdslDevIfStatsElapsedTimeLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsElapsedTimeLinkUp.setStatus("mandatory")
_XdslDevIfStatsLinkDownCount_Type = Counter32
_XdslDevIfStatsLinkDownCount_Object = MibTableColumn
xdslDevIfStatsLinkDownCount = _XdslDevIfStatsLinkDownCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 5),
    _XdslDevIfStatsLinkDownCount_Type()
)
xdslDevIfStatsLinkDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsLinkDownCount.setStatus("mandatory")
_XdslDevIfStatsUpStreamSpeed_Type = Integer32
_XdslDevIfStatsUpStreamSpeed_Object = MibTableColumn
xdslDevIfStatsUpStreamSpeed = _XdslDevIfStatsUpStreamSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 6),
    _XdslDevIfStatsUpStreamSpeed_Type()
)
xdslDevIfStatsUpStreamSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsUpStreamSpeed.setStatus("mandatory")
_XdslDevIfStatsCentralReceiverGain_Type = Integer32
_XdslDevIfStatsCentralReceiverGain_Object = MibTableColumn
xdslDevIfStatsCentralReceiverGain = _XdslDevIfStatsCentralReceiverGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 7),
    _XdslDevIfStatsCentralReceiverGain_Type()
)
xdslDevIfStatsCentralReceiverGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralReceiverGain.setStatus("mandatory")
_XdslDevIfStatsCentralRecMargin_Type = Integer32
_XdslDevIfStatsCentralRecMargin_Object = MibTableColumn
xdslDevIfStatsCentralRecMargin = _XdslDevIfStatsCentralRecMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 8),
    _XdslDevIfStatsCentralRecMargin_Type()
)
xdslDevIfStatsCentralRecMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecMargin.setStatus("mandatory")
_XdslDevIfStatsCentralRecAttenuationEstimate_Type = Integer32
_XdslDevIfStatsCentralRecAttenuationEstimate_Object = MibTableColumn
xdslDevIfStatsCentralRecAttenuationEstimate = _XdslDevIfStatsCentralRecAttenuationEstimate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 9),
    _XdslDevIfStatsCentralRecAttenuationEstimate_Type()
)
xdslDevIfStatsCentralRecAttenuationEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecAttenuationEstimate.setStatus("mandatory")
_XdslDevIfStatsCentralRecTransmitPower_Type = Integer32
_XdslDevIfStatsCentralRecTransmitPower_Object = MibTableColumn
xdslDevIfStatsCentralRecTransmitPower = _XdslDevIfStatsCentralRecTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 10),
    _XdslDevIfStatsCentralRecTransmitPower_Type()
)
xdslDevIfStatsCentralRecTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecTransmitPower.setStatus("mandatory")


class _XdslDevIfStatsCentralRecErrorRate_Type(DisplayString):
    """Custom type xdslDevIfStatsCentralRecErrorRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_XdslDevIfStatsCentralRecErrorRate_Type.__name__ = "DisplayString"
_XdslDevIfStatsCentralRecErrorRate_Object = MibTableColumn
xdslDevIfStatsCentralRecErrorRate = _XdslDevIfStatsCentralRecErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 11),
    _XdslDevIfStatsCentralRecErrorRate_Type()
)
xdslDevIfStatsCentralRecErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecErrorRate.setStatus("mandatory")
_XdslDevIfStatsCentralRecErroredSeconds_Type = Integer32
_XdslDevIfStatsCentralRecErroredSeconds_Object = MibTableColumn
xdslDevIfStatsCentralRecErroredSeconds = _XdslDevIfStatsCentralRecErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 12),
    _XdslDevIfStatsCentralRecErroredSeconds_Type()
)
xdslDevIfStatsCentralRecErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecErroredSeconds.setStatus("mandatory")
_XdslDevIfStatsCentralRecSeverelyErroredSeconds_Type = Integer32
_XdslDevIfStatsCentralRecSeverelyErroredSeconds_Object = MibTableColumn
xdslDevIfStatsCentralRecSeverelyErroredSeconds = _XdslDevIfStatsCentralRecSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 13),
    _XdslDevIfStatsCentralRecSeverelyErroredSeconds_Type()
)
xdslDevIfStatsCentralRecSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecSeverelyErroredSeconds.setStatus("mandatory")
_XdslDevIfStatsRemoteReceiverGain_Type = Integer32
_XdslDevIfStatsRemoteReceiverGain_Object = MibTableColumn
xdslDevIfStatsRemoteReceiverGain = _XdslDevIfStatsRemoteReceiverGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 14),
    _XdslDevIfStatsRemoteReceiverGain_Type()
)
xdslDevIfStatsRemoteReceiverGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteReceiverGain.setStatus("mandatory")
_XdslDevIfStatsRemoteRecMargin_Type = Integer32
_XdslDevIfStatsRemoteRecMargin_Object = MibTableColumn
xdslDevIfStatsRemoteRecMargin = _XdslDevIfStatsRemoteRecMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 15),
    _XdslDevIfStatsRemoteRecMargin_Type()
)
xdslDevIfStatsRemoteRecMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecMargin.setStatus("mandatory")
_XdslDevIfStatsRemoteRecAttenuationEstimate_Type = Integer32
_XdslDevIfStatsRemoteRecAttenuationEstimate_Object = MibTableColumn
xdslDevIfStatsRemoteRecAttenuationEstimate = _XdslDevIfStatsRemoteRecAttenuationEstimate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 16),
    _XdslDevIfStatsRemoteRecAttenuationEstimate_Type()
)
xdslDevIfStatsRemoteRecAttenuationEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecAttenuationEstimate.setStatus("mandatory")
_XdslDevIfStatsRemoteRecTransmitPower_Type = Integer32
_XdslDevIfStatsRemoteRecTransmitPower_Object = MibTableColumn
xdslDevIfStatsRemoteRecTransmitPower = _XdslDevIfStatsRemoteRecTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 17),
    _XdslDevIfStatsRemoteRecTransmitPower_Type()
)
xdslDevIfStatsRemoteRecTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecTransmitPower.setStatus("mandatory")


class _XdslDevIfStatsRemoteRecErrorRate_Type(DisplayString):
    """Custom type xdslDevIfStatsRemoteRecErrorRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_XdslDevIfStatsRemoteRecErrorRate_Type.__name__ = "DisplayString"
_XdslDevIfStatsRemoteRecErrorRate_Object = MibTableColumn
xdslDevIfStatsRemoteRecErrorRate = _XdslDevIfStatsRemoteRecErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 18),
    _XdslDevIfStatsRemoteRecErrorRate_Type()
)
xdslDevIfStatsRemoteRecErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecErrorRate.setStatus("mandatory")
_XdslDevIfStatsRemoteRecErroredSeconds_Type = Integer32
_XdslDevIfStatsRemoteRecErroredSeconds_Object = MibTableColumn
xdslDevIfStatsRemoteRecErroredSeconds = _XdslDevIfStatsRemoteRecErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 19),
    _XdslDevIfStatsRemoteRecErroredSeconds_Type()
)
xdslDevIfStatsRemoteRecErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecErroredSeconds.setStatus("mandatory")
_XdslDevIfStatsRemoteRecSeverelyErroredSeconds_Type = Integer32
_XdslDevIfStatsRemoteRecSeverelyErroredSeconds_Object = MibTableColumn
xdslDevIfStatsRemoteRecSeverelyErroredSeconds = _XdslDevIfStatsRemoteRecSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 20),
    _XdslDevIfStatsRemoteRecSeverelyErroredSeconds_Type()
)
xdslDevIfStatsRemoteRecSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecSeverelyErroredSeconds.setStatus("mandatory")
_XdslDevIfStatsRemoteOctetsCorrected_Type = Counter32
_XdslDevIfStatsRemoteOctetsCorrected_Object = MibTableColumn
xdslDevIfStatsRemoteOctetsCorrected = _XdslDevIfStatsRemoteOctetsCorrected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 21),
    _XdslDevIfStatsRemoteOctetsCorrected_Type()
)
xdslDevIfStatsRemoteOctetsCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteOctetsCorrected.setStatus("mandatory")
_XdslDevIfStatsRemoteOctetsNotCorrected_Type = Counter32
_XdslDevIfStatsRemoteOctetsNotCorrected_Object = MibTableColumn
xdslDevIfStatsRemoteOctetsNotCorrected = _XdslDevIfStatsRemoteOctetsNotCorrected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 22),
    _XdslDevIfStatsRemoteOctetsNotCorrected_Type()
)
xdslDevIfStatsRemoteOctetsNotCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteOctetsNotCorrected.setStatus("mandatory")
_XdslDevIfStatsRemoteReceivedKiloOctets_Type = Counter32
_XdslDevIfStatsRemoteReceivedKiloOctets_Object = MibTableColumn
xdslDevIfStatsRemoteReceivedKiloOctets = _XdslDevIfStatsRemoteReceivedKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 23),
    _XdslDevIfStatsRemoteReceivedKiloOctets_Type()
)
xdslDevIfStatsRemoteReceivedKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteReceivedKiloOctets.setStatus("mandatory")
_XdslDevIfStatsRemoteReceivedPkts_Type = Counter32
_XdslDevIfStatsRemoteReceivedPkts_Object = MibTableColumn
xdslDevIfStatsRemoteReceivedPkts = _XdslDevIfStatsRemoteReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 24),
    _XdslDevIfStatsRemoteReceivedPkts_Type()
)
xdslDevIfStatsRemoteReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteReceivedPkts.setStatus("mandatory")
_XdslDevIfStatsRemoteRecErrPkts_Type = Counter32
_XdslDevIfStatsRemoteRecErrPkts_Object = MibTableColumn
xdslDevIfStatsRemoteRecErrPkts = _XdslDevIfStatsRemoteRecErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 25),
    _XdslDevIfStatsRemoteRecErrPkts_Type()
)
xdslDevIfStatsRemoteRecErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecErrPkts.setStatus("mandatory")
_XdslDevIfStatsRemoteDroppedPkts_Type = Counter32
_XdslDevIfStatsRemoteDroppedPkts_Object = MibTableColumn
xdslDevIfStatsRemoteDroppedPkts = _XdslDevIfStatsRemoteDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 26),
    _XdslDevIfStatsRemoteDroppedPkts_Type()
)
xdslDevIfStatsRemoteDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteDroppedPkts.setStatus("mandatory")
_XdslDevIfStatsRemoteTransmittedKiloOctets_Type = Counter32
_XdslDevIfStatsRemoteTransmittedKiloOctets_Object = MibTableColumn
xdslDevIfStatsRemoteTransmittedKiloOctets = _XdslDevIfStatsRemoteTransmittedKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 27),
    _XdslDevIfStatsRemoteTransmittedKiloOctets_Type()
)
xdslDevIfStatsRemoteTransmittedKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteTransmittedKiloOctets.setStatus("mandatory")
_XdslDevIfStatsRemoteTransmittedPkts_Type = Counter32
_XdslDevIfStatsRemoteTransmittedPkts_Object = MibTableColumn
xdslDevIfStatsRemoteTransmittedPkts = _XdslDevIfStatsRemoteTransmittedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 28),
    _XdslDevIfStatsRemoteTransmittedPkts_Type()
)
xdslDevIfStatsRemoteTransmittedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteTransmittedPkts.setStatus("mandatory")
_XdslDevIfStatsCentralRecErroredMinutes_Type = Integer32
_XdslDevIfStatsCentralRecErroredMinutes_Object = MibTableColumn
xdslDevIfStatsCentralRecErroredMinutes = _XdslDevIfStatsCentralRecErroredMinutes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 29),
    _XdslDevIfStatsCentralRecErroredMinutes_Type()
)
xdslDevIfStatsCentralRecErroredMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecErroredMinutes.setStatus("mandatory")
_XdslDevIfStatsCentralRecSeverelyErroredMinutes_Type = Integer32
_XdslDevIfStatsCentralRecSeverelyErroredMinutes_Object = MibTableColumn
xdslDevIfStatsCentralRecSeverelyErroredMinutes = _XdslDevIfStatsCentralRecSeverelyErroredMinutes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 30),
    _XdslDevIfStatsCentralRecSeverelyErroredMinutes_Type()
)
xdslDevIfStatsCentralRecSeverelyErroredMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralRecSeverelyErroredMinutes.setStatus("mandatory")
_XdslDevIfStatsRemoteRecErroredMinutes_Type = Integer32
_XdslDevIfStatsRemoteRecErroredMinutes_Object = MibTableColumn
xdslDevIfStatsRemoteRecErroredMinutes = _XdslDevIfStatsRemoteRecErroredMinutes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 31),
    _XdslDevIfStatsRemoteRecErroredMinutes_Type()
)
xdslDevIfStatsRemoteRecErroredMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecErroredMinutes.setStatus("mandatory")
_XdslDevIfStatsRemoteRecSeverelyErroredMinutes_Type = Integer32
_XdslDevIfStatsRemoteRecSeverelyErroredMinutes_Object = MibTableColumn
xdslDevIfStatsRemoteRecSeverelyErroredMinutes = _XdslDevIfStatsRemoteRecSeverelyErroredMinutes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 32),
    _XdslDevIfStatsRemoteRecSeverelyErroredMinutes_Type()
)
xdslDevIfStatsRemoteRecSeverelyErroredMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsRemoteRecSeverelyErroredMinutes.setStatus("mandatory")
_XdslDevIfStatsCentralReceivedKiloOctets_Type = Counter32
_XdslDevIfStatsCentralReceivedKiloOctets_Object = MibTableColumn
xdslDevIfStatsCentralReceivedKiloOctets = _XdslDevIfStatsCentralReceivedKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 33),
    _XdslDevIfStatsCentralReceivedKiloOctets_Type()
)
xdslDevIfStatsCentralReceivedKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralReceivedKiloOctets.setStatus("mandatory")
_XdslDevIfStatsCentralTransmittedKiloOctets_Type = Counter32
_XdslDevIfStatsCentralTransmittedKiloOctets_Object = MibTableColumn
xdslDevIfStatsCentralTransmittedKiloOctets = _XdslDevIfStatsCentralTransmittedKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 34),
    _XdslDevIfStatsCentralTransmittedKiloOctets_Type()
)
xdslDevIfStatsCentralTransmittedKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralTransmittedKiloOctets.setStatus("mandatory")
_XdslDevIfStatsCentralTransmittedPkts_Type = Counter32
_XdslDevIfStatsCentralTransmittedPkts_Object = MibTableColumn
xdslDevIfStatsCentralTransmittedPkts = _XdslDevIfStatsCentralTransmittedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 35),
    _XdslDevIfStatsCentralTransmittedPkts_Type()
)
xdslDevIfStatsCentralTransmittedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralTransmittedPkts.setStatus("mandatory")
_XdslDevIfStatsCentralReceivedPkts_Type = Counter32
_XdslDevIfStatsCentralReceivedPkts_Object = MibTableColumn
xdslDevIfStatsCentralReceivedPkts = _XdslDevIfStatsCentralReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 36),
    _XdslDevIfStatsCentralReceivedPkts_Type()
)
xdslDevIfStatsCentralReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralReceivedPkts.setStatus("mandatory")
_XdslDevIfStatsCentralErrPkts_Type = Counter32
_XdslDevIfStatsCentralErrPkts_Object = MibTableColumn
xdslDevIfStatsCentralErrPkts = _XdslDevIfStatsCentralErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 1, 1, 1, 37),
    _XdslDevIfStatsCentralErrPkts_Type()
)
xdslDevIfStatsCentralErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfStatsCentralErrPkts.setStatus("mandatory")
_XdslDevIfConfig_ObjectIdentity = ObjectIdentity
xdslDevIfConfig = _XdslDevIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2)
)
_XdslDevIfConfigTable_Object = MibTable
xdslDevIfConfigTable = _XdslDevIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xdslDevIfConfigTable.setStatus("mandatory")
_XdslDevIfConfigEntry_Object = MibTableRow
xdslDevIfConfigEntry = _XdslDevIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1)
)
xdslDevIfConfigEntry.setIndexNames(
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslDevIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    xdslDevIfConfigEntry.setStatus("mandatory")
_XdslDevIfConfigIfIndex_Type = Integer32
_XdslDevIfConfigIfIndex_Object = MibTableColumn
xdslDevIfConfigIfIndex = _XdslDevIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 1),
    _XdslDevIfConfigIfIndex_Type()
)
xdslDevIfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevIfConfigIfIndex.setStatus("mandatory")


class _XdslDevIfConfigPortSpeedBehaviour_Type(Integer32):
    """Custom type xdslDevIfConfigPortSpeedBehaviour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_XdslDevIfConfigPortSpeedBehaviour_Type.__name__ = "Integer32"
_XdslDevIfConfigPortSpeedBehaviour_Object = MibTableColumn
xdslDevIfConfigPortSpeedBehaviour = _XdslDevIfConfigPortSpeedBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 2),
    _XdslDevIfConfigPortSpeedBehaviour_Type()
)
xdslDevIfConfigPortSpeedBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigPortSpeedBehaviour.setStatus("mandatory")


class _XdslDevIfConfigUpFixedPortSpeed_Type(Integer32):
    """Custom type xdslDevIfConfigUpFixedPortSpeed based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("s102", 14),
          ("s1040", 24),
          ("s1088", 7),
          ("s11", 20),
          ("s119", 13),
          ("s136", 12),
          ("s144", 29),
          ("s1552", 23),
          ("s204", 11),
          ("s2046", 22),
          ("s2320", 21),
          ("s272", 1),
          ("s277", 28),
          ("s34", 19),
          ("s340", 10),
          ("s400", 27),
          ("s408", 2),
          ("s45", 18),
          ("s476", 9),
          ("s51", 17),
          ("s528", 26),
          ("s544", 3),
          ("s68", 16),
          ("s680", 4),
          ("s784", 25),
          ("s816", 5),
          ("s85", 15),
          ("s91", 8),
          ("s952", 6))
    )


_XdslDevIfConfigUpFixedPortSpeed_Type.__name__ = "Integer32"
_XdslDevIfConfigUpFixedPortSpeed_Object = MibTableColumn
xdslDevIfConfigUpFixedPortSpeed = _XdslDevIfConfigUpFixedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 3),
    _XdslDevIfConfigUpFixedPortSpeed_Type()
)
xdslDevIfConfigUpFixedPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigUpFixedPortSpeed.setStatus("mandatory")


class _XdslDevIfConfigDownFixedPortSpeed_Type(Integer32):
    """Custom type xdslDevIfConfigDownFixedPortSpeed based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("s1024", 14),
          ("s1040", 23),
          ("s1280", 3),
          ("s144", 28),
          ("s1552", 22),
          ("s1600", 4),
          ("s1920", 5),
          ("s2046", 21),
          ("s2240", 6),
          ("s2320", 20),
          ("s256", 19),
          ("s2560", 7),
          ("s2688", 8),
          ("s277", 27),
          ("s3200", 9),
          ("s384", 18),
          ("s400", 26),
          ("s4480", 10),
          ("s512", 17),
          ("s5120", 11),
          ("s528", 25),
          ("s6272", 12),
          ("s640", 1),
          ("s7168", 13),
          ("s768", 16),
          ("s784", 24),
          ("s896", 15),
          ("s960", 2))
    )


_XdslDevIfConfigDownFixedPortSpeed_Type.__name__ = "Integer32"
_XdslDevIfConfigDownFixedPortSpeed_Object = MibTableColumn
xdslDevIfConfigDownFixedPortSpeed = _XdslDevIfConfigDownFixedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 4),
    _XdslDevIfConfigDownFixedPortSpeed_Type()
)
xdslDevIfConfigDownFixedPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigDownFixedPortSpeed.setStatus("mandatory")


class _XdslDevIfConfigUpAdaptiveUpperBoundPortSpeed_Type(Integer32):
    """Custom type xdslDevIfConfigUpAdaptiveUpperBoundPortSpeed based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("s102", 14),
          ("s1088", 7),
          ("s11", 20),
          ("s119", 13),
          ("s136", 12),
          ("s204", 11),
          ("s272", 1),
          ("s34", 19),
          ("s340", 10),
          ("s408", 2),
          ("s45", 18),
          ("s476", 9),
          ("s51", 17),
          ("s544", 3),
          ("s68", 16),
          ("s680", 4),
          ("s816", 5),
          ("s85", 15),
          ("s91", 8),
          ("s952", 6))
    )


_XdslDevIfConfigUpAdaptiveUpperBoundPortSpeed_Type.__name__ = "Integer32"
_XdslDevIfConfigUpAdaptiveUpperBoundPortSpeed_Object = MibTableColumn
xdslDevIfConfigUpAdaptiveUpperBoundPortSpeed = _XdslDevIfConfigUpAdaptiveUpperBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 5),
    _XdslDevIfConfigUpAdaptiveUpperBoundPortSpeed_Type()
)
xdslDevIfConfigUpAdaptiveUpperBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigUpAdaptiveUpperBoundPortSpeed.setStatus("mandatory")


class _XdslDevIfConfigUpAdaptiveLowerBoundPortSpeed_Type(Integer32):
    """Custom type xdslDevIfConfigUpAdaptiveLowerBoundPortSpeed based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("s102", 14),
          ("s1088", 7),
          ("s11", 20),
          ("s119", 13),
          ("s136", 12),
          ("s204", 11),
          ("s272", 1),
          ("s34", 19),
          ("s340", 10),
          ("s408", 2),
          ("s45", 18),
          ("s476", 9),
          ("s51", 17),
          ("s544", 3),
          ("s68", 16),
          ("s680", 4),
          ("s816", 5),
          ("s85", 15),
          ("s91", 8),
          ("s952", 6))
    )


_XdslDevIfConfigUpAdaptiveLowerBoundPortSpeed_Type.__name__ = "Integer32"
_XdslDevIfConfigUpAdaptiveLowerBoundPortSpeed_Object = MibTableColumn
xdslDevIfConfigUpAdaptiveLowerBoundPortSpeed = _XdslDevIfConfigUpAdaptiveLowerBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 6),
    _XdslDevIfConfigUpAdaptiveLowerBoundPortSpeed_Type()
)
xdslDevIfConfigUpAdaptiveLowerBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigUpAdaptiveLowerBoundPortSpeed.setStatus("mandatory")


class _XdslDevIfConfigDownAdaptiveUpperBoundPortSpeed_Type(Integer32):
    """Custom type xdslDevIfConfigDownAdaptiveUpperBoundPortSpeed based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("s1024", 14),
          ("s1280", 3),
          ("s1600", 4),
          ("s1920", 5),
          ("s2240", 6),
          ("s256", 19),
          ("s2560", 7),
          ("s2688", 8),
          ("s3200", 9),
          ("s384", 18),
          ("s4480", 10),
          ("s512", 17),
          ("s5120", 11),
          ("s6272", 12),
          ("s640", 1),
          ("s7168", 13),
          ("s768", 16),
          ("s896", 15),
          ("s960", 2))
    )


_XdslDevIfConfigDownAdaptiveUpperBoundPortSpeed_Type.__name__ = "Integer32"
_XdslDevIfConfigDownAdaptiveUpperBoundPortSpeed_Object = MibTableColumn
xdslDevIfConfigDownAdaptiveUpperBoundPortSpeed = _XdslDevIfConfigDownAdaptiveUpperBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 7),
    _XdslDevIfConfigDownAdaptiveUpperBoundPortSpeed_Type()
)
xdslDevIfConfigDownAdaptiveUpperBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigDownAdaptiveUpperBoundPortSpeed.setStatus("mandatory")


class _XdslDevIfConfigDownAdaptiveLowerBoundPortSpeed_Type(Integer32):
    """Custom type xdslDevIfConfigDownAdaptiveLowerBoundPortSpeed based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("s1024", 14),
          ("s1280", 3),
          ("s1600", 4),
          ("s1920", 5),
          ("s2240", 6),
          ("s256", 19),
          ("s2560", 7),
          ("s2688", 8),
          ("s3200", 9),
          ("s384", 18),
          ("s4480", 10),
          ("s512", 17),
          ("s5120", 11),
          ("s6272", 12),
          ("s640", 1),
          ("s7168", 13),
          ("s768", 16),
          ("s896", 15),
          ("s960", 2))
    )


_XdslDevIfConfigDownAdaptiveLowerBoundPortSpeed_Type.__name__ = "Integer32"
_XdslDevIfConfigDownAdaptiveLowerBoundPortSpeed_Object = MibTableColumn
xdslDevIfConfigDownAdaptiveLowerBoundPortSpeed = _XdslDevIfConfigDownAdaptiveLowerBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 8),
    _XdslDevIfConfigDownAdaptiveLowerBoundPortSpeed_Type()
)
xdslDevIfConfigDownAdaptiveLowerBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigDownAdaptiveLowerBoundPortSpeed.setStatus("mandatory")


class _XdslDevIfConfigReedSolomonDownForwardErrorCorrection_Type(Integer32):
    """Custom type xdslDevIfConfigReedSolomonDownForwardErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minimizeDelay", 2),
          ("minimizeError", 1),
          ("reedSolomonNotSupported", 3))
    )


_XdslDevIfConfigReedSolomonDownForwardErrorCorrection_Type.__name__ = "Integer32"
_XdslDevIfConfigReedSolomonDownForwardErrorCorrection_Object = MibTableColumn
xdslDevIfConfigReedSolomonDownForwardErrorCorrection = _XdslDevIfConfigReedSolomonDownForwardErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 9),
    _XdslDevIfConfigReedSolomonDownForwardErrorCorrection_Type()
)
xdslDevIfConfigReedSolomonDownForwardErrorCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigReedSolomonDownForwardErrorCorrection.setStatus("mandatory")
_XdslDevIfConfigMarginThreshold_Type = Integer32
_XdslDevIfConfigMarginThreshold_Object = MibTableColumn
xdslDevIfConfigMarginThreshold = _XdslDevIfConfigMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 10),
    _XdslDevIfConfigMarginThreshold_Type()
)
xdslDevIfConfigMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigMarginThreshold.setStatus("mandatory")
_XdslDevIfConfigEstimatedHrErrRateThreshold_Type = Integer32
_XdslDevIfConfigEstimatedHrErrRateThreshold_Object = MibTableColumn
xdslDevIfConfigEstimatedHrErrRateThreshold = _XdslDevIfConfigEstimatedHrErrRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 11),
    _XdslDevIfConfigEstimatedHrErrRateThreshold_Type()
)
xdslDevIfConfigEstimatedHrErrRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigEstimatedHrErrRateThreshold.setStatus("mandatory")
_XdslDevIfConfigEstimatedDayErrRateThreshold_Type = Integer32
_XdslDevIfConfigEstimatedDayErrRateThreshold_Object = MibTableColumn
xdslDevIfConfigEstimatedDayErrRateThreshold = _XdslDevIfConfigEstimatedDayErrRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 12),
    _XdslDevIfConfigEstimatedDayErrRateThreshold_Type()
)
xdslDevIfConfigEstimatedDayErrRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigEstimatedDayErrRateThreshold.setStatus("mandatory")


class _XdslDevIfConfigPortID_Type(DisplayString):
    """Custom type xdslDevIfConfigPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_XdslDevIfConfigPortID_Type.__name__ = "DisplayString"
_XdslDevIfConfigPortID_Object = MibTableColumn
xdslDevIfConfigPortID = _XdslDevIfConfigPortID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 13),
    _XdslDevIfConfigPortID_Type()
)
xdslDevIfConfigPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigPortID.setStatus("mandatory")
_XdslDevIfLinkUpDownTransitionThreshold_Type = Integer32
_XdslDevIfLinkUpDownTransitionThreshold_Object = MibTableColumn
xdslDevIfLinkUpDownTransitionThreshold = _XdslDevIfLinkUpDownTransitionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 14),
    _XdslDevIfLinkUpDownTransitionThreshold_Type()
)
xdslDevIfLinkUpDownTransitionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfLinkUpDownTransitionThreshold.setStatus("mandatory")


class _XdslDevIfConfigStartUpMargin_Type(Integer32):
    """Custom type xdslDevIfConfigStartUpMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 9),
    )


_XdslDevIfConfigStartUpMargin_Type.__name__ = "Integer32"
_XdslDevIfConfigStartUpMargin_Object = MibTableColumn
xdslDevIfConfigStartUpMargin = _XdslDevIfConfigStartUpMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 15),
    _XdslDevIfConfigStartUpMargin_Type()
)
xdslDevIfConfigStartUpMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigStartUpMargin.setStatus("mandatory")
_XdslDevIfConfigTxPowerAttenuation_Type = Integer32
_XdslDevIfConfigTxPowerAttenuation_Object = MibTableColumn
xdslDevIfConfigTxPowerAttenuation = _XdslDevIfConfigTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 16),
    _XdslDevIfConfigTxPowerAttenuation_Type()
)
xdslDevIfConfigTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigTxPowerAttenuation.setStatus("mandatory")
_XdslDevIfConfigSnTxPowerAttenuation_Type = Integer32
_XdslDevIfConfigSnTxPowerAttenuation_Object = MibTableColumn
xdslDevIfConfigSnTxPowerAttenuation = _XdslDevIfConfigSnTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 2, 1, 1, 17),
    _XdslDevIfConfigSnTxPowerAttenuation_Type()
)
xdslDevIfConfigSnTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIfConfigSnTxPowerAttenuation.setStatus("mandatory")
_XdslRemoteSys_ObjectIdentity = ObjectIdentity
xdslRemoteSys = _XdslRemoteSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3)
)
_XdslRemoteSysTable_Object = MibTable
xdslRemoteSysTable = _XdslRemoteSysTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xdslRemoteSysTable.setStatus("mandatory")
_XdslRemoteSysEntry_Object = MibTableRow
xdslRemoteSysEntry = _XdslRemoteSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1)
)
xdslRemoteSysEntry.setIndexNames(
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslRemoteSysIndex"),
)
if mibBuilder.loadTexts:
    xdslRemoteSysEntry.setStatus("mandatory")
_XdslRemoteSysIndex_Type = Integer32
_XdslRemoteSysIndex_Object = MibTableColumn
xdslRemoteSysIndex = _XdslRemoteSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 1),
    _XdslRemoteSysIndex_Type()
)
xdslRemoteSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteSysIndex.setStatus("mandatory")


class _XdslRemoteSysDescr_Type(DisplayString):
    """Custom type xdslRemoteSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XdslRemoteSysDescr_Type.__name__ = "DisplayString"
_XdslRemoteSysDescr_Object = MibTableColumn
xdslRemoteSysDescr = _XdslRemoteSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 2),
    _XdslRemoteSysDescr_Type()
)
xdslRemoteSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteSysDescr.setStatus("mandatory")
_XdslRemoteSysObjectID_Type = ObjectIdentifier
_XdslRemoteSysObjectID_Object = MibTableColumn
xdslRemoteSysObjectID = _XdslRemoteSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 3),
    _XdslRemoteSysObjectID_Type()
)
xdslRemoteSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteSysObjectID.setStatus("mandatory")
_XdslRemoteSysUpTime_Type = TimeTicks
_XdslRemoteSysUpTime_Object = MibTableColumn
xdslRemoteSysUpTime = _XdslRemoteSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 4),
    _XdslRemoteSysUpTime_Type()
)
xdslRemoteSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteSysUpTime.setStatus("mandatory")


class _XdslRemoteSysContact_Type(DisplayString):
    """Custom type xdslRemoteSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XdslRemoteSysContact_Type.__name__ = "DisplayString"
_XdslRemoteSysContact_Object = MibTableColumn
xdslRemoteSysContact = _XdslRemoteSysContact_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 5),
    _XdslRemoteSysContact_Type()
)
xdslRemoteSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslRemoteSysContact.setStatus("mandatory")


class _XdslRemoteSysName_Type(DisplayString):
    """Custom type xdslRemoteSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XdslRemoteSysName_Type.__name__ = "DisplayString"
_XdslRemoteSysName_Object = MibTableColumn
xdslRemoteSysName = _XdslRemoteSysName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 6),
    _XdslRemoteSysName_Type()
)
xdslRemoteSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslRemoteSysName.setStatus("mandatory")


class _XdslRemoteSysLocation_Type(DisplayString):
    """Custom type xdslRemoteSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XdslRemoteSysLocation_Type.__name__ = "DisplayString"
_XdslRemoteSysLocation_Object = MibTableColumn
xdslRemoteSysLocation = _XdslRemoteSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 7),
    _XdslRemoteSysLocation_Type()
)
xdslRemoteSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslRemoteSysLocation.setStatus("mandatory")


class _XdslRemoteSysServices_Type(Integer32):
    """Custom type xdslRemoteSysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_XdslRemoteSysServices_Type.__name__ = "Integer32"
_XdslRemoteSysServices_Object = MibTableColumn
xdslRemoteSysServices = _XdslRemoteSysServices_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 8),
    _XdslRemoteSysServices_Type()
)
xdslRemoteSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteSysServices.setStatus("mandatory")


class _XdslRemoteSysCircuitId_Type(DisplayString):
    """Custom type xdslRemoteSysCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_XdslRemoteSysCircuitId_Type.__name__ = "DisplayString"
_XdslRemoteSysCircuitId_Object = MibTableColumn
xdslRemoteSysCircuitId = _XdslRemoteSysCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 3, 1, 1, 9),
    _XdslRemoteSysCircuitId_Type()
)
xdslRemoteSysCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteSysCircuitId.setStatus("mandatory")
_XdslRemoteDTEStatus_ObjectIdentity = ObjectIdentity
xdslRemoteDTEStatus = _XdslRemoteDTEStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4)
)
_XdslRemoteDTEStatusTable_Object = MibTable
xdslRemoteDTEStatusTable = _XdslRemoteDTEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xdslRemoteDTEStatusTable.setStatus("mandatory")
_XdslRemoteDTEStatusEntry_Object = MibTableRow
xdslRemoteDTEStatusEntry = _XdslRemoteDTEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1)
)
xdslRemoteDTEStatusEntry.setIndexNames(
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslRemoteDTEStatusIndex"),
)
if mibBuilder.loadTexts:
    xdslRemoteDTEStatusEntry.setStatus("mandatory")
_XdslRemoteDTEStatusIndex_Type = Integer32
_XdslRemoteDTEStatusIndex_Object = MibTableColumn
xdslRemoteDTEStatusIndex = _XdslRemoteDTEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1, 1),
    _XdslRemoteDTEStatusIndex_Type()
)
xdslRemoteDTEStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteDTEStatusIndex.setStatus("mandatory")


class _XdslRemoteDTEState_Type(Integer32):
    """Custom type xdslRemoteDTEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_XdslRemoteDTEState_Type.__name__ = "Integer32"
_XdslRemoteDTEState_Object = MibTableColumn
xdslRemoteDTEState = _XdslRemoteDTEState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1, 2),
    _XdslRemoteDTEState_Type()
)
xdslRemoteDTEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteDTEState.setStatus("mandatory")


class _XdslRemoteDTEType_Type(Integer32):
    """Custom type xdslRemoteDTEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eia530", 2),
          ("v35", 1))
    )


_XdslRemoteDTEType_Type.__name__ = "Integer32"
_XdslRemoteDTEType_Object = MibTableColumn
xdslRemoteDTEType = _XdslRemoteDTEType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1, 3),
    _XdslRemoteDTEType_Type()
)
xdslRemoteDTEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteDTEType.setStatus("mandatory")


class _XdslRemoteDTEClockSource_Type(Integer32):
    """Custom type xdslRemoteDTEClockSource based on Integer32"""
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


_XdslRemoteDTEClockSource_Type.__name__ = "Integer32"
_XdslRemoteDTEClockSource_Object = MibTableColumn
xdslRemoteDTEClockSource = _XdslRemoteDTEClockSource_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1, 4),
    _XdslRemoteDTEClockSource_Type()
)
xdslRemoteDTEClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteDTEClockSource.setStatus("mandatory")


class _XdslRemoteDTEStrobe_Type(Integer32):
    """Custom type xdslRemoteDTEStrobe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallingEdge", 2),
          ("risingEdge", 1))
    )


_XdslRemoteDTEStrobe_Type.__name__ = "Integer32"
_XdslRemoteDTEStrobe_Object = MibTableColumn
xdslRemoteDTEStrobe = _XdslRemoteDTEStrobe_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1, 5),
    _XdslRemoteDTEStrobe_Type()
)
xdslRemoteDTEStrobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteDTEStrobe.setStatus("mandatory")


class _XdslRemoteDTELoopbackState_Type(Integer32):
    """Custom type xdslRemoteDTELoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_XdslRemoteDTELoopbackState_Type.__name__ = "Integer32"
_XdslRemoteDTELoopbackState_Object = MibTableColumn
xdslRemoteDTELoopbackState = _XdslRemoteDTELoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 4, 1, 1, 6),
    _XdslRemoteDTELoopbackState_Type()
)
xdslRemoteDTELoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslRemoteDTELoopbackState.setStatus("mandatory")
_XdslDevMvlIfConfig_ObjectIdentity = ObjectIdentity
xdslDevMvlIfConfig = _XdslDevMvlIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5)
)
_XdslDevMvlIfConfigTable_Object = MibTable
xdslDevMvlIfConfigTable = _XdslDevMvlIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigTable.setStatus("mandatory")
_XdslDevMvlIfConfigEntry_Object = MibTableRow
xdslDevMvlIfConfigEntry = _XdslDevMvlIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1)
)
xdslDevMvlIfConfigEntry.setIndexNames(
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslDevMvlIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigEntry.setStatus("mandatory")
_XdslDevMvlIfConfigIfIndex_Type = Integer32
_XdslDevMvlIfConfigIfIndex_Object = MibTableColumn
xdslDevMvlIfConfigIfIndex = _XdslDevMvlIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 1),
    _XdslDevMvlIfConfigIfIndex_Type()
)
xdslDevMvlIfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigIfIndex.setStatus("mandatory")
_XdslDevMvlIfConfigUpperBoundPortSpeed_Type = Integer32
_XdslDevMvlIfConfigUpperBoundPortSpeed_Object = MibTableColumn
xdslDevMvlIfConfigUpperBoundPortSpeed = _XdslDevMvlIfConfigUpperBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 2),
    _XdslDevMvlIfConfigUpperBoundPortSpeed_Type()
)
xdslDevMvlIfConfigUpperBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigUpperBoundPortSpeed.setStatus("mandatory")
_XdslDevMvlIfConfigMarginThreshold_Type = Integer32
_XdslDevMvlIfConfigMarginThreshold_Object = MibTableColumn
xdslDevMvlIfConfigMarginThreshold = _XdslDevMvlIfConfigMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 3),
    _XdslDevMvlIfConfigMarginThreshold_Type()
)
xdslDevMvlIfConfigMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigMarginThreshold.setStatus("mandatory")


class _XdslDevMvlIfConfigPortID_Type(DisplayString):
    """Custom type xdslDevMvlIfConfigPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_XdslDevMvlIfConfigPortID_Type.__name__ = "DisplayString"
_XdslDevMvlIfConfigPortID_Object = MibTableColumn
xdslDevMvlIfConfigPortID = _XdslDevMvlIfConfigPortID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 4),
    _XdslDevMvlIfConfigPortID_Type()
)
xdslDevMvlIfConfigPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigPortID.setStatus("mandatory")
_XdslDevMvlIfLinkUpDownTransitionThreshold_Type = Integer32
_XdslDevMvlIfLinkUpDownTransitionThreshold_Object = MibTableColumn
xdslDevMvlIfLinkUpDownTransitionThreshold = _XdslDevMvlIfLinkUpDownTransitionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 5),
    _XdslDevMvlIfLinkUpDownTransitionThreshold_Type()
)
xdslDevMvlIfLinkUpDownTransitionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMvlIfLinkUpDownTransitionThreshold.setStatus("mandatory")
_XdslDevMvlIfConfigOnHookTxPowerAttenuation_Type = Integer32
_XdslDevMvlIfConfigOnHookTxPowerAttenuation_Object = MibTableColumn
xdslDevMvlIfConfigOnHookTxPowerAttenuation = _XdslDevMvlIfConfigOnHookTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 6),
    _XdslDevMvlIfConfigOnHookTxPowerAttenuation_Type()
)
xdslDevMvlIfConfigOnHookTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigOnHookTxPowerAttenuation.setStatus("mandatory")
_XdslDevMvlIfConfigOffHookTxPowerAttenuation_Type = Integer32
_XdslDevMvlIfConfigOffHookTxPowerAttenuation_Object = MibTableColumn
xdslDevMvlIfConfigOffHookTxPowerAttenuation = _XdslDevMvlIfConfigOffHookTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 5, 1, 1, 7),
    _XdslDevMvlIfConfigOffHookTxPowerAttenuation_Type()
)
xdslDevMvlIfConfigOffHookTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMvlIfConfigOffHookTxPowerAttenuation.setStatus("mandatory")
_XdslDevNAPCustomerAccount_ObjectIdentity = ObjectIdentity
xdslDevNAPCustomerAccount = _XdslDevNAPCustomerAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6)
)
_XdslDevNAPCustomerAccountTable_Object = MibTable
xdslDevNAPCustomerAccountTable = _XdslDevNAPCustomerAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xdslDevNAPCustomerAccountTable.setStatus("mandatory")
_XdslDevNAPCustomerAccountEntry_Object = MibTableRow
xdslDevNAPCustomerAccountEntry = _XdslDevNAPCustomerAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6, 1, 1)
)
xdslDevNAPCustomerAccountEntry.setIndexNames(
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslDevNAPCustomerAccountIfIndex"),
    (0, "HOTWIRE-XDSL-INTERFACE-MIB", "xdslDevNAPCustomerAccountInterval"),
)
if mibBuilder.loadTexts:
    xdslDevNAPCustomerAccountEntry.setStatus("mandatory")
_XdslDevNAPCustomerAccountIfIndex_Type = Integer32
_XdslDevNAPCustomerAccountIfIndex_Object = MibTableColumn
xdslDevNAPCustomerAccountIfIndex = _XdslDevNAPCustomerAccountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6, 1, 1, 1),
    _XdslDevNAPCustomerAccountIfIndex_Type()
)
xdslDevNAPCustomerAccountIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevNAPCustomerAccountIfIndex.setStatus("mandatory")


class _XdslDevNAPCustomerAccountInterval_Type(Integer32):
    """Custom type xdslDevNAPCustomerAccountInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentDay", 1),
          ("previousDay", 2))
    )


_XdslDevNAPCustomerAccountInterval_Type.__name__ = "Integer32"
_XdslDevNAPCustomerAccountInterval_Object = MibTableColumn
xdslDevNAPCustomerAccountInterval = _XdslDevNAPCustomerAccountInterval_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6, 1, 1, 2),
    _XdslDevNAPCustomerAccountInterval_Type()
)
xdslDevNAPCustomerAccountInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevNAPCustomerAccountInterval.setStatus("mandatory")
_XdslDevNAPCustomerAccountRecKiloOctets_Type = Integer32
_XdslDevNAPCustomerAccountRecKiloOctets_Object = MibTableColumn
xdslDevNAPCustomerAccountRecKiloOctets = _XdslDevNAPCustomerAccountRecKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6, 1, 1, 3),
    _XdslDevNAPCustomerAccountRecKiloOctets_Type()
)
xdslDevNAPCustomerAccountRecKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevNAPCustomerAccountRecKiloOctets.setStatus("mandatory")
_XdslDevNAPCustomerAccountTrxKiloOctets_Type = Integer32
_XdslDevNAPCustomerAccountTrxKiloOctets_Object = MibTableColumn
xdslDevNAPCustomerAccountTrxKiloOctets = _XdslDevNAPCustomerAccountTrxKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 6, 1, 1, 4),
    _XdslDevNAPCustomerAccountTrxKiloOctets_Type()
)
xdslDevNAPCustomerAccountTrxKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevNAPCustomerAccountTrxKiloOctets.setStatus("mandatory")
_XdslLinkUpDownInformation_ObjectIdentity = ObjectIdentity
xdslLinkUpDownInformation = _XdslLinkUpDownInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 7)
)


class _XdslLinkDownReason_Type(DisplayString):
    """Custom type xdslLinkDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_XdslLinkDownReason_Type.__name__ = "DisplayString"
_XdslLinkDownReason_Object = MibScalar
xdslLinkDownReason = _XdslLinkDownReason_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 7, 1),
    _XdslLinkDownReason_Type()
)
xdslLinkDownReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdslLinkDownReason.setStatus("mandatory")
_XdslRemoteInjection_ObjectIdentity = ObjectIdentity
xdslRemoteInjection = _XdslRemoteInjection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 8)
)


class _XdslRemoteInjectionType_Type(Integer32):
    """Custom type xdslRemoteInjectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("filter", 1)
    )


_XdslRemoteInjectionType_Type.__name__ = "Integer32"
_XdslRemoteInjectionType_Object = MibScalar
xdslRemoteInjectionType = _XdslRemoteInjectionType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 8, 1),
    _XdslRemoteInjectionType_Type()
)
xdslRemoteInjectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdslRemoteInjectionType.setStatus("deprecated")
_XdslDevIDSLConfig_ObjectIdentity = ObjectIdentity
xdslDevIDSLConfig = _XdslDevIDSLConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9)
)
_XdslDevIDSLConfigTable_Object = MibTable
xdslDevIDSLConfigTable = _XdslDevIDSLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xdslDevIDSLConfigTable.setStatus("mandatory")
_XdslDevIDSLConfigEntry_Object = MibTableRow
xdslDevIDSLConfigEntry = _XdslDevIDSLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1)
)
xdslDevIDSLConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdslDevIDSLConfigEntry.setStatus("mandatory")


class _XdslDevIDSLConfigPortSpeedBehaviour_Type(Integer32):
    """Custom type xdslDevIDSLConfigPortSpeedBehaviour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_XdslDevIDSLConfigPortSpeedBehaviour_Type.__name__ = "Integer32"
_XdslDevIDSLConfigPortSpeedBehaviour_Object = MibTableColumn
xdslDevIDSLConfigPortSpeedBehaviour = _XdslDevIDSLConfigPortSpeedBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1, 1),
    _XdslDevIDSLConfigPortSpeedBehaviour_Type()
)
xdslDevIDSLConfigPortSpeedBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLConfigPortSpeedBehaviour.setStatus("mandatory")
_XdslDevIDSLConfigPortSpeed_Type = Integer32
_XdslDevIDSLConfigPortSpeed_Object = MibTableColumn
xdslDevIDSLConfigPortSpeed = _XdslDevIDSLConfigPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1, 2),
    _XdslDevIDSLConfigPortSpeed_Type()
)
xdslDevIDSLConfigPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLConfigPortSpeed.setStatus("mandatory")


class _XdslDevIDSLConfigPortID_Type(DisplayString):
    """Custom type xdslDevIDSLConfigPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_XdslDevIDSLConfigPortID_Type.__name__ = "DisplayString"
_XdslDevIDSLConfigPortID_Object = MibTableColumn
xdslDevIDSLConfigPortID = _XdslDevIDSLConfigPortID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1, 3),
    _XdslDevIDSLConfigPortID_Type()
)
xdslDevIDSLConfigPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLConfigPortID.setStatus("mandatory")


class _XdslDevIDSLTimingPortTransceiverMode_Type(Integer32):
    """Custom type xdslDevIDSLTimingPortTransceiverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("networkTiming", 1))
    )


_XdslDevIDSLTimingPortTransceiverMode_Type.__name__ = "Integer32"
_XdslDevIDSLTimingPortTransceiverMode_Object = MibTableColumn
xdslDevIDSLTimingPortTransceiverMode = _XdslDevIDSLTimingPortTransceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1, 4),
    _XdslDevIDSLTimingPortTransceiverMode_Type()
)
xdslDevIDSLTimingPortTransceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLTimingPortTransceiverMode.setStatus("mandatory")
_XdslDevIDSLConfigMarginThreshold_Type = Integer32
_XdslDevIDSLConfigMarginThreshold_Object = MibTableColumn
xdslDevIDSLConfigMarginThreshold = _XdslDevIDSLConfigMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1, 5),
    _XdslDevIDSLConfigMarginThreshold_Type()
)
xdslDevIDSLConfigMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLConfigMarginThreshold.setStatus("mandatory")
_XdslDevIDSLLinkUpDownTransitionThreshold_Type = Integer32
_XdslDevIDSLLinkUpDownTransitionThreshold_Object = MibTableColumn
xdslDevIDSLLinkUpDownTransitionThreshold = _XdslDevIDSLLinkUpDownTransitionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 9, 1, 1, 6),
    _XdslDevIDSLLinkUpDownTransitionThreshold_Type()
)
xdslDevIDSLLinkUpDownTransitionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLLinkUpDownTransitionThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects

xdslLinkUpDownTransitions = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 1)
)
xdslLinkUpDownTransitions.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslLinkUpDownTransitions.setStatus(
        ""
    )

xdslPortSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 2)
)
xdslPortSpeedLow.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslPortSpeedLow.setStatus(
        ""
    )

xdslMarginLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 3)
)
xdslMarginLow.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslMarginLow.setStatus(
        ""
    )

xdslErrorRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 4)
)
xdslErrorRateHigh.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslErrorRateHigh.setStatus(
        ""
    )

xdslPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 5)
)
xdslPortFailure.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslPortFailure.setStatus(
        ""
    )

xdslTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 6)
)
xdslTestStart.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslTestStart.setStatus(
        ""
    )

xdslRtuTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 7)
)
xdslRtuTypeMismatch.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslRtuTypeMismatch.setStatus(
        ""
    )

xdslRtuSelfTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 16)
)
xdslRtuSelfTestFail.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslRtuSelfTestFail.setStatus(
        ""
    )

xdslRtuLastGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 17)
)
xdslRtuLastGasp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslRtuLastGasp.setStatus(
        ""
    )

xdslSNDeviceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 18)
)
xdslSNDeviceFail.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslSNDeviceFail.setStatus(
        ""
    )

xdslSNSelfTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 19)
)
xdslSNSelfTestFail.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslSNSelfTestFail.setStatus(
        ""
    )

xdslSNFatalReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 20)
)
xdslSNFatalReset.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslSNFatalReset.setStatus(
        ""
    )

xdslLinkDownAnalysisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 21)
)
xdslLinkDownAnalysisTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HOTWIRE-XDSL-INTERFACE-MIB", "xdslLinkDownReason"))
)
if mibBuilder.loadTexts:
    xdslLinkDownAnalysisTrap.setStatus(
        ""
    )

xdslRemoteInjectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 22)
)
xdslRemoteInjectionFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HOT-DOMAIN-MIB", "pdnPortConfigVNID"),
        ("HOTWIRE-XDSL-INTERFACE-MIB", "xdslRemoteInjectionType"))
)
if mibBuilder.loadTexts:
    xdslRemoteInjectionFailureTrap.setStatus(
        ""
    )

xdslRemoteInjectionIncompatibleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 23)
)
xdslRemoteInjectionIncompatibleTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HOT-DOMAIN-MIB", "pdnPortConfigVNID"),
        ("HOTWIRE-XDSL-INTERFACE-MIB", "xdslRemoteInjectionType"))
)
if mibBuilder.loadTexts:
    xdslRemoteInjectionIncompatibleTrap.setStatus(
        ""
    )

xdslLossOfNetworkTimingSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 24)
)
xdslLossOfNetworkTimingSignalTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslLossOfNetworkTimingSignalTrap.setStatus(
        ""
    )

xdslPortSpeedNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 102)
)
xdslPortSpeedNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslPortSpeedNormal.setStatus(
        ""
    )

xdslMarginNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 103)
)
xdslMarginNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslMarginNormal.setStatus(
        ""
    )

xdslErrorRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 104)
)
xdslErrorRateNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslErrorRateNormal.setStatus(
        ""
    )

xdslPortOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 105)
)
xdslPortOperational.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslPortOperational.setStatus(
        ""
    )

xdslTestOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 106)
)
xdslTestOver.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslTestOver.setStatus(
        ""
    )

xdslRtuTypeMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8, 1, 0, 107)
)
xdslRtuTypeMismatchClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslRtuTypeMismatchClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOTWIRE-XDSL-INTERFACE-MIB",
    **{"DisplayString": DisplayString,
       "xdslDevice": xdslDevice,
       "xdslLinkUpDownTransitions": xdslLinkUpDownTransitions,
       "xdslPortSpeedLow": xdslPortSpeedLow,
       "xdslMarginLow": xdslMarginLow,
       "xdslErrorRateHigh": xdslErrorRateHigh,
       "xdslPortFailure": xdslPortFailure,
       "xdslTestStart": xdslTestStart,
       "xdslRtuTypeMismatch": xdslRtuTypeMismatch,
       "xdslRtuSelfTestFail": xdslRtuSelfTestFail,
       "xdslRtuLastGasp": xdslRtuLastGasp,
       "xdslSNDeviceFail": xdslSNDeviceFail,
       "xdslSNSelfTestFail": xdslSNSelfTestFail,
       "xdslSNFatalReset": xdslSNFatalReset,
       "xdslLinkDownAnalysisTrap": xdslLinkDownAnalysisTrap,
       "xdslRemoteInjectionFailureTrap": xdslRemoteInjectionFailureTrap,
       "xdslRemoteInjectionIncompatibleTrap": xdslRemoteInjectionIncompatibleTrap,
       "xdslLossOfNetworkTimingSignalTrap": xdslLossOfNetworkTimingSignalTrap,
       "xdslPortSpeedNormal": xdslPortSpeedNormal,
       "xdslMarginNormal": xdslMarginNormal,
       "xdslErrorRateNormal": xdslErrorRateNormal,
       "xdslPortOperational": xdslPortOperational,
       "xdslTestOver": xdslTestOver,
       "xdslRtuTypeMismatchClear": xdslRtuTypeMismatchClear,
       "xdslDevIfStats": xdslDevIfStats,
       "xdslDevIfIntervalStatsTable": xdslDevIfIntervalStatsTable,
       "xdslDevIfIntervalStatsEntry": xdslDevIfIntervalStatsEntry,
       "xdslDevIfStatsIfIndex": xdslDevIfStatsIfIndex,
       "xdslDevIfStatsInterval": xdslDevIfStatsInterval,
       "xdslDevIfStatsValid15MinuteIntervalCount": xdslDevIfStatsValid15MinuteIntervalCount,
       "xdslDevIfStatsElapsedTimeLinkUp": xdslDevIfStatsElapsedTimeLinkUp,
       "xdslDevIfStatsLinkDownCount": xdslDevIfStatsLinkDownCount,
       "xdslDevIfStatsUpStreamSpeed": xdslDevIfStatsUpStreamSpeed,
       "xdslDevIfStatsCentralReceiverGain": xdslDevIfStatsCentralReceiverGain,
       "xdslDevIfStatsCentralRecMargin": xdslDevIfStatsCentralRecMargin,
       "xdslDevIfStatsCentralRecAttenuationEstimate": xdslDevIfStatsCentralRecAttenuationEstimate,
       "xdslDevIfStatsCentralRecTransmitPower": xdslDevIfStatsCentralRecTransmitPower,
       "xdslDevIfStatsCentralRecErrorRate": xdslDevIfStatsCentralRecErrorRate,
       "xdslDevIfStatsCentralRecErroredSeconds": xdslDevIfStatsCentralRecErroredSeconds,
       "xdslDevIfStatsCentralRecSeverelyErroredSeconds": xdslDevIfStatsCentralRecSeverelyErroredSeconds,
       "xdslDevIfStatsRemoteReceiverGain": xdslDevIfStatsRemoteReceiverGain,
       "xdslDevIfStatsRemoteRecMargin": xdslDevIfStatsRemoteRecMargin,
       "xdslDevIfStatsRemoteRecAttenuationEstimate": xdslDevIfStatsRemoteRecAttenuationEstimate,
       "xdslDevIfStatsRemoteRecTransmitPower": xdslDevIfStatsRemoteRecTransmitPower,
       "xdslDevIfStatsRemoteRecErrorRate": xdslDevIfStatsRemoteRecErrorRate,
       "xdslDevIfStatsRemoteRecErroredSeconds": xdslDevIfStatsRemoteRecErroredSeconds,
       "xdslDevIfStatsRemoteRecSeverelyErroredSeconds": xdslDevIfStatsRemoteRecSeverelyErroredSeconds,
       "xdslDevIfStatsRemoteOctetsCorrected": xdslDevIfStatsRemoteOctetsCorrected,
       "xdslDevIfStatsRemoteOctetsNotCorrected": xdslDevIfStatsRemoteOctetsNotCorrected,
       "xdslDevIfStatsRemoteReceivedKiloOctets": xdslDevIfStatsRemoteReceivedKiloOctets,
       "xdslDevIfStatsRemoteReceivedPkts": xdslDevIfStatsRemoteReceivedPkts,
       "xdslDevIfStatsRemoteRecErrPkts": xdslDevIfStatsRemoteRecErrPkts,
       "xdslDevIfStatsRemoteDroppedPkts": xdslDevIfStatsRemoteDroppedPkts,
       "xdslDevIfStatsRemoteTransmittedKiloOctets": xdslDevIfStatsRemoteTransmittedKiloOctets,
       "xdslDevIfStatsRemoteTransmittedPkts": xdslDevIfStatsRemoteTransmittedPkts,
       "xdslDevIfStatsCentralRecErroredMinutes": xdslDevIfStatsCentralRecErroredMinutes,
       "xdslDevIfStatsCentralRecSeverelyErroredMinutes": xdslDevIfStatsCentralRecSeverelyErroredMinutes,
       "xdslDevIfStatsRemoteRecErroredMinutes": xdslDevIfStatsRemoteRecErroredMinutes,
       "xdslDevIfStatsRemoteRecSeverelyErroredMinutes": xdslDevIfStatsRemoteRecSeverelyErroredMinutes,
       "xdslDevIfStatsCentralReceivedKiloOctets": xdslDevIfStatsCentralReceivedKiloOctets,
       "xdslDevIfStatsCentralTransmittedKiloOctets": xdslDevIfStatsCentralTransmittedKiloOctets,
       "xdslDevIfStatsCentralTransmittedPkts": xdslDevIfStatsCentralTransmittedPkts,
       "xdslDevIfStatsCentralReceivedPkts": xdslDevIfStatsCentralReceivedPkts,
       "xdslDevIfStatsCentralErrPkts": xdslDevIfStatsCentralErrPkts,
       "xdslDevIfConfig": xdslDevIfConfig,
       "xdslDevIfConfigTable": xdslDevIfConfigTable,
       "xdslDevIfConfigEntry": xdslDevIfConfigEntry,
       "xdslDevIfConfigIfIndex": xdslDevIfConfigIfIndex,
       "xdslDevIfConfigPortSpeedBehaviour": xdslDevIfConfigPortSpeedBehaviour,
       "xdslDevIfConfigUpFixedPortSpeed": xdslDevIfConfigUpFixedPortSpeed,
       "xdslDevIfConfigDownFixedPortSpeed": xdslDevIfConfigDownFixedPortSpeed,
       "xdslDevIfConfigUpAdaptiveUpperBoundPortSpeed": xdslDevIfConfigUpAdaptiveUpperBoundPortSpeed,
       "xdslDevIfConfigUpAdaptiveLowerBoundPortSpeed": xdslDevIfConfigUpAdaptiveLowerBoundPortSpeed,
       "xdslDevIfConfigDownAdaptiveUpperBoundPortSpeed": xdslDevIfConfigDownAdaptiveUpperBoundPortSpeed,
       "xdslDevIfConfigDownAdaptiveLowerBoundPortSpeed": xdslDevIfConfigDownAdaptiveLowerBoundPortSpeed,
       "xdslDevIfConfigReedSolomonDownForwardErrorCorrection": xdslDevIfConfigReedSolomonDownForwardErrorCorrection,
       "xdslDevIfConfigMarginThreshold": xdslDevIfConfigMarginThreshold,
       "xdslDevIfConfigEstimatedHrErrRateThreshold": xdslDevIfConfigEstimatedHrErrRateThreshold,
       "xdslDevIfConfigEstimatedDayErrRateThreshold": xdslDevIfConfigEstimatedDayErrRateThreshold,
       "xdslDevIfConfigPortID": xdslDevIfConfigPortID,
       "xdslDevIfLinkUpDownTransitionThreshold": xdslDevIfLinkUpDownTransitionThreshold,
       "xdslDevIfConfigStartUpMargin": xdslDevIfConfigStartUpMargin,
       "xdslDevIfConfigTxPowerAttenuation": xdslDevIfConfigTxPowerAttenuation,
       "xdslDevIfConfigSnTxPowerAttenuation": xdslDevIfConfigSnTxPowerAttenuation,
       "xdslRemoteSys": xdslRemoteSys,
       "xdslRemoteSysTable": xdslRemoteSysTable,
       "xdslRemoteSysEntry": xdslRemoteSysEntry,
       "xdslRemoteSysIndex": xdslRemoteSysIndex,
       "xdslRemoteSysDescr": xdslRemoteSysDescr,
       "xdslRemoteSysObjectID": xdslRemoteSysObjectID,
       "xdslRemoteSysUpTime": xdslRemoteSysUpTime,
       "xdslRemoteSysContact": xdslRemoteSysContact,
       "xdslRemoteSysName": xdslRemoteSysName,
       "xdslRemoteSysLocation": xdslRemoteSysLocation,
       "xdslRemoteSysServices": xdslRemoteSysServices,
       "xdslRemoteSysCircuitId": xdslRemoteSysCircuitId,
       "xdslRemoteDTEStatus": xdslRemoteDTEStatus,
       "xdslRemoteDTEStatusTable": xdslRemoteDTEStatusTable,
       "xdslRemoteDTEStatusEntry": xdslRemoteDTEStatusEntry,
       "xdslRemoteDTEStatusIndex": xdslRemoteDTEStatusIndex,
       "xdslRemoteDTEState": xdslRemoteDTEState,
       "xdslRemoteDTEType": xdslRemoteDTEType,
       "xdslRemoteDTEClockSource": xdslRemoteDTEClockSource,
       "xdslRemoteDTEStrobe": xdslRemoteDTEStrobe,
       "xdslRemoteDTELoopbackState": xdslRemoteDTELoopbackState,
       "xdslDevMvlIfConfig": xdslDevMvlIfConfig,
       "xdslDevMvlIfConfigTable": xdslDevMvlIfConfigTable,
       "xdslDevMvlIfConfigEntry": xdslDevMvlIfConfigEntry,
       "xdslDevMvlIfConfigIfIndex": xdslDevMvlIfConfigIfIndex,
       "xdslDevMvlIfConfigUpperBoundPortSpeed": xdslDevMvlIfConfigUpperBoundPortSpeed,
       "xdslDevMvlIfConfigMarginThreshold": xdslDevMvlIfConfigMarginThreshold,
       "xdslDevMvlIfConfigPortID": xdslDevMvlIfConfigPortID,
       "xdslDevMvlIfLinkUpDownTransitionThreshold": xdslDevMvlIfLinkUpDownTransitionThreshold,
       "xdslDevMvlIfConfigOnHookTxPowerAttenuation": xdslDevMvlIfConfigOnHookTxPowerAttenuation,
       "xdslDevMvlIfConfigOffHookTxPowerAttenuation": xdslDevMvlIfConfigOffHookTxPowerAttenuation,
       "xdslDevNAPCustomerAccount": xdslDevNAPCustomerAccount,
       "xdslDevNAPCustomerAccountTable": xdslDevNAPCustomerAccountTable,
       "xdslDevNAPCustomerAccountEntry": xdslDevNAPCustomerAccountEntry,
       "xdslDevNAPCustomerAccountIfIndex": xdslDevNAPCustomerAccountIfIndex,
       "xdslDevNAPCustomerAccountInterval": xdslDevNAPCustomerAccountInterval,
       "xdslDevNAPCustomerAccountRecKiloOctets": xdslDevNAPCustomerAccountRecKiloOctets,
       "xdslDevNAPCustomerAccountTrxKiloOctets": xdslDevNAPCustomerAccountTrxKiloOctets,
       "xdslLinkUpDownInformation": xdslLinkUpDownInformation,
       "xdslLinkDownReason": xdslLinkDownReason,
       "xdslRemoteInjection": xdslRemoteInjection,
       "xdslRemoteInjectionType": xdslRemoteInjectionType,
       "xdslDevIDSLConfig": xdslDevIDSLConfig,
       "xdslDevIDSLConfigTable": xdslDevIDSLConfigTable,
       "xdslDevIDSLConfigEntry": xdslDevIDSLConfigEntry,
       "xdslDevIDSLConfigPortSpeedBehaviour": xdslDevIDSLConfigPortSpeedBehaviour,
       "xdslDevIDSLConfigPortSpeed": xdslDevIDSLConfigPortSpeed,
       "xdslDevIDSLConfigPortID": xdslDevIDSLConfigPortID,
       "xdslDevIDSLTimingPortTransceiverMode": xdslDevIDSLTimingPortTransceiverMode,
       "xdslDevIDSLConfigMarginThreshold": xdslDevIDSLConfigMarginThreshold,
       "xdslDevIDSLLinkUpDownTransitionThreshold": xdslDevIDSLLinkUpDownTransitionThreshold}
)
