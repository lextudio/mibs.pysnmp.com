# SNMP MIB module (ZhoneGR303-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneGR303-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:20 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(PerfCurrentCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount")

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

(zhoneSystemConfigurationDateAndTime,) = mibBuilder.importSymbols(
    "ZHONE-SYSTEM-MIB",
    "zhoneSystemConfigurationDateAndTime")

(zhoneVoice,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneVoice")

(ZhoneAdminString,
 ZhoneRowStatus,
 ZhoneShelfValueOrZero,
 ZhoneSlotValueOrZero) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus",
    "ZhoneShelfValueOrZero",
    "ZhoneSlotValueOrZero")


# MODULE-IDENTITY

zhoneGR303 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1)
)
zhoneGR303.setRevisions(
        ("2003-12-23 11:09",
         "2003-11-14 13:10",
         "2001-11-15 10:45",
         "2001-08-31 12:30",
         "2001-08-14 14:47",
         "2001-06-26 15:00",
         "2001-03-28 10:55",
         "2001-02-15 18:47",
         "2001-02-01 13:01",
         "2001-01-26 11:48",
         "2000-12-12 11:57",
         "2000-09-12 12:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InterfaceGroupTable_Object = MibTable
interfaceGroupTable = _InterfaceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceGroupTable.setStatus("current")
_InterfaceGroupEntry_Object = MibTableRow
interfaceGroupEntry = _InterfaceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1)
)
interfaceGroupEntry.setIndexNames(
    (0, "ZhoneGR303-MIB", "igNameId"),
)
if mibBuilder.loadTexts:
    interfaceGroupEntry.setStatus("current")
_IgNameId_Type = ZhoneAdminString
_IgNameId_Object = MibTableColumn
igNameId = _IgNameId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 1),
    _IgNameId_Type()
)
igNameId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igNameId.setStatus("current")
_IgShelf_Type = ZhoneShelfValueOrZero
_IgShelf_Object = MibTableColumn
igShelf = _IgShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 2),
    _IgShelf_Type()
)
igShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igShelf.setStatus("current")
_IgSlot_Type = ZhoneSlotValueOrZero
_IgSlot_Object = MibTableColumn
igSlot = _IgSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 3),
    _IgSlot_Type()
)
igSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igSlot.setStatus("current")
_IgPeerShelf_Type = ZhoneShelfValueOrZero
_IgPeerShelf_Object = MibTableColumn
igPeerShelf = _IgPeerShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 4),
    _IgPeerShelf_Type()
)
igPeerShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igPeerShelf.setStatus("current")
_IgPeerSlot_Type = ZhoneSlotValueOrZero
_IgPeerSlot_Object = MibTableColumn
igPeerSlot = _IgPeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 5),
    _IgPeerSlot_Type()
)
igPeerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igPeerSlot.setStatus("current")


class _IgSwitchType_Type(Integer32):
    """Custom type igSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("lucent5Ess", 2),
          ("lucentGtd5", 4),
          ("nortelDms100", 3),
          ("santeraSanteraOne", 5),
          ("taquaIx7000", 7),
          ("telicaPlexus9000", 6))
    )


_IgSwitchType_Type.__name__ = "Integer32"
_IgSwitchType_Object = MibTableColumn
igSwitchType = _IgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 6),
    _IgSwitchType_Type()
)
igSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSwitchType.setStatus("current")
_IgPrimaryEocTmcDs1IfIndex_Type = InterfaceIndexOrZero
_IgPrimaryEocTmcDs1IfIndex_Object = MibTableColumn
igPrimaryEocTmcDs1IfIndex = _IgPrimaryEocTmcDs1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 7),
    _IgPrimaryEocTmcDs1IfIndex_Type()
)
igPrimaryEocTmcDs1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igPrimaryEocTmcDs1IfIndex.setStatus("current")
_IgSecondaryEocTmcDs1IfIndex_Type = InterfaceIndexOrZero
_IgSecondaryEocTmcDs1IfIndex_Object = MibTableColumn
igSecondaryEocTmcDs1IfIndex = _IgSecondaryEocTmcDs1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 8),
    _IgSecondaryEocTmcDs1IfIndex_Type()
)
igSecondaryEocTmcDs1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igSecondaryEocTmcDs1IfIndex.setStatus("current")


class _IgAdminStatus_Type(Integer32):
    """Custom type igAdminStatus based on Integer32"""
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


_IgAdminStatus_Type.__name__ = "Integer32"
_IgAdminStatus_Object = MibTableColumn
igAdminStatus = _IgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 9),
    _IgAdminStatus_Type()
)
igAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igAdminStatus.setStatus("current")


class _IgOperationalStatus_Type(Integer32):
    """Custom type igOperationalStatus based on Integer32"""
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
        *(("inoperable", 2),
          ("inoperableIsInProgress", 4),
          ("inoperableOosInProgress", 5),
          ("operable", 1),
          ("standby", 3))
    )


_IgOperationalStatus_Type.__name__ = "Integer32"
_IgOperationalStatus_Object = MibTableColumn
igOperationalStatus = _IgOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 10),
    _IgOperationalStatus_Type()
)
igOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igOperationalStatus.setStatus("current")


class _IgPeerStatus_Type(Integer32):
    """Custom type igPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configuredAndAvailable", 2),
          ("configuredAndUnavailable", 3),
          ("noStandbyConfigured", 1))
    )


_IgPeerStatus_Type.__name__ = "Integer32"
_IgPeerStatus_Object = MibTableColumn
igPeerStatus = _IgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 11),
    _IgPeerStatus_Type()
)
igPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igPeerStatus.setStatus("current")


class _IgMaxConfigCalls_Type(Gauge32):
    """Custom type igMaxConfigCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 670),
    )


_IgMaxConfigCalls_Type.__name__ = "Gauge32"
_IgMaxConfigCalls_Object = MibTableColumn
igMaxConfigCalls = _IgMaxConfigCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 12),
    _IgMaxConfigCalls_Type()
)
igMaxConfigCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igMaxConfigCalls.setStatus("current")
if mibBuilder.loadTexts:
    igMaxConfigCalls.setUnits("calls")


class _IgCurrActiveCalls_Type(Gauge32):
    """Custom type igCurrActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 670),
    )


_IgCurrActiveCalls_Type.__name__ = "Gauge32"
_IgCurrActiveCalls_Object = MibTableColumn
igCurrActiveCalls = _IgCurrActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 13),
    _IgCurrActiveCalls_Type()
)
igCurrActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    igCurrActiveCalls.setUnits("calls")


class _IgStatsTimeElapsed_Type(Integer32):
    """Custom type igStatsTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_IgStatsTimeElapsed_Type.__name__ = "Integer32"
_IgStatsTimeElapsed_Object = MibTableColumn
igStatsTimeElapsed = _IgStatsTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 14),
    _IgStatsTimeElapsed_Type()
)
igStatsTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igStatsTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    igStatsTimeElapsed.setUnits("seconds")


class _IgStatsValidIntervals_Type(Integer32):
    """Custom type igStatsValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_IgStatsValidIntervals_Type.__name__ = "Integer32"
_IgStatsValidIntervals_Object = MibTableColumn
igStatsValidIntervals = _IgStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 15),
    _IgStatsValidIntervals_Type()
)
igStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igStatsValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    igStatsValidIntervals.setUnits("intervals")


class _IgStatsInvalidIntervals_Type(Integer32):
    """Custom type igStatsInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_IgStatsInvalidIntervals_Type.__name__ = "Integer32"
_IgStatsInvalidIntervals_Object = MibTableColumn
igStatsInvalidIntervals = _IgStatsInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 16),
    _IgStatsInvalidIntervals_Type()
)
igStatsInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igStatsInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    igStatsInvalidIntervals.setUnits("intervals")
_IgRowStatus_Type = ZhoneRowStatus
_IgRowStatus_Object = MibTableColumn
igRowStatus = _IgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 17),
    _IgRowStatus_Type()
)
igRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igRowStatus.setStatus("current")


class _IgWorkingMode_Type(Integer32):
    """Custom type igWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_IgWorkingMode_Type.__name__ = "Integer32"
_IgWorkingMode_Object = MibTableColumn
igWorkingMode = _IgWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 18),
    _IgWorkingMode_Type()
)
igWorkingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igWorkingMode.setStatus("current")
_IgControlChannelTable_Object = MibTable
igControlChannelTable = _IgControlChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    igControlChannelTable.setStatus("current")
_IgControlChannelEntry_Object = MibTableRow
igControlChannelEntry = _IgControlChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    igControlChannelEntry.setStatus("current")


class _IgControlChannelTmcPrimarySvcState_Type(Integer32):
    """Custom type igControlChannelTmcPrimarySvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("outOfService", 3),
          ("standby", 2))
    )


_IgControlChannelTmcPrimarySvcState_Type.__name__ = "Integer32"
_IgControlChannelTmcPrimarySvcState_Object = MibTableColumn
igControlChannelTmcPrimarySvcState = _IgControlChannelTmcPrimarySvcState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 1),
    _IgControlChannelTmcPrimarySvcState_Type()
)
igControlChannelTmcPrimarySvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igControlChannelTmcPrimarySvcState.setStatus("current")


class _IgControlChannelTmcSecondarySvcState_Type(Integer32):
    """Custom type igControlChannelTmcSecondarySvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("outOfService", 3),
          ("standby", 2))
    )


_IgControlChannelTmcSecondarySvcState_Type.__name__ = "Integer32"
_IgControlChannelTmcSecondarySvcState_Object = MibTableColumn
igControlChannelTmcSecondarySvcState = _IgControlChannelTmcSecondarySvcState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 2),
    _IgControlChannelTmcSecondarySvcState_Type()
)
igControlChannelTmcSecondarySvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igControlChannelTmcSecondarySvcState.setStatus("current")


class _IgControlChannelT303_Type(Integer32):
    """Custom type igControlChannelT303 based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 700),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(1700, 1700),
        ValueRangeConstraint(2200, 2200),
        ValueRangeConstraint(2700, 2700),
        ValueRangeConstraint(3200, 3200),
        ValueRangeConstraint(3700, 3700),
        ValueRangeConstraint(4200, 4200),
        ValueRangeConstraint(4700, 4700),
    )


_IgControlChannelT303_Type.__name__ = "Integer32"
_IgControlChannelT303_Object = MibTableColumn
igControlChannelT303 = _IgControlChannelT303_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 3),
    _IgControlChannelT303_Type()
)
igControlChannelT303.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igControlChannelT303.setStatus("current")
if mibBuilder.loadTexts:
    igControlChannelT303.setUnits("milliseconds")


class _IgControlChannelT396_Type(Integer32):
    """Custom type igControlChannelT396 based on Integer32"""
    defaultValue = 14700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 700),
        ValueRangeConstraint(1700, 1700),
        ValueRangeConstraint(2700, 2700),
        ValueRangeConstraint(3700, 3700),
        ValueRangeConstraint(4700, 4700),
        ValueRangeConstraint(5700, 5700),
        ValueRangeConstraint(6700, 6700),
        ValueRangeConstraint(7700, 7700),
        ValueRangeConstraint(8700, 8700),
        ValueRangeConstraint(9700, 9700),
        ValueRangeConstraint(10700, 10700),
        ValueRangeConstraint(11700, 11700),
        ValueRangeConstraint(12700, 12700),
        ValueRangeConstraint(13700, 13700),
        ValueRangeConstraint(14700, 14700),
    )


_IgControlChannelT396_Type.__name__ = "Integer32"
_IgControlChannelT396_Object = MibTableColumn
igControlChannelT396 = _IgControlChannelT396_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 4),
    _IgControlChannelT396_Type()
)
igControlChannelT396.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igControlChannelT396.setStatus("current")
if mibBuilder.loadTexts:
    igControlChannelT396.setUnits("milliseconds")


class _IgSapi0MaxOutstandingFrames_Type(Integer32):
    """Custom type igSapi0MaxOutstandingFrames based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IgSapi0MaxOutstandingFrames_Type.__name__ = "Integer32"
_IgSapi0MaxOutstandingFrames_Object = MibTableColumn
igSapi0MaxOutstandingFrames = _IgSapi0MaxOutstandingFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 5),
    _IgSapi0MaxOutstandingFrames_Type()
)
igSapi0MaxOutstandingFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi0MaxOutstandingFrames.setStatus("current")
if mibBuilder.loadTexts:
    igSapi0MaxOutstandingFrames.setUnits("frames")


class _IgSapi0N200_Type(Integer32):
    """Custom type igSapi0N200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IgSapi0N200_Type.__name__ = "Integer32"
_IgSapi0N200_Object = MibTableColumn
igSapi0N200 = _IgSapi0N200_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 6),
    _IgSapi0N200_Type()
)
igSapi0N200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi0N200.setStatus("current")


class _IgSapi0T200_Type(Integer32):
    """Custom type igSapi0T200 based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(350, 350),
    )


_IgSapi0T200_Type.__name__ = "Integer32"
_IgSapi0T200_Object = MibTableColumn
igSapi0T200 = _IgSapi0T200_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 7),
    _IgSapi0T200_Type()
)
igSapi0T200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi0T200.setStatus("current")
if mibBuilder.loadTexts:
    igSapi0T200.setUnits("milliseconds")


class _IgSapi0T203_Type(Integer32):
    """Custom type igSapi0T203 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(110, 110),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(130, 130),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(170, 170),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(190, 190),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(210, 210),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(230, 230),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(260, 260),
        ValueRangeConstraint(270, 270),
        ValueRangeConstraint(280, 280),
        ValueRangeConstraint(290, 290),
        ValueRangeConstraint(300, 300),
    )


_IgSapi0T203_Type.__name__ = "Integer32"
_IgSapi0T203_Object = MibTableColumn
igSapi0T203 = _IgSapi0T203_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 8),
    _IgSapi0T203_Type()
)
igSapi0T203.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi0T203.setStatus("current")
if mibBuilder.loadTexts:
    igSapi0T203.setUnits("seconds")


class _IgSapi0PpsMode_Type(Integer32):
    """Custom type igSapi0PpsMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("notApplicable", 3),
          ("notInhibited", 2))
    )


_IgSapi0PpsMode_Type.__name__ = "Integer32"
_IgSapi0PpsMode_Object = MibTableColumn
igSapi0PpsMode = _IgSapi0PpsMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 9),
    _IgSapi0PpsMode_Type()
)
igSapi0PpsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi0PpsMode.setStatus("current")


class _IgSapi1MaxOutstandingFrames_Type(Integer32):
    """Custom type igSapi1MaxOutstandingFrames based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IgSapi1MaxOutstandingFrames_Type.__name__ = "Integer32"
_IgSapi1MaxOutstandingFrames_Object = MibTableColumn
igSapi1MaxOutstandingFrames = _IgSapi1MaxOutstandingFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 10),
    _IgSapi1MaxOutstandingFrames_Type()
)
igSapi1MaxOutstandingFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi1MaxOutstandingFrames.setStatus("current")
if mibBuilder.loadTexts:
    igSapi1MaxOutstandingFrames.setUnits("frames")


class _IgSapi1N200_Type(Integer32):
    """Custom type igSapi1N200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IgSapi1N200_Type.__name__ = "Integer32"
_IgSapi1N200_Object = MibTableColumn
igSapi1N200 = _IgSapi1N200_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 11),
    _IgSapi1N200_Type()
)
igSapi1N200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi1N200.setStatus("current")


class _IgSapi1T200_Type(Integer32):
    """Custom type igSapi1T200 based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(350, 350),
    )


_IgSapi1T200_Type.__name__ = "Integer32"
_IgSapi1T200_Object = MibTableColumn
igSapi1T200 = _IgSapi1T200_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 12),
    _IgSapi1T200_Type()
)
igSapi1T200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi1T200.setStatus("current")
if mibBuilder.loadTexts:
    igSapi1T200.setUnits("milliseconds")


class _IgSapi1T203_Type(Integer32):
    """Custom type igSapi1T203 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(110, 110),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(130, 130),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(170, 170),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(190, 190),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(210, 210),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(230, 230),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(260, 260),
        ValueRangeConstraint(270, 270),
        ValueRangeConstraint(280, 280),
        ValueRangeConstraint(290, 290),
        ValueRangeConstraint(300, 300),
    )


_IgSapi1T203_Type.__name__ = "Integer32"
_IgSapi1T203_Object = MibTableColumn
igSapi1T203 = _IgSapi1T203_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 13),
    _IgSapi1T203_Type()
)
igSapi1T203.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi1T203.setStatus("current")
if mibBuilder.loadTexts:
    igSapi1T203.setUnits("seconds")


class _IgSapi1PpsMode_Type(Integer32):
    """Custom type igSapi1PpsMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("notApplicable", 3),
          ("notInhibited", 2))
    )


_IgSapi1PpsMode_Type.__name__ = "Integer32"
_IgSapi1PpsMode_Object = MibTableColumn
igSapi1PpsMode = _IgSapi1PpsMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 14),
    _IgSapi1PpsMode_Type()
)
igSapi1PpsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igSapi1PpsMode.setStatus("current")


class _IgControlChannelEocPrimarySvcState_Type(Integer32):
    """Custom type igControlChannelEocPrimarySvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("outOfService", 3),
          ("standby", 2))
    )


_IgControlChannelEocPrimarySvcState_Type.__name__ = "Integer32"
_IgControlChannelEocPrimarySvcState_Object = MibTableColumn
igControlChannelEocPrimarySvcState = _IgControlChannelEocPrimarySvcState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 15),
    _IgControlChannelEocPrimarySvcState_Type()
)
igControlChannelEocPrimarySvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igControlChannelEocPrimarySvcState.setStatus("current")


class _IgControlChannelEocSecondarySvcState_Type(Integer32):
    """Custom type igControlChannelEocSecondarySvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("outOfService", 3),
          ("standby", 2))
    )


_IgControlChannelEocSecondarySvcState_Type.__name__ = "Integer32"
_IgControlChannelEocSecondarySvcState_Object = MibTableColumn
igControlChannelEocSecondarySvcState = _IgControlChannelEocSecondarySvcState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 17),
    _IgControlChannelEocSecondarySvcState_Type()
)
igControlChannelEocSecondarySvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igControlChannelEocSecondarySvcState.setStatus("current")
_IgStatsCurrentTable_Object = MibTable
igStatsCurrentTable = _IgStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    igStatsCurrentTable.setStatus("current")
_IgStatsCurrentEntry_Object = MibTableRow
igStatsCurrentEntry = _IgStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    igStatsCurrentEntry.setStatus("current")
_IgCurrentOutboundCalls_Type = PerfCurrentCount
_IgCurrentOutboundCalls_Object = MibTableColumn
igCurrentOutboundCalls = _IgCurrentOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 1),
    _IgCurrentOutboundCalls_Type()
)
igCurrentOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentOutboundCalls.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentOutboundCalls.setUnits("calls")
_IgCurrentInboundCalls_Type = PerfCurrentCount
_IgCurrentInboundCalls_Object = MibTableColumn
igCurrentInboundCalls = _IgCurrentInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 2),
    _IgCurrentInboundCalls_Type()
)
igCurrentInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentInboundCalls.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentInboundCalls.setUnits("calls")
_IgCurrentOutboundCallsBlocked_Type = PerfCurrentCount
_IgCurrentOutboundCallsBlocked_Object = MibTableColumn
igCurrentOutboundCallsBlocked = _IgCurrentOutboundCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 3),
    _IgCurrentOutboundCallsBlocked_Type()
)
igCurrentOutboundCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentOutboundCallsBlocked.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentOutboundCallsBlocked.setUnits("calls")
_IgCurrentGR303ProtocolErrors_Type = PerfCurrentCount
_IgCurrentGR303ProtocolErrors_Object = MibTableColumn
igCurrentGR303ProtocolErrors = _IgCurrentGR303ProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 4),
    _IgCurrentGR303ProtocolErrors_Type()
)
igCurrentGR303ProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentGR303ProtocolErrors.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentGR303ProtocolErrors.setUnits("errors")
_IgCurrentTMCLapdSent_Type = PerfCurrentCount
_IgCurrentTMCLapdSent_Object = MibTableColumn
igCurrentTMCLapdSent = _IgCurrentTMCLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 5),
    _IgCurrentTMCLapdSent_Type()
)
igCurrentTMCLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentTMCLapdSent.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentTMCLapdSent.setUnits("frames")
_IgCurrentTMCLapdRcvd_Type = PerfCurrentCount
_IgCurrentTMCLapdRcvd_Object = MibTableColumn
igCurrentTMCLapdRcvd = _IgCurrentTMCLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 6),
    _IgCurrentTMCLapdRcvd_Type()
)
igCurrentTMCLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentTMCLapdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentTMCLapdRcvd.setUnits("frames")
_IgCurrentTMCLapdRcvdErrs_Type = PerfCurrentCount
_IgCurrentTMCLapdRcvdErrs_Object = MibTableColumn
igCurrentTMCLapdRcvdErrs = _IgCurrentTMCLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 7),
    _IgCurrentTMCLapdRcvdErrs_Type()
)
igCurrentTMCLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentTMCLapdRcvdErrs.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentTMCLapdRcvdErrs.setUnits("frames")
_IgCurrentEOCLapdSent_Type = PerfCurrentCount
_IgCurrentEOCLapdSent_Object = MibTableColumn
igCurrentEOCLapdSent = _IgCurrentEOCLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 8),
    _IgCurrentEOCLapdSent_Type()
)
igCurrentEOCLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentEOCLapdSent.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentEOCLapdSent.setUnits("frames")
_IgCurrentEOCLapdRcvd_Type = PerfCurrentCount
_IgCurrentEOCLapdRcvd_Object = MibTableColumn
igCurrentEOCLapdRcvd = _IgCurrentEOCLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 9),
    _IgCurrentEOCLapdRcvd_Type()
)
igCurrentEOCLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentEOCLapdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentEOCLapdRcvd.setUnits("frames")
_IgCurrentEOCLapdRcvdErrs_Type = PerfCurrentCount
_IgCurrentEOCLapdRcvdErrs_Object = MibTableColumn
igCurrentEOCLapdRcvdErrs = _IgCurrentEOCLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 10),
    _IgCurrentEOCLapdRcvdErrs_Type()
)
igCurrentEOCLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCurrentEOCLapdRcvdErrs.setStatus("current")
if mibBuilder.loadTexts:
    igCurrentEOCLapdRcvdErrs.setUnits("frames")
_IgStatsIntervalTable_Object = MibTable
igStatsIntervalTable = _IgStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4)
)
if mibBuilder.loadTexts:
    igStatsIntervalTable.setStatus("current")
_IgStatsIntervalEntry_Object = MibTableRow
igStatsIntervalEntry = _IgStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1)
)
igStatsIntervalEntry.setIndexNames(
    (0, "ZhoneGR303-MIB", "igNameId"),
    (0, "ZhoneGR303-MIB", "igIntervalNumber"),
)
if mibBuilder.loadTexts:
    igStatsIntervalEntry.setStatus("current")


class _IgIntervalNumber_Type(Integer32):
    """Custom type igIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IgIntervalNumber_Type.__name__ = "Integer32"
_IgIntervalNumber_Object = MibTableColumn
igIntervalNumber = _IgIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 1),
    _IgIntervalNumber_Type()
)
igIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igIntervalNumber.setStatus("current")
_IgIntervalOutboundCalls_Type = PerfCurrentCount
_IgIntervalOutboundCalls_Object = MibTableColumn
igIntervalOutboundCalls = _IgIntervalOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 2),
    _IgIntervalOutboundCalls_Type()
)
igIntervalOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalOutboundCalls.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalOutboundCalls.setUnits("calls")
_IgIntervalInboundCalls_Type = PerfCurrentCount
_IgIntervalInboundCalls_Object = MibTableColumn
igIntervalInboundCalls = _IgIntervalInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 3),
    _IgIntervalInboundCalls_Type()
)
igIntervalInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalInboundCalls.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalInboundCalls.setUnits("calls")
_IgIntervalOutboundCallsBlocked_Type = PerfCurrentCount
_IgIntervalOutboundCallsBlocked_Object = MibTableColumn
igIntervalOutboundCallsBlocked = _IgIntervalOutboundCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 4),
    _IgIntervalOutboundCallsBlocked_Type()
)
igIntervalOutboundCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalOutboundCallsBlocked.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalOutboundCallsBlocked.setUnits("calls")
_IgIntervalGR303ProtocolErrors_Type = PerfCurrentCount
_IgIntervalGR303ProtocolErrors_Object = MibTableColumn
igIntervalGR303ProtocolErrors = _IgIntervalGR303ProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 5),
    _IgIntervalGR303ProtocolErrors_Type()
)
igIntervalGR303ProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalGR303ProtocolErrors.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalGR303ProtocolErrors.setUnits("errors")
_IgIntervalTMCLapdSent_Type = PerfCurrentCount
_IgIntervalTMCLapdSent_Object = MibTableColumn
igIntervalTMCLapdSent = _IgIntervalTMCLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 6),
    _IgIntervalTMCLapdSent_Type()
)
igIntervalTMCLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalTMCLapdSent.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalTMCLapdSent.setUnits("frames")
_IgIntervalTMCLapdRcvd_Type = PerfCurrentCount
_IgIntervalTMCLapdRcvd_Object = MibTableColumn
igIntervalTMCLapdRcvd = _IgIntervalTMCLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 7),
    _IgIntervalTMCLapdRcvd_Type()
)
igIntervalTMCLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalTMCLapdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalTMCLapdRcvd.setUnits("frames")
_IgintervalTMCLapdRcvdErrs_Type = PerfCurrentCount
_IgintervalTMCLapdRcvdErrs_Object = MibTableColumn
igintervalTMCLapdRcvdErrs = _IgintervalTMCLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 8),
    _IgintervalTMCLapdRcvdErrs_Type()
)
igintervalTMCLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igintervalTMCLapdRcvdErrs.setStatus("current")
if mibBuilder.loadTexts:
    igintervalTMCLapdRcvdErrs.setUnits("frames")
_IgIntervalEOCLapdSent_Type = PerfCurrentCount
_IgIntervalEOCLapdSent_Object = MibTableColumn
igIntervalEOCLapdSent = _IgIntervalEOCLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 9),
    _IgIntervalEOCLapdSent_Type()
)
igIntervalEOCLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalEOCLapdSent.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalEOCLapdSent.setUnits("frames")
_IgIntervalEOCLapdRcvd_Type = PerfCurrentCount
_IgIntervalEOCLapdRcvd_Object = MibTableColumn
igIntervalEOCLapdRcvd = _IgIntervalEOCLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 10),
    _IgIntervalEOCLapdRcvd_Type()
)
igIntervalEOCLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalEOCLapdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalEOCLapdRcvd.setUnits("frames")
_IgIntervalEOCLapdRcvdErrs_Type = PerfCurrentCount
_IgIntervalEOCLapdRcvdErrs_Object = MibTableColumn
igIntervalEOCLapdRcvdErrs = _IgIntervalEOCLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 11),
    _IgIntervalEOCLapdRcvdErrs_Type()
)
igIntervalEOCLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalEOCLapdRcvdErrs.setStatus("current")
if mibBuilder.loadTexts:
    igIntervalEOCLapdRcvdErrs.setUnits("frames")


class _IgIntervalValidData_Type(TruthValue):
    """Custom type igIntervalValidData based on TruthValue"""


_IgIntervalValidData_Object = MibTableColumn
igIntervalValidData = _IgIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 12),
    _IgIntervalValidData_Type()
)
igIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igIntervalValidData.setStatus("current")
_IgStatsTotalTable_Object = MibTable
igStatsTotalTable = _IgStatsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5)
)
if mibBuilder.loadTexts:
    igStatsTotalTable.setStatus("current")
_IgStatsTotalEntry_Object = MibTableRow
igStatsTotalEntry = _IgStatsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    igStatsTotalEntry.setStatus("current")
_IgTotalOutboundCalls_Type = PerfCurrentCount
_IgTotalOutboundCalls_Object = MibTableColumn
igTotalOutboundCalls = _IgTotalOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 1),
    _IgTotalOutboundCalls_Type()
)
igTotalOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalOutboundCalls.setStatus("current")
if mibBuilder.loadTexts:
    igTotalOutboundCalls.setUnits("calls")
_IgTotalInboundCalls_Type = PerfCurrentCount
_IgTotalInboundCalls_Object = MibTableColumn
igTotalInboundCalls = _IgTotalInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 2),
    _IgTotalInboundCalls_Type()
)
igTotalInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalInboundCalls.setStatus("current")
if mibBuilder.loadTexts:
    igTotalInboundCalls.setUnits("calls")
_IgTotalOutboundCallsBlocked_Type = PerfCurrentCount
_IgTotalOutboundCallsBlocked_Object = MibTableColumn
igTotalOutboundCallsBlocked = _IgTotalOutboundCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 3),
    _IgTotalOutboundCallsBlocked_Type()
)
igTotalOutboundCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalOutboundCallsBlocked.setStatus("current")
if mibBuilder.loadTexts:
    igTotalOutboundCallsBlocked.setUnits("calls")
_IgTotalGR303ProtocolErrors_Type = PerfCurrentCount
_IgTotalGR303ProtocolErrors_Object = MibTableColumn
igTotalGR303ProtocolErrors = _IgTotalGR303ProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 4),
    _IgTotalGR303ProtocolErrors_Type()
)
igTotalGR303ProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalGR303ProtocolErrors.setStatus("current")
if mibBuilder.loadTexts:
    igTotalGR303ProtocolErrors.setUnits("errors")
_IgTotalTMCLapdSent_Type = PerfCurrentCount
_IgTotalTMCLapdSent_Object = MibTableColumn
igTotalTMCLapdSent = _IgTotalTMCLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 5),
    _IgTotalTMCLapdSent_Type()
)
igTotalTMCLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalTMCLapdSent.setStatus("current")
if mibBuilder.loadTexts:
    igTotalTMCLapdSent.setUnits("frames")
_IgTotalTMCLapdRcvd_Type = PerfCurrentCount
_IgTotalTMCLapdRcvd_Object = MibTableColumn
igTotalTMCLapdRcvd = _IgTotalTMCLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 6),
    _IgTotalTMCLapdRcvd_Type()
)
igTotalTMCLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalTMCLapdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    igTotalTMCLapdRcvd.setUnits("frames")
_IgTotalTMCLapdRcvdErrs_Type = PerfCurrentCount
_IgTotalTMCLapdRcvdErrs_Object = MibTableColumn
igTotalTMCLapdRcvdErrs = _IgTotalTMCLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 7),
    _IgTotalTMCLapdRcvdErrs_Type()
)
igTotalTMCLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalTMCLapdRcvdErrs.setStatus("current")
if mibBuilder.loadTexts:
    igTotalTMCLapdRcvdErrs.setUnits("frames")
_IgTotalEOCLapdSent_Type = PerfCurrentCount
_IgTotalEOCLapdSent_Object = MibTableColumn
igTotalEOCLapdSent = _IgTotalEOCLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 8),
    _IgTotalEOCLapdSent_Type()
)
igTotalEOCLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalEOCLapdSent.setStatus("current")
if mibBuilder.loadTexts:
    igTotalEOCLapdSent.setUnits("frames")
_IgTotalEOCLapdRcvd_Type = PerfCurrentCount
_IgTotalEOCLapdRcvd_Object = MibTableColumn
igTotalEOCLapdRcvd = _IgTotalEOCLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 9),
    _IgTotalEOCLapdRcvd_Type()
)
igTotalEOCLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalEOCLapdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    igTotalEOCLapdRcvd.setUnits("frames")
_IgTotalEOCLapdRcvdErrs_Type = PerfCurrentCount
_IgTotalEOCLapdRcvdErrs_Object = MibTableColumn
igTotalEOCLapdRcvdErrs = _IgTotalEOCLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 10),
    _IgTotalEOCLapdRcvdErrs_Type()
)
igTotalEOCLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igTotalEOCLapdRcvdErrs.setStatus("current")
if mibBuilder.loadTexts:
    igTotalEOCLapdRcvdErrs.setUnits("frames")
_Ds1LineMappingTable_Object = MibTable
ds1LineMappingTable = _Ds1LineMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ds1LineMappingTable.setStatus("current")
_Ds1LineMappingEntry_Object = MibTableRow
ds1LineMappingEntry = _Ds1LineMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1)
)
ds1LineMappingEntry.setIndexNames(
    (0, "ZhoneGR303-MIB", "igNameId"),
    (0, "ZhoneGR303-MIB", "dsnLgId"),
    (0, "ZhoneGR303-MIB", "ds1ChannelNumber"),
)
if mibBuilder.loadTexts:
    ds1LineMappingEntry.setStatus("current")


class _DsnLgId_Type(Integer32):
    """Custom type dsnLgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsnLgId_Type.__name__ = "Integer32"
_DsnLgId_Object = MibTableColumn
dsnLgId = _DsnLgId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 1),
    _DsnLgId_Type()
)
dsnLgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsnLgId.setStatus("current")


class _Ds1ChannelNumber_Type(Integer32):
    """Custom type ds1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Ds1ChannelNumber_Type.__name__ = "Integer32"
_Ds1ChannelNumber_Object = MibTableColumn
ds1ChannelNumber = _Ds1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 2),
    _Ds1ChannelNumber_Type()
)
ds1ChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ds1ChannelNumber.setStatus("current")


class _Ds1Role_Type(Integer32):
    """Custom type ds1Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("payload", 1),
          ("primary", 3),
          ("secondary", 2))
    )


_Ds1Role_Type.__name__ = "Integer32"
_Ds1Role_Object = MibTableColumn
ds1Role = _Ds1Role_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 3),
    _Ds1Role_Type()
)
ds1Role.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ds1Role.setStatus("current")
_Ds1IfIndex_Type = InterfaceIndexOrZero
_Ds1IfIndex_Object = MibTableColumn
ds1IfIndex = _Ds1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 4),
    _Ds1IfIndex_Type()
)
ds1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IfIndex.setStatus("current")
_Ds1LineMappingRowStatus_Type = ZhoneRowStatus
_Ds1LineMappingRowStatus_Object = MibTableColumn
ds1LineMappingRowStatus = _Ds1LineMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 5),
    _Ds1LineMappingRowStatus_Type()
)
ds1LineMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ds1LineMappingRowStatus.setStatus("current")


class _Ds1LogicalId_Type(Integer32):
    """Custom type ds1LogicalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Ds1LogicalId_Type.__name__ = "Integer32"
_Ds1LogicalId_Object = MibTableColumn
ds1LogicalId = _Ds1LogicalId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 6),
    _Ds1LogicalId_Type()
)
ds1LogicalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ds1LogicalId.setStatus("current")
_IgCrvTable_Object = MibTable
igCrvTable = _IgCrvTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7)
)
if mibBuilder.loadTexts:
    igCrvTable.setStatus("current")
_IgCrvEntry_Object = MibTableRow
igCrvEntry = _IgCrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1)
)
igCrvEntry.setIndexNames(
    (0, "ZhoneGR303-MIB", "igNameId"),
    (0, "ZhoneGR303-MIB", "igCrv"),
)
if mibBuilder.loadTexts:
    igCrvEntry.setStatus("current")


class _IgCrv_Type(Integer32):
    """Custom type igCrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_IgCrv_Type.__name__ = "Integer32"
_IgCrv_Object = MibTableColumn
igCrv = _IgCrv_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 1),
    _IgCrv_Type()
)
igCrv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igCrv.setStatus("current")


class _IgCrvLocalAdminState_Type(Integer32):
    """Custom type igCrvLocalAdminState based on Integer32"""
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


_IgCrvLocalAdminState_Type.__name__ = "Integer32"
_IgCrvLocalAdminState_Object = MibTableColumn
igCrvLocalAdminState = _IgCrvLocalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 2),
    _IgCrvLocalAdminState_Type()
)
igCrvLocalAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igCrvLocalAdminState.setStatus("current")


class _IgCrvRemoteAdminState_Type(Integer32):
    """Custom type igCrvRemoteAdminState based on Integer32"""
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


_IgCrvRemoteAdminState_Type.__name__ = "Integer32"
_IgCrvRemoteAdminState_Object = MibTableColumn
igCrvRemoteAdminState = _IgCrvRemoteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 3),
    _IgCrvRemoteAdminState_Type()
)
igCrvRemoteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCrvRemoteAdminState.setStatus("current")


class _IgCrvOperStatus_Type(Bits):
    """Custom type igCrvOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("fault", 1),
          ("manualOos", 2),
          ("notConnected", 5),
          ("removedFromServiceBySwitch", 3),
          ("unEquipped", 4),
          ("up", 0))
    )

_IgCrvOperStatus_Type.__name__ = "Bits"
_IgCrvOperStatus_Object = MibTableColumn
igCrvOperStatus = _IgCrvOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 4),
    _IgCrvOperStatus_Type()
)
igCrvOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCrvOperStatus.setStatus("current")


class _IgCrvTmcState_Type(Integer32):
    """Custom type igCrvTmcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("permanentSignal", 2))
    )


_IgCrvTmcState_Type.__name__ = "Integer32"
_IgCrvTmcState_Object = MibTableColumn
igCrvTmcState = _IgCrvTmcState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 5),
    _IgCrvTmcState_Type()
)
igCrvTmcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igCrvTmcState.setStatus("current")


class _IgCrvSignalType_Type(Integer32):
    """Custom type igCrvSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("electronicbusinessset", 5),
          ("groundstart", 3),
          ("loopreversebattery", 4),
          ("loopstart", 2))
    )


_IgCrvSignalType_Type.__name__ = "Integer32"
_IgCrvSignalType_Object = MibTableColumn
igCrvSignalType = _IgCrvSignalType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 6),
    _IgCrvSignalType_Type()
)
igCrvSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igCrvSignalType.setStatus("current")
_IgCrvRowStatus_Type = ZhoneRowStatus
_IgCrvRowStatus_Object = MibTableColumn
igCrvRowStatus = _IgCrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 7),
    _IgCrvRowStatus_Type()
)
igCrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igCrvRowStatus.setStatus("current")
_Gr303Traps_ObjectIdentity = ObjectIdentity
gr303Traps = _Gr303Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8)
)
if mibBuilder.loadTexts:
    gr303Traps.setStatus("current")
_Gr303TrapsPrefix_ObjectIdentity = ObjectIdentity
gr303TrapsPrefix = _Gr303TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0)
)
if mibBuilder.loadTexts:
    gr303TrapsPrefix.setStatus("current")
interfaceGroupEntry.registerAugmentions(
    ("ZhoneGR303-MIB",
     "igControlChannelEntry")
)
igControlChannelEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
interfaceGroupEntry.registerAugmentions(
    ("ZhoneGR303-MIB",
     "igStatsCurrentEntry")
)
igStatsCurrentEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
interfaceGroupEntry.registerAugmentions(
    ("ZhoneGR303-MIB",
     "igStatsTotalEntry")
)
igStatsTotalEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())

# Managed Objects groups


# Notification objects

igOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 1)
)
igOperStatusChange.setObjects(
      *(("ZhoneGR303-MIB", "igAdminStatus"),
        ("ZhoneGR303-MIB", "igOperationalStatus"))
)
if mibBuilder.loadTexts:
    igOperStatusChange.setStatus(
        "current"
    )

igTmcPrimaryStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 2)
)
igTmcPrimaryStateChange.setObjects(
    ("ZhoneGR303-MIB", "igControlChannelTmcPrimarySvcState")
)
if mibBuilder.loadTexts:
    igTmcPrimaryStateChange.setStatus(
        "current"
    )

igTmcSecondaryStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 3)
)
igTmcSecondaryStateChange.setObjects(
    ("ZhoneGR303-MIB", "igControlChannelTmcSecondarySvcState")
)
if mibBuilder.loadTexts:
    igTmcSecondaryStateChange.setStatus(
        "current"
    )

igEocPrimaryStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 4)
)
igEocPrimaryStateChange.setObjects(
    ("ZhoneGR303-MIB", "igControlChannelEocPrimarySvcState")
)
if mibBuilder.loadTexts:
    igEocPrimaryStateChange.setStatus(
        "current"
    )

igEocSecondaryStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 5)
)
igEocSecondaryStateChange.setObjects(
    ("ZhoneGR303-MIB", "igControlChannelEocSecondarySvcState")
)
if mibBuilder.loadTexts:
    igEocSecondaryStateChange.setStatus(
        "current"
    )

igCrvRemoteStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 6)
)
igCrvRemoteStateChange.setObjects(
      *(("ZhoneGR303-MIB", "igCrvLocalAdminState"),
        ("ZhoneGR303-MIB", "igCrvRemoteAdminState"),
        ("ZhoneGR303-MIB", "igCrvOperStatus"))
)
if mibBuilder.loadTexts:
    igCrvRemoteStateChange.setStatus(
        "current"
    )

igCrvTmcStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 7)
)
igCrvTmcStateChange.setObjects(
    ("ZhoneGR303-MIB", "igCrvTmcState")
)
if mibBuilder.loadTexts:
    igCrvTmcStateChange.setStatus(
        "current"
    )

igSystemTimeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 8)
)
igSystemTimeChange.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationDateAndTime"),
        ("ZhoneGR303-MIB", "igRowStatus"))
)
if mibBuilder.loadTexts:
    igSystemTimeChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneGR303-MIB",
    **{"zhoneGR303": zhoneGR303,
       "interfaceGroupTable": interfaceGroupTable,
       "interfaceGroupEntry": interfaceGroupEntry,
       "igNameId": igNameId,
       "igShelf": igShelf,
       "igSlot": igSlot,
       "igPeerShelf": igPeerShelf,
       "igPeerSlot": igPeerSlot,
       "igSwitchType": igSwitchType,
       "igPrimaryEocTmcDs1IfIndex": igPrimaryEocTmcDs1IfIndex,
       "igSecondaryEocTmcDs1IfIndex": igSecondaryEocTmcDs1IfIndex,
       "igAdminStatus": igAdminStatus,
       "igOperationalStatus": igOperationalStatus,
       "igPeerStatus": igPeerStatus,
       "igMaxConfigCalls": igMaxConfigCalls,
       "igCurrActiveCalls": igCurrActiveCalls,
       "igStatsTimeElapsed": igStatsTimeElapsed,
       "igStatsValidIntervals": igStatsValidIntervals,
       "igStatsInvalidIntervals": igStatsInvalidIntervals,
       "igRowStatus": igRowStatus,
       "igWorkingMode": igWorkingMode,
       "igControlChannelTable": igControlChannelTable,
       "igControlChannelEntry": igControlChannelEntry,
       "igControlChannelTmcPrimarySvcState": igControlChannelTmcPrimarySvcState,
       "igControlChannelTmcSecondarySvcState": igControlChannelTmcSecondarySvcState,
       "igControlChannelT303": igControlChannelT303,
       "igControlChannelT396": igControlChannelT396,
       "igSapi0MaxOutstandingFrames": igSapi0MaxOutstandingFrames,
       "igSapi0N200": igSapi0N200,
       "igSapi0T200": igSapi0T200,
       "igSapi0T203": igSapi0T203,
       "igSapi0PpsMode": igSapi0PpsMode,
       "igSapi1MaxOutstandingFrames": igSapi1MaxOutstandingFrames,
       "igSapi1N200": igSapi1N200,
       "igSapi1T200": igSapi1T200,
       "igSapi1T203": igSapi1T203,
       "igSapi1PpsMode": igSapi1PpsMode,
       "igControlChannelEocPrimarySvcState": igControlChannelEocPrimarySvcState,
       "igControlChannelEocSecondarySvcState": igControlChannelEocSecondarySvcState,
       "igStatsCurrentTable": igStatsCurrentTable,
       "igStatsCurrentEntry": igStatsCurrentEntry,
       "igCurrentOutboundCalls": igCurrentOutboundCalls,
       "igCurrentInboundCalls": igCurrentInboundCalls,
       "igCurrentOutboundCallsBlocked": igCurrentOutboundCallsBlocked,
       "igCurrentGR303ProtocolErrors": igCurrentGR303ProtocolErrors,
       "igCurrentTMCLapdSent": igCurrentTMCLapdSent,
       "igCurrentTMCLapdRcvd": igCurrentTMCLapdRcvd,
       "igCurrentTMCLapdRcvdErrs": igCurrentTMCLapdRcvdErrs,
       "igCurrentEOCLapdSent": igCurrentEOCLapdSent,
       "igCurrentEOCLapdRcvd": igCurrentEOCLapdRcvd,
       "igCurrentEOCLapdRcvdErrs": igCurrentEOCLapdRcvdErrs,
       "igStatsIntervalTable": igStatsIntervalTable,
       "igStatsIntervalEntry": igStatsIntervalEntry,
       "igIntervalNumber": igIntervalNumber,
       "igIntervalOutboundCalls": igIntervalOutboundCalls,
       "igIntervalInboundCalls": igIntervalInboundCalls,
       "igIntervalOutboundCallsBlocked": igIntervalOutboundCallsBlocked,
       "igIntervalGR303ProtocolErrors": igIntervalGR303ProtocolErrors,
       "igIntervalTMCLapdSent": igIntervalTMCLapdSent,
       "igIntervalTMCLapdRcvd": igIntervalTMCLapdRcvd,
       "igintervalTMCLapdRcvdErrs": igintervalTMCLapdRcvdErrs,
       "igIntervalEOCLapdSent": igIntervalEOCLapdSent,
       "igIntervalEOCLapdRcvd": igIntervalEOCLapdRcvd,
       "igIntervalEOCLapdRcvdErrs": igIntervalEOCLapdRcvdErrs,
       "igIntervalValidData": igIntervalValidData,
       "igStatsTotalTable": igStatsTotalTable,
       "igStatsTotalEntry": igStatsTotalEntry,
       "igTotalOutboundCalls": igTotalOutboundCalls,
       "igTotalInboundCalls": igTotalInboundCalls,
       "igTotalOutboundCallsBlocked": igTotalOutboundCallsBlocked,
       "igTotalGR303ProtocolErrors": igTotalGR303ProtocolErrors,
       "igTotalTMCLapdSent": igTotalTMCLapdSent,
       "igTotalTMCLapdRcvd": igTotalTMCLapdRcvd,
       "igTotalTMCLapdRcvdErrs": igTotalTMCLapdRcvdErrs,
       "igTotalEOCLapdSent": igTotalEOCLapdSent,
       "igTotalEOCLapdRcvd": igTotalEOCLapdRcvd,
       "igTotalEOCLapdRcvdErrs": igTotalEOCLapdRcvdErrs,
       "ds1LineMappingTable": ds1LineMappingTable,
       "ds1LineMappingEntry": ds1LineMappingEntry,
       "dsnLgId": dsnLgId,
       "ds1ChannelNumber": ds1ChannelNumber,
       "ds1Role": ds1Role,
       "ds1IfIndex": ds1IfIndex,
       "ds1LineMappingRowStatus": ds1LineMappingRowStatus,
       "ds1LogicalId": ds1LogicalId,
       "igCrvTable": igCrvTable,
       "igCrvEntry": igCrvEntry,
       "igCrv": igCrv,
       "igCrvLocalAdminState": igCrvLocalAdminState,
       "igCrvRemoteAdminState": igCrvRemoteAdminState,
       "igCrvOperStatus": igCrvOperStatus,
       "igCrvTmcState": igCrvTmcState,
       "igCrvSignalType": igCrvSignalType,
       "igCrvRowStatus": igCrvRowStatus,
       "gr303Traps": gr303Traps,
       "gr303TrapsPrefix": gr303TrapsPrefix,
       "igOperStatusChange": igOperStatusChange,
       "igTmcPrimaryStateChange": igTmcPrimaryStateChange,
       "igTmcSecondaryStateChange": igTmcSecondaryStateChange,
       "igEocPrimaryStateChange": igEocPrimaryStateChange,
       "igEocSecondaryStateChange": igEocSecondaryStateChange,
       "igCrvRemoteStateChange": igCrvRemoteStateChange,
       "igCrvTmcStateChange": igCrvTmcStateChange,
       "igSystemTimeChange": igSystemTimeChange}
)
