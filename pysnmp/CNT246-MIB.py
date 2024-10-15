# SNMP MIB module (CNT246-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT246-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:59 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cnt2Transport = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6)
)
cnt2Transport.setRevisions(
        ("1901-03-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cnt2TransportTable_Object = MibTable
cnt2TransportTable = _Cnt2TransportTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    cnt2TransportTable.setStatus("current")
_Cnt2TransportEntry_Object = MibTableRow
cnt2TransportEntry = _Cnt2TransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1)
)
cnt2TransportEntry.setIndexNames(
    (0, "CNT246-MIB", "cnt2TransportSlotIndex"),
    (0, "CNT246-MIB", "cnt2TransportIndex"),
)
if mibBuilder.loadTexts:
    cnt2TransportEntry.setStatus("current")
_Cnt2TransportSlotIndex_Type = Integer32
_Cnt2TransportSlotIndex_Object = MibTableColumn
cnt2TransportSlotIndex = _Cnt2TransportSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 1),
    _Cnt2TransportSlotIndex_Type()
)
cnt2TransportSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportSlotIndex.setStatus("current")
_Cnt2TransportIndex_Type = Integer32
_Cnt2TransportIndex_Object = MibTableColumn
cnt2TransportIndex = _Cnt2TransportIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 2),
    _Cnt2TransportIndex_Type()
)
cnt2TransportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportIndex.setStatus("current")
_Cnt2TransportBus_Type = Integer32
_Cnt2TransportBus_Object = MibTableColumn
cnt2TransportBus = _Cnt2TransportBus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 3),
    _Cnt2TransportBus_Type()
)
cnt2TransportBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportBus.setStatus("current")
_Cnt2TransportVid_Type = Integer32
_Cnt2TransportVid_Object = MibTableColumn
cnt2TransportVid = _Cnt2TransportVid_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 4),
    _Cnt2TransportVid_Type()
)
cnt2TransportVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportVid.setStatus("current")


class _Cnt2TransportLinkType_Type(Integer32):
    """Custom type cnt2TransportLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11,
              12,
              13,
              14,
              99)
        )
    )
    namedValues = NamedValues(
        *(("atm", 8),
          ("ds3e3", 12),
          ("ethernet", 9),
          ("fddi", 11),
          ("fibrechannel", 10),
          ("ipv4", 14),
          ("lane", 13),
          ("unknown", 99))
    )


_Cnt2TransportLinkType_Type.__name__ = "Integer32"
_Cnt2TransportLinkType_Object = MibTableColumn
cnt2TransportLinkType = _Cnt2TransportLinkType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 5),
    _Cnt2TransportLinkType_Type()
)
cnt2TransportLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportLinkType.setStatus("current")
_Cnt2TransportLinkDesc_Type = DisplayString
_Cnt2TransportLinkDesc_Object = MibTableColumn
cnt2TransportLinkDesc = _Cnt2TransportLinkDesc_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 6),
    _Cnt2TransportLinkDesc_Type()
)
cnt2TransportLinkDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportLinkDesc.setStatus("current")


class _Cnt2TransportLinkStatus_Type(Integer32):
    """Custom type cnt2TransportLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cnt2TransportLinkStatus_Type.__name__ = "Integer32"
_Cnt2TransportLinkStatus_Object = MibTableColumn
cnt2TransportLinkStatus = _Cnt2TransportLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 7),
    _Cnt2TransportLinkStatus_Type()
)
cnt2TransportLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportLinkStatus.setStatus("current")


class _Cnt2TransportIPtosPrecedence_Type(Integer32):
    """Custom type cnt2TransportIPtosPrecedence based on Integer32"""
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
        *(("criticECP", 6),
          ("flash", 4),
          ("flashOverride", 5),
          ("immediate", 3),
          ("internetworkControl", 7),
          ("networkControl", 8),
          ("priority", 2),
          ("routine", 1))
    )


_Cnt2TransportIPtosPrecedence_Type.__name__ = "Integer32"
_Cnt2TransportIPtosPrecedence_Object = MibTableColumn
cnt2TransportIPtosPrecedence = _Cnt2TransportIPtosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 8),
    _Cnt2TransportIPtosPrecedence_Type()
)
cnt2TransportIPtosPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportIPtosPrecedence.setStatus("current")


class _Cnt2TransportIPtosDelay_Type(Integer32):
    """Custom type cnt2TransportIPtosDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Cnt2TransportIPtosDelay_Type.__name__ = "Integer32"
_Cnt2TransportIPtosDelay_Object = MibTableColumn
cnt2TransportIPtosDelay = _Cnt2TransportIPtosDelay_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 9),
    _Cnt2TransportIPtosDelay_Type()
)
cnt2TransportIPtosDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportIPtosDelay.setStatus("current")


class _Cnt2TransportIPtosThruput_Type(Integer32):
    """Custom type cnt2TransportIPtosThruput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_Cnt2TransportIPtosThruput_Type.__name__ = "Integer32"
_Cnt2TransportIPtosThruput_Object = MibTableColumn
cnt2TransportIPtosThruput = _Cnt2TransportIPtosThruput_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 10),
    _Cnt2TransportIPtosThruput_Type()
)
cnt2TransportIPtosThruput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportIPtosThruput.setStatus("current")


class _Cnt2TransportIPtosRelibility_Type(Integer32):
    """Custom type cnt2TransportIPtosRelibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_Cnt2TransportIPtosRelibility_Type.__name__ = "Integer32"
_Cnt2TransportIPtosRelibility_Object = MibTableColumn
cnt2TransportIPtosRelibility = _Cnt2TransportIPtosRelibility_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 11),
    _Cnt2TransportIPtosRelibility_Type()
)
cnt2TransportIPtosRelibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportIPtosRelibility.setStatus("current")


class _Cnt2TransportRemoteIp_Type(IpAddress):
    """Custom type cnt2TransportRemoteIp based on IpAddress"""
    defaultValue = 0


_Cnt2TransportRemoteIp_Object = MibTableColumn
cnt2TransportRemoteIp = _Cnt2TransportRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 12),
    _Cnt2TransportRemoteIp_Type()
)
cnt2TransportRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportRemoteIp.setStatus("current")


class _Cnt2TransportProtocol_Type(Integer32):
    """Custom type cnt2TransportProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sap", 1)
    )


_Cnt2TransportProtocol_Type.__name__ = "Integer32"
_Cnt2TransportProtocol_Object = MibTableColumn
cnt2TransportProtocol = _Cnt2TransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 13),
    _Cnt2TransportProtocol_Type()
)
cnt2TransportProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportProtocol.setStatus("current")


class _Cnt2TransportCompressionOption_Type(Integer32):
    """Custom type cnt2TransportCompressionOption based on Integer32"""
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


_Cnt2TransportCompressionOption_Type.__name__ = "Integer32"
_Cnt2TransportCompressionOption_Object = MibTableColumn
cnt2TransportCompressionOption = _Cnt2TransportCompressionOption_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 14),
    _Cnt2TransportCompressionOption_Type()
)
cnt2TransportCompressionOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportCompressionOption.setStatus("current")
_Cnt2TransportMaxXmitRate_Type = Integer32
_Cnt2TransportMaxXmitRate_Object = MibTableColumn
cnt2TransportMaxXmitRate = _Cnt2TransportMaxXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 15),
    _Cnt2TransportMaxXmitRate_Type()
)
cnt2TransportMaxXmitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportMaxXmitRate.setStatus("current")
_Cnt2TransportResetTime_Type = TimeTicks
_Cnt2TransportResetTime_Object = MibTableColumn
cnt2TransportResetTime = _Cnt2TransportResetTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 16),
    _Cnt2TransportResetTime_Type()
)
cnt2TransportResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportResetTime.setStatus("current")
_Cnt2TransportInPkts_Type = Counter32
_Cnt2TransportInPkts_Object = MibTableColumn
cnt2TransportInPkts = _Cnt2TransportInPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 17),
    _Cnt2TransportInPkts_Type()
)
cnt2TransportInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportInPkts.setStatus("current")
_Cnt2TransportInOctets_Type = Counter64
_Cnt2TransportInOctets_Object = MibTableColumn
cnt2TransportInOctets = _Cnt2TransportInOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 18),
    _Cnt2TransportInOctets_Type()
)
cnt2TransportInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportInOctets.setStatus("current")
_Cnt2TransportOutPkts_Type = Counter32
_Cnt2TransportOutPkts_Object = MibTableColumn
cnt2TransportOutPkts = _Cnt2TransportOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 19),
    _Cnt2TransportOutPkts_Type()
)
cnt2TransportOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportOutPkts.setStatus("current")
_Cnt2TransportOutOctets_Type = Counter64
_Cnt2TransportOutOctets_Object = MibTableColumn
cnt2TransportOutOctets = _Cnt2TransportOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 20),
    _Cnt2TransportOutOctets_Type()
)
cnt2TransportOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportOutOctets.setStatus("current")
_Cnt2TransportRexmit_Type = Counter32
_Cnt2TransportRexmit_Object = MibTableColumn
cnt2TransportRexmit = _Cnt2TransportRexmit_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 21),
    _Cnt2TransportRexmit_Type()
)
cnt2TransportRexmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportRexmit.setStatus("current")
_Cnt2TransportOosHigh_Type = Counter32
_Cnt2TransportOosHigh_Object = MibTableColumn
cnt2TransportOosHigh = _Cnt2TransportOosHigh_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 22),
    _Cnt2TransportOosHigh_Type()
)
cnt2TransportOosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportOosHigh.setStatus("current")


class _Cnt2TransportStatsReset_Type(Integer32):
    """Custom type cnt2TransportStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("all", 1)
    )


_Cnt2TransportStatsReset_Type.__name__ = "Integer32"
_Cnt2TransportStatsReset_Object = MibTableColumn
cnt2TransportStatsReset = _Cnt2TransportStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 23),
    _Cnt2TransportStatsReset_Type()
)
cnt2TransportStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2TransportStatsReset.setStatus("current")
_Cnt2TransportRawOutOctets_Type = Counter64
_Cnt2TransportRawOutOctets_Object = MibTableColumn
cnt2TransportRawOutOctets = _Cnt2TransportRawOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 24),
    _Cnt2TransportRawOutOctets_Type()
)
cnt2TransportRawOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportRawOutOctets.setStatus("current")
_Cnt2TransportRawInOctets_Type = Counter64
_Cnt2TransportRawInOctets_Object = MibTableColumn
cnt2TransportRawInOctets = _Cnt2TransportRawInOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 25),
    _Cnt2TransportRawInOctets_Type()
)
cnt2TransportRawInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportRawInOctets.setStatus("current")
_Cnt2TransportWindowSize_Type = Integer32
_Cnt2TransportWindowSize_Object = MibTableColumn
cnt2TransportWindowSize = _Cnt2TransportWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 26),
    _Cnt2TransportWindowSize_Type()
)
cnt2TransportWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportWindowSize.setStatus("current")
_Cnt2TransportSegmentSize_Type = Integer32
_Cnt2TransportSegmentSize_Object = MibTableColumn
cnt2TransportSegmentSize = _Cnt2TransportSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 27),
    _Cnt2TransportSegmentSize_Type()
)
cnt2TransportSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportSegmentSize.setStatus("current")
_Cnt2TransportSegmentSizeHi_Type = Integer32
_Cnt2TransportSegmentSizeHi_Object = MibTableColumn
cnt2TransportSegmentSizeHi = _Cnt2TransportSegmentSizeHi_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 28),
    _Cnt2TransportSegmentSizeHi_Type()
)
cnt2TransportSegmentSizeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportSegmentSizeHi.setStatus("current")
_Cnt2TransportRoundTripTimer_Type = Integer32
_Cnt2TransportRoundTripTimer_Object = MibTableColumn
cnt2TransportRoundTripTimer = _Cnt2TransportRoundTripTimer_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 29),
    _Cnt2TransportRoundTripTimer_Type()
)
cnt2TransportRoundTripTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportRoundTripTimer.setStatus("current")
_Cnt2TransportHoldCount_Type = Counter32
_Cnt2TransportHoldCount_Object = MibTableColumn
cnt2TransportHoldCount = _Cnt2TransportHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 30),
    _Cnt2TransportHoldCount_Type()
)
cnt2TransportHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportHoldCount.setStatus("current")
_Cnt2TransportHoldCountRatio1_Type = Counter32
_Cnt2TransportHoldCountRatio1_Object = MibTableColumn
cnt2TransportHoldCountRatio1 = _Cnt2TransportHoldCountRatio1_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 31),
    _Cnt2TransportHoldCountRatio1_Type()
)
cnt2TransportHoldCountRatio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportHoldCountRatio1.setStatus("current")
_Cnt2TransportHoldCountRatio2_Type = Counter32
_Cnt2TransportHoldCountRatio2_Object = MibTableColumn
cnt2TransportHoldCountRatio2 = _Cnt2TransportHoldCountRatio2_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 32),
    _Cnt2TransportHoldCountRatio2_Type()
)
cnt2TransportHoldCountRatio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportHoldCountRatio2.setStatus("current")
_Cnt2TransportHoldCountRatio3_Type = Counter32
_Cnt2TransportHoldCountRatio3_Object = MibTableColumn
cnt2TransportHoldCountRatio3 = _Cnt2TransportHoldCountRatio3_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 33),
    _Cnt2TransportHoldCountRatio3_Type()
)
cnt2TransportHoldCountRatio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportHoldCountRatio3.setStatus("current")
_Cnt2TransportTotalDisconnect_Type = Counter32
_Cnt2TransportTotalDisconnect_Object = MibTableColumn
cnt2TransportTotalDisconnect = _Cnt2TransportTotalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 34),
    _Cnt2TransportTotalDisconnect_Type()
)
cnt2TransportTotalDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2TransportTotalDisconnect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT246-MIB",
    **{"cnt2Transport": cnt2Transport,
       "cnt2TransportTable": cnt2TransportTable,
       "cnt2TransportEntry": cnt2TransportEntry,
       "cnt2TransportSlotIndex": cnt2TransportSlotIndex,
       "cnt2TransportIndex": cnt2TransportIndex,
       "cnt2TransportBus": cnt2TransportBus,
       "cnt2TransportVid": cnt2TransportVid,
       "cnt2TransportLinkType": cnt2TransportLinkType,
       "cnt2TransportLinkDesc": cnt2TransportLinkDesc,
       "cnt2TransportLinkStatus": cnt2TransportLinkStatus,
       "cnt2TransportIPtosPrecedence": cnt2TransportIPtosPrecedence,
       "cnt2TransportIPtosDelay": cnt2TransportIPtosDelay,
       "cnt2TransportIPtosThruput": cnt2TransportIPtosThruput,
       "cnt2TransportIPtosRelibility": cnt2TransportIPtosRelibility,
       "cnt2TransportRemoteIp": cnt2TransportRemoteIp,
       "cnt2TransportProtocol": cnt2TransportProtocol,
       "cnt2TransportCompressionOption": cnt2TransportCompressionOption,
       "cnt2TransportMaxXmitRate": cnt2TransportMaxXmitRate,
       "cnt2TransportResetTime": cnt2TransportResetTime,
       "cnt2TransportInPkts": cnt2TransportInPkts,
       "cnt2TransportInOctets": cnt2TransportInOctets,
       "cnt2TransportOutPkts": cnt2TransportOutPkts,
       "cnt2TransportOutOctets": cnt2TransportOutOctets,
       "cnt2TransportRexmit": cnt2TransportRexmit,
       "cnt2TransportOosHigh": cnt2TransportOosHigh,
       "cnt2TransportStatsReset": cnt2TransportStatsReset,
       "cnt2TransportRawOutOctets": cnt2TransportRawOutOctets,
       "cnt2TransportRawInOctets": cnt2TransportRawInOctets,
       "cnt2TransportWindowSize": cnt2TransportWindowSize,
       "cnt2TransportSegmentSize": cnt2TransportSegmentSize,
       "cnt2TransportSegmentSizeHi": cnt2TransportSegmentSizeHi,
       "cnt2TransportRoundTripTimer": cnt2TransportRoundTripTimer,
       "cnt2TransportHoldCount": cnt2TransportHoldCount,
       "cnt2TransportHoldCountRatio1": cnt2TransportHoldCountRatio1,
       "cnt2TransportHoldCountRatio2": cnt2TransportHoldCountRatio2,
       "cnt2TransportHoldCountRatio3": cnt2TransportHoldCountRatio3,
       "cnt2TransportTotalDisconnect": cnt2TransportTotalDisconnect}
)
