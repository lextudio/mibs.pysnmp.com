# SNMP MIB module (ACC-AT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-AT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:48 2024
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
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccAt_ObjectIdentity = ObjectIdentity
accAt = _AccAt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28)
)
_AccAtNode_ObjectIdentity = ObjectIdentity
accAtNode = _AccAtNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1)
)


class _AccAtNodeAdState_Type(Integer32):
    """Custom type accAtNodeAdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 1))
    )


_AccAtNodeAdState_Type.__name__ = "Integer32"
_AccAtNodeAdState_Object = MibScalar
accAtNodeAdState = _AccAtNodeAdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 1),
    _AccAtNodeAdState_Type()
)
accAtNodeAdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeAdState.setStatus("mandatory")


class _AccAtNodeChecksum_Type(Integer32):
    """Custom type accAtNodeChecksum based on Integer32"""
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


_AccAtNodeChecksum_Type.__name__ = "Integer32"
_AccAtNodeChecksum_Object = MibScalar
accAtNodeChecksum = _AccAtNodeChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 2),
    _AccAtNodeChecksum_Type()
)
accAtNodeChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeChecksum.setStatus("mandatory")
_AccAtNodeAarpExpire_Type = TimeTicks
_AccAtNodeAarpExpire_Object = MibScalar
accAtNodeAarpExpire = _AccAtNodeAarpExpire_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 3),
    _AccAtNodeAarpExpire_Type()
)
accAtNodeAarpExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeAarpExpire.setStatus("mandatory")


class _AccAtNodeFfrRouting_Type(Integer32):
    """Custom type accAtNodeFfrRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_AccAtNodeFfrRouting_Type.__name__ = "Integer32"
_AccAtNodeFfrRouting_Object = MibScalar
accAtNodeFfrRouting = _AccAtNodeFfrRouting_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 4),
    _AccAtNodeFfrRouting_Type()
)
accAtNodeFfrRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeFfrRouting.setStatus("mandatory")
_AccAtAarpTable_Object = MibTable
accAtAarpTable = _AccAtAarpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2)
)
if mibBuilder.loadTexts:
    accAtAarpTable.setStatus("mandatory")
_AccAtAarpEntry_Object = MibTableRow
accAtAarpEntry = _AccAtAarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1)
)
accAtAarpEntry.setIndexNames(
    (0, "ACC-AT", "accAtAarpTabPort"),
    (0, "ACC-AT", "accAtAarpTabNetAddr"),
)
if mibBuilder.loadTexts:
    accAtAarpEntry.setStatus("mandatory")


class _AccAtAarpTabPort_Type(Integer32):
    """Custom type accAtAarpTabPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccAtAarpTabPort_Type.__name__ = "Integer32"
_AccAtAarpTabPort_Object = MibTableColumn
accAtAarpTabPort = _AccAtAarpTabPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 1),
    _AccAtAarpTabPort_Type()
)
accAtAarpTabPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabPort.setStatus("mandatory")
_AccAtAarpTabMacAddr_Type = OctetString
_AccAtAarpTabMacAddr_Object = MibTableColumn
accAtAarpTabMacAddr = _AccAtAarpTabMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 2),
    _AccAtAarpTabMacAddr_Type()
)
accAtAarpTabMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabMacAddr.setStatus("mandatory")
_AccAtAarpTabNetAddr_Type = OctetString
_AccAtAarpTabNetAddr_Object = MibTableColumn
accAtAarpTabNetAddr = _AccAtAarpTabNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 3),
    _AccAtAarpTabNetAddr_Type()
)
accAtAarpTabNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabNetAddr.setStatus("mandatory")


class _AccAtAarpTabStatus_Type(Integer32):
    """Custom type accAtAarpTabStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("pending", 3),
          ("static", 2))
    )


_AccAtAarpTabStatus_Type.__name__ = "Integer32"
_AccAtAarpTabStatus_Object = MibTableColumn
accAtAarpTabStatus = _AccAtAarpTabStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 4),
    _AccAtAarpTabStatus_Type()
)
accAtAarpTabStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabStatus.setStatus("mandatory")
_AccAtAarpStatsTable_Object = MibTable
accAtAarpStatsTable = _AccAtAarpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3)
)
if mibBuilder.loadTexts:
    accAtAarpStatsTable.setStatus("mandatory")
_AccAtAarpStatsEntry_Object = MibTableRow
accAtAarpStatsEntry = _AccAtAarpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1)
)
accAtAarpStatsEntry.setIndexNames(
    (0, "ACC-AT", "accAtPortTabIndex"),
)
if mibBuilder.loadTexts:
    accAtAarpStatsEntry.setStatus("mandatory")
_AccAtAarpStatsInRequests_Type = Counter32
_AccAtAarpStatsInRequests_Object = MibTableColumn
accAtAarpStatsInRequests = _AccAtAarpStatsInRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 1),
    _AccAtAarpStatsInRequests_Type()
)
accAtAarpStatsInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInRequests.setStatus("mandatory")
_AccAtAarpStatsInResponses_Type = Counter32
_AccAtAarpStatsInResponses_Object = MibTableColumn
accAtAarpStatsInResponses = _AccAtAarpStatsInResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 2),
    _AccAtAarpStatsInResponses_Type()
)
accAtAarpStatsInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInResponses.setStatus("mandatory")
_AccAtAarpStatsInProbes_Type = Counter32
_AccAtAarpStatsInProbes_Object = MibTableColumn
accAtAarpStatsInProbes = _AccAtAarpStatsInProbes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 3),
    _AccAtAarpStatsInProbes_Type()
)
accAtAarpStatsInProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInProbes.setStatus("mandatory")
_AccAtAarpStatsOutRequests_Type = Counter32
_AccAtAarpStatsOutRequests_Object = MibTableColumn
accAtAarpStatsOutRequests = _AccAtAarpStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 4),
    _AccAtAarpStatsOutRequests_Type()
)
accAtAarpStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutRequests.setStatus("mandatory")
_AccAtAarpStatsOutResponses_Type = Counter32
_AccAtAarpStatsOutResponses_Object = MibTableColumn
accAtAarpStatsOutResponses = _AccAtAarpStatsOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 5),
    _AccAtAarpStatsOutResponses_Type()
)
accAtAarpStatsOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutResponses.setStatus("mandatory")
_AccAtAarpStatsOutProbes_Type = Counter32
_AccAtAarpStatsOutProbes_Object = MibTableColumn
accAtAarpStatsOutProbes = _AccAtAarpStatsOutProbes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 6),
    _AccAtAarpStatsOutProbes_Type()
)
accAtAarpStatsOutProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutProbes.setStatus("mandatory")
_AccAtAarpStatsNoReplys_Type = Counter32
_AccAtAarpStatsNoReplys_Object = MibTableColumn
accAtAarpStatsNoReplys = _AccAtAarpStatsNoReplys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 7),
    _AccAtAarpStatsNoReplys_Type()
)
accAtAarpStatsNoReplys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsNoReplys.setStatus("mandatory")
_AccAtAarpStatsExpires_Type = Counter32
_AccAtAarpStatsExpires_Object = MibTableColumn
accAtAarpStatsExpires = _AccAtAarpStatsExpires_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 8),
    _AccAtAarpStatsExpires_Type()
)
accAtAarpStatsExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsExpires.setStatus("mandatory")
_AccAtAarpStatsDiscards_Type = Counter32
_AccAtAarpStatsDiscards_Object = MibTableColumn
accAtAarpStatsDiscards = _AccAtAarpStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 9),
    _AccAtAarpStatsDiscards_Type()
)
accAtAarpStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsDiscards.setStatus("mandatory")
_AccAtAarpStatsInErrors_Type = Counter32
_AccAtAarpStatsInErrors_Object = MibTableColumn
accAtAarpStatsInErrors = _AccAtAarpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 10),
    _AccAtAarpStatsInErrors_Type()
)
accAtAarpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInErrors.setStatus("mandatory")
_AccAtAarpStatsOutErrors_Type = Counter32
_AccAtAarpStatsOutErrors_Object = MibTableColumn
accAtAarpStatsOutErrors = _AccAtAarpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 11),
    _AccAtAarpStatsOutErrors_Type()
)
accAtAarpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutErrors.setStatus("mandatory")
_AccAtAdbStats_ObjectIdentity = ObjectIdentity
accAtAdbStats = _AccAtAdbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4)
)
_AccAtAdbStatsCacheds_Type = Counter32
_AccAtAdbStatsCacheds_Object = MibScalar
accAtAdbStatsCacheds = _AccAtAdbStatsCacheds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 1),
    _AccAtAdbStatsCacheds_Type()
)
accAtAdbStatsCacheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsCacheds.setStatus("mandatory")
_AccAtAdbStatsRotates_Type = Counter32
_AccAtAdbStatsRotates_Object = MibScalar
accAtAdbStatsRotates = _AccAtAdbStatsRotates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 2),
    _AccAtAdbStatsRotates_Type()
)
accAtAdbStatsRotates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsRotates.setStatus("mandatory")
_AccAtAdbStatsNoEntries_Type = Counter32
_AccAtAdbStatsNoEntries_Object = MibScalar
accAtAdbStatsNoEntries = _AccAtAdbStatsNoEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 3),
    _AccAtAdbStatsNoEntries_Type()
)
accAtAdbStatsNoEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsNoEntries.setStatus("mandatory")
_AccAtAdbStatsAdds_Type = Counter32
_AccAtAdbStatsAdds_Object = MibScalar
accAtAdbStatsAdds = _AccAtAdbStatsAdds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 4),
    _AccAtAdbStatsAdds_Type()
)
accAtAdbStatsAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsAdds.setStatus("mandatory")
_AccAtAdbStatsUpdates_Type = Counter32
_AccAtAdbStatsUpdates_Object = MibScalar
accAtAdbStatsUpdates = _AccAtAdbStatsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 5),
    _AccAtAdbStatsUpdates_Type()
)
accAtAdbStatsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsUpdates.setStatus("mandatory")
_AccAtAdbStatsDeletes_Type = Counter32
_AccAtAdbStatsDeletes_Object = MibScalar
accAtAdbStatsDeletes = _AccAtAdbStatsDeletes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 6),
    _AccAtAdbStatsDeletes_Type()
)
accAtAdbStatsDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsDeletes.setStatus("mandatory")
_AccAtAdbStatsTrims_Type = Counter32
_AccAtAdbStatsTrims_Object = MibScalar
accAtAdbStatsTrims = _AccAtAdbStatsTrims_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 7),
    _AccAtAdbStatsTrims_Type()
)
accAtAdbStatsTrims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsTrims.setStatus("mandatory")
_AccAtAdbStatsDiscards_Type = Counter32
_AccAtAdbStatsDiscards_Object = MibScalar
accAtAdbStatsDiscards = _AccAtAdbStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 8),
    _AccAtAdbStatsDiscards_Type()
)
accAtAdbStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsDiscards.setStatus("mandatory")
_AccAtDdpStats_ObjectIdentity = ObjectIdentity
accAtDdpStats = _AccAtDdpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5)
)
_AccAtDdpStatsNoOutRoutes_Type = Counter32
_AccAtDdpStatsNoOutRoutes_Object = MibScalar
accAtDdpStatsNoOutRoutes = _AccAtDdpStatsNoOutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5, 1),
    _AccAtDdpStatsNoOutRoutes_Type()
)
accAtDdpStatsNoOutRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtDdpStatsNoOutRoutes.setStatus("mandatory")
_AccAtDdpStatsInErrors_Type = Counter32
_AccAtDdpStatsInErrors_Object = MibScalar
accAtDdpStatsInErrors = _AccAtDdpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5, 2),
    _AccAtDdpStatsInErrors_Type()
)
accAtDdpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtDdpStatsInErrors.setStatus("mandatory")
_AccAtDdpStatsOutErrors_Type = Counter32
_AccAtDdpStatsOutErrors_Object = MibScalar
accAtDdpStatsOutErrors = _AccAtDdpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5, 3),
    _AccAtDdpStatsOutErrors_Type()
)
accAtDdpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtDdpStatsOutErrors.setStatus("mandatory")
_AccAtNetTable_Object = MibTable
accAtNetTable = _AccAtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6)
)
if mibBuilder.loadTexts:
    accAtNetTable.setStatus("mandatory")
_AccAtNetEntry_Object = MibTableRow
accAtNetEntry = _AccAtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1)
)
accAtNetEntry.setIndexNames(
    (0, "ACC-AT", "atportIndex"),
)
if mibBuilder.loadTexts:
    accAtNetEntry.setStatus("mandatory")


class _AccAtNetTabProtocol_Type(Integer32):
    """Custom type accAtNetTabProtocol based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("dial", 11),
          ("ethertalk1", 1),
          ("ethertalk2", 2),
          ("fddi", 8),
          ("framerelay", 6),
          ("lapb", 4),
          ("multilinkgroup", 12),
          ("ppp", 7),
          ("tokentalk", 3),
          ("x25", 5))
    )


_AccAtNetTabProtocol_Type.__name__ = "Integer32"
_AccAtNetTabProtocol_Object = MibTableColumn
accAtNetTabProtocol = _AccAtNetTabProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 1),
    _AccAtNetTabProtocol_Type()
)
accAtNetTabProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabProtocol.setStatus("mandatory")


class _AccAtNetTabRtmpIncr_Type(Integer32):
    """Custom type accAtNetTabRtmpIncr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AccAtNetTabRtmpIncr_Type.__name__ = "Integer32"
_AccAtNetTabRtmpIncr_Object = MibTableColumn
accAtNetTabRtmpIncr = _AccAtNetTabRtmpIncr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 2),
    _AccAtNetTabRtmpIncr_Type()
)
accAtNetTabRtmpIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabRtmpIncr.setStatus("mandatory")


class _AccAtNetTabRtmpSend_Type(TimeTicks):
    """Custom type accAtNetTabRtmpSend based on TimeTicks"""
    defaultValue = 1000


_AccAtNetTabRtmpSend_Object = MibTableColumn
accAtNetTabRtmpSend = _AccAtNetTabRtmpSend_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 3),
    _AccAtNetTabRtmpSend_Type()
)
accAtNetTabRtmpSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabRtmpSend.setStatus("mandatory")
_AccAtNetTabX25Addr1_Type = OctetString
_AccAtNetTabX25Addr1_Object = MibTableColumn
accAtNetTabX25Addr1 = _AccAtNetTabX25Addr1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 4),
    _AccAtNetTabX25Addr1_Type()
)
accAtNetTabX25Addr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25Addr1.setStatus("mandatory")
_AccAtNetTabX25Addr2_Type = OctetString
_AccAtNetTabX25Addr2_Object = MibTableColumn
accAtNetTabX25Addr2 = _AccAtNetTabX25Addr2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 5),
    _AccAtNetTabX25Addr2_Type()
)
accAtNetTabX25Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25Addr2.setStatus("mandatory")


class _AccAtNetTabX25Idle_Type(TimeTicks):
    """Custom type accAtNetTabX25Idle based on TimeTicks"""
    defaultValue = 30000


_AccAtNetTabX25Idle_Object = MibTableColumn
accAtNetTabX25Idle = _AccAtNetTabX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 6),
    _AccAtNetTabX25Idle_Type()
)
accAtNetTabX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25Idle.setStatus("mandatory")


class _AccAtNetTabX25PktSize_Type(Integer32):
    """Custom type accAtNetTabX25PktSize based on Integer32"""
    defaultValue = 0


_AccAtNetTabX25PktSize_Object = MibTableColumn
accAtNetTabX25PktSize = _AccAtNetTabX25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 7),
    _AccAtNetTabX25PktSize_Type()
)
accAtNetTabX25PktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25PktSize.setStatus("mandatory")


class _AccAtNetTabX25WinSize_Type(Integer32):
    """Custom type accAtNetTabX25WinSize based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccAtNetTabX25WinSize_Type.__name__ = "Integer32"
_AccAtNetTabX25WinSize_Object = MibTableColumn
accAtNetTabX25WinSize = _AccAtNetTabX25WinSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 8),
    _AccAtNetTabX25WinSize_Type()
)
accAtNetTabX25WinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25WinSize.setStatus("mandatory")


class _AccAtNetTabX25FacIndex_Type(Integer32):
    """Custom type accAtNetTabX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccAtNetTabX25FacIndex_Type.__name__ = "Integer32"
_AccAtNetTabX25FacIndex_Object = MibTableColumn
accAtNetTabX25FacIndex = _AccAtNetTabX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 9),
    _AccAtNetTabX25FacIndex_Type()
)
accAtNetTabX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25FacIndex.setStatus("mandatory")
_AccAtPortTable_Object = MibTable
accAtPortTable = _AccAtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7)
)
if mibBuilder.loadTexts:
    accAtPortTable.setStatus("mandatory")
_AccAtPortEntry_Object = MibTableRow
accAtPortEntry = _AccAtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1)
)
accAtPortEntry.setIndexNames(
    (0, "ACC-AT", "accAtPortTabIndex"),
)
if mibBuilder.loadTexts:
    accAtPortEntry.setStatus("mandatory")


class _AccAtPortTabIndex_Type(Integer32):
    """Custom type accAtPortTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccAtPortTabIndex_Type.__name__ = "Integer32"
_AccAtPortTabIndex_Object = MibTableColumn
accAtPortTabIndex = _AccAtPortTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 1),
    _AccAtPortTabIndex_Type()
)
accAtPortTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabIndex.setStatus("mandatory")
_AccAtPortTabNetAddr_Type = OctetString
_AccAtPortTabNetAddr_Object = MibTableColumn
accAtPortTabNetAddr = _AccAtPortTabNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 2),
    _AccAtPortTabNetAddr_Type()
)
accAtPortTabNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabNetAddr.setStatus("mandatory")


class _AccAtPortTabState_Type(Integer32):
    """Custom type accAtPortTabState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("error", 11),
          ("probe1", 3),
          ("probe2", 6),
          ("query", 7),
          ("ready", 8),
          ("start1", 2),
          ("start2", 4),
          ("stop1", 10),
          ("stop2", 9),
          ("up", 5))
    )


_AccAtPortTabState_Type.__name__ = "Integer32"
_AccAtPortTabState_Object = MibTableColumn
accAtPortTabState = _AccAtPortTabState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 3),
    _AccAtPortTabState_Type()
)
accAtPortTabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabState.setStatus("mandatory")
_AccAtPortTabDescr_Type = DisplayString
_AccAtPortTabDescr_Object = MibTableColumn
accAtPortTabDescr = _AccAtPortTabDescr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 4),
    _AccAtPortTabDescr_Type()
)
accAtPortTabDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabDescr.setStatus("mandatory")
_AccAtPortTabErrCode_Type = Integer32
_AccAtPortTabErrCode_Object = MibTableColumn
accAtPortTabErrCode = _AccAtPortTabErrCode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 5),
    _AccAtPortTabErrCode_Type()
)
accAtPortTabErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrCode.setStatus("mandatory")
_AccAtPortTabErrTime_Type = TimeTicks
_AccAtPortTabErrTime_Object = MibTableColumn
accAtPortTabErrTime = _AccAtPortTabErrTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 6),
    _AccAtPortTabErrTime_Type()
)
accAtPortTabErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrTime.setStatus("mandatory")
_AccAtPortTabErrAddr_Type = OctetString
_AccAtPortTabErrAddr_Object = MibTableColumn
accAtPortTabErrAddr = _AccAtPortTabErrAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 7),
    _AccAtPortTabErrAddr_Type()
)
accAtPortTabErrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrAddr.setStatus("mandatory")
_AccAtPortTabErrDescr_Type = DisplayString
_AccAtPortTabErrDescr_Object = MibTableColumn
accAtPortTabErrDescr = _AccAtPortTabErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 8),
    _AccAtPortTabErrDescr_Type()
)
accAtPortTabErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrDescr.setStatus("mandatory")
_AccAtPortTabErrCount_Type = Integer32
_AccAtPortTabErrCount_Object = MibTableColumn
accAtPortTabErrCount = _AccAtPortTabErrCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 9),
    _AccAtPortTabErrCount_Type()
)
accAtPortTabErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrCount.setStatus("mandatory")
_AccAtPortStatsTable_Object = MibTable
accAtPortStatsTable = _AccAtPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8)
)
if mibBuilder.loadTexts:
    accAtPortStatsTable.setStatus("mandatory")
_AccAtPortStatsEntry_Object = MibTableRow
accAtPortStatsEntry = _AccAtPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1)
)
accAtPortStatsEntry.setIndexNames(
    (0, "ACC-AT", "accAtPortTabIndex"),
)
if mibBuilder.loadTexts:
    accAtPortStatsEntry.setStatus("mandatory")
_AccAtPortStatsInTotals_Type = Counter32
_AccAtPortStatsInTotals_Object = MibTableColumn
accAtPortStatsInTotals = _AccAtPortStatsInTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 1),
    _AccAtPortStatsInTotals_Type()
)
accAtPortStatsInTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInTotals.setStatus("mandatory")
_AccAtPortStatsInShorts_Type = Counter32
_AccAtPortStatsInShorts_Object = MibTableColumn
accAtPortStatsInShorts = _AccAtPortStatsInShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 2),
    _AccAtPortStatsInShorts_Type()
)
accAtPortStatsInShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInShorts.setStatus("mandatory")
_AccAtPortStatsNotForMes_Type = Counter32
_AccAtPortStatsNotForMes_Object = MibTableColumn
accAtPortStatsNotForMes = _AccAtPortStatsNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 3),
    _AccAtPortStatsNotForMes_Type()
)
accAtPortStatsNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsNotForMes.setStatus("mandatory")
_AccAtPortStatsTooShorts_Type = Counter32
_AccAtPortStatsTooShorts_Object = MibTableColumn
accAtPortStatsTooShorts = _AccAtPortStatsTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 4),
    _AccAtPortStatsTooShorts_Type()
)
accAtPortStatsTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsTooShorts.setStatus("mandatory")
_AccAtPortStatsTooLongs_Type = Counter32
_AccAtPortStatsTooLongs_Object = MibTableColumn
accAtPortStatsTooLongs = _AccAtPortStatsTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 5),
    _AccAtPortStatsTooLongs_Type()
)
accAtPortStatsTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsTooLongs.setStatus("mandatory")
_AccAtPortStatsChksums_Type = Counter32
_AccAtPortStatsChksums_Object = MibTableColumn
accAtPortStatsChksums = _AccAtPortStatsChksums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 6),
    _AccAtPortStatsChksums_Type()
)
accAtPortStatsChksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsChksums.setStatus("mandatory")
_AccAtPortStatsNotMyNets_Type = Counter32
_AccAtPortStatsNotMyNets_Object = MibTableColumn
accAtPortStatsNotMyNets = _AccAtPortStatsNotMyNets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 7),
    _AccAtPortStatsNotMyNets_Type()
)
accAtPortStatsNotMyNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsNotMyNets.setStatus("mandatory")
_AccAtPortStatsInFwdReqs_Type = Counter32
_AccAtPortStatsInFwdReqs_Object = MibTableColumn
accAtPortStatsInFwdReqs = _AccAtPortStatsInFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 8),
    _AccAtPortStatsInFwdReqs_Type()
)
accAtPortStatsInFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInFwdReqs.setStatus("mandatory")
_AccAtPortStatsFwdBcasts_Type = Counter32
_AccAtPortStatsFwdBcasts_Object = MibTableColumn
accAtPortStatsFwdBcasts = _AccAtPortStatsFwdBcasts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 9),
    _AccAtPortStatsFwdBcasts_Type()
)
accAtPortStatsFwdBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsFwdBcasts.setStatus("mandatory")
_AccAtPortStatsNoFwdRoutes_Type = Counter32
_AccAtPortStatsNoFwdRoutes_Object = MibTableColumn
accAtPortStatsNoFwdRoutes = _AccAtPortStatsNoFwdRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 10),
    _AccAtPortStatsNoFwdRoutes_Type()
)
accAtPortStatsNoFwdRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsNoFwdRoutes.setStatus("mandatory")
_AccAtPortStatsHopCounts_Type = Counter32
_AccAtPortStatsHopCounts_Object = MibTableColumn
accAtPortStatsHopCounts = _AccAtPortStatsHopCounts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 11),
    _AccAtPortStatsHopCounts_Type()
)
accAtPortStatsHopCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsHopCounts.setStatus("mandatory")
_AccAtPortStatsReflects_Type = Counter32
_AccAtPortStatsReflects_Object = MibTableColumn
accAtPortStatsReflects = _AccAtPortStatsReflects_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 12),
    _AccAtPortStatsReflects_Type()
)
accAtPortStatsReflects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsReflects.setStatus("mandatory")
_AccAtPortStatsOutTotals_Type = Counter32
_AccAtPortStatsOutTotals_Object = MibTableColumn
accAtPortStatsOutTotals = _AccAtPortStatsOutTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 13),
    _AccAtPortStatsOutTotals_Type()
)
accAtPortStatsOutTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutTotals.setStatus("mandatory")
_AccAtPortStatsOutShorts_Type = Counter32
_AccAtPortStatsOutShorts_Object = MibTableColumn
accAtPortStatsOutShorts = _AccAtPortStatsOutShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 14),
    _AccAtPortStatsOutShorts_Type()
)
accAtPortStatsOutShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutShorts.setStatus("mandatory")
_AccAtPortStatsOutFwdReqs_Type = Counter32
_AccAtPortStatsOutFwdReqs_Object = MibTableColumn
accAtPortStatsOutFwdReqs = _AccAtPortStatsOutFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 15),
    _AccAtPortStatsOutFwdReqs_Type()
)
accAtPortStatsOutFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutFwdReqs.setStatus("mandatory")
_AccAtPortStatsInErrors_Type = Counter32
_AccAtPortStatsInErrors_Object = MibTableColumn
accAtPortStatsInErrors = _AccAtPortStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 16),
    _AccAtPortStatsInErrors_Type()
)
accAtPortStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInErrors.setStatus("mandatory")
_AccAtPortStatsOutErrors_Type = Counter32
_AccAtPortStatsOutErrors_Object = MibTableColumn
accAtPortStatsOutErrors = _AccAtPortStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 17),
    _AccAtPortStatsOutErrors_Type()
)
accAtPortStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutErrors.setStatus("mandatory")
_AccAtRtmpStats_ObjectIdentity = ObjectIdentity
accAtRtmpStats = _AccAtRtmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9)
)
_AccAtRtmpStatsInRequests_Type = Counter32
_AccAtRtmpStatsInRequests_Object = MibScalar
accAtRtmpStatsInRequests = _AccAtRtmpStatsInRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 1),
    _AccAtRtmpStatsInRequests_Type()
)
accAtRtmpStatsInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInRequests.setStatus("mandatory")
_AccAtRtmpStatsInDataReqs_Type = Counter32
_AccAtRtmpStatsInDataReqs_Object = MibScalar
accAtRtmpStatsInDataReqs = _AccAtRtmpStatsInDataReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 2),
    _AccAtRtmpStatsInDataReqs_Type()
)
accAtRtmpStatsInDataReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInDataReqs.setStatus("mandatory")
_AccAtRtmpStatsInResponses_Type = Counter32
_AccAtRtmpStatsInResponses_Object = MibScalar
accAtRtmpStatsInResponses = _AccAtRtmpStatsInResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 3),
    _AccAtRtmpStatsInResponses_Type()
)
accAtRtmpStatsInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInResponses.setStatus("mandatory")
_AccAtRtmpStatsInDataResps_Type = Counter32
_AccAtRtmpStatsInDataResps_Object = MibScalar
accAtRtmpStatsInDataResps = _AccAtRtmpStatsInDataResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 4),
    _AccAtRtmpStatsInDataResps_Type()
)
accAtRtmpStatsInDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInDataResps.setStatus("mandatory")
_AccAtRtmpStatsOutRequests_Type = Counter32
_AccAtRtmpStatsOutRequests_Object = MibScalar
accAtRtmpStatsOutRequests = _AccAtRtmpStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 5),
    _AccAtRtmpStatsOutRequests_Type()
)
accAtRtmpStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutRequests.setStatus("mandatory")
_AccAtRtmpStatsOutDataReqs_Type = Counter32
_AccAtRtmpStatsOutDataReqs_Object = MibScalar
accAtRtmpStatsOutDataReqs = _AccAtRtmpStatsOutDataReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 6),
    _AccAtRtmpStatsOutDataReqs_Type()
)
accAtRtmpStatsOutDataReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutDataReqs.setStatus("mandatory")
_AccAtRtmpStatsOutResponses_Type = Counter32
_AccAtRtmpStatsOutResponses_Object = MibScalar
accAtRtmpStatsOutResponses = _AccAtRtmpStatsOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 7),
    _AccAtRtmpStatsOutResponses_Type()
)
accAtRtmpStatsOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutResponses.setStatus("mandatory")
_AccAtRtmpStatsOutDataResps_Type = Counter32
_AccAtRtmpStatsOutDataResps_Object = MibScalar
accAtRtmpStatsOutDataResps = _AccAtRtmpStatsOutDataResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 8),
    _AccAtRtmpStatsOutDataResps_Type()
)
accAtRtmpStatsOutDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutDataResps.setStatus("mandatory")
_AccAtRtmpStatsNetConflicts_Type = Counter32
_AccAtRtmpStatsNetConflicts_Object = MibScalar
accAtRtmpStatsNetConflicts = _AccAtRtmpStatsNetConflicts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 9),
    _AccAtRtmpStatsNetConflicts_Type()
)
accAtRtmpStatsNetConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsNetConflicts.setStatus("mandatory")
_AccAtRtmpStatsInErrors_Type = Counter32
_AccAtRtmpStatsInErrors_Object = MibScalar
accAtRtmpStatsInErrors = _AccAtRtmpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 10),
    _AccAtRtmpStatsInErrors_Type()
)
accAtRtmpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInErrors.setStatus("mandatory")
_AccAtRtmpStatsOutErrors_Type = Counter32
_AccAtRtmpStatsOutErrors_Object = MibScalar
accAtRtmpStatsOutErrors = _AccAtRtmpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 11),
    _AccAtRtmpStatsOutErrors_Type()
)
accAtRtmpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutErrors.setStatus("mandatory")
_AccAtRdbStats_ObjectIdentity = ObjectIdentity
accAtRdbStats = _AccAtRdbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10)
)
_AccAtRdbStatsCacheds_Type = Counter32
_AccAtRdbStatsCacheds_Object = MibScalar
accAtRdbStatsCacheds = _AccAtRdbStatsCacheds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 1),
    _AccAtRdbStatsCacheds_Type()
)
accAtRdbStatsCacheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsCacheds.setStatus("mandatory")
_AccAtRdbStatsSearchs_Type = Counter32
_AccAtRdbStatsSearchs_Object = MibScalar
accAtRdbStatsSearchs = _AccAtRdbStatsSearchs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 2),
    _AccAtRdbStatsSearchs_Type()
)
accAtRdbStatsSearchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsSearchs.setStatus("mandatory")
_AccAtRdbStatsNoRoutes_Type = Counter32
_AccAtRdbStatsNoRoutes_Object = MibScalar
accAtRdbStatsNoRoutes = _AccAtRdbStatsNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 3),
    _AccAtRdbStatsNoRoutes_Type()
)
accAtRdbStatsNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsNoRoutes.setStatus("mandatory")
_AccAtRdbStatsAdds_Type = Counter32
_AccAtRdbStatsAdds_Object = MibScalar
accAtRdbStatsAdds = _AccAtRdbStatsAdds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 4),
    _AccAtRdbStatsAdds_Type()
)
accAtRdbStatsAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsAdds.setStatus("mandatory")
_AccAtRdbStatsUpdates_Type = Counter32
_AccAtRdbStatsUpdates_Object = MibScalar
accAtRdbStatsUpdates = _AccAtRdbStatsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 5),
    _AccAtRdbStatsUpdates_Type()
)
accAtRdbStatsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsUpdates.setStatus("mandatory")
_AccAtRdbStatsDeletes_Type = Counter32
_AccAtRdbStatsDeletes_Object = MibScalar
accAtRdbStatsDeletes = _AccAtRdbStatsDeletes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 6),
    _AccAtRdbStatsDeletes_Type()
)
accAtRdbStatsDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsDeletes.setStatus("mandatory")
_AccAtNbpStats_ObjectIdentity = ObjectIdentity
accAtNbpStats = _AccAtNbpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11)
)
_AccAtNbpStatsInBrReqs_Type = Counter32
_AccAtNbpStatsInBrReqs_Object = MibScalar
accAtNbpStatsInBrReqs = _AccAtNbpStatsInBrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 1),
    _AccAtNbpStatsInBrReqs_Type()
)
accAtNbpStatsInBrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInBrReqs.setStatus("mandatory")
_AccAtNbpStatsInLkUpReqs_Type = Counter32
_AccAtNbpStatsInLkUpReqs_Object = MibScalar
accAtNbpStatsInLkUpReqs = _AccAtNbpStatsInLkUpReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 2),
    _AccAtNbpStatsInLkUpReqs_Type()
)
accAtNbpStatsInLkUpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInLkUpReqs.setStatus("mandatory")
_AccAtNbpStatsInLkUpResps_Type = Counter32
_AccAtNbpStatsInLkUpResps_Object = MibScalar
accAtNbpStatsInLkUpResps = _AccAtNbpStatsInLkUpResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 3),
    _AccAtNbpStatsInLkUpResps_Type()
)
accAtNbpStatsInLkUpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInLkUpResps.setStatus("mandatory")
_AccAtNbpStatsInFwdReqs_Type = Counter32
_AccAtNbpStatsInFwdReqs_Object = MibScalar
accAtNbpStatsInFwdReqs = _AccAtNbpStatsInFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 4),
    _AccAtNbpStatsInFwdReqs_Type()
)
accAtNbpStatsInFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInFwdReqs.setStatus("mandatory")
_AccAtNbpStatsOutBrReqs_Type = Counter32
_AccAtNbpStatsOutBrReqs_Object = MibScalar
accAtNbpStatsOutBrReqs = _AccAtNbpStatsOutBrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 5),
    _AccAtNbpStatsOutBrReqs_Type()
)
accAtNbpStatsOutBrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutBrReqs.setStatus("mandatory")
_AccAtNbpStatsOutLkUpReqs_Type = Counter32
_AccAtNbpStatsOutLkUpReqs_Object = MibScalar
accAtNbpStatsOutLkUpReqs = _AccAtNbpStatsOutLkUpReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 6),
    _AccAtNbpStatsOutLkUpReqs_Type()
)
accAtNbpStatsOutLkUpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutLkUpReqs.setStatus("mandatory")
_AccAtNbpStatsOutLkUpResps_Type = Counter32
_AccAtNbpStatsOutLkUpResps_Object = MibScalar
accAtNbpStatsOutLkUpResps = _AccAtNbpStatsOutLkUpResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 7),
    _AccAtNbpStatsOutLkUpResps_Type()
)
accAtNbpStatsOutLkUpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutLkUpResps.setStatus("mandatory")
_AccAtNbpStatsOutFwdReqs_Type = Counter32
_AccAtNbpStatsOutFwdReqs_Object = MibScalar
accAtNbpStatsOutFwdReqs = _AccAtNbpStatsOutFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 8),
    _AccAtNbpStatsOutFwdReqs_Type()
)
accAtNbpStatsOutFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutFwdReqs.setStatus("mandatory")
_AccAtNbpStatsNoZones_Type = Counter32
_AccAtNbpStatsNoZones_Object = MibScalar
accAtNbpStatsNoZones = _AccAtNbpStatsNoZones_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 9),
    _AccAtNbpStatsNoZones_Type()
)
accAtNbpStatsNoZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsNoZones.setStatus("mandatory")
_AccAtNbpStatsInErrors_Type = Counter32
_AccAtNbpStatsInErrors_Object = MibScalar
accAtNbpStatsInErrors = _AccAtNbpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 10),
    _AccAtNbpStatsInErrors_Type()
)
accAtNbpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInErrors.setStatus("mandatory")
_AccAtNbpStatsOutErrors_Type = Counter32
_AccAtNbpStatsOutErrors_Object = MibScalar
accAtNbpStatsOutErrors = _AccAtNbpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 11),
    _AccAtNbpStatsOutErrors_Type()
)
accAtNbpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutErrors.setStatus("mandatory")
_AccAtZipStats_ObjectIdentity = ObjectIdentity
accAtZipStats = _AccAtZipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12)
)
_AccAtZipStatsInQuerys_Type = Counter32
_AccAtZipStatsInQuerys_Object = MibScalar
accAtZipStatsInQuerys = _AccAtZipStatsInQuerys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 1),
    _AccAtZipStatsInQuerys_Type()
)
accAtZipStatsInQuerys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInQuerys.setStatus("mandatory")
_AccAtZipStatsInReplies_Type = Counter32
_AccAtZipStatsInReplies_Object = MibScalar
accAtZipStatsInReplies = _AccAtZipStatsInReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 2),
    _AccAtZipStatsInReplies_Type()
)
accAtZipStatsInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInReplies.setStatus("mandatory")
_AccAtZipStatsInExtReplies_Type = Counter32
_AccAtZipStatsInExtReplies_Object = MibScalar
accAtZipStatsInExtReplies = _AccAtZipStatsInExtReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 3),
    _AccAtZipStatsInExtReplies_Type()
)
accAtZipStatsInExtReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInExtReplies.setStatus("mandatory")
_AccAtZipStatsInInfoReqs_Type = Counter32
_AccAtZipStatsInInfoReqs_Object = MibScalar
accAtZipStatsInInfoReqs = _AccAtZipStatsInInfoReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 4),
    _AccAtZipStatsInInfoReqs_Type()
)
accAtZipStatsInInfoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInInfoReqs.setStatus("mandatory")
_AccAtZipStatsInInfoReps_Type = Counter32
_AccAtZipStatsInInfoReps_Object = MibScalar
accAtZipStatsInInfoReps = _AccAtZipStatsInInfoReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 5),
    _AccAtZipStatsInInfoReps_Type()
)
accAtZipStatsInInfoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInInfoReps.setStatus("mandatory")
_AccAtZipStatsInTakeDowns_Type = Counter32
_AccAtZipStatsInTakeDowns_Object = MibScalar
accAtZipStatsInTakeDowns = _AccAtZipStatsInTakeDowns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 6),
    _AccAtZipStatsInTakeDowns_Type()
)
accAtZipStatsInTakeDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInTakeDowns.setStatus("mandatory")
_AccAtZipStatsInBringUps_Type = Counter32
_AccAtZipStatsInBringUps_Object = MibScalar
accAtZipStatsInBringUps = _AccAtZipStatsInBringUps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 7),
    _AccAtZipStatsInBringUps_Type()
)
accAtZipStatsInBringUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInBringUps.setStatus("mandatory")
_AccAtZipStatsInNotifies_Type = Counter32
_AccAtZipStatsInNotifies_Object = MibScalar
accAtZipStatsInNotifies = _AccAtZipStatsInNotifies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 8),
    _AccAtZipStatsInNotifies_Type()
)
accAtZipStatsInNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInNotifies.setStatus("mandatory")
_AccAtZipStatsInGetZLReqs_Type = Counter32
_AccAtZipStatsInGetZLReqs_Object = MibScalar
accAtZipStatsInGetZLReqs = _AccAtZipStatsInGetZLReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 9),
    _AccAtZipStatsInGetZLReqs_Type()
)
accAtZipStatsInGetZLReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInGetZLReqs.setStatus("mandatory")
_AccAtZipStatsInGetLZReqs_Type = Counter32
_AccAtZipStatsInGetLZReqs_Object = MibScalar
accAtZipStatsInGetLZReqs = _AccAtZipStatsInGetLZReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 10),
    _AccAtZipStatsInGetLZReqs_Type()
)
accAtZipStatsInGetLZReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInGetLZReqs.setStatus("mandatory")
_AccAtZipStatsInGetMZReqs_Type = Counter32
_AccAtZipStatsInGetMZReqs_Object = MibScalar
accAtZipStatsInGetMZReqs = _AccAtZipStatsInGetMZReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 11),
    _AccAtZipStatsInGetMZReqs_Type()
)
accAtZipStatsInGetMZReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInGetMZReqs.setStatus("mandatory")
_AccAtZipStatsOutQueries_Type = Counter32
_AccAtZipStatsOutQueries_Object = MibScalar
accAtZipStatsOutQueries = _AccAtZipStatsOutQueries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 12),
    _AccAtZipStatsOutQueries_Type()
)
accAtZipStatsOutQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutQueries.setStatus("mandatory")
_AccAtZipStatsOutReplies_Type = Counter32
_AccAtZipStatsOutReplies_Object = MibScalar
accAtZipStatsOutReplies = _AccAtZipStatsOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 13),
    _AccAtZipStatsOutReplies_Type()
)
accAtZipStatsOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutReplies.setStatus("mandatory")
_AccAtZipStatsOutExtReplies_Type = Counter32
_AccAtZipStatsOutExtReplies_Object = MibScalar
accAtZipStatsOutExtReplies = _AccAtZipStatsOutExtReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 14),
    _AccAtZipStatsOutExtReplies_Type()
)
accAtZipStatsOutExtReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutExtReplies.setStatus("mandatory")
_AccAtZipStatsOutInfoReqs_Type = Counter32
_AccAtZipStatsOutInfoReqs_Object = MibScalar
accAtZipStatsOutInfoReqs = _AccAtZipStatsOutInfoReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 15),
    _AccAtZipStatsOutInfoReqs_Type()
)
accAtZipStatsOutInfoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutInfoReqs.setStatus("mandatory")
_AccAtZipStatsOutInfoReps_Type = Counter32
_AccAtZipStatsOutInfoReps_Object = MibScalar
accAtZipStatsOutInfoReps = _AccAtZipStatsOutInfoReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 16),
    _AccAtZipStatsOutInfoReps_Type()
)
accAtZipStatsOutInfoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutInfoReps.setStatus("mandatory")
_AccAtZipStatsOutGetZLReps_Type = Counter32
_AccAtZipStatsOutGetZLReps_Object = MibScalar
accAtZipStatsOutGetZLReps = _AccAtZipStatsOutGetZLReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 17),
    _AccAtZipStatsOutGetZLReps_Type()
)
accAtZipStatsOutGetZLReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutGetZLReps.setStatus("mandatory")
_AccAtZipStatsOutGetLZReps_Type = Counter32
_AccAtZipStatsOutGetLZReps_Object = MibScalar
accAtZipStatsOutGetLZReps = _AccAtZipStatsOutGetLZReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 18),
    _AccAtZipStatsOutGetLZReps_Type()
)
accAtZipStatsOutGetLZReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutGetLZReps.setStatus("mandatory")
_AccAtZipStatsOutGetMZReps_Type = Counter32
_AccAtZipStatsOutGetMZReps_Object = MibScalar
accAtZipStatsOutGetMZReps = _AccAtZipStatsOutGetMZReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 19),
    _AccAtZipStatsOutGetMZReps_Type()
)
accAtZipStatsOutGetMZReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutGetMZReps.setStatus("mandatory")
_AccAtZipStatsZoneConflicts_Type = Counter32
_AccAtZipStatsZoneConflicts_Object = MibScalar
accAtZipStatsZoneConflicts = _AccAtZipStatsZoneConflicts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 20),
    _AccAtZipStatsZoneConflicts_Type()
)
accAtZipStatsZoneConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsZoneConflicts.setStatus("mandatory")
_AccAtZipStatsInErrors_Type = Counter32
_AccAtZipStatsInErrors_Object = MibScalar
accAtZipStatsInErrors = _AccAtZipStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 21),
    _AccAtZipStatsInErrors_Type()
)
accAtZipStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInErrors.setStatus("mandatory")
_AccAtZipStatsOutErrors_Type = Counter32
_AccAtZipStatsOutErrors_Object = MibScalar
accAtZipStatsOutErrors = _AccAtZipStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 22),
    _AccAtZipStatsOutErrors_Type()
)
accAtZipStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutErrors.setStatus("mandatory")
_AccAtAepStats_ObjectIdentity = ObjectIdentity
accAtAepStats = _AccAtAepStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 13)
)
_AccAtAepStatsInErrors_Type = Counter32
_AccAtAepStatsInErrors_Object = MibScalar
accAtAepStatsInErrors = _AccAtAepStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 13, 1),
    _AccAtAepStatsInErrors_Type()
)
accAtAepStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAepStatsInErrors.setStatus("mandatory")
_AccAtAepStatsOutErrors_Type = Counter32
_AccAtAepStatsOutErrors_Object = MibScalar
accAtAepStatsOutErrors = _AccAtAepStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 13, 2),
    _AccAtAepStatsOutErrors_Type()
)
accAtAepStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAepStatsOutErrors.setStatus("mandatory")
_AccAtZoneListTable_Object = MibTable
accAtZoneListTable = _AccAtZoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14)
)
if mibBuilder.loadTexts:
    accAtZoneListTable.setStatus("mandatory")
_AccAtZoneListEntry_Object = MibTableRow
accAtZoneListEntry = _AccAtZoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1)
)
accAtZoneListEntry.setIndexNames(
    (0, "ACC-AT", "accAtZoneListPort"),
    (0, "ACC-AT", "accAtZoneListName"),
)
if mibBuilder.loadTexts:
    accAtZoneListEntry.setStatus("mandatory")


class _AccAtZoneListPort_Type(Integer32):
    """Custom type accAtZoneListPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccAtZoneListPort_Type.__name__ = "Integer32"
_AccAtZoneListPort_Object = MibTableColumn
accAtZoneListPort = _AccAtZoneListPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1, 1),
    _AccAtZoneListPort_Type()
)
accAtZoneListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneListPort.setStatus("mandatory")


class _AccAtZoneListStatus_Type(Integer32):
    """Custom type accAtZoneListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("default", 2),
          ("invalid", 3))
    )


_AccAtZoneListStatus_Type.__name__ = "Integer32"
_AccAtZoneListStatus_Object = MibTableColumn
accAtZoneListStatus = _AccAtZoneListStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1, 2),
    _AccAtZoneListStatus_Type()
)
accAtZoneListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtZoneListStatus.setStatus("mandatory")
_AccAtZoneListName_Type = DisplayString
_AccAtZoneListName_Object = MibTableColumn
accAtZoneListName = _AccAtZoneListName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1, 3),
    _AccAtZoneListName_Type()
)
accAtZoneListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneListName.setStatus("mandatory")
_AccAtZoneBynameTable_Object = MibTable
accAtZoneBynameTable = _AccAtZoneBynameTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15)
)
if mibBuilder.loadTexts:
    accAtZoneBynameTable.setStatus("mandatory")
_AccAtZoneBynameEntry_Object = MibTableRow
accAtZoneBynameEntry = _AccAtZoneBynameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1)
)
accAtZoneBynameEntry.setIndexNames(
    (0, "ACC-AT", "accAtZoneBynameNetMin"),
    (0, "ACC-AT", "accAtZoneBynameName"),
)
if mibBuilder.loadTexts:
    accAtZoneBynameEntry.setStatus("mandatory")
_AccAtZoneBynameNetMin_Type = OctetString
_AccAtZoneBynameNetMin_Object = MibTableColumn
accAtZoneBynameNetMin = _AccAtZoneBynameNetMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1, 1),
    _AccAtZoneBynameNetMin_Type()
)
accAtZoneBynameNetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynameNetMin.setStatus("mandatory")
_AccAtZoneBynameNetMax_Type = OctetString
_AccAtZoneBynameNetMax_Object = MibTableColumn
accAtZoneBynameNetMax = _AccAtZoneBynameNetMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1, 2),
    _AccAtZoneBynameNetMax_Type()
)
accAtZoneBynameNetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynameNetMax.setStatus("mandatory")
_AccAtZoneBynameName_Type = DisplayString
_AccAtZoneBynameName_Object = MibTableColumn
accAtZoneBynameName = _AccAtZoneBynameName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1, 3),
    _AccAtZoneBynameName_Type()
)
accAtZoneBynameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynameName.setStatus("mandatory")
_AccAtZoneBynetTable_Object = MibTable
accAtZoneBynetTable = _AccAtZoneBynetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16)
)
if mibBuilder.loadTexts:
    accAtZoneBynetTable.setStatus("mandatory")
_AccAtZoneBynetEntry_Object = MibTableRow
accAtZoneBynetEntry = _AccAtZoneBynetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1)
)
accAtZoneBynetEntry.setIndexNames(
    (0, "ACC-AT", "accAtZoneBynameNetMin"),
    (0, "ACC-AT", "accAtZoneBynameName"),
)
if mibBuilder.loadTexts:
    accAtZoneBynetEntry.setStatus("mandatory")
_AccAtZoneBynetNetMin_Type = OctetString
_AccAtZoneBynetNetMin_Object = MibTableColumn
accAtZoneBynetNetMin = _AccAtZoneBynetNetMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1, 1),
    _AccAtZoneBynetNetMin_Type()
)
accAtZoneBynetNetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynetNetMin.setStatus("mandatory")
_AccAtZoneBynetNetMax_Type = OctetString
_AccAtZoneBynetNetMax_Object = MibTableColumn
accAtZoneBynetNetMax = _AccAtZoneBynetNetMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1, 2),
    _AccAtZoneBynetNetMax_Type()
)
accAtZoneBynetNetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynetNetMax.setStatus("mandatory")
_AccAtZoneBynetName_Type = DisplayString
_AccAtZoneBynetName_Object = MibTableColumn
accAtZoneBynetName = _AccAtZoneBynetName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1, 3),
    _AccAtZoneBynetName_Type()
)
accAtZoneBynetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynetName.setStatus("mandatory")
_AccAtForwardFilterTable_Object = MibTable
accAtForwardFilterTable = _AccAtForwardFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17)
)
if mibBuilder.loadTexts:
    accAtForwardFilterTable.setStatus("mandatory")
_AccAtForwardFilterEntry_Object = MibTableRow
accAtForwardFilterEntry = _AccAtForwardFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1)
)
accAtForwardFilterEntry.setIndexNames(
    (0, "ACC-AT", "accAtForwardFilterToMin"),
    (0, "ACC-AT", "accAtForwardFilterToMax"),
    (0, "ACC-AT", "accAtForwardFilterFromMin"),
    (0, "ACC-AT", "accAtForwardFilterFromMax"),
    (0, "ACC-AT", "accAtForwardFilterSocketMin"),
    (0, "ACC-AT", "accAtForwardFilterSocketMax"),
    (0, "ACC-AT", "accAtForwardFilterType"),
)
if mibBuilder.loadTexts:
    accAtForwardFilterEntry.setStatus("mandatory")
_AccAtForwardFilterToMin_Type = OctetString
_AccAtForwardFilterToMin_Object = MibTableColumn
accAtForwardFilterToMin = _AccAtForwardFilterToMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 1),
    _AccAtForwardFilterToMin_Type()
)
accAtForwardFilterToMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterToMin.setStatus("mandatory")
_AccAtForwardFilterToMax_Type = OctetString
_AccAtForwardFilterToMax_Object = MibTableColumn
accAtForwardFilterToMax = _AccAtForwardFilterToMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 2),
    _AccAtForwardFilterToMax_Type()
)
accAtForwardFilterToMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterToMax.setStatus("mandatory")
_AccAtForwardFilterFromMin_Type = OctetString
_AccAtForwardFilterFromMin_Object = MibTableColumn
accAtForwardFilterFromMin = _AccAtForwardFilterFromMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 3),
    _AccAtForwardFilterFromMin_Type()
)
accAtForwardFilterFromMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterFromMin.setStatus("mandatory")
_AccAtForwardFilterFromMax_Type = OctetString
_AccAtForwardFilterFromMax_Object = MibTableColumn
accAtForwardFilterFromMax = _AccAtForwardFilterFromMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 4),
    _AccAtForwardFilterFromMax_Type()
)
accAtForwardFilterFromMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterFromMax.setStatus("mandatory")


class _AccAtForwardFilterSocketMin_Type(Integer32):
    """Custom type accAtForwardFilterSocketMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccAtForwardFilterSocketMin_Type.__name__ = "Integer32"
_AccAtForwardFilterSocketMin_Object = MibTableColumn
accAtForwardFilterSocketMin = _AccAtForwardFilterSocketMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 5),
    _AccAtForwardFilterSocketMin_Type()
)
accAtForwardFilterSocketMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterSocketMin.setStatus("mandatory")


class _AccAtForwardFilterSocketMax_Type(Integer32):
    """Custom type accAtForwardFilterSocketMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccAtForwardFilterSocketMax_Type.__name__ = "Integer32"
_AccAtForwardFilterSocketMax_Object = MibTableColumn
accAtForwardFilterSocketMax = _AccAtForwardFilterSocketMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 6),
    _AccAtForwardFilterSocketMax_Type()
)
accAtForwardFilterSocketMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterSocketMax.setStatus("mandatory")


class _AccAtForwardFilterType_Type(Integer32):
    """Custom type accAtForwardFilterType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("adsp", 7),
          ("aep", 4),
          ("any", 1),
          ("atp", 3),
          ("nbp", 2),
          ("nbpBroadcast", 8),
          ("nbpForwardRequest", 11),
          ("nbpRequest", 9),
          ("nbpResponse", 10),
          ("rtmp", 5),
          ("zip", 6))
    )


_AccAtForwardFilterType_Type.__name__ = "Integer32"
_AccAtForwardFilterType_Object = MibTableColumn
accAtForwardFilterType = _AccAtForwardFilterType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 7),
    _AccAtForwardFilterType_Type()
)
accAtForwardFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterType.setStatus("mandatory")


class _AccAtForwardFilterDisposition_Type(Integer32):
    """Custom type accAtForwardFilterDisposition based on Integer32"""
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
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccAtForwardFilterDisposition_Type.__name__ = "Integer32"
_AccAtForwardFilterDisposition_Object = MibTableColumn
accAtForwardFilterDisposition = _AccAtForwardFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 8),
    _AccAtForwardFilterDisposition_Type()
)
accAtForwardFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterDisposition.setStatus("mandatory")


class _AccAtForwardFilterStatus_Type(Integer32):
    """Custom type accAtForwardFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccAtForwardFilterStatus_Type.__name__ = "Integer32"
_AccAtForwardFilterStatus_Object = MibTableColumn
accAtForwardFilterStatus = _AccAtForwardFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 9),
    _AccAtForwardFilterStatus_Type()
)
accAtForwardFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterStatus.setStatus("mandatory")
_AccAtRouteFilterTable_Object = MibTable
accAtRouteFilterTable = _AccAtRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18)
)
if mibBuilder.loadTexts:
    accAtRouteFilterTable.setStatus("mandatory")
_AccAtRouteFilterEntry_Object = MibTableRow
accAtRouteFilterEntry = _AccAtRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1)
)
accAtRouteFilterEntry.setIndexNames(
    (0, "ACC-AT", "accAtRouteFilterRouterMin"),
    (0, "ACC-AT", "accAtRouteFilterRouterMax"),
    (0, "ACC-AT", "accAtRouteFilterRangeMin"),
    (0, "ACC-AT", "accAtRouteFilterRangeMax"),
)
if mibBuilder.loadTexts:
    accAtRouteFilterEntry.setStatus("mandatory")
_AccAtRouteFilterRouterMin_Type = OctetString
_AccAtRouteFilterRouterMin_Object = MibTableColumn
accAtRouteFilterRouterMin = _AccAtRouteFilterRouterMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 1),
    _AccAtRouteFilterRouterMin_Type()
)
accAtRouteFilterRouterMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRouterMin.setStatus("mandatory")
_AccAtRouteFilterRouterMax_Type = OctetString
_AccAtRouteFilterRouterMax_Object = MibTableColumn
accAtRouteFilterRouterMax = _AccAtRouteFilterRouterMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 2),
    _AccAtRouteFilterRouterMax_Type()
)
accAtRouteFilterRouterMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRouterMax.setStatus("mandatory")
_AccAtRouteFilterRangeMin_Type = OctetString
_AccAtRouteFilterRangeMin_Object = MibTableColumn
accAtRouteFilterRangeMin = _AccAtRouteFilterRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 3),
    _AccAtRouteFilterRangeMin_Type()
)
accAtRouteFilterRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRangeMin.setStatus("mandatory")
_AccAtRouteFilterRangeMax_Type = OctetString
_AccAtRouteFilterRangeMax_Object = MibTableColumn
accAtRouteFilterRangeMax = _AccAtRouteFilterRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 4),
    _AccAtRouteFilterRangeMax_Type()
)
accAtRouteFilterRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRangeMax.setStatus("mandatory")


class _AccAtRouteFilterDisposition_Type(Integer32):
    """Custom type accAtRouteFilterDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccAtRouteFilterDisposition_Type.__name__ = "Integer32"
_AccAtRouteFilterDisposition_Object = MibTableColumn
accAtRouteFilterDisposition = _AccAtRouteFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 5),
    _AccAtRouteFilterDisposition_Type()
)
accAtRouteFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterDisposition.setStatus("mandatory")


class _AccAtRouteFilterStatus_Type(Integer32):
    """Custom type accAtRouteFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccAtRouteFilterStatus_Type.__name__ = "Integer32"
_AccAtRouteFilterStatus_Object = MibTableColumn
accAtRouteFilterStatus = _AccAtRouteFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 6),
    _AccAtRouteFilterStatus_Type()
)
accAtRouteFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-AT",
    **{"accAt": accAt,
       "accAtNode": accAtNode,
       "accAtNodeAdState": accAtNodeAdState,
       "accAtNodeChecksum": accAtNodeChecksum,
       "accAtNodeAarpExpire": accAtNodeAarpExpire,
       "accAtNodeFfrRouting": accAtNodeFfrRouting,
       "accAtAarpTable": accAtAarpTable,
       "accAtAarpEntry": accAtAarpEntry,
       "accAtAarpTabPort": accAtAarpTabPort,
       "accAtAarpTabMacAddr": accAtAarpTabMacAddr,
       "accAtAarpTabNetAddr": accAtAarpTabNetAddr,
       "accAtAarpTabStatus": accAtAarpTabStatus,
       "accAtAarpStatsTable": accAtAarpStatsTable,
       "accAtAarpStatsEntry": accAtAarpStatsEntry,
       "accAtAarpStatsInRequests": accAtAarpStatsInRequests,
       "accAtAarpStatsInResponses": accAtAarpStatsInResponses,
       "accAtAarpStatsInProbes": accAtAarpStatsInProbes,
       "accAtAarpStatsOutRequests": accAtAarpStatsOutRequests,
       "accAtAarpStatsOutResponses": accAtAarpStatsOutResponses,
       "accAtAarpStatsOutProbes": accAtAarpStatsOutProbes,
       "accAtAarpStatsNoReplys": accAtAarpStatsNoReplys,
       "accAtAarpStatsExpires": accAtAarpStatsExpires,
       "accAtAarpStatsDiscards": accAtAarpStatsDiscards,
       "accAtAarpStatsInErrors": accAtAarpStatsInErrors,
       "accAtAarpStatsOutErrors": accAtAarpStatsOutErrors,
       "accAtAdbStats": accAtAdbStats,
       "accAtAdbStatsCacheds": accAtAdbStatsCacheds,
       "accAtAdbStatsRotates": accAtAdbStatsRotates,
       "accAtAdbStatsNoEntries": accAtAdbStatsNoEntries,
       "accAtAdbStatsAdds": accAtAdbStatsAdds,
       "accAtAdbStatsUpdates": accAtAdbStatsUpdates,
       "accAtAdbStatsDeletes": accAtAdbStatsDeletes,
       "accAtAdbStatsTrims": accAtAdbStatsTrims,
       "accAtAdbStatsDiscards": accAtAdbStatsDiscards,
       "accAtDdpStats": accAtDdpStats,
       "accAtDdpStatsNoOutRoutes": accAtDdpStatsNoOutRoutes,
       "accAtDdpStatsInErrors": accAtDdpStatsInErrors,
       "accAtDdpStatsOutErrors": accAtDdpStatsOutErrors,
       "accAtNetTable": accAtNetTable,
       "accAtNetEntry": accAtNetEntry,
       "accAtNetTabProtocol": accAtNetTabProtocol,
       "accAtNetTabRtmpIncr": accAtNetTabRtmpIncr,
       "accAtNetTabRtmpSend": accAtNetTabRtmpSend,
       "accAtNetTabX25Addr1": accAtNetTabX25Addr1,
       "accAtNetTabX25Addr2": accAtNetTabX25Addr2,
       "accAtNetTabX25Idle": accAtNetTabX25Idle,
       "accAtNetTabX25PktSize": accAtNetTabX25PktSize,
       "accAtNetTabX25WinSize": accAtNetTabX25WinSize,
       "accAtNetTabX25FacIndex": accAtNetTabX25FacIndex,
       "accAtPortTable": accAtPortTable,
       "accAtPortEntry": accAtPortEntry,
       "accAtPortTabIndex": accAtPortTabIndex,
       "accAtPortTabNetAddr": accAtPortTabNetAddr,
       "accAtPortTabState": accAtPortTabState,
       "accAtPortTabDescr": accAtPortTabDescr,
       "accAtPortTabErrCode": accAtPortTabErrCode,
       "accAtPortTabErrTime": accAtPortTabErrTime,
       "accAtPortTabErrAddr": accAtPortTabErrAddr,
       "accAtPortTabErrDescr": accAtPortTabErrDescr,
       "accAtPortTabErrCount": accAtPortTabErrCount,
       "accAtPortStatsTable": accAtPortStatsTable,
       "accAtPortStatsEntry": accAtPortStatsEntry,
       "accAtPortStatsInTotals": accAtPortStatsInTotals,
       "accAtPortStatsInShorts": accAtPortStatsInShorts,
       "accAtPortStatsNotForMes": accAtPortStatsNotForMes,
       "accAtPortStatsTooShorts": accAtPortStatsTooShorts,
       "accAtPortStatsTooLongs": accAtPortStatsTooLongs,
       "accAtPortStatsChksums": accAtPortStatsChksums,
       "accAtPortStatsNotMyNets": accAtPortStatsNotMyNets,
       "accAtPortStatsInFwdReqs": accAtPortStatsInFwdReqs,
       "accAtPortStatsFwdBcasts": accAtPortStatsFwdBcasts,
       "accAtPortStatsNoFwdRoutes": accAtPortStatsNoFwdRoutes,
       "accAtPortStatsHopCounts": accAtPortStatsHopCounts,
       "accAtPortStatsReflects": accAtPortStatsReflects,
       "accAtPortStatsOutTotals": accAtPortStatsOutTotals,
       "accAtPortStatsOutShorts": accAtPortStatsOutShorts,
       "accAtPortStatsOutFwdReqs": accAtPortStatsOutFwdReqs,
       "accAtPortStatsInErrors": accAtPortStatsInErrors,
       "accAtPortStatsOutErrors": accAtPortStatsOutErrors,
       "accAtRtmpStats": accAtRtmpStats,
       "accAtRtmpStatsInRequests": accAtRtmpStatsInRequests,
       "accAtRtmpStatsInDataReqs": accAtRtmpStatsInDataReqs,
       "accAtRtmpStatsInResponses": accAtRtmpStatsInResponses,
       "accAtRtmpStatsInDataResps": accAtRtmpStatsInDataResps,
       "accAtRtmpStatsOutRequests": accAtRtmpStatsOutRequests,
       "accAtRtmpStatsOutDataReqs": accAtRtmpStatsOutDataReqs,
       "accAtRtmpStatsOutResponses": accAtRtmpStatsOutResponses,
       "accAtRtmpStatsOutDataResps": accAtRtmpStatsOutDataResps,
       "accAtRtmpStatsNetConflicts": accAtRtmpStatsNetConflicts,
       "accAtRtmpStatsInErrors": accAtRtmpStatsInErrors,
       "accAtRtmpStatsOutErrors": accAtRtmpStatsOutErrors,
       "accAtRdbStats": accAtRdbStats,
       "accAtRdbStatsCacheds": accAtRdbStatsCacheds,
       "accAtRdbStatsSearchs": accAtRdbStatsSearchs,
       "accAtRdbStatsNoRoutes": accAtRdbStatsNoRoutes,
       "accAtRdbStatsAdds": accAtRdbStatsAdds,
       "accAtRdbStatsUpdates": accAtRdbStatsUpdates,
       "accAtRdbStatsDeletes": accAtRdbStatsDeletes,
       "accAtNbpStats": accAtNbpStats,
       "accAtNbpStatsInBrReqs": accAtNbpStatsInBrReqs,
       "accAtNbpStatsInLkUpReqs": accAtNbpStatsInLkUpReqs,
       "accAtNbpStatsInLkUpResps": accAtNbpStatsInLkUpResps,
       "accAtNbpStatsInFwdReqs": accAtNbpStatsInFwdReqs,
       "accAtNbpStatsOutBrReqs": accAtNbpStatsOutBrReqs,
       "accAtNbpStatsOutLkUpReqs": accAtNbpStatsOutLkUpReqs,
       "accAtNbpStatsOutLkUpResps": accAtNbpStatsOutLkUpResps,
       "accAtNbpStatsOutFwdReqs": accAtNbpStatsOutFwdReqs,
       "accAtNbpStatsNoZones": accAtNbpStatsNoZones,
       "accAtNbpStatsInErrors": accAtNbpStatsInErrors,
       "accAtNbpStatsOutErrors": accAtNbpStatsOutErrors,
       "accAtZipStats": accAtZipStats,
       "accAtZipStatsInQuerys": accAtZipStatsInQuerys,
       "accAtZipStatsInReplies": accAtZipStatsInReplies,
       "accAtZipStatsInExtReplies": accAtZipStatsInExtReplies,
       "accAtZipStatsInInfoReqs": accAtZipStatsInInfoReqs,
       "accAtZipStatsInInfoReps": accAtZipStatsInInfoReps,
       "accAtZipStatsInTakeDowns": accAtZipStatsInTakeDowns,
       "accAtZipStatsInBringUps": accAtZipStatsInBringUps,
       "accAtZipStatsInNotifies": accAtZipStatsInNotifies,
       "accAtZipStatsInGetZLReqs": accAtZipStatsInGetZLReqs,
       "accAtZipStatsInGetLZReqs": accAtZipStatsInGetLZReqs,
       "accAtZipStatsInGetMZReqs": accAtZipStatsInGetMZReqs,
       "accAtZipStatsOutQueries": accAtZipStatsOutQueries,
       "accAtZipStatsOutReplies": accAtZipStatsOutReplies,
       "accAtZipStatsOutExtReplies": accAtZipStatsOutExtReplies,
       "accAtZipStatsOutInfoReqs": accAtZipStatsOutInfoReqs,
       "accAtZipStatsOutInfoReps": accAtZipStatsOutInfoReps,
       "accAtZipStatsOutGetZLReps": accAtZipStatsOutGetZLReps,
       "accAtZipStatsOutGetLZReps": accAtZipStatsOutGetLZReps,
       "accAtZipStatsOutGetMZReps": accAtZipStatsOutGetMZReps,
       "accAtZipStatsZoneConflicts": accAtZipStatsZoneConflicts,
       "accAtZipStatsInErrors": accAtZipStatsInErrors,
       "accAtZipStatsOutErrors": accAtZipStatsOutErrors,
       "accAtAepStats": accAtAepStats,
       "accAtAepStatsInErrors": accAtAepStatsInErrors,
       "accAtAepStatsOutErrors": accAtAepStatsOutErrors,
       "accAtZoneListTable": accAtZoneListTable,
       "accAtZoneListEntry": accAtZoneListEntry,
       "accAtZoneListPort": accAtZoneListPort,
       "accAtZoneListStatus": accAtZoneListStatus,
       "accAtZoneListName": accAtZoneListName,
       "accAtZoneBynameTable": accAtZoneBynameTable,
       "accAtZoneBynameEntry": accAtZoneBynameEntry,
       "accAtZoneBynameNetMin": accAtZoneBynameNetMin,
       "accAtZoneBynameNetMax": accAtZoneBynameNetMax,
       "accAtZoneBynameName": accAtZoneBynameName,
       "accAtZoneBynetTable": accAtZoneBynetTable,
       "accAtZoneBynetEntry": accAtZoneBynetEntry,
       "accAtZoneBynetNetMin": accAtZoneBynetNetMin,
       "accAtZoneBynetNetMax": accAtZoneBynetNetMax,
       "accAtZoneBynetName": accAtZoneBynetName,
       "accAtForwardFilterTable": accAtForwardFilterTable,
       "accAtForwardFilterEntry": accAtForwardFilterEntry,
       "accAtForwardFilterToMin": accAtForwardFilterToMin,
       "accAtForwardFilterToMax": accAtForwardFilterToMax,
       "accAtForwardFilterFromMin": accAtForwardFilterFromMin,
       "accAtForwardFilterFromMax": accAtForwardFilterFromMax,
       "accAtForwardFilterSocketMin": accAtForwardFilterSocketMin,
       "accAtForwardFilterSocketMax": accAtForwardFilterSocketMax,
       "accAtForwardFilterType": accAtForwardFilterType,
       "accAtForwardFilterDisposition": accAtForwardFilterDisposition,
       "accAtForwardFilterStatus": accAtForwardFilterStatus,
       "accAtRouteFilterTable": accAtRouteFilterTable,
       "accAtRouteFilterEntry": accAtRouteFilterEntry,
       "accAtRouteFilterRouterMin": accAtRouteFilterRouterMin,
       "accAtRouteFilterRouterMax": accAtRouteFilterRouterMax,
       "accAtRouteFilterRangeMin": accAtRouteFilterRangeMin,
       "accAtRouteFilterRangeMax": accAtRouteFilterRangeMax,
       "accAtRouteFilterDisposition": accAtRouteFilterDisposition,
       "accAtRouteFilterStatus": accAtRouteFilterStatus}
)
