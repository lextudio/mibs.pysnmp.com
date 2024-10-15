# SNMP MIB module (ASCEND-ADVANCED-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-ADVANCED-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:52 2024
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

(DisplayString,
 advancedAgent) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "DisplayString",
    "advancedAgent")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _WanUseTrunkGroups_Type(Integer32):
    """Custom type wanUseTrunkGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-use", 1),
          ("use", 2))
    )


_WanUseTrunkGroups_Type.__name__ = "Integer32"
_WanUseTrunkGroups_Object = MibScalar
wanUseTrunkGroups = _WanUseTrunkGroups_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 20),
    _WanUseTrunkGroups_Type()
)
wanUseTrunkGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUseTrunkGroups.setStatus("mandatory")
_WanLineTable_Object = MibTable
wanLineTable = _WanLineTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21)
)
if mibBuilder.loadTexts:
    wanLineTable.setStatus("mandatory")
_WanLineEntry_Object = MibTableRow
wanLineEntry = _WanLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1)
)
wanLineEntry.setIndexNames(
    (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineIfIndex"),
)
if mibBuilder.loadTexts:
    wanLineEntry.setStatus("mandatory")
_WanLineIfIndex_Type = Integer32
_WanLineIfIndex_Object = MibTableColumn
wanLineIfIndex = _WanLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 1),
    _WanLineIfIndex_Type()
)
wanLineIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineIfIndex.setStatus("mandatory")
_WanLineName_Type = DisplayString
_WanLineName_Object = MibTableColumn
wanLineName = _WanLineName_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 2),
    _WanLineName_Type()
)
wanLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineName.setStatus("mandatory")
_WanLineType_Type = ObjectIdentifier
_WanLineType_Object = MibTableColumn
wanLineType = _WanLineType_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 3),
    _WanLineType_Type()
)
wanLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineType.setStatus("mandatory")
_WanLineChannels_Type = Integer32
_WanLineChannels_Object = MibTableColumn
wanLineChannels = _WanLineChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 4),
    _WanLineChannels_Type()
)
wanLineChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannels.setStatus("mandatory")


class _WanLineState_Type(Integer32):
    """Custom type wanLineState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ls-active", 13),
          ("ls-ais-receive", 11),
          ("ls-disabled", 3),
          ("ls-does-not-exist", 2),
          ("ls-loss-of-sync", 9),
          ("ls-maintenance", 14),
          ("ls-multipoint-1", 7),
          ("ls-multipoint-2", 8),
          ("ls-no-d-channel", 12),
          ("ls-no-logical", 5),
          ("ls-no-physical", 4),
          ("ls-point-to-point", 6),
          ("ls-unknown", 1),
          ("ls-yellow-alarm", 10))
    )


_WanLineState_Type.__name__ = "Integer32"
_WanLineState_Object = MibTableColumn
wanLineState = _WanLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 5),
    _WanLineState_Type()
)
wanLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineState.setStatus("mandatory")
_WanLineStateString_Type = DisplayString
_WanLineStateString_Object = MibTableColumn
wanLineStateString = _WanLineStateString_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 6),
    _WanLineStateString_Type()
)
wanLineStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineStateString.setStatus("mandatory")
_WanLineActiveChannels_Type = Integer32
_WanLineActiveChannels_Object = MibTableColumn
wanLineActiveChannels = _WanLineActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 7),
    _WanLineActiveChannels_Type()
)
wanLineActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineActiveChannels.setStatus("mandatory")


class _WanLineUsage_Type(Integer32):
    """Custom type wanLineUsage based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("lu-disabled", 3),
          ("lu-drop-and-insert", 7),
          ("lu-enabled", 4),
          ("lu-quiesced", 6),
          ("lu-t-online-user", 8),
          ("lu-t-online-zgr", 9),
          ("lu-trunk", 5),
          ("lu-unavailable", 2),
          ("lu-unknown", 1))
    )


_WanLineUsage_Type.__name__ = "Integer32"
_WanLineUsage_Object = MibTableColumn
wanLineUsage = _WanLineUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 8),
    _WanLineUsage_Type()
)
wanLineUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLineUsage.setStatus("mandatory")
_WanLineHuntGrpPhoneNumber1_Type = DisplayString
_WanLineHuntGrpPhoneNumber1_Object = MibTableColumn
wanLineHuntGrpPhoneNumber1 = _WanLineHuntGrpPhoneNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 9),
    _WanLineHuntGrpPhoneNumber1_Type()
)
wanLineHuntGrpPhoneNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLineHuntGrpPhoneNumber1.setStatus("mandatory")
_WanLineHuntGrpPhoneNumber2_Type = DisplayString
_WanLineHuntGrpPhoneNumber2_Object = MibTableColumn
wanLineHuntGrpPhoneNumber2 = _WanLineHuntGrpPhoneNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 10),
    _WanLineHuntGrpPhoneNumber2_Type()
)
wanLineHuntGrpPhoneNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLineHuntGrpPhoneNumber2.setStatus("mandatory")
_WanLineHuntGrpPhoneNumber3_Type = DisplayString
_WanLineHuntGrpPhoneNumber3_Object = MibTableColumn
wanLineHuntGrpPhoneNumber3 = _WanLineHuntGrpPhoneNumber3_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 11),
    _WanLineHuntGrpPhoneNumber3_Type()
)
wanLineHuntGrpPhoneNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLineHuntGrpPhoneNumber3.setStatus("mandatory")
_WanLineAvailableChannels_Type = Integer32
_WanLineAvailableChannels_Object = MibTableColumn
wanLineAvailableChannels = _WanLineAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 12),
    _WanLineAvailableChannels_Type()
)
wanLineAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineAvailableChannels.setStatus("mandatory")
_WanLineSwitchedChannels_Type = Integer32
_WanLineSwitchedChannels_Object = MibTableColumn
wanLineSwitchedChannels = _WanLineSwitchedChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 13),
    _WanLineSwitchedChannels_Type()
)
wanLineSwitchedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineSwitchedChannels.setStatus("mandatory")
_WanLineDisabledChannels_Type = Integer32
_WanLineDisabledChannels_Object = MibTableColumn
wanLineDisabledChannels = _WanLineDisabledChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 14),
    _WanLineDisabledChannels_Type()
)
wanLineDisabledChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineDisabledChannels.setStatus("mandatory")
_WanLineNailedChannels_Type = Integer32
_WanLineNailedChannels_Object = MibTableColumn
wanLineNailedChannels = _WanLineNailedChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 15),
    _WanLineNailedChannels_Type()
)
wanLineNailedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineNailedChannels.setStatus("mandatory")
_WanLineOutOfServiceChannels_Type = Integer32
_WanLineOutOfServiceChannels_Object = MibTableColumn
wanLineOutOfServiceChannels = _WanLineOutOfServiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 16),
    _WanLineOutOfServiceChannels_Type()
)
wanLineOutOfServiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineOutOfServiceChannels.setStatus("mandatory")
_WanLineNet2NetChannels_Type = Integer32
_WanLineNet2NetChannels_Object = MibTableColumn
wanLineNet2NetChannels = _WanLineNet2NetChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 17),
    _WanLineNet2NetChannels_Type()
)
wanLineNet2NetChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineNet2NetChannels.setStatus("mandatory")
_WanLineDtptChannels_Type = Integer32
_WanLineDtptChannels_Object = MibTableColumn
wanLineDtptChannels = _WanLineDtptChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 18),
    _WanLineDtptChannels_Type()
)
wanLineDtptChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineDtptChannels.setStatus("mandatory")
_WanLineChannelTable_Object = MibTable
wanLineChannelTable = _WanLineChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22)
)
if mibBuilder.loadTexts:
    wanLineChannelTable.setStatus("mandatory")
_WanLineChannelEntry_Object = MibTableRow
wanLineChannelEntry = _WanLineChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1)
)
wanLineChannelEntry.setIndexNames(
    (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineChannelIfIndex"),
    (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineChannelIndex"),
)
if mibBuilder.loadTexts:
    wanLineChannelEntry.setStatus("mandatory")
_WanLineChannelIfIndex_Type = Integer32
_WanLineChannelIfIndex_Object = MibTableColumn
wanLineChannelIfIndex = _WanLineChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 1),
    _WanLineChannelIfIndex_Type()
)
wanLineChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelIfIndex.setStatus("mandatory")
_WanLineChannelIndex_Type = Integer32
_WanLineChannelIndex_Object = MibTableColumn
wanLineChannelIndex = _WanLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 2),
    _WanLineChannelIndex_Type()
)
wanLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelIndex.setStatus("mandatory")


class _WanLineChannelState_Type(Integer32):
    """Custom type wanLineChannelState based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("bs-backup-d", 15),
          ("bs-clear-pending", 8),
          ("bs-connected", 11),
          ("bs-connected-dtpt", 24),
          ("bs-connected-net2net", 21),
          ("bs-current-d", 14),
          ("bs-cut-through", 13),
          ("bs-dialing", 9),
          ("bs-dialing-dtpt", 22),
          ("bs-dialing-net2net", 19),
          ("bs-disabled", 18),
          ("bs-held", 6),
          ("bs-idle", 7),
          ("bs-maintenance", 16),
          ("bs-nailed-up", 5),
          ("bs-out-of-service", 4),
          ("bs-ringing", 10),
          ("bs-ringing-dtpt", 23),
          ("bs-ringing-net2net", 20),
          ("bs-signaling", 12),
          ("bs-spc-up", 17),
          ("bs-unavailable", 2),
          ("bs-unknown", 1),
          ("bs-unused", 3))
    )


_WanLineChannelState_Type.__name__ = "Integer32"
_WanLineChannelState_Object = MibTableColumn
wanLineChannelState = _WanLineChannelState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 3),
    _WanLineChannelState_Type()
)
wanLineChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelState.setStatus("mandatory")
_WanLineChannelStateString_Type = DisplayString
_WanLineChannelStateString_Object = MibTableColumn
wanLineChannelStateString = _WanLineChannelStateString_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 4),
    _WanLineChannelStateString_Type()
)
wanLineChannelStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelStateString.setStatus("mandatory")
_WanLineChannelErrorCount_Type = Integer32
_WanLineChannelErrorCount_Object = MibTableColumn
wanLineChannelErrorCount = _WanLineChannelErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 5),
    _WanLineChannelErrorCount_Type()
)
wanLineChannelErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelErrorCount.setStatus("mandatory")


class _WanLineChannelUsage_Type(Integer32):
    """Custom type wanLineChannelUsage based on Integer32"""
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
        *(("ds0-cas-channel", 9),
          ("ds0-clear-64", 5),
          ("ds0-cut-through", 4),
          ("ds0-nfas-prime-d", 7),
          ("ds0-nfas-sec-d", 8),
          ("ds0-pri-d-channel", 6),
          ("ds0-spc-channel", 10),
          ("ds0-switched-channel", 3),
          ("ds0-unknown-channel", 1),
          ("ds0-unused-channel", 2))
    )


_WanLineChannelUsage_Type.__name__ = "Integer32"
_WanLineChannelUsage_Object = MibTableColumn
wanLineChannelUsage = _WanLineChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 6),
    _WanLineChannelUsage_Type()
)
wanLineChannelUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelUsage.setStatus("mandatory")
_WanLineChannelTrunkGroup_Type = Integer32
_WanLineChannelTrunkGroup_Object = MibTableColumn
wanLineChannelTrunkGroup = _WanLineChannelTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 7),
    _WanLineChannelTrunkGroup_Type()
)
wanLineChannelTrunkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelTrunkGroup.setStatus("mandatory")
_WanLineChannelPhoneNumber_Type = DisplayString
_WanLineChannelPhoneNumber_Object = MibTableColumn
wanLineChannelPhoneNumber = _WanLineChannelPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 8),
    _WanLineChannelPhoneNumber_Type()
)
wanLineChannelPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelPhoneNumber.setStatus("mandatory")
_WanLineChannelSlot_Type = Integer32
_WanLineChannelSlot_Object = MibTableColumn
wanLineChannelSlot = _WanLineChannelSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 9),
    _WanLineChannelSlot_Type()
)
wanLineChannelSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelSlot.setStatus("mandatory")
_WanLineChannelPort_Type = Integer32
_WanLineChannelPort_Object = MibTableColumn
wanLineChannelPort = _WanLineChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 10),
    _WanLineChannelPort_Type()
)
wanLineChannelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelPort.setStatus("mandatory")


class _WanLineChannelNailedState_Type(Integer32):
    """Custom type wanLineChannelNailedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nailed-active", 3),
          ("nailed-held", 2),
          ("not-applicable", 1))
    )


_WanLineChannelNailedState_Type.__name__ = "Integer32"
_WanLineChannelNailedState_Object = MibTableColumn
wanLineChannelNailedState = _WanLineChannelNailedState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 11),
    _WanLineChannelNailedState_Type()
)
wanLineChannelNailedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelNailedState.setStatus("mandatory")
_WanAvailableChannels_Type = Integer32
_WanAvailableChannels_Object = MibScalar
wanAvailableChannels = _WanAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 23),
    _WanAvailableChannels_Type()
)
wanAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAvailableChannels.setStatus("mandatory")
_WanSwitchedChannels_Type = Integer32
_WanSwitchedChannels_Object = MibScalar
wanSwitchedChannels = _WanSwitchedChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 24),
    _WanSwitchedChannels_Type()
)
wanSwitchedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanSwitchedChannels.setStatus("mandatory")
_WanDisabledChannels_Type = Integer32
_WanDisabledChannels_Object = MibScalar
wanDisabledChannels = _WanDisabledChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 25),
    _WanDisabledChannels_Type()
)
wanDisabledChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDisabledChannels.setStatus("mandatory")
_WanActiveChannels_Type = Integer32
_WanActiveChannels_Object = MibScalar
wanActiveChannels = _WanActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 26),
    _WanActiveChannels_Type()
)
wanActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanActiveChannels.setStatus("mandatory")
_WanNailedChannels_Type = Integer32
_WanNailedChannels_Object = MibScalar
wanNailedChannels = _WanNailedChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 27),
    _WanNailedChannels_Type()
)
wanNailedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNailedChannels.setStatus("mandatory")
_WanOutOfServiceChannels_Type = Integer32
_WanOutOfServiceChannels_Object = MibScalar
wanOutOfServiceChannels = _WanOutOfServiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 28),
    _WanOutOfServiceChannels_Type()
)
wanOutOfServiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanOutOfServiceChannels.setStatus("mandatory")
_WanLineChannelUsageTable_Object = MibTable
wanLineChannelUsageTable = _WanLineChannelUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 29)
)
if mibBuilder.loadTexts:
    wanLineChannelUsageTable.setStatus("mandatory")
_WanLineChannelUsageEntry_Object = MibTableRow
wanLineChannelUsageEntry = _WanLineChannelUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 29, 1)
)
wanLineChannelUsageEntry.setIndexNames(
    (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineUsage"),
    (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineChannelState"),
)
if mibBuilder.loadTexts:
    wanLineChannelUsageEntry.setStatus("mandatory")
_WanLineChannelUsageCount_Type = Integer32
_WanLineChannelUsageCount_Object = MibTableColumn
wanLineChannelUsageCount = _WanLineChannelUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 29, 1, 1),
    _WanLineChannelUsageCount_Type()
)
wanLineChannelUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanLineChannelUsageCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-ADVANCED-AGENT-MIB",
    **{"wanUseTrunkGroups": wanUseTrunkGroups,
       "wanLineTable": wanLineTable,
       "wanLineEntry": wanLineEntry,
       "wanLineIfIndex": wanLineIfIndex,
       "wanLineName": wanLineName,
       "wanLineType": wanLineType,
       "wanLineChannels": wanLineChannels,
       "wanLineState": wanLineState,
       "wanLineStateString": wanLineStateString,
       "wanLineActiveChannels": wanLineActiveChannels,
       "wanLineUsage": wanLineUsage,
       "wanLineHuntGrpPhoneNumber1": wanLineHuntGrpPhoneNumber1,
       "wanLineHuntGrpPhoneNumber2": wanLineHuntGrpPhoneNumber2,
       "wanLineHuntGrpPhoneNumber3": wanLineHuntGrpPhoneNumber3,
       "wanLineAvailableChannels": wanLineAvailableChannels,
       "wanLineSwitchedChannels": wanLineSwitchedChannels,
       "wanLineDisabledChannels": wanLineDisabledChannels,
       "wanLineNailedChannels": wanLineNailedChannels,
       "wanLineOutOfServiceChannels": wanLineOutOfServiceChannels,
       "wanLineNet2NetChannels": wanLineNet2NetChannels,
       "wanLineDtptChannels": wanLineDtptChannels,
       "wanLineChannelTable": wanLineChannelTable,
       "wanLineChannelEntry": wanLineChannelEntry,
       "wanLineChannelIfIndex": wanLineChannelIfIndex,
       "wanLineChannelIndex": wanLineChannelIndex,
       "wanLineChannelState": wanLineChannelState,
       "wanLineChannelStateString": wanLineChannelStateString,
       "wanLineChannelErrorCount": wanLineChannelErrorCount,
       "wanLineChannelUsage": wanLineChannelUsage,
       "wanLineChannelTrunkGroup": wanLineChannelTrunkGroup,
       "wanLineChannelPhoneNumber": wanLineChannelPhoneNumber,
       "wanLineChannelSlot": wanLineChannelSlot,
       "wanLineChannelPort": wanLineChannelPort,
       "wanLineChannelNailedState": wanLineChannelNailedState,
       "wanAvailableChannels": wanAvailableChannels,
       "wanSwitchedChannels": wanSwitchedChannels,
       "wanDisabledChannels": wanDisabledChannels,
       "wanActiveChannels": wanActiveChannels,
       "wanNailedChannels": wanNailedChannels,
       "wanOutOfServiceChannels": wanOutOfServiceChannels,
       "wanLineChannelUsageTable": wanLineChannelUsageTable,
       "wanLineChannelUsageEntry": wanLineChannelUsageEntry,
       "wanLineChannelUsageCount": wanLineChannelUsageCount}
)
