# SNMP MIB module (NNCFRINTSTATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCFRINTSTATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:23 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(NncExtIntvlStateType,) = mibBuilder.importSymbols(
    "NNC-INTERVAL-STATISTICS-TC-MIB",
    "NncExtIntvlStateType")

(NncExtCounter64,
 nncExtensions) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "NncExtCounter64",
    "nncExtensions")

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

nncFrIntStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncFrIntStatisticsObjects_ObjectIdentity = ObjectIdentity
nncFrIntStatisticsObjects = _NncFrIntStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1)
)
_NncFrStrStatCurrentTable_Object = MibTable
nncFrStrStatCurrentTable = _NncFrStrStatCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1)
)
if mibBuilder.loadTexts:
    nncFrStrStatCurrentTable.setStatus("current")
_NncFrStrStatCurrentEntry_Object = MibTableRow
nncFrStrStatCurrentEntry = _NncFrStrStatCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1)
)
nncFrStrStatCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncFrStrStatCurrentEntry.setStatus("current")
_NncFrStrStatCurrentState_Type = NncExtIntvlStateType
_NncFrStrStatCurrentState_Object = MibTableColumn
nncFrStrStatCurrentState = _NncFrStrStatCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 1),
    _NncFrStrStatCurrentState_Type()
)
nncFrStrStatCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentState.setStatus("current")


class _NncFrStrStatCurrentAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncFrStrStatCurrentAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_NncFrStrStatCurrentAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncFrStrStatCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncFrStrStatCurrentAbsoluteIntervalNumber = _NncFrStrStatCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 2),
    _NncFrStrStatCurrentAbsoluteIntervalNumber_Type()
)
nncFrStrStatCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentAbsoluteIntervalNumber.setStatus("current")
_NncFrStrStatCurrentInOctets_Type = NncExtCounter64
_NncFrStrStatCurrentInOctets_Object = MibTableColumn
nncFrStrStatCurrentInOctets = _NncFrStrStatCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 3),
    _NncFrStrStatCurrentInOctets_Type()
)
nncFrStrStatCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInOctets.setStatus("current")
_NncFrStrStatCurrentOutOctets_Type = NncExtCounter64
_NncFrStrStatCurrentOutOctets_Object = MibTableColumn
nncFrStrStatCurrentOutOctets = _NncFrStrStatCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 4),
    _NncFrStrStatCurrentOutOctets_Type()
)
nncFrStrStatCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutOctets.setStatus("current")
_NncFrStrStatCurrentInUCastPackets_Type = NncExtCounter64
_NncFrStrStatCurrentInUCastPackets_Object = MibTableColumn
nncFrStrStatCurrentInUCastPackets = _NncFrStrStatCurrentInUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 5),
    _NncFrStrStatCurrentInUCastPackets_Type()
)
nncFrStrStatCurrentInUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInUCastPackets.setStatus("current")
_NncFrStrStatCurrentOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatCurrentOutUCastPackets_Object = MibTableColumn
nncFrStrStatCurrentOutUCastPackets = _NncFrStrStatCurrentOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 6),
    _NncFrStrStatCurrentOutUCastPackets_Type()
)
nncFrStrStatCurrentOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutUCastPackets.setStatus("current")
_NncFrStrStatCurrentInDiscards_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscards_Object = MibTableColumn
nncFrStrStatCurrentInDiscards = _NncFrStrStatCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 7),
    _NncFrStrStatCurrentInDiscards_Type()
)
nncFrStrStatCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscards.setStatus("current")
_NncFrStrStatCurrentOutDiscards_Type = NncExtCounter64
_NncFrStrStatCurrentOutDiscards_Object = MibTableColumn
nncFrStrStatCurrentOutDiscards = _NncFrStrStatCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 8),
    _NncFrStrStatCurrentOutDiscards_Type()
)
nncFrStrStatCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutDiscards.setStatus("current")
_NncFrStrStatCurrentInErrors_Type = NncExtCounter64
_NncFrStrStatCurrentInErrors_Object = MibTableColumn
nncFrStrStatCurrentInErrors = _NncFrStrStatCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 9),
    _NncFrStrStatCurrentInErrors_Type()
)
nncFrStrStatCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInErrors.setStatus("current")
_NncFrStrStatCurrentOutErrors_Type = NncExtCounter64
_NncFrStrStatCurrentOutErrors_Object = MibTableColumn
nncFrStrStatCurrentOutErrors = _NncFrStrStatCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 10),
    _NncFrStrStatCurrentOutErrors_Type()
)
nncFrStrStatCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutErrors.setStatus("current")
_NncFrStrStatCurrentSigUserProtErrors_Type = NncExtCounter64
_NncFrStrStatCurrentSigUserProtErrors_Object = MibTableColumn
nncFrStrStatCurrentSigUserProtErrors = _NncFrStrStatCurrentSigUserProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 11),
    _NncFrStrStatCurrentSigUserProtErrors_Type()
)
nncFrStrStatCurrentSigUserProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentSigUserProtErrors.setStatus("current")
_NncFrStrStatCurrentSigNetProtErrors_Type = NncExtCounter64
_NncFrStrStatCurrentSigNetProtErrors_Object = MibTableColumn
nncFrStrStatCurrentSigNetProtErrors = _NncFrStrStatCurrentSigNetProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 12),
    _NncFrStrStatCurrentSigNetProtErrors_Type()
)
nncFrStrStatCurrentSigNetProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentSigNetProtErrors.setStatus("current")
_NncFrStrStatCurrentSigUserLinkRelErrors_Type = NncExtCounter64
_NncFrStrStatCurrentSigUserLinkRelErrors_Object = MibTableColumn
nncFrStrStatCurrentSigUserLinkRelErrors = _NncFrStrStatCurrentSigUserLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 13),
    _NncFrStrStatCurrentSigUserLinkRelErrors_Type()
)
nncFrStrStatCurrentSigUserLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentSigUserLinkRelErrors.setStatus("current")
_NncFrStrStatCurrentSigNetLinkRelErrors_Type = NncExtCounter64
_NncFrStrStatCurrentSigNetLinkRelErrors_Object = MibTableColumn
nncFrStrStatCurrentSigNetLinkRelErrors = _NncFrStrStatCurrentSigNetLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 14),
    _NncFrStrStatCurrentSigNetLinkRelErrors_Type()
)
nncFrStrStatCurrentSigNetLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentSigNetLinkRelErrors.setStatus("current")
_NncFrStrStatCurrentSigUserChanInactive_Type = NncExtCounter64
_NncFrStrStatCurrentSigUserChanInactive_Object = MibTableColumn
nncFrStrStatCurrentSigUserChanInactive = _NncFrStrStatCurrentSigUserChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 15),
    _NncFrStrStatCurrentSigUserChanInactive_Type()
)
nncFrStrStatCurrentSigUserChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentSigUserChanInactive.setStatus("current")
_NncFrStrStatCurrentSigNetChanInactive_Type = NncExtCounter64
_NncFrStrStatCurrentSigNetChanInactive_Object = MibTableColumn
nncFrStrStatCurrentSigNetChanInactive = _NncFrStrStatCurrentSigNetChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 16),
    _NncFrStrStatCurrentSigNetChanInactive_Type()
)
nncFrStrStatCurrentSigNetChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentSigNetChanInactive.setStatus("current")
_NncFrStrStatCurrentStSCAlarms_Type = Counter32
_NncFrStrStatCurrentStSCAlarms_Object = MibTableColumn
nncFrStrStatCurrentStSCAlarms = _NncFrStrStatCurrentStSCAlarms_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 17),
    _NncFrStrStatCurrentStSCAlarms_Type()
)
nncFrStrStatCurrentStSCAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStSCAlarms.setStatus("current")
_NncFrStrStatCurrentStTimeSC_Type = Gauge32
_NncFrStrStatCurrentStTimeSC_Object = MibTableColumn
nncFrStrStatCurrentStTimeSC = _NncFrStrStatCurrentStTimeSC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 18),
    _NncFrStrStatCurrentStTimeSC_Type()
)
nncFrStrStatCurrentStTimeSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStTimeSC.setStatus("current")
_NncFrStrStatCurrentStMaxDurationRED_Type = Counter32
_NncFrStrStatCurrentStMaxDurationRED_Object = MibTableColumn
nncFrStrStatCurrentStMaxDurationRED = _NncFrStrStatCurrentStMaxDurationRED_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 19),
    _NncFrStrStatCurrentStMaxDurationRED_Type()
)
nncFrStrStatCurrentStMaxDurationRED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStMaxDurationRED.setStatus("current")
_NncFrStrStatCurrentStMCAlarms_Type = Counter32
_NncFrStrStatCurrentStMCAlarms_Object = MibTableColumn
nncFrStrStatCurrentStMCAlarms = _NncFrStrStatCurrentStMCAlarms_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 20),
    _NncFrStrStatCurrentStMCAlarms_Type()
)
nncFrStrStatCurrentStMCAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStMCAlarms.setStatus("current")
_NncFrStrStatCurrentStTimeMC_Type = Gauge32
_NncFrStrStatCurrentStTimeMC_Object = MibTableColumn
nncFrStrStatCurrentStTimeMC = _NncFrStrStatCurrentStTimeMC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 21),
    _NncFrStrStatCurrentStTimeMC_Type()
)
nncFrStrStatCurrentStTimeMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStTimeMC.setStatus("current")


class _NncFrStrStatCurrentOutLinkUtilization_Type(Gauge32):
    """Custom type nncFrStrStatCurrentOutLinkUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NncFrStrStatCurrentOutLinkUtilization_Type.__name__ = "Gauge32"
_NncFrStrStatCurrentOutLinkUtilization_Object = MibTableColumn
nncFrStrStatCurrentOutLinkUtilization = _NncFrStrStatCurrentOutLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 22),
    _NncFrStrStatCurrentOutLinkUtilization_Type()
)
nncFrStrStatCurrentOutLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutLinkUtilization.setStatus("current")


class _NncFrStrStatCurrentInLinkUtilization_Type(Gauge32):
    """Custom type nncFrStrStatCurrentInLinkUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NncFrStrStatCurrentInLinkUtilization_Type.__name__ = "Gauge32"
_NncFrStrStatCurrentInLinkUtilization_Object = MibTableColumn
nncFrStrStatCurrentInLinkUtilization = _NncFrStrStatCurrentInLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 23),
    _NncFrStrStatCurrentInLinkUtilization_Type()
)
nncFrStrStatCurrentInLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInLinkUtilization.setStatus("current")
_NncFrStrStatCurrentInInvdLength_Type = NncExtCounter64
_NncFrStrStatCurrentInInvdLength_Object = MibTableColumn
nncFrStrStatCurrentInInvdLength = _NncFrStrStatCurrentInInvdLength_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 24),
    _NncFrStrStatCurrentInInvdLength_Type()
)
nncFrStrStatCurrentInInvdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInInvdLength.setStatus("current")


class _NncFrStrStatCurrentStLastErroredDLCI_Type(Integer32):
    """Custom type nncFrStrStatCurrentStLastErroredDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_NncFrStrStatCurrentStLastErroredDLCI_Type.__name__ = "Integer32"
_NncFrStrStatCurrentStLastErroredDLCI_Object = MibTableColumn
nncFrStrStatCurrentStLastErroredDLCI = _NncFrStrStatCurrentStLastErroredDLCI_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 25),
    _NncFrStrStatCurrentStLastErroredDLCI_Type()
)
nncFrStrStatCurrentStLastErroredDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLastErroredDLCI.setStatus("current")
_NncFrStrStatCurrentInDiscdOctetsCOS_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdOctetsCOS_Object = MibTableColumn
nncFrStrStatCurrentInDiscdOctetsCOS = _NncFrStrStatCurrentInDiscdOctetsCOS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 26),
    _NncFrStrStatCurrentInDiscdOctetsCOS_Type()
)
nncFrStrStatCurrentInDiscdOctetsCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdOctetsCOS.setStatus("current")
_NncFrStrStatCurrentInDiscdCOSDESet_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdCOSDESet_Object = MibTableColumn
nncFrStrStatCurrentInDiscdCOSDESet = _NncFrStrStatCurrentInDiscdCOSDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 27),
    _NncFrStrStatCurrentInDiscdCOSDESet_Type()
)
nncFrStrStatCurrentInDiscdCOSDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdCOSDESet.setStatus("current")
_NncFrStrStatCurrentInDiscdCOSDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdCOSDEClr_Object = MibTableColumn
nncFrStrStatCurrentInDiscdCOSDEClr = _NncFrStrStatCurrentInDiscdCOSDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 28),
    _NncFrStrStatCurrentInDiscdCOSDEClr_Type()
)
nncFrStrStatCurrentInDiscdCOSDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdCOSDEClr.setStatus("current")
_NncFrStrStatCurrentInDiscdBadEncaps_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdBadEncaps_Object = MibTableColumn
nncFrStrStatCurrentInDiscdBadEncaps = _NncFrStrStatCurrentInDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 29),
    _NncFrStrStatCurrentInDiscdBadEncaps_Type()
)
nncFrStrStatCurrentInDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdBadEncaps.setStatus("current")
_NncFrStrStatCurrentOutDiscdBadEncaps_Type = NncExtCounter64
_NncFrStrStatCurrentOutDiscdBadEncaps_Object = MibTableColumn
nncFrStrStatCurrentOutDiscdBadEncaps = _NncFrStrStatCurrentOutDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 30),
    _NncFrStrStatCurrentOutDiscdBadEncaps_Type()
)
nncFrStrStatCurrentOutDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutDiscdBadEncaps.setStatus("current")
_NncFrStrStatCurrentInDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdUnsupEncaps_Object = MibTableColumn
nncFrStrStatCurrentInDiscdUnsupEncaps = _NncFrStrStatCurrentInDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 31),
    _NncFrStrStatCurrentInDiscdUnsupEncaps_Type()
)
nncFrStrStatCurrentInDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdUnsupEncaps.setStatus("current")
_NncFrStrStatCurrentOutDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrStrStatCurrentOutDiscdUnsupEncaps_Object = MibTableColumn
nncFrStrStatCurrentOutDiscdUnsupEncaps = _NncFrStrStatCurrentOutDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 32),
    _NncFrStrStatCurrentOutDiscdUnsupEncaps_Type()
)
nncFrStrStatCurrentOutDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutDiscdUnsupEncaps.setStatus("current")
_NncFrStrStatCurrentOutDiscdDESet_Type = NncExtCounter64
_NncFrStrStatCurrentOutDiscdDESet_Object = MibTableColumn
nncFrStrStatCurrentOutDiscdDESet = _NncFrStrStatCurrentOutDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 33),
    _NncFrStrStatCurrentOutDiscdDESet_Type()
)
nncFrStrStatCurrentOutDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutDiscdDESet.setStatus("current")
_NncFrStrStatCurrentOutDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentOutDiscdDEClr_Object = MibTableColumn
nncFrStrStatCurrentOutDiscdDEClr = _NncFrStrStatCurrentOutDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 34),
    _NncFrStrStatCurrentOutDiscdDEClr_Type()
)
nncFrStrStatCurrentOutDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutDiscdDEClr.setStatus("current")
_NncFrStrStatCurrentInDiscdDESet_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdDESet_Object = MibTableColumn
nncFrStrStatCurrentInDiscdDESet = _NncFrStrStatCurrentInDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 35),
    _NncFrStrStatCurrentInDiscdDESet_Type()
)
nncFrStrStatCurrentInDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdDESet.setStatus("current")
_NncFrStrStatCurrentInDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentInDiscdDEClr_Object = MibTableColumn
nncFrStrStatCurrentInDiscdDEClr = _NncFrStrStatCurrentInDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 36),
    _NncFrStrStatCurrentInDiscdDEClr_Type()
)
nncFrStrStatCurrentInDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInDiscdDEClr.setStatus("current")
_NncFrStrStatCurrentStLMSigInvldField_Type = NncExtCounter64
_NncFrStrStatCurrentStLMSigInvldField_Object = MibTableColumn
nncFrStrStatCurrentStLMSigInvldField = _NncFrStrStatCurrentStLMSigInvldField_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 37),
    _NncFrStrStatCurrentStLMSigInvldField_Type()
)
nncFrStrStatCurrentStLMSigInvldField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMSigInvldField.setStatus("current")
_NncFrStrStatCurrentStLMSigUnsupMsgType_Type = NncExtCounter64
_NncFrStrStatCurrentStLMSigUnsupMsgType_Object = MibTableColumn
nncFrStrStatCurrentStLMSigUnsupMsgType = _NncFrStrStatCurrentStLMSigUnsupMsgType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 38),
    _NncFrStrStatCurrentStLMSigUnsupMsgType_Type()
)
nncFrStrStatCurrentStLMSigUnsupMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMSigUnsupMsgType.setStatus("current")
_NncFrStrStatCurrentStLMSigInvldEID_Type = NncExtCounter64
_NncFrStrStatCurrentStLMSigInvldEID_Object = MibTableColumn
nncFrStrStatCurrentStLMSigInvldEID = _NncFrStrStatCurrentStLMSigInvldEID_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 39),
    _NncFrStrStatCurrentStLMSigInvldEID_Type()
)
nncFrStrStatCurrentStLMSigInvldEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMSigInvldEID.setStatus("current")
_NncFrStrStatCurrentStLMSigInvldIELen_Type = NncExtCounter64
_NncFrStrStatCurrentStLMSigInvldIELen_Object = MibTableColumn
nncFrStrStatCurrentStLMSigInvldIELen = _NncFrStrStatCurrentStLMSigInvldIELen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 40),
    _NncFrStrStatCurrentStLMSigInvldIELen_Type()
)
nncFrStrStatCurrentStLMSigInvldIELen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMSigInvldIELen.setStatus("current")
_NncFrStrStatCurrentStLMSigInvldRepType_Type = NncExtCounter64
_NncFrStrStatCurrentStLMSigInvldRepType_Object = MibTableColumn
nncFrStrStatCurrentStLMSigInvldRepType = _NncFrStrStatCurrentStLMSigInvldRepType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 41),
    _NncFrStrStatCurrentStLMSigInvldRepType_Type()
)
nncFrStrStatCurrentStLMSigInvldRepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMSigInvldRepType.setStatus("current")
_NncFrStrStatCurrentStLMSigFrmWithNoIEs_Type = NncExtCounter64
_NncFrStrStatCurrentStLMSigFrmWithNoIEs_Object = MibTableColumn
nncFrStrStatCurrentStLMSigFrmWithNoIEs = _NncFrStrStatCurrentStLMSigFrmWithNoIEs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 42),
    _NncFrStrStatCurrentStLMSigFrmWithNoIEs_Type()
)
nncFrStrStatCurrentStLMSigFrmWithNoIEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMSigFrmWithNoIEs.setStatus("current")
_NncFrStrStatCurrentStUserSequenceErrs_Type = NncExtCounter64
_NncFrStrStatCurrentStUserSequenceErrs_Object = MibTableColumn
nncFrStrStatCurrentStUserSequenceErrs = _NncFrStrStatCurrentStUserSequenceErrs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 43),
    _NncFrStrStatCurrentStUserSequenceErrs_Type()
)
nncFrStrStatCurrentStUserSequenceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStUserSequenceErrs.setStatus("current")
_NncFrStrStatCurrentStNetSequenceErrs_Type = NncExtCounter64
_NncFrStrStatCurrentStNetSequenceErrs_Object = MibTableColumn
nncFrStrStatCurrentStNetSequenceErrs = _NncFrStrStatCurrentStNetSequenceErrs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 44),
    _NncFrStrStatCurrentStNetSequenceErrs_Type()
)
nncFrStrStatCurrentStNetSequenceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStNetSequenceErrs.setStatus("current")
_NncFrStrStatCurrentStLMUTimeoutsnT1_Type = NncExtCounter64
_NncFrStrStatCurrentStLMUTimeoutsnT1_Object = MibTableColumn
nncFrStrStatCurrentStLMUTimeoutsnT1 = _NncFrStrStatCurrentStLMUTimeoutsnT1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 45),
    _NncFrStrStatCurrentStLMUTimeoutsnT1_Type()
)
nncFrStrStatCurrentStLMUTimeoutsnT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMUTimeoutsnT1.setStatus("current")
_NncFrStrStatCurrentStLMUStatusMsgsRcvd_Type = NncExtCounter64
_NncFrStrStatCurrentStLMUStatusMsgsRcvd_Object = MibTableColumn
nncFrStrStatCurrentStLMUStatusMsgsRcvd = _NncFrStrStatCurrentStLMUStatusMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 46),
    _NncFrStrStatCurrentStLMUStatusMsgsRcvd_Type()
)
nncFrStrStatCurrentStLMUStatusMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMUStatusMsgsRcvd.setStatus("current")
_NncFrStrStatCurrentStLMUStatusENQMsgsSent_Type = NncExtCounter64
_NncFrStrStatCurrentStLMUStatusENQMsgsSent_Object = MibTableColumn
nncFrStrStatCurrentStLMUStatusENQMsgsSent = _NncFrStrStatCurrentStLMUStatusENQMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 47),
    _NncFrStrStatCurrentStLMUStatusENQMsgsSent_Type()
)
nncFrStrStatCurrentStLMUStatusENQMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMUStatusENQMsgsSent.setStatus("current")
_NncFrStrStatCurrentStLMUAsyncStatusRcvd_Type = NncExtCounter64
_NncFrStrStatCurrentStLMUAsyncStatusRcvd_Object = MibTableColumn
nncFrStrStatCurrentStLMUAsyncStatusRcvd = _NncFrStrStatCurrentStLMUAsyncStatusRcvd_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 48),
    _NncFrStrStatCurrentStLMUAsyncStatusRcvd_Type()
)
nncFrStrStatCurrentStLMUAsyncStatusRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMUAsyncStatusRcvd.setStatus("current")
_NncFrStrStatCurrentStLMNTimeoutsnT2_Type = NncExtCounter64
_NncFrStrStatCurrentStLMNTimeoutsnT2_Object = MibTableColumn
nncFrStrStatCurrentStLMNTimeoutsnT2 = _NncFrStrStatCurrentStLMNTimeoutsnT2_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 49),
    _NncFrStrStatCurrentStLMNTimeoutsnT2_Type()
)
nncFrStrStatCurrentStLMNTimeoutsnT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMNTimeoutsnT2.setStatus("current")
_NncFrStrStatCurrentStLMNStatusMsgsSent_Type = NncExtCounter64
_NncFrStrStatCurrentStLMNStatusMsgsSent_Object = MibTableColumn
nncFrStrStatCurrentStLMNStatusMsgsSent = _NncFrStrStatCurrentStLMNStatusMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 50),
    _NncFrStrStatCurrentStLMNStatusMsgsSent_Type()
)
nncFrStrStatCurrentStLMNStatusMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMNStatusMsgsSent.setStatus("current")
_NncFrStrStatCurrentStLMNStatusENQMsgsRcvd_Type = NncExtCounter64
_NncFrStrStatCurrentStLMNStatusENQMsgsRcvd_Object = MibTableColumn
nncFrStrStatCurrentStLMNStatusENQMsgsRcvd = _NncFrStrStatCurrentStLMNStatusENQMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 51),
    _NncFrStrStatCurrentStLMNStatusENQMsgsRcvd_Type()
)
nncFrStrStatCurrentStLMNStatusENQMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMNStatusENQMsgsRcvd.setStatus("current")
_NncFrStrStatCurrentStLMNAsyncStatusSent_Type = NncExtCounter64
_NncFrStrStatCurrentStLMNAsyncStatusSent_Object = MibTableColumn
nncFrStrStatCurrentStLMNAsyncStatusSent = _NncFrStrStatCurrentStLMNAsyncStatusSent_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 52),
    _NncFrStrStatCurrentStLMNAsyncStatusSent_Type()
)
nncFrStrStatCurrentStLMNAsyncStatusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStLMNAsyncStatusSent.setStatus("current")
_NncFrStrStatCurrentInCRCErrors_Type = NncExtCounter64
_NncFrStrStatCurrentInCRCErrors_Object = MibTableColumn
nncFrStrStatCurrentInCRCErrors = _NncFrStrStatCurrentInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 53),
    _NncFrStrStatCurrentInCRCErrors_Type()
)
nncFrStrStatCurrentInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInCRCErrors.setStatus("current")
_NncFrStrStatCurrentInNonIntegral_Type = NncExtCounter64
_NncFrStrStatCurrentInNonIntegral_Object = MibTableColumn
nncFrStrStatCurrentInNonIntegral = _NncFrStrStatCurrentInNonIntegral_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 54),
    _NncFrStrStatCurrentInNonIntegral_Type()
)
nncFrStrStatCurrentInNonIntegral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInNonIntegral.setStatus("current")
_NncFrStrStatCurrentInReservedDLCI_Type = NncExtCounter64
_NncFrStrStatCurrentInReservedDLCI_Object = MibTableColumn
nncFrStrStatCurrentInReservedDLCI = _NncFrStrStatCurrentInReservedDLCI_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 55),
    _NncFrStrStatCurrentInReservedDLCI_Type()
)
nncFrStrStatCurrentInReservedDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInReservedDLCI.setStatus("current")
_NncFrStrStatCurrentInInvldEA_Type = NncExtCounter64
_NncFrStrStatCurrentInInvldEA_Object = MibTableColumn
nncFrStrStatCurrentInInvldEA = _NncFrStrStatCurrentInInvldEA_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 56),
    _NncFrStrStatCurrentInInvldEA_Type()
)
nncFrStrStatCurrentInInvldEA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInInvldEA.setStatus("current")
_NncFrStrStatCurrentStFrmTooSmall_Type = NncExtCounter64
_NncFrStrStatCurrentStFrmTooSmall_Object = MibTableColumn
nncFrStrStatCurrentStFrmTooSmall = _NncFrStrStatCurrentStFrmTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 57),
    _NncFrStrStatCurrentStFrmTooSmall_Type()
)
nncFrStrStatCurrentStFrmTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStFrmTooSmall.setStatus("current")
_NncFrStrStatCurrentInAborts_Type = NncExtCounter64
_NncFrStrStatCurrentInAborts_Object = MibTableColumn
nncFrStrStatCurrentInAborts = _NncFrStrStatCurrentInAborts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 58),
    _NncFrStrStatCurrentInAborts_Type()
)
nncFrStrStatCurrentInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInAborts.setStatus("current")
_NncFrStrStatCurrentInSumOfDisagremnts_Type = NncExtCounter64
_NncFrStrStatCurrentInSumOfDisagremnts_Object = MibTableColumn
nncFrStrStatCurrentInSumOfDisagremnts = _NncFrStrStatCurrentInSumOfDisagremnts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 59),
    _NncFrStrStatCurrentInSumOfDisagremnts_Type()
)
nncFrStrStatCurrentInSumOfDisagremnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInSumOfDisagremnts.setStatus("current")
_NncFrStrStatCurrentInOverRuns_Type = NncExtCounter64
_NncFrStrStatCurrentInOverRuns_Object = MibTableColumn
nncFrStrStatCurrentInOverRuns = _NncFrStrStatCurrentInOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 60),
    _NncFrStrStatCurrentInOverRuns_Type()
)
nncFrStrStatCurrentInOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentInOverRuns.setStatus("current")
_NncFrStrStatCurrentOutUnderRuns_Type = NncExtCounter64
_NncFrStrStatCurrentOutUnderRuns_Object = MibTableColumn
nncFrStrStatCurrentOutUnderRuns = _NncFrStrStatCurrentOutUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 61),
    _NncFrStrStatCurrentOutUnderRuns_Type()
)
nncFrStrStatCurrentOutUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentOutUnderRuns.setStatus("current")
_NncFrStrStatCurrentStIntervalDuration_Type = Integer32
_NncFrStrStatCurrentStIntervalDuration_Object = MibTableColumn
nncFrStrStatCurrentStIntervalDuration = _NncFrStrStatCurrentStIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 62),
    _NncFrStrStatCurrentStIntervalDuration_Type()
)
nncFrStrStatCurrentStIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentStIntervalDuration.setStatus("current")


class _NncFrStrStatCurrentBestEffortPeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatCurrentBestEffortPeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatCurrentBestEffortPeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatCurrentBestEffortPeakDelay_Object = MibTableColumn
nncFrStrStatCurrentBestEffortPeakDelay = _NncFrStrStatCurrentBestEffortPeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 63),
    _NncFrStrStatCurrentBestEffortPeakDelay_Type()
)
nncFrStrStatCurrentBestEffortPeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentBestEffortPeakDelay.setStatus("current")


class _NncFrStrStatCurrentCommittedPeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatCurrentCommittedPeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatCurrentCommittedPeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatCurrentCommittedPeakDelay_Object = MibTableColumn
nncFrStrStatCurrentCommittedPeakDelay = _NncFrStrStatCurrentCommittedPeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 64),
    _NncFrStrStatCurrentCommittedPeakDelay_Type()
)
nncFrStrStatCurrentCommittedPeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentCommittedPeakDelay.setStatus("current")


class _NncFrStrStatCurrentLowDelayPeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatCurrentLowDelayPeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatCurrentLowDelayPeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatCurrentLowDelayPeakDelay_Object = MibTableColumn
nncFrStrStatCurrentLowDelayPeakDelay = _NncFrStrStatCurrentLowDelayPeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 65),
    _NncFrStrStatCurrentLowDelayPeakDelay_Type()
)
nncFrStrStatCurrentLowDelayPeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentLowDelayPeakDelay.setStatus("current")


class _NncFrStrStatCurrentRealTimePeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatCurrentRealTimePeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatCurrentRealTimePeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatCurrentRealTimePeakDelay_Object = MibTableColumn
nncFrStrStatCurrentRealTimePeakDelay = _NncFrStrStatCurrentRealTimePeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 66),
    _NncFrStrStatCurrentRealTimePeakDelay_Type()
)
nncFrStrStatCurrentRealTimePeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentRealTimePeakDelay.setStatus("current")
_NncFrStrStatCurrentBestEffortAccDelay_Type = NncExtCounter64
_NncFrStrStatCurrentBestEffortAccDelay_Object = MibTableColumn
nncFrStrStatCurrentBestEffortAccDelay = _NncFrStrStatCurrentBestEffortAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 67),
    _NncFrStrStatCurrentBestEffortAccDelay_Type()
)
nncFrStrStatCurrentBestEffortAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentBestEffortAccDelay.setStatus("current")
_NncFrStrStatCurrentCommittedAccDelay_Type = NncExtCounter64
_NncFrStrStatCurrentCommittedAccDelay_Object = MibTableColumn
nncFrStrStatCurrentCommittedAccDelay = _NncFrStrStatCurrentCommittedAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 68),
    _NncFrStrStatCurrentCommittedAccDelay_Type()
)
nncFrStrStatCurrentCommittedAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentCommittedAccDelay.setStatus("current")
_NncFrStrStatCurrentLowDelayAccDelay_Type = NncExtCounter64
_NncFrStrStatCurrentLowDelayAccDelay_Object = MibTableColumn
nncFrStrStatCurrentLowDelayAccDelay = _NncFrStrStatCurrentLowDelayAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 69),
    _NncFrStrStatCurrentLowDelayAccDelay_Type()
)
nncFrStrStatCurrentLowDelayAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentLowDelayAccDelay.setStatus("current")
_NncFrStrStatCurrentRealTimeAccDelay_Type = NncExtCounter64
_NncFrStrStatCurrentRealTimeAccDelay_Object = MibTableColumn
nncFrStrStatCurrentRealTimeAccDelay = _NncFrStrStatCurrentRealTimeAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 70),
    _NncFrStrStatCurrentRealTimeAccDelay_Type()
)
nncFrStrStatCurrentRealTimeAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentRealTimeAccDelay.setStatus("current")
_NncFrStrStatCurrentBestEffortOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatCurrentBestEffortOutUCastPackets_Object = MibTableColumn
nncFrStrStatCurrentBestEffortOutUCastPackets = _NncFrStrStatCurrentBestEffortOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 71),
    _NncFrStrStatCurrentBestEffortOutUCastPackets_Type()
)
nncFrStrStatCurrentBestEffortOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentBestEffortOutUCastPackets.setStatus("current")
_NncFrStrStatCurrentCommittedOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatCurrentCommittedOutUCastPackets_Object = MibTableColumn
nncFrStrStatCurrentCommittedOutUCastPackets = _NncFrStrStatCurrentCommittedOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 72),
    _NncFrStrStatCurrentCommittedOutUCastPackets_Type()
)
nncFrStrStatCurrentCommittedOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentCommittedOutUCastPackets.setStatus("current")
_NncFrStrStatCurrentLowDelayOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatCurrentLowDelayOutUCastPackets_Object = MibTableColumn
nncFrStrStatCurrentLowDelayOutUCastPackets = _NncFrStrStatCurrentLowDelayOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 73),
    _NncFrStrStatCurrentLowDelayOutUCastPackets_Type()
)
nncFrStrStatCurrentLowDelayOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentLowDelayOutUCastPackets.setStatus("current")
_NncFrStrStatCurrentRealTimeOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatCurrentRealTimeOutUCastPackets_Object = MibTableColumn
nncFrStrStatCurrentRealTimeOutUCastPackets = _NncFrStrStatCurrentRealTimeOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 74),
    _NncFrStrStatCurrentRealTimeOutUCastPackets_Type()
)
nncFrStrStatCurrentRealTimeOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentRealTimeOutUCastPackets.setStatus("current")
_NncFrStrStatCurrentBestEffortUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentBestEffortUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatCurrentBestEffortUCastPacketsDEClr = _NncFrStrStatCurrentBestEffortUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 75),
    _NncFrStrStatCurrentBestEffortUCastPacketsDEClr_Type()
)
nncFrStrStatCurrentBestEffortUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentBestEffortUCastPacketsDEClr.setStatus("current")
_NncFrStrStatCurrentCommittedUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentCommittedUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatCurrentCommittedUCastPacketsDEClr = _NncFrStrStatCurrentCommittedUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 76),
    _NncFrStrStatCurrentCommittedUCastPacketsDEClr_Type()
)
nncFrStrStatCurrentCommittedUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentCommittedUCastPacketsDEClr.setStatus("current")
_NncFrStrStatCurrentLowDelayUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentLowDelayUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatCurrentLowDelayUCastPacketsDEClr = _NncFrStrStatCurrentLowDelayUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 77),
    _NncFrStrStatCurrentLowDelayUCastPacketsDEClr_Type()
)
nncFrStrStatCurrentLowDelayUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentLowDelayUCastPacketsDEClr.setStatus("current")
_NncFrStrStatCurrentRealTimeUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentRealTimeUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatCurrentRealTimeUCastPacketsDEClr = _NncFrStrStatCurrentRealTimeUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 78),
    _NncFrStrStatCurrentRealTimeUCastPacketsDEClr_Type()
)
nncFrStrStatCurrentRealTimeUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentRealTimeUCastPacketsDEClr.setStatus("current")
_NncFrStrStatCurrentBestEffortDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentBestEffortDiscdDEClr_Object = MibTableColumn
nncFrStrStatCurrentBestEffortDiscdDEClr = _NncFrStrStatCurrentBestEffortDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 79),
    _NncFrStrStatCurrentBestEffortDiscdDEClr_Type()
)
nncFrStrStatCurrentBestEffortDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentBestEffortDiscdDEClr.setStatus("current")
_NncFrStrStatCurrentCommittedDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentCommittedDiscdDEClr_Object = MibTableColumn
nncFrStrStatCurrentCommittedDiscdDEClr = _NncFrStrStatCurrentCommittedDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 80),
    _NncFrStrStatCurrentCommittedDiscdDEClr_Type()
)
nncFrStrStatCurrentCommittedDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentCommittedDiscdDEClr.setStatus("current")
_NncFrStrStatCurrentLowDelayDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentLowDelayDiscdDEClr_Object = MibTableColumn
nncFrStrStatCurrentLowDelayDiscdDEClr = _NncFrStrStatCurrentLowDelayDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 81),
    _NncFrStrStatCurrentLowDelayDiscdDEClr_Type()
)
nncFrStrStatCurrentLowDelayDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentLowDelayDiscdDEClr.setStatus("current")
_NncFrStrStatCurrentRealTimeDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatCurrentRealTimeDiscdDEClr_Object = MibTableColumn
nncFrStrStatCurrentRealTimeDiscdDEClr = _NncFrStrStatCurrentRealTimeDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 1, 1, 82),
    _NncFrStrStatCurrentRealTimeDiscdDEClr_Type()
)
nncFrStrStatCurrentRealTimeDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatCurrentRealTimeDiscdDEClr.setStatus("current")
_NncFrStrStatIntervalTable_Object = MibTable
nncFrStrStatIntervalTable = _NncFrStrStatIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2)
)
if mibBuilder.loadTexts:
    nncFrStrStatIntervalTable.setStatus("current")
_NncFrStrStatIntervalEntry_Object = MibTableRow
nncFrStrStatIntervalEntry = _NncFrStrStatIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1)
)
nncFrStrStatIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncFrStrStatIntervalEntry.setStatus("current")


class _NncFrStrStatIntervalNumber_Type(Integer32):
    """Custom type nncFrStrStatIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncFrStrStatIntervalNumber_Type.__name__ = "Integer32"
_NncFrStrStatIntervalNumber_Object = MibTableColumn
nncFrStrStatIntervalNumber = _NncFrStrStatIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 1),
    _NncFrStrStatIntervalNumber_Type()
)
nncFrStrStatIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalNumber.setStatus("current")
_NncFrStrStatIntervalState_Type = NncExtIntvlStateType
_NncFrStrStatIntervalState_Object = MibTableColumn
nncFrStrStatIntervalState = _NncFrStrStatIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 2),
    _NncFrStrStatIntervalState_Type()
)
nncFrStrStatIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalState.setStatus("current")


class _NncFrStrStatIntervalAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncFrStrStatIntervalAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_NncFrStrStatIntervalAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncFrStrStatIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncFrStrStatIntervalAbsoluteIntervalNumber = _NncFrStrStatIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 3),
    _NncFrStrStatIntervalAbsoluteIntervalNumber_Type()
)
nncFrStrStatIntervalAbsoluteIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalAbsoluteIntervalNumber.setStatus("current")
_NncFrStrStatIntervalInOctets_Type = NncExtCounter64
_NncFrStrStatIntervalInOctets_Object = MibTableColumn
nncFrStrStatIntervalInOctets = _NncFrStrStatIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 4),
    _NncFrStrStatIntervalInOctets_Type()
)
nncFrStrStatIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInOctets.setStatus("current")
_NncFrStrStatIntervalOutOctets_Type = NncExtCounter64
_NncFrStrStatIntervalOutOctets_Object = MibTableColumn
nncFrStrStatIntervalOutOctets = _NncFrStrStatIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 5),
    _NncFrStrStatIntervalOutOctets_Type()
)
nncFrStrStatIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutOctets.setStatus("current")
_NncFrStrStatIntervalInUCastPackets_Type = NncExtCounter64
_NncFrStrStatIntervalInUCastPackets_Object = MibTableColumn
nncFrStrStatIntervalInUCastPackets = _NncFrStrStatIntervalInUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 6),
    _NncFrStrStatIntervalInUCastPackets_Type()
)
nncFrStrStatIntervalInUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInUCastPackets.setStatus("current")
_NncFrStrStatIntervalOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatIntervalOutUCastPackets_Object = MibTableColumn
nncFrStrStatIntervalOutUCastPackets = _NncFrStrStatIntervalOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 7),
    _NncFrStrStatIntervalOutUCastPackets_Type()
)
nncFrStrStatIntervalOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutUCastPackets.setStatus("current")
_NncFrStrStatIntervalInDiscards_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscards_Object = MibTableColumn
nncFrStrStatIntervalInDiscards = _NncFrStrStatIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 8),
    _NncFrStrStatIntervalInDiscards_Type()
)
nncFrStrStatIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscards.setStatus("current")
_NncFrStrStatIntervalOutDiscards_Type = NncExtCounter64
_NncFrStrStatIntervalOutDiscards_Object = MibTableColumn
nncFrStrStatIntervalOutDiscards = _NncFrStrStatIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 9),
    _NncFrStrStatIntervalOutDiscards_Type()
)
nncFrStrStatIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutDiscards.setStatus("current")
_NncFrStrStatIntervalInErrors_Type = NncExtCounter64
_NncFrStrStatIntervalInErrors_Object = MibTableColumn
nncFrStrStatIntervalInErrors = _NncFrStrStatIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 10),
    _NncFrStrStatIntervalInErrors_Type()
)
nncFrStrStatIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInErrors.setStatus("current")
_NncFrStrStatIntervalOutErrors_Type = NncExtCounter64
_NncFrStrStatIntervalOutErrors_Object = MibTableColumn
nncFrStrStatIntervalOutErrors = _NncFrStrStatIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 11),
    _NncFrStrStatIntervalOutErrors_Type()
)
nncFrStrStatIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutErrors.setStatus("current")
_NncFrStrStatIntervalSigUserProtErrors_Type = NncExtCounter64
_NncFrStrStatIntervalSigUserProtErrors_Object = MibTableColumn
nncFrStrStatIntervalSigUserProtErrors = _NncFrStrStatIntervalSigUserProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 12),
    _NncFrStrStatIntervalSigUserProtErrors_Type()
)
nncFrStrStatIntervalSigUserProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalSigUserProtErrors.setStatus("current")
_NncFrStrStatIntervalSigNetProtErrors_Type = NncExtCounter64
_NncFrStrStatIntervalSigNetProtErrors_Object = MibTableColumn
nncFrStrStatIntervalSigNetProtErrors = _NncFrStrStatIntervalSigNetProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 13),
    _NncFrStrStatIntervalSigNetProtErrors_Type()
)
nncFrStrStatIntervalSigNetProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalSigNetProtErrors.setStatus("current")
_NncFrStrStatIntervalSigUserLinkRelErrors_Type = NncExtCounter64
_NncFrStrStatIntervalSigUserLinkRelErrors_Object = MibTableColumn
nncFrStrStatIntervalSigUserLinkRelErrors = _NncFrStrStatIntervalSigUserLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 14),
    _NncFrStrStatIntervalSigUserLinkRelErrors_Type()
)
nncFrStrStatIntervalSigUserLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalSigUserLinkRelErrors.setStatus("current")
_NncFrStrStatIntervalSigNetLinkRelErrors_Type = NncExtCounter64
_NncFrStrStatIntervalSigNetLinkRelErrors_Object = MibTableColumn
nncFrStrStatIntervalSigNetLinkRelErrors = _NncFrStrStatIntervalSigNetLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 15),
    _NncFrStrStatIntervalSigNetLinkRelErrors_Type()
)
nncFrStrStatIntervalSigNetLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalSigNetLinkRelErrors.setStatus("current")
_NncFrStrStatIntervalSigUserChanInactive_Type = NncExtCounter64
_NncFrStrStatIntervalSigUserChanInactive_Object = MibTableColumn
nncFrStrStatIntervalSigUserChanInactive = _NncFrStrStatIntervalSigUserChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 16),
    _NncFrStrStatIntervalSigUserChanInactive_Type()
)
nncFrStrStatIntervalSigUserChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalSigUserChanInactive.setStatus("current")
_NncFrStrStatIntervalSigNetChanInactive_Type = NncExtCounter64
_NncFrStrStatIntervalSigNetChanInactive_Object = MibTableColumn
nncFrStrStatIntervalSigNetChanInactive = _NncFrStrStatIntervalSigNetChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 17),
    _NncFrStrStatIntervalSigNetChanInactive_Type()
)
nncFrStrStatIntervalSigNetChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalSigNetChanInactive.setStatus("current")
_NncFrStrStatIntervalStSCAlarms_Type = Counter32
_NncFrStrStatIntervalStSCAlarms_Object = MibTableColumn
nncFrStrStatIntervalStSCAlarms = _NncFrStrStatIntervalStSCAlarms_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 18),
    _NncFrStrStatIntervalStSCAlarms_Type()
)
nncFrStrStatIntervalStSCAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStSCAlarms.setStatus("current")
_NncFrStrStatIntervalStTimeSC_Type = Gauge32
_NncFrStrStatIntervalStTimeSC_Object = MibTableColumn
nncFrStrStatIntervalStTimeSC = _NncFrStrStatIntervalStTimeSC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 19),
    _NncFrStrStatIntervalStTimeSC_Type()
)
nncFrStrStatIntervalStTimeSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStTimeSC.setStatus("current")
_NncFrStrStatIntervalStMaxDurationRED_Type = Counter32
_NncFrStrStatIntervalStMaxDurationRED_Object = MibTableColumn
nncFrStrStatIntervalStMaxDurationRED = _NncFrStrStatIntervalStMaxDurationRED_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 20),
    _NncFrStrStatIntervalStMaxDurationRED_Type()
)
nncFrStrStatIntervalStMaxDurationRED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStMaxDurationRED.setStatus("current")
_NncFrStrStatIntervalStMCAlarms_Type = Counter32
_NncFrStrStatIntervalStMCAlarms_Object = MibTableColumn
nncFrStrStatIntervalStMCAlarms = _NncFrStrStatIntervalStMCAlarms_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 21),
    _NncFrStrStatIntervalStMCAlarms_Type()
)
nncFrStrStatIntervalStMCAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStMCAlarms.setStatus("current")
_NncFrStrStatIntervalStTimeMC_Type = Gauge32
_NncFrStrStatIntervalStTimeMC_Object = MibTableColumn
nncFrStrStatIntervalStTimeMC = _NncFrStrStatIntervalStTimeMC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 22),
    _NncFrStrStatIntervalStTimeMC_Type()
)
nncFrStrStatIntervalStTimeMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStTimeMC.setStatus("current")


class _NncFrStrStatIntervalOutLinkUtilization_Type(Gauge32):
    """Custom type nncFrStrStatIntervalOutLinkUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NncFrStrStatIntervalOutLinkUtilization_Type.__name__ = "Gauge32"
_NncFrStrStatIntervalOutLinkUtilization_Object = MibTableColumn
nncFrStrStatIntervalOutLinkUtilization = _NncFrStrStatIntervalOutLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 23),
    _NncFrStrStatIntervalOutLinkUtilization_Type()
)
nncFrStrStatIntervalOutLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutLinkUtilization.setStatus("current")


class _NncFrStrStatIntervalInLinkUtilization_Type(Gauge32):
    """Custom type nncFrStrStatIntervalInLinkUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NncFrStrStatIntervalInLinkUtilization_Type.__name__ = "Gauge32"
_NncFrStrStatIntervalInLinkUtilization_Object = MibTableColumn
nncFrStrStatIntervalInLinkUtilization = _NncFrStrStatIntervalInLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 24),
    _NncFrStrStatIntervalInLinkUtilization_Type()
)
nncFrStrStatIntervalInLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInLinkUtilization.setStatus("current")
_NncFrStrStatIntervalInInvdLength_Type = NncExtCounter64
_NncFrStrStatIntervalInInvdLength_Object = MibTableColumn
nncFrStrStatIntervalInInvdLength = _NncFrStrStatIntervalInInvdLength_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 25),
    _NncFrStrStatIntervalInInvdLength_Type()
)
nncFrStrStatIntervalInInvdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInInvdLength.setStatus("current")


class _NncFrStrStatIntervalStLastErroredDLCI_Type(Integer32):
    """Custom type nncFrStrStatIntervalStLastErroredDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_NncFrStrStatIntervalStLastErroredDLCI_Type.__name__ = "Integer32"
_NncFrStrStatIntervalStLastErroredDLCI_Object = MibTableColumn
nncFrStrStatIntervalStLastErroredDLCI = _NncFrStrStatIntervalStLastErroredDLCI_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 26),
    _NncFrStrStatIntervalStLastErroredDLCI_Type()
)
nncFrStrStatIntervalStLastErroredDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLastErroredDLCI.setStatus("current")
_NncFrStrStatIntervalInDiscdOctetsCOS_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdOctetsCOS_Object = MibTableColumn
nncFrStrStatIntervalInDiscdOctetsCOS = _NncFrStrStatIntervalInDiscdOctetsCOS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 27),
    _NncFrStrStatIntervalInDiscdOctetsCOS_Type()
)
nncFrStrStatIntervalInDiscdOctetsCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdOctetsCOS.setStatus("current")
_NncFrStrStatIntervalInDiscdCOSDESet_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdCOSDESet_Object = MibTableColumn
nncFrStrStatIntervalInDiscdCOSDESet = _NncFrStrStatIntervalInDiscdCOSDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 28),
    _NncFrStrStatIntervalInDiscdCOSDESet_Type()
)
nncFrStrStatIntervalInDiscdCOSDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdCOSDESet.setStatus("current")
_NncFrStrStatIntervalInDiscdCOSDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdCOSDEClr_Object = MibTableColumn
nncFrStrStatIntervalInDiscdCOSDEClr = _NncFrStrStatIntervalInDiscdCOSDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 29),
    _NncFrStrStatIntervalInDiscdCOSDEClr_Type()
)
nncFrStrStatIntervalInDiscdCOSDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdCOSDEClr.setStatus("current")
_NncFrStrStatIntervalInDiscdBadEncaps_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdBadEncaps_Object = MibTableColumn
nncFrStrStatIntervalInDiscdBadEncaps = _NncFrStrStatIntervalInDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 30),
    _NncFrStrStatIntervalInDiscdBadEncaps_Type()
)
nncFrStrStatIntervalInDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdBadEncaps.setStatus("current")
_NncFrStrStatIntervalOutDiscdBadEncaps_Type = NncExtCounter64
_NncFrStrStatIntervalOutDiscdBadEncaps_Object = MibTableColumn
nncFrStrStatIntervalOutDiscdBadEncaps = _NncFrStrStatIntervalOutDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 31),
    _NncFrStrStatIntervalOutDiscdBadEncaps_Type()
)
nncFrStrStatIntervalOutDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutDiscdBadEncaps.setStatus("current")
_NncFrStrStatIntervalInDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdUnsupEncaps_Object = MibTableColumn
nncFrStrStatIntervalInDiscdUnsupEncaps = _NncFrStrStatIntervalInDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 32),
    _NncFrStrStatIntervalInDiscdUnsupEncaps_Type()
)
nncFrStrStatIntervalInDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdUnsupEncaps.setStatus("current")
_NncFrStrStatIntervalOutDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrStrStatIntervalOutDiscdUnsupEncaps_Object = MibTableColumn
nncFrStrStatIntervalOutDiscdUnsupEncaps = _NncFrStrStatIntervalOutDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 33),
    _NncFrStrStatIntervalOutDiscdUnsupEncaps_Type()
)
nncFrStrStatIntervalOutDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutDiscdUnsupEncaps.setStatus("current")
_NncFrStrStatIntervalOutDiscdDESet_Type = NncExtCounter64
_NncFrStrStatIntervalOutDiscdDESet_Object = MibTableColumn
nncFrStrStatIntervalOutDiscdDESet = _NncFrStrStatIntervalOutDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 34),
    _NncFrStrStatIntervalOutDiscdDESet_Type()
)
nncFrStrStatIntervalOutDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutDiscdDESet.setStatus("current")
_NncFrStrStatIntervalOutDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalOutDiscdDEClr_Object = MibTableColumn
nncFrStrStatIntervalOutDiscdDEClr = _NncFrStrStatIntervalOutDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 35),
    _NncFrStrStatIntervalOutDiscdDEClr_Type()
)
nncFrStrStatIntervalOutDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutDiscdDEClr.setStatus("current")
_NncFrStrStatIntervalInDiscdDESet_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdDESet_Object = MibTableColumn
nncFrStrStatIntervalInDiscdDESet = _NncFrStrStatIntervalInDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 36),
    _NncFrStrStatIntervalInDiscdDESet_Type()
)
nncFrStrStatIntervalInDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdDESet.setStatus("current")
_NncFrStrStatIntervalInDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalInDiscdDEClr_Object = MibTableColumn
nncFrStrStatIntervalInDiscdDEClr = _NncFrStrStatIntervalInDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 37),
    _NncFrStrStatIntervalInDiscdDEClr_Type()
)
nncFrStrStatIntervalInDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInDiscdDEClr.setStatus("current")
_NncFrStrStatIntervalStLMSigInvldField_Type = NncExtCounter64
_NncFrStrStatIntervalStLMSigInvldField_Object = MibTableColumn
nncFrStrStatIntervalStLMSigInvldField = _NncFrStrStatIntervalStLMSigInvldField_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 38),
    _NncFrStrStatIntervalStLMSigInvldField_Type()
)
nncFrStrStatIntervalStLMSigInvldField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMSigInvldField.setStatus("current")
_NncFrStrStatIntervalStLMSigUnsupMsgType_Type = NncExtCounter64
_NncFrStrStatIntervalStLMSigUnsupMsgType_Object = MibTableColumn
nncFrStrStatIntervalStLMSigUnsupMsgType = _NncFrStrStatIntervalStLMSigUnsupMsgType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 39),
    _NncFrStrStatIntervalStLMSigUnsupMsgType_Type()
)
nncFrStrStatIntervalStLMSigUnsupMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMSigUnsupMsgType.setStatus("current")
_NncFrStrStatIntervalStLMSigInvldEID_Type = NncExtCounter64
_NncFrStrStatIntervalStLMSigInvldEID_Object = MibTableColumn
nncFrStrStatIntervalStLMSigInvldEID = _NncFrStrStatIntervalStLMSigInvldEID_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 40),
    _NncFrStrStatIntervalStLMSigInvldEID_Type()
)
nncFrStrStatIntervalStLMSigInvldEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMSigInvldEID.setStatus("current")
_NncFrStrStatIntervalStLMSigInvldIELen_Type = NncExtCounter64
_NncFrStrStatIntervalStLMSigInvldIELen_Object = MibTableColumn
nncFrStrStatIntervalStLMSigInvldIELen = _NncFrStrStatIntervalStLMSigInvldIELen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 41),
    _NncFrStrStatIntervalStLMSigInvldIELen_Type()
)
nncFrStrStatIntervalStLMSigInvldIELen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMSigInvldIELen.setStatus("current")
_NncFrStrStatIntervalStLMSigInvldRepType_Type = NncExtCounter64
_NncFrStrStatIntervalStLMSigInvldRepType_Object = MibTableColumn
nncFrStrStatIntervalStLMSigInvldRepType = _NncFrStrStatIntervalStLMSigInvldRepType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 42),
    _NncFrStrStatIntervalStLMSigInvldRepType_Type()
)
nncFrStrStatIntervalStLMSigInvldRepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMSigInvldRepType.setStatus("current")
_NncFrStrStatIntervalStLMSigFrmWithNoIEs_Type = NncExtCounter64
_NncFrStrStatIntervalStLMSigFrmWithNoIEs_Object = MibTableColumn
nncFrStrStatIntervalStLMSigFrmWithNoIEs = _NncFrStrStatIntervalStLMSigFrmWithNoIEs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 43),
    _NncFrStrStatIntervalStLMSigFrmWithNoIEs_Type()
)
nncFrStrStatIntervalStLMSigFrmWithNoIEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMSigFrmWithNoIEs.setStatus("current")
_NncFrStrStatIntervalStUserSequenceErrs_Type = NncExtCounter64
_NncFrStrStatIntervalStUserSequenceErrs_Object = MibTableColumn
nncFrStrStatIntervalStUserSequenceErrs = _NncFrStrStatIntervalStUserSequenceErrs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 44),
    _NncFrStrStatIntervalStUserSequenceErrs_Type()
)
nncFrStrStatIntervalStUserSequenceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStUserSequenceErrs.setStatus("current")
_NncFrStrStatIntervalStNetSequenceErrs_Type = NncExtCounter64
_NncFrStrStatIntervalStNetSequenceErrs_Object = MibTableColumn
nncFrStrStatIntervalStNetSequenceErrs = _NncFrStrStatIntervalStNetSequenceErrs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 45),
    _NncFrStrStatIntervalStNetSequenceErrs_Type()
)
nncFrStrStatIntervalStNetSequenceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStNetSequenceErrs.setStatus("current")
_NncFrStrStatIntervalStLMUTimeoutsnT1_Type = NncExtCounter64
_NncFrStrStatIntervalStLMUTimeoutsnT1_Object = MibTableColumn
nncFrStrStatIntervalStLMUTimeoutsnT1 = _NncFrStrStatIntervalStLMUTimeoutsnT1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 46),
    _NncFrStrStatIntervalStLMUTimeoutsnT1_Type()
)
nncFrStrStatIntervalStLMUTimeoutsnT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMUTimeoutsnT1.setStatus("current")
_NncFrStrStatIntervalStLMUStatusMsgsRcvd_Type = NncExtCounter64
_NncFrStrStatIntervalStLMUStatusMsgsRcvd_Object = MibTableColumn
nncFrStrStatIntervalStLMUStatusMsgsRcvd = _NncFrStrStatIntervalStLMUStatusMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 47),
    _NncFrStrStatIntervalStLMUStatusMsgsRcvd_Type()
)
nncFrStrStatIntervalStLMUStatusMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMUStatusMsgsRcvd.setStatus("current")
_NncFrStrStatIntervalStLMUStatusENQMsgsSent_Type = NncExtCounter64
_NncFrStrStatIntervalStLMUStatusENQMsgsSent_Object = MibTableColumn
nncFrStrStatIntervalStLMUStatusENQMsgsSent = _NncFrStrStatIntervalStLMUStatusENQMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 48),
    _NncFrStrStatIntervalStLMUStatusENQMsgsSent_Type()
)
nncFrStrStatIntervalStLMUStatusENQMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMUStatusENQMsgsSent.setStatus("current")
_NncFrStrStatIntervalStLMUAsyncStatusRcvd_Type = NncExtCounter64
_NncFrStrStatIntervalStLMUAsyncStatusRcvd_Object = MibTableColumn
nncFrStrStatIntervalStLMUAsyncStatusRcvd = _NncFrStrStatIntervalStLMUAsyncStatusRcvd_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 49),
    _NncFrStrStatIntervalStLMUAsyncStatusRcvd_Type()
)
nncFrStrStatIntervalStLMUAsyncStatusRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMUAsyncStatusRcvd.setStatus("current")
_NncFrStrStatIntervalStLMNTimeoutsnT2_Type = NncExtCounter64
_NncFrStrStatIntervalStLMNTimeoutsnT2_Object = MibTableColumn
nncFrStrStatIntervalStLMNTimeoutsnT2 = _NncFrStrStatIntervalStLMNTimeoutsnT2_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 50),
    _NncFrStrStatIntervalStLMNTimeoutsnT2_Type()
)
nncFrStrStatIntervalStLMNTimeoutsnT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMNTimeoutsnT2.setStatus("current")
_NncFrStrStatIntervalStLMNStatusMsgsSent_Type = NncExtCounter64
_NncFrStrStatIntervalStLMNStatusMsgsSent_Object = MibTableColumn
nncFrStrStatIntervalStLMNStatusMsgsSent = _NncFrStrStatIntervalStLMNStatusMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 51),
    _NncFrStrStatIntervalStLMNStatusMsgsSent_Type()
)
nncFrStrStatIntervalStLMNStatusMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMNStatusMsgsSent.setStatus("current")
_NncFrStrStatIntervalStLMNStatusENQMsgsRcvd_Type = NncExtCounter64
_NncFrStrStatIntervalStLMNStatusENQMsgsRcvd_Object = MibTableColumn
nncFrStrStatIntervalStLMNStatusENQMsgsRcvd = _NncFrStrStatIntervalStLMNStatusENQMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 52),
    _NncFrStrStatIntervalStLMNStatusENQMsgsRcvd_Type()
)
nncFrStrStatIntervalStLMNStatusENQMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMNStatusENQMsgsRcvd.setStatus("current")
_NncFrStrStatIntervalStLMNAsyncStatusSent_Type = NncExtCounter64
_NncFrStrStatIntervalStLMNAsyncStatusSent_Object = MibTableColumn
nncFrStrStatIntervalStLMNAsyncStatusSent = _NncFrStrStatIntervalStLMNAsyncStatusSent_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 53),
    _NncFrStrStatIntervalStLMNAsyncStatusSent_Type()
)
nncFrStrStatIntervalStLMNAsyncStatusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStLMNAsyncStatusSent.setStatus("current")
_NncFrStrStatIntervalInCRCErrors_Type = NncExtCounter64
_NncFrStrStatIntervalInCRCErrors_Object = MibTableColumn
nncFrStrStatIntervalInCRCErrors = _NncFrStrStatIntervalInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 54),
    _NncFrStrStatIntervalInCRCErrors_Type()
)
nncFrStrStatIntervalInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInCRCErrors.setStatus("current")
_NncFrStrStatIntervalInNonIntegral_Type = NncExtCounter64
_NncFrStrStatIntervalInNonIntegral_Object = MibTableColumn
nncFrStrStatIntervalInNonIntegral = _NncFrStrStatIntervalInNonIntegral_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 55),
    _NncFrStrStatIntervalInNonIntegral_Type()
)
nncFrStrStatIntervalInNonIntegral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInNonIntegral.setStatus("current")
_NncFrStrStatIntervalInReservedDLCI_Type = NncExtCounter64
_NncFrStrStatIntervalInReservedDLCI_Object = MibTableColumn
nncFrStrStatIntervalInReservedDLCI = _NncFrStrStatIntervalInReservedDLCI_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 56),
    _NncFrStrStatIntervalInReservedDLCI_Type()
)
nncFrStrStatIntervalInReservedDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInReservedDLCI.setStatus("current")
_NncFrStrStatIntervalInInvldEA_Type = NncExtCounter64
_NncFrStrStatIntervalInInvldEA_Object = MibTableColumn
nncFrStrStatIntervalInInvldEA = _NncFrStrStatIntervalInInvldEA_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 57),
    _NncFrStrStatIntervalInInvldEA_Type()
)
nncFrStrStatIntervalInInvldEA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInInvldEA.setStatus("current")
_NncFrStrStatIntervalStFrmTooSmall_Type = NncExtCounter64
_NncFrStrStatIntervalStFrmTooSmall_Object = MibTableColumn
nncFrStrStatIntervalStFrmTooSmall = _NncFrStrStatIntervalStFrmTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 58),
    _NncFrStrStatIntervalStFrmTooSmall_Type()
)
nncFrStrStatIntervalStFrmTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStFrmTooSmall.setStatus("current")
_NncFrStrStatIntervalInAborts_Type = NncExtCounter64
_NncFrStrStatIntervalInAborts_Object = MibTableColumn
nncFrStrStatIntervalInAborts = _NncFrStrStatIntervalInAborts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 59),
    _NncFrStrStatIntervalInAborts_Type()
)
nncFrStrStatIntervalInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInAborts.setStatus("current")
_NncFrStrStatIntervalInSumOfDisagremnts_Type = NncExtCounter64
_NncFrStrStatIntervalInSumOfDisagremnts_Object = MibTableColumn
nncFrStrStatIntervalInSumOfDisagremnts = _NncFrStrStatIntervalInSumOfDisagremnts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 60),
    _NncFrStrStatIntervalInSumOfDisagremnts_Type()
)
nncFrStrStatIntervalInSumOfDisagremnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInSumOfDisagremnts.setStatus("current")
_NncFrStrStatIntervalInOverRuns_Type = NncExtCounter64
_NncFrStrStatIntervalInOverRuns_Object = MibTableColumn
nncFrStrStatIntervalInOverRuns = _NncFrStrStatIntervalInOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 61),
    _NncFrStrStatIntervalInOverRuns_Type()
)
nncFrStrStatIntervalInOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalInOverRuns.setStatus("current")
_NncFrStrStatIntervalOutUnderRuns_Type = NncExtCounter64
_NncFrStrStatIntervalOutUnderRuns_Object = MibTableColumn
nncFrStrStatIntervalOutUnderRuns = _NncFrStrStatIntervalOutUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 62),
    _NncFrStrStatIntervalOutUnderRuns_Type()
)
nncFrStrStatIntervalOutUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalOutUnderRuns.setStatus("current")
_NncFrStrStatIntervalStIntervalDuration_Type = Integer32
_NncFrStrStatIntervalStIntervalDuration_Object = MibTableColumn
nncFrStrStatIntervalStIntervalDuration = _NncFrStrStatIntervalStIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 63),
    _NncFrStrStatIntervalStIntervalDuration_Type()
)
nncFrStrStatIntervalStIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalStIntervalDuration.setStatus("current")


class _NncFrStrStatIntervalBestEffortPeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatIntervalBestEffortPeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatIntervalBestEffortPeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatIntervalBestEffortPeakDelay_Object = MibTableColumn
nncFrStrStatIntervalBestEffortPeakDelay = _NncFrStrStatIntervalBestEffortPeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 64),
    _NncFrStrStatIntervalBestEffortPeakDelay_Type()
)
nncFrStrStatIntervalBestEffortPeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalBestEffortPeakDelay.setStatus("current")


class _NncFrStrStatIntervalCommittedPeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatIntervalCommittedPeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatIntervalCommittedPeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatIntervalCommittedPeakDelay_Object = MibTableColumn
nncFrStrStatIntervalCommittedPeakDelay = _NncFrStrStatIntervalCommittedPeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 65),
    _NncFrStrStatIntervalCommittedPeakDelay_Type()
)
nncFrStrStatIntervalCommittedPeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalCommittedPeakDelay.setStatus("current")


class _NncFrStrStatIntervalLowDelayPeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatIntervalLowDelayPeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatIntervalLowDelayPeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatIntervalLowDelayPeakDelay_Object = MibTableColumn
nncFrStrStatIntervalLowDelayPeakDelay = _NncFrStrStatIntervalLowDelayPeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 66),
    _NncFrStrStatIntervalLowDelayPeakDelay_Type()
)
nncFrStrStatIntervalLowDelayPeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalLowDelayPeakDelay.setStatus("current")


class _NncFrStrStatIntervalRealTimePeakDelay_Type(Gauge32):
    """Custom type nncFrStrStatIntervalRealTimePeakDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NncFrStrStatIntervalRealTimePeakDelay_Type.__name__ = "Gauge32"
_NncFrStrStatIntervalRealTimePeakDelay_Object = MibTableColumn
nncFrStrStatIntervalRealTimePeakDelay = _NncFrStrStatIntervalRealTimePeakDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 67),
    _NncFrStrStatIntervalRealTimePeakDelay_Type()
)
nncFrStrStatIntervalRealTimePeakDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalRealTimePeakDelay.setStatus("current")
_NncFrStrStatIntervalBestEffortAccDelay_Type = NncExtCounter64
_NncFrStrStatIntervalBestEffortAccDelay_Object = MibTableColumn
nncFrStrStatIntervalBestEffortAccDelay = _NncFrStrStatIntervalBestEffortAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 68),
    _NncFrStrStatIntervalBestEffortAccDelay_Type()
)
nncFrStrStatIntervalBestEffortAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalBestEffortAccDelay.setStatus("current")
_NncFrStrStatIntervalCommittedAccDelay_Type = NncExtCounter64
_NncFrStrStatIntervalCommittedAccDelay_Object = MibTableColumn
nncFrStrStatIntervalCommittedAccDelay = _NncFrStrStatIntervalCommittedAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 69),
    _NncFrStrStatIntervalCommittedAccDelay_Type()
)
nncFrStrStatIntervalCommittedAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalCommittedAccDelay.setStatus("current")
_NncFrStrStatIntervalLowDelayAccDelay_Type = NncExtCounter64
_NncFrStrStatIntervalLowDelayAccDelay_Object = MibTableColumn
nncFrStrStatIntervalLowDelayAccDelay = _NncFrStrStatIntervalLowDelayAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 70),
    _NncFrStrStatIntervalLowDelayAccDelay_Type()
)
nncFrStrStatIntervalLowDelayAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalLowDelayAccDelay.setStatus("current")
_NncFrStrStatIntervalRealTimeAccDelay_Type = NncExtCounter64
_NncFrStrStatIntervalRealTimeAccDelay_Object = MibTableColumn
nncFrStrStatIntervalRealTimeAccDelay = _NncFrStrStatIntervalRealTimeAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 71),
    _NncFrStrStatIntervalRealTimeAccDelay_Type()
)
nncFrStrStatIntervalRealTimeAccDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalRealTimeAccDelay.setStatus("current")
_NncFrStrStatIntervalBestEffortOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatIntervalBestEffortOutUCastPackets_Object = MibTableColumn
nncFrStrStatIntervalBestEffortOutUCastPackets = _NncFrStrStatIntervalBestEffortOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 72),
    _NncFrStrStatIntervalBestEffortOutUCastPackets_Type()
)
nncFrStrStatIntervalBestEffortOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalBestEffortOutUCastPackets.setStatus("current")
_NncFrStrStatIntervalCommittedOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatIntervalCommittedOutUCastPackets_Object = MibTableColumn
nncFrStrStatIntervalCommittedOutUCastPackets = _NncFrStrStatIntervalCommittedOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 73),
    _NncFrStrStatIntervalCommittedOutUCastPackets_Type()
)
nncFrStrStatIntervalCommittedOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalCommittedOutUCastPackets.setStatus("current")
_NncFrStrStatIntervalLowDelayOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatIntervalLowDelayOutUCastPackets_Object = MibTableColumn
nncFrStrStatIntervalLowDelayOutUCastPackets = _NncFrStrStatIntervalLowDelayOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 74),
    _NncFrStrStatIntervalLowDelayOutUCastPackets_Type()
)
nncFrStrStatIntervalLowDelayOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalLowDelayOutUCastPackets.setStatus("current")
_NncFrStrStatIntervalRealTimeOutUCastPackets_Type = NncExtCounter64
_NncFrStrStatIntervalRealTimeOutUCastPackets_Object = MibTableColumn
nncFrStrStatIntervalRealTimeOutUCastPackets = _NncFrStrStatIntervalRealTimeOutUCastPackets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 75),
    _NncFrStrStatIntervalRealTimeOutUCastPackets_Type()
)
nncFrStrStatIntervalRealTimeOutUCastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalRealTimeOutUCastPackets.setStatus("current")
_NncFrStrStatIntervalBestEffortUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalBestEffortUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatIntervalBestEffortUCastPacketsDEClr = _NncFrStrStatIntervalBestEffortUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 76),
    _NncFrStrStatIntervalBestEffortUCastPacketsDEClr_Type()
)
nncFrStrStatIntervalBestEffortUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalBestEffortUCastPacketsDEClr.setStatus("current")
_NncFrStrStatIntervalCommittedUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalCommittedUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatIntervalCommittedUCastPacketsDEClr = _NncFrStrStatIntervalCommittedUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 77),
    _NncFrStrStatIntervalCommittedUCastPacketsDEClr_Type()
)
nncFrStrStatIntervalCommittedUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalCommittedUCastPacketsDEClr.setStatus("current")
_NncFrStrStatIntervalLowDelayUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalLowDelayUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatIntervalLowDelayUCastPacketsDEClr = _NncFrStrStatIntervalLowDelayUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 78),
    _NncFrStrStatIntervalLowDelayUCastPacketsDEClr_Type()
)
nncFrStrStatIntervalLowDelayUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalLowDelayUCastPacketsDEClr.setStatus("current")
_NncFrStrStatIntervalRealTimeUCastPacketsDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalRealTimeUCastPacketsDEClr_Object = MibTableColumn
nncFrStrStatIntervalRealTimeUCastPacketsDEClr = _NncFrStrStatIntervalRealTimeUCastPacketsDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 79),
    _NncFrStrStatIntervalRealTimeUCastPacketsDEClr_Type()
)
nncFrStrStatIntervalRealTimeUCastPacketsDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalRealTimeUCastPacketsDEClr.setStatus("current")
_NncFrStrStatIntervalBestEffortDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalBestEffortDiscdDEClr_Object = MibTableColumn
nncFrStrStatIntervalBestEffortDiscdDEClr = _NncFrStrStatIntervalBestEffortDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 80),
    _NncFrStrStatIntervalBestEffortDiscdDEClr_Type()
)
nncFrStrStatIntervalBestEffortDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalBestEffortDiscdDEClr.setStatus("current")
_NncFrStrStatIntervalCommittedDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalCommittedDiscdDEClr_Object = MibTableColumn
nncFrStrStatIntervalCommittedDiscdDEClr = _NncFrStrStatIntervalCommittedDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 81),
    _NncFrStrStatIntervalCommittedDiscdDEClr_Type()
)
nncFrStrStatIntervalCommittedDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalCommittedDiscdDEClr.setStatus("current")
_NncFrStrStatIntervalLowDelayDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalLowDelayDiscdDEClr_Object = MibTableColumn
nncFrStrStatIntervalLowDelayDiscdDEClr = _NncFrStrStatIntervalLowDelayDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 82),
    _NncFrStrStatIntervalLowDelayDiscdDEClr_Type()
)
nncFrStrStatIntervalLowDelayDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalLowDelayDiscdDEClr.setStatus("current")
_NncFrStrStatIntervalRealTimeDiscdDEClr_Type = NncExtCounter64
_NncFrStrStatIntervalRealTimeDiscdDEClr_Object = MibTableColumn
nncFrStrStatIntervalRealTimeDiscdDEClr = _NncFrStrStatIntervalRealTimeDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 2, 1, 83),
    _NncFrStrStatIntervalRealTimeDiscdDEClr_Type()
)
nncFrStrStatIntervalRealTimeDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrStatIntervalRealTimeDiscdDEClr.setStatus("current")
_NncFrPVCEndptStatCurrentTable_Object = MibTable
nncFrPVCEndptStatCurrentTable = _NncFrPVCEndptStatCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3)
)
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentTable.setStatus("current")
_NncFrPVCEndptStatCurrentEntry_Object = MibTableRow
nncFrPVCEndptStatCurrentEntry = _NncFrPVCEndptStatCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1)
)
nncFrPVCEndptStatCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentDLCINumber"),
)
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentEntry.setStatus("current")


class _NncFrPVCEndptStatCurrentDLCINumber_Type(Integer32):
    """Custom type nncFrPVCEndptStatCurrentDLCINumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NncFrPVCEndptStatCurrentDLCINumber_Type.__name__ = "Integer32"
_NncFrPVCEndptStatCurrentDLCINumber_Object = MibTableColumn
nncFrPVCEndptStatCurrentDLCINumber = _NncFrPVCEndptStatCurrentDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 1),
    _NncFrPVCEndptStatCurrentDLCINumber_Type()
)
nncFrPVCEndptStatCurrentDLCINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentDLCINumber.setStatus("current")
_NncFrPVCEndptStatCurrentState_Type = NncExtIntvlStateType
_NncFrPVCEndptStatCurrentState_Object = MibTableColumn
nncFrPVCEndptStatCurrentState = _NncFrPVCEndptStatCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 2),
    _NncFrPVCEndptStatCurrentState_Type()
)
nncFrPVCEndptStatCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentState.setStatus("current")


class _NncFrPVCEndptStatCurrentAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncFrPVCEndptStatCurrentAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_NncFrPVCEndptStatCurrentAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncFrPVCEndptStatCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncFrPVCEndptStatCurrentAbsoluteIntervalNumber = _NncFrPVCEndptStatCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 3),
    _NncFrPVCEndptStatCurrentAbsoluteIntervalNumber_Type()
)
nncFrPVCEndptStatCurrentAbsoluteIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentAbsoluteIntervalNumber.setStatus("current")
_NncFrPVCEndptStatCurrentInFrames_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInFrames_Object = MibTableColumn
nncFrPVCEndptStatCurrentInFrames = _NncFrPVCEndptStatCurrentInFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 4),
    _NncFrPVCEndptStatCurrentInFrames_Type()
)
nncFrPVCEndptStatCurrentInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInFrames.setStatus("current")
_NncFrPVCEndptStatCurrentOutFrames_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutFrames_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutFrames = _NncFrPVCEndptStatCurrentOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 5),
    _NncFrPVCEndptStatCurrentOutFrames_Type()
)
nncFrPVCEndptStatCurrentOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutFrames.setStatus("current")
_NncFrPVCEndptStatCurrentInOctets_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInOctets_Object = MibTableColumn
nncFrPVCEndptStatCurrentInOctets = _NncFrPVCEndptStatCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 6),
    _NncFrPVCEndptStatCurrentInOctets_Type()
)
nncFrPVCEndptStatCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInOctets.setStatus("current")
_NncFrPVCEndptStatCurrentOutOctets_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutOctets_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutOctets = _NncFrPVCEndptStatCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 7),
    _NncFrPVCEndptStatCurrentOutOctets_Type()
)
nncFrPVCEndptStatCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutOctets.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscards_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscards_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscards = _NncFrPVCEndptStatCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 8),
    _NncFrPVCEndptStatCurrentInDiscards_Type()
)
nncFrPVCEndptStatCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscards.setStatus("current")
_NncFrPVCEndptStatCurrentOutExcessFrames_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutExcessFrames_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutExcessFrames = _NncFrPVCEndptStatCurrentOutExcessFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 9),
    _NncFrPVCEndptStatCurrentOutExcessFrames_Type()
)
nncFrPVCEndptStatCurrentOutExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutExcessFrames.setStatus("current")
_NncFrPVCEndptStatCurrentInDEFrames_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDEFrames_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDEFrames = _NncFrPVCEndptStatCurrentInDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 10),
    _NncFrPVCEndptStatCurrentInDEFrames_Type()
)
nncFrPVCEndptStatCurrentInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDEFrames.setStatus("current")
_NncFrPVCEndptStatCurrentInCosTagDeFrames_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInCosTagDeFrames_Object = MibTableColumn
nncFrPVCEndptStatCurrentInCosTagDeFrames = _NncFrPVCEndptStatCurrentInCosTagDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 11),
    _NncFrPVCEndptStatCurrentInCosTagDeFrames_Type()
)
nncFrPVCEndptStatCurrentInCosTagDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInCosTagDeFrames.setStatus("current")
_NncFrPVCEndptStatCurrentInOctetsDESet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInOctetsDESet_Object = MibTableColumn
nncFrPVCEndptStatCurrentInOctetsDESet = _NncFrPVCEndptStatCurrentInOctetsDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 12),
    _NncFrPVCEndptStatCurrentInOctetsDESet_Type()
)
nncFrPVCEndptStatCurrentInOctetsDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInOctetsDESet.setStatus("current")
_NncFrPVCEndptStatCurrentInFramesBECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInFramesBECNSet_Object = MibTableColumn
nncFrPVCEndptStatCurrentInFramesBECNSet = _NncFrPVCEndptStatCurrentInFramesBECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 13),
    _NncFrPVCEndptStatCurrentInFramesBECNSet_Type()
)
nncFrPVCEndptStatCurrentInFramesBECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInFramesBECNSet.setStatus("current")
_NncFrPVCEndptStatCurrentInFramesFECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInFramesFECNSet_Object = MibTableColumn
nncFrPVCEndptStatCurrentInFramesFECNSet = _NncFrPVCEndptStatCurrentInFramesFECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 14),
    _NncFrPVCEndptStatCurrentInFramesFECNSet_Type()
)
nncFrPVCEndptStatCurrentInFramesFECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInFramesFECNSet.setStatus("current")
_NncFrPVCEndptStatCurrentInInvdLength_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInInvdLength_Object = MibTableColumn
nncFrPVCEndptStatCurrentInInvdLength = _NncFrPVCEndptStatCurrentInInvdLength_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 15),
    _NncFrPVCEndptStatCurrentInInvdLength_Type()
)
nncFrPVCEndptStatCurrentInInvdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInInvdLength.setStatus("current")
_NncFrPVCEndptStatCurrentOutOctetsDESet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutOctetsDESet_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutOctetsDESet = _NncFrPVCEndptStatCurrentOutOctetsDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 16),
    _NncFrPVCEndptStatCurrentOutOctetsDESet_Type()
)
nncFrPVCEndptStatCurrentOutOctetsDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutOctetsDESet.setStatus("current")
_NncFrPVCEndptStatCurrentOutFramesBECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutFramesBECNSet_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutFramesBECNSet = _NncFrPVCEndptStatCurrentOutFramesBECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 17),
    _NncFrPVCEndptStatCurrentOutFramesBECNSet_Type()
)
nncFrPVCEndptStatCurrentOutFramesBECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutFramesBECNSet.setStatus("current")
_NncFrPVCEndptStatCurrentOutFramesFECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutFramesFECNSet_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutFramesFECNSet = _NncFrPVCEndptStatCurrentOutFramesFECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 18),
    _NncFrPVCEndptStatCurrentOutFramesFECNSet_Type()
)
nncFrPVCEndptStatCurrentOutFramesFECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutFramesFECNSet.setStatus("current")
_NncFrPVCEndptStatCurrentOutFramesInRed_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutFramesInRed_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutFramesInRed = _NncFrPVCEndptStatCurrentOutFramesInRed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 19),
    _NncFrPVCEndptStatCurrentOutFramesInRed_Type()
)
nncFrPVCEndptStatCurrentOutFramesInRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutFramesInRed.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdOctetsCOS_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdOctetsCOS_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdOctetsCOS = _NncFrPVCEndptStatCurrentInDiscdOctetsCOS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 20),
    _NncFrPVCEndptStatCurrentInDiscdOctetsCOS_Type()
)
nncFrPVCEndptStatCurrentInDiscdOctetsCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdOctetsCOS.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdDESet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdDESet_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdDESet = _NncFrPVCEndptStatCurrentInDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 21),
    _NncFrPVCEndptStatCurrentInDiscdDESet_Type()
)
nncFrPVCEndptStatCurrentInDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdDESet.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdDEClr_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdDEClr_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdDEClr = _NncFrPVCEndptStatCurrentInDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 22),
    _NncFrPVCEndptStatCurrentInDiscdDEClr_Type()
)
nncFrPVCEndptStatCurrentInDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdDEClr.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdBadEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdBadEncaps_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdBadEncaps = _NncFrPVCEndptStatCurrentInDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 23),
    _NncFrPVCEndptStatCurrentInDiscdBadEncaps_Type()
)
nncFrPVCEndptStatCurrentInDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdBadEncaps.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdUnsupEncaps_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdUnsupEncaps = _NncFrPVCEndptStatCurrentInDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 24),
    _NncFrPVCEndptStatCurrentInDiscdUnsupEncaps_Type()
)
nncFrPVCEndptStatCurrentInDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdUnsupEncaps.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdCOSDESet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdCOSDESet_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdCOSDESet = _NncFrPVCEndptStatCurrentInDiscdCOSDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 25),
    _NncFrPVCEndptStatCurrentInDiscdCOSDESet_Type()
)
nncFrPVCEndptStatCurrentInDiscdCOSDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdCOSDESet.setStatus("current")
_NncFrPVCEndptStatCurrentInDiscdCOSDEClr_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentInDiscdCOSDEClr_Object = MibTableColumn
nncFrPVCEndptStatCurrentInDiscdCOSDEClr = _NncFrPVCEndptStatCurrentInDiscdCOSDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 26),
    _NncFrPVCEndptStatCurrentInDiscdCOSDEClr_Type()
)
nncFrPVCEndptStatCurrentInDiscdCOSDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentInDiscdCOSDEClr.setStatus("current")
_NncFrPVCEndptStatCurrentOutDiscdDESet_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutDiscdDESet_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutDiscdDESet = _NncFrPVCEndptStatCurrentOutDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 27),
    _NncFrPVCEndptStatCurrentOutDiscdDESet_Type()
)
nncFrPVCEndptStatCurrentOutDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutDiscdDESet.setStatus("current")
_NncFrPVCEndptStatCurrentOutDiscdDEClr_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutDiscdDEClr_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutDiscdDEClr = _NncFrPVCEndptStatCurrentOutDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 28),
    _NncFrPVCEndptStatCurrentOutDiscdDEClr_Type()
)
nncFrPVCEndptStatCurrentOutDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutDiscdDEClr.setStatus("current")
_NncFrPVCEndptStatCurrentOutDiscdBadEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutDiscdBadEncaps_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutDiscdBadEncaps = _NncFrPVCEndptStatCurrentOutDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 29),
    _NncFrPVCEndptStatCurrentOutDiscdBadEncaps_Type()
)
nncFrPVCEndptStatCurrentOutDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutDiscdBadEncaps.setStatus("current")
_NncFrPVCEndptStatCurrentOutDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentOutDiscdUnsupEncaps_Object = MibTableColumn
nncFrPVCEndptStatCurrentOutDiscdUnsupEncaps = _NncFrPVCEndptStatCurrentOutDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 30),
    _NncFrPVCEndptStatCurrentOutDiscdUnsupEncaps_Type()
)
nncFrPVCEndptStatCurrentOutDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentOutDiscdUnsupEncaps.setStatus("current")
_NncFrPVCEndptStatCurrentStReasDiscards_Type = NncExtCounter64
_NncFrPVCEndptStatCurrentStReasDiscards_Object = MibTableColumn
nncFrPVCEndptStatCurrentStReasDiscards = _NncFrPVCEndptStatCurrentStReasDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 3, 1, 31),
    _NncFrPVCEndptStatCurrentStReasDiscards_Type()
)
nncFrPVCEndptStatCurrentStReasDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentStReasDiscards.setStatus("current")
_NncFrPVCEndptStatIntervalTable_Object = MibTable
nncFrPVCEndptStatIntervalTable = _NncFrPVCEndptStatIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4)
)
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalTable.setStatus("current")
_NncFrPVCEndptStatIntervalEntry_Object = MibTableRow
nncFrPVCEndptStatIntervalEntry = _NncFrPVCEndptStatIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1)
)
nncFrPVCEndptStatIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalDLCINumber"),
    (0, "NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalEntry.setStatus("current")


class _NncFrPVCEndptStatIntervalDLCINumber_Type(Integer32):
    """Custom type nncFrPVCEndptStatIntervalDLCINumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NncFrPVCEndptStatIntervalDLCINumber_Type.__name__ = "Integer32"
_NncFrPVCEndptStatIntervalDLCINumber_Object = MibTableColumn
nncFrPVCEndptStatIntervalDLCINumber = _NncFrPVCEndptStatIntervalDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 1),
    _NncFrPVCEndptStatIntervalDLCINumber_Type()
)
nncFrPVCEndptStatIntervalDLCINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalDLCINumber.setStatus("current")


class _NncFrPVCEndptStatIntervalNumber_Type(Integer32):
    """Custom type nncFrPVCEndptStatIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncFrPVCEndptStatIntervalNumber_Type.__name__ = "Integer32"
_NncFrPVCEndptStatIntervalNumber_Object = MibTableColumn
nncFrPVCEndptStatIntervalNumber = _NncFrPVCEndptStatIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 2),
    _NncFrPVCEndptStatIntervalNumber_Type()
)
nncFrPVCEndptStatIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalNumber.setStatus("current")
_NncFrPVCEndptStatIntervalState_Type = NncExtIntvlStateType
_NncFrPVCEndptStatIntervalState_Object = MibTableColumn
nncFrPVCEndptStatIntervalState = _NncFrPVCEndptStatIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 3),
    _NncFrPVCEndptStatIntervalState_Type()
)
nncFrPVCEndptStatIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalState.setStatus("current")


class _NncFrPVCEndptStatIntervalAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncFrPVCEndptStatIntervalAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_NncFrPVCEndptStatIntervalAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncFrPVCEndptStatIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncFrPVCEndptStatIntervalAbsoluteIntervalNumber = _NncFrPVCEndptStatIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 4),
    _NncFrPVCEndptStatIntervalAbsoluteIntervalNumber_Type()
)
nncFrPVCEndptStatIntervalAbsoluteIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalAbsoluteIntervalNumber.setStatus("current")
_NncFrPVCEndptStatIntervalInFrames_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInFrames_Object = MibTableColumn
nncFrPVCEndptStatIntervalInFrames = _NncFrPVCEndptStatIntervalInFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 5),
    _NncFrPVCEndptStatIntervalInFrames_Type()
)
nncFrPVCEndptStatIntervalInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInFrames.setStatus("current")
_NncFrPVCEndptStatIntervalOutFrames_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutFrames_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutFrames = _NncFrPVCEndptStatIntervalOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 6),
    _NncFrPVCEndptStatIntervalOutFrames_Type()
)
nncFrPVCEndptStatIntervalOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutFrames.setStatus("current")
_NncFrPVCEndptStatIntervalInOctets_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInOctets_Object = MibTableColumn
nncFrPVCEndptStatIntervalInOctets = _NncFrPVCEndptStatIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 7),
    _NncFrPVCEndptStatIntervalInOctets_Type()
)
nncFrPVCEndptStatIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInOctets.setStatus("current")
_NncFrPVCEndptStatIntervalOutOctets_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutOctets_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutOctets = _NncFrPVCEndptStatIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 8),
    _NncFrPVCEndptStatIntervalOutOctets_Type()
)
nncFrPVCEndptStatIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutOctets.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscards_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscards_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscards = _NncFrPVCEndptStatIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 9),
    _NncFrPVCEndptStatIntervalInDiscards_Type()
)
nncFrPVCEndptStatIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscards.setStatus("current")
_NncFrPVCEndptStatIntervalOutExcessFrames_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutExcessFrames_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutExcessFrames = _NncFrPVCEndptStatIntervalOutExcessFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 10),
    _NncFrPVCEndptStatIntervalOutExcessFrames_Type()
)
nncFrPVCEndptStatIntervalOutExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutExcessFrames.setStatus("current")
_NncFrPVCEndptStatIntervalInDEFrames_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDEFrames_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDEFrames = _NncFrPVCEndptStatIntervalInDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 11),
    _NncFrPVCEndptStatIntervalInDEFrames_Type()
)
nncFrPVCEndptStatIntervalInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDEFrames.setStatus("current")
_NncFrPVCEndptStatIntervalInCosTagDeFrames_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInCosTagDeFrames_Object = MibTableColumn
nncFrPVCEndptStatIntervalInCosTagDeFrames = _NncFrPVCEndptStatIntervalInCosTagDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 12),
    _NncFrPVCEndptStatIntervalInCosTagDeFrames_Type()
)
nncFrPVCEndptStatIntervalInCosTagDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInCosTagDeFrames.setStatus("current")
_NncFrPVCEndptStatIntervalInOctetsDESet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInOctetsDESet_Object = MibTableColumn
nncFrPVCEndptStatIntervalInOctetsDESet = _NncFrPVCEndptStatIntervalInOctetsDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 13),
    _NncFrPVCEndptStatIntervalInOctetsDESet_Type()
)
nncFrPVCEndptStatIntervalInOctetsDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInOctetsDESet.setStatus("current")
_NncFrPVCEndptStatIntervalInFramesBECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInFramesBECNSet_Object = MibTableColumn
nncFrPVCEndptStatIntervalInFramesBECNSet = _NncFrPVCEndptStatIntervalInFramesBECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 14),
    _NncFrPVCEndptStatIntervalInFramesBECNSet_Type()
)
nncFrPVCEndptStatIntervalInFramesBECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInFramesBECNSet.setStatus("current")
_NncFrPVCEndptStatIntervalInFramesFECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInFramesFECNSet_Object = MibTableColumn
nncFrPVCEndptStatIntervalInFramesFECNSet = _NncFrPVCEndptStatIntervalInFramesFECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 15),
    _NncFrPVCEndptStatIntervalInFramesFECNSet_Type()
)
nncFrPVCEndptStatIntervalInFramesFECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInFramesFECNSet.setStatus("current")
_NncFrPVCEndptStatIntervalInInvdLength_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInInvdLength_Object = MibTableColumn
nncFrPVCEndptStatIntervalInInvdLength = _NncFrPVCEndptStatIntervalInInvdLength_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 16),
    _NncFrPVCEndptStatIntervalInInvdLength_Type()
)
nncFrPVCEndptStatIntervalInInvdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInInvdLength.setStatus("current")
_NncFrPVCEndptStatIntervalOutOctetsDESet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutOctetsDESet_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutOctetsDESet = _NncFrPVCEndptStatIntervalOutOctetsDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 17),
    _NncFrPVCEndptStatIntervalOutOctetsDESet_Type()
)
nncFrPVCEndptStatIntervalOutOctetsDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutOctetsDESet.setStatus("current")
_NncFrPVCEndptStatIntervalOutFramesBECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutFramesBECNSet_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutFramesBECNSet = _NncFrPVCEndptStatIntervalOutFramesBECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 18),
    _NncFrPVCEndptStatIntervalOutFramesBECNSet_Type()
)
nncFrPVCEndptStatIntervalOutFramesBECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutFramesBECNSet.setStatus("current")
_NncFrPVCEndptStatIntervalOutFramesFECNSet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutFramesFECNSet_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutFramesFECNSet = _NncFrPVCEndptStatIntervalOutFramesFECNSet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 19),
    _NncFrPVCEndptStatIntervalOutFramesFECNSet_Type()
)
nncFrPVCEndptStatIntervalOutFramesFECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutFramesFECNSet.setStatus("current")
_NncFrPVCEndptStatIntervalOutFramesInRed_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutFramesInRed_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutFramesInRed = _NncFrPVCEndptStatIntervalOutFramesInRed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 20),
    _NncFrPVCEndptStatIntervalOutFramesInRed_Type()
)
nncFrPVCEndptStatIntervalOutFramesInRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutFramesInRed.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdOctetsCOS_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdOctetsCOS_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdOctetsCOS = _NncFrPVCEndptStatIntervalInDiscdOctetsCOS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 21),
    _NncFrPVCEndptStatIntervalInDiscdOctetsCOS_Type()
)
nncFrPVCEndptStatIntervalInDiscdOctetsCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdOctetsCOS.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdDESet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdDESet_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdDESet = _NncFrPVCEndptStatIntervalInDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 22),
    _NncFrPVCEndptStatIntervalInDiscdDESet_Type()
)
nncFrPVCEndptStatIntervalInDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdDESet.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdDEClr_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdDEClr_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdDEClr = _NncFrPVCEndptStatIntervalInDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 23),
    _NncFrPVCEndptStatIntervalInDiscdDEClr_Type()
)
nncFrPVCEndptStatIntervalInDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdDEClr.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdBadEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdBadEncaps_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdBadEncaps = _NncFrPVCEndptStatIntervalInDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 24),
    _NncFrPVCEndptStatIntervalInDiscdBadEncaps_Type()
)
nncFrPVCEndptStatIntervalInDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdBadEncaps.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdUnsupEncaps_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdUnsupEncaps = _NncFrPVCEndptStatIntervalInDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 25),
    _NncFrPVCEndptStatIntervalInDiscdUnsupEncaps_Type()
)
nncFrPVCEndptStatIntervalInDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdUnsupEncaps.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdCOSDESet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdCOSDESet_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdCOSDESet = _NncFrPVCEndptStatIntervalInDiscdCOSDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 26),
    _NncFrPVCEndptStatIntervalInDiscdCOSDESet_Type()
)
nncFrPVCEndptStatIntervalInDiscdCOSDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdCOSDESet.setStatus("current")
_NncFrPVCEndptStatIntervalInDiscdCOSDEClr_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalInDiscdCOSDEClr_Object = MibTableColumn
nncFrPVCEndptStatIntervalInDiscdCOSDEClr = _NncFrPVCEndptStatIntervalInDiscdCOSDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 27),
    _NncFrPVCEndptStatIntervalInDiscdCOSDEClr_Type()
)
nncFrPVCEndptStatIntervalInDiscdCOSDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalInDiscdCOSDEClr.setStatus("current")
_NncFrPVCEndptStatIntervalOutDiscdDESet_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutDiscdDESet_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutDiscdDESet = _NncFrPVCEndptStatIntervalOutDiscdDESet_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 28),
    _NncFrPVCEndptStatIntervalOutDiscdDESet_Type()
)
nncFrPVCEndptStatIntervalOutDiscdDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutDiscdDESet.setStatus("current")
_NncFrPVCEndptStatIntervalOutDiscdDEClr_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutDiscdDEClr_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutDiscdDEClr = _NncFrPVCEndptStatIntervalOutDiscdDEClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 29),
    _NncFrPVCEndptStatIntervalOutDiscdDEClr_Type()
)
nncFrPVCEndptStatIntervalOutDiscdDEClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutDiscdDEClr.setStatus("current")
_NncFrPVCEndptStatIntervalOutDiscdBadEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutDiscdBadEncaps_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutDiscdBadEncaps = _NncFrPVCEndptStatIntervalOutDiscdBadEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 30),
    _NncFrPVCEndptStatIntervalOutDiscdBadEncaps_Type()
)
nncFrPVCEndptStatIntervalOutDiscdBadEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutDiscdBadEncaps.setStatus("current")
_NncFrPVCEndptStatIntervalOutDiscdUnsupEncaps_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalOutDiscdUnsupEncaps_Object = MibTableColumn
nncFrPVCEndptStatIntervalOutDiscdUnsupEncaps = _NncFrPVCEndptStatIntervalOutDiscdUnsupEncaps_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 31),
    _NncFrPVCEndptStatIntervalOutDiscdUnsupEncaps_Type()
)
nncFrPVCEndptStatIntervalOutDiscdUnsupEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalOutDiscdUnsupEncaps.setStatus("current")
_NncFrPVCEndptStatIntervalStReasDiscards_Type = NncExtCounter64
_NncFrPVCEndptStatIntervalStReasDiscards_Object = MibTableColumn
nncFrPVCEndptStatIntervalStReasDiscards = _NncFrPVCEndptStatIntervalStReasDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 4, 1, 32),
    _NncFrPVCEndptStatIntervalStReasDiscards_Type()
)
nncFrPVCEndptStatIntervalStReasDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalStReasDiscards.setStatus("current")


class _NncFrDepthOfHistoricalStrata_Type(Integer32):
    """Custom type nncFrDepthOfHistoricalStrata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncFrDepthOfHistoricalStrata_Type.__name__ = "Integer32"
_NncFrDepthOfHistoricalStrata_Object = MibScalar
nncFrDepthOfHistoricalStrata = _NncFrDepthOfHistoricalStrata_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 5),
    _NncFrDepthOfHistoricalStrata_Type()
)
nncFrDepthOfHistoricalStrata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrDepthOfHistoricalStrata.setStatus("current")
_NncFrStrBertStatTable_Object = MibTable
nncFrStrBertStatTable = _NncFrStrBertStatTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6)
)
if mibBuilder.loadTexts:
    nncFrStrBertStatTable.setStatus("current")
_NncFrStrBertStatEntry_Object = MibTableRow
nncFrStrBertStatEntry = _NncFrStrBertStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1)
)
nncFrStrBertStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncFrStrBertStatEntry.setStatus("current")
_NncFrStrBertDlci_Type = Integer32
_NncFrStrBertDlci_Object = MibTableColumn
nncFrStrBertDlci = _NncFrStrBertDlci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 1),
    _NncFrStrBertDlci_Type()
)
nncFrStrBertDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertDlci.setStatus("current")


class _NncFrStrBertStatStatus_Type(Integer32):
    """Custom type nncFrStrBertStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NncFrStrBertStatStatus_Type.__name__ = "Integer32"
_NncFrStrBertStatStatus_Object = MibTableColumn
nncFrStrBertStatStatus = _NncFrStrBertStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 2),
    _NncFrStrBertStatStatus_Type()
)
nncFrStrBertStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatStatus.setStatus("current")
_NncFrStrBertStatTxFrames_Type = Gauge32
_NncFrStrBertStatTxFrames_Object = MibTableColumn
nncFrStrBertStatTxFrames = _NncFrStrBertStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 3),
    _NncFrStrBertStatTxFrames_Type()
)
nncFrStrBertStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatTxFrames.setStatus("current")
_NncFrStrBertStatRxFrames_Type = Gauge32
_NncFrStrBertStatRxFrames_Object = MibTableColumn
nncFrStrBertStatRxFrames = _NncFrStrBertStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 4),
    _NncFrStrBertStatRxFrames_Type()
)
nncFrStrBertStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatRxFrames.setStatus("current")
_NncFrStrBertStatRxBytes_Type = Gauge32
_NncFrStrBertStatRxBytes_Object = MibTableColumn
nncFrStrBertStatRxBytes = _NncFrStrBertStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 5),
    _NncFrStrBertStatRxBytes_Type()
)
nncFrStrBertStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatRxBytes.setStatus("current")
_NncFrStrBertStatTxBytes_Type = Gauge32
_NncFrStrBertStatTxBytes_Object = MibTableColumn
nncFrStrBertStatTxBytes = _NncFrStrBertStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 6),
    _NncFrStrBertStatTxBytes_Type()
)
nncFrStrBertStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatTxBytes.setStatus("current")
_NncFrStrBertStatRxErrors_Type = Gauge32
_NncFrStrBertStatRxErrors_Object = MibTableColumn
nncFrStrBertStatRxErrors = _NncFrStrBertStatRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 7),
    _NncFrStrBertStatRxErrors_Type()
)
nncFrStrBertStatRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatRxErrors.setStatus("current")
_NncFrStrBertStatEstErrors_Type = Gauge32
_NncFrStrBertStatEstErrors_Object = MibTableColumn
nncFrStrBertStatEstErrors = _NncFrStrBertStatEstErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 1, 6, 1, 8),
    _NncFrStrBertStatEstErrors_Type()
)
nncFrStrBertStatEstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrStrBertStatEstErrors.setStatus("current")
_NncFrIntStatisticsTraps_ObjectIdentity = ObjectIdentity
nncFrIntStatisticsTraps = _NncFrIntStatisticsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 2)
)
_NncFrIntStatisticsGroups_ObjectIdentity = ObjectIdentity
nncFrIntStatisticsGroups = _NncFrIntStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 3)
)
_NncFrIntStatisticsCompliances_ObjectIdentity = ObjectIdentity
nncFrIntStatisticsCompliances = _NncFrIntStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 4)
)

# Managed Objects groups

nncFrStrStatCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 3, 1)
)
nncFrStrStatCurrentGroup.setObjects(
      *(("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentState"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentAbsoluteIntervalNumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscards"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutDiscards"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentSigUserProtErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentSigNetProtErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentSigUserLinkRelErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentSigNetLinkRelErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentSigUserChanInactive"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentSigNetChanInactive"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStSCAlarms"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStTimeSC"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStMaxDurationRED"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStMCAlarms"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStTimeMC"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutLinkUtilization"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInLinkUtilization"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInInvdLength"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLastErroredDLCI"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdOctetsCOS"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdCOSDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdCOSDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMSigInvldField"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMSigUnsupMsgType"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMSigInvldEID"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMSigInvldIELen"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMSigInvldRepType"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMSigFrmWithNoIEs"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStUserSequenceErrs"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStNetSequenceErrs"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMUTimeoutsnT1"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMUStatusMsgsRcvd"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMUStatusENQMsgsSent"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMUAsyncStatusRcvd"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMNTimeoutsnT2"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMNStatusMsgsSent"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMNStatusENQMsgsRcvd"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStLMNAsyncStatusSent"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInCRCErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInNonIntegral"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInReservedDLCI"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInInvldEA"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStFrmTooSmall"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInAborts"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInSumOfDisagremnts"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentInOverRuns"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentOutUnderRuns"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentStIntervalDuration"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentBestEffortPeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentCommittedPeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentLowDelayPeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentRealTimePeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentBestEffortAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentCommittedAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentLowDelayAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentRealTimeAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentBestEffortOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentCommittedOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentLowDelayOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentRealTimeOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentBestEffortUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentCommittedUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentLowDelayUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentRealTimeUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentBestEffortDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentCommittedDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentLowDelayDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatCurrentRealTimeDiscdDEClr"))
)
if mibBuilder.loadTexts:
    nncFrStrStatCurrentGroup.setStatus("current")

nncFrStrStatIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 3, 2)
)
nncFrStrStatIntervalGroup.setObjects(
      *(("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalNumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalState"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalAbsoluteIntervalNumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscards"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutDiscards"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalSigUserProtErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalSigNetProtErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalSigUserLinkRelErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalSigNetLinkRelErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalSigUserChanInactive"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalSigNetChanInactive"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStSCAlarms"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStTimeSC"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStMaxDurationRED"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStMCAlarms"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStTimeMC"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutLinkUtilization"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInLinkUtilization"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInInvdLength"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLastErroredDLCI"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdOctetsCOS"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdCOSDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdCOSDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMSigInvldField"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMSigUnsupMsgType"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMSigInvldEID"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMSigInvldIELen"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMSigInvldRepType"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMSigFrmWithNoIEs"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStUserSequenceErrs"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStNetSequenceErrs"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMUTimeoutsnT1"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMUStatusMsgsRcvd"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMUStatusENQMsgsSent"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMUAsyncStatusRcvd"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMNTimeoutsnT2"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMNStatusMsgsSent"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMNStatusENQMsgsRcvd"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStLMNAsyncStatusSent"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInCRCErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInNonIntegral"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInReservedDLCI"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInInvldEA"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStFrmTooSmall"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInAborts"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInSumOfDisagremnts"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalInOverRuns"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalOutUnderRuns"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalStIntervalDuration"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalBestEffortPeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalCommittedPeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalLowDelayPeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalRealTimePeakDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalBestEffortAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalCommittedAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalLowDelayAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalRealTimeAccDelay"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalBestEffortOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalCommittedOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalLowDelayOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalRealTimeOutUCastPackets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalBestEffortUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalCommittedUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalLowDelayUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalRealTimeUCastPacketsDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalBestEffortDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalCommittedDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalLowDelayDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrStatIntervalRealTimeDiscdDEClr"))
)
if mibBuilder.loadTexts:
    nncFrStrStatIntervalGroup.setStatus("current")

nncFrPVCEndptStatCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 3, 3)
)
nncFrPVCEndptStatCurrentGroup.setObjects(
      *(("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentDLCINumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentState"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentAbsoluteIntervalNumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscards"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutExcessFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDEFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInCosTagDeFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInOctetsDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInFramesBECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInFramesFECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInInvdLength"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutOctetsDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutFramesBECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutFramesFECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutFramesInRed"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdOctetsCOS"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdCOSDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentInDiscdCOSDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentOutDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatCurrentStReasDiscards"))
)
if mibBuilder.loadTexts:
    nncFrPVCEndptStatCurrentGroup.setStatus("current")

nncFrPVCEndptStatIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 3, 4)
)
nncFrPVCEndptStatIntervalGroup.setObjects(
      *(("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalDLCINumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalNumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalState"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalAbsoluteIntervalNumber"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutOctets"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscards"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutExcessFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDEFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInCosTagDeFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInOctetsDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInFramesBECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInFramesFECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInInvdLength"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutOctetsDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutFramesBECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutFramesFECNSet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutFramesInRed"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdOctetsCOS"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdCOSDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalInDiscdCOSDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutDiscdDESet"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutDiscdDEClr"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutDiscdBadEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalOutDiscdUnsupEncaps"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrPVCEndptStatIntervalStReasDiscards"))
)
if mibBuilder.loadTexts:
    nncFrPVCEndptStatIntervalGroup.setStatus("current")

nncFrStrBertStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 3, 6)
)
nncFrStrBertStatGroup.setObjects(
      *(("NNCFRINTSTATISTICS-MIB", "nncFrStrBertDlci"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatStatus"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatTxFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatRxFrames"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatTxBytes"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatRxBytes"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatRxErrors"),
        ("NNCFRINTSTATISTICS-MIB", "nncFrStrBertStatEstErrors"))
)
if mibBuilder.loadTexts:
    nncFrStrBertStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncFrIntStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 30, 4, 1)
)
if mibBuilder.loadTexts:
    nncFrIntStatisticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCFRINTSTATISTICS-MIB",
    **{"nncFrIntStatistics": nncFrIntStatistics,
       "nncFrIntStatisticsObjects": nncFrIntStatisticsObjects,
       "nncFrStrStatCurrentTable": nncFrStrStatCurrentTable,
       "nncFrStrStatCurrentEntry": nncFrStrStatCurrentEntry,
       "nncFrStrStatCurrentState": nncFrStrStatCurrentState,
       "nncFrStrStatCurrentAbsoluteIntervalNumber": nncFrStrStatCurrentAbsoluteIntervalNumber,
       "nncFrStrStatCurrentInOctets": nncFrStrStatCurrentInOctets,
       "nncFrStrStatCurrentOutOctets": nncFrStrStatCurrentOutOctets,
       "nncFrStrStatCurrentInUCastPackets": nncFrStrStatCurrentInUCastPackets,
       "nncFrStrStatCurrentOutUCastPackets": nncFrStrStatCurrentOutUCastPackets,
       "nncFrStrStatCurrentInDiscards": nncFrStrStatCurrentInDiscards,
       "nncFrStrStatCurrentOutDiscards": nncFrStrStatCurrentOutDiscards,
       "nncFrStrStatCurrentInErrors": nncFrStrStatCurrentInErrors,
       "nncFrStrStatCurrentOutErrors": nncFrStrStatCurrentOutErrors,
       "nncFrStrStatCurrentSigUserProtErrors": nncFrStrStatCurrentSigUserProtErrors,
       "nncFrStrStatCurrentSigNetProtErrors": nncFrStrStatCurrentSigNetProtErrors,
       "nncFrStrStatCurrentSigUserLinkRelErrors": nncFrStrStatCurrentSigUserLinkRelErrors,
       "nncFrStrStatCurrentSigNetLinkRelErrors": nncFrStrStatCurrentSigNetLinkRelErrors,
       "nncFrStrStatCurrentSigUserChanInactive": nncFrStrStatCurrentSigUserChanInactive,
       "nncFrStrStatCurrentSigNetChanInactive": nncFrStrStatCurrentSigNetChanInactive,
       "nncFrStrStatCurrentStSCAlarms": nncFrStrStatCurrentStSCAlarms,
       "nncFrStrStatCurrentStTimeSC": nncFrStrStatCurrentStTimeSC,
       "nncFrStrStatCurrentStMaxDurationRED": nncFrStrStatCurrentStMaxDurationRED,
       "nncFrStrStatCurrentStMCAlarms": nncFrStrStatCurrentStMCAlarms,
       "nncFrStrStatCurrentStTimeMC": nncFrStrStatCurrentStTimeMC,
       "nncFrStrStatCurrentOutLinkUtilization": nncFrStrStatCurrentOutLinkUtilization,
       "nncFrStrStatCurrentInLinkUtilization": nncFrStrStatCurrentInLinkUtilization,
       "nncFrStrStatCurrentInInvdLength": nncFrStrStatCurrentInInvdLength,
       "nncFrStrStatCurrentStLastErroredDLCI": nncFrStrStatCurrentStLastErroredDLCI,
       "nncFrStrStatCurrentInDiscdOctetsCOS": nncFrStrStatCurrentInDiscdOctetsCOS,
       "nncFrStrStatCurrentInDiscdCOSDESet": nncFrStrStatCurrentInDiscdCOSDESet,
       "nncFrStrStatCurrentInDiscdCOSDEClr": nncFrStrStatCurrentInDiscdCOSDEClr,
       "nncFrStrStatCurrentInDiscdBadEncaps": nncFrStrStatCurrentInDiscdBadEncaps,
       "nncFrStrStatCurrentOutDiscdBadEncaps": nncFrStrStatCurrentOutDiscdBadEncaps,
       "nncFrStrStatCurrentInDiscdUnsupEncaps": nncFrStrStatCurrentInDiscdUnsupEncaps,
       "nncFrStrStatCurrentOutDiscdUnsupEncaps": nncFrStrStatCurrentOutDiscdUnsupEncaps,
       "nncFrStrStatCurrentOutDiscdDESet": nncFrStrStatCurrentOutDiscdDESet,
       "nncFrStrStatCurrentOutDiscdDEClr": nncFrStrStatCurrentOutDiscdDEClr,
       "nncFrStrStatCurrentInDiscdDESet": nncFrStrStatCurrentInDiscdDESet,
       "nncFrStrStatCurrentInDiscdDEClr": nncFrStrStatCurrentInDiscdDEClr,
       "nncFrStrStatCurrentStLMSigInvldField": nncFrStrStatCurrentStLMSigInvldField,
       "nncFrStrStatCurrentStLMSigUnsupMsgType": nncFrStrStatCurrentStLMSigUnsupMsgType,
       "nncFrStrStatCurrentStLMSigInvldEID": nncFrStrStatCurrentStLMSigInvldEID,
       "nncFrStrStatCurrentStLMSigInvldIELen": nncFrStrStatCurrentStLMSigInvldIELen,
       "nncFrStrStatCurrentStLMSigInvldRepType": nncFrStrStatCurrentStLMSigInvldRepType,
       "nncFrStrStatCurrentStLMSigFrmWithNoIEs": nncFrStrStatCurrentStLMSigFrmWithNoIEs,
       "nncFrStrStatCurrentStUserSequenceErrs": nncFrStrStatCurrentStUserSequenceErrs,
       "nncFrStrStatCurrentStNetSequenceErrs": nncFrStrStatCurrentStNetSequenceErrs,
       "nncFrStrStatCurrentStLMUTimeoutsnT1": nncFrStrStatCurrentStLMUTimeoutsnT1,
       "nncFrStrStatCurrentStLMUStatusMsgsRcvd": nncFrStrStatCurrentStLMUStatusMsgsRcvd,
       "nncFrStrStatCurrentStLMUStatusENQMsgsSent": nncFrStrStatCurrentStLMUStatusENQMsgsSent,
       "nncFrStrStatCurrentStLMUAsyncStatusRcvd": nncFrStrStatCurrentStLMUAsyncStatusRcvd,
       "nncFrStrStatCurrentStLMNTimeoutsnT2": nncFrStrStatCurrentStLMNTimeoutsnT2,
       "nncFrStrStatCurrentStLMNStatusMsgsSent": nncFrStrStatCurrentStLMNStatusMsgsSent,
       "nncFrStrStatCurrentStLMNStatusENQMsgsRcvd": nncFrStrStatCurrentStLMNStatusENQMsgsRcvd,
       "nncFrStrStatCurrentStLMNAsyncStatusSent": nncFrStrStatCurrentStLMNAsyncStatusSent,
       "nncFrStrStatCurrentInCRCErrors": nncFrStrStatCurrentInCRCErrors,
       "nncFrStrStatCurrentInNonIntegral": nncFrStrStatCurrentInNonIntegral,
       "nncFrStrStatCurrentInReservedDLCI": nncFrStrStatCurrentInReservedDLCI,
       "nncFrStrStatCurrentInInvldEA": nncFrStrStatCurrentInInvldEA,
       "nncFrStrStatCurrentStFrmTooSmall": nncFrStrStatCurrentStFrmTooSmall,
       "nncFrStrStatCurrentInAborts": nncFrStrStatCurrentInAborts,
       "nncFrStrStatCurrentInSumOfDisagremnts": nncFrStrStatCurrentInSumOfDisagremnts,
       "nncFrStrStatCurrentInOverRuns": nncFrStrStatCurrentInOverRuns,
       "nncFrStrStatCurrentOutUnderRuns": nncFrStrStatCurrentOutUnderRuns,
       "nncFrStrStatCurrentStIntervalDuration": nncFrStrStatCurrentStIntervalDuration,
       "nncFrStrStatCurrentBestEffortPeakDelay": nncFrStrStatCurrentBestEffortPeakDelay,
       "nncFrStrStatCurrentCommittedPeakDelay": nncFrStrStatCurrentCommittedPeakDelay,
       "nncFrStrStatCurrentLowDelayPeakDelay": nncFrStrStatCurrentLowDelayPeakDelay,
       "nncFrStrStatCurrentRealTimePeakDelay": nncFrStrStatCurrentRealTimePeakDelay,
       "nncFrStrStatCurrentBestEffortAccDelay": nncFrStrStatCurrentBestEffortAccDelay,
       "nncFrStrStatCurrentCommittedAccDelay": nncFrStrStatCurrentCommittedAccDelay,
       "nncFrStrStatCurrentLowDelayAccDelay": nncFrStrStatCurrentLowDelayAccDelay,
       "nncFrStrStatCurrentRealTimeAccDelay": nncFrStrStatCurrentRealTimeAccDelay,
       "nncFrStrStatCurrentBestEffortOutUCastPackets": nncFrStrStatCurrentBestEffortOutUCastPackets,
       "nncFrStrStatCurrentCommittedOutUCastPackets": nncFrStrStatCurrentCommittedOutUCastPackets,
       "nncFrStrStatCurrentLowDelayOutUCastPackets": nncFrStrStatCurrentLowDelayOutUCastPackets,
       "nncFrStrStatCurrentRealTimeOutUCastPackets": nncFrStrStatCurrentRealTimeOutUCastPackets,
       "nncFrStrStatCurrentBestEffortUCastPacketsDEClr": nncFrStrStatCurrentBestEffortUCastPacketsDEClr,
       "nncFrStrStatCurrentCommittedUCastPacketsDEClr": nncFrStrStatCurrentCommittedUCastPacketsDEClr,
       "nncFrStrStatCurrentLowDelayUCastPacketsDEClr": nncFrStrStatCurrentLowDelayUCastPacketsDEClr,
       "nncFrStrStatCurrentRealTimeUCastPacketsDEClr": nncFrStrStatCurrentRealTimeUCastPacketsDEClr,
       "nncFrStrStatCurrentBestEffortDiscdDEClr": nncFrStrStatCurrentBestEffortDiscdDEClr,
       "nncFrStrStatCurrentCommittedDiscdDEClr": nncFrStrStatCurrentCommittedDiscdDEClr,
       "nncFrStrStatCurrentLowDelayDiscdDEClr": nncFrStrStatCurrentLowDelayDiscdDEClr,
       "nncFrStrStatCurrentRealTimeDiscdDEClr": nncFrStrStatCurrentRealTimeDiscdDEClr,
       "nncFrStrStatIntervalTable": nncFrStrStatIntervalTable,
       "nncFrStrStatIntervalEntry": nncFrStrStatIntervalEntry,
       "nncFrStrStatIntervalNumber": nncFrStrStatIntervalNumber,
       "nncFrStrStatIntervalState": nncFrStrStatIntervalState,
       "nncFrStrStatIntervalAbsoluteIntervalNumber": nncFrStrStatIntervalAbsoluteIntervalNumber,
       "nncFrStrStatIntervalInOctets": nncFrStrStatIntervalInOctets,
       "nncFrStrStatIntervalOutOctets": nncFrStrStatIntervalOutOctets,
       "nncFrStrStatIntervalInUCastPackets": nncFrStrStatIntervalInUCastPackets,
       "nncFrStrStatIntervalOutUCastPackets": nncFrStrStatIntervalOutUCastPackets,
       "nncFrStrStatIntervalInDiscards": nncFrStrStatIntervalInDiscards,
       "nncFrStrStatIntervalOutDiscards": nncFrStrStatIntervalOutDiscards,
       "nncFrStrStatIntervalInErrors": nncFrStrStatIntervalInErrors,
       "nncFrStrStatIntervalOutErrors": nncFrStrStatIntervalOutErrors,
       "nncFrStrStatIntervalSigUserProtErrors": nncFrStrStatIntervalSigUserProtErrors,
       "nncFrStrStatIntervalSigNetProtErrors": nncFrStrStatIntervalSigNetProtErrors,
       "nncFrStrStatIntervalSigUserLinkRelErrors": nncFrStrStatIntervalSigUserLinkRelErrors,
       "nncFrStrStatIntervalSigNetLinkRelErrors": nncFrStrStatIntervalSigNetLinkRelErrors,
       "nncFrStrStatIntervalSigUserChanInactive": nncFrStrStatIntervalSigUserChanInactive,
       "nncFrStrStatIntervalSigNetChanInactive": nncFrStrStatIntervalSigNetChanInactive,
       "nncFrStrStatIntervalStSCAlarms": nncFrStrStatIntervalStSCAlarms,
       "nncFrStrStatIntervalStTimeSC": nncFrStrStatIntervalStTimeSC,
       "nncFrStrStatIntervalStMaxDurationRED": nncFrStrStatIntervalStMaxDurationRED,
       "nncFrStrStatIntervalStMCAlarms": nncFrStrStatIntervalStMCAlarms,
       "nncFrStrStatIntervalStTimeMC": nncFrStrStatIntervalStTimeMC,
       "nncFrStrStatIntervalOutLinkUtilization": nncFrStrStatIntervalOutLinkUtilization,
       "nncFrStrStatIntervalInLinkUtilization": nncFrStrStatIntervalInLinkUtilization,
       "nncFrStrStatIntervalInInvdLength": nncFrStrStatIntervalInInvdLength,
       "nncFrStrStatIntervalStLastErroredDLCI": nncFrStrStatIntervalStLastErroredDLCI,
       "nncFrStrStatIntervalInDiscdOctetsCOS": nncFrStrStatIntervalInDiscdOctetsCOS,
       "nncFrStrStatIntervalInDiscdCOSDESet": nncFrStrStatIntervalInDiscdCOSDESet,
       "nncFrStrStatIntervalInDiscdCOSDEClr": nncFrStrStatIntervalInDiscdCOSDEClr,
       "nncFrStrStatIntervalInDiscdBadEncaps": nncFrStrStatIntervalInDiscdBadEncaps,
       "nncFrStrStatIntervalOutDiscdBadEncaps": nncFrStrStatIntervalOutDiscdBadEncaps,
       "nncFrStrStatIntervalInDiscdUnsupEncaps": nncFrStrStatIntervalInDiscdUnsupEncaps,
       "nncFrStrStatIntervalOutDiscdUnsupEncaps": nncFrStrStatIntervalOutDiscdUnsupEncaps,
       "nncFrStrStatIntervalOutDiscdDESet": nncFrStrStatIntervalOutDiscdDESet,
       "nncFrStrStatIntervalOutDiscdDEClr": nncFrStrStatIntervalOutDiscdDEClr,
       "nncFrStrStatIntervalInDiscdDESet": nncFrStrStatIntervalInDiscdDESet,
       "nncFrStrStatIntervalInDiscdDEClr": nncFrStrStatIntervalInDiscdDEClr,
       "nncFrStrStatIntervalStLMSigInvldField": nncFrStrStatIntervalStLMSigInvldField,
       "nncFrStrStatIntervalStLMSigUnsupMsgType": nncFrStrStatIntervalStLMSigUnsupMsgType,
       "nncFrStrStatIntervalStLMSigInvldEID": nncFrStrStatIntervalStLMSigInvldEID,
       "nncFrStrStatIntervalStLMSigInvldIELen": nncFrStrStatIntervalStLMSigInvldIELen,
       "nncFrStrStatIntervalStLMSigInvldRepType": nncFrStrStatIntervalStLMSigInvldRepType,
       "nncFrStrStatIntervalStLMSigFrmWithNoIEs": nncFrStrStatIntervalStLMSigFrmWithNoIEs,
       "nncFrStrStatIntervalStUserSequenceErrs": nncFrStrStatIntervalStUserSequenceErrs,
       "nncFrStrStatIntervalStNetSequenceErrs": nncFrStrStatIntervalStNetSequenceErrs,
       "nncFrStrStatIntervalStLMUTimeoutsnT1": nncFrStrStatIntervalStLMUTimeoutsnT1,
       "nncFrStrStatIntervalStLMUStatusMsgsRcvd": nncFrStrStatIntervalStLMUStatusMsgsRcvd,
       "nncFrStrStatIntervalStLMUStatusENQMsgsSent": nncFrStrStatIntervalStLMUStatusENQMsgsSent,
       "nncFrStrStatIntervalStLMUAsyncStatusRcvd": nncFrStrStatIntervalStLMUAsyncStatusRcvd,
       "nncFrStrStatIntervalStLMNTimeoutsnT2": nncFrStrStatIntervalStLMNTimeoutsnT2,
       "nncFrStrStatIntervalStLMNStatusMsgsSent": nncFrStrStatIntervalStLMNStatusMsgsSent,
       "nncFrStrStatIntervalStLMNStatusENQMsgsRcvd": nncFrStrStatIntervalStLMNStatusENQMsgsRcvd,
       "nncFrStrStatIntervalStLMNAsyncStatusSent": nncFrStrStatIntervalStLMNAsyncStatusSent,
       "nncFrStrStatIntervalInCRCErrors": nncFrStrStatIntervalInCRCErrors,
       "nncFrStrStatIntervalInNonIntegral": nncFrStrStatIntervalInNonIntegral,
       "nncFrStrStatIntervalInReservedDLCI": nncFrStrStatIntervalInReservedDLCI,
       "nncFrStrStatIntervalInInvldEA": nncFrStrStatIntervalInInvldEA,
       "nncFrStrStatIntervalStFrmTooSmall": nncFrStrStatIntervalStFrmTooSmall,
       "nncFrStrStatIntervalInAborts": nncFrStrStatIntervalInAborts,
       "nncFrStrStatIntervalInSumOfDisagremnts": nncFrStrStatIntervalInSumOfDisagremnts,
       "nncFrStrStatIntervalInOverRuns": nncFrStrStatIntervalInOverRuns,
       "nncFrStrStatIntervalOutUnderRuns": nncFrStrStatIntervalOutUnderRuns,
       "nncFrStrStatIntervalStIntervalDuration": nncFrStrStatIntervalStIntervalDuration,
       "nncFrStrStatIntervalBestEffortPeakDelay": nncFrStrStatIntervalBestEffortPeakDelay,
       "nncFrStrStatIntervalCommittedPeakDelay": nncFrStrStatIntervalCommittedPeakDelay,
       "nncFrStrStatIntervalLowDelayPeakDelay": nncFrStrStatIntervalLowDelayPeakDelay,
       "nncFrStrStatIntervalRealTimePeakDelay": nncFrStrStatIntervalRealTimePeakDelay,
       "nncFrStrStatIntervalBestEffortAccDelay": nncFrStrStatIntervalBestEffortAccDelay,
       "nncFrStrStatIntervalCommittedAccDelay": nncFrStrStatIntervalCommittedAccDelay,
       "nncFrStrStatIntervalLowDelayAccDelay": nncFrStrStatIntervalLowDelayAccDelay,
       "nncFrStrStatIntervalRealTimeAccDelay": nncFrStrStatIntervalRealTimeAccDelay,
       "nncFrStrStatIntervalBestEffortOutUCastPackets": nncFrStrStatIntervalBestEffortOutUCastPackets,
       "nncFrStrStatIntervalCommittedOutUCastPackets": nncFrStrStatIntervalCommittedOutUCastPackets,
       "nncFrStrStatIntervalLowDelayOutUCastPackets": nncFrStrStatIntervalLowDelayOutUCastPackets,
       "nncFrStrStatIntervalRealTimeOutUCastPackets": nncFrStrStatIntervalRealTimeOutUCastPackets,
       "nncFrStrStatIntervalBestEffortUCastPacketsDEClr": nncFrStrStatIntervalBestEffortUCastPacketsDEClr,
       "nncFrStrStatIntervalCommittedUCastPacketsDEClr": nncFrStrStatIntervalCommittedUCastPacketsDEClr,
       "nncFrStrStatIntervalLowDelayUCastPacketsDEClr": nncFrStrStatIntervalLowDelayUCastPacketsDEClr,
       "nncFrStrStatIntervalRealTimeUCastPacketsDEClr": nncFrStrStatIntervalRealTimeUCastPacketsDEClr,
       "nncFrStrStatIntervalBestEffortDiscdDEClr": nncFrStrStatIntervalBestEffortDiscdDEClr,
       "nncFrStrStatIntervalCommittedDiscdDEClr": nncFrStrStatIntervalCommittedDiscdDEClr,
       "nncFrStrStatIntervalLowDelayDiscdDEClr": nncFrStrStatIntervalLowDelayDiscdDEClr,
       "nncFrStrStatIntervalRealTimeDiscdDEClr": nncFrStrStatIntervalRealTimeDiscdDEClr,
       "nncFrPVCEndptStatCurrentTable": nncFrPVCEndptStatCurrentTable,
       "nncFrPVCEndptStatCurrentEntry": nncFrPVCEndptStatCurrentEntry,
       "nncFrPVCEndptStatCurrentDLCINumber": nncFrPVCEndptStatCurrentDLCINumber,
       "nncFrPVCEndptStatCurrentState": nncFrPVCEndptStatCurrentState,
       "nncFrPVCEndptStatCurrentAbsoluteIntervalNumber": nncFrPVCEndptStatCurrentAbsoluteIntervalNumber,
       "nncFrPVCEndptStatCurrentInFrames": nncFrPVCEndptStatCurrentInFrames,
       "nncFrPVCEndptStatCurrentOutFrames": nncFrPVCEndptStatCurrentOutFrames,
       "nncFrPVCEndptStatCurrentInOctets": nncFrPVCEndptStatCurrentInOctets,
       "nncFrPVCEndptStatCurrentOutOctets": nncFrPVCEndptStatCurrentOutOctets,
       "nncFrPVCEndptStatCurrentInDiscards": nncFrPVCEndptStatCurrentInDiscards,
       "nncFrPVCEndptStatCurrentOutExcessFrames": nncFrPVCEndptStatCurrentOutExcessFrames,
       "nncFrPVCEndptStatCurrentInDEFrames": nncFrPVCEndptStatCurrentInDEFrames,
       "nncFrPVCEndptStatCurrentInCosTagDeFrames": nncFrPVCEndptStatCurrentInCosTagDeFrames,
       "nncFrPVCEndptStatCurrentInOctetsDESet": nncFrPVCEndptStatCurrentInOctetsDESet,
       "nncFrPVCEndptStatCurrentInFramesBECNSet": nncFrPVCEndptStatCurrentInFramesBECNSet,
       "nncFrPVCEndptStatCurrentInFramesFECNSet": nncFrPVCEndptStatCurrentInFramesFECNSet,
       "nncFrPVCEndptStatCurrentInInvdLength": nncFrPVCEndptStatCurrentInInvdLength,
       "nncFrPVCEndptStatCurrentOutOctetsDESet": nncFrPVCEndptStatCurrentOutOctetsDESet,
       "nncFrPVCEndptStatCurrentOutFramesBECNSet": nncFrPVCEndptStatCurrentOutFramesBECNSet,
       "nncFrPVCEndptStatCurrentOutFramesFECNSet": nncFrPVCEndptStatCurrentOutFramesFECNSet,
       "nncFrPVCEndptStatCurrentOutFramesInRed": nncFrPVCEndptStatCurrentOutFramesInRed,
       "nncFrPVCEndptStatCurrentInDiscdOctetsCOS": nncFrPVCEndptStatCurrentInDiscdOctetsCOS,
       "nncFrPVCEndptStatCurrentInDiscdDESet": nncFrPVCEndptStatCurrentInDiscdDESet,
       "nncFrPVCEndptStatCurrentInDiscdDEClr": nncFrPVCEndptStatCurrentInDiscdDEClr,
       "nncFrPVCEndptStatCurrentInDiscdBadEncaps": nncFrPVCEndptStatCurrentInDiscdBadEncaps,
       "nncFrPVCEndptStatCurrentInDiscdUnsupEncaps": nncFrPVCEndptStatCurrentInDiscdUnsupEncaps,
       "nncFrPVCEndptStatCurrentInDiscdCOSDESet": nncFrPVCEndptStatCurrentInDiscdCOSDESet,
       "nncFrPVCEndptStatCurrentInDiscdCOSDEClr": nncFrPVCEndptStatCurrentInDiscdCOSDEClr,
       "nncFrPVCEndptStatCurrentOutDiscdDESet": nncFrPVCEndptStatCurrentOutDiscdDESet,
       "nncFrPVCEndptStatCurrentOutDiscdDEClr": nncFrPVCEndptStatCurrentOutDiscdDEClr,
       "nncFrPVCEndptStatCurrentOutDiscdBadEncaps": nncFrPVCEndptStatCurrentOutDiscdBadEncaps,
       "nncFrPVCEndptStatCurrentOutDiscdUnsupEncaps": nncFrPVCEndptStatCurrentOutDiscdUnsupEncaps,
       "nncFrPVCEndptStatCurrentStReasDiscards": nncFrPVCEndptStatCurrentStReasDiscards,
       "nncFrPVCEndptStatIntervalTable": nncFrPVCEndptStatIntervalTable,
       "nncFrPVCEndptStatIntervalEntry": nncFrPVCEndptStatIntervalEntry,
       "nncFrPVCEndptStatIntervalDLCINumber": nncFrPVCEndptStatIntervalDLCINumber,
       "nncFrPVCEndptStatIntervalNumber": nncFrPVCEndptStatIntervalNumber,
       "nncFrPVCEndptStatIntervalState": nncFrPVCEndptStatIntervalState,
       "nncFrPVCEndptStatIntervalAbsoluteIntervalNumber": nncFrPVCEndptStatIntervalAbsoluteIntervalNumber,
       "nncFrPVCEndptStatIntervalInFrames": nncFrPVCEndptStatIntervalInFrames,
       "nncFrPVCEndptStatIntervalOutFrames": nncFrPVCEndptStatIntervalOutFrames,
       "nncFrPVCEndptStatIntervalInOctets": nncFrPVCEndptStatIntervalInOctets,
       "nncFrPVCEndptStatIntervalOutOctets": nncFrPVCEndptStatIntervalOutOctets,
       "nncFrPVCEndptStatIntervalInDiscards": nncFrPVCEndptStatIntervalInDiscards,
       "nncFrPVCEndptStatIntervalOutExcessFrames": nncFrPVCEndptStatIntervalOutExcessFrames,
       "nncFrPVCEndptStatIntervalInDEFrames": nncFrPVCEndptStatIntervalInDEFrames,
       "nncFrPVCEndptStatIntervalInCosTagDeFrames": nncFrPVCEndptStatIntervalInCosTagDeFrames,
       "nncFrPVCEndptStatIntervalInOctetsDESet": nncFrPVCEndptStatIntervalInOctetsDESet,
       "nncFrPVCEndptStatIntervalInFramesBECNSet": nncFrPVCEndptStatIntervalInFramesBECNSet,
       "nncFrPVCEndptStatIntervalInFramesFECNSet": nncFrPVCEndptStatIntervalInFramesFECNSet,
       "nncFrPVCEndptStatIntervalInInvdLength": nncFrPVCEndptStatIntervalInInvdLength,
       "nncFrPVCEndptStatIntervalOutOctetsDESet": nncFrPVCEndptStatIntervalOutOctetsDESet,
       "nncFrPVCEndptStatIntervalOutFramesBECNSet": nncFrPVCEndptStatIntervalOutFramesBECNSet,
       "nncFrPVCEndptStatIntervalOutFramesFECNSet": nncFrPVCEndptStatIntervalOutFramesFECNSet,
       "nncFrPVCEndptStatIntervalOutFramesInRed": nncFrPVCEndptStatIntervalOutFramesInRed,
       "nncFrPVCEndptStatIntervalInDiscdOctetsCOS": nncFrPVCEndptStatIntervalInDiscdOctetsCOS,
       "nncFrPVCEndptStatIntervalInDiscdDESet": nncFrPVCEndptStatIntervalInDiscdDESet,
       "nncFrPVCEndptStatIntervalInDiscdDEClr": nncFrPVCEndptStatIntervalInDiscdDEClr,
       "nncFrPVCEndptStatIntervalInDiscdBadEncaps": nncFrPVCEndptStatIntervalInDiscdBadEncaps,
       "nncFrPVCEndptStatIntervalInDiscdUnsupEncaps": nncFrPVCEndptStatIntervalInDiscdUnsupEncaps,
       "nncFrPVCEndptStatIntervalInDiscdCOSDESet": nncFrPVCEndptStatIntervalInDiscdCOSDESet,
       "nncFrPVCEndptStatIntervalInDiscdCOSDEClr": nncFrPVCEndptStatIntervalInDiscdCOSDEClr,
       "nncFrPVCEndptStatIntervalOutDiscdDESet": nncFrPVCEndptStatIntervalOutDiscdDESet,
       "nncFrPVCEndptStatIntervalOutDiscdDEClr": nncFrPVCEndptStatIntervalOutDiscdDEClr,
       "nncFrPVCEndptStatIntervalOutDiscdBadEncaps": nncFrPVCEndptStatIntervalOutDiscdBadEncaps,
       "nncFrPVCEndptStatIntervalOutDiscdUnsupEncaps": nncFrPVCEndptStatIntervalOutDiscdUnsupEncaps,
       "nncFrPVCEndptStatIntervalStReasDiscards": nncFrPVCEndptStatIntervalStReasDiscards,
       "nncFrDepthOfHistoricalStrata": nncFrDepthOfHistoricalStrata,
       "nncFrStrBertStatTable": nncFrStrBertStatTable,
       "nncFrStrBertStatEntry": nncFrStrBertStatEntry,
       "nncFrStrBertDlci": nncFrStrBertDlci,
       "nncFrStrBertStatStatus": nncFrStrBertStatStatus,
       "nncFrStrBertStatTxFrames": nncFrStrBertStatTxFrames,
       "nncFrStrBertStatRxFrames": nncFrStrBertStatRxFrames,
       "nncFrStrBertStatRxBytes": nncFrStrBertStatRxBytes,
       "nncFrStrBertStatTxBytes": nncFrStrBertStatTxBytes,
       "nncFrStrBertStatRxErrors": nncFrStrBertStatRxErrors,
       "nncFrStrBertStatEstErrors": nncFrStrBertStatEstErrors,
       "nncFrIntStatisticsTraps": nncFrIntStatisticsTraps,
       "nncFrIntStatisticsGroups": nncFrIntStatisticsGroups,
       "nncFrStrStatCurrentGroup": nncFrStrStatCurrentGroup,
       "nncFrStrStatIntervalGroup": nncFrStrStatIntervalGroup,
       "nncFrPVCEndptStatCurrentGroup": nncFrPVCEndptStatCurrentGroup,
       "nncFrPVCEndptStatIntervalGroup": nncFrPVCEndptStatIntervalGroup,
       "nncFrStrBertStatGroup": nncFrStrBertStatGroup,
       "nncFrIntStatisticsCompliances": nncFrIntStatisticsCompliances,
       "nncFrIntStatisticsCompliance": nncFrIntStatisticsCompliance}
)
