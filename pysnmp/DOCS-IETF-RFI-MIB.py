# SNMP MIB module (DOCS-IETF-RFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IETF-RFI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:40 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

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

docsIfMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127)
)
docsIfMib.setRevisions(
        ("2003-03-02 00:00",
         "1999-08-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class TenthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class DocsisVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("docsis10", 1),
          ("docsis11", 2),
          ("docsis20", 3))
    )



class DocsisQosVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docsis10", 1),
          ("docsis11", 2))
    )



class DocsisUpstreamType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atdma", 2),
          ("scdma", 3),
          ("tdma", 1),
          ("tdmaAndAtdma", 4),
          ("unknown", 0))
    )



class DocsisUpstreamTypeStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atdma", 2),
          ("scdma", 3),
          ("tdma", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_DocsIfMibObjects_ObjectIdentity = ObjectIdentity
docsIfMibObjects = _DocsIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 1)
)
_DocsIfBaseObjects_ObjectIdentity = ObjectIdentity
docsIfBaseObjects = _DocsIfBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1)
)
_DocsIfDownstreamChannelTable_Object = MibTable
docsIfDownstreamChannelTable = _DocsIfDownstreamChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfDownstreamChannelTable.setStatus("current")
_DocsIfDownstreamChannelEntry_Object = MibTableRow
docsIfDownstreamChannelEntry = _DocsIfDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1)
)
docsIfDownstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfDownstreamChannelEntry.setStatus("current")


class _DocsIfDownChannelId_Type(Integer32):
    """Custom type docsIfDownChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfDownChannelId_Type.__name__ = "Integer32"
_DocsIfDownChannelId_Object = MibTableColumn
docsIfDownChannelId = _DocsIfDownChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 1),
    _DocsIfDownChannelId_Type()
)
docsIfDownChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfDownChannelId.setStatus("current")


class _DocsIfDownChannelFrequency_Type(Integer32):
    """Custom type docsIfDownChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DocsIfDownChannelFrequency_Type.__name__ = "Integer32"
_DocsIfDownChannelFrequency_Object = MibTableColumn
docsIfDownChannelFrequency = _DocsIfDownChannelFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 2),
    _DocsIfDownChannelFrequency_Type()
)
docsIfDownChannelFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfDownChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIfDownChannelFrequency.setUnits("hertz")


class _DocsIfDownChannelWidth_Type(Integer32):
    """Custom type docsIfDownChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_DocsIfDownChannelWidth_Type.__name__ = "Integer32"
_DocsIfDownChannelWidth_Object = MibTableColumn
docsIfDownChannelWidth = _DocsIfDownChannelWidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 3),
    _DocsIfDownChannelWidth_Type()
)
docsIfDownChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfDownChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    docsIfDownChannelWidth.setUnits("hertz")


class _DocsIfDownChannelModulation_Type(Integer32):
    """Custom type docsIfDownChannelModulation based on Integer32"""
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


_DocsIfDownChannelModulation_Type.__name__ = "Integer32"
_DocsIfDownChannelModulation_Object = MibTableColumn
docsIfDownChannelModulation = _DocsIfDownChannelModulation_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 4),
    _DocsIfDownChannelModulation_Type()
)
docsIfDownChannelModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfDownChannelModulation.setStatus("current")


class _DocsIfDownChannelInterleave_Type(Integer32):
    """Custom type docsIfDownChannelInterleave based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("taps128Increment1", 7),
          ("taps12increment17", 8),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps8Increment16", 3),
          ("unknown", 1))
    )


_DocsIfDownChannelInterleave_Type.__name__ = "Integer32"
_DocsIfDownChannelInterleave_Object = MibTableColumn
docsIfDownChannelInterleave = _DocsIfDownChannelInterleave_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 5),
    _DocsIfDownChannelInterleave_Type()
)
docsIfDownChannelInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfDownChannelInterleave.setStatus("current")
_DocsIfDownChannelPower_Type = TenthdBmV
_DocsIfDownChannelPower_Object = MibTableColumn
docsIfDownChannelPower = _DocsIfDownChannelPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 6),
    _DocsIfDownChannelPower_Type()
)
docsIfDownChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfDownChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIfDownChannelPower.setUnits("dBmV")


class _DocsIfDownChannelAnnex_Type(Integer32):
    """Custom type docsIfDownChannelAnnex based on Integer32"""
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


_DocsIfDownChannelAnnex_Type.__name__ = "Integer32"
_DocsIfDownChannelAnnex_Object = MibTableColumn
docsIfDownChannelAnnex = _DocsIfDownChannelAnnex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 7),
    _DocsIfDownChannelAnnex_Type()
)
docsIfDownChannelAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfDownChannelAnnex.setStatus("current")
_DocsIfUpstreamChannelTable_Object = MibTable
docsIfUpstreamChannelTable = _DocsIfUpstreamChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsIfUpstreamChannelTable.setStatus("current")
_DocsIfUpstreamChannelEntry_Object = MibTableRow
docsIfUpstreamChannelEntry = _DocsIfUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1)
)
docsIfUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfUpstreamChannelEntry.setStatus("current")


class _DocsIfUpChannelId_Type(Integer32):
    """Custom type docsIfUpChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfUpChannelId_Type.__name__ = "Integer32"
_DocsIfUpChannelId_Object = MibTableColumn
docsIfUpChannelId = _DocsIfUpChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 1),
    _DocsIfUpChannelId_Type()
)
docsIfUpChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfUpChannelId.setStatus("current")


class _DocsIfUpChannelFrequency_Type(Integer32):
    """Custom type docsIfUpChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DocsIfUpChannelFrequency_Type.__name__ = "Integer32"
_DocsIfUpChannelFrequency_Object = MibTableColumn
docsIfUpChannelFrequency = _DocsIfUpChannelFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 2),
    _DocsIfUpChannelFrequency_Type()
)
docsIfUpChannelFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIfUpChannelFrequency.setUnits("hertz")


class _DocsIfUpChannelWidth_Type(Integer32):
    """Custom type docsIfUpChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000000),
    )


_DocsIfUpChannelWidth_Type.__name__ = "Integer32"
_DocsIfUpChannelWidth_Object = MibTableColumn
docsIfUpChannelWidth = _DocsIfUpChannelWidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 3),
    _DocsIfUpChannelWidth_Type()
)
docsIfUpChannelWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    docsIfUpChannelWidth.setUnits("hertz")
_DocsIfUpChannelModulationProfile_Type = Unsigned32
_DocsIfUpChannelModulationProfile_Object = MibTableColumn
docsIfUpChannelModulationProfile = _DocsIfUpChannelModulationProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 4),
    _DocsIfUpChannelModulationProfile_Type()
)
docsIfUpChannelModulationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelModulationProfile.setStatus("current")
_DocsIfUpChannelSlotSize_Type = Unsigned32
_DocsIfUpChannelSlotSize_Object = MibTableColumn
docsIfUpChannelSlotSize = _DocsIfUpChannelSlotSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 5),
    _DocsIfUpChannelSlotSize_Type()
)
docsIfUpChannelSlotSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelSlotSize.setStatus("current")
_DocsIfUpChannelTxTimingOffset_Type = Unsigned32
_DocsIfUpChannelTxTimingOffset_Object = MibTableColumn
docsIfUpChannelTxTimingOffset = _DocsIfUpChannelTxTimingOffset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 6),
    _DocsIfUpChannelTxTimingOffset_Type()
)
docsIfUpChannelTxTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfUpChannelTxTimingOffset.setStatus("current")


class _DocsIfUpChannelRangingBackoffStart_Type(Integer32):
    """Custom type docsIfUpChannelRangingBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIfUpChannelRangingBackoffStart_Type.__name__ = "Integer32"
_DocsIfUpChannelRangingBackoffStart_Object = MibTableColumn
docsIfUpChannelRangingBackoffStart = _DocsIfUpChannelRangingBackoffStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 7),
    _DocsIfUpChannelRangingBackoffStart_Type()
)
docsIfUpChannelRangingBackoffStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelRangingBackoffStart.setStatus("current")


class _DocsIfUpChannelRangingBackoffEnd_Type(Integer32):
    """Custom type docsIfUpChannelRangingBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIfUpChannelRangingBackoffEnd_Type.__name__ = "Integer32"
_DocsIfUpChannelRangingBackoffEnd_Object = MibTableColumn
docsIfUpChannelRangingBackoffEnd = _DocsIfUpChannelRangingBackoffEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 8),
    _DocsIfUpChannelRangingBackoffEnd_Type()
)
docsIfUpChannelRangingBackoffEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelRangingBackoffEnd.setStatus("current")


class _DocsIfUpChannelTxBackoffStart_Type(Integer32):
    """Custom type docsIfUpChannelTxBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIfUpChannelTxBackoffStart_Type.__name__ = "Integer32"
_DocsIfUpChannelTxBackoffStart_Object = MibTableColumn
docsIfUpChannelTxBackoffStart = _DocsIfUpChannelTxBackoffStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 9),
    _DocsIfUpChannelTxBackoffStart_Type()
)
docsIfUpChannelTxBackoffStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelTxBackoffStart.setStatus("current")


class _DocsIfUpChannelTxBackoffEnd_Type(Integer32):
    """Custom type docsIfUpChannelTxBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIfUpChannelTxBackoffEnd_Type.__name__ = "Integer32"
_DocsIfUpChannelTxBackoffEnd_Object = MibTableColumn
docsIfUpChannelTxBackoffEnd = _DocsIfUpChannelTxBackoffEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 10),
    _DocsIfUpChannelTxBackoffEnd_Type()
)
docsIfUpChannelTxBackoffEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelTxBackoffEnd.setStatus("current")


class _DocsIfUpChannelScdmaActiveCodes_Type(Unsigned32):
    """Custom type docsIfUpChannelScdmaActiveCodes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 128),
    )


_DocsIfUpChannelScdmaActiveCodes_Type.__name__ = "Unsigned32"
_DocsIfUpChannelScdmaActiveCodes_Object = MibTableColumn
docsIfUpChannelScdmaActiveCodes = _DocsIfUpChannelScdmaActiveCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 11),
    _DocsIfUpChannelScdmaActiveCodes_Type()
)
docsIfUpChannelScdmaActiveCodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelScdmaActiveCodes.setStatus("current")


class _DocsIfUpChannelScdmaCodesPerSlot_Type(Integer32):
    """Custom type docsIfUpChannelScdmaCodesPerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 32),
    )


_DocsIfUpChannelScdmaCodesPerSlot_Type.__name__ = "Integer32"
_DocsIfUpChannelScdmaCodesPerSlot_Object = MibTableColumn
docsIfUpChannelScdmaCodesPerSlot = _DocsIfUpChannelScdmaCodesPerSlot_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 12),
    _DocsIfUpChannelScdmaCodesPerSlot_Type()
)
docsIfUpChannelScdmaCodesPerSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelScdmaCodesPerSlot.setStatus("current")


class _DocsIfUpChannelScdmaFrameSize_Type(Unsigned32):
    """Custom type docsIfUpChannelScdmaFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DocsIfUpChannelScdmaFrameSize_Type.__name__ = "Unsigned32"
_DocsIfUpChannelScdmaFrameSize_Object = MibTableColumn
docsIfUpChannelScdmaFrameSize = _DocsIfUpChannelScdmaFrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 13),
    _DocsIfUpChannelScdmaFrameSize_Type()
)
docsIfUpChannelScdmaFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelScdmaFrameSize.setStatus("current")


class _DocsIfUpChannelScdmaHoppingSeed_Type(Unsigned32):
    """Custom type docsIfUpChannelScdmaHoppingSeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_DocsIfUpChannelScdmaHoppingSeed_Type.__name__ = "Unsigned32"
_DocsIfUpChannelScdmaHoppingSeed_Object = MibTableColumn
docsIfUpChannelScdmaHoppingSeed = _DocsIfUpChannelScdmaHoppingSeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 14),
    _DocsIfUpChannelScdmaHoppingSeed_Type()
)
docsIfUpChannelScdmaHoppingSeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelScdmaHoppingSeed.setStatus("current")
_DocsIfUpChannelType_Type = DocsisUpstreamType
_DocsIfUpChannelType_Object = MibTableColumn
docsIfUpChannelType = _DocsIfUpChannelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 15),
    _DocsIfUpChannelType_Type()
)
docsIfUpChannelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelType.setStatus("current")
_DocsIfUpChannelCloneFrom_Type = InterfaceIndexOrZero
_DocsIfUpChannelCloneFrom_Object = MibTableColumn
docsIfUpChannelCloneFrom = _DocsIfUpChannelCloneFrom_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 16),
    _DocsIfUpChannelCloneFrom_Type()
)
docsIfUpChannelCloneFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelCloneFrom.setStatus("current")
_DocsIfUpChannelUpdate_Type = TruthValue
_DocsIfUpChannelUpdate_Object = MibTableColumn
docsIfUpChannelUpdate = _DocsIfUpChannelUpdate_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 17),
    _DocsIfUpChannelUpdate_Type()
)
docsIfUpChannelUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelUpdate.setStatus("current")
_DocsIfUpChannelStatus_Type = RowStatus
_DocsIfUpChannelStatus_Object = MibTableColumn
docsIfUpChannelStatus = _DocsIfUpChannelStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 18),
    _DocsIfUpChannelStatus_Type()
)
docsIfUpChannelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelStatus.setStatus("current")
_DocsIfUpChannelPreEqEnable_Type = TruthValue
_DocsIfUpChannelPreEqEnable_Object = MibTableColumn
docsIfUpChannelPreEqEnable = _DocsIfUpChannelPreEqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 19),
    _DocsIfUpChannelPreEqEnable_Type()
)
docsIfUpChannelPreEqEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfUpChannelPreEqEnable.setStatus("current")
_DocsIfQosProfileTable_Object = MibTable
docsIfQosProfileTable = _DocsIfQosProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3)
)
if mibBuilder.loadTexts:
    docsIfQosProfileTable.setStatus("current")
_DocsIfQosProfileEntry_Object = MibTableRow
docsIfQosProfileEntry = _DocsIfQosProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1)
)
docsIfQosProfileEntry.setIndexNames(
    (0, "DOCS-IETF-RFI-MIB", "docsIfQosProfIndex"),
)
if mibBuilder.loadTexts:
    docsIfQosProfileEntry.setStatus("current")


class _DocsIfQosProfIndex_Type(Integer32):
    """Custom type docsIfQosProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsIfQosProfIndex_Type.__name__ = "Integer32"
_DocsIfQosProfIndex_Object = MibTableColumn
docsIfQosProfIndex = _DocsIfQosProfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 1),
    _DocsIfQosProfIndex_Type()
)
docsIfQosProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfQosProfIndex.setStatus("current")


class _DocsIfQosProfPriority_Type(Integer32):
    """Custom type docsIfQosProfPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsIfQosProfPriority_Type.__name__ = "Integer32"
_DocsIfQosProfPriority_Object = MibTableColumn
docsIfQosProfPriority = _DocsIfQosProfPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 2),
    _DocsIfQosProfPriority_Type()
)
docsIfQosProfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfPriority.setStatus("current")


class _DocsIfQosProfMaxUpBandwidth_Type(Integer32):
    """Custom type docsIfQosProfMaxUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_DocsIfQosProfMaxUpBandwidth_Type.__name__ = "Integer32"
_DocsIfQosProfMaxUpBandwidth_Object = MibTableColumn
docsIfQosProfMaxUpBandwidth = _DocsIfQosProfMaxUpBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 3),
    _DocsIfQosProfMaxUpBandwidth_Type()
)
docsIfQosProfMaxUpBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfMaxUpBandwidth.setStatus("current")


class _DocsIfQosProfGuarUpBandwidth_Type(Integer32):
    """Custom type docsIfQosProfGuarUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_DocsIfQosProfGuarUpBandwidth_Type.__name__ = "Integer32"
_DocsIfQosProfGuarUpBandwidth_Object = MibTableColumn
docsIfQosProfGuarUpBandwidth = _DocsIfQosProfGuarUpBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 4),
    _DocsIfQosProfGuarUpBandwidth_Type()
)
docsIfQosProfGuarUpBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfGuarUpBandwidth.setStatus("current")


class _DocsIfQosProfMaxDownBandwidth_Type(Integer32):
    """Custom type docsIfQosProfMaxDownBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_DocsIfQosProfMaxDownBandwidth_Type.__name__ = "Integer32"
_DocsIfQosProfMaxDownBandwidth_Object = MibTableColumn
docsIfQosProfMaxDownBandwidth = _DocsIfQosProfMaxDownBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 5),
    _DocsIfQosProfMaxDownBandwidth_Type()
)
docsIfQosProfMaxDownBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfMaxDownBandwidth.setStatus("current")


class _DocsIfQosProfMaxTxBurst_Type(Integer32):
    """Custom type docsIfQosProfMaxTxBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfQosProfMaxTxBurst_Type.__name__ = "Integer32"
_DocsIfQosProfMaxTxBurst_Object = MibTableColumn
docsIfQosProfMaxTxBurst = _DocsIfQosProfMaxTxBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 6),
    _DocsIfQosProfMaxTxBurst_Type()
)
docsIfQosProfMaxTxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfMaxTxBurst.setStatus("deprecated")


class _DocsIfQosProfBaselinePrivacy_Type(TruthValue):
    """Custom type docsIfQosProfBaselinePrivacy based on TruthValue"""


_DocsIfQosProfBaselinePrivacy_Object = MibTableColumn
docsIfQosProfBaselinePrivacy = _DocsIfQosProfBaselinePrivacy_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 7),
    _DocsIfQosProfBaselinePrivacy_Type()
)
docsIfQosProfBaselinePrivacy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfBaselinePrivacy.setStatus("current")
_DocsIfQosProfStatus_Type = RowStatus
_DocsIfQosProfStatus_Object = MibTableColumn
docsIfQosProfStatus = _DocsIfQosProfStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 8),
    _DocsIfQosProfStatus_Type()
)
docsIfQosProfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfStatus.setStatus("current")


class _DocsIfQosProfMaxTransmitBurst_Type(Integer32):
    """Custom type docsIfQosProfMaxTransmitBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIfQosProfMaxTransmitBurst_Type.__name__ = "Integer32"
_DocsIfQosProfMaxTransmitBurst_Object = MibTableColumn
docsIfQosProfMaxTransmitBurst = _DocsIfQosProfMaxTransmitBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 9),
    _DocsIfQosProfMaxTransmitBurst_Type()
)
docsIfQosProfMaxTransmitBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfQosProfMaxTransmitBurst.setStatus("current")
_DocsIfSignalQualityTable_Object = MibTable
docsIfSignalQualityTable = _DocsIfSignalQualityTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsIfSignalQualityTable.setStatus("current")
_DocsIfSignalQualityEntry_Object = MibTableRow
docsIfSignalQualityEntry = _DocsIfSignalQualityEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1)
)
docsIfSignalQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfSignalQualityEntry.setStatus("current")
_DocsIfSigQIncludesContention_Type = TruthValue
_DocsIfSigQIncludesContention_Object = MibTableColumn
docsIfSigQIncludesContention = _DocsIfSigQIncludesContention_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 1),
    _DocsIfSigQIncludesContention_Type()
)
docsIfSigQIncludesContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQIncludesContention.setStatus("current")
_DocsIfSigQUnerroreds_Type = Counter32
_DocsIfSigQUnerroreds_Object = MibTableColumn
docsIfSigQUnerroreds = _DocsIfSigQUnerroreds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 2),
    _DocsIfSigQUnerroreds_Type()
)
docsIfSigQUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQUnerroreds.setStatus("current")
_DocsIfSigQCorrecteds_Type = Counter32
_DocsIfSigQCorrecteds_Object = MibTableColumn
docsIfSigQCorrecteds = _DocsIfSigQCorrecteds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 3),
    _DocsIfSigQCorrecteds_Type()
)
docsIfSigQCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQCorrecteds.setStatus("current")
_DocsIfSigQUncorrectables_Type = Counter32
_DocsIfSigQUncorrectables_Object = MibTableColumn
docsIfSigQUncorrectables = _DocsIfSigQUncorrectables_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 4),
    _DocsIfSigQUncorrectables_Type()
)
docsIfSigQUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQUncorrectables.setStatus("current")
_DocsIfSigQSignalNoise_Type = TenthdB
_DocsIfSigQSignalNoise_Object = MibTableColumn
docsIfSigQSignalNoise = _DocsIfSigQSignalNoise_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 5),
    _DocsIfSigQSignalNoise_Type()
)
docsIfSigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    docsIfSigQSignalNoise.setUnits("dB")


class _DocsIfSigQMicroreflections_Type(Integer32):
    """Custom type docsIfSigQMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfSigQMicroreflections_Type.__name__ = "Integer32"
_DocsIfSigQMicroreflections_Object = MibTableColumn
docsIfSigQMicroreflections = _DocsIfSigQMicroreflections_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 6),
    _DocsIfSigQMicroreflections_Type()
)
docsIfSigQMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    docsIfSigQMicroreflections.setUnits("dBc")


class _DocsIfSigQEqualizationData_Type(OctetString):
    """Custom type docsIfSigQEqualizationData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DocsIfSigQEqualizationData_Type.__name__ = "OctetString"
_DocsIfSigQEqualizationData_Object = MibTableColumn
docsIfSigQEqualizationData = _DocsIfSigQEqualizationData_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 7),
    _DocsIfSigQEqualizationData_Type()
)
docsIfSigQEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQEqualizationData.setStatus("current")
_DocsIfSigQExtUnerroreds_Type = Counter64
_DocsIfSigQExtUnerroreds_Object = MibTableColumn
docsIfSigQExtUnerroreds = _DocsIfSigQExtUnerroreds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 8),
    _DocsIfSigQExtUnerroreds_Type()
)
docsIfSigQExtUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQExtUnerroreds.setStatus("current")
_DocsIfSigQExtCorrecteds_Type = Counter64
_DocsIfSigQExtCorrecteds_Object = MibTableColumn
docsIfSigQExtCorrecteds = _DocsIfSigQExtCorrecteds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 9),
    _DocsIfSigQExtCorrecteds_Type()
)
docsIfSigQExtCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQExtCorrecteds.setStatus("current")
_DocsIfSigQExtUncorrectables_Type = Counter64
_DocsIfSigQExtUncorrectables_Object = MibTableColumn
docsIfSigQExtUncorrectables = _DocsIfSigQExtUncorrectables_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 10),
    _DocsIfSigQExtUncorrectables_Type()
)
docsIfSigQExtUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfSigQExtUncorrectables.setStatus("current")
_DocsIfDocsisBaseCapability_Type = DocsisVersion
_DocsIfDocsisBaseCapability_Object = MibScalar
docsIfDocsisBaseCapability = _DocsIfDocsisBaseCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 5),
    _DocsIfDocsisBaseCapability_Type()
)
docsIfDocsisBaseCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfDocsisBaseCapability.setStatus("current")
_DocsIfCmObjects_ObjectIdentity = ObjectIdentity
docsIfCmObjects = _DocsIfCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2)
)
_DocsIfCmMacTable_Object = MibTable
docsIfCmMacTable = _DocsIfCmMacTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsIfCmMacTable.setStatus("current")
_DocsIfCmMacEntry_Object = MibTableRow
docsIfCmMacEntry = _DocsIfCmMacEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1)
)
docsIfCmMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmMacEntry.setStatus("current")
_DocsIfCmCmtsAddress_Type = MacAddress
_DocsIfCmCmtsAddress_Object = MibTableColumn
docsIfCmCmtsAddress = _DocsIfCmCmtsAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 1),
    _DocsIfCmCmtsAddress_Type()
)
docsIfCmCmtsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmCmtsAddress.setStatus("current")


class _DocsIfCmCapabilities_Type(Bits):
    """Custom type docsIfCmCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("atmCells", 0),
          ("concatenation", 1))
    )

_DocsIfCmCapabilities_Type.__name__ = "Bits"
_DocsIfCmCapabilities_Object = MibTableColumn
docsIfCmCapabilities = _DocsIfCmCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 2),
    _DocsIfCmCapabilities_Type()
)
docsIfCmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmCapabilities.setStatus("current")


class _DocsIfCmRangingRespTimeout_Type(TimeTicks):
    """Custom type docsIfCmRangingRespTimeout based on TimeTicks"""
    defaultValue = 20


_DocsIfCmRangingRespTimeout_Object = MibTableColumn
docsIfCmRangingRespTimeout = _DocsIfCmRangingRespTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 3),
    _DocsIfCmRangingRespTimeout_Type()
)
docsIfCmRangingRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmRangingRespTimeout.setStatus("obsolete")


class _DocsIfCmRangingTimeout_Type(TimeInterval):
    """Custom type docsIfCmRangingTimeout based on TimeInterval"""
    defaultValue = 20


_DocsIfCmRangingTimeout_Object = MibTableColumn
docsIfCmRangingTimeout = _DocsIfCmRangingTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 4),
    _DocsIfCmRangingTimeout_Type()
)
docsIfCmRangingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmRangingTimeout.setStatus("current")
_DocsIfCmStatusTable_Object = MibTable
docsIfCmStatusTable = _DocsIfCmStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsIfCmStatusTable.setStatus("current")
_DocsIfCmStatusEntry_Object = MibTableRow
docsIfCmStatusEntry = _DocsIfCmStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1)
)
docsIfCmStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmStatusEntry.setStatus("current")


class _DocsIfCmStatusValue_Type(Integer32):
    """Custom type docsIfCmStatusValue based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 13),
          ("ipComplete", 7),
          ("notReady", 2),
          ("notSynchronized", 3),
          ("operational", 12),
          ("other", 1),
          ("paramTransferComplete", 10),
          ("phySynchronized", 4),
          ("rangingComplete", 6),
          ("registrationComplete", 11),
          ("securityEstablished", 9),
          ("todEstablished", 8),
          ("usParametersAcquired", 5))
    )


_DocsIfCmStatusValue_Type.__name__ = "Integer32"
_DocsIfCmStatusValue_Object = MibTableColumn
docsIfCmStatusValue = _DocsIfCmStatusValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 1),
    _DocsIfCmStatusValue_Type()
)
docsIfCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusValue.setStatus("current")


class _DocsIfCmStatusCode_Type(OctetString):
    """Custom type docsIfCmStatusCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DocsIfCmStatusCode_Type.__name__ = "OctetString"
_DocsIfCmStatusCode_Object = MibTableColumn
docsIfCmStatusCode = _DocsIfCmStatusCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 2),
    _DocsIfCmStatusCode_Type()
)
docsIfCmStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusCode.setStatus("current")
_DocsIfCmStatusTxPower_Type = TenthdBmV
_DocsIfCmStatusTxPower_Object = MibTableColumn
docsIfCmStatusTxPower = _DocsIfCmStatusTxPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 3),
    _DocsIfCmStatusTxPower_Type()
)
docsIfCmStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusTxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmStatusTxPower.setUnits("dBmV")
_DocsIfCmStatusResets_Type = Counter32
_DocsIfCmStatusResets_Object = MibTableColumn
docsIfCmStatusResets = _DocsIfCmStatusResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 4),
    _DocsIfCmStatusResets_Type()
)
docsIfCmStatusResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusResets.setStatus("current")
_DocsIfCmStatusLostSyncs_Type = Counter32
_DocsIfCmStatusLostSyncs_Object = MibTableColumn
docsIfCmStatusLostSyncs = _DocsIfCmStatusLostSyncs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 5),
    _DocsIfCmStatusLostSyncs_Type()
)
docsIfCmStatusLostSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusLostSyncs.setStatus("current")
_DocsIfCmStatusInvalidMaps_Type = Counter32
_DocsIfCmStatusInvalidMaps_Object = MibTableColumn
docsIfCmStatusInvalidMaps = _DocsIfCmStatusInvalidMaps_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 6),
    _DocsIfCmStatusInvalidMaps_Type()
)
docsIfCmStatusInvalidMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusInvalidMaps.setStatus("current")
_DocsIfCmStatusInvalidUcds_Type = Counter32
_DocsIfCmStatusInvalidUcds_Object = MibTableColumn
docsIfCmStatusInvalidUcds = _DocsIfCmStatusInvalidUcds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 7),
    _DocsIfCmStatusInvalidUcds_Type()
)
docsIfCmStatusInvalidUcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusInvalidUcds.setStatus("current")
_DocsIfCmStatusInvalidRangingResponses_Type = Counter32
_DocsIfCmStatusInvalidRangingResponses_Object = MibTableColumn
docsIfCmStatusInvalidRangingResponses = _DocsIfCmStatusInvalidRangingResponses_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 8),
    _DocsIfCmStatusInvalidRangingResponses_Type()
)
docsIfCmStatusInvalidRangingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusInvalidRangingResponses.setStatus("current")
_DocsIfCmStatusInvalidRegistrationResponses_Type = Counter32
_DocsIfCmStatusInvalidRegistrationResponses_Object = MibTableColumn
docsIfCmStatusInvalidRegistrationResponses = _DocsIfCmStatusInvalidRegistrationResponses_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 9),
    _DocsIfCmStatusInvalidRegistrationResponses_Type()
)
docsIfCmStatusInvalidRegistrationResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusInvalidRegistrationResponses.setStatus("current")
_DocsIfCmStatusT1Timeouts_Type = Counter32
_DocsIfCmStatusT1Timeouts_Object = MibTableColumn
docsIfCmStatusT1Timeouts = _DocsIfCmStatusT1Timeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 10),
    _DocsIfCmStatusT1Timeouts_Type()
)
docsIfCmStatusT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusT1Timeouts.setStatus("current")
_DocsIfCmStatusT2Timeouts_Type = Counter32
_DocsIfCmStatusT2Timeouts_Object = MibTableColumn
docsIfCmStatusT2Timeouts = _DocsIfCmStatusT2Timeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 11),
    _DocsIfCmStatusT2Timeouts_Type()
)
docsIfCmStatusT2Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusT2Timeouts.setStatus("current")
_DocsIfCmStatusT3Timeouts_Type = Counter32
_DocsIfCmStatusT3Timeouts_Object = MibTableColumn
docsIfCmStatusT3Timeouts = _DocsIfCmStatusT3Timeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 12),
    _DocsIfCmStatusT3Timeouts_Type()
)
docsIfCmStatusT3Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusT3Timeouts.setStatus("current")
_DocsIfCmStatusT4Timeouts_Type = Counter32
_DocsIfCmStatusT4Timeouts_Object = MibTableColumn
docsIfCmStatusT4Timeouts = _DocsIfCmStatusT4Timeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 13),
    _DocsIfCmStatusT4Timeouts_Type()
)
docsIfCmStatusT4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusT4Timeouts.setStatus("current")
_DocsIfCmStatusRangingAborteds_Type = Counter32
_DocsIfCmStatusRangingAborteds_Object = MibTableColumn
docsIfCmStatusRangingAborteds = _DocsIfCmStatusRangingAborteds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 14),
    _DocsIfCmStatusRangingAborteds_Type()
)
docsIfCmStatusRangingAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusRangingAborteds.setStatus("current")
_DocsIfCmStatusDocsisOperMode_Type = DocsisQosVersion
_DocsIfCmStatusDocsisOperMode_Object = MibTableColumn
docsIfCmStatusDocsisOperMode = _DocsIfCmStatusDocsisOperMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 15),
    _DocsIfCmStatusDocsisOperMode_Type()
)
docsIfCmStatusDocsisOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusDocsisOperMode.setStatus("current")
_DocsIfCmStatusModulationType_Type = DocsisUpstreamTypeStatus
_DocsIfCmStatusModulationType_Object = MibTableColumn
docsIfCmStatusModulationType = _DocsIfCmStatusModulationType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 16),
    _DocsIfCmStatusModulationType_Type()
)
docsIfCmStatusModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusModulationType.setStatus("current")


class _DocsIfCmStatusEqualizationData_Type(OctetString):
    """Custom type docsIfCmStatusEqualizationData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DocsIfCmStatusEqualizationData_Type.__name__ = "OctetString"
_DocsIfCmStatusEqualizationData_Object = MibTableColumn
docsIfCmStatusEqualizationData = _DocsIfCmStatusEqualizationData_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 17),
    _DocsIfCmStatusEqualizationData_Type()
)
docsIfCmStatusEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmStatusEqualizationData.setStatus("current")
_DocsIfCmServiceTable_Object = MibTable
docsIfCmServiceTable = _DocsIfCmServiceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3)
)
if mibBuilder.loadTexts:
    docsIfCmServiceTable.setStatus("current")
_DocsIfCmServiceEntry_Object = MibTableRow
docsIfCmServiceEntry = _DocsIfCmServiceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1)
)
docsIfCmServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmServiceId"),
)
if mibBuilder.loadTexts:
    docsIfCmServiceEntry.setStatus("current")


class _DocsIfCmServiceId_Type(Integer32):
    """Custom type docsIfCmServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsIfCmServiceId_Type.__name__ = "Integer32"
_DocsIfCmServiceId_Object = MibTableColumn
docsIfCmServiceId = _DocsIfCmServiceId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 1),
    _DocsIfCmServiceId_Type()
)
docsIfCmServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmServiceId.setStatus("current")


class _DocsIfCmServiceQosProfile_Type(Integer32):
    """Custom type docsIfCmServiceQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsIfCmServiceQosProfile_Type.__name__ = "Integer32"
_DocsIfCmServiceQosProfile_Object = MibTableColumn
docsIfCmServiceQosProfile = _DocsIfCmServiceQosProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 2),
    _DocsIfCmServiceQosProfile_Type()
)
docsIfCmServiceQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceQosProfile.setStatus("current")
_DocsIfCmServiceTxSlotsImmed_Type = Counter32
_DocsIfCmServiceTxSlotsImmed_Object = MibTableColumn
docsIfCmServiceTxSlotsImmed = _DocsIfCmServiceTxSlotsImmed_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 3),
    _DocsIfCmServiceTxSlotsImmed_Type()
)
docsIfCmServiceTxSlotsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceTxSlotsImmed.setStatus("current")
_DocsIfCmServiceTxSlotsDed_Type = Counter32
_DocsIfCmServiceTxSlotsDed_Object = MibTableColumn
docsIfCmServiceTxSlotsDed = _DocsIfCmServiceTxSlotsDed_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 4),
    _DocsIfCmServiceTxSlotsDed_Type()
)
docsIfCmServiceTxSlotsDed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceTxSlotsDed.setStatus("current")
_DocsIfCmServiceTxRetries_Type = Counter32
_DocsIfCmServiceTxRetries_Object = MibTableColumn
docsIfCmServiceTxRetries = _DocsIfCmServiceTxRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 5),
    _DocsIfCmServiceTxRetries_Type()
)
docsIfCmServiceTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceTxRetries.setStatus("current")
_DocsIfCmServiceTxExceededs_Type = Counter32
_DocsIfCmServiceTxExceededs_Object = MibTableColumn
docsIfCmServiceTxExceededs = _DocsIfCmServiceTxExceededs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 6),
    _DocsIfCmServiceTxExceededs_Type()
)
docsIfCmServiceTxExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceTxExceededs.setStatus("current")
_DocsIfCmServiceRqRetries_Type = Counter32
_DocsIfCmServiceRqRetries_Object = MibTableColumn
docsIfCmServiceRqRetries = _DocsIfCmServiceRqRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 7),
    _DocsIfCmServiceRqRetries_Type()
)
docsIfCmServiceRqRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceRqRetries.setStatus("current")
_DocsIfCmServiceRqExceededs_Type = Counter32
_DocsIfCmServiceRqExceededs_Object = MibTableColumn
docsIfCmServiceRqExceededs = _DocsIfCmServiceRqExceededs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 8),
    _DocsIfCmServiceRqExceededs_Type()
)
docsIfCmServiceRqExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceRqExceededs.setStatus("current")
_DocsIfCmServiceExtTxSlotsImmed_Type = Counter64
_DocsIfCmServiceExtTxSlotsImmed_Object = MibTableColumn
docsIfCmServiceExtTxSlotsImmed = _DocsIfCmServiceExtTxSlotsImmed_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 9),
    _DocsIfCmServiceExtTxSlotsImmed_Type()
)
docsIfCmServiceExtTxSlotsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceExtTxSlotsImmed.setStatus("current")
_DocsIfCmServiceExtTxSlotsDed_Type = Counter64
_DocsIfCmServiceExtTxSlotsDed_Object = MibTableColumn
docsIfCmServiceExtTxSlotsDed = _DocsIfCmServiceExtTxSlotsDed_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 10),
    _DocsIfCmServiceExtTxSlotsDed_Type()
)
docsIfCmServiceExtTxSlotsDed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmServiceExtTxSlotsDed.setStatus("current")
_DocsIfCmtsObjects_ObjectIdentity = ObjectIdentity
docsIfCmtsObjects = _DocsIfCmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3)
)
_DocsIfCmtsMacTable_Object = MibTable
docsIfCmtsMacTable = _DocsIfCmtsMacTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsIfCmtsMacTable.setStatus("current")
_DocsIfCmtsMacEntry_Object = MibTableRow
docsIfCmtsMacEntry = _DocsIfCmtsMacEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1)
)
docsIfCmtsMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmtsMacEntry.setStatus("current")


class _DocsIfCmtsCapabilities_Type(Bits):
    """Custom type docsIfCmtsCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("atmCells", 0),
          ("concatenation", 1))
    )

_DocsIfCmtsCapabilities_Type.__name__ = "Bits"
_DocsIfCmtsCapabilities_Object = MibTableColumn
docsIfCmtsCapabilities = _DocsIfCmtsCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 1),
    _DocsIfCmtsCapabilities_Type()
)
docsIfCmtsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCapabilities.setStatus("current")


class _DocsIfCmtsSyncInterval_Type(Integer32):
    """Custom type docsIfCmtsSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_DocsIfCmtsSyncInterval_Type.__name__ = "Integer32"
_DocsIfCmtsSyncInterval_Object = MibTableColumn
docsIfCmtsSyncInterval = _DocsIfCmtsSyncInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 2),
    _DocsIfCmtsSyncInterval_Type()
)
docsIfCmtsSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsSyncInterval.setUnits("Milliseconds")


class _DocsIfCmtsUcdInterval_Type(Integer32):
    """Custom type docsIfCmtsUcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_DocsIfCmtsUcdInterval_Type.__name__ = "Integer32"
_DocsIfCmtsUcdInterval_Object = MibTableColumn
docsIfCmtsUcdInterval = _DocsIfCmtsUcdInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 3),
    _DocsIfCmtsUcdInterval_Type()
)
docsIfCmtsUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsUcdInterval.setUnits("Milliseconds")


class _DocsIfCmtsMaxServiceIds_Type(Integer32):
    """Custom type docsIfCmtsMaxServiceIds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsIfCmtsMaxServiceIds_Type.__name__ = "Integer32"
_DocsIfCmtsMaxServiceIds_Object = MibTableColumn
docsIfCmtsMaxServiceIds = _DocsIfCmtsMaxServiceIds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 4),
    _DocsIfCmtsMaxServiceIds_Type()
)
docsIfCmtsMaxServiceIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsMaxServiceIds.setStatus("current")
_DocsIfCmtsInsertionInterval_Type = TimeTicks
_DocsIfCmtsInsertionInterval_Object = MibTableColumn
docsIfCmtsInsertionInterval = _DocsIfCmtsInsertionInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 5),
    _DocsIfCmtsInsertionInterval_Type()
)
docsIfCmtsInsertionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsInsertionInterval.setStatus("obsolete")


class _DocsIfCmtsInvitedRangingAttempts_Type(Integer32):
    """Custom type docsIfCmtsInvitedRangingAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsIfCmtsInvitedRangingAttempts_Type.__name__ = "Integer32"
_DocsIfCmtsInvitedRangingAttempts_Object = MibTableColumn
docsIfCmtsInvitedRangingAttempts = _DocsIfCmtsInvitedRangingAttempts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 6),
    _DocsIfCmtsInvitedRangingAttempts_Type()
)
docsIfCmtsInvitedRangingAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsInvitedRangingAttempts.setStatus("current")
_DocsIfCmtsInsertInterval_Type = TimeInterval
_DocsIfCmtsInsertInterval_Object = MibTableColumn
docsIfCmtsInsertInterval = _DocsIfCmtsInsertInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 7),
    _DocsIfCmtsInsertInterval_Type()
)
docsIfCmtsInsertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsInsertInterval.setStatus("current")
_DocsIfCmtsStatusTable_Object = MibTable
docsIfCmtsStatusTable = _DocsIfCmtsStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2)
)
if mibBuilder.loadTexts:
    docsIfCmtsStatusTable.setStatus("current")
_DocsIfCmtsStatusEntry_Object = MibTableRow
docsIfCmtsStatusEntry = _DocsIfCmtsStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1)
)
docsIfCmtsStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmtsStatusEntry.setStatus("current")
_DocsIfCmtsStatusInvalidRangeReqs_Type = Counter32
_DocsIfCmtsStatusInvalidRangeReqs_Object = MibTableColumn
docsIfCmtsStatusInvalidRangeReqs = _DocsIfCmtsStatusInvalidRangeReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 1),
    _DocsIfCmtsStatusInvalidRangeReqs_Type()
)
docsIfCmtsStatusInvalidRangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsStatusInvalidRangeReqs.setStatus("current")
_DocsIfCmtsStatusRangingAborteds_Type = Counter32
_DocsIfCmtsStatusRangingAborteds_Object = MibTableColumn
docsIfCmtsStatusRangingAborteds = _DocsIfCmtsStatusRangingAborteds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 2),
    _DocsIfCmtsStatusRangingAborteds_Type()
)
docsIfCmtsStatusRangingAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsStatusRangingAborteds.setStatus("current")
_DocsIfCmtsStatusInvalidRegReqs_Type = Counter32
_DocsIfCmtsStatusInvalidRegReqs_Object = MibTableColumn
docsIfCmtsStatusInvalidRegReqs = _DocsIfCmtsStatusInvalidRegReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 3),
    _DocsIfCmtsStatusInvalidRegReqs_Type()
)
docsIfCmtsStatusInvalidRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsStatusInvalidRegReqs.setStatus("current")
_DocsIfCmtsStatusFailedRegReqs_Type = Counter32
_DocsIfCmtsStatusFailedRegReqs_Object = MibTableColumn
docsIfCmtsStatusFailedRegReqs = _DocsIfCmtsStatusFailedRegReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 4),
    _DocsIfCmtsStatusFailedRegReqs_Type()
)
docsIfCmtsStatusFailedRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsStatusFailedRegReqs.setStatus("current")
_DocsIfCmtsStatusInvalidDataReqs_Type = Counter32
_DocsIfCmtsStatusInvalidDataReqs_Object = MibTableColumn
docsIfCmtsStatusInvalidDataReqs = _DocsIfCmtsStatusInvalidDataReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 5),
    _DocsIfCmtsStatusInvalidDataReqs_Type()
)
docsIfCmtsStatusInvalidDataReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsStatusInvalidDataReqs.setStatus("current")
_DocsIfCmtsStatusT5Timeouts_Type = Counter32
_DocsIfCmtsStatusT5Timeouts_Object = MibTableColumn
docsIfCmtsStatusT5Timeouts = _DocsIfCmtsStatusT5Timeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 6),
    _DocsIfCmtsStatusT5Timeouts_Type()
)
docsIfCmtsStatusT5Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsStatusT5Timeouts.setStatus("current")
_DocsIfCmtsCmStatusTable_Object = MibTable
docsIfCmtsCmStatusTable = _DocsIfCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3)
)
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusTable.setStatus("current")
_DocsIfCmtsCmStatusEntry_Object = MibTableRow
docsIfCmtsCmStatusEntry = _DocsIfCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1)
)
docsIfCmtsCmStatusEntry.setIndexNames(
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusEntry.setStatus("current")


class _DocsIfCmtsCmStatusIndex_Type(Integer32):
    """Custom type docsIfCmtsCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsIfCmtsCmStatusIndex_Type.__name__ = "Integer32"
_DocsIfCmtsCmStatusIndex_Object = MibTableColumn
docsIfCmtsCmStatusIndex = _DocsIfCmtsCmStatusIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 1),
    _DocsIfCmtsCmStatusIndex_Type()
)
docsIfCmtsCmStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusIndex.setStatus("current")
_DocsIfCmtsCmStatusMacAddress_Type = MacAddress
_DocsIfCmtsCmStatusMacAddress_Object = MibTableColumn
docsIfCmtsCmStatusMacAddress = _DocsIfCmtsCmStatusMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 2),
    _DocsIfCmtsCmStatusMacAddress_Type()
)
docsIfCmtsCmStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusMacAddress.setStatus("current")
_DocsIfCmtsCmStatusIpAddress_Type = IpAddress
_DocsIfCmtsCmStatusIpAddress_Object = MibTableColumn
docsIfCmtsCmStatusIpAddress = _DocsIfCmtsCmStatusIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 3),
    _DocsIfCmtsCmStatusIpAddress_Type()
)
docsIfCmtsCmStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusIpAddress.setStatus("deprecated")
_DocsIfCmtsCmStatusDownChannelIfIndex_Type = InterfaceIndexOrZero
_DocsIfCmtsCmStatusDownChannelIfIndex_Object = MibTableColumn
docsIfCmtsCmStatusDownChannelIfIndex = _DocsIfCmtsCmStatusDownChannelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 4),
    _DocsIfCmtsCmStatusDownChannelIfIndex_Type()
)
docsIfCmtsCmStatusDownChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusDownChannelIfIndex.setStatus("current")
_DocsIfCmtsCmStatusUpChannelIfIndex_Type = InterfaceIndexOrZero
_DocsIfCmtsCmStatusUpChannelIfIndex_Object = MibTableColumn
docsIfCmtsCmStatusUpChannelIfIndex = _DocsIfCmtsCmStatusUpChannelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 5),
    _DocsIfCmtsCmStatusUpChannelIfIndex_Type()
)
docsIfCmtsCmStatusUpChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusUpChannelIfIndex.setStatus("current")
_DocsIfCmtsCmStatusRxPower_Type = TenthdBmV
_DocsIfCmtsCmStatusRxPower_Object = MibTableColumn
docsIfCmtsCmStatusRxPower = _DocsIfCmtsCmStatusRxPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 6),
    _DocsIfCmtsCmStatusRxPower_Type()
)
docsIfCmtsCmStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusRxPower.setUnits("dBmV")
_DocsIfCmtsCmStatusTimingOffset_Type = Unsigned32
_DocsIfCmtsCmStatusTimingOffset_Object = MibTableColumn
docsIfCmtsCmStatusTimingOffset = _DocsIfCmtsCmStatusTimingOffset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 7),
    _DocsIfCmtsCmStatusTimingOffset_Type()
)
docsIfCmtsCmStatusTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusTimingOffset.setStatus("current")


class _DocsIfCmtsCmStatusEqualizationData_Type(OctetString):
    """Custom type docsIfCmtsCmStatusEqualizationData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DocsIfCmtsCmStatusEqualizationData_Type.__name__ = "OctetString"
_DocsIfCmtsCmStatusEqualizationData_Object = MibTableColumn
docsIfCmtsCmStatusEqualizationData = _DocsIfCmtsCmStatusEqualizationData_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 8),
    _DocsIfCmtsCmStatusEqualizationData_Type()
)
docsIfCmtsCmStatusEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusEqualizationData.setStatus("current")


class _DocsIfCmtsCmStatusValue_Type(Integer32):
    """Custom type docsIfCmtsCmStatusValue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("ipComplete", 5),
          ("operational", 8),
          ("other", 1),
          ("ranging", 2),
          ("rangingAborted", 3),
          ("rangingComplete", 4),
          ("registrationComplete", 6))
    )


_DocsIfCmtsCmStatusValue_Type.__name__ = "Integer32"
_DocsIfCmtsCmStatusValue_Object = MibTableColumn
docsIfCmtsCmStatusValue = _DocsIfCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 9),
    _DocsIfCmtsCmStatusValue_Type()
)
docsIfCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusValue.setStatus("current")
_DocsIfCmtsCmStatusUnerroreds_Type = Counter32
_DocsIfCmtsCmStatusUnerroreds_Object = MibTableColumn
docsIfCmtsCmStatusUnerroreds = _DocsIfCmtsCmStatusUnerroreds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 10),
    _DocsIfCmtsCmStatusUnerroreds_Type()
)
docsIfCmtsCmStatusUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusUnerroreds.setStatus("current")
_DocsIfCmtsCmStatusCorrecteds_Type = Counter32
_DocsIfCmtsCmStatusCorrecteds_Object = MibTableColumn
docsIfCmtsCmStatusCorrecteds = _DocsIfCmtsCmStatusCorrecteds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 11),
    _DocsIfCmtsCmStatusCorrecteds_Type()
)
docsIfCmtsCmStatusCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusCorrecteds.setStatus("current")
_DocsIfCmtsCmStatusUncorrectables_Type = Counter32
_DocsIfCmtsCmStatusUncorrectables_Object = MibTableColumn
docsIfCmtsCmStatusUncorrectables = _DocsIfCmtsCmStatusUncorrectables_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 12),
    _DocsIfCmtsCmStatusUncorrectables_Type()
)
docsIfCmtsCmStatusUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusUncorrectables.setStatus("current")
_DocsIfCmtsCmStatusSignalNoise_Type = TenthdB
_DocsIfCmtsCmStatusSignalNoise_Object = MibTableColumn
docsIfCmtsCmStatusSignalNoise = _DocsIfCmtsCmStatusSignalNoise_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 13),
    _DocsIfCmtsCmStatusSignalNoise_Type()
)
docsIfCmtsCmStatusSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusSignalNoise.setUnits("dB")


class _DocsIfCmtsCmStatusMicroreflections_Type(Integer32):
    """Custom type docsIfCmtsCmStatusMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfCmtsCmStatusMicroreflections_Type.__name__ = "Integer32"
_DocsIfCmtsCmStatusMicroreflections_Object = MibTableColumn
docsIfCmtsCmStatusMicroreflections = _DocsIfCmtsCmStatusMicroreflections_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 14),
    _DocsIfCmtsCmStatusMicroreflections_Type()
)
docsIfCmtsCmStatusMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusMicroreflections.setUnits("dBc")
_DocsIfCmtsCmStatusExtUnerroreds_Type = Counter64
_DocsIfCmtsCmStatusExtUnerroreds_Object = MibTableColumn
docsIfCmtsCmStatusExtUnerroreds = _DocsIfCmtsCmStatusExtUnerroreds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 15),
    _DocsIfCmtsCmStatusExtUnerroreds_Type()
)
docsIfCmtsCmStatusExtUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusExtUnerroreds.setStatus("current")
_DocsIfCmtsCmStatusExtCorrecteds_Type = Counter64
_DocsIfCmtsCmStatusExtCorrecteds_Object = MibTableColumn
docsIfCmtsCmStatusExtCorrecteds = _DocsIfCmtsCmStatusExtCorrecteds_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 16),
    _DocsIfCmtsCmStatusExtCorrecteds_Type()
)
docsIfCmtsCmStatusExtCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusExtCorrecteds.setStatus("current")
_DocsIfCmtsCmStatusExtUncorrectables_Type = Counter64
_DocsIfCmtsCmStatusExtUncorrectables_Object = MibTableColumn
docsIfCmtsCmStatusExtUncorrectables = _DocsIfCmtsCmStatusExtUncorrectables_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 17),
    _DocsIfCmtsCmStatusExtUncorrectables_Type()
)
docsIfCmtsCmStatusExtUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusExtUncorrectables.setStatus("current")
_DocsIfCmtsCmStatusDocsisRegMode_Type = DocsisQosVersion
_DocsIfCmtsCmStatusDocsisRegMode_Object = MibTableColumn
docsIfCmtsCmStatusDocsisRegMode = _DocsIfCmtsCmStatusDocsisRegMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 18),
    _DocsIfCmtsCmStatusDocsisRegMode_Type()
)
docsIfCmtsCmStatusDocsisRegMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusDocsisRegMode.setStatus("current")
_DocsIfCmtsCmStatusModulationType_Type = DocsisUpstreamTypeStatus
_DocsIfCmtsCmStatusModulationType_Object = MibTableColumn
docsIfCmtsCmStatusModulationType = _DocsIfCmtsCmStatusModulationType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 19),
    _DocsIfCmtsCmStatusModulationType_Type()
)
docsIfCmtsCmStatusModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusModulationType.setStatus("current")
_DocsIfCmtsCmStatusInetAddressType_Type = InetAddressType
_DocsIfCmtsCmStatusInetAddressType_Object = MibTableColumn
docsIfCmtsCmStatusInetAddressType = _DocsIfCmtsCmStatusInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 20),
    _DocsIfCmtsCmStatusInetAddressType_Type()
)
docsIfCmtsCmStatusInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusInetAddressType.setStatus("current")
_DocsIfCmtsCmStatusInetAddress_Type = InetAddress
_DocsIfCmtsCmStatusInetAddress_Object = MibTableColumn
docsIfCmtsCmStatusInetAddress = _DocsIfCmtsCmStatusInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 21),
    _DocsIfCmtsCmStatusInetAddress_Type()
)
docsIfCmtsCmStatusInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusInetAddress.setStatus("current")
_DocsIfCmtsServiceTable_Object = MibTable
docsIfCmtsServiceTable = _DocsIfCmtsServiceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4)
)
if mibBuilder.loadTexts:
    docsIfCmtsServiceTable.setStatus("current")
_DocsIfCmtsServiceEntry_Object = MibTableRow
docsIfCmtsServiceEntry = _DocsIfCmtsServiceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1)
)
docsIfCmtsServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsServiceId"),
)
if mibBuilder.loadTexts:
    docsIfCmtsServiceEntry.setStatus("current")


class _DocsIfCmtsServiceId_Type(Integer32):
    """Custom type docsIfCmtsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsIfCmtsServiceId_Type.__name__ = "Integer32"
_DocsIfCmtsServiceId_Object = MibTableColumn
docsIfCmtsServiceId = _DocsIfCmtsServiceId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 1),
    _DocsIfCmtsServiceId_Type()
)
docsIfCmtsServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsServiceId.setStatus("current")


class _DocsIfCmtsServiceCmStatusIndex_Type(Integer32):
    """Custom type docsIfCmtsServiceCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIfCmtsServiceCmStatusIndex_Type.__name__ = "Integer32"
_DocsIfCmtsServiceCmStatusIndex_Object = MibTableColumn
docsIfCmtsServiceCmStatusIndex = _DocsIfCmtsServiceCmStatusIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 2),
    _DocsIfCmtsServiceCmStatusIndex_Type()
)
docsIfCmtsServiceCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsServiceCmStatusIndex.setStatus("deprecated")


class _DocsIfCmtsServiceAdminStatus_Type(Integer32):
    """Custom type docsIfCmtsServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destroyed", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_DocsIfCmtsServiceAdminStatus_Type.__name__ = "Integer32"
_DocsIfCmtsServiceAdminStatus_Object = MibTableColumn
docsIfCmtsServiceAdminStatus = _DocsIfCmtsServiceAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 3),
    _DocsIfCmtsServiceAdminStatus_Type()
)
docsIfCmtsServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsServiceAdminStatus.setStatus("current")


class _DocsIfCmtsServiceQosProfile_Type(Integer32):
    """Custom type docsIfCmtsServiceQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsIfCmtsServiceQosProfile_Type.__name__ = "Integer32"
_DocsIfCmtsServiceQosProfile_Object = MibTableColumn
docsIfCmtsServiceQosProfile = _DocsIfCmtsServiceQosProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 4),
    _DocsIfCmtsServiceQosProfile_Type()
)
docsIfCmtsServiceQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsServiceQosProfile.setStatus("current")
_DocsIfCmtsServiceCreateTime_Type = TimeStamp
_DocsIfCmtsServiceCreateTime_Object = MibTableColumn
docsIfCmtsServiceCreateTime = _DocsIfCmtsServiceCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 5),
    _DocsIfCmtsServiceCreateTime_Type()
)
docsIfCmtsServiceCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsServiceCreateTime.setStatus("current")
_DocsIfCmtsServiceInOctets_Type = Counter32
_DocsIfCmtsServiceInOctets_Object = MibTableColumn
docsIfCmtsServiceInOctets = _DocsIfCmtsServiceInOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 6),
    _DocsIfCmtsServiceInOctets_Type()
)
docsIfCmtsServiceInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsServiceInOctets.setStatus("current")
_DocsIfCmtsServiceInPackets_Type = Counter32
_DocsIfCmtsServiceInPackets_Object = MibTableColumn
docsIfCmtsServiceInPackets = _DocsIfCmtsServiceInPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 7),
    _DocsIfCmtsServiceInPackets_Type()
)
docsIfCmtsServiceInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsServiceInPackets.setStatus("current")


class _DocsIfCmtsServiceNewCmStatusIndex_Type(Integer32):
    """Custom type docsIfCmtsServiceNewCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DocsIfCmtsServiceNewCmStatusIndex_Type.__name__ = "Integer32"
_DocsIfCmtsServiceNewCmStatusIndex_Object = MibTableColumn
docsIfCmtsServiceNewCmStatusIndex = _DocsIfCmtsServiceNewCmStatusIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 8),
    _DocsIfCmtsServiceNewCmStatusIndex_Type()
)
docsIfCmtsServiceNewCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsServiceNewCmStatusIndex.setStatus("current")
_DocsIfCmtsModulationTable_Object = MibTable
docsIfCmtsModulationTable = _DocsIfCmtsModulationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5)
)
if mibBuilder.loadTexts:
    docsIfCmtsModulationTable.setStatus("current")
_DocsIfCmtsModulationEntry_Object = MibTableRow
docsIfCmtsModulationEntry = _DocsIfCmtsModulationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1)
)
docsIfCmtsModulationEntry.setIndexNames(
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsModIndex"),
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsModIntervalUsageCode"),
)
if mibBuilder.loadTexts:
    docsIfCmtsModulationEntry.setStatus("current")


class _DocsIfCmtsModIndex_Type(Integer32):
    """Custom type docsIfCmtsModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsIfCmtsModIndex_Type.__name__ = "Integer32"
_DocsIfCmtsModIndex_Object = MibTableColumn
docsIfCmtsModIndex = _DocsIfCmtsModIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 1),
    _DocsIfCmtsModIndex_Type()
)
docsIfCmtsModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsModIndex.setStatus("current")


class _DocsIfCmtsModIntervalUsageCode_Type(Integer32):
    """Custom type docsIfCmtsModIntervalUsageCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("advPhyLongData", 10),
          ("advPhyShortData", 9),
          ("initialRanging", 3),
          ("longData", 6),
          ("periodicRanging", 4),
          ("request", 1),
          ("requestData", 2),
          ("shortData", 5),
          ("ugs", 11))
    )


_DocsIfCmtsModIntervalUsageCode_Type.__name__ = "Integer32"
_DocsIfCmtsModIntervalUsageCode_Object = MibTableColumn
docsIfCmtsModIntervalUsageCode = _DocsIfCmtsModIntervalUsageCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 2),
    _DocsIfCmtsModIntervalUsageCode_Type()
)
docsIfCmtsModIntervalUsageCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsModIntervalUsageCode.setStatus("current")
_DocsIfCmtsModControl_Type = RowStatus
_DocsIfCmtsModControl_Object = MibTableColumn
docsIfCmtsModControl = _DocsIfCmtsModControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 3),
    _DocsIfCmtsModControl_Type()
)
docsIfCmtsModControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModControl.setStatus("current")


class _DocsIfCmtsModType_Type(Integer32):
    """Custom type docsIfCmtsModType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("qam128", 7),
          ("qam16", 3),
          ("qam32", 5),
          ("qam64", 6),
          ("qam8", 4),
          ("qpsk", 2))
    )


_DocsIfCmtsModType_Type.__name__ = "Integer32"
_DocsIfCmtsModType_Object = MibTableColumn
docsIfCmtsModType = _DocsIfCmtsModType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 4),
    _DocsIfCmtsModType_Type()
)
docsIfCmtsModType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModType.setStatus("current")


class _DocsIfCmtsModPreambleLen_Type(Integer32):
    """Custom type docsIfCmtsModPreambleLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536),
    )


_DocsIfCmtsModPreambleLen_Type.__name__ = "Integer32"
_DocsIfCmtsModPreambleLen_Object = MibTableColumn
docsIfCmtsModPreambleLen = _DocsIfCmtsModPreambleLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 5),
    _DocsIfCmtsModPreambleLen_Type()
)
docsIfCmtsModPreambleLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModPreambleLen.setStatus("current")


class _DocsIfCmtsModDifferentialEncoding_Type(TruthValue):
    """Custom type docsIfCmtsModDifferentialEncoding based on TruthValue"""


_DocsIfCmtsModDifferentialEncoding_Object = MibTableColumn
docsIfCmtsModDifferentialEncoding = _DocsIfCmtsModDifferentialEncoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 6),
    _DocsIfCmtsModDifferentialEncoding_Type()
)
docsIfCmtsModDifferentialEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModDifferentialEncoding.setStatus("current")


class _DocsIfCmtsModFECErrorCorrection_Type(Integer32):
    """Custom type docsIfCmtsModFECErrorCorrection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIfCmtsModFECErrorCorrection_Type.__name__ = "Integer32"
_DocsIfCmtsModFECErrorCorrection_Object = MibTableColumn
docsIfCmtsModFECErrorCorrection = _DocsIfCmtsModFECErrorCorrection_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 7),
    _DocsIfCmtsModFECErrorCorrection_Type()
)
docsIfCmtsModFECErrorCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModFECErrorCorrection.setStatus("current")


class _DocsIfCmtsModFECCodewordLength_Type(Integer32):
    """Custom type docsIfCmtsModFECCodewordLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIfCmtsModFECCodewordLength_Type.__name__ = "Integer32"
_DocsIfCmtsModFECCodewordLength_Object = MibTableColumn
docsIfCmtsModFECCodewordLength = _DocsIfCmtsModFECCodewordLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 8),
    _DocsIfCmtsModFECCodewordLength_Type()
)
docsIfCmtsModFECCodewordLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModFECCodewordLength.setStatus("current")


class _DocsIfCmtsModScramblerSeed_Type(Integer32):
    """Custom type docsIfCmtsModScramblerSeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_DocsIfCmtsModScramblerSeed_Type.__name__ = "Integer32"
_DocsIfCmtsModScramblerSeed_Object = MibTableColumn
docsIfCmtsModScramblerSeed = _DocsIfCmtsModScramblerSeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 9),
    _DocsIfCmtsModScramblerSeed_Type()
)
docsIfCmtsModScramblerSeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModScramblerSeed.setStatus("current")


class _DocsIfCmtsModMaxBurstSize_Type(Integer32):
    """Custom type docsIfCmtsModMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfCmtsModMaxBurstSize_Type.__name__ = "Integer32"
_DocsIfCmtsModMaxBurstSize_Object = MibTableColumn
docsIfCmtsModMaxBurstSize = _DocsIfCmtsModMaxBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 10),
    _DocsIfCmtsModMaxBurstSize_Type()
)
docsIfCmtsModMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModMaxBurstSize.setStatus("current")
_DocsIfCmtsModGuardTimeSize_Type = Unsigned32
_DocsIfCmtsModGuardTimeSize_Object = MibTableColumn
docsIfCmtsModGuardTimeSize = _DocsIfCmtsModGuardTimeSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 11),
    _DocsIfCmtsModGuardTimeSize_Type()
)
docsIfCmtsModGuardTimeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsModGuardTimeSize.setStatus("current")


class _DocsIfCmtsModLastCodewordShortened_Type(TruthValue):
    """Custom type docsIfCmtsModLastCodewordShortened based on TruthValue"""


_DocsIfCmtsModLastCodewordShortened_Object = MibTableColumn
docsIfCmtsModLastCodewordShortened = _DocsIfCmtsModLastCodewordShortened_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 12),
    _DocsIfCmtsModLastCodewordShortened_Type()
)
docsIfCmtsModLastCodewordShortened.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModLastCodewordShortened.setStatus("current")


class _DocsIfCmtsModScrambler_Type(TruthValue):
    """Custom type docsIfCmtsModScrambler based on TruthValue"""


_DocsIfCmtsModScrambler_Object = MibTableColumn
docsIfCmtsModScrambler = _DocsIfCmtsModScrambler_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 13),
    _DocsIfCmtsModScrambler_Type()
)
docsIfCmtsModScrambler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModScrambler.setStatus("current")


class _DocsIfCmtsModByteInterleaverDepth_Type(Unsigned32):
    """Custom type docsIfCmtsModByteInterleaverDepth based on Unsigned32"""
    defaultValue = 1


_DocsIfCmtsModByteInterleaverDepth_Object = MibTableColumn
docsIfCmtsModByteInterleaverDepth = _DocsIfCmtsModByteInterleaverDepth_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 14),
    _DocsIfCmtsModByteInterleaverDepth_Type()
)
docsIfCmtsModByteInterleaverDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModByteInterleaverDepth.setStatus("current")


class _DocsIfCmtsModByteInterleaverBlockSize_Type(Unsigned32):
    """Custom type docsIfCmtsModByteInterleaverBlockSize based on Unsigned32"""
    defaultValue = 18


_DocsIfCmtsModByteInterleaverBlockSize_Object = MibTableColumn
docsIfCmtsModByteInterleaverBlockSize = _DocsIfCmtsModByteInterleaverBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 15),
    _DocsIfCmtsModByteInterleaverBlockSize_Type()
)
docsIfCmtsModByteInterleaverBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModByteInterleaverBlockSize.setStatus("current")


class _DocsIfCmtsModPreambleType_Type(Integer32):
    """Custom type docsIfCmtsModPreambleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qpsk0", 1),
          ("qpsk1", 2))
    )


_DocsIfCmtsModPreambleType_Type.__name__ = "Integer32"
_DocsIfCmtsModPreambleType_Object = MibTableColumn
docsIfCmtsModPreambleType = _DocsIfCmtsModPreambleType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 16),
    _DocsIfCmtsModPreambleType_Type()
)
docsIfCmtsModPreambleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModPreambleType.setStatus("current")


class _DocsIfCmtsModTcmErrorCorrectionOn_Type(TruthValue):
    """Custom type docsIfCmtsModTcmErrorCorrectionOn based on TruthValue"""


_DocsIfCmtsModTcmErrorCorrectionOn_Object = MibTableColumn
docsIfCmtsModTcmErrorCorrectionOn = _DocsIfCmtsModTcmErrorCorrectionOn_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 17),
    _DocsIfCmtsModTcmErrorCorrectionOn_Type()
)
docsIfCmtsModTcmErrorCorrectionOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModTcmErrorCorrectionOn.setStatus("current")


class _DocsIfCmtsModScdmaInterleaverStepSize_Type(Unsigned32):
    """Custom type docsIfCmtsModScdmaInterleaverStepSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_DocsIfCmtsModScdmaInterleaverStepSize_Type.__name__ = "Unsigned32"
_DocsIfCmtsModScdmaInterleaverStepSize_Object = MibTableColumn
docsIfCmtsModScdmaInterleaverStepSize = _DocsIfCmtsModScdmaInterleaverStepSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 18),
    _DocsIfCmtsModScdmaInterleaverStepSize_Type()
)
docsIfCmtsModScdmaInterleaverStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModScdmaInterleaverStepSize.setStatus("current")
_DocsIfCmtsModScdmaSpreaderEnable_Type = TruthValue
_DocsIfCmtsModScdmaSpreaderEnable_Object = MibTableColumn
docsIfCmtsModScdmaSpreaderEnable = _DocsIfCmtsModScdmaSpreaderEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 19),
    _DocsIfCmtsModScdmaSpreaderEnable_Type()
)
docsIfCmtsModScdmaSpreaderEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModScdmaSpreaderEnable.setStatus("current")


class _DocsIfCmtsModScdmaSubframeCodes_Type(Unsigned32):
    """Custom type docsIfCmtsModScdmaSubframeCodes based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_DocsIfCmtsModScdmaSubframeCodes_Type.__name__ = "Unsigned32"
_DocsIfCmtsModScdmaSubframeCodes_Object = MibTableColumn
docsIfCmtsModScdmaSubframeCodes = _DocsIfCmtsModScdmaSubframeCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 20),
    _DocsIfCmtsModScdmaSubframeCodes_Type()
)
docsIfCmtsModScdmaSubframeCodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModScdmaSubframeCodes.setStatus("current")


class _DocsIfCmtsModChannelType_Type(DocsisUpstreamType):
    """Custom type docsIfCmtsModChannelType based on DocsisUpstreamType"""


_DocsIfCmtsModChannelType_Object = MibTableColumn
docsIfCmtsModChannelType = _DocsIfCmtsModChannelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 21),
    _DocsIfCmtsModChannelType_Type()
)
docsIfCmtsModChannelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfCmtsModChannelType.setStatus("current")


class _DocsIfCmtsQosProfilePermissions_Type(Bits):
    """Custom type docsIfCmtsQosProfilePermissions based on Bits"""
    namedValues = NamedValues(
        *(("createByManagement", 0),
          ("createByModems", 2),
          ("updateByManagement", 1))
    )

_DocsIfCmtsQosProfilePermissions_Type.__name__ = "Bits"
_DocsIfCmtsQosProfilePermissions_Object = MibScalar
docsIfCmtsQosProfilePermissions = _DocsIfCmtsQosProfilePermissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 6),
    _DocsIfCmtsQosProfilePermissions_Type()
)
docsIfCmtsQosProfilePermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsQosProfilePermissions.setStatus("current")
_DocsIfCmtsMacToCmTable_Object = MibTable
docsIfCmtsMacToCmTable = _DocsIfCmtsMacToCmTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7)
)
if mibBuilder.loadTexts:
    docsIfCmtsMacToCmTable.setStatus("current")
_DocsIfCmtsMacToCmEntry_Object = MibTableRow
docsIfCmtsMacToCmEntry = _DocsIfCmtsMacToCmEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7, 1)
)
docsIfCmtsMacToCmEntry.setIndexNames(
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsCmMac"),
)
if mibBuilder.loadTexts:
    docsIfCmtsMacToCmEntry.setStatus("current")
_DocsIfCmtsCmMac_Type = MacAddress
_DocsIfCmtsCmMac_Object = MibTableColumn
docsIfCmtsCmMac = _DocsIfCmtsCmMac_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7, 1, 1),
    _DocsIfCmtsCmMac_Type()
)
docsIfCmtsCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsCmMac.setStatus("current")


class _DocsIfCmtsCmPtr_Type(Integer32):
    """Custom type docsIfCmtsCmPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsIfCmtsCmPtr_Type.__name__ = "Integer32"
_DocsIfCmtsCmPtr_Object = MibTableColumn
docsIfCmtsCmPtr = _DocsIfCmtsCmPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7, 1, 2),
    _DocsIfCmtsCmPtr_Type()
)
docsIfCmtsCmPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmPtr.setStatus("current")


class _DocsIfCmtsChannelUtilizationInterval_Type(Integer32):
    """Custom type docsIfCmtsChannelUtilizationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DocsIfCmtsChannelUtilizationInterval_Type.__name__ = "Integer32"
_DocsIfCmtsChannelUtilizationInterval_Object = MibScalar
docsIfCmtsChannelUtilizationInterval = _DocsIfCmtsChannelUtilizationInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 8),
    _DocsIfCmtsChannelUtilizationInterval_Type()
)
docsIfCmtsChannelUtilizationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtilizationInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtilizationInterval.setUnits("seconds")
_DocsIfCmtsChannelUtilizationTable_Object = MibTable
docsIfCmtsChannelUtilizationTable = _DocsIfCmtsChannelUtilizationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 9)
)
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtilizationTable.setStatus("current")
_DocsIfCmtsChannelUtilizationEntry_Object = MibTableRow
docsIfCmtsChannelUtilizationEntry = _DocsIfCmtsChannelUtilizationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 9, 1)
)
docsIfCmtsChannelUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsChannelUtIfType"),
    (0, "DOCS-IETF-RFI-MIB", "docsIfCmtsChannelUtId"),
)
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtilizationEntry.setStatus("current")
_DocsIfCmtsChannelUtIfType_Type = IANAifType
_DocsIfCmtsChannelUtIfType_Object = MibTableColumn
docsIfCmtsChannelUtIfType = _DocsIfCmtsChannelUtIfType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 9, 1, 1),
    _DocsIfCmtsChannelUtIfType_Type()
)
docsIfCmtsChannelUtIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtIfType.setStatus("current")


class _DocsIfCmtsChannelUtId_Type(Integer32):
    """Custom type docsIfCmtsChannelUtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfCmtsChannelUtId_Type.__name__ = "Integer32"
_DocsIfCmtsChannelUtId_Object = MibTableColumn
docsIfCmtsChannelUtId = _DocsIfCmtsChannelUtId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 9, 1, 2),
    _DocsIfCmtsChannelUtId_Type()
)
docsIfCmtsChannelUtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtId.setStatus("current")


class _DocsIfCmtsChannelUtUtilization_Type(Integer32):
    """Custom type docsIfCmtsChannelUtUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DocsIfCmtsChannelUtUtilization_Type.__name__ = "Integer32"
_DocsIfCmtsChannelUtUtilization_Object = MibTableColumn
docsIfCmtsChannelUtUtilization = _DocsIfCmtsChannelUtUtilization_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 9, 1, 3),
    _DocsIfCmtsChannelUtUtilization_Type()
)
docsIfCmtsChannelUtUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtUtilization.setStatus("current")
if mibBuilder.loadTexts:
    docsIfCmtsChannelUtUtilization.setUnits("percent")
_DocsIfCmtsDownChannelCounterTable_Object = MibTable
docsIfCmtsDownChannelCounterTable = _DocsIfCmtsDownChannelCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10)
)
if mibBuilder.loadTexts:
    docsIfCmtsDownChannelCounterTable.setStatus("current")
_DocsIfCmtsDownChannelCounterEntry_Object = MibTableRow
docsIfCmtsDownChannelCounterEntry = _DocsIfCmtsDownChannelCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10, 1)
)
docsIfCmtsDownChannelCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmtsDownChannelCounterEntry.setStatus("current")


class _DocsIfCmtsDownChnlCtrId_Type(Integer32):
    """Custom type docsIfCmtsDownChnlCtrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfCmtsDownChnlCtrId_Type.__name__ = "Integer32"
_DocsIfCmtsDownChnlCtrId_Object = MibTableColumn
docsIfCmtsDownChnlCtrId = _DocsIfCmtsDownChnlCtrId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10, 1, 1),
    _DocsIfCmtsDownChnlCtrId_Type()
)
docsIfCmtsDownChnlCtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsDownChnlCtrId.setStatus("current")
_DocsIfCmtsDownChnlCtrTotalBytes_Type = Counter32
_DocsIfCmtsDownChnlCtrTotalBytes_Object = MibTableColumn
docsIfCmtsDownChnlCtrTotalBytes = _DocsIfCmtsDownChnlCtrTotalBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10, 1, 2),
    _DocsIfCmtsDownChnlCtrTotalBytes_Type()
)
docsIfCmtsDownChnlCtrTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsDownChnlCtrTotalBytes.setStatus("current")
_DocsIfCmtsDownChnlCtrUsedBytes_Type = Counter32
_DocsIfCmtsDownChnlCtrUsedBytes_Object = MibTableColumn
docsIfCmtsDownChnlCtrUsedBytes = _DocsIfCmtsDownChnlCtrUsedBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10, 1, 3),
    _DocsIfCmtsDownChnlCtrUsedBytes_Type()
)
docsIfCmtsDownChnlCtrUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsDownChnlCtrUsedBytes.setStatus("current")
_DocsIfCmtsDownChnlCtrExtTotalBytes_Type = Counter64
_DocsIfCmtsDownChnlCtrExtTotalBytes_Object = MibTableColumn
docsIfCmtsDownChnlCtrExtTotalBytes = _DocsIfCmtsDownChnlCtrExtTotalBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10, 1, 4),
    _DocsIfCmtsDownChnlCtrExtTotalBytes_Type()
)
docsIfCmtsDownChnlCtrExtTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsDownChnlCtrExtTotalBytes.setStatus("current")
_DocsIfCmtsDownChnlCtrExtUsedBytes_Type = Counter64
_DocsIfCmtsDownChnlCtrExtUsedBytes_Object = MibTableColumn
docsIfCmtsDownChnlCtrExtUsedBytes = _DocsIfCmtsDownChnlCtrExtUsedBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 10, 1, 5),
    _DocsIfCmtsDownChnlCtrExtUsedBytes_Type()
)
docsIfCmtsDownChnlCtrExtUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsDownChnlCtrExtUsedBytes.setStatus("current")
_DocsIfCmtsUpChannelCounterTable_Object = MibTable
docsIfCmtsUpChannelCounterTable = _DocsIfCmtsUpChannelCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11)
)
if mibBuilder.loadTexts:
    docsIfCmtsUpChannelCounterTable.setStatus("current")
_DocsIfCmtsUpChannelCounterEntry_Object = MibTableRow
docsIfCmtsUpChannelCounterEntry = _DocsIfCmtsUpChannelCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1)
)
docsIfCmtsUpChannelCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfCmtsUpChannelCounterEntry.setStatus("current")


class _DocsIfCmtsUpChnlCtrId_Type(Integer32):
    """Custom type docsIfCmtsUpChnlCtrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIfCmtsUpChnlCtrId_Type.__name__ = "Integer32"
_DocsIfCmtsUpChnlCtrId_Object = MibTableColumn
docsIfCmtsUpChnlCtrId = _DocsIfCmtsUpChnlCtrId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 1),
    _DocsIfCmtsUpChnlCtrId_Type()
)
docsIfCmtsUpChnlCtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrId.setStatus("current")
_DocsIfCmtsUpChnlCtrTotalMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrTotalMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrTotalMslots = _DocsIfCmtsUpChnlCtrTotalMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 2),
    _DocsIfCmtsUpChnlCtrTotalMslots_Type()
)
docsIfCmtsUpChnlCtrTotalMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrTotalMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrUcastGrantedMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrUcastGrantedMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrUcastGrantedMslots = _DocsIfCmtsUpChnlCtrUcastGrantedMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 3),
    _DocsIfCmtsUpChnlCtrUcastGrantedMslots_Type()
)
docsIfCmtsUpChnlCtrUcastGrantedMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrUcastGrantedMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrTotalCntnMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrTotalCntnMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrTotalCntnMslots = _DocsIfCmtsUpChnlCtrTotalCntnMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 4),
    _DocsIfCmtsUpChnlCtrTotalCntnMslots_Type()
)
docsIfCmtsUpChnlCtrTotalCntnMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrTotalCntnMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrUsedCntnMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrUsedCntnMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrUsedCntnMslots = _DocsIfCmtsUpChnlCtrUsedCntnMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 5),
    _DocsIfCmtsUpChnlCtrUsedCntnMslots_Type()
)
docsIfCmtsUpChnlCtrUsedCntnMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrUsedCntnMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtTotalMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtTotalMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtTotalMslots = _DocsIfCmtsUpChnlCtrExtTotalMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 6),
    _DocsIfCmtsUpChnlCtrExtTotalMslots_Type()
)
docsIfCmtsUpChnlCtrExtTotalMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtTotalMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtUcastGrantedMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtUcastGrantedMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtUcastGrantedMslots = _DocsIfCmtsUpChnlCtrExtUcastGrantedMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 7),
    _DocsIfCmtsUpChnlCtrExtUcastGrantedMslots_Type()
)
docsIfCmtsUpChnlCtrExtUcastGrantedMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtUcastGrantedMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtTotalCntnMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtTotalCntnMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtTotalCntnMslots = _DocsIfCmtsUpChnlCtrExtTotalCntnMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 8),
    _DocsIfCmtsUpChnlCtrExtTotalCntnMslots_Type()
)
docsIfCmtsUpChnlCtrExtTotalCntnMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtTotalCntnMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtUsedCntnMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtUsedCntnMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtUsedCntnMslots = _DocsIfCmtsUpChnlCtrExtUsedCntnMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 9),
    _DocsIfCmtsUpChnlCtrExtUsedCntnMslots_Type()
)
docsIfCmtsUpChnlCtrExtUsedCntnMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtUsedCntnMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrCollCntnMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrCollCntnMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrCollCntnMslots = _DocsIfCmtsUpChnlCtrCollCntnMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 10),
    _DocsIfCmtsUpChnlCtrCollCntnMslots_Type()
)
docsIfCmtsUpChnlCtrCollCntnMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrCollCntnMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrTotalCntnReqMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrTotalCntnReqMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrTotalCntnReqMslots = _DocsIfCmtsUpChnlCtrTotalCntnReqMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 11),
    _DocsIfCmtsUpChnlCtrTotalCntnReqMslots_Type()
)
docsIfCmtsUpChnlCtrTotalCntnReqMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrTotalCntnReqMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrUsedCntnReqMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrUsedCntnReqMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrUsedCntnReqMslots = _DocsIfCmtsUpChnlCtrUsedCntnReqMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 12),
    _DocsIfCmtsUpChnlCtrUsedCntnReqMslots_Type()
)
docsIfCmtsUpChnlCtrUsedCntnReqMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrUsedCntnReqMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrCollCntnReqMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrCollCntnReqMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrCollCntnReqMslots = _DocsIfCmtsUpChnlCtrCollCntnReqMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 13),
    _DocsIfCmtsUpChnlCtrCollCntnReqMslots_Type()
)
docsIfCmtsUpChnlCtrCollCntnReqMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrCollCntnReqMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrTotalCntnReqDataMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrTotalCntnReqDataMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrTotalCntnReqDataMslots = _DocsIfCmtsUpChnlCtrTotalCntnReqDataMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 14),
    _DocsIfCmtsUpChnlCtrTotalCntnReqDataMslots_Type()
)
docsIfCmtsUpChnlCtrTotalCntnReqDataMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrTotalCntnReqDataMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrUsedCntnReqDataMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrUsedCntnReqDataMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrUsedCntnReqDataMslots = _DocsIfCmtsUpChnlCtrUsedCntnReqDataMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 15),
    _DocsIfCmtsUpChnlCtrUsedCntnReqDataMslots_Type()
)
docsIfCmtsUpChnlCtrUsedCntnReqDataMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrUsedCntnReqDataMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrCollCntnReqDataMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrCollCntnReqDataMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrCollCntnReqDataMslots = _DocsIfCmtsUpChnlCtrCollCntnReqDataMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 16),
    _DocsIfCmtsUpChnlCtrCollCntnReqDataMslots_Type()
)
docsIfCmtsUpChnlCtrCollCntnReqDataMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrCollCntnReqDataMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrTotalCntnInitMaintMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrTotalCntnInitMaintMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots = _DocsIfCmtsUpChnlCtrTotalCntnInitMaintMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 17),
    _DocsIfCmtsUpChnlCtrTotalCntnInitMaintMslots_Type()
)
docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrUsedCntnInitMaintMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrUsedCntnInitMaintMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots = _DocsIfCmtsUpChnlCtrUsedCntnInitMaintMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 18),
    _DocsIfCmtsUpChnlCtrUsedCntnInitMaintMslots_Type()
)
docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrCollCntnInitMaintMslots_Type = Counter32
_DocsIfCmtsUpChnlCtrCollCntnInitMaintMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrCollCntnInitMaintMslots = _DocsIfCmtsUpChnlCtrCollCntnInitMaintMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 19),
    _DocsIfCmtsUpChnlCtrCollCntnInitMaintMslots_Type()
)
docsIfCmtsUpChnlCtrCollCntnInitMaintMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrCollCntnInitMaintMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtCollCntnMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtCollCntnMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtCollCntnMslots = _DocsIfCmtsUpChnlCtrExtCollCntnMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 20),
    _DocsIfCmtsUpChnlCtrExtCollCntnMslots_Type()
)
docsIfCmtsUpChnlCtrExtCollCntnMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtCollCntnMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtTotalCntnReqMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtTotalCntnReqMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtTotalCntnReqMslots = _DocsIfCmtsUpChnlCtrExtTotalCntnReqMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 21),
    _DocsIfCmtsUpChnlCtrExtTotalCntnReqMslots_Type()
)
docsIfCmtsUpChnlCtrExtTotalCntnReqMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtTotalCntnReqMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtUsedCntnReqMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtUsedCntnReqMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtUsedCntnReqMslots = _DocsIfCmtsUpChnlCtrExtUsedCntnReqMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 22),
    _DocsIfCmtsUpChnlCtrExtUsedCntnReqMslots_Type()
)
docsIfCmtsUpChnlCtrExtUsedCntnReqMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtUsedCntnReqMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtCollCntnReqMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtCollCntnReqMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtCollCntnReqMslots = _DocsIfCmtsUpChnlCtrExtCollCntnReqMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 23),
    _DocsIfCmtsUpChnlCtrExtCollCntnReqMslots_Type()
)
docsIfCmtsUpChnlCtrExtCollCntnReqMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtCollCntnReqMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots = _DocsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 24),
    _DocsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots_Type()
)
docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots = _DocsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 25),
    _DocsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots_Type()
)
docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtCollCntnReqDataMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtCollCntnReqDataMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots = _DocsIfCmtsUpChnlCtrExtCollCntnReqDataMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 26),
    _DocsIfCmtsUpChnlCtrExtCollCntnReqDataMslots_Type()
)
docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots = _DocsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 27),
    _DocsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots_Type()
)
docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots = _DocsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 28),
    _DocsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots_Type()
)
docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots.setStatus("current")
_DocsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots_Type = Counter64
_DocsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots_Object = MibTableColumn
docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots = _DocsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 11, 1, 29),
    _DocsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots_Type()
)
docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots.setStatus("current")
_DocsIfNotification_ObjectIdentity = ObjectIdentity
docsIfNotification = _DocsIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 2)
)
_DocsIfConformance_ObjectIdentity = ObjectIdentity
docsIfConformance = _DocsIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 3)
)
_DocsIfCompliances_ObjectIdentity = ObjectIdentity
docsIfCompliances = _DocsIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 1)
)
_DocsIfGroups_ObjectIdentity = ObjectIdentity
docsIfGroups = _DocsIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 2)
)
_DocsIfCompliancesV2_ObjectIdentity = ObjectIdentity
docsIfCompliancesV2 = _DocsIfCompliancesV2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 3)
)
_DocsIfGroupsV2_ObjectIdentity = ObjectIdentity
docsIfGroupsV2 = _DocsIfGroupsV2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 4)
)

# Managed Objects groups

docsIfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 1)
)
docsIfBasicGroup.setObjects(
      *(("DOCS-IETF-RFI-MIB", "docsIfDownChannelId"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelFrequency"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelWidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelModulation"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelInterleave"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelPower"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelId"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelFrequency"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelWidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelModulationProfile"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelSlotSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelTxTimingOffset"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelRangingBackoffStart"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelRangingBackoffEnd"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelTxBackoffStart"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelTxBackoffEnd"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfPriority"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfMaxUpBandwidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfGuarUpBandwidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfMaxDownBandwidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfMaxTxBurst"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfBaselinePrivacy"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfStatus"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQIncludesContention"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQUnerroreds"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQCorrecteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQUncorrectables"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQSignalNoise"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQMicroreflections"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQEqualizationData"))
)
if mibBuilder.loadTexts:
    docsIfBasicGroup.setStatus("current")

docsIfCmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 2)
)
docsIfCmGroup.setObjects(
      *(("DOCS-IETF-RFI-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmCapabilities"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmRangingTimeout"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusValue"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusCode"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusTxPower"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusResets"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusLostSyncs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidMaps"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidUcds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidRangingResponses"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidRegistrationResponses"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT1Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT2Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT3Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT4Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusRangingAborteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceQosProfile"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxSlotsImmed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxSlotsDed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxRetries"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxExceededs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceRqRetries"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceRqExceededs"))
)
if mibBuilder.loadTexts:
    docsIfCmGroup.setStatus("current")

docsIfCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 3)
)
docsIfCmtsGroup.setObjects(
      *(("DOCS-IETF-RFI-MIB", "docsIfCmtsCapabilities"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsSyncInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUcdInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsMaxServiceIds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsInvitedRangingAttempts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsInsertInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusInvalidRangeReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusRangingAborteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusInvalidRegReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusFailedRegReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusInvalidDataReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusT5Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusIpAddress"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusRxPower"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusTimingOffset"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusEqualizationData"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusValue"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusUnerroreds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusCorrecteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusUncorrectables"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusSignalNoise"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusMicroreflections"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceCmStatusIndex"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceAdminStatus"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceQosProfile"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceCreateTime"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceInOctets"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceInPackets"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModControl"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModPreambleLen"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModDifferentialEncoding"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModFECErrorCorrection"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModFECCodewordLength"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScramblerSeed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModMaxBurstSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModGuardTimeSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModLastCodewordShortened"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScrambler"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsQosProfilePermissions"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmPtr"))
)
if mibBuilder.loadTexts:
    docsIfCmtsGroup.setStatus("current")

docsIfBasicGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 4, 1)
)
docsIfBasicGroupV2.setObjects(
      *(("DOCS-IETF-RFI-MIB", "docsIfDownChannelId"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelFrequency"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelWidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelModulation"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelInterleave"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelPower"),
        ("DOCS-IETF-RFI-MIB", "docsIfDownChannelAnnex"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelId"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelFrequency"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelWidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelModulationProfile"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelSlotSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelTxTimingOffset"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelRangingBackoffStart"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelRangingBackoffEnd"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelTxBackoffStart"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelTxBackoffEnd"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelScdmaActiveCodes"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelScdmaCodesPerSlot"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelScdmaFrameSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelScdmaHoppingSeed"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelType"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelCloneFrom"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelUpdate"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelStatus"),
        ("DOCS-IETF-RFI-MIB", "docsIfUpChannelPreEqEnable"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfPriority"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfMaxUpBandwidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfGuarUpBandwidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfMaxDownBandwidth"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfBaselinePrivacy"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfStatus"),
        ("DOCS-IETF-RFI-MIB", "docsIfQosProfMaxTransmitBurst"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQIncludesContention"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQUnerroreds"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQCorrecteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQUncorrectables"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQSignalNoise"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQMicroreflections"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQEqualizationData"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQExtUnerroreds"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQExtCorrecteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfSigQExtUncorrectables"),
        ("DOCS-IETF-RFI-MIB", "docsIfDocsisBaseCapability"))
)
if mibBuilder.loadTexts:
    docsIfBasicGroupV2.setStatus("current")

docsIfCmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 4, 2)
)
docsIfCmGroupV2.setObjects(
      *(("DOCS-IETF-RFI-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmCapabilities"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmRangingTimeout"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusValue"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusCode"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusTxPower"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusResets"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusLostSyncs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidMaps"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidUcds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidRangingResponses"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusInvalidRegistrationResponses"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT1Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT2Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT3Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusT4Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusRangingAborteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusModulationType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmStatusEqualizationData"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceQosProfile"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxSlotsImmed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxSlotsDed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxRetries"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceTxExceededs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceRqRetries"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceRqExceededs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceExtTxSlotsImmed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmServiceExtTxSlotsDed"))
)
if mibBuilder.loadTexts:
    docsIfCmGroupV2.setStatus("current")

docsIfCmtsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 4, 3)
)
docsIfCmtsGroupV2.setObjects(
      *(("DOCS-IETF-RFI-MIB", "docsIfCmtsCapabilities"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsSyncInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUcdInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsMaxServiceIds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsInvitedRangingAttempts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsInsertInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusInvalidRangeReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusRangingAborteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusInvalidRegReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusFailedRegReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusInvalidDataReqs"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsStatusT5Timeouts"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusRxPower"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusTimingOffset"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusEqualizationData"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusValue"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusUnerroreds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusCorrecteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusUncorrectables"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusSignalNoise"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusMicroreflections"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusExtUnerroreds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusExtCorrecteds"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusExtUncorrectables"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusModulationType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusInetAddressType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmStatusInetAddress"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceAdminStatus"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceQosProfile"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceCreateTime"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceInOctets"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceInPackets"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsServiceNewCmStatusIndex"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModControl"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModPreambleLen"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModDifferentialEncoding"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModFECErrorCorrection"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModFECCodewordLength"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScramblerSeed"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModMaxBurstSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModGuardTimeSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModLastCodewordShortened"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScrambler"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModByteInterleaverDepth"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModByteInterleaverBlockSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModPreambleType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModTcmErrorCorrectionOn"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScdmaInterleaverStepSize"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScdmaSpreaderEnable"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModScdmaSubframeCodes"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsModChannelType"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsQosProfilePermissions"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsCmPtr"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsChannelUtilizationInterval"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsChannelUtUtilization"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsDownChnlCtrId"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsDownChnlCtrTotalBytes"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsDownChnlCtrUsedBytes"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsDownChnlCtrExtTotalBytes"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsDownChnlCtrExtUsedBytes"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrId"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrTotalMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrUcastGrantedMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrTotalCntnMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrUsedCntnMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtTotalMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtUcastGrantedMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtTotalCntnMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtUsedCntnMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrCollCntnMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrTotalCntnReqMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrUsedCntnReqMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrCollCntnReqMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrTotalCntnReqDataMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrUsedCntnReqDataMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrCollCntnReqDataMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrCollCntnInitMaintMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtCollCntnMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtTotalCntnReqMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtUsedCntnReqMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtCollCntnReqMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots"),
        ("DOCS-IETF-RFI-MIB", "docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots"))
)
if mibBuilder.loadTexts:
    docsIfCmtsGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsIfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfBasicCompliance.setStatus(
        "current"
    )

docsIfBasicComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 3, 3, 1)
)
if mibBuilder.loadTexts:
    docsIfBasicComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IETF-RFI-MIB",
    **{"TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "DocsisVersion": DocsisVersion,
       "DocsisQosVersion": DocsisQosVersion,
       "DocsisUpstreamType": DocsisUpstreamType,
       "DocsisUpstreamTypeStatus": DocsisUpstreamTypeStatus,
       "docsIfMib": docsIfMib,
       "docsIfMibObjects": docsIfMibObjects,
       "docsIfBaseObjects": docsIfBaseObjects,
       "docsIfDownstreamChannelTable": docsIfDownstreamChannelTable,
       "docsIfDownstreamChannelEntry": docsIfDownstreamChannelEntry,
       "docsIfDownChannelId": docsIfDownChannelId,
       "docsIfDownChannelFrequency": docsIfDownChannelFrequency,
       "docsIfDownChannelWidth": docsIfDownChannelWidth,
       "docsIfDownChannelModulation": docsIfDownChannelModulation,
       "docsIfDownChannelInterleave": docsIfDownChannelInterleave,
       "docsIfDownChannelPower": docsIfDownChannelPower,
       "docsIfDownChannelAnnex": docsIfDownChannelAnnex,
       "docsIfUpstreamChannelTable": docsIfUpstreamChannelTable,
       "docsIfUpstreamChannelEntry": docsIfUpstreamChannelEntry,
       "docsIfUpChannelId": docsIfUpChannelId,
       "docsIfUpChannelFrequency": docsIfUpChannelFrequency,
       "docsIfUpChannelWidth": docsIfUpChannelWidth,
       "docsIfUpChannelModulationProfile": docsIfUpChannelModulationProfile,
       "docsIfUpChannelSlotSize": docsIfUpChannelSlotSize,
       "docsIfUpChannelTxTimingOffset": docsIfUpChannelTxTimingOffset,
       "docsIfUpChannelRangingBackoffStart": docsIfUpChannelRangingBackoffStart,
       "docsIfUpChannelRangingBackoffEnd": docsIfUpChannelRangingBackoffEnd,
       "docsIfUpChannelTxBackoffStart": docsIfUpChannelTxBackoffStart,
       "docsIfUpChannelTxBackoffEnd": docsIfUpChannelTxBackoffEnd,
       "docsIfUpChannelScdmaActiveCodes": docsIfUpChannelScdmaActiveCodes,
       "docsIfUpChannelScdmaCodesPerSlot": docsIfUpChannelScdmaCodesPerSlot,
       "docsIfUpChannelScdmaFrameSize": docsIfUpChannelScdmaFrameSize,
       "docsIfUpChannelScdmaHoppingSeed": docsIfUpChannelScdmaHoppingSeed,
       "docsIfUpChannelType": docsIfUpChannelType,
       "docsIfUpChannelCloneFrom": docsIfUpChannelCloneFrom,
       "docsIfUpChannelUpdate": docsIfUpChannelUpdate,
       "docsIfUpChannelStatus": docsIfUpChannelStatus,
       "docsIfUpChannelPreEqEnable": docsIfUpChannelPreEqEnable,
       "docsIfQosProfileTable": docsIfQosProfileTable,
       "docsIfQosProfileEntry": docsIfQosProfileEntry,
       "docsIfQosProfIndex": docsIfQosProfIndex,
       "docsIfQosProfPriority": docsIfQosProfPriority,
       "docsIfQosProfMaxUpBandwidth": docsIfQosProfMaxUpBandwidth,
       "docsIfQosProfGuarUpBandwidth": docsIfQosProfGuarUpBandwidth,
       "docsIfQosProfMaxDownBandwidth": docsIfQosProfMaxDownBandwidth,
       "docsIfQosProfMaxTxBurst": docsIfQosProfMaxTxBurst,
       "docsIfQosProfBaselinePrivacy": docsIfQosProfBaselinePrivacy,
       "docsIfQosProfStatus": docsIfQosProfStatus,
       "docsIfQosProfMaxTransmitBurst": docsIfQosProfMaxTransmitBurst,
       "docsIfSignalQualityTable": docsIfSignalQualityTable,
       "docsIfSignalQualityEntry": docsIfSignalQualityEntry,
       "docsIfSigQIncludesContention": docsIfSigQIncludesContention,
       "docsIfSigQUnerroreds": docsIfSigQUnerroreds,
       "docsIfSigQCorrecteds": docsIfSigQCorrecteds,
       "docsIfSigQUncorrectables": docsIfSigQUncorrectables,
       "docsIfSigQSignalNoise": docsIfSigQSignalNoise,
       "docsIfSigQMicroreflections": docsIfSigQMicroreflections,
       "docsIfSigQEqualizationData": docsIfSigQEqualizationData,
       "docsIfSigQExtUnerroreds": docsIfSigQExtUnerroreds,
       "docsIfSigQExtCorrecteds": docsIfSigQExtCorrecteds,
       "docsIfSigQExtUncorrectables": docsIfSigQExtUncorrectables,
       "docsIfDocsisBaseCapability": docsIfDocsisBaseCapability,
       "docsIfCmObjects": docsIfCmObjects,
       "docsIfCmMacTable": docsIfCmMacTable,
       "docsIfCmMacEntry": docsIfCmMacEntry,
       "docsIfCmCmtsAddress": docsIfCmCmtsAddress,
       "docsIfCmCapabilities": docsIfCmCapabilities,
       "docsIfCmRangingRespTimeout": docsIfCmRangingRespTimeout,
       "docsIfCmRangingTimeout": docsIfCmRangingTimeout,
       "docsIfCmStatusTable": docsIfCmStatusTable,
       "docsIfCmStatusEntry": docsIfCmStatusEntry,
       "docsIfCmStatusValue": docsIfCmStatusValue,
       "docsIfCmStatusCode": docsIfCmStatusCode,
       "docsIfCmStatusTxPower": docsIfCmStatusTxPower,
       "docsIfCmStatusResets": docsIfCmStatusResets,
       "docsIfCmStatusLostSyncs": docsIfCmStatusLostSyncs,
       "docsIfCmStatusInvalidMaps": docsIfCmStatusInvalidMaps,
       "docsIfCmStatusInvalidUcds": docsIfCmStatusInvalidUcds,
       "docsIfCmStatusInvalidRangingResponses": docsIfCmStatusInvalidRangingResponses,
       "docsIfCmStatusInvalidRegistrationResponses": docsIfCmStatusInvalidRegistrationResponses,
       "docsIfCmStatusT1Timeouts": docsIfCmStatusT1Timeouts,
       "docsIfCmStatusT2Timeouts": docsIfCmStatusT2Timeouts,
       "docsIfCmStatusT3Timeouts": docsIfCmStatusT3Timeouts,
       "docsIfCmStatusT4Timeouts": docsIfCmStatusT4Timeouts,
       "docsIfCmStatusRangingAborteds": docsIfCmStatusRangingAborteds,
       "docsIfCmStatusDocsisOperMode": docsIfCmStatusDocsisOperMode,
       "docsIfCmStatusModulationType": docsIfCmStatusModulationType,
       "docsIfCmStatusEqualizationData": docsIfCmStatusEqualizationData,
       "docsIfCmServiceTable": docsIfCmServiceTable,
       "docsIfCmServiceEntry": docsIfCmServiceEntry,
       "docsIfCmServiceId": docsIfCmServiceId,
       "docsIfCmServiceQosProfile": docsIfCmServiceQosProfile,
       "docsIfCmServiceTxSlotsImmed": docsIfCmServiceTxSlotsImmed,
       "docsIfCmServiceTxSlotsDed": docsIfCmServiceTxSlotsDed,
       "docsIfCmServiceTxRetries": docsIfCmServiceTxRetries,
       "docsIfCmServiceTxExceededs": docsIfCmServiceTxExceededs,
       "docsIfCmServiceRqRetries": docsIfCmServiceRqRetries,
       "docsIfCmServiceRqExceededs": docsIfCmServiceRqExceededs,
       "docsIfCmServiceExtTxSlotsImmed": docsIfCmServiceExtTxSlotsImmed,
       "docsIfCmServiceExtTxSlotsDed": docsIfCmServiceExtTxSlotsDed,
       "docsIfCmtsObjects": docsIfCmtsObjects,
       "docsIfCmtsMacTable": docsIfCmtsMacTable,
       "docsIfCmtsMacEntry": docsIfCmtsMacEntry,
       "docsIfCmtsCapabilities": docsIfCmtsCapabilities,
       "docsIfCmtsSyncInterval": docsIfCmtsSyncInterval,
       "docsIfCmtsUcdInterval": docsIfCmtsUcdInterval,
       "docsIfCmtsMaxServiceIds": docsIfCmtsMaxServiceIds,
       "docsIfCmtsInsertionInterval": docsIfCmtsInsertionInterval,
       "docsIfCmtsInvitedRangingAttempts": docsIfCmtsInvitedRangingAttempts,
       "docsIfCmtsInsertInterval": docsIfCmtsInsertInterval,
       "docsIfCmtsStatusTable": docsIfCmtsStatusTable,
       "docsIfCmtsStatusEntry": docsIfCmtsStatusEntry,
       "docsIfCmtsStatusInvalidRangeReqs": docsIfCmtsStatusInvalidRangeReqs,
       "docsIfCmtsStatusRangingAborteds": docsIfCmtsStatusRangingAborteds,
       "docsIfCmtsStatusInvalidRegReqs": docsIfCmtsStatusInvalidRegReqs,
       "docsIfCmtsStatusFailedRegReqs": docsIfCmtsStatusFailedRegReqs,
       "docsIfCmtsStatusInvalidDataReqs": docsIfCmtsStatusInvalidDataReqs,
       "docsIfCmtsStatusT5Timeouts": docsIfCmtsStatusT5Timeouts,
       "docsIfCmtsCmStatusTable": docsIfCmtsCmStatusTable,
       "docsIfCmtsCmStatusEntry": docsIfCmtsCmStatusEntry,
       "docsIfCmtsCmStatusIndex": docsIfCmtsCmStatusIndex,
       "docsIfCmtsCmStatusMacAddress": docsIfCmtsCmStatusMacAddress,
       "docsIfCmtsCmStatusIpAddress": docsIfCmtsCmStatusIpAddress,
       "docsIfCmtsCmStatusDownChannelIfIndex": docsIfCmtsCmStatusDownChannelIfIndex,
       "docsIfCmtsCmStatusUpChannelIfIndex": docsIfCmtsCmStatusUpChannelIfIndex,
       "docsIfCmtsCmStatusRxPower": docsIfCmtsCmStatusRxPower,
       "docsIfCmtsCmStatusTimingOffset": docsIfCmtsCmStatusTimingOffset,
       "docsIfCmtsCmStatusEqualizationData": docsIfCmtsCmStatusEqualizationData,
       "docsIfCmtsCmStatusValue": docsIfCmtsCmStatusValue,
       "docsIfCmtsCmStatusUnerroreds": docsIfCmtsCmStatusUnerroreds,
       "docsIfCmtsCmStatusCorrecteds": docsIfCmtsCmStatusCorrecteds,
       "docsIfCmtsCmStatusUncorrectables": docsIfCmtsCmStatusUncorrectables,
       "docsIfCmtsCmStatusSignalNoise": docsIfCmtsCmStatusSignalNoise,
       "docsIfCmtsCmStatusMicroreflections": docsIfCmtsCmStatusMicroreflections,
       "docsIfCmtsCmStatusExtUnerroreds": docsIfCmtsCmStatusExtUnerroreds,
       "docsIfCmtsCmStatusExtCorrecteds": docsIfCmtsCmStatusExtCorrecteds,
       "docsIfCmtsCmStatusExtUncorrectables": docsIfCmtsCmStatusExtUncorrectables,
       "docsIfCmtsCmStatusDocsisRegMode": docsIfCmtsCmStatusDocsisRegMode,
       "docsIfCmtsCmStatusModulationType": docsIfCmtsCmStatusModulationType,
       "docsIfCmtsCmStatusInetAddressType": docsIfCmtsCmStatusInetAddressType,
       "docsIfCmtsCmStatusInetAddress": docsIfCmtsCmStatusInetAddress,
       "docsIfCmtsServiceTable": docsIfCmtsServiceTable,
       "docsIfCmtsServiceEntry": docsIfCmtsServiceEntry,
       "docsIfCmtsServiceId": docsIfCmtsServiceId,
       "docsIfCmtsServiceCmStatusIndex": docsIfCmtsServiceCmStatusIndex,
       "docsIfCmtsServiceAdminStatus": docsIfCmtsServiceAdminStatus,
       "docsIfCmtsServiceQosProfile": docsIfCmtsServiceQosProfile,
       "docsIfCmtsServiceCreateTime": docsIfCmtsServiceCreateTime,
       "docsIfCmtsServiceInOctets": docsIfCmtsServiceInOctets,
       "docsIfCmtsServiceInPackets": docsIfCmtsServiceInPackets,
       "docsIfCmtsServiceNewCmStatusIndex": docsIfCmtsServiceNewCmStatusIndex,
       "docsIfCmtsModulationTable": docsIfCmtsModulationTable,
       "docsIfCmtsModulationEntry": docsIfCmtsModulationEntry,
       "docsIfCmtsModIndex": docsIfCmtsModIndex,
       "docsIfCmtsModIntervalUsageCode": docsIfCmtsModIntervalUsageCode,
       "docsIfCmtsModControl": docsIfCmtsModControl,
       "docsIfCmtsModType": docsIfCmtsModType,
       "docsIfCmtsModPreambleLen": docsIfCmtsModPreambleLen,
       "docsIfCmtsModDifferentialEncoding": docsIfCmtsModDifferentialEncoding,
       "docsIfCmtsModFECErrorCorrection": docsIfCmtsModFECErrorCorrection,
       "docsIfCmtsModFECCodewordLength": docsIfCmtsModFECCodewordLength,
       "docsIfCmtsModScramblerSeed": docsIfCmtsModScramblerSeed,
       "docsIfCmtsModMaxBurstSize": docsIfCmtsModMaxBurstSize,
       "docsIfCmtsModGuardTimeSize": docsIfCmtsModGuardTimeSize,
       "docsIfCmtsModLastCodewordShortened": docsIfCmtsModLastCodewordShortened,
       "docsIfCmtsModScrambler": docsIfCmtsModScrambler,
       "docsIfCmtsModByteInterleaverDepth": docsIfCmtsModByteInterleaverDepth,
       "docsIfCmtsModByteInterleaverBlockSize": docsIfCmtsModByteInterleaverBlockSize,
       "docsIfCmtsModPreambleType": docsIfCmtsModPreambleType,
       "docsIfCmtsModTcmErrorCorrectionOn": docsIfCmtsModTcmErrorCorrectionOn,
       "docsIfCmtsModScdmaInterleaverStepSize": docsIfCmtsModScdmaInterleaverStepSize,
       "docsIfCmtsModScdmaSpreaderEnable": docsIfCmtsModScdmaSpreaderEnable,
       "docsIfCmtsModScdmaSubframeCodes": docsIfCmtsModScdmaSubframeCodes,
       "docsIfCmtsModChannelType": docsIfCmtsModChannelType,
       "docsIfCmtsQosProfilePermissions": docsIfCmtsQosProfilePermissions,
       "docsIfCmtsMacToCmTable": docsIfCmtsMacToCmTable,
       "docsIfCmtsMacToCmEntry": docsIfCmtsMacToCmEntry,
       "docsIfCmtsCmMac": docsIfCmtsCmMac,
       "docsIfCmtsCmPtr": docsIfCmtsCmPtr,
       "docsIfCmtsChannelUtilizationInterval": docsIfCmtsChannelUtilizationInterval,
       "docsIfCmtsChannelUtilizationTable": docsIfCmtsChannelUtilizationTable,
       "docsIfCmtsChannelUtilizationEntry": docsIfCmtsChannelUtilizationEntry,
       "docsIfCmtsChannelUtIfType": docsIfCmtsChannelUtIfType,
       "docsIfCmtsChannelUtId": docsIfCmtsChannelUtId,
       "docsIfCmtsChannelUtUtilization": docsIfCmtsChannelUtUtilization,
       "docsIfCmtsDownChannelCounterTable": docsIfCmtsDownChannelCounterTable,
       "docsIfCmtsDownChannelCounterEntry": docsIfCmtsDownChannelCounterEntry,
       "docsIfCmtsDownChnlCtrId": docsIfCmtsDownChnlCtrId,
       "docsIfCmtsDownChnlCtrTotalBytes": docsIfCmtsDownChnlCtrTotalBytes,
       "docsIfCmtsDownChnlCtrUsedBytes": docsIfCmtsDownChnlCtrUsedBytes,
       "docsIfCmtsDownChnlCtrExtTotalBytes": docsIfCmtsDownChnlCtrExtTotalBytes,
       "docsIfCmtsDownChnlCtrExtUsedBytes": docsIfCmtsDownChnlCtrExtUsedBytes,
       "docsIfCmtsUpChannelCounterTable": docsIfCmtsUpChannelCounterTable,
       "docsIfCmtsUpChannelCounterEntry": docsIfCmtsUpChannelCounterEntry,
       "docsIfCmtsUpChnlCtrId": docsIfCmtsUpChnlCtrId,
       "docsIfCmtsUpChnlCtrTotalMslots": docsIfCmtsUpChnlCtrTotalMslots,
       "docsIfCmtsUpChnlCtrUcastGrantedMslots": docsIfCmtsUpChnlCtrUcastGrantedMslots,
       "docsIfCmtsUpChnlCtrTotalCntnMslots": docsIfCmtsUpChnlCtrTotalCntnMslots,
       "docsIfCmtsUpChnlCtrUsedCntnMslots": docsIfCmtsUpChnlCtrUsedCntnMslots,
       "docsIfCmtsUpChnlCtrExtTotalMslots": docsIfCmtsUpChnlCtrExtTotalMslots,
       "docsIfCmtsUpChnlCtrExtUcastGrantedMslots": docsIfCmtsUpChnlCtrExtUcastGrantedMslots,
       "docsIfCmtsUpChnlCtrExtTotalCntnMslots": docsIfCmtsUpChnlCtrExtTotalCntnMslots,
       "docsIfCmtsUpChnlCtrExtUsedCntnMslots": docsIfCmtsUpChnlCtrExtUsedCntnMslots,
       "docsIfCmtsUpChnlCtrCollCntnMslots": docsIfCmtsUpChnlCtrCollCntnMslots,
       "docsIfCmtsUpChnlCtrTotalCntnReqMslots": docsIfCmtsUpChnlCtrTotalCntnReqMslots,
       "docsIfCmtsUpChnlCtrUsedCntnReqMslots": docsIfCmtsUpChnlCtrUsedCntnReqMslots,
       "docsIfCmtsUpChnlCtrCollCntnReqMslots": docsIfCmtsUpChnlCtrCollCntnReqMslots,
       "docsIfCmtsUpChnlCtrTotalCntnReqDataMslots": docsIfCmtsUpChnlCtrTotalCntnReqDataMslots,
       "docsIfCmtsUpChnlCtrUsedCntnReqDataMslots": docsIfCmtsUpChnlCtrUsedCntnReqDataMslots,
       "docsIfCmtsUpChnlCtrCollCntnReqDataMslots": docsIfCmtsUpChnlCtrCollCntnReqDataMslots,
       "docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots": docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots,
       "docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots": docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots,
       "docsIfCmtsUpChnlCtrCollCntnInitMaintMslots": docsIfCmtsUpChnlCtrCollCntnInitMaintMslots,
       "docsIfCmtsUpChnlCtrExtCollCntnMslots": docsIfCmtsUpChnlCtrExtCollCntnMslots,
       "docsIfCmtsUpChnlCtrExtTotalCntnReqMslots": docsIfCmtsUpChnlCtrExtTotalCntnReqMslots,
       "docsIfCmtsUpChnlCtrExtUsedCntnReqMslots": docsIfCmtsUpChnlCtrExtUsedCntnReqMslots,
       "docsIfCmtsUpChnlCtrExtCollCntnReqMslots": docsIfCmtsUpChnlCtrExtCollCntnReqMslots,
       "docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots": docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots,
       "docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots": docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots,
       "docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots": docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots,
       "docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots": docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots,
       "docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots": docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots,
       "docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots": docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots,
       "docsIfNotification": docsIfNotification,
       "docsIfConformance": docsIfConformance,
       "docsIfCompliances": docsIfCompliances,
       "docsIfBasicCompliance": docsIfBasicCompliance,
       "docsIfGroups": docsIfGroups,
       "docsIfBasicGroup": docsIfBasicGroup,
       "docsIfCmGroup": docsIfCmGroup,
       "docsIfCmtsGroup": docsIfCmtsGroup,
       "docsIfCompliancesV2": docsIfCompliancesV2,
       "docsIfBasicComplianceV2": docsIfBasicComplianceV2,
       "docsIfGroupsV2": docsIfGroupsV2,
       "docsIfBasicGroupV2": docsIfBasicGroupV2,
       "docsIfCmGroupV2": docsIfCmGroupV2,
       "docsIfCmtsGroupV2": docsIfCmtsGroupV2}
)
