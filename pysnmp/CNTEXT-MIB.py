# SNMP MIB module (CNTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:02 2024
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

(cntExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "cntExt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apCntExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApCntRuleOrder_Type(Integer32):
    """Custom type apCntRuleOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cacheRuleFirst", 1),
          ("hierarchicalFirst", 0))
    )


_ApCntRuleOrder_Type.__name__ = "Integer32"
_ApCntRuleOrder_Object = MibScalar
apCntRuleOrder = _ApCntRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 2),
    _ApCntRuleOrder_Type()
)
apCntRuleOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntRuleOrder.setStatus("current")
_ApCntTable_Object = MibTable
apCntTable = _ApCntTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4)
)
if mibBuilder.loadTexts:
    apCntTable.setStatus("current")
_ApCntEntry_Object = MibTableRow
apCntEntry = _ApCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1)
)
apCntEntry.setIndexNames(
    (0, "CNTEXT-MIB", "apCntOwner"),
    (0, "CNTEXT-MIB", "apCntName"),
)
if mibBuilder.loadTexts:
    apCntEntry.setStatus("current")


class _ApCntOwner_Type(DisplayString):
    """Custom type apCntOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntOwner_Type.__name__ = "DisplayString"
_ApCntOwner_Object = MibTableColumn
apCntOwner = _ApCntOwner_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 1),
    _ApCntOwner_Type()
)
apCntOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntOwner.setStatus("current")


class _ApCntName_Type(DisplayString):
    """Custom type apCntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntName_Type.__name__ = "DisplayString"
_ApCntName_Object = MibTableColumn
apCntName = _ApCntName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 2),
    _ApCntName_Type()
)
apCntName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntName.setStatus("current")
_ApCntIndex_Type = Integer32
_ApCntIndex_Object = MibTableColumn
apCntIndex = _ApCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 3),
    _ApCntIndex_Type()
)
apCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntIndex.setStatus("current")
_ApCntIPAddress_Type = IpAddress
_ApCntIPAddress_Object = MibTableColumn
apCntIPAddress = _ApCntIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 4),
    _ApCntIPAddress_Type()
)
apCntIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntIPAddress.setStatus("current")


class _ApCntIPProtocol_Type(Integer32):
    """Custom type apCntIPProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_ApCntIPProtocol_Type.__name__ = "Integer32"
_ApCntIPProtocol_Object = MibTableColumn
apCntIPProtocol = _ApCntIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 5),
    _ApCntIPProtocol_Type()
)
apCntIPProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntIPProtocol.setStatus("current")


class _ApCntPort_Type(Integer32):
    """Custom type apCntPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntPort_Type.__name__ = "Integer32"
_ApCntPort_Object = MibTableColumn
apCntPort = _ApCntPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 6),
    _ApCntPort_Type()
)
apCntPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntPort.setStatus("current")


class _ApCntUrl_Type(DisplayString):
    """Custom type apCntUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApCntUrl_Type.__name__ = "DisplayString"
_ApCntUrl_Object = MibTableColumn
apCntUrl = _ApCntUrl_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 7),
    _ApCntUrl_Type()
)
apCntUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntUrl.setStatus("current")


class _ApCntSticky_Type(Integer32):
    """Custom type apCntSticky based on Integer32"""
    defaultValue = 1

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
        *(("arrowpoint-cookie", 8),
          ("cookies", 5),
          ("cookieurl", 3),
          ("none", 1),
          ("ssl", 2),
          ("sticky-srcip", 7),
          ("sticky-srcip-dstport", 6),
          ("url", 4))
    )


_ApCntSticky_Type.__name__ = "Integer32"
_ApCntSticky_Object = MibTableColumn
apCntSticky = _ApCntSticky_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 8),
    _ApCntSticky_Type()
)
apCntSticky.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntSticky.setStatus("current")


class _ApCntBalance_Type(Integer32):
    """Custom type apCntBalance based on Integer32"""
    defaultValue = 1

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
        *(("aca", 2),
          ("destip", 3),
          ("domain", 5),
          ("domainhash", 9),
          ("leastconn", 7),
          ("roundrobin", 1),
          ("srcip", 4),
          ("url", 6),
          ("urlhash", 10),
          ("weightedrr", 8))
    )


_ApCntBalance_Type.__name__ = "Integer32"
_ApCntBalance_Object = MibTableColumn
apCntBalance = _ApCntBalance_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 9),
    _ApCntBalance_Type()
)
apCntBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntBalance.setStatus("current")


class _ApCntQOSTag_Type(Integer32):
    """Custom type apCntQOSTag based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ApCntQOSTag_Type.__name__ = "Integer32"
_ApCntQOSTag_Object = MibTableColumn
apCntQOSTag = _ApCntQOSTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 10),
    _ApCntQOSTag_Type()
)
apCntQOSTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntQOSTag.setStatus("current")


class _ApCntEnable_Type(Integer32):
    """Custom type apCntEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntEnable_Type.__name__ = "Integer32"
_ApCntEnable_Object = MibTableColumn
apCntEnable = _ApCntEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 11),
    _ApCntEnable_Type()
)
apCntEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntEnable.setStatus("current")


class _ApCntRedirect_Type(DisplayString):
    """Custom type apCntRedirect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApCntRedirect_Type.__name__ = "DisplayString"
_ApCntRedirect_Object = MibTableColumn
apCntRedirect = _ApCntRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 12),
    _ApCntRedirect_Type()
)
apCntRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntRedirect.setStatus("current")


class _ApCntDrop_Type(DisplayString):
    """Custom type apCntDrop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApCntDrop_Type.__name__ = "DisplayString"
_ApCntDrop_Object = MibTableColumn
apCntDrop = _ApCntDrop_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 13),
    _ApCntDrop_Type()
)
apCntDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntDrop.setStatus("current")


class _ApCntSize_Type(Integer32):
    """Custom type apCntSize based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntSize_Type.__name__ = "Integer32"
_ApCntSize_Object = MibTableColumn
apCntSize = _ApCntSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 14),
    _ApCntSize_Type()
)
apCntSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntSize.setStatus("obsolete")


class _ApCntPersistence_Type(Integer32):
    """Custom type apCntPersistence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntPersistence_Type.__name__ = "Integer32"
_ApCntPersistence_Object = MibTableColumn
apCntPersistence = _ApCntPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 15),
    _ApCntPersistence_Type()
)
apCntPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntPersistence.setStatus("current")


class _ApCntAuthor_Type(DisplayString):
    """Custom type apCntAuthor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApCntAuthor_Type.__name__ = "DisplayString"
_ApCntAuthor_Object = MibTableColumn
apCntAuthor = _ApCntAuthor_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 16),
    _ApCntAuthor_Type()
)
apCntAuthor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntAuthor.setStatus("current")


class _ApCntSpider_Type(Integer32):
    """Custom type apCntSpider based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntSpider_Type.__name__ = "Integer32"
_ApCntSpider_Object = MibTableColumn
apCntSpider = _ApCntSpider_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 17),
    _ApCntSpider_Type()
)
apCntSpider.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntSpider.setStatus("current")
_ApCntHits_Type = Counter32
_ApCntHits_Object = MibTableColumn
apCntHits = _ApCntHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 18),
    _ApCntHits_Type()
)
apCntHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntHits.setStatus("current")
_ApCntRedirects_Type = Counter32
_ApCntRedirects_Object = MibTableColumn
apCntRedirects = _ApCntRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 19),
    _ApCntRedirects_Type()
)
apCntRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntRedirects.setStatus("current")
_ApCntDrops_Type = Counter32
_ApCntDrops_Object = MibTableColumn
apCntDrops = _ApCntDrops_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 20),
    _ApCntDrops_Type()
)
apCntDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntDrops.setStatus("current")
_ApCntRejNoServices_Type = Counter32
_ApCntRejNoServices_Object = MibTableColumn
apCntRejNoServices = _ApCntRejNoServices_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 21),
    _ApCntRejNoServices_Type()
)
apCntRejNoServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntRejNoServices.setStatus("current")
_ApCntRejServOverload_Type = Counter32
_ApCntRejServOverload_Object = MibTableColumn
apCntRejServOverload = _ApCntRejServOverload_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 22),
    _ApCntRejServOverload_Type()
)
apCntRejServOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntRejServOverload.setStatus("current")
_ApCntSpoofs_Type = Counter32
_ApCntSpoofs_Object = MibTableColumn
apCntSpoofs = _ApCntSpoofs_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 23),
    _ApCntSpoofs_Type()
)
apCntSpoofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntSpoofs.setStatus("current")
_ApCntNats_Type = Counter32
_ApCntNats_Object = MibTableColumn
apCntNats = _ApCntNats_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 24),
    _ApCntNats_Type()
)
apCntNats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntNats.setStatus("current")
_ApCntByteCount_Type = Counter32
_ApCntByteCount_Object = MibTableColumn
apCntByteCount = _ApCntByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 25),
    _ApCntByteCount_Type()
)
apCntByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntByteCount.setStatus("current")
_ApCntFrameCount_Type = Counter32
_ApCntFrameCount_Object = MibTableColumn
apCntFrameCount = _ApCntFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 26),
    _ApCntFrameCount_Type()
)
apCntFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntFrameCount.setStatus("current")


class _ApCntZeroButton_Type(Integer32):
    """Custom type apCntZeroButton based on Integer32"""
    defaultValue = 0


_ApCntZeroButton_Object = MibTableColumn
apCntZeroButton = _ApCntZeroButton_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 27),
    _ApCntZeroButton_Type()
)
apCntZeroButton.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntZeroButton.setStatus("current")


class _ApCntHotListEnabled_Type(Integer32):
    """Custom type apCntHotListEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntHotListEnabled_Type.__name__ = "Integer32"
_ApCntHotListEnabled_Object = MibTableColumn
apCntHotListEnabled = _ApCntHotListEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 28),
    _ApCntHotListEnabled_Type()
)
apCntHotListEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntHotListEnabled.setStatus("current")


class _ApCntHotListSize_Type(Integer32):
    """Custom type apCntHotListSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApCntHotListSize_Type.__name__ = "Integer32"
_ApCntHotListSize_Object = MibTableColumn
apCntHotListSize = _ApCntHotListSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 29),
    _ApCntHotListSize_Type()
)
apCntHotListSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntHotListSize.setStatus("current")


class _ApCntHotListThreshold_Type(Integer32):
    """Custom type apCntHotListThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntHotListThreshold_Type.__name__ = "Integer32"
_ApCntHotListThreshold_Object = MibTableColumn
apCntHotListThreshold = _ApCntHotListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 30),
    _ApCntHotListThreshold_Type()
)
apCntHotListThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntHotListThreshold.setStatus("current")


class _ApCntHotListType_Type(Integer32):
    """Custom type apCntHotListType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("hitCount", 0)
    )


_ApCntHotListType_Type.__name__ = "Integer32"
_ApCntHotListType_Object = MibTableColumn
apCntHotListType = _ApCntHotListType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 31),
    _ApCntHotListType_Type()
)
apCntHotListType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntHotListType.setStatus("current")


class _ApCntHotListInterval_Type(Integer32):
    """Custom type apCntHotListInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ApCntHotListInterval_Type.__name__ = "Integer32"
_ApCntHotListInterval_Object = MibTableColumn
apCntHotListInterval = _ApCntHotListInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 32),
    _ApCntHotListInterval_Type()
)
apCntHotListInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntHotListInterval.setStatus("current")


class _ApCntFlowTrack_Type(Integer32):
    """Custom type apCntFlowTrack based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntFlowTrack_Type.__name__ = "Integer32"
_ApCntFlowTrack_Object = MibTableColumn
apCntFlowTrack = _ApCntFlowTrack_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 33),
    _ApCntFlowTrack_Type()
)
apCntFlowTrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntFlowTrack.setStatus("current")


class _ApCntWeightMask_Type(DisplayString):
    """Custom type apCntWeightMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApCntWeightMask_Type.__name__ = "DisplayString"
_ApCntWeightMask_Object = MibTableColumn
apCntWeightMask = _ApCntWeightMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 34),
    _ApCntWeightMask_Type()
)
apCntWeightMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntWeightMask.setStatus("current")
_ApCntStickyMask_Type = IpAddress
_ApCntStickyMask_Object = MibTableColumn
apCntStickyMask = _ApCntStickyMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 35),
    _ApCntStickyMask_Type()
)
apCntStickyMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyMask.setStatus("current")


class _ApCntCookieStartPos_Type(Integer32):
    """Custom type apCntCookieStartPos based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ApCntCookieStartPos_Type.__name__ = "Integer32"
_ApCntCookieStartPos_Object = MibTableColumn
apCntCookieStartPos = _ApCntCookieStartPos_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 36),
    _ApCntCookieStartPos_Type()
)
apCntCookieStartPos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntCookieStartPos.setStatus("current")


class _ApCntHeuristicCookieFence_Type(Integer32):
    """Custom type apCntHeuristicCookieFence based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApCntHeuristicCookieFence_Type.__name__ = "Integer32"
_ApCntHeuristicCookieFence_Object = MibTableColumn
apCntHeuristicCookieFence = _ApCntHeuristicCookieFence_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 37),
    _ApCntHeuristicCookieFence_Type()
)
apCntHeuristicCookieFence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntHeuristicCookieFence.setStatus("current")


class _ApCntEqlName_Type(DisplayString):
    """Custom type apCntEqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApCntEqlName_Type.__name__ = "DisplayString"
_ApCntEqlName_Object = MibTableColumn
apCntEqlName = _ApCntEqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 38),
    _ApCntEqlName_Type()
)
apCntEqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntEqlName.setStatus("current")


class _ApCntCacheFalloverType_Type(Integer32):
    """Custom type apCntCacheFalloverType based on Integer32"""
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
        *(("bypass", 3),
          ("linear", 1),
          ("next", 2))
    )


_ApCntCacheFalloverType_Type.__name__ = "Integer32"
_ApCntCacheFalloverType_Object = MibTableColumn
apCntCacheFalloverType = _ApCntCacheFalloverType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 39),
    _ApCntCacheFalloverType_Type()
)
apCntCacheFalloverType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntCacheFalloverType.setStatus("current")


class _ApCntLocalLoadThreshold_Type(Integer32):
    """Custom type apCntLocalLoadThreshold based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_ApCntLocalLoadThreshold_Type.__name__ = "Integer32"
_ApCntLocalLoadThreshold_Object = MibTableColumn
apCntLocalLoadThreshold = _ApCntLocalLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 40),
    _ApCntLocalLoadThreshold_Type()
)
apCntLocalLoadThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntLocalLoadThreshold.setStatus("current")
_ApCntStatus_Type = RowStatus
_ApCntStatus_Object = MibTableColumn
apCntStatus = _ApCntStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 41),
    _ApCntStatus_Type()
)
apCntStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStatus.setStatus("current")


class _ApCntRedirectLoadThreshold_Type(Integer32):
    """Custom type apCntRedirectLoadThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntRedirectLoadThreshold_Type.__name__ = "Integer32"
_ApCntRedirectLoadThreshold_Object = MibTableColumn
apCntRedirectLoadThreshold = _ApCntRedirectLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 42),
    _ApCntRedirectLoadThreshold_Type()
)
apCntRedirectLoadThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntRedirectLoadThreshold.setStatus("current")


class _ApCntContentType_Type(Integer32):
    """Custom type apCntContentType based on Integer32"""
    defaultValue = 1

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
        *(("bypass", 5),
          ("ftp-control", 2),
          ("ftp-publish", 6),
          ("http", 1),
          ("realaudio-control", 3),
          ("ssl", 4))
    )


_ApCntContentType_Type.__name__ = "Integer32"
_ApCntContentType_Object = MibTableColumn
apCntContentType = _ApCntContentType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 43),
    _ApCntContentType_Type()
)
apCntContentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntContentType.setStatus("current")


class _ApCntStickyInactivity_Type(Integer32):
    """Custom type apCntStickyInactivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntStickyInactivity_Type.__name__ = "Integer32"
_ApCntStickyInactivity_Object = MibTableColumn
apCntStickyInactivity = _ApCntStickyInactivity_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 44),
    _ApCntStickyInactivity_Type()
)
apCntStickyInactivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyInactivity.setStatus("current")


class _ApCntDNSBalance_Type(Integer32):
    """Custom type apCntDNSBalance based on Integer32"""
    defaultValue = 3

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
        *(("leastloaded", 4),
          ("preferlocal", 1),
          ("roundrobin", 2),
          ("useownerdnsbalance", 3))
    )


_ApCntDNSBalance_Type.__name__ = "Integer32"
_ApCntDNSBalance_Object = MibTableColumn
apCntDNSBalance = _ApCntDNSBalance_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 45),
    _ApCntDNSBalance_Type()
)
apCntDNSBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntDNSBalance.setStatus("current")


class _ApCntStickyGroup_Type(Integer32):
    """Custom type apCntStickyGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntStickyGroup_Type.__name__ = "Integer32"
_ApCntStickyGroup_Object = MibTableColumn
apCntStickyGroup = _ApCntStickyGroup_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 46),
    _ApCntStickyGroup_Type()
)
apCntStickyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyGroup.setStatus("current")
_ApCntAppTypeBypasses_Type = Counter32
_ApCntAppTypeBypasses_Object = MibTableColumn
apCntAppTypeBypasses = _ApCntAppTypeBypasses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 47),
    _ApCntAppTypeBypasses_Type()
)
apCntAppTypeBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAppTypeBypasses.setStatus("current")
_ApCntNoSvcBypasses_Type = Counter32
_ApCntNoSvcBypasses_Object = MibTableColumn
apCntNoSvcBypasses = _ApCntNoSvcBypasses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 48),
    _ApCntNoSvcBypasses_Type()
)
apCntNoSvcBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntNoSvcBypasses.setStatus("current")
_ApCntSvcLoadBypasses_Type = Counter32
_ApCntSvcLoadBypasses_Object = MibTableColumn
apCntSvcLoadBypasses = _ApCntSvcLoadBypasses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 49),
    _ApCntSvcLoadBypasses_Type()
)
apCntSvcLoadBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntSvcLoadBypasses.setStatus("current")
_ApCntConnCtBypasses_Type = Counter32
_ApCntConnCtBypasses_Object = MibTableColumn
apCntConnCtBypasses = _ApCntConnCtBypasses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 50),
    _ApCntConnCtBypasses_Type()
)
apCntConnCtBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntConnCtBypasses.setStatus("current")


class _ApCntUrqlTblName_Type(DisplayString):
    """Custom type apCntUrqlTblName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntUrqlTblName_Type.__name__ = "DisplayString"
_ApCntUrqlTblName_Object = MibTableColumn
apCntUrqlTblName = _ApCntUrqlTblName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 51),
    _ApCntUrqlTblName_Type()
)
apCntUrqlTblName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntUrqlTblName.setStatus("current")


class _ApCntStickyStrPre_Type(DisplayString):
    """Custom type apCntStickyStrPre based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApCntStickyStrPre_Type.__name__ = "DisplayString"
_ApCntStickyStrPre_Object = MibTableColumn
apCntStickyStrPre = _ApCntStickyStrPre_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 52),
    _ApCntStickyStrPre_Type()
)
apCntStickyStrPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrPre.setStatus("current")


class _ApCntStickyStrEos_Type(DisplayString):
    """Custom type apCntStickyStrEos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ApCntStickyStrEos_Type.__name__ = "DisplayString"
_ApCntStickyStrEos_Object = MibTableColumn
apCntStickyStrEos = _ApCntStickyStrEos_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 53),
    _ApCntStickyStrEos_Type()
)
apCntStickyStrEos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrEos.setStatus("current")


class _ApCntStickyStrSkipLen_Type(Integer32):
    """Custom type apCntStickyStrSkipLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ApCntStickyStrSkipLen_Type.__name__ = "Integer32"
_ApCntStickyStrSkipLen_Object = MibTableColumn
apCntStickyStrSkipLen = _ApCntStickyStrSkipLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 54),
    _ApCntStickyStrSkipLen_Type()
)
apCntStickyStrSkipLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrSkipLen.setStatus("current")


class _ApCntStickyStrProcLen_Type(Integer32):
    """Custom type apCntStickyStrProcLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ApCntStickyStrProcLen_Type.__name__ = "Integer32"
_ApCntStickyStrProcLen_Object = MibTableColumn
apCntStickyStrProcLen = _ApCntStickyStrProcLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 55),
    _ApCntStickyStrProcLen_Type()
)
apCntStickyStrProcLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrProcLen.setStatus("current")


class _ApCntStickyStrAction_Type(Integer32):
    """Custom type apCntStickyStrAction based on Integer32"""
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
        *(("hash-a", 1),
          ("hash-crc32", 3),
          ("hash-xor", 2),
          ("match-service-cookie", 4))
    )


_ApCntStickyStrAction_Type.__name__ = "Integer32"
_ApCntStickyStrAction_Object = MibTableColumn
apCntStickyStrAction = _ApCntStickyStrAction_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 56),
    _ApCntStickyStrAction_Type()
)
apCntStickyStrAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrAction.setStatus("current")


class _ApCntStickyStrAsciiConv_Type(Integer32):
    """Custom type apCntStickyStrAsciiConv based on Integer32"""
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


_ApCntStickyStrAsciiConv_Type.__name__ = "Integer32"
_ApCntStickyStrAsciiConv_Object = MibTableColumn
apCntStickyStrAsciiConv = _ApCntStickyStrAsciiConv_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 57),
    _ApCntStickyStrAsciiConv_Type()
)
apCntStickyStrAsciiConv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrAsciiConv.setStatus("current")


class _ApCntPrimarySorryServer_Type(DisplayString):
    """Custom type apCntPrimarySorryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntPrimarySorryServer_Type.__name__ = "DisplayString"
_ApCntPrimarySorryServer_Object = MibTableColumn
apCntPrimarySorryServer = _ApCntPrimarySorryServer_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 58),
    _ApCntPrimarySorryServer_Type()
)
apCntPrimarySorryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntPrimarySorryServer.setStatus("current")


class _ApCntSecondSorryServer_Type(DisplayString):
    """Custom type apCntSecondSorryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntSecondSorryServer_Type.__name__ = "DisplayString"
_ApCntSecondSorryServer_Object = MibTableColumn
apCntSecondSorryServer = _ApCntSecondSorryServer_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 59),
    _ApCntSecondSorryServer_Type()
)
apCntSecondSorryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntSecondSorryServer.setStatus("current")
_ApCntPrimarySorryHits_Type = Counter32
_ApCntPrimarySorryHits_Object = MibTableColumn
apCntPrimarySorryHits = _ApCntPrimarySorryHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 60),
    _ApCntPrimarySorryHits_Type()
)
apCntPrimarySorryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntPrimarySorryHits.setStatus("current")
_ApCntSecondSorryHits_Type = Counter32
_ApCntSecondSorryHits_Object = MibTableColumn
apCntSecondSorryHits = _ApCntSecondSorryHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 61),
    _ApCntSecondSorryHits_Type()
)
apCntSecondSorryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntSecondSorryHits.setStatus("current")


class _ApCntStickySrvrDownFailover_Type(Integer32):
    """Custom type apCntStickySrvrDownFailover based on Integer32"""
    defaultValue = 3

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
        *(("balance", 3),
          ("redirect", 2),
          ("reject", 1),
          ("sticky-srcip", 4),
          ("sticky-srcip-dstport", 5))
    )


_ApCntStickySrvrDownFailover_Type.__name__ = "Integer32"
_ApCntStickySrvrDownFailover_Object = MibTableColumn
apCntStickySrvrDownFailover = _ApCntStickySrvrDownFailover_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 62),
    _ApCntStickySrvrDownFailover_Type()
)
apCntStickySrvrDownFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickySrvrDownFailover.setStatus("current")


class _ApCntStickyStrType_Type(Integer32):
    """Custom type apCntStickyStrType based on Integer32"""
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
        *(("cookies", 3),
          ("cookieurl", 1),
          ("url", 2))
    )


_ApCntStickyStrType_Type.__name__ = "Integer32"
_ApCntStickyStrType_Object = MibTableColumn
apCntStickyStrType = _ApCntStickyStrType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 63),
    _ApCntStickyStrType_Type()
)
apCntStickyStrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyStrType.setStatus("current")


class _ApCntParamBypass_Type(Integer32):
    """Custom type apCntParamBypass based on Integer32"""
    defaultValue = 2

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


_ApCntParamBypass_Type.__name__ = "Integer32"
_ApCntParamBypass_Object = MibTableColumn
apCntParamBypass = _ApCntParamBypass_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 64),
    _ApCntParamBypass_Type()
)
apCntParamBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntParamBypass.setStatus("current")


class _ApCntAvgLocalLoad_Type(Integer32):
    """Custom type apCntAvgLocalLoad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntAvgLocalLoad_Type.__name__ = "Integer32"
_ApCntAvgLocalLoad_Object = MibTableColumn
apCntAvgLocalLoad = _ApCntAvgLocalLoad_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 65),
    _ApCntAvgLocalLoad_Type()
)
apCntAvgLocalLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAvgLocalLoad.setStatus("current")


class _ApCntAvgRemoteLoad_Type(Integer32):
    """Custom type apCntAvgRemoteLoad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntAvgRemoteLoad_Type.__name__ = "Integer32"
_ApCntAvgRemoteLoad_Object = MibTableColumn
apCntAvgRemoteLoad = _ApCntAvgRemoteLoad_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 66),
    _ApCntAvgRemoteLoad_Type()
)
apCntAvgRemoteLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAvgRemoteLoad.setStatus("current")


class _ApCntDqlName_Type(DisplayString):
    """Custom type apCntDqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntDqlName_Type.__name__ = "DisplayString"
_ApCntDqlName_Object = MibTableColumn
apCntDqlName = _ApCntDqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 67),
    _ApCntDqlName_Type()
)
apCntDqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntDqlName.setStatus("current")


class _ApCntIPAddressRange_Type(Integer32):
    """Custom type apCntIPAddressRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApCntIPAddressRange_Type.__name__ = "Integer32"
_ApCntIPAddressRange_Object = MibTableColumn
apCntIPAddressRange = _ApCntIPAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 68),
    _ApCntIPAddressRange_Type()
)
apCntIPAddressRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntIPAddressRange.setStatus("current")


class _ApCntTagListName_Type(DisplayString):
    """Custom type apCntTagListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntTagListName_Type.__name__ = "DisplayString"
_ApCntTagListName_Object = MibTableColumn
apCntTagListName = _ApCntTagListName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 69),
    _ApCntTagListName_Type()
)
apCntTagListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntTagListName.setStatus("current")


class _ApCntStickyNoCookieAction_Type(Integer32):
    """Custom type apCntStickyNoCookieAction based on Integer32"""
    defaultValue = 1

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
        *(("loadbalance", 1),
          ("redirect", 3),
          ("reject", 2),
          ("service", 4))
    )


_ApCntStickyNoCookieAction_Type.__name__ = "Integer32"
_ApCntStickyNoCookieAction_Object = MibTableColumn
apCntStickyNoCookieAction = _ApCntStickyNoCookieAction_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 70),
    _ApCntStickyNoCookieAction_Type()
)
apCntStickyNoCookieAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyNoCookieAction.setStatus("current")


class _ApCntStickyNoCookieString_Type(DisplayString):
    """Custom type apCntStickyNoCookieString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApCntStickyNoCookieString_Type.__name__ = "DisplayString"
_ApCntStickyNoCookieString_Object = MibTableColumn
apCntStickyNoCookieString = _ApCntStickyNoCookieString_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 71),
    _ApCntStickyNoCookieString_Type()
)
apCntStickyNoCookieString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyNoCookieString.setStatus("current")


class _ApCntStickyCookiePath_Type(DisplayString):
    """Custom type apCntStickyCookiePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_ApCntStickyCookiePath_Type.__name__ = "DisplayString"
_ApCntStickyCookiePath_Object = MibTableColumn
apCntStickyCookiePath = _ApCntStickyCookiePath_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 72),
    _ApCntStickyCookiePath_Type()
)
apCntStickyCookiePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyCookiePath.setStatus("current")


class _ApCntStickyCookieExp_Type(DisplayString):
    """Custom type apCntStickyCookieExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_ApCntStickyCookieExp_Type.__name__ = "DisplayString"
_ApCntStickyCookieExp_Object = MibTableColumn
apCntStickyCookieExp = _ApCntStickyCookieExp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 73),
    _ApCntStickyCookieExp_Type()
)
apCntStickyCookieExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyCookieExp.setStatus("current")


class _ApCntStickyCacheExp_Type(Integer32):
    """Custom type apCntStickyCacheExp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ApCntStickyCacheExp_Type.__name__ = "Integer32"
_ApCntStickyCacheExp_Object = MibTableColumn
apCntStickyCacheExp = _ApCntStickyCacheExp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 74),
    _ApCntStickyCacheExp_Type()
)
apCntStickyCacheExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntStickyCacheExp.setStatus("current")


class _ApCntTagWeight_Type(Integer32):
    """Custom type apCntTagWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ApCntTagWeight_Type.__name__ = "Integer32"
_ApCntTagWeight_Object = MibTableColumn
apCntTagWeight = _ApCntTagWeight_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 4, 1, 75),
    _ApCntTagWeight_Type()
)
apCntTagWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntTagWeight.setStatus("current")
_ApCntAclBypassCt_Type = Counter32
_ApCntAclBypassCt_Object = MibScalar
apCntAclBypassCt = _ApCntAclBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 5),
    _ApCntAclBypassCt_Type()
)
apCntAclBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAclBypassCt.setStatus("current")
_ApCntNoRuleBypassCt_Type = Counter32
_ApCntNoRuleBypassCt_Object = MibScalar
apCntNoRuleBypassCt = _ApCntNoRuleBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 6),
    _ApCntNoRuleBypassCt_Type()
)
apCntNoRuleBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntNoRuleBypassCt.setStatus("current")
_ApCntCacheMissBypassCt_Type = Counter32
_ApCntCacheMissBypassCt_Object = MibScalar
apCntCacheMissBypassCt = _ApCntCacheMissBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 7),
    _ApCntCacheMissBypassCt_Type()
)
apCntCacheMissBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntCacheMissBypassCt.setStatus("current")
_ApCntGarbageBypassCt_Type = Counter32
_ApCntGarbageBypassCt_Object = MibScalar
apCntGarbageBypassCt = _ApCntGarbageBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 8),
    _ApCntGarbageBypassCt_Type()
)
apCntGarbageBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntGarbageBypassCt.setStatus("current")
_ApCntUrlParamsBypassCt_Type = Counter32
_ApCntUrlParamsBypassCt_Object = MibScalar
apCntUrlParamsBypassCt = _ApCntUrlParamsBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 9),
    _ApCntUrlParamsBypassCt_Type()
)
apCntUrlParamsBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntUrlParamsBypassCt.setStatus("current")


class _ApCntBypassConnectionPersistence_Type(Integer32):
    """Custom type apCntBypassConnectionPersistence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntBypassConnectionPersistence_Type.__name__ = "Integer32"
_ApCntBypassConnectionPersistence_Object = MibScalar
apCntBypassConnectionPersistence = _ApCntBypassConnectionPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 10),
    _ApCntBypassConnectionPersistence_Type()
)
apCntBypassConnectionPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntBypassConnectionPersistence.setStatus("current")


class _ApCntPersistenceResetMethod_Type(Integer32):
    """Custom type apCntPersistenceResetMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("redirect", 0),
          ("remap", 1))
    )


_ApCntPersistenceResetMethod_Type.__name__ = "Integer32"
_ApCntPersistenceResetMethod_Object = MibScalar
apCntPersistenceResetMethod = _ApCntPersistenceResetMethod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 16, 11),
    _ApCntPersistenceResetMethod_Type()
)
apCntPersistenceResetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntPersistenceResetMethod.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNTEXT-MIB",
    **{"apCntExtMib": apCntExtMib,
       "apCntRuleOrder": apCntRuleOrder,
       "apCntTable": apCntTable,
       "apCntEntry": apCntEntry,
       "apCntOwner": apCntOwner,
       "apCntName": apCntName,
       "apCntIndex": apCntIndex,
       "apCntIPAddress": apCntIPAddress,
       "apCntIPProtocol": apCntIPProtocol,
       "apCntPort": apCntPort,
       "apCntUrl": apCntUrl,
       "apCntSticky": apCntSticky,
       "apCntBalance": apCntBalance,
       "apCntQOSTag": apCntQOSTag,
       "apCntEnable": apCntEnable,
       "apCntRedirect": apCntRedirect,
       "apCntDrop": apCntDrop,
       "apCntSize": apCntSize,
       "apCntPersistence": apCntPersistence,
       "apCntAuthor": apCntAuthor,
       "apCntSpider": apCntSpider,
       "apCntHits": apCntHits,
       "apCntRedirects": apCntRedirects,
       "apCntDrops": apCntDrops,
       "apCntRejNoServices": apCntRejNoServices,
       "apCntRejServOverload": apCntRejServOverload,
       "apCntSpoofs": apCntSpoofs,
       "apCntNats": apCntNats,
       "apCntByteCount": apCntByteCount,
       "apCntFrameCount": apCntFrameCount,
       "apCntZeroButton": apCntZeroButton,
       "apCntHotListEnabled": apCntHotListEnabled,
       "apCntHotListSize": apCntHotListSize,
       "apCntHotListThreshold": apCntHotListThreshold,
       "apCntHotListType": apCntHotListType,
       "apCntHotListInterval": apCntHotListInterval,
       "apCntFlowTrack": apCntFlowTrack,
       "apCntWeightMask": apCntWeightMask,
       "apCntStickyMask": apCntStickyMask,
       "apCntCookieStartPos": apCntCookieStartPos,
       "apCntHeuristicCookieFence": apCntHeuristicCookieFence,
       "apCntEqlName": apCntEqlName,
       "apCntCacheFalloverType": apCntCacheFalloverType,
       "apCntLocalLoadThreshold": apCntLocalLoadThreshold,
       "apCntStatus": apCntStatus,
       "apCntRedirectLoadThreshold": apCntRedirectLoadThreshold,
       "apCntContentType": apCntContentType,
       "apCntStickyInactivity": apCntStickyInactivity,
       "apCntDNSBalance": apCntDNSBalance,
       "apCntStickyGroup": apCntStickyGroup,
       "apCntAppTypeBypasses": apCntAppTypeBypasses,
       "apCntNoSvcBypasses": apCntNoSvcBypasses,
       "apCntSvcLoadBypasses": apCntSvcLoadBypasses,
       "apCntConnCtBypasses": apCntConnCtBypasses,
       "apCntUrqlTblName": apCntUrqlTblName,
       "apCntStickyStrPre": apCntStickyStrPre,
       "apCntStickyStrEos": apCntStickyStrEos,
       "apCntStickyStrSkipLen": apCntStickyStrSkipLen,
       "apCntStickyStrProcLen": apCntStickyStrProcLen,
       "apCntStickyStrAction": apCntStickyStrAction,
       "apCntStickyStrAsciiConv": apCntStickyStrAsciiConv,
       "apCntPrimarySorryServer": apCntPrimarySorryServer,
       "apCntSecondSorryServer": apCntSecondSorryServer,
       "apCntPrimarySorryHits": apCntPrimarySorryHits,
       "apCntSecondSorryHits": apCntSecondSorryHits,
       "apCntStickySrvrDownFailover": apCntStickySrvrDownFailover,
       "apCntStickyStrType": apCntStickyStrType,
       "apCntParamBypass": apCntParamBypass,
       "apCntAvgLocalLoad": apCntAvgLocalLoad,
       "apCntAvgRemoteLoad": apCntAvgRemoteLoad,
       "apCntDqlName": apCntDqlName,
       "apCntIPAddressRange": apCntIPAddressRange,
       "apCntTagListName": apCntTagListName,
       "apCntStickyNoCookieAction": apCntStickyNoCookieAction,
       "apCntStickyNoCookieString": apCntStickyNoCookieString,
       "apCntStickyCookiePath": apCntStickyCookiePath,
       "apCntStickyCookieExp": apCntStickyCookieExp,
       "apCntStickyCacheExp": apCntStickyCacheExp,
       "apCntTagWeight": apCntTagWeight,
       "apCntAclBypassCt": apCntAclBypassCt,
       "apCntNoRuleBypassCt": apCntNoRuleBypassCt,
       "apCntCacheMissBypassCt": apCntCacheMissBypassCt,
       "apCntGarbageBypassCt": apCntGarbageBypassCt,
       "apCntUrlParamsBypassCt": apCntUrlParamsBypassCt,
       "apCntBypassConnectionPersistence": apCntBypassConnectionPersistence,
       "apCntPersistenceResetMethod": apCntPersistenceResetMethod}
)
