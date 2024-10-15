# SNMP MIB module (RFC1243-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1243-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:41 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DdpAddress(OctetString):
    """Custom type DdpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Appletalk_ObjectIdentity = ObjectIdentity
appletalk = _Appletalk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13)
)
_Llap_ObjectIdentity = ObjectIdentity
llap = _Llap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 1)
)
_LlapTable_Object = MibTable
llapTable = _LlapTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    llapTable.setStatus("mandatory")
_LlapEntry_Object = MibTableRow
llapEntry = _LlapEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1)
)
llapEntry.setIndexNames(
    (0, "RFC1243-MIB", "llapIfIndex"),
)
if mibBuilder.loadTexts:
    llapEntry.setStatus("mandatory")
_LlapIfIndex_Type = Integer32
_LlapIfIndex_Object = MibTableColumn
llapIfIndex = _LlapIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 1),
    _LlapIfIndex_Type()
)
llapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapIfIndex.setStatus("mandatory")
_LlapInPkts_Type = Counter32
_LlapInPkts_Object = MibTableColumn
llapInPkts = _LlapInPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 2),
    _LlapInPkts_Type()
)
llapInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInPkts.setStatus("mandatory")
_LlapOutPkts_Type = Counter32
_LlapOutPkts_Object = MibTableColumn
llapOutPkts = _LlapOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 3),
    _LlapOutPkts_Type()
)
llapOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapOutPkts.setStatus("mandatory")
_LlapInNoHandlers_Type = Counter32
_LlapInNoHandlers_Object = MibTableColumn
llapInNoHandlers = _LlapInNoHandlers_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 4),
    _LlapInNoHandlers_Type()
)
llapInNoHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInNoHandlers.setStatus("mandatory")
_LlapInLengthErrors_Type = Counter32
_LlapInLengthErrors_Object = MibTableColumn
llapInLengthErrors = _LlapInLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 5),
    _LlapInLengthErrors_Type()
)
llapInLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInLengthErrors.setStatus("mandatory")
_LlapInErrors_Type = Counter32
_LlapInErrors_Object = MibTableColumn
llapInErrors = _LlapInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 6),
    _LlapInErrors_Type()
)
llapInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInErrors.setStatus("mandatory")
_LlapCollisions_Type = Counter32
_LlapCollisions_Object = MibTableColumn
llapCollisions = _LlapCollisions_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 7),
    _LlapCollisions_Type()
)
llapCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapCollisions.setStatus("mandatory")
_LlapDefers_Type = Counter32
_LlapDefers_Object = MibTableColumn
llapDefers = _LlapDefers_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 8),
    _LlapDefers_Type()
)
llapDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapDefers.setStatus("mandatory")
_LlapNoDataErrors_Type = Counter32
_LlapNoDataErrors_Object = MibTableColumn
llapNoDataErrors = _LlapNoDataErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 9),
    _LlapNoDataErrors_Type()
)
llapNoDataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapNoDataErrors.setStatus("mandatory")
_LlapRandomCTSErrors_Type = Counter32
_LlapRandomCTSErrors_Object = MibTableColumn
llapRandomCTSErrors = _LlapRandomCTSErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 10),
    _LlapRandomCTSErrors_Type()
)
llapRandomCTSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapRandomCTSErrors.setStatus("mandatory")
_LlapFCSErrors_Type = Counter32
_LlapFCSErrors_Object = MibTableColumn
llapFCSErrors = _LlapFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 11),
    _LlapFCSErrors_Type()
)
llapFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapFCSErrors.setStatus("mandatory")
_Aarp_ObjectIdentity = ObjectIdentity
aarp = _Aarp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 2)
)
_AarpTable_Object = MibTable
aarpTable = _AarpTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    aarpTable.setStatus("mandatory")
_AarpEntry_Object = MibTableRow
aarpEntry = _AarpEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1)
)
aarpEntry.setIndexNames(
    (0, "RFC1243-MIB", "aarpIfIndex"),
    (0, "RFC1243-MIB", "aarpNetAddress"),
)
if mibBuilder.loadTexts:
    aarpEntry.setStatus("mandatory")
_AarpIfIndex_Type = Integer32
_AarpIfIndex_Object = MibTableColumn
aarpIfIndex = _AarpIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 1),
    _AarpIfIndex_Type()
)
aarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpIfIndex.setStatus("mandatory")
_AarpPhysAddress_Type = OctetString
_AarpPhysAddress_Object = MibTableColumn
aarpPhysAddress = _AarpPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 2),
    _AarpPhysAddress_Type()
)
aarpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpPhysAddress.setStatus("mandatory")
_AarpNetAddress_Type = DdpAddress
_AarpNetAddress_Object = MibTableColumn
aarpNetAddress = _AarpNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 3),
    _AarpNetAddress_Type()
)
aarpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpNetAddress.setStatus("mandatory")
_Atport_ObjectIdentity = ObjectIdentity
atport = _Atport_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 3)
)
_AtportTable_Object = MibTable
atportTable = _AtportTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    atportTable.setStatus("mandatory")
_AtportEntry_Object = MibTableRow
atportEntry = _AtportEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1)
)
atportEntry.setIndexNames(
    (0, "RFC1243-MIB", "atportIndex"),
)
if mibBuilder.loadTexts:
    atportEntry.setStatus("mandatory")
_AtportIndex_Type = Integer32
_AtportIndex_Object = MibTableColumn
atportIndex = _AtportIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 1),
    _AtportIndex_Type()
)
atportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportIndex.setStatus("mandatory")
_AtportDescr_Type = DisplayString
_AtportDescr_Object = MibTableColumn
atportDescr = _AtportDescr_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 2),
    _AtportDescr_Type()
)
atportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportDescr.setStatus("mandatory")


class _AtportType_Type(Integer32):
    """Custom type atportType based on Integer32"""
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
        *(("ethertalk1", 3),
          ("ethertalk2", 4),
          ("iptalk", 6),
          ("localtalk", 2),
          ("other", 1),
          ("serial-nonstandard", 8),
          ("serial-ppp", 7),
          ("tokentalk", 5),
          ("virtual", 9))
    )


_AtportType_Type.__name__ = "Integer32"
_AtportType_Object = MibTableColumn
atportType = _AtportType_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 3),
    _AtportType_Type()
)
atportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportType.setStatus("mandatory")


class _AtportNetStart_Type(OctetString):
    """Custom type atportNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtportNetStart_Type.__name__ = "OctetString"
_AtportNetStart_Object = MibTableColumn
atportNetStart = _AtportNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 4),
    _AtportNetStart_Type()
)
atportNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetStart.setStatus("mandatory")


class _AtportNetEnd_Type(OctetString):
    """Custom type atportNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtportNetEnd_Type.__name__ = "OctetString"
_AtportNetEnd_Object = MibTableColumn
atportNetEnd = _AtportNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 5),
    _AtportNetEnd_Type()
)
atportNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetEnd.setStatus("mandatory")
_AtportNetAddress_Type = DdpAddress
_AtportNetAddress_Object = MibTableColumn
atportNetAddress = _AtportNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 6),
    _AtportNetAddress_Type()
)
atportNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetAddress.setStatus("mandatory")


class _AtportStatus_Type(Integer32):
    """Custom type atportStatus based on Integer32"""
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
        *(("invalid", 4),
          ("off", 3),
          ("operational", 1),
          ("unconfigured", 2))
    )


_AtportStatus_Type.__name__ = "Integer32"
_AtportStatus_Object = MibTableColumn
atportStatus = _AtportStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 7),
    _AtportStatus_Type()
)
atportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportStatus.setStatus("mandatory")


class _AtportNetConfig_Type(Integer32):
    """Custom type atportNetConfig based on Integer32"""
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
        *(("configured", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("unconfigured", 4))
    )


_AtportNetConfig_Type.__name__ = "Integer32"
_AtportNetConfig_Object = MibTableColumn
atportNetConfig = _AtportNetConfig_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 8),
    _AtportNetConfig_Type()
)
atportNetConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportNetConfig.setStatus("mandatory")


class _AtportZoneConfig_Type(Integer32):
    """Custom type atportZoneConfig based on Integer32"""
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
        *(("configured", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("unconfigured", 4))
    )


_AtportZoneConfig_Type.__name__ = "Integer32"
_AtportZoneConfig_Object = MibTableColumn
atportZoneConfig = _AtportZoneConfig_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 9),
    _AtportZoneConfig_Type()
)
atportZoneConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportZoneConfig.setStatus("mandatory")
_AtportZone_Type = OctetString
_AtportZone_Object = MibTableColumn
atportZone = _AtportZone_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 10),
    _AtportZone_Type()
)
atportZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZone.setStatus("mandatory")
_AtportIfIndex_Type = Integer32
_AtportIfIndex_Object = MibTableColumn
atportIfIndex = _AtportIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 11),
    _AtportIfIndex_Type()
)
atportIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportIfIndex.setStatus("mandatory")
_Ddp_ObjectIdentity = ObjectIdentity
ddp = _Ddp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 4)
)
_DdpOutRequests_Type = Counter32
_DdpOutRequests_Object = MibScalar
ddpOutRequests = _DdpOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1),
    _DdpOutRequests_Type()
)
ddpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutRequests.setStatus("mandatory")
_DdpOutShorts_Type = Counter32
_DdpOutShorts_Object = MibScalar
ddpOutShorts = _DdpOutShorts_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 2),
    _DdpOutShorts_Type()
)
ddpOutShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutShorts.setStatus("mandatory")
_DdpOutLongs_Type = Counter32
_DdpOutLongs_Object = MibScalar
ddpOutLongs = _DdpOutLongs_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 3),
    _DdpOutLongs_Type()
)
ddpOutLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutLongs.setStatus("mandatory")
_DdpInReceives_Type = Counter32
_DdpInReceives_Object = MibScalar
ddpInReceives = _DdpInReceives_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 4),
    _DdpInReceives_Type()
)
ddpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpInReceives.setStatus("mandatory")
_DdpForwRequests_Type = Counter32
_DdpForwRequests_Object = MibScalar
ddpForwRequests = _DdpForwRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 5),
    _DdpForwRequests_Type()
)
ddpForwRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwRequests.setStatus("mandatory")
_DdpInLocalDatagrams_Type = Counter32
_DdpInLocalDatagrams_Object = MibScalar
ddpInLocalDatagrams = _DdpInLocalDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 6),
    _DdpInLocalDatagrams_Type()
)
ddpInLocalDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpInLocalDatagrams.setStatus("mandatory")
_DdpNoProtocolHandlers_Type = Counter32
_DdpNoProtocolHandlers_Object = MibScalar
ddpNoProtocolHandlers = _DdpNoProtocolHandlers_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 7),
    _DdpNoProtocolHandlers_Type()
)
ddpNoProtocolHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpNoProtocolHandlers.setStatus("mandatory")
_DdpOutNoRoutes_Type = Counter32
_DdpOutNoRoutes_Object = MibScalar
ddpOutNoRoutes = _DdpOutNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 8),
    _DdpOutNoRoutes_Type()
)
ddpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutNoRoutes.setStatus("mandatory")
_DdpTooShortErrors_Type = Counter32
_DdpTooShortErrors_Object = MibScalar
ddpTooShortErrors = _DdpTooShortErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 9),
    _DdpTooShortErrors_Type()
)
ddpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpTooShortErrors.setStatus("mandatory")
_DdpTooLongErrors_Type = Counter32
_DdpTooLongErrors_Object = MibScalar
ddpTooLongErrors = _DdpTooLongErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 10),
    _DdpTooLongErrors_Type()
)
ddpTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpTooLongErrors.setStatus("mandatory")
_DdpBroadcastErrors_Type = Counter32
_DdpBroadcastErrors_Object = MibScalar
ddpBroadcastErrors = _DdpBroadcastErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 11),
    _DdpBroadcastErrors_Type()
)
ddpBroadcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpBroadcastErrors.setStatus("mandatory")
_DdpShortDDPErrors_Type = Counter32
_DdpShortDDPErrors_Object = MibScalar
ddpShortDDPErrors = _DdpShortDDPErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 12),
    _DdpShortDDPErrors_Type()
)
ddpShortDDPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpShortDDPErrors.setStatus("mandatory")
_DdpHopCountErrors_Type = Counter32
_DdpHopCountErrors_Object = MibScalar
ddpHopCountErrors = _DdpHopCountErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 13),
    _DdpHopCountErrors_Type()
)
ddpHopCountErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpHopCountErrors.setStatus("mandatory")
_DdpChecksumErrors_Type = Counter32
_DdpChecksumErrors_Object = MibScalar
ddpChecksumErrors = _DdpChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 14),
    _DdpChecksumErrors_Type()
)
ddpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpChecksumErrors.setStatus("mandatory")
_Rtmp_ObjectIdentity = ObjectIdentity
rtmp = _Rtmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 5)
)
_RtmpTable_Object = MibTable
rtmpTable = _RtmpTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1)
)
if mibBuilder.loadTexts:
    rtmpTable.setStatus("mandatory")
_RtmpEntry_Object = MibTableRow
rtmpEntry = _RtmpEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1)
)
rtmpEntry.setIndexNames(
    (0, "RFC1243-MIB", "rtmpRangeStart"),
)
if mibBuilder.loadTexts:
    rtmpEntry.setStatus("mandatory")


class _RtmpRangeStart_Type(OctetString):
    """Custom type rtmpRangeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_RtmpRangeStart_Type.__name__ = "OctetString"
_RtmpRangeStart_Object = MibTableColumn
rtmpRangeStart = _RtmpRangeStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 1),
    _RtmpRangeStart_Type()
)
rtmpRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpRangeStart.setStatus("mandatory")


class _RtmpRangeEnd_Type(OctetString):
    """Custom type rtmpRangeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_RtmpRangeEnd_Type.__name__ = "OctetString"
_RtmpRangeEnd_Object = MibTableColumn
rtmpRangeEnd = _RtmpRangeEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 2),
    _RtmpRangeEnd_Type()
)
rtmpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpRangeEnd.setStatus("mandatory")
_RtmpNextHop_Type = OctetString
_RtmpNextHop_Object = MibTableColumn
rtmpNextHop = _RtmpNextHop_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 3),
    _RtmpNextHop_Type()
)
rtmpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpNextHop.setStatus("mandatory")


class _RtmpType_Type(Integer32):
    """Custom type rtmpType based on Integer32"""
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
        *(("appletalk", 2),
          ("other", 1),
          ("serial-nonstandard", 4),
          ("serial-ppp", 3))
    )


_RtmpType_Type.__name__ = "Integer32"
_RtmpType_Object = MibTableColumn
rtmpType = _RtmpType_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 4),
    _RtmpType_Type()
)
rtmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpType.setStatus("mandatory")
_RtmpPort_Type = Integer32
_RtmpPort_Object = MibTableColumn
rtmpPort = _RtmpPort_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 5),
    _RtmpPort_Type()
)
rtmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpPort.setStatus("mandatory")
_RtmpHops_Type = Integer32
_RtmpHops_Object = MibTableColumn
rtmpHops = _RtmpHops_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 6),
    _RtmpHops_Type()
)
rtmpHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpHops.setStatus("mandatory")


class _RtmpState_Type(Integer32):
    """Custom type rtmpState based on Integer32"""
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
        *(("bad", 4),
          ("goingBad", 3),
          ("good", 1),
          ("suspect", 2))
    )


_RtmpState_Type.__name__ = "Integer32"
_RtmpState_Object = MibTableColumn
rtmpState = _RtmpState_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 7),
    _RtmpState_Type()
)
rtmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpState.setStatus("mandatory")
_Kip_ObjectIdentity = ObjectIdentity
kip = _Kip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 6)
)
_KipTable_Object = MibTable
kipTable = _KipTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1)
)
if mibBuilder.loadTexts:
    kipTable.setStatus("mandatory")
_KipEntry_Object = MibTableRow
kipEntry = _KipEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1)
)
kipEntry.setIndexNames(
    (0, "RFC1243-MIB", "kipNetStart"),
)
if mibBuilder.loadTexts:
    kipEntry.setStatus("mandatory")


class _KipNetStart_Type(OctetString):
    """Custom type kipNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_KipNetStart_Type.__name__ = "OctetString"
_KipNetStart_Object = MibTableColumn
kipNetStart = _KipNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 1),
    _KipNetStart_Type()
)
kipNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNetStart.setStatus("mandatory")


class _KipNetEnd_Type(OctetString):
    """Custom type kipNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_KipNetEnd_Type.__name__ = "OctetString"
_KipNetEnd_Object = MibTableColumn
kipNetEnd = _KipNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 2),
    _KipNetEnd_Type()
)
kipNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNetEnd.setStatus("mandatory")
_KipNextHop_Type = IpAddress
_KipNextHop_Object = MibTableColumn
kipNextHop = _KipNextHop_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 3),
    _KipNextHop_Type()
)
kipNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNextHop.setStatus("mandatory")
_KipHopCount_Type = Integer32
_KipHopCount_Object = MibTableColumn
kipHopCount = _KipHopCount_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 4),
    _KipHopCount_Type()
)
kipHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipHopCount.setStatus("mandatory")
_KipBCastAddr_Type = IpAddress
_KipBCastAddr_Object = MibTableColumn
kipBCastAddr = _KipBCastAddr_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 5),
    _KipBCastAddr_Type()
)
kipBCastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipBCastAddr.setStatus("mandatory")


class _KipCore_Type(Integer32):
    """Custom type kipCore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("core", 1),
          ("notcore", 2))
    )


_KipCore_Type.__name__ = "Integer32"
_KipCore_Object = MibTableColumn
kipCore = _KipCore_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 6),
    _KipCore_Type()
)
kipCore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipCore.setStatus("mandatory")


class _KipType_Type(Integer32):
    """Custom type kipType based on Integer32"""
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
        *(("host", 3),
          ("kipRouter", 1),
          ("net", 2),
          ("other", 4))
    )


_KipType_Type.__name__ = "Integer32"
_KipType_Object = MibTableColumn
kipType = _KipType_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 7),
    _KipType_Type()
)
kipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipType.setStatus("mandatory")


class _KipState_Type(Integer32):
    """Custom type kipState based on Integer32"""
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
          ("invalid", 3),
          ("learned", 2))
    )


_KipState_Type.__name__ = "Integer32"
_KipState_Object = MibTableColumn
kipState = _KipState_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 8),
    _KipState_Type()
)
kipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipState.setStatus("mandatory")


class _KipShare_Type(Integer32):
    """Custom type kipShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("shared", 1))
    )


_KipShare_Type.__name__ = "Integer32"
_KipShare_Object = MibTableColumn
kipShare = _KipShare_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 9),
    _KipShare_Type()
)
kipShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipShare.setStatus("mandatory")
_Zip_ObjectIdentity = ObjectIdentity
zip = _Zip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 7)
)
_ZipTable_Object = MibTable
zipTable = _ZipTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1)
)
if mibBuilder.loadTexts:
    zipTable.setStatus("mandatory")
_ZipEntry_Object = MibTableRow
zipEntry = _ZipEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1)
)
zipEntry.setIndexNames(
    (0, "RFC1243-MIB", "zipZoneNetStart"),
    (0, "RFC1243-MIB", "zipZoneIndex"),
)
if mibBuilder.loadTexts:
    zipEntry.setStatus("mandatory")
_ZipZoneName_Type = OctetString
_ZipZoneName_Object = MibTableColumn
zipZoneName = _ZipZoneName_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 1),
    _ZipZoneName_Type()
)
zipZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneName.setStatus("mandatory")
_ZipZoneIndex_Type = Integer32
_ZipZoneIndex_Object = MibTableColumn
zipZoneIndex = _ZipZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 2),
    _ZipZoneIndex_Type()
)
zipZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneIndex.setStatus("mandatory")


class _ZipZoneNetStart_Type(OctetString):
    """Custom type zipZoneNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ZipZoneNetStart_Type.__name__ = "OctetString"
_ZipZoneNetStart_Object = MibTableColumn
zipZoneNetStart = _ZipZoneNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 3),
    _ZipZoneNetStart_Type()
)
zipZoneNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneNetStart.setStatus("mandatory")


class _ZipZoneNetEnd_Type(OctetString):
    """Custom type zipZoneNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ZipZoneNetEnd_Type.__name__ = "OctetString"
_ZipZoneNetEnd_Object = MibTableColumn
zipZoneNetEnd = _ZipZoneNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 4),
    _ZipZoneNetEnd_Type()
)
zipZoneNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneNetEnd.setStatus("mandatory")


class _ZipZoneState_Type(Integer32):
    """Custom type zipZoneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ZipZoneState_Type.__name__ = "Integer32"
_ZipZoneState_Object = MibTableColumn
zipZoneState = _ZipZoneState_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 5),
    _ZipZoneState_Type()
)
zipZoneState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneState.setStatus("mandatory")
_Nbp_ObjectIdentity = ObjectIdentity
nbp = _Nbp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 8)
)
_NbpTable_Object = MibTable
nbpTable = _NbpTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1)
)
if mibBuilder.loadTexts:
    nbpTable.setStatus("mandatory")
_NbpEntry_Object = MibTableRow
nbpEntry = _NbpEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1)
)
nbpEntry.setIndexNames(
    (0, "RFC1243-MIB", "nbpIndex"),
)
if mibBuilder.loadTexts:
    nbpEntry.setStatus("mandatory")
_NbpIndex_Type = Integer32
_NbpIndex_Object = MibTableColumn
nbpIndex = _NbpIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 1),
    _NbpIndex_Type()
)
nbpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpIndex.setStatus("mandatory")
_NbpObject_Type = OctetString
_NbpObject_Object = MibTableColumn
nbpObject = _NbpObject_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 2),
    _NbpObject_Type()
)
nbpObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpObject.setStatus("mandatory")
_NbpType_Type = OctetString
_NbpType_Object = MibTableColumn
nbpType = _NbpType_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 3),
    _NbpType_Type()
)
nbpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpType.setStatus("mandatory")
_NbpZone_Type = OctetString
_NbpZone_Object = MibTableColumn
nbpZone = _NbpZone_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 4),
    _NbpZone_Type()
)
nbpZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpZone.setStatus("mandatory")


class _NbpState_Type(Integer32):
    """Custom type nbpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbpState_Type.__name__ = "Integer32"
_NbpState_Object = MibTableColumn
nbpState = _NbpState_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 5),
    _NbpState_Type()
)
nbpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpState.setStatus("mandatory")
_Atecho_ObjectIdentity = ObjectIdentity
atecho = _Atecho_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 9)
)
_AtechoRequests_Type = Counter32
_AtechoRequests_Object = MibScalar
atechoRequests = _AtechoRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1),
    _AtechoRequests_Type()
)
atechoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atechoRequests.setStatus("mandatory")
_AtechoReplies_Type = Counter32
_AtechoReplies_Object = MibScalar
atechoReplies = _AtechoReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 2),
    _AtechoReplies_Type()
)
atechoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atechoReplies.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1243-MIB",
    **{"DdpAddress": DdpAddress,
       "appletalk": appletalk,
       "llap": llap,
       "llapTable": llapTable,
       "llapEntry": llapEntry,
       "llapIfIndex": llapIfIndex,
       "llapInPkts": llapInPkts,
       "llapOutPkts": llapOutPkts,
       "llapInNoHandlers": llapInNoHandlers,
       "llapInLengthErrors": llapInLengthErrors,
       "llapInErrors": llapInErrors,
       "llapCollisions": llapCollisions,
       "llapDefers": llapDefers,
       "llapNoDataErrors": llapNoDataErrors,
       "llapRandomCTSErrors": llapRandomCTSErrors,
       "llapFCSErrors": llapFCSErrors,
       "aarp": aarp,
       "aarpTable": aarpTable,
       "aarpEntry": aarpEntry,
       "aarpIfIndex": aarpIfIndex,
       "aarpPhysAddress": aarpPhysAddress,
       "aarpNetAddress": aarpNetAddress,
       "atport": atport,
       "atportTable": atportTable,
       "atportEntry": atportEntry,
       "atportIndex": atportIndex,
       "atportDescr": atportDescr,
       "atportType": atportType,
       "atportNetStart": atportNetStart,
       "atportNetEnd": atportNetEnd,
       "atportNetAddress": atportNetAddress,
       "atportStatus": atportStatus,
       "atportNetConfig": atportNetConfig,
       "atportZoneConfig": atportZoneConfig,
       "atportZone": atportZone,
       "atportIfIndex": atportIfIndex,
       "ddp": ddp,
       "ddpOutRequests": ddpOutRequests,
       "ddpOutShorts": ddpOutShorts,
       "ddpOutLongs": ddpOutLongs,
       "ddpInReceives": ddpInReceives,
       "ddpForwRequests": ddpForwRequests,
       "ddpInLocalDatagrams": ddpInLocalDatagrams,
       "ddpNoProtocolHandlers": ddpNoProtocolHandlers,
       "ddpOutNoRoutes": ddpOutNoRoutes,
       "ddpTooShortErrors": ddpTooShortErrors,
       "ddpTooLongErrors": ddpTooLongErrors,
       "ddpBroadcastErrors": ddpBroadcastErrors,
       "ddpShortDDPErrors": ddpShortDDPErrors,
       "ddpHopCountErrors": ddpHopCountErrors,
       "ddpChecksumErrors": ddpChecksumErrors,
       "rtmp": rtmp,
       "rtmpTable": rtmpTable,
       "rtmpEntry": rtmpEntry,
       "rtmpRangeStart": rtmpRangeStart,
       "rtmpRangeEnd": rtmpRangeEnd,
       "rtmpNextHop": rtmpNextHop,
       "rtmpType": rtmpType,
       "rtmpPort": rtmpPort,
       "rtmpHops": rtmpHops,
       "rtmpState": rtmpState,
       "kip": kip,
       "kipTable": kipTable,
       "kipEntry": kipEntry,
       "kipNetStart": kipNetStart,
       "kipNetEnd": kipNetEnd,
       "kipNextHop": kipNextHop,
       "kipHopCount": kipHopCount,
       "kipBCastAddr": kipBCastAddr,
       "kipCore": kipCore,
       "kipType": kipType,
       "kipState": kipState,
       "kipShare": kipShare,
       "zip": zip,
       "zipTable": zipTable,
       "zipEntry": zipEntry,
       "zipZoneName": zipZoneName,
       "zipZoneIndex": zipZoneIndex,
       "zipZoneNetStart": zipZoneNetStart,
       "zipZoneNetEnd": zipZoneNetEnd,
       "zipZoneState": zipZoneState,
       "nbp": nbp,
       "nbpTable": nbpTable,
       "nbpEntry": nbpEntry,
       "nbpIndex": nbpIndex,
       "nbpObject": nbpObject,
       "nbpType": nbpType,
       "nbpZone": nbpZone,
       "nbpState": nbpState,
       "atecho": atecho,
       "atechoRequests": atechoRequests,
       "atechoReplies": atechoReplies}
)
