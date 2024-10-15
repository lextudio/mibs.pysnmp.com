# SNMP MIB module (SONUS-RTCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-RTCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:07 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")

(SonusBoolean,
 SonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusBoolean",
    "SonusShelfIndex")


# MODULE-IDENTITY

sonusRtcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusRtcpMIBObjects_ObjectIdentity = ObjectIdentity
sonusRtcpMIBObjects = _SonusRtcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1)
)
_SonusRtcpShelfAdmnTable_Object = MibTable
sonusRtcpShelfAdmnTable = _SonusRtcpShelfAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnTable.setStatus("current")
_SonusRtcpShelfAdmnEntry_Object = MibTableRow
sonusRtcpShelfAdmnEntry = _SonusRtcpShelfAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1)
)
sonusRtcpShelfAdmnEntry.setIndexNames(
    (0, "SONUS-RTCP-MIB", "sonusRtcpShelfAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnEntry.setStatus("current")
_SonusRtcpShelfAdmnIndex_Type = SonusShelfIndex
_SonusRtcpShelfAdmnIndex_Object = MibTableColumn
sonusRtcpShelfAdmnIndex = _SonusRtcpShelfAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 1),
    _SonusRtcpShelfAdmnIndex_Type()
)
sonusRtcpShelfAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnIndex.setStatus("current")


class _SonusRtcpShelfAdmnSrInterval_Type(Integer32):
    """Custom type sonusRtcpShelfAdmnSrInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_SonusRtcpShelfAdmnSrInterval_Type.__name__ = "Integer32"
_SonusRtcpShelfAdmnSrInterval_Object = MibTableColumn
sonusRtcpShelfAdmnSrInterval = _SonusRtcpShelfAdmnSrInterval_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 2),
    _SonusRtcpShelfAdmnSrInterval_Type()
)
sonusRtcpShelfAdmnSrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnSrInterval.setStatus("current")


class _SonusRtcpShelfAdmnEstablishInterval_Type(Integer32):
    """Custom type sonusRtcpShelfAdmnEstablishInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SonusRtcpShelfAdmnEstablishInterval_Type.__name__ = "Integer32"
_SonusRtcpShelfAdmnEstablishInterval_Object = MibTableColumn
sonusRtcpShelfAdmnEstablishInterval = _SonusRtcpShelfAdmnEstablishInterval_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 3),
    _SonusRtcpShelfAdmnEstablishInterval_Type()
)
sonusRtcpShelfAdmnEstablishInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnEstablishInterval.setStatus("current")


class _SonusRtcpShelfAdmnLossTrapHistoryEntries_Type(Integer32):
    """Custom type sonusRtcpShelfAdmnLossTrapHistoryEntries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SonusRtcpShelfAdmnLossTrapHistoryEntries_Type.__name__ = "Integer32"
_SonusRtcpShelfAdmnLossTrapHistoryEntries_Object = MibTableColumn
sonusRtcpShelfAdmnLossTrapHistoryEntries = _SonusRtcpShelfAdmnLossTrapHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 4),
    _SonusRtcpShelfAdmnLossTrapHistoryEntries_Type()
)
sonusRtcpShelfAdmnLossTrapHistoryEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnLossTrapHistoryEntries.setStatus("current")


class _SonusRtcpShelfAdmnAbsenceTrapHistoryEntries_Type(Integer32):
    """Custom type sonusRtcpShelfAdmnAbsenceTrapHistoryEntries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SonusRtcpShelfAdmnAbsenceTrapHistoryEntries_Type.__name__ = "Integer32"
_SonusRtcpShelfAdmnAbsenceTrapHistoryEntries_Object = MibTableColumn
sonusRtcpShelfAdmnAbsenceTrapHistoryEntries = _SonusRtcpShelfAdmnAbsenceTrapHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 5),
    _SonusRtcpShelfAdmnAbsenceTrapHistoryEntries_Type()
)
sonusRtcpShelfAdmnAbsenceTrapHistoryEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnAbsenceTrapHistoryEntries.setStatus("current")


class _SonusRtcpShelfAdmnLossTrapHistoryTableReset_Type(Integer32):
    """Custom type sonusRtcpShelfAdmnLossTrapHistoryTableReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unknown", 1))
    )


_SonusRtcpShelfAdmnLossTrapHistoryTableReset_Type.__name__ = "Integer32"
_SonusRtcpShelfAdmnLossTrapHistoryTableReset_Object = MibTableColumn
sonusRtcpShelfAdmnLossTrapHistoryTableReset = _SonusRtcpShelfAdmnLossTrapHistoryTableReset_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 6),
    _SonusRtcpShelfAdmnLossTrapHistoryTableReset_Type()
)
sonusRtcpShelfAdmnLossTrapHistoryTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnLossTrapHistoryTableReset.setStatus("current")


class _SonusRtcpShelfAdmnAbsenceTrapHistoryTableReset_Type(Integer32):
    """Custom type sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unknown", 1))
    )


_SonusRtcpShelfAdmnAbsenceTrapHistoryTableReset_Type.__name__ = "Integer32"
_SonusRtcpShelfAdmnAbsenceTrapHistoryTableReset_Object = MibTableColumn
sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset = _SonusRtcpShelfAdmnAbsenceTrapHistoryTableReset_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 1, 1, 7),
    _SonusRtcpShelfAdmnAbsenceTrapHistoryTableReset_Type()
)
sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatusTable_Object = MibTable
sonusRtcpSlotLinkLossTrapStatusTable = _SonusRtcpSlotLinkLossTrapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatusTable.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatusEntry_Object = MibTableRow
sonusRtcpSlotLinkLossTrapStatusEntry = _SonusRtcpSlotLinkLossTrapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1)
)
sonusRtcpSlotLinkLossTrapStatusEntry.setIndexNames(
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatShelfIndex"),
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatSlotIndex"),
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatSrcIpAddress"),
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkLossTrapStatDestIpAddress"),
)
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatusEntry.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatShelfIndex_Type = SonusShelfIndex
_SonusRtcpSlotLinkLossTrapStatShelfIndex_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatShelfIndex = _SonusRtcpSlotLinkLossTrapStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 1),
    _SonusRtcpSlotLinkLossTrapStatShelfIndex_Type()
)
sonusRtcpSlotLinkLossTrapStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatShelfIndex.setStatus("current")


class _SonusRtcpSlotLinkLossTrapStatSlotIndex_Type(Integer32):
    """Custom type sonusRtcpSlotLinkLossTrapStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRtcpSlotLinkLossTrapStatSlotIndex_Type.__name__ = "Integer32"
_SonusRtcpSlotLinkLossTrapStatSlotIndex_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatSlotIndex = _SonusRtcpSlotLinkLossTrapStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 2),
    _SonusRtcpSlotLinkLossTrapStatSlotIndex_Type()
)
sonusRtcpSlotLinkLossTrapStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatSlotIndex.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatSrcIpAddress_Type = IpAddress
_SonusRtcpSlotLinkLossTrapStatSrcIpAddress_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatSrcIpAddress = _SonusRtcpSlotLinkLossTrapStatSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 3),
    _SonusRtcpSlotLinkLossTrapStatSrcIpAddress_Type()
)
sonusRtcpSlotLinkLossTrapStatSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatSrcIpAddress.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatDestIpAddress_Type = IpAddress
_SonusRtcpSlotLinkLossTrapStatDestIpAddress_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatDestIpAddress = _SonusRtcpSlotLinkLossTrapStatDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 4),
    _SonusRtcpSlotLinkLossTrapStatDestIpAddress_Type()
)
sonusRtcpSlotLinkLossTrapStatDestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatDestIpAddress.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatCount_Type = Integer32
_SonusRtcpSlotLinkLossTrapStatCount_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatCount = _SonusRtcpSlotLinkLossTrapStatCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 5),
    _SonusRtcpSlotLinkLossTrapStatCount_Type()
)
sonusRtcpSlotLinkLossTrapStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatCount.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatTotalCount_Type = Integer32
_SonusRtcpSlotLinkLossTrapStatTotalCount_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatTotalCount = _SonusRtcpSlotLinkLossTrapStatTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 6),
    _SonusRtcpSlotLinkLossTrapStatTotalCount_Type()
)
sonusRtcpSlotLinkLossTrapStatTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatTotalCount.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatStartTime_Type = DateAndTime
_SonusRtcpSlotLinkLossTrapStatStartTime_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatStartTime = _SonusRtcpSlotLinkLossTrapStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 7),
    _SonusRtcpSlotLinkLossTrapStatStartTime_Type()
)
sonusRtcpSlotLinkLossTrapStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatStartTime.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatLastTime_Type = DateAndTime
_SonusRtcpSlotLinkLossTrapStatLastTime_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatLastTime = _SonusRtcpSlotLinkLossTrapStatLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 8),
    _SonusRtcpSlotLinkLossTrapStatLastTime_Type()
)
sonusRtcpSlotLinkLossTrapStatLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatLastTime.setStatus("current")
_SonusRtcpSlotLinkLossTrapStatActive_Type = SonusBoolean
_SonusRtcpSlotLinkLossTrapStatActive_Object = MibTableColumn
sonusRtcpSlotLinkLossTrapStatActive = _SonusRtcpSlotLinkLossTrapStatActive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 4, 1, 9),
    _SonusRtcpSlotLinkLossTrapStatActive_Type()
)
sonusRtcpSlotLinkLossTrapStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkLossTrapStatActive.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatusTable_Object = MibTable
sonusRtcpSlotLinkAbsenceTrapStatusTable = _SonusRtcpSlotLinkAbsenceTrapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5)
)
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatusTable.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatusEntry_Object = MibTableRow
sonusRtcpSlotLinkAbsenceTrapStatusEntry = _SonusRtcpSlotLinkAbsenceTrapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1)
)
sonusRtcpSlotLinkAbsenceTrapStatusEntry.setIndexNames(
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatShelfIndex"),
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatSlotIndex"),
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress"),
    (0, "SONUS-RTCP-MIB", "sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress"),
)
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatusEntry.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatShelfIndex_Type = SonusShelfIndex
_SonusRtcpSlotLinkAbsenceTrapStatShelfIndex_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatShelfIndex = _SonusRtcpSlotLinkAbsenceTrapStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 1),
    _SonusRtcpSlotLinkAbsenceTrapStatShelfIndex_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatShelfIndex.setStatus("current")


class _SonusRtcpSlotLinkAbsenceTrapStatSlotIndex_Type(Integer32):
    """Custom type sonusRtcpSlotLinkAbsenceTrapStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRtcpSlotLinkAbsenceTrapStatSlotIndex_Type.__name__ = "Integer32"
_SonusRtcpSlotLinkAbsenceTrapStatSlotIndex_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatSlotIndex = _SonusRtcpSlotLinkAbsenceTrapStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 2),
    _SonusRtcpSlotLinkAbsenceTrapStatSlotIndex_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatSlotIndex.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress_Type = IpAddress
_SonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress = _SonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 3),
    _SonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatDestIpAddress_Type = IpAddress
_SonusRtcpSlotLinkAbsenceTrapStatDestIpAddress_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress = _SonusRtcpSlotLinkAbsenceTrapStatDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 4),
    _SonusRtcpSlotLinkAbsenceTrapStatDestIpAddress_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatCount_Type = Integer32
_SonusRtcpSlotLinkAbsenceTrapStatCount_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatCount = _SonusRtcpSlotLinkAbsenceTrapStatCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 5),
    _SonusRtcpSlotLinkAbsenceTrapStatCount_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatCount.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatTotalCount_Type = Integer32
_SonusRtcpSlotLinkAbsenceTrapStatTotalCount_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatTotalCount = _SonusRtcpSlotLinkAbsenceTrapStatTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 6),
    _SonusRtcpSlotLinkAbsenceTrapStatTotalCount_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatTotalCount.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatStartTime_Type = DateAndTime
_SonusRtcpSlotLinkAbsenceTrapStatStartTime_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatStartTime = _SonusRtcpSlotLinkAbsenceTrapStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 7),
    _SonusRtcpSlotLinkAbsenceTrapStatStartTime_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatStartTime.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatLastTime_Type = DateAndTime
_SonusRtcpSlotLinkAbsenceTrapStatLastTime_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatLastTime = _SonusRtcpSlotLinkAbsenceTrapStatLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 8),
    _SonusRtcpSlotLinkAbsenceTrapStatLastTime_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatLastTime.setStatus("current")
_SonusRtcpSlotLinkAbsenceTrapStatActive_Type = SonusBoolean
_SonusRtcpSlotLinkAbsenceTrapStatActive_Object = MibTableColumn
sonusRtcpSlotLinkAbsenceTrapStatActive = _SonusRtcpSlotLinkAbsenceTrapStatActive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 1, 5, 1, 9),
    _SonusRtcpSlotLinkAbsenceTrapStatActive_Type()
)
sonusRtcpSlotLinkAbsenceTrapStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpSlotLinkAbsenceTrapStatActive.setStatus("current")
_SonusRtcpMIBNotifications_ObjectIdentity = ObjectIdentity
sonusRtcpMIBNotifications = _SonusRtcpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2)
)
_SonusRtcpMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusRtcpMIBNotificationsPrefix = _SonusRtcpMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0)
)
_SonusRtcpMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusRtcpMIBNotificationsObjects = _SonusRtcpMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 1)
)
_SonusRtcpLocalIpAddr_Type = IpAddress
_SonusRtcpLocalIpAddr_Object = MibScalar
sonusRtcpLocalIpAddr = _SonusRtcpLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 1, 1),
    _SonusRtcpLocalIpAddr_Type()
)
sonusRtcpLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpLocalIpAddr.setStatus("current")
_SonusRtcpRemoteIpAddr_Type = IpAddress
_SonusRtcpRemoteIpAddr_Object = MibScalar
sonusRtcpRemoteIpAddr = _SonusRtcpRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 1, 2),
    _SonusRtcpRemoteIpAddr_Type()
)
sonusRtcpRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRtcpRemoteIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects

sonusRtcpPacketLossThresholdExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 1)
)
sonusRtcpPacketLossThresholdExceededNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRtcpPacketLossThresholdExceededNotification.setStatus(
        "current"
    )

sonusRtcpPacketLossThresholdClearedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 2)
)
sonusRtcpPacketLossThresholdClearedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRtcpPacketLossThresholdClearedNotification.setStatus(
        "current"
    )

sonusRtcpNoRtpOrRtcpPacketsReceivedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 3)
)
sonusRtcpNoRtpOrRtcpPacketsReceivedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRtcpNoRtpOrRtcpPacketsReceivedNotification.setStatus(
        "current"
    )

sonusRtcpNoRtpOrRtcpPacketsClearedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 7, 2, 0, 4)
)
sonusRtcpNoRtpOrRtcpPacketsClearedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRtcpNoRtpOrRtcpPacketsClearedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-RTCP-MIB",
    **{"sonusRtcpMIB": sonusRtcpMIB,
       "sonusRtcpMIBObjects": sonusRtcpMIBObjects,
       "sonusRtcpShelfAdmnTable": sonusRtcpShelfAdmnTable,
       "sonusRtcpShelfAdmnEntry": sonusRtcpShelfAdmnEntry,
       "sonusRtcpShelfAdmnIndex": sonusRtcpShelfAdmnIndex,
       "sonusRtcpShelfAdmnSrInterval": sonusRtcpShelfAdmnSrInterval,
       "sonusRtcpShelfAdmnEstablishInterval": sonusRtcpShelfAdmnEstablishInterval,
       "sonusRtcpShelfAdmnLossTrapHistoryEntries": sonusRtcpShelfAdmnLossTrapHistoryEntries,
       "sonusRtcpShelfAdmnAbsenceTrapHistoryEntries": sonusRtcpShelfAdmnAbsenceTrapHistoryEntries,
       "sonusRtcpShelfAdmnLossTrapHistoryTableReset": sonusRtcpShelfAdmnLossTrapHistoryTableReset,
       "sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset": sonusRtcpShelfAdmnAbsenceTrapHistoryTableReset,
       "sonusRtcpSlotLinkLossTrapStatusTable": sonusRtcpSlotLinkLossTrapStatusTable,
       "sonusRtcpSlotLinkLossTrapStatusEntry": sonusRtcpSlotLinkLossTrapStatusEntry,
       "sonusRtcpSlotLinkLossTrapStatShelfIndex": sonusRtcpSlotLinkLossTrapStatShelfIndex,
       "sonusRtcpSlotLinkLossTrapStatSlotIndex": sonusRtcpSlotLinkLossTrapStatSlotIndex,
       "sonusRtcpSlotLinkLossTrapStatSrcIpAddress": sonusRtcpSlotLinkLossTrapStatSrcIpAddress,
       "sonusRtcpSlotLinkLossTrapStatDestIpAddress": sonusRtcpSlotLinkLossTrapStatDestIpAddress,
       "sonusRtcpSlotLinkLossTrapStatCount": sonusRtcpSlotLinkLossTrapStatCount,
       "sonusRtcpSlotLinkLossTrapStatTotalCount": sonusRtcpSlotLinkLossTrapStatTotalCount,
       "sonusRtcpSlotLinkLossTrapStatStartTime": sonusRtcpSlotLinkLossTrapStatStartTime,
       "sonusRtcpSlotLinkLossTrapStatLastTime": sonusRtcpSlotLinkLossTrapStatLastTime,
       "sonusRtcpSlotLinkLossTrapStatActive": sonusRtcpSlotLinkLossTrapStatActive,
       "sonusRtcpSlotLinkAbsenceTrapStatusTable": sonusRtcpSlotLinkAbsenceTrapStatusTable,
       "sonusRtcpSlotLinkAbsenceTrapStatusEntry": sonusRtcpSlotLinkAbsenceTrapStatusEntry,
       "sonusRtcpSlotLinkAbsenceTrapStatShelfIndex": sonusRtcpSlotLinkAbsenceTrapStatShelfIndex,
       "sonusRtcpSlotLinkAbsenceTrapStatSlotIndex": sonusRtcpSlotLinkAbsenceTrapStatSlotIndex,
       "sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress": sonusRtcpSlotLinkAbsenceTrapStatSrcIpAddress,
       "sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress": sonusRtcpSlotLinkAbsenceTrapStatDestIpAddress,
       "sonusRtcpSlotLinkAbsenceTrapStatCount": sonusRtcpSlotLinkAbsenceTrapStatCount,
       "sonusRtcpSlotLinkAbsenceTrapStatTotalCount": sonusRtcpSlotLinkAbsenceTrapStatTotalCount,
       "sonusRtcpSlotLinkAbsenceTrapStatStartTime": sonusRtcpSlotLinkAbsenceTrapStatStartTime,
       "sonusRtcpSlotLinkAbsenceTrapStatLastTime": sonusRtcpSlotLinkAbsenceTrapStatLastTime,
       "sonusRtcpSlotLinkAbsenceTrapStatActive": sonusRtcpSlotLinkAbsenceTrapStatActive,
       "sonusRtcpMIBNotifications": sonusRtcpMIBNotifications,
       "sonusRtcpMIBNotificationsPrefix": sonusRtcpMIBNotificationsPrefix,
       "sonusRtcpPacketLossThresholdExceededNotification": sonusRtcpPacketLossThresholdExceededNotification,
       "sonusRtcpPacketLossThresholdClearedNotification": sonusRtcpPacketLossThresholdClearedNotification,
       "sonusRtcpNoRtpOrRtcpPacketsReceivedNotification": sonusRtcpNoRtpOrRtcpPacketsReceivedNotification,
       "sonusRtcpNoRtpOrRtcpPacketsClearedNotification": sonusRtcpNoRtpOrRtcpPacketsClearedNotification,
       "sonusRtcpMIBNotificationsObjects": sonusRtcpMIBNotificationsObjects,
       "sonusRtcpLocalIpAddr": sonusRtcpLocalIpAddr,
       "sonusRtcpRemoteIpAddr": sonusRtcpRemoteIpAddr}
)
