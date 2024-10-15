# SNMP MIB module (CISCO-WIRELESS-DOCS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-DOCS-EXT-MIB
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

(cwdIfHeMacEntry,
 cwdIfHeServiceEntry,
 cwdIfHeSuStatusDownChanIfIndex,
 cwdIfHeSuStatusEntry,
 cwdIfHeSuStatusIndex,
 cwdIfHeSuStatusIpAddress,
 cwdIfHeSuStatusMacAddress,
 cwdIfHeSuStatusServiceId,
 cwdIfHeSuStatusUpChanIfIndex,
 cwdIfQosProfIndex,
 cwdIfQosProfileEntry) = mibBuilder.importSymbols(
    "CISCO-WIRELESS-DOCS-IF-MIB",
    "cwdIfHeMacEntry",
    "cwdIfHeServiceEntry",
    "cwdIfHeSuStatusDownChanIfIndex",
    "cwdIfHeSuStatusEntry",
    "cwdIfHeSuStatusIndex",
    "cwdIfHeSuStatusIpAddress",
    "cwdIfHeSuStatusMacAddress",
    "cwdIfHeSuStatusServiceId",
    "cwdIfHeSuStatusUpChanIfIndex",
    "cwdIfQosProfIndex",
    "cwdIfQosProfileEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessDocsExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169)
)
ciscoWirelessDocsExtMIB.setRevisions(
        ("2000-07-17 10:03",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWirelessDocsExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWirelessDocsExtMIBObjects = _CiscoWirelessDocsExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1)
)
_CwdxQosCtrlObjects_ObjectIdentity = ObjectIdentity
cwdxQosCtrlObjects = _CwdxQosCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1)
)
_CwdxQosCtrlUpTable_Object = MibTable
cwdxQosCtrlUpTable = _CwdxQosCtrlUpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwdxQosCtrlUpTable.setStatus("current")
_CwdxQosCtrlUpEntry_Object = MibTableRow
cwdxQosCtrlUpEntry = _CwdxQosCtrlUpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1, 1)
)
cwdxQosCtrlUpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdxQosCtrlUpEntry.setStatus("current")
_CwdxQosCtrlUpAdmissionCtrl_Type = TruthValue
_CwdxQosCtrlUpAdmissionCtrl_Object = MibTableColumn
cwdxQosCtrlUpAdmissionCtrl = _CwdxQosCtrlUpAdmissionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1, 1, 1),
    _CwdxQosCtrlUpAdmissionCtrl_Type()
)
cwdxQosCtrlUpAdmissionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpAdmissionCtrl.setStatus("current")


class _CwdxQosCtrlUpMaxRsvdBWPercent_Type(Integer32):
    """Custom type cwdxQosCtrlUpMaxRsvdBWPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_CwdxQosCtrlUpMaxRsvdBWPercent_Type.__name__ = "Integer32"
_CwdxQosCtrlUpMaxRsvdBWPercent_Object = MibTableColumn
cwdxQosCtrlUpMaxRsvdBWPercent = _CwdxQosCtrlUpMaxRsvdBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1, 1, 2),
    _CwdxQosCtrlUpMaxRsvdBWPercent_Type()
)
cwdxQosCtrlUpMaxRsvdBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpMaxRsvdBWPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpMaxRsvdBWPercent.setUnits("percent")
_CwdxQosCtrlUpAdmissionRejects_Type = Counter32
_CwdxQosCtrlUpAdmissionRejects_Object = MibTableColumn
cwdxQosCtrlUpAdmissionRejects = _CwdxQosCtrlUpAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1, 1, 3),
    _CwdxQosCtrlUpAdmissionRejects_Type()
)
cwdxQosCtrlUpAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpAdmissionRejects.setStatus("current")


class _CwdxQosCtrlUpReservedBW_Type(Integer32):
    """Custom type cwdxQosCtrlUpReservedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CwdxQosCtrlUpReservedBW_Type.__name__ = "Integer32"
_CwdxQosCtrlUpReservedBW_Object = MibTableColumn
cwdxQosCtrlUpReservedBW = _CwdxQosCtrlUpReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1, 1, 4),
    _CwdxQosCtrlUpReservedBW_Type()
)
cwdxQosCtrlUpReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpReservedBW.setStatus("current")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpReservedBW.setUnits("bits/second")


class _CwdxQosCtrlUpMaxVirtualBW_Type(Integer32):
    """Custom type cwdxQosCtrlUpMaxVirtualBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CwdxQosCtrlUpMaxVirtualBW_Type.__name__ = "Integer32"
_CwdxQosCtrlUpMaxVirtualBW_Object = MibTableColumn
cwdxQosCtrlUpMaxVirtualBW = _CwdxQosCtrlUpMaxVirtualBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 1, 1, 5),
    _CwdxQosCtrlUpMaxVirtualBW_Type()
)
cwdxQosCtrlUpMaxVirtualBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpMaxVirtualBW.setStatus("current")
if mibBuilder.loadTexts:
    cwdxQosCtrlUpMaxVirtualBW.setUnits("bits/second")
_CwdxQosIfRateLimitTable_Object = MibTable
cwdxQosIfRateLimitTable = _CwdxQosIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwdxQosIfRateLimitTable.setStatus("current")
_CwdxQosIfRateLimitEntry_Object = MibTableRow
cwdxQosIfRateLimitEntry = _CwdxQosIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 2, 1)
)
cwdxQosIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdxQosIfRateLimitEntry.setStatus("current")


class _CwdxQosIfRateLimitAlgo_Type(Integer32):
    """Custom type cwdxQosIfRateLimitAlgo based on Integer32"""
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
        *(("carLike", 3),
          ("noRateLimit", 1),
          ("oneSecBurst", 2),
          ("shaping", 5),
          ("wgtExPacketDiscard", 4))
    )


_CwdxQosIfRateLimitAlgo_Type.__name__ = "Integer32"
_CwdxQosIfRateLimitAlgo_Object = MibTableColumn
cwdxQosIfRateLimitAlgo = _CwdxQosIfRateLimitAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 2, 1, 1),
    _CwdxQosIfRateLimitAlgo_Type()
)
cwdxQosIfRateLimitAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosIfRateLimitAlgo.setStatus("current")


class _CwdxQosIfRateLimitExpWgt_Type(Integer32):
    """Custom type cwdxQosIfRateLimitExpWgt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CwdxQosIfRateLimitExpWgt_Type.__name__ = "Integer32"
_CwdxQosIfRateLimitExpWgt_Object = MibTableColumn
cwdxQosIfRateLimitExpWgt = _CwdxQosIfRateLimitExpWgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 2, 1, 2),
    _CwdxQosIfRateLimitExpWgt_Type()
)
cwdxQosIfRateLimitExpWgt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosIfRateLimitExpWgt.setStatus("current")


class _CwdxQosIfRateLimitShpMaxDelay_Type(Integer32):
    """Custom type cwdxQosIfRateLimitShpMaxDelay based on Integer32"""
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
        *(("msec1024", 5),
          ("msec128", 2),
          ("msec256", 3),
          ("msec512", 4),
          ("na", 1))
    )


_CwdxQosIfRateLimitShpMaxDelay_Type.__name__ = "Integer32"
_CwdxQosIfRateLimitShpMaxDelay_Object = MibTableColumn
cwdxQosIfRateLimitShpMaxDelay = _CwdxQosIfRateLimitShpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 2, 1, 3),
    _CwdxQosIfRateLimitShpMaxDelay_Type()
)
cwdxQosIfRateLimitShpMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosIfRateLimitShpMaxDelay.setStatus("current")


class _CwdxQosIfRateLimitShpGranularity_Type(Integer32):
    """Custom type cwdxQosIfRateLimitShpGranularity based on Integer32"""
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
        *(("msec1", 2),
          ("msec16", 6),
          ("msec2", 3),
          ("msec4", 4),
          ("msec8", 5),
          ("na", 1))
    )


_CwdxQosIfRateLimitShpGranularity_Type.__name__ = "Integer32"
_CwdxQosIfRateLimitShpGranularity_Object = MibTableColumn
cwdxQosIfRateLimitShpGranularity = _CwdxQosIfRateLimitShpGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 2, 1, 4),
    _CwdxQosIfRateLimitShpGranularity_Type()
)
cwdxQosIfRateLimitShpGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosIfRateLimitShpGranularity.setStatus("current")
_CwdxHeServiceExtTable_Object = MibTable
cwdxHeServiceExtTable = _CwdxHeServiceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cwdxHeServiceExtTable.setStatus("current")
_CwdxHeServiceExtEntry_Object = MibTableRow
cwdxHeServiceExtEntry = _CwdxHeServiceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwdxHeServiceExtEntry.setStatus("current")
_CwdxIfHeServiceOutOctets_Type = Counter32
_CwdxIfHeServiceOutOctets_Object = MibTableColumn
cwdxIfHeServiceOutOctets = _CwdxIfHeServiceOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 3, 1, 1),
    _CwdxIfHeServiceOutOctets_Type()
)
cwdxIfHeServiceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeServiceOutOctets.setStatus("current")
_CwdxIfHeServiceOutPackets_Type = Counter32
_CwdxIfHeServiceOutPackets_Object = MibTableColumn
cwdxIfHeServiceOutPackets = _CwdxIfHeServiceOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 3, 1, 2),
    _CwdxIfHeServiceOutPackets_Type()
)
cwdxIfHeServiceOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeServiceOutPackets.setStatus("current")
_CwdxQosMaxUpBWExcessRequests_Type = Counter32
_CwdxQosMaxUpBWExcessRequests_Object = MibTableColumn
cwdxQosMaxUpBWExcessRequests = _CwdxQosMaxUpBWExcessRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 3, 1, 3),
    _CwdxQosMaxUpBWExcessRequests_Type()
)
cwdxQosMaxUpBWExcessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxQosMaxUpBWExcessRequests.setStatus("current")
_CwdxQosMaxDownBWExcessPackets_Type = Counter32
_CwdxQosMaxDownBWExcessPackets_Object = MibTableColumn
cwdxQosMaxDownBWExcessPackets = _CwdxQosMaxDownBWExcessPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 1, 3, 1, 4),
    _CwdxQosMaxDownBWExcessPackets_Type()
)
cwdxQosMaxDownBWExcessPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxQosMaxDownBWExcessPackets.setStatus("current")
_CwdxQosQueueObjects_ObjectIdentity = ObjectIdentity
cwdxQosQueueObjects = _CwdxQosQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2)
)
_CwdxBWQueueTable_Object = MibTable
cwdxBWQueueTable = _CwdxBWQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwdxBWQueueTable.setStatus("current")
_CwdxBWQueueEntry_Object = MibTableRow
cwdxBWQueueEntry = _CwdxBWQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1)
)
cwdxBWQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueNameCode"),
)
if mibBuilder.loadTexts:
    cwdxBWQueueEntry.setStatus("current")


class _CwdxBWQueueNameCode_Type(Integer32):
    """Custom type cwdxBWQueueNameCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cirQ", 1),
          ("tbeQ", 2))
    )


_CwdxBWQueueNameCode_Type.__name__ = "Integer32"
_CwdxBWQueueNameCode_Object = MibTableColumn
cwdxBWQueueNameCode = _CwdxBWQueueNameCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 1),
    _CwdxBWQueueNameCode_Type()
)
cwdxBWQueueNameCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdxBWQueueNameCode.setStatus("current")


class _CwdxBWQueueOrder_Type(Integer32):
    """Custom type cwdxBWQueueOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CwdxBWQueueOrder_Type.__name__ = "Integer32"
_CwdxBWQueueOrder_Object = MibTableColumn
cwdxBWQueueOrder = _CwdxBWQueueOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 2),
    _CwdxBWQueueOrder_Type()
)
cwdxBWQueueOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxBWQueueOrder.setStatus("current")


class _CwdxBWQueueNumServedBeforeYield_Type(Integer32):
    """Custom type cwdxBWQueueNumServedBeforeYield based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CwdxBWQueueNumServedBeforeYield_Type.__name__ = "Integer32"
_CwdxBWQueueNumServedBeforeYield_Object = MibTableColumn
cwdxBWQueueNumServedBeforeYield = _CwdxBWQueueNumServedBeforeYield_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 3),
    _CwdxBWQueueNumServedBeforeYield_Type()
)
cwdxBWQueueNumServedBeforeYield.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxBWQueueNumServedBeforeYield.setStatus("current")


class _CwdxBWQueueType_Type(Integer32):
    """Custom type cwdxBWQueueType based on Integer32"""
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
        *(("fifo", 3),
          ("other", 2),
          ("priority", 4),
          ("unknown", 1))
    )


_CwdxBWQueueType_Type.__name__ = "Integer32"
_CwdxBWQueueType_Object = MibTableColumn
cwdxBWQueueType = _CwdxBWQueueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 4),
    _CwdxBWQueueType_Type()
)
cwdxBWQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxBWQueueType.setStatus("current")
_CwdxBWQueueMaxDepth_Type = Integer32
_CwdxBWQueueMaxDepth_Object = MibTableColumn
cwdxBWQueueMaxDepth = _CwdxBWQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 5),
    _CwdxBWQueueMaxDepth_Type()
)
cwdxBWQueueMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxBWQueueMaxDepth.setStatus("current")
_CwdxBWQueueDepth_Type = Integer32
_CwdxBWQueueDepth_Object = MibTableColumn
cwdxBWQueueDepth = _CwdxBWQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 6),
    _CwdxBWQueueDepth_Type()
)
cwdxBWQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxBWQueueDepth.setStatus("current")
_CwdxBWQueueDiscards_Type = Counter32
_CwdxBWQueueDiscards_Object = MibTableColumn
cwdxBWQueueDiscards = _CwdxBWQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 2, 1, 1, 7),
    _CwdxBWQueueDiscards_Type()
)
cwdxBWQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxBWQueueDiscards.setStatus("current")
_CwdxHeSuCpeObjects_ObjectIdentity = ObjectIdentity
cwdxHeSuCpeObjects = _CwdxHeSuCpeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3)
)
_CwdxCpeTable_Object = MibTable
cwdxCpeTable = _CwdxCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwdxCpeTable.setStatus("current")
_CwdxCpeEntry_Object = MibTableRow
cwdxCpeEntry = _CwdxCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 1, 1)
)
cwdxCpeEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxCpeStatusIndex"),
    (0, "CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxCpeMacAddress"),
)
if mibBuilder.loadTexts:
    cwdxCpeEntry.setStatus("current")


class _CwdxCpeStatusIndex_Type(Integer32):
    """Custom type cwdxCpeStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwdxCpeStatusIndex_Type.__name__ = "Integer32"
_CwdxCpeStatusIndex_Object = MibTableColumn
cwdxCpeStatusIndex = _CwdxCpeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 1, 1, 1),
    _CwdxCpeStatusIndex_Type()
)
cwdxCpeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdxCpeStatusIndex.setStatus("current")
_CwdxCpeMacAddress_Type = MacAddress
_CwdxCpeMacAddress_Object = MibTableColumn
cwdxCpeMacAddress = _CwdxCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 1, 1, 2),
    _CwdxCpeMacAddress_Type()
)
cwdxCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdxCpeMacAddress.setStatus("current")
_CwdxCpeIpAddress_Type = IpAddress
_CwdxCpeIpAddress_Object = MibTableColumn
cwdxCpeIpAddress = _CwdxCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 1, 1, 3),
    _CwdxCpeIpAddress_Type()
)
cwdxCpeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxCpeIpAddress.setStatus("current")
_CwdxCpeAccessGroup_Type = DisplayString
_CwdxCpeAccessGroup_Object = MibTableColumn
cwdxCpeAccessGroup = _CwdxCpeAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 1, 1, 4),
    _CwdxCpeAccessGroup_Type()
)
cwdxCpeAccessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxCpeAccessGroup.setStatus("current")
_CwdxSuMappingTable_Object = MibTable
cwdxSuMappingTable = _CwdxSuMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cwdxSuMappingTable.setStatus("current")
_CwdxSuMappingEntry_Object = MibTableRow
cwdxSuMappingEntry = _CwdxSuMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 2, 1)
)
cwdxSuMappingEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxSuMappingMacAddress"),
)
if mibBuilder.loadTexts:
    cwdxSuMappingEntry.setStatus("current")


class _CwdxSuMappingStatusIndex_Type(Integer32):
    """Custom type cwdxSuMappingStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwdxSuMappingStatusIndex_Type.__name__ = "Integer32"
_CwdxSuMappingStatusIndex_Object = MibTableColumn
cwdxSuMappingStatusIndex = _CwdxSuMappingStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 2, 1, 1),
    _CwdxSuMappingStatusIndex_Type()
)
cwdxSuMappingStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxSuMappingStatusIndex.setStatus("current")
_CwdxSuMappingMacAddress_Type = MacAddress
_CwdxSuMappingMacAddress_Object = MibTableColumn
cwdxSuMappingMacAddress = _CwdxSuMappingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 2, 1, 2),
    _CwdxSuMappingMacAddress_Type()
)
cwdxSuMappingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdxSuMappingMacAddress.setStatus("current")
_CwdxHeSuStatusExtTable_Object = MibTable
cwdxHeSuStatusExtTable = _CwdxHeSuStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cwdxHeSuStatusExtTable.setStatus("current")
_CwdxHeSuStatusExtEntry_Object = MibTableRow
cwdxHeSuStatusExtEntry = _CwdxHeSuStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cwdxHeSuStatusExtEntry.setStatus("current")


class _CwdxHeSuStatusValue_Type(Integer32):
    """Custom type cwdxHeSuStatusValue based on Integer32"""
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
        *(("initDhcpReqRcvd", 4),
          ("initRangingRcvd", 3),
          ("initTftpPacketRcvd", 13),
          ("initTodRequestRcvd", 14),
          ("kekRejected", 10),
          ("offline", 1),
          ("online", 12),
          ("onlineKekAssigned", 6),
          ("onlineNetAccessDisabled", 5),
          ("onlineTekAssigned", 7),
          ("others", 2),
          ("rejectBadCos", 9),
          ("rejectBadMic", 8),
          ("tekRejected", 11))
    )


_CwdxHeSuStatusValue_Type.__name__ = "Integer32"
_CwdxHeSuStatusValue_Object = MibTableColumn
cwdxHeSuStatusValue = _CwdxHeSuStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 1),
    _CwdxHeSuStatusValue_Type()
)
cwdxHeSuStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxHeSuStatusValue.setStatus("current")
_CwdxIfHeSuStatusOnlineTimes_Type = Counter32
_CwdxIfHeSuStatusOnlineTimes_Object = MibTableColumn
cwdxIfHeSuStatusOnlineTimes = _CwdxIfHeSuStatusOnlineTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 2),
    _CwdxIfHeSuStatusOnlineTimes_Type()
)
cwdxIfHeSuStatusOnlineTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusOnlineTimes.setStatus("current")


class _CwdxIfHeSuStatusPercentOnline_Type(Integer32):
    """Custom type cwdxIfHeSuStatusPercentOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CwdxIfHeSuStatusPercentOnline_Type.__name__ = "Integer32"
_CwdxIfHeSuStatusPercentOnline_Object = MibTableColumn
cwdxIfHeSuStatusPercentOnline = _CwdxIfHeSuStatusPercentOnline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 3),
    _CwdxIfHeSuStatusPercentOnline_Type()
)
cwdxIfHeSuStatusPercentOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusPercentOnline.setStatus("current")
_CwdxIfHeSuStatusMinOnlineTime_Type = TimeInterval
_CwdxIfHeSuStatusMinOnlineTime_Object = MibTableColumn
cwdxIfHeSuStatusMinOnlineTime = _CwdxIfHeSuStatusMinOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 4),
    _CwdxIfHeSuStatusMinOnlineTime_Type()
)
cwdxIfHeSuStatusMinOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusMinOnlineTime.setStatus("current")
_CwdxIfHeSuStatusAvgOnlineTime_Type = TimeInterval
_CwdxIfHeSuStatusAvgOnlineTime_Object = MibTableColumn
cwdxIfHeSuStatusAvgOnlineTime = _CwdxIfHeSuStatusAvgOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 5),
    _CwdxIfHeSuStatusAvgOnlineTime_Type()
)
cwdxIfHeSuStatusAvgOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusAvgOnlineTime.setStatus("current")
_CwdxIfHeSuStatusMaxOnlineTime_Type = TimeInterval
_CwdxIfHeSuStatusMaxOnlineTime_Object = MibTableColumn
cwdxIfHeSuStatusMaxOnlineTime = _CwdxIfHeSuStatusMaxOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 6),
    _CwdxIfHeSuStatusMaxOnlineTime_Type()
)
cwdxIfHeSuStatusMaxOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusMaxOnlineTime.setStatus("current")
_CwdxIfHeSuStatusMinOfflineTime_Type = TimeInterval
_CwdxIfHeSuStatusMinOfflineTime_Object = MibTableColumn
cwdxIfHeSuStatusMinOfflineTime = _CwdxIfHeSuStatusMinOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 7),
    _CwdxIfHeSuStatusMinOfflineTime_Type()
)
cwdxIfHeSuStatusMinOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusMinOfflineTime.setStatus("current")
_CwdxIfHeSuStatusAvgOfflineTime_Type = TimeInterval
_CwdxIfHeSuStatusAvgOfflineTime_Object = MibTableColumn
cwdxIfHeSuStatusAvgOfflineTime = _CwdxIfHeSuStatusAvgOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 8),
    _CwdxIfHeSuStatusAvgOfflineTime_Type()
)
cwdxIfHeSuStatusAvgOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusAvgOfflineTime.setStatus("current")
_CwdxIfHeSuStatusMaxOfflineTime_Type = TimeInterval
_CwdxIfHeSuStatusMaxOfflineTime_Object = MibTableColumn
cwdxIfHeSuStatusMaxOfflineTime = _CwdxIfHeSuStatusMaxOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 9),
    _CwdxIfHeSuStatusMaxOfflineTime_Type()
)
cwdxIfHeSuStatusMaxOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusMaxOfflineTime.setStatus("current")


class _CwdxIfHeSuStatusDynSidCount_Type(Integer32):
    """Custom type cwdxIfHeSuStatusDynSidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CwdxIfHeSuStatusDynSidCount_Type.__name__ = "Integer32"
_CwdxIfHeSuStatusDynSidCount_Object = MibTableColumn
cwdxIfHeSuStatusDynSidCount = _CwdxIfHeSuStatusDynSidCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 3, 1, 10),
    _CwdxIfHeSuStatusDynSidCount_Type()
)
cwdxIfHeSuStatusDynSidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxIfHeSuStatusDynSidCount.setStatus("current")
_CwdxHeMacExtTable_Object = MibTable
cwdxHeMacExtTable = _CwdxHeMacExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cwdxHeMacExtTable.setStatus("current")
_CwdxHeMacExtEntry_Object = MibTableRow
cwdxHeMacExtEntry = _CwdxHeMacExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cwdxHeMacExtEntry.setStatus("current")
_CwdxHeSuOnOffTrapEnable_Type = TruthValue
_CwdxHeSuOnOffTrapEnable_Object = MibTableColumn
cwdxHeSuOnOffTrapEnable = _CwdxHeSuOnOffTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4, 1, 1),
    _CwdxHeSuOnOffTrapEnable_Type()
)
cwdxHeSuOnOffTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxHeSuOnOffTrapEnable.setStatus("current")


class _CwdxHeSuOnOffTrapInterval_Type(Integer32):
    """Custom type cwdxHeSuOnOffTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CwdxHeSuOnOffTrapInterval_Type.__name__ = "Integer32"
_CwdxHeSuOnOffTrapInterval_Object = MibTableColumn
cwdxHeSuOnOffTrapInterval = _CwdxHeSuOnOffTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4, 1, 2),
    _CwdxHeSuOnOffTrapInterval_Type()
)
cwdxHeSuOnOffTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxHeSuOnOffTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwdxHeSuOnOffTrapInterval.setUnits("seconds")


class _CwdxHeSuDefaultMaxCpes_Type(Integer32):
    """Custom type cwdxHeSuDefaultMaxCpes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwdxHeSuDefaultMaxCpes_Type.__name__ = "Integer32"
_CwdxHeSuDefaultMaxCpes_Object = MibTableColumn
cwdxHeSuDefaultMaxCpes = _CwdxHeSuDefaultMaxCpes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4, 1, 3),
    _CwdxHeSuDefaultMaxCpes_Type()
)
cwdxHeSuDefaultMaxCpes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxHeSuDefaultMaxCpes.setStatus("current")


class _CwdxHeTotalSusRegistered_Type(Integer32):
    """Custom type cwdxHeTotalSusRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwdxHeTotalSusRegistered_Type.__name__ = "Integer32"
_CwdxHeTotalSusRegistered_Object = MibTableColumn
cwdxHeTotalSusRegistered = _CwdxHeTotalSusRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4, 1, 4),
    _CwdxHeTotalSusRegistered_Type()
)
cwdxHeTotalSusRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxHeTotalSusRegistered.setStatus("current")


class _CwdxHeTotalSusOffline_Type(Integer32):
    """Custom type cwdxHeTotalSusOffline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwdxHeTotalSusOffline_Type.__name__ = "Integer32"
_CwdxHeTotalSusOffline_Object = MibTableColumn
cwdxHeTotalSusOffline = _CwdxHeTotalSusOffline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 4, 1, 5),
    _CwdxHeTotalSusOffline_Type()
)
cwdxHeTotalSusOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxHeTotalSusOffline.setStatus("current")


class _CwdxHeSuChOverTimeExpiration_Type(Integer32):
    """Custom type cwdxHeSuChOverTimeExpiration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CwdxHeSuChOverTimeExpiration_Type.__name__ = "Integer32"
_CwdxHeSuChOverTimeExpiration_Object = MibScalar
cwdxHeSuChOverTimeExpiration = _CwdxHeSuChOverTimeExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 5),
    _CwdxHeSuChOverTimeExpiration_Type()
)
cwdxHeSuChOverTimeExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxHeSuChOverTimeExpiration.setStatus("current")
if mibBuilder.loadTexts:
    cwdxHeSuChOverTimeExpiration.setUnits("minutes")
_CwdxHeSuChOverTable_Object = MibTable
cwdxHeSuChOverTable = _CwdxHeSuChOverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cwdxHeSuChOverTable.setStatus("current")
_CwdxHeSuChOverEntry_Object = MibTableRow
cwdxHeSuChOverEntry = _CwdxHeSuChOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1)
)
cwdxHeSuChOverEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverSerialNumber"),
)
if mibBuilder.loadTexts:
    cwdxHeSuChOverEntry.setStatus("current")


class _CwdxHeSuChOverSerialNumber_Type(Integer32):
    """Custom type cwdxHeSuChOverSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwdxHeSuChOverSerialNumber_Type.__name__ = "Integer32"
_CwdxHeSuChOverSerialNumber_Object = MibTableColumn
cwdxHeSuChOverSerialNumber = _CwdxHeSuChOverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 1),
    _CwdxHeSuChOverSerialNumber_Type()
)
cwdxHeSuChOverSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdxHeSuChOverSerialNumber.setStatus("current")
_CwdxHeSuChOverMacAddress_Type = MacAddress
_CwdxHeSuChOverMacAddress_Object = MibTableColumn
cwdxHeSuChOverMacAddress = _CwdxHeSuChOverMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 2),
    _CwdxHeSuChOverMacAddress_Type()
)
cwdxHeSuChOverMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxHeSuChOverMacAddress.setStatus("current")


class _CwdxHeSuChOverDownFrequency_Type(Integer32):
    """Custom type cwdxHeSuChOverDownFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CwdxHeSuChOverDownFrequency_Type.__name__ = "Integer32"
_CwdxHeSuChOverDownFrequency_Object = MibTableColumn
cwdxHeSuChOverDownFrequency = _CwdxHeSuChOverDownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 3),
    _CwdxHeSuChOverDownFrequency_Type()
)
cwdxHeSuChOverDownFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxHeSuChOverDownFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwdxHeSuChOverDownFrequency.setUnits("hertz")


class _CwdxHeSuChOverUpChannelId_Type(Integer32):
    """Custom type cwdxHeSuChOverUpChannelId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CwdxHeSuChOverUpChannelId_Type.__name__ = "Integer32"
_CwdxHeSuChOverUpChannelId_Object = MibTableColumn
cwdxHeSuChOverUpChannelId = _CwdxHeSuChOverUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 4),
    _CwdxHeSuChOverUpChannelId_Type()
)
cwdxHeSuChOverUpChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxHeSuChOverUpChannelId.setStatus("current")


class _CwdxHeSuChOverTrapOnCompletion_Type(TruthValue):
    """Custom type cwdxHeSuChOverTrapOnCompletion based on TruthValue"""


_CwdxHeSuChOverTrapOnCompletion_Object = MibTableColumn
cwdxHeSuChOverTrapOnCompletion = _CwdxHeSuChOverTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 5),
    _CwdxHeSuChOverTrapOnCompletion_Type()
)
cwdxHeSuChOverTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxHeSuChOverTrapOnCompletion.setStatus("current")
_CwdxHeSuChOverOpInitiatedTime_Type = TimeStamp
_CwdxHeSuChOverOpInitiatedTime_Object = MibTableColumn
cwdxHeSuChOverOpInitiatedTime = _CwdxHeSuChOverOpInitiatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 6),
    _CwdxHeSuChOverOpInitiatedTime_Type()
)
cwdxHeSuChOverOpInitiatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxHeSuChOverOpInitiatedTime.setStatus("current")


class _CwdxHeSuChOverState_Type(Integer32):
    """Custom type cwdxHeSuChOverState based on Integer32"""
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
        *(("commandNotActive", 2),
          ("messageSent", 1),
          ("noOpNeeded", 3),
          ("suNotFound", 4),
          ("timeOut", 6),
          ("waitToSendMessage", 5))
    )


_CwdxHeSuChOverState_Type.__name__ = "Integer32"
_CwdxHeSuChOverState_Object = MibTableColumn
cwdxHeSuChOverState = _CwdxHeSuChOverState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 7),
    _CwdxHeSuChOverState_Type()
)
cwdxHeSuChOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdxHeSuChOverState.setStatus("current")
_CwdxHeSuChOverRowStatus_Type = RowStatus
_CwdxHeSuChOverRowStatus_Object = MibTableColumn
cwdxHeSuChOverRowStatus = _CwdxHeSuChOverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 6, 1, 8),
    _CwdxHeSuChOverRowStatus_Type()
)
cwdxHeSuChOverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxHeSuChOverRowStatus.setStatus("current")
_CwdxHeSuTable_Object = MibTable
cwdxHeSuTable = _CwdxHeSuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cwdxHeSuTable.setStatus("current")
_CwdxHeSuEntry_Object = MibTableRow
cwdxHeSuEntry = _CwdxHeSuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 7, 1)
)
cwdxHeSuEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusIndex"),
)
if mibBuilder.loadTexts:
    cwdxHeSuEntry.setStatus("current")


class _CwdxHeSuMaxCpeNumber_Type(Integer32):
    """Custom type cwdxHeSuMaxCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CwdxHeSuMaxCpeNumber_Type.__name__ = "Integer32"
_CwdxHeSuMaxCpeNumber_Object = MibTableColumn
cwdxHeSuMaxCpeNumber = _CwdxHeSuMaxCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 3, 7, 1, 1),
    _CwdxHeSuMaxCpeNumber_Type()
)
cwdxHeSuMaxCpeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxHeSuMaxCpeNumber.setStatus("current")
_CwdxQosProfileExtObjects_ObjectIdentity = ObjectIdentity
cwdxQosProfileExtObjects = _CwdxQosProfileExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4)
)
_CwdxQosProfileExtTable_Object = MibTable
cwdxQosProfileExtTable = _CwdxQosProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwdxQosProfileExtTable.setStatus("current")
_CwdxQosProfileExtEntry_Object = MibTableRow
cwdxQosProfileExtEntry = _CwdxQosProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cwdxQosProfileExtEntry.setStatus("current")


class _CwdxQosProfGrantInterval_Type(Integer32):
    """Custom type cwdxQosProfGrantInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwdxQosProfGrantInterval_Type.__name__ = "Integer32"
_CwdxQosProfGrantInterval_Object = MibTableColumn
cwdxQosProfGrantInterval = _CwdxQosProfGrantInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1, 1, 1),
    _CwdxQosProfGrantInterval_Type()
)
cwdxQosProfGrantInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxQosProfGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwdxQosProfGrantInterval.setUnits("milliseconds")


class _CwdxQosProfGrantSize_Type(Integer32):
    """Custom type cwdxQosProfGrantSize based on Integer32"""
    defaultValue = 229

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwdxQosProfGrantSize_Type.__name__ = "Integer32"
_CwdxQosProfGrantSize_Object = MibTableColumn
cwdxQosProfGrantSize = _CwdxQosProfGrantSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1, 1, 2),
    _CwdxQosProfGrantSize_Type()
)
cwdxQosProfGrantSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxQosProfGrantSize.setStatus("current")
if mibBuilder.loadTexts:
    cwdxQosProfGrantSize.setUnits("bytes")


class _CwdxQosProfName_Type(DisplayString):
    """Custom type cwdxQosProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwdxQosProfName_Type.__name__ = "DisplayString"
_CwdxQosProfName_Object = MibTableColumn
cwdxQosProfName = _CwdxQosProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1, 1, 3),
    _CwdxQosProfName_Type()
)
cwdxQosProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxQosProfName.setStatus("current")


class _CwdxQosProfTosOverwriteMask_Type(Integer32):
    """Custom type cwdxQosProfTosOverwriteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwdxQosProfTosOverwriteMask_Type.__name__ = "Integer32"
_CwdxQosProfTosOverwriteMask_Object = MibTableColumn
cwdxQosProfTosOverwriteMask = _CwdxQosProfTosOverwriteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1, 1, 4),
    _CwdxQosProfTosOverwriteMask_Type()
)
cwdxQosProfTosOverwriteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxQosProfTosOverwriteMask.setStatus("current")


class _CwdxQosProfTosOverwriteValue_Type(Integer32):
    """Custom type cwdxQosProfTosOverwriteValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwdxQosProfTosOverwriteValue_Type.__name__ = "Integer32"
_CwdxQosProfTosOverwriteValue_Object = MibTableColumn
cwdxQosProfTosOverwriteValue = _CwdxQosProfTosOverwriteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 1, 1, 5),
    _CwdxQosProfTosOverwriteValue_Type()
)
cwdxQosProfTosOverwriteValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdxQosProfTosOverwriteValue.setStatus("current")
_CwdxQosIpTosRatelimitTable_Object = MibTable
cwdxQosIpTosRatelimitTable = _CwdxQosIpTosRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cwdxQosIpTosRatelimitTable.setStatus("current")
_CwdxQosIpTosRatelimitEntry_Object = MibTableRow
cwdxQosIpTosRatelimitEntry = _CwdxQosIpTosRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 2, 1)
)
cwdxQosIpTosRatelimitEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfIndex"),
    (0, "CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosIpTosRatelimitIndex"),
)
if mibBuilder.loadTexts:
    cwdxQosIpTosRatelimitEntry.setStatus("current")


class _CwdxQosIpTosRatelimitIndex_Type(Integer32):
    """Custom type cwdxQosIpTosRatelimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CwdxQosIpTosRatelimitIndex_Type.__name__ = "Integer32"
_CwdxQosIpTosRatelimitIndex_Object = MibTableColumn
cwdxQosIpTosRatelimitIndex = _CwdxQosIpTosRatelimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 2, 1, 1),
    _CwdxQosIpTosRatelimitIndex_Type()
)
cwdxQosIpTosRatelimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdxQosIpTosRatelimitIndex.setStatus("current")


class _CwdxQosIpTosRatelimitMaxDownRate_Type(Integer32):
    """Custom type cwdxQosIpTosRatelimitMaxDownRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CwdxQosIpTosRatelimitMaxDownRate_Type.__name__ = "Integer32"
_CwdxQosIpTosRatelimitMaxDownRate_Object = MibTableColumn
cwdxQosIpTosRatelimitMaxDownRate = _CwdxQosIpTosRatelimitMaxDownRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 1, 4, 2, 1, 2),
    _CwdxQosIpTosRatelimitMaxDownRate_Type()
)
cwdxQosIpTosRatelimitMaxDownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdxQosIpTosRatelimitMaxDownRate.setStatus("current")
if mibBuilder.loadTexts:
    cwdxQosIpTosRatelimitMaxDownRate.setUnits("bps")
_CiscoWirelessDocsExtNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoWirelessDocsExtNotificationsPrefix = _CiscoWirelessDocsExtNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 2)
)
_CiscoWirelessDocsExtNotifications_ObjectIdentity = ObjectIdentity
ciscoWirelessDocsExtNotifications = _CiscoWirelessDocsExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 2, 0)
)
_CiscoWirelessDocsExtConformance_ObjectIdentity = ObjectIdentity
ciscoWirelessDocsExtConformance = _CiscoWirelessDocsExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3)
)
_CwdxDocsExtCompliances_ObjectIdentity = ObjectIdentity
cwdxDocsExtCompliances = _CwdxDocsExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3, 1)
)
_CwdxDocsExtGroups_ObjectIdentity = ObjectIdentity
cwdxDocsExtGroups = _CwdxDocsExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3, 2)
)
cwdIfHeServiceEntry.registerAugmentions(
    ("CISCO-WIRELESS-DOCS-EXT-MIB",
     "cwdxHeServiceExtEntry")
)
cwdxHeServiceExtEntry.setIndexNames(*cwdIfHeServiceEntry.getIndexNames())
cwdIfHeSuStatusEntry.registerAugmentions(
    ("CISCO-WIRELESS-DOCS-EXT-MIB",
     "cwdxHeSuStatusExtEntry")
)
cwdxHeSuStatusExtEntry.setIndexNames(*cwdIfHeSuStatusEntry.getIndexNames())
cwdIfHeMacEntry.registerAugmentions(
    ("CISCO-WIRELESS-DOCS-EXT-MIB",
     "cwdxHeMacExtEntry")
)
cwdxHeMacExtEntry.setIndexNames(*cwdIfHeMacEntry.getIndexNames())
cwdIfQosProfileEntry.registerAugmentions(
    ("CISCO-WIRELESS-DOCS-EXT-MIB",
     "cwdxQosProfileExtEntry")
)
cwdxQosProfileExtEntry.setIndexNames(*cwdIfQosProfileEntry.getIndexNames())

# Managed Objects groups

cwdxQosCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3, 2, 1)
)
cwdxQosCtrlGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosCtrlUpAdmissionRejects"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosCtrlUpReservedBW"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosIfRateLimitAlgo"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosIfRateLimitExpWgt"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosIfRateLimitShpMaxDelay"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosIfRateLimitShpGranularity"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeServiceOutOctets"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeServiceOutPackets"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosMaxUpBWExcessRequests"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosMaxDownBWExcessPackets"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosProfGrantInterval"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosProfGrantSize"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosProfName"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosProfTosOverwriteMask"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosProfTosOverwriteValue"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxQosIpTosRatelimitMaxDownRate"))
)
if mibBuilder.loadTexts:
    cwdxQosCtrlGroup.setStatus("current")

cwdxQosQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3, 2, 2)
)
cwdxQosQueueGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueOrder"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueNumServedBeforeYield"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueType"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueMaxDepth"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueDepth"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxBWQueueDiscards"))
)
if mibBuilder.loadTexts:
    cwdxQosQueueGroup.setStatus("current")

cwdxHeSuCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3, 2, 3)
)
cwdxHeSuCpeGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxCpeIpAddress"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxCpeAccessGroup"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxSuMappingStatusIndex"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuStatusValue"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusOnlineTimes"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusPercentOnline"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusMinOnlineTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusAvgOnlineTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusMaxOnlineTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusMinOfflineTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusAvgOfflineTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusMaxOfflineTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxIfHeSuStatusDynSidCount"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuOnOffTrapEnable"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuOnOffTrapInterval"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuDefaultMaxCpes"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeTotalSusRegistered"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeTotalSusOffline"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverTimeExpiration"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverMacAddress"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverDownFrequency"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverUpChannelId"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverTrapOnCompletion"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverOpInitiatedTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverState"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverRowStatus"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuMaxCpeNumber"))
)
if mibBuilder.loadTexts:
    cwdxHeSuCpeGroup.setStatus("current")


# Notification objects

cwdxHeSuOnOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 2, 0, 1)
)
cwdxHeSuOnOffNotification.setObjects(
      *(("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusMacAddress"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusIpAddress"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusDownChanIfIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusUpChanIfIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusServiceId"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuStatusValue"))
)
if mibBuilder.loadTexts:
    cwdxHeSuOnOffNotification.setStatus(
        "current"
    )

cwdxHeSuChOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 2, 0, 2)
)
cwdxHeSuChOverNotification.setObjects(
      *(("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverMacAddress"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverDownFrequency"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverUpChannelId"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverOpInitiatedTime"),
        ("CISCO-WIRELESS-DOCS-EXT-MIB", "cwdxHeSuChOverState"))
)
if mibBuilder.loadTexts:
    cwdxHeSuChOverNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cwdxDocsExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 169, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cwdxDocsExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-DOCS-EXT-MIB",
    **{"ciscoWirelessDocsExtMIB": ciscoWirelessDocsExtMIB,
       "ciscoWirelessDocsExtMIBObjects": ciscoWirelessDocsExtMIBObjects,
       "cwdxQosCtrlObjects": cwdxQosCtrlObjects,
       "cwdxQosCtrlUpTable": cwdxQosCtrlUpTable,
       "cwdxQosCtrlUpEntry": cwdxQosCtrlUpEntry,
       "cwdxQosCtrlUpAdmissionCtrl": cwdxQosCtrlUpAdmissionCtrl,
       "cwdxQosCtrlUpMaxRsvdBWPercent": cwdxQosCtrlUpMaxRsvdBWPercent,
       "cwdxQosCtrlUpAdmissionRejects": cwdxQosCtrlUpAdmissionRejects,
       "cwdxQosCtrlUpReservedBW": cwdxQosCtrlUpReservedBW,
       "cwdxQosCtrlUpMaxVirtualBW": cwdxQosCtrlUpMaxVirtualBW,
       "cwdxQosIfRateLimitTable": cwdxQosIfRateLimitTable,
       "cwdxQosIfRateLimitEntry": cwdxQosIfRateLimitEntry,
       "cwdxQosIfRateLimitAlgo": cwdxQosIfRateLimitAlgo,
       "cwdxQosIfRateLimitExpWgt": cwdxQosIfRateLimitExpWgt,
       "cwdxQosIfRateLimitShpMaxDelay": cwdxQosIfRateLimitShpMaxDelay,
       "cwdxQosIfRateLimitShpGranularity": cwdxQosIfRateLimitShpGranularity,
       "cwdxHeServiceExtTable": cwdxHeServiceExtTable,
       "cwdxHeServiceExtEntry": cwdxHeServiceExtEntry,
       "cwdxIfHeServiceOutOctets": cwdxIfHeServiceOutOctets,
       "cwdxIfHeServiceOutPackets": cwdxIfHeServiceOutPackets,
       "cwdxQosMaxUpBWExcessRequests": cwdxQosMaxUpBWExcessRequests,
       "cwdxQosMaxDownBWExcessPackets": cwdxQosMaxDownBWExcessPackets,
       "cwdxQosQueueObjects": cwdxQosQueueObjects,
       "cwdxBWQueueTable": cwdxBWQueueTable,
       "cwdxBWQueueEntry": cwdxBWQueueEntry,
       "cwdxBWQueueNameCode": cwdxBWQueueNameCode,
       "cwdxBWQueueOrder": cwdxBWQueueOrder,
       "cwdxBWQueueNumServedBeforeYield": cwdxBWQueueNumServedBeforeYield,
       "cwdxBWQueueType": cwdxBWQueueType,
       "cwdxBWQueueMaxDepth": cwdxBWQueueMaxDepth,
       "cwdxBWQueueDepth": cwdxBWQueueDepth,
       "cwdxBWQueueDiscards": cwdxBWQueueDiscards,
       "cwdxHeSuCpeObjects": cwdxHeSuCpeObjects,
       "cwdxCpeTable": cwdxCpeTable,
       "cwdxCpeEntry": cwdxCpeEntry,
       "cwdxCpeStatusIndex": cwdxCpeStatusIndex,
       "cwdxCpeMacAddress": cwdxCpeMacAddress,
       "cwdxCpeIpAddress": cwdxCpeIpAddress,
       "cwdxCpeAccessGroup": cwdxCpeAccessGroup,
       "cwdxSuMappingTable": cwdxSuMappingTable,
       "cwdxSuMappingEntry": cwdxSuMappingEntry,
       "cwdxSuMappingStatusIndex": cwdxSuMappingStatusIndex,
       "cwdxSuMappingMacAddress": cwdxSuMappingMacAddress,
       "cwdxHeSuStatusExtTable": cwdxHeSuStatusExtTable,
       "cwdxHeSuStatusExtEntry": cwdxHeSuStatusExtEntry,
       "cwdxHeSuStatusValue": cwdxHeSuStatusValue,
       "cwdxIfHeSuStatusOnlineTimes": cwdxIfHeSuStatusOnlineTimes,
       "cwdxIfHeSuStatusPercentOnline": cwdxIfHeSuStatusPercentOnline,
       "cwdxIfHeSuStatusMinOnlineTime": cwdxIfHeSuStatusMinOnlineTime,
       "cwdxIfHeSuStatusAvgOnlineTime": cwdxIfHeSuStatusAvgOnlineTime,
       "cwdxIfHeSuStatusMaxOnlineTime": cwdxIfHeSuStatusMaxOnlineTime,
       "cwdxIfHeSuStatusMinOfflineTime": cwdxIfHeSuStatusMinOfflineTime,
       "cwdxIfHeSuStatusAvgOfflineTime": cwdxIfHeSuStatusAvgOfflineTime,
       "cwdxIfHeSuStatusMaxOfflineTime": cwdxIfHeSuStatusMaxOfflineTime,
       "cwdxIfHeSuStatusDynSidCount": cwdxIfHeSuStatusDynSidCount,
       "cwdxHeMacExtTable": cwdxHeMacExtTable,
       "cwdxHeMacExtEntry": cwdxHeMacExtEntry,
       "cwdxHeSuOnOffTrapEnable": cwdxHeSuOnOffTrapEnable,
       "cwdxHeSuOnOffTrapInterval": cwdxHeSuOnOffTrapInterval,
       "cwdxHeSuDefaultMaxCpes": cwdxHeSuDefaultMaxCpes,
       "cwdxHeTotalSusRegistered": cwdxHeTotalSusRegistered,
       "cwdxHeTotalSusOffline": cwdxHeTotalSusOffline,
       "cwdxHeSuChOverTimeExpiration": cwdxHeSuChOverTimeExpiration,
       "cwdxHeSuChOverTable": cwdxHeSuChOverTable,
       "cwdxHeSuChOverEntry": cwdxHeSuChOverEntry,
       "cwdxHeSuChOverSerialNumber": cwdxHeSuChOverSerialNumber,
       "cwdxHeSuChOverMacAddress": cwdxHeSuChOverMacAddress,
       "cwdxHeSuChOverDownFrequency": cwdxHeSuChOverDownFrequency,
       "cwdxHeSuChOverUpChannelId": cwdxHeSuChOverUpChannelId,
       "cwdxHeSuChOverTrapOnCompletion": cwdxHeSuChOverTrapOnCompletion,
       "cwdxHeSuChOverOpInitiatedTime": cwdxHeSuChOverOpInitiatedTime,
       "cwdxHeSuChOverState": cwdxHeSuChOverState,
       "cwdxHeSuChOverRowStatus": cwdxHeSuChOverRowStatus,
       "cwdxHeSuTable": cwdxHeSuTable,
       "cwdxHeSuEntry": cwdxHeSuEntry,
       "cwdxHeSuMaxCpeNumber": cwdxHeSuMaxCpeNumber,
       "cwdxQosProfileExtObjects": cwdxQosProfileExtObjects,
       "cwdxQosProfileExtTable": cwdxQosProfileExtTable,
       "cwdxQosProfileExtEntry": cwdxQosProfileExtEntry,
       "cwdxQosProfGrantInterval": cwdxQosProfGrantInterval,
       "cwdxQosProfGrantSize": cwdxQosProfGrantSize,
       "cwdxQosProfName": cwdxQosProfName,
       "cwdxQosProfTosOverwriteMask": cwdxQosProfTosOverwriteMask,
       "cwdxQosProfTosOverwriteValue": cwdxQosProfTosOverwriteValue,
       "cwdxQosIpTosRatelimitTable": cwdxQosIpTosRatelimitTable,
       "cwdxQosIpTosRatelimitEntry": cwdxQosIpTosRatelimitEntry,
       "cwdxQosIpTosRatelimitIndex": cwdxQosIpTosRatelimitIndex,
       "cwdxQosIpTosRatelimitMaxDownRate": cwdxQosIpTosRatelimitMaxDownRate,
       "ciscoWirelessDocsExtNotificationsPrefix": ciscoWirelessDocsExtNotificationsPrefix,
       "ciscoWirelessDocsExtNotifications": ciscoWirelessDocsExtNotifications,
       "cwdxHeSuOnOffNotification": cwdxHeSuOnOffNotification,
       "cwdxHeSuChOverNotification": cwdxHeSuChOverNotification,
       "ciscoWirelessDocsExtConformance": ciscoWirelessDocsExtConformance,
       "cwdxDocsExtCompliances": cwdxDocsExtCompliances,
       "cwdxDocsExtCompliance": cwdxDocsExtCompliance,
       "cwdxDocsExtGroups": cwdxDocsExtGroups,
       "cwdxQosCtrlGroup": cwdxQosCtrlGroup,
       "cwdxQosQueueGroup": cwdxQosQueueGroup,
       "cwdxHeSuCpeGroup": cwdxHeSuCpeGroup}
)
