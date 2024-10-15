# SNMP MIB module (GBOND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBOND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:02 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfIntervalThreshold,
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfTotalCount,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfIntervalThreshold",
    "HCPerfInvalidIntervals",
    "HCPerfTimeElapsed",
    "HCPerfTotalCount",
    "HCPerfValidIntervals")

(IANAgBondScheme,
 IANAgBondSchemeList) = mibBuilder.importSymbols(
    "IANA-GBOND-TC-MIB",
    "IANAgBondScheme",
    "IANAgBondSchemeList")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gBondMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 211)
)
gBondMIB.setRevisions(
        ("2013-02-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GBondPm1DayIntervalThreshold(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



# MIB Managed Objects in the order of their OIDs

_GBondObjects_ObjectIdentity = ObjectIdentity
gBondObjects = _GBondObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1)
)
_GBondPort_ObjectIdentity = ObjectIdentity
gBondPort = _GBondPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 1)
)
_GBondPortNotifications_ObjectIdentity = ObjectIdentity
gBondPortNotifications = _GBondPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0)
)
_GBondPortConfTable_Object = MibTable
gBondPortConfTable = _GBondPortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gBondPortConfTable.setStatus("current")
_GBondPortConfEntry_Object = MibTableRow
gBondPortConfEntry = _GBondPortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1)
)
gBondPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondPortConfEntry.setStatus("current")
_GBondPortConfAdminScheme_Type = IANAgBondScheme
_GBondPortConfAdminScheme_Object = MibTableColumn
gBondPortConfAdminScheme = _GBondPortConfAdminScheme_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 1),
    _GBondPortConfAdminScheme_Type()
)
gBondPortConfAdminScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfAdminScheme.setStatus("current")
_GBondPortConfPeerAdminScheme_Type = IANAgBondScheme
_GBondPortConfPeerAdminScheme_Object = MibTableColumn
gBondPortConfPeerAdminScheme = _GBondPortConfPeerAdminScheme_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 2),
    _GBondPortConfPeerAdminScheme_Type()
)
gBondPortConfPeerAdminScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfPeerAdminScheme.setStatus("current")


class _GBondPortConfDiscoveryCode_Type(PhysAddress):
    """Custom type gBondPortConfDiscoveryCode based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GBondPortConfDiscoveryCode_Type.__name__ = "PhysAddress"
_GBondPortConfDiscoveryCode_Object = MibTableColumn
gBondPortConfDiscoveryCode = _GBondPortConfDiscoveryCode_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 3),
    _GBondPortConfDiscoveryCode_Type()
)
gBondPortConfDiscoveryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfDiscoveryCode.setStatus("current")


class _GBondPortConfTargetUpDataRate_Type(Unsigned32):
    """Custom type gBondPortConfTargetUpDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000000),
    )


_GBondPortConfTargetUpDataRate_Type.__name__ = "Unsigned32"
_GBondPortConfTargetUpDataRate_Object = MibTableColumn
gBondPortConfTargetUpDataRate = _GBondPortConfTargetUpDataRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 4),
    _GBondPortConfTargetUpDataRate_Type()
)
gBondPortConfTargetUpDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfTargetUpDataRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortConfTargetUpDataRate.setUnits("Kbps")


class _GBondPortConfTargetDnDataRate_Type(Unsigned32):
    """Custom type gBondPortConfTargetDnDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000000),
    )


_GBondPortConfTargetDnDataRate_Type.__name__ = "Unsigned32"
_GBondPortConfTargetDnDataRate_Object = MibTableColumn
gBondPortConfTargetDnDataRate = _GBondPortConfTargetDnDataRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 5),
    _GBondPortConfTargetDnDataRate_Type()
)
gBondPortConfTargetDnDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfTargetDnDataRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortConfTargetDnDataRate.setUnits("Kbps")


class _GBondPortConfThreshLowUpRate_Type(Unsigned32):
    """Custom type gBondPortConfThreshLowUpRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_GBondPortConfThreshLowUpRate_Type.__name__ = "Unsigned32"
_GBondPortConfThreshLowUpRate_Object = MibTableColumn
gBondPortConfThreshLowUpRate = _GBondPortConfThreshLowUpRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 6),
    _GBondPortConfThreshLowUpRate_Type()
)
gBondPortConfThreshLowUpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfThreshLowUpRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortConfThreshLowUpRate.setUnits("Kbps")


class _GBondPortConfThreshLowDnRate_Type(Unsigned32):
    """Custom type gBondPortConfThreshLowDnRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_GBondPortConfThreshLowDnRate_Type.__name__ = "Unsigned32"
_GBondPortConfThreshLowDnRate_Object = MibTableColumn
gBondPortConfThreshLowDnRate = _GBondPortConfThreshLowDnRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 7),
    _GBondPortConfThreshLowDnRate_Type()
)
gBondPortConfThreshLowDnRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfThreshLowDnRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortConfThreshLowDnRate.setUnits("Kbps")
_GBondPortConfLowRateCrossingEnable_Type = TruthValue
_GBondPortConfLowRateCrossingEnable_Object = MibTableColumn
gBondPortConfLowRateCrossingEnable = _GBondPortConfLowRateCrossingEnable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 8),
    _GBondPortConfLowRateCrossingEnable_Type()
)
gBondPortConfLowRateCrossingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfLowRateCrossingEnable.setStatus("current")


class _GBondPortConfPmTcaConfProfile_Type(SnmpAdminString):
    """Custom type gBondPortConfPmTcaConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GBondPortConfPmTcaConfProfile_Type.__name__ = "SnmpAdminString"
_GBondPortConfPmTcaConfProfile_Object = MibTableColumn
gBondPortConfPmTcaConfProfile = _GBondPortConfPmTcaConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 9),
    _GBondPortConfPmTcaConfProfile_Type()
)
gBondPortConfPmTcaConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfPmTcaConfProfile.setStatus("current")
_GBondPortConfPmTcaEnable_Type = TruthValue
_GBondPortConfPmTcaEnable_Object = MibTableColumn
gBondPortConfPmTcaEnable = _GBondPortConfPmTcaEnable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 10),
    _GBondPortConfPmTcaEnable_Type()
)
gBondPortConfPmTcaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondPortConfPmTcaEnable.setStatus("current")
_GBondPortCapTable_Object = MibTable
gBondPortCapTable = _GBondPortCapTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gBondPortCapTable.setStatus("current")
_GBondPortCapEntry_Object = MibTableRow
gBondPortCapEntry = _GBondPortCapEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 2, 1)
)
gBondPortCapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondPortCapEntry.setStatus("current")
_GBondPortCapSchemesSupported_Type = IANAgBondSchemeList
_GBondPortCapSchemesSupported_Object = MibTableColumn
gBondPortCapSchemesSupported = _GBondPortCapSchemesSupported_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 2, 1, 1),
    _GBondPortCapSchemesSupported_Type()
)
gBondPortCapSchemesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortCapSchemesSupported.setStatus("current")
_GBondPortCapPeerSchemesSupported_Type = IANAgBondSchemeList
_GBondPortCapPeerSchemesSupported_Object = MibTableColumn
gBondPortCapPeerSchemesSupported = _GBondPortCapPeerSchemesSupported_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 2, 1, 2),
    _GBondPortCapPeerSchemesSupported_Type()
)
gBondPortCapPeerSchemesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortCapPeerSchemesSupported.setStatus("current")


class _GBondPortCapCapacity_Type(Unsigned32):
    """Custom type gBondPortCapCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GBondPortCapCapacity_Type.__name__ = "Unsigned32"
_GBondPortCapCapacity_Object = MibTableColumn
gBondPortCapCapacity = _GBondPortCapCapacity_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 2, 1, 3),
    _GBondPortCapCapacity_Type()
)
gBondPortCapCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortCapCapacity.setStatus("current")


class _GBondPortCapPeerCapacity_Type(Unsigned32):
    """Custom type gBondPortCapPeerCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_GBondPortCapPeerCapacity_Type.__name__ = "Unsigned32"
_GBondPortCapPeerCapacity_Object = MibTableColumn
gBondPortCapPeerCapacity = _GBondPortCapPeerCapacity_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 2, 1, 4),
    _GBondPortCapPeerCapacity_Type()
)
gBondPortCapPeerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortCapPeerCapacity.setStatus("current")
_GBondPortStatTable_Object = MibTable
gBondPortStatTable = _GBondPortStatTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gBondPortStatTable.setStatus("current")
_GBondPortStatEntry_Object = MibTableRow
gBondPortStatEntry = _GBondPortStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1)
)
gBondPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondPortStatEntry.setStatus("current")
_GBondPortStatOperScheme_Type = IANAgBondScheme
_GBondPortStatOperScheme_Object = MibTableColumn
gBondPortStatOperScheme = _GBondPortStatOperScheme_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 1),
    _GBondPortStatOperScheme_Type()
)
gBondPortStatOperScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatOperScheme.setStatus("current")
_GBondPortStatPeerOperScheme_Type = IANAgBondScheme
_GBondPortStatPeerOperScheme_Object = MibTableColumn
gBondPortStatPeerOperScheme = _GBondPortStatPeerOperScheme_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 2),
    _GBondPortStatPeerOperScheme_Type()
)
gBondPortStatPeerOperScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatPeerOperScheme.setStatus("current")
_GBondPortStatUpDataRate_Type = Gauge32
_GBondPortStatUpDataRate_Object = MibTableColumn
gBondPortStatUpDataRate = _GBondPortStatUpDataRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 3),
    _GBondPortStatUpDataRate_Type()
)
gBondPortStatUpDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatUpDataRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortStatUpDataRate.setUnits("bps")
_GBondPortStatDnDataRate_Type = Gauge32
_GBondPortStatDnDataRate_Object = MibTableColumn
gBondPortStatDnDataRate = _GBondPortStatDnDataRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 4),
    _GBondPortStatDnDataRate_Type()
)
gBondPortStatDnDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatDnDataRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortStatDnDataRate.setUnits("bps")


class _GBondPortStatFltStatus_Type(Bits):
    """Custom type gBondPortStatFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("bceSubTypeMismatch", 3),
          ("init", 5),
          ("lowRate", 4),
          ("noPeer", 0),
          ("peerBondSchemeMismatch", 2),
          ("peerPowerLoss", 1),
          ("ready", 6))
    )

_GBondPortStatFltStatus_Type.__name__ = "Bits"
_GBondPortStatFltStatus_Object = MibTableColumn
gBondPortStatFltStatus = _GBondPortStatFltStatus_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 5),
    _GBondPortStatFltStatus_Type()
)
gBondPortStatFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatFltStatus.setStatus("current")


class _GBondPortStatSide_Type(Integer32):
    """Custom type gBondPortStatSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("office", 2),
          ("subscriber", 1),
          ("unknown", 3))
    )


_GBondPortStatSide_Type.__name__ = "Integer32"
_GBondPortStatSide_Object = MibTableColumn
gBondPortStatSide = _GBondPortStatSide_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 6),
    _GBondPortStatSide_Type()
)
gBondPortStatSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatSide.setStatus("current")


class _GBondPortStatNumBCEs_Type(Unsigned32):
    """Custom type gBondPortStatNumBCEs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_GBondPortStatNumBCEs_Type.__name__ = "Unsigned32"
_GBondPortStatNumBCEs_Object = MibTableColumn
gBondPortStatNumBCEs = _GBondPortStatNumBCEs_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 3, 1, 7),
    _GBondPortStatNumBCEs_Type()
)
gBondPortStatNumBCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortStatNumBCEs.setStatus("current")
_GBondPortPM_ObjectIdentity = ObjectIdentity
gBondPortPM = _GBondPortPM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4)
)
_GBondPortPmCurTable_Object = MibTable
gBondPortPmCurTable = _GBondPortPmCurTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    gBondPortPmCurTable.setStatus("current")
_GBondPortPmCurEntry_Object = MibTableRow
gBondPortPmCurEntry = _GBondPortPmCurEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1)
)
gBondPortPmCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondPortPmCurEntry.setStatus("current")
_GBondPortPmCurES_Type = HCPerfTotalCount
_GBondPortPmCurES_Object = MibTableColumn
gBondPortPmCurES = _GBondPortPmCurES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 1),
    _GBondPortPmCurES_Type()
)
gBondPortPmCurES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCurES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCurES.setUnits("seconds")
_GBondPortPmCurSES_Type = HCPerfTotalCount
_GBondPortPmCurSES_Object = MibTableColumn
gBondPortPmCurSES = _GBondPortPmCurSES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 2),
    _GBondPortPmCurSES_Type()
)
gBondPortPmCurSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCurSES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCurSES.setUnits("seconds")
_GBondPortPmCurUAS_Type = HCPerfTotalCount
_GBondPortPmCurUAS_Object = MibTableColumn
gBondPortPmCurUAS = _GBondPortPmCurUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 3),
    _GBondPortPmCurUAS_Type()
)
gBondPortPmCurUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCurUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCurUAS.setUnits("seconds")
_GBondPortPmCur15MinValidIntervals_Type = HCPerfValidIntervals
_GBondPortPmCur15MinValidIntervals_Object = MibTableColumn
gBondPortPmCur15MinValidIntervals = _GBondPortPmCur15MinValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 4),
    _GBondPortPmCur15MinValidIntervals_Type()
)
gBondPortPmCur15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinValidIntervals.setStatus("current")
_GBondPortPmCur15MinInvalidIntervals_Type = HCPerfInvalidIntervals
_GBondPortPmCur15MinInvalidIntervals_Object = MibTableColumn
gBondPortPmCur15MinInvalidIntervals = _GBondPortPmCur15MinInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 5),
    _GBondPortPmCur15MinInvalidIntervals_Type()
)
gBondPortPmCur15MinInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinInvalidIntervals.setStatus("current")
_GBondPortPmCur15MinTimeElapsed_Type = HCPerfTimeElapsed
_GBondPortPmCur15MinTimeElapsed_Object = MibTableColumn
gBondPortPmCur15MinTimeElapsed = _GBondPortPmCur15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 6),
    _GBondPortPmCur15MinTimeElapsed_Type()
)
gBondPortPmCur15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinTimeElapsed.setUnits("seconds")
_GBondPortPmCur15MinES_Type = HCPerfCurrentCount
_GBondPortPmCur15MinES_Object = MibTableColumn
gBondPortPmCur15MinES = _GBondPortPmCur15MinES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 7),
    _GBondPortPmCur15MinES_Type()
)
gBondPortPmCur15MinES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinES.setUnits("seconds")
_GBondPortPmCur15MinSES_Type = HCPerfCurrentCount
_GBondPortPmCur15MinSES_Object = MibTableColumn
gBondPortPmCur15MinSES = _GBondPortPmCur15MinSES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 8),
    _GBondPortPmCur15MinSES_Type()
)
gBondPortPmCur15MinSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinSES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinSES.setUnits("seconds")
_GBondPortPmCur15MinUAS_Type = HCPerfCurrentCount
_GBondPortPmCur15MinUAS_Object = MibTableColumn
gBondPortPmCur15MinUAS = _GBondPortPmCur15MinUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 9),
    _GBondPortPmCur15MinUAS_Type()
)
gBondPortPmCur15MinUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur15MinUAS.setUnits("seconds")


class _GBondPortPmCur1DayValidIntervals_Type(Unsigned32):
    """Custom type gBondPortPmCur1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GBondPortPmCur1DayValidIntervals_Type.__name__ = "Unsigned32"
_GBondPortPmCur1DayValidIntervals_Object = MibTableColumn
gBondPortPmCur1DayValidIntervals = _GBondPortPmCur1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 10),
    _GBondPortPmCur1DayValidIntervals_Type()
)
gBondPortPmCur1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayValidIntervals.setUnits("days")


class _GBondPortPmCur1DayInvalidIntervals_Type(Unsigned32):
    """Custom type gBondPortPmCur1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GBondPortPmCur1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_GBondPortPmCur1DayInvalidIntervals_Object = MibTableColumn
gBondPortPmCur1DayInvalidIntervals = _GBondPortPmCur1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 11),
    _GBondPortPmCur1DayInvalidIntervals_Type()
)
gBondPortPmCur1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayInvalidIntervals.setUnits("days")
_GBondPortPmCur1DayTimeElapsed_Type = HCPerfTimeElapsed
_GBondPortPmCur1DayTimeElapsed_Object = MibTableColumn
gBondPortPmCur1DayTimeElapsed = _GBondPortPmCur1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 12),
    _GBondPortPmCur1DayTimeElapsed_Type()
)
gBondPortPmCur1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayTimeElapsed.setUnits("seconds")
_GBondPortPmCur1DayES_Type = HCPerfCurrentCount
_GBondPortPmCur1DayES_Object = MibTableColumn
gBondPortPmCur1DayES = _GBondPortPmCur1DayES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 13),
    _GBondPortPmCur1DayES_Type()
)
gBondPortPmCur1DayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayES.setUnits("seconds")
_GBondPortPmCur1DaySES_Type = HCPerfCurrentCount
_GBondPortPmCur1DaySES_Object = MibTableColumn
gBondPortPmCur1DaySES = _GBondPortPmCur1DaySES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 14),
    _GBondPortPmCur1DaySES_Type()
)
gBondPortPmCur1DaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur1DaySES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur1DaySES.setUnits("seconds")
_GBondPortPmCur1DayUAS_Type = HCPerfCurrentCount
_GBondPortPmCur1DayUAS_Object = MibTableColumn
gBondPortPmCur1DayUAS = _GBondPortPmCur1DayUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 1, 1, 15),
    _GBondPortPmCur1DayUAS_Type()
)
gBondPortPmCur1DayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmCur1DayUAS.setUnits("seconds")
_GBondPortPm15MinTable_Object = MibTable
gBondPortPm15MinTable = _GBondPortPm15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    gBondPortPm15MinTable.setStatus("current")
_GBondPortPm15MinEntry_Object = MibTableRow
gBondPortPm15MinEntry = _GBondPortPm15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1)
)
gBondPortPm15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "GBOND-MIB", "gBondPortPm15MinIntervalIndex"),
)
if mibBuilder.loadTexts:
    gBondPortPm15MinEntry.setStatus("current")


class _GBondPortPm15MinIntervalIndex_Type(Unsigned32):
    """Custom type gBondPortPm15MinIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GBondPortPm15MinIntervalIndex_Type.__name__ = "Unsigned32"
_GBondPortPm15MinIntervalIndex_Object = MibTableColumn
gBondPortPm15MinIntervalIndex = _GBondPortPm15MinIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1, 1),
    _GBondPortPm15MinIntervalIndex_Type()
)
gBondPortPm15MinIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalIndex.setStatus("current")
_GBondPortPm15MinIntervalMoniTime_Type = HCPerfTimeElapsed
_GBondPortPm15MinIntervalMoniTime_Object = MibTableColumn
gBondPortPm15MinIntervalMoniTime = _GBondPortPm15MinIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1, 2),
    _GBondPortPm15MinIntervalMoniTime_Type()
)
gBondPortPm15MinIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalMoniTime.setUnits("seconds")
_GBondPortPm15MinIntervalES_Type = HCPerfIntervalCount
_GBondPortPm15MinIntervalES_Object = MibTableColumn
gBondPortPm15MinIntervalES = _GBondPortPm15MinIntervalES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1, 3),
    _GBondPortPm15MinIntervalES_Type()
)
gBondPortPm15MinIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalES.setUnits("seconds")
_GBondPortPm15MinIntervalSES_Type = HCPerfIntervalCount
_GBondPortPm15MinIntervalSES_Object = MibTableColumn
gBondPortPm15MinIntervalSES = _GBondPortPm15MinIntervalSES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1, 4),
    _GBondPortPm15MinIntervalSES_Type()
)
gBondPortPm15MinIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalSES.setUnits("seconds")
_GBondPortPm15MinIntervalUAS_Type = HCPerfIntervalCount
_GBondPortPm15MinIntervalUAS_Object = MibTableColumn
gBondPortPm15MinIntervalUAS = _GBondPortPm15MinIntervalUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1, 5),
    _GBondPortPm15MinIntervalUAS_Type()
)
gBondPortPm15MinIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalUAS.setUnits("seconds")
_GBondPortPm15MinIntervalValid_Type = TruthValue
_GBondPortPm15MinIntervalValid_Object = MibTableColumn
gBondPortPm15MinIntervalValid = _GBondPortPm15MinIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 2, 1, 6),
    _GBondPortPm15MinIntervalValid_Type()
)
gBondPortPm15MinIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm15MinIntervalValid.setStatus("current")
_GBondPortPm1DayTable_Object = MibTable
gBondPortPm1DayTable = _GBondPortPm1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    gBondPortPm1DayTable.setStatus("current")
_GBondPortPm1DayEntry_Object = MibTableRow
gBondPortPm1DayEntry = _GBondPortPm1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1)
)
gBondPortPm1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "GBOND-MIB", "gBondPortPm1DayIntervalIndex"),
)
if mibBuilder.loadTexts:
    gBondPortPm1DayEntry.setStatus("current")


class _GBondPortPm1DayIntervalIndex_Type(Unsigned32):
    """Custom type gBondPortPm1DayIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_GBondPortPm1DayIntervalIndex_Type.__name__ = "Unsigned32"
_GBondPortPm1DayIntervalIndex_Object = MibTableColumn
gBondPortPm1DayIntervalIndex = _GBondPortPm1DayIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1, 1),
    _GBondPortPm1DayIntervalIndex_Type()
)
gBondPortPm1DayIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalIndex.setStatus("current")
_GBondPortPm1DayIntervalMoniTime_Type = HCPerfTimeElapsed
_GBondPortPm1DayIntervalMoniTime_Object = MibTableColumn
gBondPortPm1DayIntervalMoniTime = _GBondPortPm1DayIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1, 2),
    _GBondPortPm1DayIntervalMoniTime_Type()
)
gBondPortPm1DayIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalMoniTime.setUnits("seconds")
_GBondPortPm1DayIntervalES_Type = HCPerfIntervalCount
_GBondPortPm1DayIntervalES_Object = MibTableColumn
gBondPortPm1DayIntervalES = _GBondPortPm1DayIntervalES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1, 3),
    _GBondPortPm1DayIntervalES_Type()
)
gBondPortPm1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalES.setUnits("seconds")
_GBondPortPm1DayIntervalSES_Type = HCPerfIntervalCount
_GBondPortPm1DayIntervalSES_Object = MibTableColumn
gBondPortPm1DayIntervalSES = _GBondPortPm1DayIntervalSES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1, 4),
    _GBondPortPm1DayIntervalSES_Type()
)
gBondPortPm1DayIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalSES.setUnits("seconds")
_GBondPortPm1DayIntervalUAS_Type = HCPerfIntervalCount
_GBondPortPm1DayIntervalUAS_Object = MibTableColumn
gBondPortPm1DayIntervalUAS = _GBondPortPm1DayIntervalUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1, 5),
    _GBondPortPm1DayIntervalUAS_Type()
)
gBondPortPm1DayIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalUAS.setUnits("seconds")
_GBondPortPm1DayIntervalValid_Type = TruthValue
_GBondPortPm1DayIntervalValid_Object = MibTableColumn
gBondPortPm1DayIntervalValid = _GBondPortPm1DayIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 3, 1, 6),
    _GBondPortPm1DayIntervalValid_Type()
)
gBondPortPm1DayIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondPortPm1DayIntervalValid.setStatus("current")
_GBondPortPmTcaProfileTable_Object = MibTable
gBondPortPmTcaProfileTable = _GBondPortPmTcaProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileTable.setStatus("current")
_GBondPortPmTcaProfileEntry_Object = MibTableRow
gBondPortPmTcaProfileEntry = _GBondPortPmTcaProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1)
)
gBondPortPmTcaProfileEntry.setIndexNames(
    (0, "GBOND-MIB", "gBondPortPmTcaProfileName"),
)
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileEntry.setStatus("current")


class _GBondPortPmTcaProfileName_Type(SnmpAdminString):
    """Custom type gBondPortPmTcaProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GBondPortPmTcaProfileName_Type.__name__ = "SnmpAdminString"
_GBondPortPmTcaProfileName_Object = MibTableColumn
gBondPortPmTcaProfileName = _GBondPortPmTcaProfileName_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 1),
    _GBondPortPmTcaProfileName_Type()
)
gBondPortPmTcaProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileName.setStatus("current")
_GBondPortPmTcaProfileThresh15MinES_Type = HCPerfIntervalThreshold
_GBondPortPmTcaProfileThresh15MinES_Object = MibTableColumn
gBondPortPmTcaProfileThresh15MinES = _GBondPortPmTcaProfileThresh15MinES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 2),
    _GBondPortPmTcaProfileThresh15MinES_Type()
)
gBondPortPmTcaProfileThresh15MinES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh15MinES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh15MinES.setUnits("seconds")
_GBondPortPmTcaProfileThresh15MinSES_Type = HCPerfIntervalThreshold
_GBondPortPmTcaProfileThresh15MinSES_Object = MibTableColumn
gBondPortPmTcaProfileThresh15MinSES = _GBondPortPmTcaProfileThresh15MinSES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 3),
    _GBondPortPmTcaProfileThresh15MinSES_Type()
)
gBondPortPmTcaProfileThresh15MinSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh15MinSES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh15MinSES.setUnits("seconds")
_GBondPortPmTcaProfileThresh15MinUAS_Type = HCPerfIntervalThreshold
_GBondPortPmTcaProfileThresh15MinUAS_Object = MibTableColumn
gBondPortPmTcaProfileThresh15MinUAS = _GBondPortPmTcaProfileThresh15MinUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 4),
    _GBondPortPmTcaProfileThresh15MinUAS_Type()
)
gBondPortPmTcaProfileThresh15MinUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh15MinUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh15MinUAS.setUnits("seconds")
_GBondPortPmTcaProfileThresh1DayES_Type = GBondPm1DayIntervalThreshold
_GBondPortPmTcaProfileThresh1DayES_Object = MibTableColumn
gBondPortPmTcaProfileThresh1DayES = _GBondPortPmTcaProfileThresh1DayES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 5),
    _GBondPortPmTcaProfileThresh1DayES_Type()
)
gBondPortPmTcaProfileThresh1DayES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh1DayES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh1DayES.setUnits("seconds")
_GBondPortPmTcaProfileThresh1DaySES_Type = GBondPm1DayIntervalThreshold
_GBondPortPmTcaProfileThresh1DaySES_Object = MibTableColumn
gBondPortPmTcaProfileThresh1DaySES = _GBondPortPmTcaProfileThresh1DaySES_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 6),
    _GBondPortPmTcaProfileThresh1DaySES_Type()
)
gBondPortPmTcaProfileThresh1DaySES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh1DaySES.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh1DaySES.setUnits("seconds")
_GBondPortPmTcaProfileThresh1DayUAS_Type = GBondPm1DayIntervalThreshold
_GBondPortPmTcaProfileThresh1DayUAS_Object = MibTableColumn
gBondPortPmTcaProfileThresh1DayUAS = _GBondPortPmTcaProfileThresh1DayUAS_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 7),
    _GBondPortPmTcaProfileThresh1DayUAS_Type()
)
gBondPortPmTcaProfileThresh1DayUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh1DayUAS.setStatus("current")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileThresh1DayUAS.setUnits("seconds")
_GBondPortPmTcaProfileRowStatus_Type = RowStatus
_GBondPortPmTcaProfileRowStatus_Object = MibTableColumn
gBondPortPmTcaProfileRowStatus = _GBondPortPmTcaProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 4, 4, 1, 8),
    _GBondPortPmTcaProfileRowStatus_Type()
)
gBondPortPmTcaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gBondPortPmTcaProfileRowStatus.setStatus("current")
_GBondBce_ObjectIdentity = ObjectIdentity
gBondBce = _GBondBce_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 2)
)
_GBondBceConfTable_Object = MibTable
gBondBceConfTable = _GBondBceConfTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gBondBceConfTable.setStatus("current")
_GBondBceConfEntry_Object = MibTableRow
gBondBceConfEntry = _GBondBceConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 1, 1)
)
gBondBceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondBceConfEntry.setStatus("current")


class _GBondBceConfRemoteDiscoveryCode_Type(PhysAddress):
    """Custom type gBondBceConfRemoteDiscoveryCode based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_GBondBceConfRemoteDiscoveryCode_Type.__name__ = "PhysAddress"
_GBondBceConfRemoteDiscoveryCode_Object = MibTableColumn
gBondBceConfRemoteDiscoveryCode = _GBondBceConfRemoteDiscoveryCode_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 1, 1, 1),
    _GBondBceConfRemoteDiscoveryCode_Type()
)
gBondBceConfRemoteDiscoveryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondBceConfRemoteDiscoveryCode.setStatus("current")
_GBondConformance_ObjectIdentity = ObjectIdentity
gBondConformance = _GBondConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2)
)
_GBondGroups_ObjectIdentity = ObjectIdentity
gBondGroups = _GBondGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 1)
)
_GBondCompliances_ObjectIdentity = ObjectIdentity
gBondCompliances = _GBondCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 2)
)

# Managed Objects groups

gBondBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1)
)
gBondBasicGroup.setObjects(
      *(("GBOND-MIB", "gBondPortStatOperScheme"),
        ("GBOND-MIB", "gBondPortStatUpDataRate"),
        ("GBOND-MIB", "gBondPortStatDnDataRate"),
        ("GBOND-MIB", "gBondPortConfTargetUpDataRate"),
        ("GBOND-MIB", "gBondPortConfTargetDnDataRate"),
        ("GBOND-MIB", "gBondPortCapSchemesSupported"),
        ("GBOND-MIB", "gBondPortCapCapacity"),
        ("GBOND-MIB", "gBondPortStatNumBCEs"),
        ("GBOND-MIB", "gBondPortStatSide"),
        ("GBOND-MIB", "gBondPortStatFltStatus"))
)
if mibBuilder.loadTexts:
    gBondBasicGroup.setStatus("current")

gBondDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 2)
)
gBondDiscoveryGroup.setObjects(
      *(("GBOND-MIB", "gBondPortStatPeerOperScheme"),
        ("GBOND-MIB", "gBondPortCapPeerSchemesSupported"),
        ("GBOND-MIB", "gBondPortCapPeerCapacity"),
        ("GBOND-MIB", "gBondPortConfDiscoveryCode"),
        ("GBOND-MIB", "gBondBceConfRemoteDiscoveryCode"))
)
if mibBuilder.loadTexts:
    gBondDiscoveryGroup.setStatus("current")

gBondMultiSchemeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 3)
)
gBondMultiSchemeGroup.setObjects(
      *(("GBOND-MIB", "gBondPortConfAdminScheme"),
        ("GBOND-MIB", "gBondPortConfPeerAdminScheme"))
)
if mibBuilder.loadTexts:
    gBondMultiSchemeGroup.setStatus("current")

gBondTcaConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 4)
)
gBondTcaConfGroup.setObjects(
      *(("GBOND-MIB", "gBondPortConfThreshLowUpRate"),
        ("GBOND-MIB", "gBondPortConfThreshLowDnRate"),
        ("GBOND-MIB", "gBondPortConfLowRateCrossingEnable"))
)
if mibBuilder.loadTexts:
    gBondTcaConfGroup.setStatus("current")

gBondPmCurGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 6)
)
gBondPmCurGroup.setObjects(
      *(("GBOND-MIB", "gBondPortPmCurES"),
        ("GBOND-MIB", "gBondPortPmCurSES"),
        ("GBOND-MIB", "gBondPortPmCurUAS"),
        ("GBOND-MIB", "gBondPortPmCur15MinValidIntervals"),
        ("GBOND-MIB", "gBondPortPmCur15MinInvalidIntervals"),
        ("GBOND-MIB", "gBondPortPmCur15MinTimeElapsed"),
        ("GBOND-MIB", "gBondPortPmCur15MinES"),
        ("GBOND-MIB", "gBondPortPmCur15MinSES"),
        ("GBOND-MIB", "gBondPortPmCur15MinUAS"),
        ("GBOND-MIB", "gBondPortPmCur1DayValidIntervals"),
        ("GBOND-MIB", "gBondPortPmCur1DayInvalidIntervals"),
        ("GBOND-MIB", "gBondPortPmCur1DayTimeElapsed"),
        ("GBOND-MIB", "gBondPortPmCur1DayES"),
        ("GBOND-MIB", "gBondPortPmCur1DaySES"),
        ("GBOND-MIB", "gBondPortPmCur1DayUAS"))
)
if mibBuilder.loadTexts:
    gBondPmCurGroup.setStatus("current")

gBondPm15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 7)
)
gBondPm15MinGroup.setObjects(
      *(("GBOND-MIB", "gBondPortPm15MinIntervalMoniTime"),
        ("GBOND-MIB", "gBondPortPm15MinIntervalES"),
        ("GBOND-MIB", "gBondPortPm15MinIntervalSES"),
        ("GBOND-MIB", "gBondPortPm15MinIntervalUAS"),
        ("GBOND-MIB", "gBondPortPm15MinIntervalValid"))
)
if mibBuilder.loadTexts:
    gBondPm15MinGroup.setStatus("current")

gBondPm1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 8)
)
gBondPm1DayGroup.setObjects(
      *(("GBOND-MIB", "gBondPortPm1DayIntervalMoniTime"),
        ("GBOND-MIB", "gBondPortPm1DayIntervalES"),
        ("GBOND-MIB", "gBondPortPm1DayIntervalSES"),
        ("GBOND-MIB", "gBondPortPm1DayIntervalUAS"),
        ("GBOND-MIB", "gBondPortPm1DayIntervalValid"))
)
if mibBuilder.loadTexts:
    gBondPm1DayGroup.setStatus("current")

gBondPmTcaConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 9)
)
gBondPmTcaConfGroup.setObjects(
      *(("GBOND-MIB", "gBondPortConfPmTcaConfProfile"),
        ("GBOND-MIB", "gBondPortConfPmTcaEnable"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh15MinES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh15MinSES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh15MinUAS"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh1DayES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh1DaySES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh1DayUAS"),
        ("GBOND-MIB", "gBondPortPmTcaProfileRowStatus"))
)
if mibBuilder.loadTexts:
    gBondPmTcaConfGroup.setStatus("current")


# Notification objects

gBondLowUpRateCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 1)
)
gBondLowUpRateCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortStatUpDataRate"),
        ("GBOND-MIB", "gBondPortConfThreshLowUpRate"))
)
if mibBuilder.loadTexts:
    gBondLowUpRateCrossing.setStatus(
        "current"
    )

gBondLowDnRateCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 2)
)
gBondLowDnRateCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortStatDnDataRate"),
        ("GBOND-MIB", "gBondPortConfThreshLowDnRate"))
)
if mibBuilder.loadTexts:
    gBondLowDnRateCrossing.setStatus(
        "current"
    )

gBondPmTca15MinESCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 3)
)
gBondPmTca15MinESCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortPmCur15MinES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh15MinES"))
)
if mibBuilder.loadTexts:
    gBondPmTca15MinESCrossing.setStatus(
        "current"
    )

gBondPmTca15MinSESCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 4)
)
gBondPmTca15MinSESCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortPmCur15MinSES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh15MinSES"))
)
if mibBuilder.loadTexts:
    gBondPmTca15MinSESCrossing.setStatus(
        "current"
    )

gBondPmTca15MinUASCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 5)
)
gBondPmTca15MinUASCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortPmCur15MinUAS"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh15MinUAS"))
)
if mibBuilder.loadTexts:
    gBondPmTca15MinUASCrossing.setStatus(
        "current"
    )

gBondPmTca1DayESCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 6)
)
gBondPmTca1DayESCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortPmCur1DayES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh1DayES"))
)
if mibBuilder.loadTexts:
    gBondPmTca1DayESCrossing.setStatus(
        "current"
    )

gBondPmTca1DaySESCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 7)
)
gBondPmTca1DaySESCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortPmCur1DaySES"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh1DaySES"))
)
if mibBuilder.loadTexts:
    gBondPmTca1DaySESCrossing.setStatus(
        "current"
    )

gBondPmTca1DayUASCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 0, 8)
)
gBondPmTca1DayUASCrossing.setObjects(
      *(("GBOND-MIB", "gBondPortPmCur1DayUAS"),
        ("GBOND-MIB", "gBondPortPmTcaProfileThresh1DayUAS"))
)
if mibBuilder.loadTexts:
    gBondPmTca1DayUASCrossing.setStatus(
        "current"
    )


# Notifications groups

gBondTcaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 5)
)
gBondTcaNotificationGroup.setObjects(
      *(("GBOND-MIB", "gBondLowUpRateCrossing"),
        ("GBOND-MIB", "gBondLowDnRateCrossing"))
)
if mibBuilder.loadTexts:
    gBondTcaNotificationGroup.setStatus(
        "current"
    )

gBondPmTcaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 10)
)
gBondPmTcaNotificationGroup.setObjects(
      *(("GBOND-MIB", "gBondPmTca15MinESCrossing"),
        ("GBOND-MIB", "gBondPmTca15MinSESCrossing"),
        ("GBOND-MIB", "gBondPmTca15MinUASCrossing"),
        ("GBOND-MIB", "gBondPmTca1DayESCrossing"),
        ("GBOND-MIB", "gBondPmTca1DaySESCrossing"),
        ("GBOND-MIB", "gBondPmTca1DayUASCrossing"))
)
if mibBuilder.loadTexts:
    gBondPmTcaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gBondCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 211, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gBondCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBOND-MIB",
    **{"GBondPm1DayIntervalThreshold": GBondPm1DayIntervalThreshold,
       "gBondMIB": gBondMIB,
       "gBondObjects": gBondObjects,
       "gBondPort": gBondPort,
       "gBondPortNotifications": gBondPortNotifications,
       "gBondLowUpRateCrossing": gBondLowUpRateCrossing,
       "gBondLowDnRateCrossing": gBondLowDnRateCrossing,
       "gBondPmTca15MinESCrossing": gBondPmTca15MinESCrossing,
       "gBondPmTca15MinSESCrossing": gBondPmTca15MinSESCrossing,
       "gBondPmTca15MinUASCrossing": gBondPmTca15MinUASCrossing,
       "gBondPmTca1DayESCrossing": gBondPmTca1DayESCrossing,
       "gBondPmTca1DaySESCrossing": gBondPmTca1DaySESCrossing,
       "gBondPmTca1DayUASCrossing": gBondPmTca1DayUASCrossing,
       "gBondPortConfTable": gBondPortConfTable,
       "gBondPortConfEntry": gBondPortConfEntry,
       "gBondPortConfAdminScheme": gBondPortConfAdminScheme,
       "gBondPortConfPeerAdminScheme": gBondPortConfPeerAdminScheme,
       "gBondPortConfDiscoveryCode": gBondPortConfDiscoveryCode,
       "gBondPortConfTargetUpDataRate": gBondPortConfTargetUpDataRate,
       "gBondPortConfTargetDnDataRate": gBondPortConfTargetDnDataRate,
       "gBondPortConfThreshLowUpRate": gBondPortConfThreshLowUpRate,
       "gBondPortConfThreshLowDnRate": gBondPortConfThreshLowDnRate,
       "gBondPortConfLowRateCrossingEnable": gBondPortConfLowRateCrossingEnable,
       "gBondPortConfPmTcaConfProfile": gBondPortConfPmTcaConfProfile,
       "gBondPortConfPmTcaEnable": gBondPortConfPmTcaEnable,
       "gBondPortCapTable": gBondPortCapTable,
       "gBondPortCapEntry": gBondPortCapEntry,
       "gBondPortCapSchemesSupported": gBondPortCapSchemesSupported,
       "gBondPortCapPeerSchemesSupported": gBondPortCapPeerSchemesSupported,
       "gBondPortCapCapacity": gBondPortCapCapacity,
       "gBondPortCapPeerCapacity": gBondPortCapPeerCapacity,
       "gBondPortStatTable": gBondPortStatTable,
       "gBondPortStatEntry": gBondPortStatEntry,
       "gBondPortStatOperScheme": gBondPortStatOperScheme,
       "gBondPortStatPeerOperScheme": gBondPortStatPeerOperScheme,
       "gBondPortStatUpDataRate": gBondPortStatUpDataRate,
       "gBondPortStatDnDataRate": gBondPortStatDnDataRate,
       "gBondPortStatFltStatus": gBondPortStatFltStatus,
       "gBondPortStatSide": gBondPortStatSide,
       "gBondPortStatNumBCEs": gBondPortStatNumBCEs,
       "gBondPortPM": gBondPortPM,
       "gBondPortPmCurTable": gBondPortPmCurTable,
       "gBondPortPmCurEntry": gBondPortPmCurEntry,
       "gBondPortPmCurES": gBondPortPmCurES,
       "gBondPortPmCurSES": gBondPortPmCurSES,
       "gBondPortPmCurUAS": gBondPortPmCurUAS,
       "gBondPortPmCur15MinValidIntervals": gBondPortPmCur15MinValidIntervals,
       "gBondPortPmCur15MinInvalidIntervals": gBondPortPmCur15MinInvalidIntervals,
       "gBondPortPmCur15MinTimeElapsed": gBondPortPmCur15MinTimeElapsed,
       "gBondPortPmCur15MinES": gBondPortPmCur15MinES,
       "gBondPortPmCur15MinSES": gBondPortPmCur15MinSES,
       "gBondPortPmCur15MinUAS": gBondPortPmCur15MinUAS,
       "gBondPortPmCur1DayValidIntervals": gBondPortPmCur1DayValidIntervals,
       "gBondPortPmCur1DayInvalidIntervals": gBondPortPmCur1DayInvalidIntervals,
       "gBondPortPmCur1DayTimeElapsed": gBondPortPmCur1DayTimeElapsed,
       "gBondPortPmCur1DayES": gBondPortPmCur1DayES,
       "gBondPortPmCur1DaySES": gBondPortPmCur1DaySES,
       "gBondPortPmCur1DayUAS": gBondPortPmCur1DayUAS,
       "gBondPortPm15MinTable": gBondPortPm15MinTable,
       "gBondPortPm15MinEntry": gBondPortPm15MinEntry,
       "gBondPortPm15MinIntervalIndex": gBondPortPm15MinIntervalIndex,
       "gBondPortPm15MinIntervalMoniTime": gBondPortPm15MinIntervalMoniTime,
       "gBondPortPm15MinIntervalES": gBondPortPm15MinIntervalES,
       "gBondPortPm15MinIntervalSES": gBondPortPm15MinIntervalSES,
       "gBondPortPm15MinIntervalUAS": gBondPortPm15MinIntervalUAS,
       "gBondPortPm15MinIntervalValid": gBondPortPm15MinIntervalValid,
       "gBondPortPm1DayTable": gBondPortPm1DayTable,
       "gBondPortPm1DayEntry": gBondPortPm1DayEntry,
       "gBondPortPm1DayIntervalIndex": gBondPortPm1DayIntervalIndex,
       "gBondPortPm1DayIntervalMoniTime": gBondPortPm1DayIntervalMoniTime,
       "gBondPortPm1DayIntervalES": gBondPortPm1DayIntervalES,
       "gBondPortPm1DayIntervalSES": gBondPortPm1DayIntervalSES,
       "gBondPortPm1DayIntervalUAS": gBondPortPm1DayIntervalUAS,
       "gBondPortPm1DayIntervalValid": gBondPortPm1DayIntervalValid,
       "gBondPortPmTcaProfileTable": gBondPortPmTcaProfileTable,
       "gBondPortPmTcaProfileEntry": gBondPortPmTcaProfileEntry,
       "gBondPortPmTcaProfileName": gBondPortPmTcaProfileName,
       "gBondPortPmTcaProfileThresh15MinES": gBondPortPmTcaProfileThresh15MinES,
       "gBondPortPmTcaProfileThresh15MinSES": gBondPortPmTcaProfileThresh15MinSES,
       "gBondPortPmTcaProfileThresh15MinUAS": gBondPortPmTcaProfileThresh15MinUAS,
       "gBondPortPmTcaProfileThresh1DayES": gBondPortPmTcaProfileThresh1DayES,
       "gBondPortPmTcaProfileThresh1DaySES": gBondPortPmTcaProfileThresh1DaySES,
       "gBondPortPmTcaProfileThresh1DayUAS": gBondPortPmTcaProfileThresh1DayUAS,
       "gBondPortPmTcaProfileRowStatus": gBondPortPmTcaProfileRowStatus,
       "gBondBce": gBondBce,
       "gBondBceConfTable": gBondBceConfTable,
       "gBondBceConfEntry": gBondBceConfEntry,
       "gBondBceConfRemoteDiscoveryCode": gBondBceConfRemoteDiscoveryCode,
       "gBondConformance": gBondConformance,
       "gBondGroups": gBondGroups,
       "gBondBasicGroup": gBondBasicGroup,
       "gBondDiscoveryGroup": gBondDiscoveryGroup,
       "gBondMultiSchemeGroup": gBondMultiSchemeGroup,
       "gBondTcaConfGroup": gBondTcaConfGroup,
       "gBondTcaNotificationGroup": gBondTcaNotificationGroup,
       "gBondPmCurGroup": gBondPmCurGroup,
       "gBondPm15MinGroup": gBondPm15MinGroup,
       "gBondPm1DayGroup": gBondPm1DayGroup,
       "gBondPmTcaConfGroup": gBondPmTcaConfGroup,
       "gBondPmTcaNotificationGroup": gBondPmTcaNotificationGroup,
       "gBondCompliances": gBondCompliances,
       "gBondCompliance": gBondCompliance}
)
