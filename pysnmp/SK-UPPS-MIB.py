# SNMP MIB module (SK-UPPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SK-UPPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:37 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

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


# Types definitions



class FddiMACLongAddressType(OctetString):
    """Custom type FddiMACLongAddressType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sk_ObjectIdentity = ObjectIdentity
sk = _Sk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179)
)
_SkMibs_ObjectIdentity = ObjectIdentity
skMibs = _SkMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2)
)
_Sk_board_ObjectIdentity = ObjectIdentity
sk_board = _Sk_board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2)
)
_Sk_board_status_ObjectIdentity = ObjectIdentity
sk_board_status = _Sk_board_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1)
)
_StTable_Object = MibTable
stTable = _StTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    stTable.setStatus("mandatory")
_StEntry_Object = MibTableRow
stEntry = _StEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1)
)
stEntry.setIndexNames(
    (0, "SK-UPPS-MIB", "stIfIndex"),
)
if mibBuilder.loadTexts:
    stEntry.setStatus("mandatory")
_StIfIndex_Type = Integer32
_StIfIndex_Object = MibTableColumn
stIfIndex = _StIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 1),
    _StIfIndex_Type()
)
stIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stIfIndex.setStatus("mandatory")


class _StVersion_Type(DisplayString):
    """Custom type stVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StVersion_Type.__name__ = "DisplayString"
_StVersion_Object = MibTableColumn
stVersion = _StVersion_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 2),
    _StVersion_Type()
)
stVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stVersion.setStatus("mandatory")
_StLogAddress_Type = OctetString
_StLogAddress_Object = MibTableColumn
stLogAddress = _StLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 3),
    _StLogAddress_Type()
)
stLogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stLogAddress.setStatus("mandatory")
_StInterrupt_Type = Integer32
_StInterrupt_Object = MibTableColumn
stInterrupt = _StInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 4),
    _StInterrupt_Type()
)
stInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stInterrupt.setStatus("mandatory")


class _StBaseAddress_Type(DisplayString):
    """Custom type stBaseAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StBaseAddress_Type.__name__ = "DisplayString"
_StBaseAddress_Object = MibTableColumn
stBaseAddress = _StBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 5),
    _StBaseAddress_Type()
)
stBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stBaseAddress.setStatus("mandatory")


class _StRAMSize_Type(DisplayString):
    """Custom type stRAMSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StRAMSize_Type.__name__ = "DisplayString"
_StRAMSize_Object = MibTableColumn
stRAMSize = _StRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 6),
    _StRAMSize_Type()
)
stRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRAMSize.setStatus("mandatory")


class _StIOPort_Type(DisplayString):
    """Custom type stIOPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StIOPort_Type.__name__ = "DisplayString"
_StIOPort_Object = MibTableColumn
stIOPort = _StIOPort_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 7),
    _StIOPort_Type()
)
stIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stIOPort.setStatus("mandatory")
_StDMALine_Type = Integer32
_StDMALine_Object = MibTableColumn
stDMALine = _StDMALine_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 8),
    _StDMALine_Type()
)
stDMALine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stDMALine.setStatus("mandatory")
_StNumMbufs_Type = Integer32
_StNumMbufs_Object = MibTableColumn
stNumMbufs = _StNumMbufs_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 9),
    _StNumMbufs_Type()
)
stNumMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stNumMbufs.setStatus("mandatory")
_StMaxTxMbufs_Type = Integer32
_StMaxTxMbufs_Object = MibTableColumn
stMaxTxMbufs = _StMaxTxMbufs_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 10),
    _StMaxTxMbufs_Type()
)
stMaxTxMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMaxTxMbufs.setStatus("mandatory")
_StMaxRxMbufs_Type = Integer32
_StMaxRxMbufs_Object = MibTableColumn
stMaxRxMbufs = _StMaxRxMbufs_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 11),
    _StMaxRxMbufs_Type()
)
stMaxRxMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMaxRxMbufs.setStatus("mandatory")
_StCurrentPacketFilter_Type = Integer32
_StCurrentPacketFilter_Object = MibTableColumn
stCurrentPacketFilter = _StCurrentPacketFilter_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 12),
    _StCurrentPacketFilter_Type()
)
stCurrentPacketFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCurrentPacketFilter.setStatus("mandatory")


class _StServiceInterrupt_Type(DisplayString):
    """Custom type stServiceInterrupt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StServiceInterrupt_Type.__name__ = "DisplayString"
_StServiceInterrupt_Object = MibTableColumn
stServiceInterrupt = _StServiceInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 13),
    _StServiceInterrupt_Type()
)
stServiceInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stServiceInterrupt.setStatus("mandatory")


class _StOEMSignature_Type(DisplayString):
    """Custom type stOEMSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StOEMSignature_Type.__name__ = "DisplayString"
_StOEMSignature_Object = MibTableColumn
stOEMSignature = _StOEMSignature_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 14),
    _StOEMSignature_Type()
)
stOEMSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stOEMSignature.setStatus("mandatory")


class _StTopology_Type(Integer32):
    """Custom type stTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 2),
          ("token-ring", 3))
    )


_StTopology_Type.__name__ = "Integer32"
_StTopology_Object = MibTableColumn
stTopology = _StTopology_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 15),
    _StTopology_Type()
)
stTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTopology.setStatus("mandatory")
_StIORange_Type = Integer32
_StIORange_Object = MibTableColumn
stIORange = _StIORange_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 1, 1, 1, 16),
    _StIORange_Type()
)
stIORange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stIORange.setStatus("mandatory")
_Sk_board_client_ObjectIdentity = ObjectIdentity
sk_board_client = _Sk_board_client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2)
)
_ClTable_Object = MibTable
clTable = _ClTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    clTable.setStatus("mandatory")
_ClEntry_Object = MibTableRow
clEntry = _ClEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1)
)
clEntry.setIndexNames(
    (0, "SK-UPPS-MIB", "clPID"),
)
if mibBuilder.loadTexts:
    clEntry.setStatus("mandatory")
_ClIfIndex_Type = Integer32
_ClIfIndex_Object = MibTableColumn
clIfIndex = _ClIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1, 1),
    _ClIfIndex_Type()
)
clIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIfIndex.setStatus("mandatory")


class _ClType_Type(DisplayString):
    """Custom type clType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClType_Type.__name__ = "DisplayString"
_ClType_Object = MibTableColumn
clType = _ClType_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1, 2),
    _ClType_Type()
)
clType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clType.setStatus("mandatory")
_ClMulticast_Type = Integer32
_ClMulticast_Object = MibTableColumn
clMulticast = _ClMulticast_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1, 3),
    _ClMulticast_Type()
)
clMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMulticast.setStatus("mandatory")


class _ClName_Type(DisplayString):
    """Custom type clName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClName_Type.__name__ = "DisplayString"
_ClName_Object = MibTableColumn
clName = _ClName_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1, 4),
    _ClName_Type()
)
clName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clName.setStatus("mandatory")
_ClMode_Type = Integer32
_ClMode_Object = MibTableColumn
clMode = _ClMode_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1, 5),
    _ClMode_Type()
)
clMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMode.setStatus("mandatory")
_ClPID_Type = Integer32
_ClPID_Object = MibTableColumn
clPID = _ClPID_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 2, 1, 1, 6),
    _ClPID_Type()
)
clPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPID.setStatus("mandatory")
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3)
)
_EthStatsTable_Object = MibTable
ethStatsTable = _EthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ethStatsTable.setStatus("mandatory")
_EthStatsEntry_Object = MibTableRow
ethStatsEntry = _EthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1)
)
ethStatsEntry.setIndexNames(
    (0, "SK-UPPS-MIB", "ethStatsIndex"),
)
if mibBuilder.loadTexts:
    ethStatsEntry.setStatus("mandatory")
_EthStatsIndex_Type = Integer32
_EthStatsIndex_Object = MibTableColumn
ethStatsIndex = _EthStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 1),
    _EthStatsIndex_Type()
)
ethStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsIndex.setStatus("mandatory")
_EthStatsAlignmentErrors_Type = Counter32
_EthStatsAlignmentErrors_Object = MibTableColumn
ethStatsAlignmentErrors = _EthStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 2),
    _EthStatsAlignmentErrors_Type()
)
ethStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsAlignmentErrors.setStatus("mandatory")
_EthStatsFCSErrors_Type = Counter32
_EthStatsFCSErrors_Object = MibTableColumn
ethStatsFCSErrors = _EthStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 3),
    _EthStatsFCSErrors_Type()
)
ethStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsFCSErrors.setStatus("mandatory")
_EthStatsSingleCollisionFrames_Type = Counter32
_EthStatsSingleCollisionFrames_Object = MibTableColumn
ethStatsSingleCollisionFrames = _EthStatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 4),
    _EthStatsSingleCollisionFrames_Type()
)
ethStatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsSingleCollisionFrames.setStatus("mandatory")
_EthStatsMultipleCollisionFrames_Type = Counter32
_EthStatsMultipleCollisionFrames_Object = MibTableColumn
ethStatsMultipleCollisionFrames = _EthStatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 5),
    _EthStatsMultipleCollisionFrames_Type()
)
ethStatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsMultipleCollisionFrames.setStatus("mandatory")
_EthStatsSQETestErrors_Type = Counter32
_EthStatsSQETestErrors_Object = MibTableColumn
ethStatsSQETestErrors = _EthStatsSQETestErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 6),
    _EthStatsSQETestErrors_Type()
)
ethStatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsSQETestErrors.setStatus("mandatory")
_EthStatsDeferredTransmissions_Type = Counter32
_EthStatsDeferredTransmissions_Object = MibTableColumn
ethStatsDeferredTransmissions = _EthStatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 7),
    _EthStatsDeferredTransmissions_Type()
)
ethStatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsDeferredTransmissions.setStatus("mandatory")
_EthStatsLateCollisions_Type = Counter32
_EthStatsLateCollisions_Object = MibTableColumn
ethStatsLateCollisions = _EthStatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 8),
    _EthStatsLateCollisions_Type()
)
ethStatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsLateCollisions.setStatus("mandatory")
_EthStatsExcessiveCollisions_Type = Counter32
_EthStatsExcessiveCollisions_Object = MibTableColumn
ethStatsExcessiveCollisions = _EthStatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 9),
    _EthStatsExcessiveCollisions_Type()
)
ethStatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsExcessiveCollisions.setStatus("mandatory")
_EthStatsInternalMacTransErrors_Type = Counter32
_EthStatsInternalMacTransErrors_Object = MibTableColumn
ethStatsInternalMacTransErrors = _EthStatsInternalMacTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 10),
    _EthStatsInternalMacTransErrors_Type()
)
ethStatsInternalMacTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsInternalMacTransErrors.setStatus("mandatory")
_EthStatsCarrierSenseErrors_Type = Counter32
_EthStatsCarrierSenseErrors_Object = MibTableColumn
ethStatsCarrierSenseErrors = _EthStatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 11),
    _EthStatsCarrierSenseErrors_Type()
)
ethStatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsCarrierSenseErrors.setStatus("mandatory")
_EthStatsExcessiveDeferrals_Type = Counter32
_EthStatsExcessiveDeferrals_Object = MibTableColumn
ethStatsExcessiveDeferrals = _EthStatsExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 12),
    _EthStatsExcessiveDeferrals_Type()
)
ethStatsExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsExcessiveDeferrals.setStatus("mandatory")
_EthStatsFrameTooLongs_Type = Counter32
_EthStatsFrameTooLongs_Object = MibTableColumn
ethStatsFrameTooLongs = _EthStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 13),
    _EthStatsFrameTooLongs_Type()
)
ethStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsFrameTooLongs.setStatus("mandatory")
_EthStatsInRangeLengthErrors_Type = Counter32
_EthStatsInRangeLengthErrors_Object = MibTableColumn
ethStatsInRangeLengthErrors = _EthStatsInRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 14),
    _EthStatsInRangeLengthErrors_Type()
)
ethStatsInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsInRangeLengthErrors.setStatus("mandatory")
_EthStatsOutOfRangeLengthFields_Type = Counter32
_EthStatsOutOfRangeLengthFields_Object = MibTableColumn
ethStatsOutOfRangeLengthFields = _EthStatsOutOfRangeLengthFields_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 15),
    _EthStatsOutOfRangeLengthFields_Type()
)
ethStatsOutOfRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsOutOfRangeLengthFields.setStatus("mandatory")
_EthStatsInternalMacRecvErrors_Type = Counter32
_EthStatsInternalMacRecvErrors_Object = MibTableColumn
ethStatsInternalMacRecvErrors = _EthStatsInternalMacRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 3, 1, 1, 16),
    _EthStatsInternalMacRecvErrors_Type()
)
ethStatsInternalMacRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsInternalMacRecvErrors.setStatus("mandatory")
_Tok_ObjectIdentity = ObjectIdentity
tok = _Tok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4)
)
_TokStatsTable_Object = MibTable
tokStatsTable = _TokStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tokStatsTable.setStatus("mandatory")
_TokStatsEntry_Object = MibTableRow
tokStatsEntry = _TokStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1)
)
tokStatsEntry.setIndexNames(
    (0, "SK-UPPS-MIB", "tokStatsIndex"),
)
if mibBuilder.loadTexts:
    tokStatsEntry.setStatus("mandatory")
_TokStatsIndex_Type = Integer32
_TokStatsIndex_Object = MibTableColumn
tokStatsIndex = _TokStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 1),
    _TokStatsIndex_Type()
)
tokStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsIndex.setStatus("mandatory")
_TokStatsUpstreamNbr_Type = OctetString
_TokStatsUpstreamNbr_Object = MibTableColumn
tokStatsUpstreamNbr = _TokStatsUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 2),
    _TokStatsUpstreamNbr_Type()
)
tokStatsUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsUpstreamNbr.setStatus("mandatory")
_TokStatsLocalRingNumber_Type = Integer32
_TokStatsLocalRingNumber_Object = MibTableColumn
tokStatsLocalRingNumber = _TokStatsLocalRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 3),
    _TokStatsLocalRingNumber_Type()
)
tokStatsLocalRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsLocalRingNumber.setStatus("mandatory")
_TokStatsRingUpCounts_Type = Counter32
_TokStatsRingUpCounts_Object = MibTableColumn
tokStatsRingUpCounts = _TokStatsRingUpCounts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 4),
    _TokStatsRingUpCounts_Type()
)
tokStatsRingUpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsRingUpCounts.setStatus("mandatory")
_TokStatsSignalLossErrors_Type = Counter32
_TokStatsSignalLossErrors_Object = MibTableColumn
tokStatsSignalLossErrors = _TokStatsSignalLossErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 5),
    _TokStatsSignalLossErrors_Type()
)
tokStatsSignalLossErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsSignalLossErrors.setStatus("mandatory")
_TokStatsLobeWireFaults_Type = Counter32
_TokStatsLobeWireFaults_Object = MibTableColumn
tokStatsLobeWireFaults = _TokStatsLobeWireFaults_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 6),
    _TokStatsLobeWireFaults_Type()
)
tokStatsLobeWireFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsLobeWireFaults.setStatus("mandatory")
_TokStatsRingRecoveryCounts_Type = Counter32
_TokStatsRingRecoveryCounts_Object = MibTableColumn
tokStatsRingRecoveryCounts = _TokStatsRingRecoveryCounts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 7),
    _TokStatsRingRecoveryCounts_Type()
)
tokStatsRingRecoveryCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsRingRecoveryCounts.setStatus("mandatory")
_TokStatsLineErrors_Type = Counter32
_TokStatsLineErrors_Object = MibTableColumn
tokStatsLineErrors = _TokStatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 8),
    _TokStatsLineErrors_Type()
)
tokStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsLineErrors.setStatus("mandatory")
_TokStatsBurstErrors_Type = Counter32
_TokStatsBurstErrors_Object = MibTableColumn
tokStatsBurstErrors = _TokStatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 9),
    _TokStatsBurstErrors_Type()
)
tokStatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsBurstErrors.setStatus("mandatory")
_TokStatsARI_FCIErrors_Type = Counter32
_TokStatsARI_FCIErrors_Object = MibScalar
tokStatsARI_FCIErrors = _TokStatsARI_FCIErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 10),
    _TokStatsARI_FCIErrors_Type()
)
tokStatsARI_FCIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsARI_FCIErrors.setStatus("mandatory")
_TokStatsLostFrameErrors_Type = Counter32
_TokStatsLostFrameErrors_Object = MibTableColumn
tokStatsLostFrameErrors = _TokStatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 11),
    _TokStatsLostFrameErrors_Type()
)
tokStatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsLostFrameErrors.setStatus("mandatory")
_TokStatsReceiveCongestionErrors_Type = Counter32
_TokStatsReceiveCongestionErrors_Object = MibTableColumn
tokStatsReceiveCongestionErrors = _TokStatsReceiveCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 12),
    _TokStatsReceiveCongestionErrors_Type()
)
tokStatsReceiveCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsReceiveCongestionErrors.setStatus("mandatory")
_TokStatsFrameCopiedErrors_Type = Counter32
_TokStatsFrameCopiedErrors_Object = MibTableColumn
tokStatsFrameCopiedErrors = _TokStatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 13),
    _TokStatsFrameCopiedErrors_Type()
)
tokStatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsFrameCopiedErrors.setStatus("mandatory")
_TokStatsTokenErrors_Type = Counter32
_TokStatsTokenErrors_Object = MibTableColumn
tokStatsTokenErrors = _TokStatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 14),
    _TokStatsTokenErrors_Type()
)
tokStatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsTokenErrors.setStatus("mandatory")
_TokStatsDMABusErrors_Type = Counter32
_TokStatsDMABusErrors_Object = MibTableColumn
tokStatsDMABusErrors = _TokStatsDMABusErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 15),
    _TokStatsDMABusErrors_Type()
)
tokStatsDMABusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsDMABusErrors.setStatus("mandatory")
_TokStatsDMAParityErrors_Type = Counter32
_TokStatsDMAParityErrors_Object = MibTableColumn
tokStatsDMAParityErrors = _TokStatsDMAParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 16),
    _TokStatsDMAParityErrors_Type()
)
tokStatsDMAParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsDMAParityErrors.setStatus("mandatory")
_TokStatsReceiveOverflowErrors_Type = Counter32
_TokStatsReceiveOverflowErrors_Object = MibTableColumn
tokStatsReceiveOverflowErrors = _TokStatsReceiveOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 4, 1, 1, 17),
    _TokStatsReceiveOverflowErrors_Type()
)
tokStatsReceiveOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokStatsReceiveOverflowErrors.setStatus("mandatory")
_Fddi_ObjectIdentity = ObjectIdentity
fddi = _Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5)
)
_FddiStatsTable_Object = MibTable
fddiStatsTable = _FddiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fddiStatsTable.setStatus("mandatory")
_FddiStatsEntry_Object = MibTableRow
fddiStatsEntry = _FddiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1)
)
fddiStatsEntry.setIndexNames(
    (0, "SK-UPPS-MIB", "fddiStatsIndex"),
)
if mibBuilder.loadTexts:
    fddiStatsEntry.setStatus("mandatory")
_FddiStatsIndex_Type = Integer32
_FddiStatsIndex_Object = MibTableColumn
fddiStatsIndex = _FddiStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 1),
    _FddiStatsIndex_Type()
)
fddiStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsIndex.setStatus("mandatory")


class _FddiSMTOpVersionId_Type(Integer32):
    """Custom type fddiSMTOpVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddiSMTOpVersionId_Type.__name__ = "Integer32"
_FddiSMTOpVersionId_Object = MibTableColumn
fddiSMTOpVersionId = _FddiSMTOpVersionId_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 2),
    _FddiSMTOpVersionId_Type()
)
fddiSMTOpVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiSMTOpVersionId.setStatus("mandatory")


class _FddiSMTCFState_Type(Integer32):
    """Custom type fddiSMTCFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_FddiSMTCFState_Type.__name__ = "Integer32"
_FddiSMTCFState_Object = MibTableColumn
fddiSMTCFState = _FddiSMTCFState_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 3),
    _FddiSMTCFState_Type()
)
fddiSMTCFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiSMTCFState.setStatus("mandatory")
_FddiSMTFrameSends_Type = Counter32
_FddiSMTFrameSends_Object = MibTableColumn
fddiSMTFrameSends = _FddiSMTFrameSends_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 4),
    _FddiSMTFrameSends_Type()
)
fddiSMTFrameSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiSMTFrameSends.setStatus("mandatory")
_FddiSMTFrameReceives_Type = Counter32
_FddiSMTFrameReceives_Object = MibTableColumn
fddiSMTFrameReceives = _FddiSMTFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 5),
    _FddiSMTFrameReceives_Type()
)
fddiSMTFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiSMTFrameReceives.setStatus("mandatory")
_FddiSMTRingUps_Type = Counter32
_FddiSMTRingUps_Object = MibTableColumn
fddiSMTRingUps = _FddiSMTRingUps_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 6),
    _FddiSMTRingUps_Type()
)
fddiSMTRingUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiSMTRingUps.setStatus("mandatory")
_FddiMACUpstreamNbr_Type = FddiMACLongAddressType
_FddiMACUpstreamNbr_Object = MibTableColumn
fddiMACUpstreamNbr = _FddiMACUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 7),
    _FddiMACUpstreamNbr_Type()
)
fddiMACUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiMACUpstreamNbr.setStatus("mandatory")
_FddiMACDownstreamNbr_Type = FddiMACLongAddressType
_FddiMACDownstreamNbr_Object = MibTableColumn
fddiMACDownstreamNbr = _FddiMACDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 8),
    _FddiMACDownstreamNbr_Type()
)
fddiMACDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiMACDownstreamNbr.setStatus("mandatory")
_FddiMACFrameCts_Type = Counter32
_FddiMACFrameCts_Object = MibTableColumn
fddiMACFrameCts = _FddiMACFrameCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 9),
    _FddiMACFrameCts_Type()
)
fddiMACFrameCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiMACFrameCts.setStatus("mandatory")
_FddiMACErrorCts_Type = Counter32
_FddiMACErrorCts_Object = MibTableColumn
fddiMACErrorCts = _FddiMACErrorCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 10),
    _FddiMACErrorCts_Type()
)
fddiMACErrorCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiMACErrorCts.setStatus("mandatory")
_FddiMACLostCts_Type = Counter32
_FddiMACLostCts_Object = MibTableColumn
fddiMACLostCts = _FddiMACLostCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 11),
    _FddiMACLostCts_Type()
)
fddiMACLostCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiMACLostCts.setStatus("mandatory")


class _FddiPORT1LerEstimate_Type(Integer32):
    """Custom type fddiPORT1LerEstimate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_FddiPORT1LerEstimate_Type.__name__ = "Integer32"
_FddiPORT1LerEstimate_Object = MibTableColumn
fddiPORT1LerEstimate = _FddiPORT1LerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 12),
    _FddiPORT1LerEstimate_Type()
)
fddiPORT1LerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPORT1LerEstimate.setStatus("mandatory")


class _FddiPORT2LerEstimate_Type(Integer32):
    """Custom type fddiPORT2LerEstimate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_FddiPORT2LerEstimate_Type.__name__ = "Integer32"
_FddiPORT2LerEstimate_Object = MibTableColumn
fddiPORT2LerEstimate = _FddiPORT2LerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 13),
    _FddiPORT2LerEstimate_Type()
)
fddiPORT2LerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPORT2LerEstimate.setStatus("mandatory")


class _FddiATTACHMENTClass_Type(Integer32):
    """Custom type fddiATTACHMENTClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 3),
          ("dual-attachment", 2),
          ("single-attachment", 1))
    )


_FddiATTACHMENTClass_Type.__name__ = "Integer32"
_FddiATTACHMENTClass_Object = MibTableColumn
fddiATTACHMENTClass = _FddiATTACHMENTClass_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 14),
    _FddiATTACHMENTClass_Type()
)
fddiATTACHMENTClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiATTACHMENTClass.setStatus("mandatory")


class _FddiATTACHOptBypassPresent_Type(Integer32):
    """Custom type fddiATTACHOptBypassPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddiATTACHOptBypassPresent_Type.__name__ = "Integer32"
_FddiATTACHOptBypassPresent_Object = MibTableColumn
fddiATTACHOptBypassPresent = _FddiATTACHOptBypassPresent_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 5, 1, 1, 15),
    _FddiATTACHOptBypassPresent_Type()
)
fddiATTACHOptBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiATTACHOptBypassPresent.setStatus("mandatory")
_Sk_board_statistics_ObjectIdentity = ObjectIdentity
sk_board_statistics = _Sk_board_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6)
)
_StatsTable_Object = MibTable
statsTable = _StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    statsTable.setStatus("mandatory")
_StatsEntry_Object = MibTableRow
statsEntry = _StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6, 1, 1)
)
statsEntry.setIndexNames(
    (0, "SK-UPPS-MIB", "statsIfIndex"),
)
if mibBuilder.loadTexts:
    statsEntry.setStatus("mandatory")
_StatsIfIndex_Type = Integer32
_StatsIfIndex_Object = MibTableColumn
statsIfIndex = _StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6, 1, 1, 1),
    _StatsIfIndex_Type()
)
statsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsIfIndex.setStatus("mandatory")
_StatsFCSErrors_Type = Counter32
_StatsFCSErrors_Object = MibTableColumn
statsFCSErrors = _StatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6, 1, 1, 2),
    _StatsFCSErrors_Type()
)
statsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsFCSErrors.setStatus("mandatory")
_StatsAlignmentErrors_Type = Counter32
_StatsAlignmentErrors_Object = MibTableColumn
statsAlignmentErrors = _StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6, 1, 1, 3),
    _StatsAlignmentErrors_Type()
)
statsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsAlignmentErrors.setStatus("mandatory")
_StatsFrameTooLongs_Type = Counter32
_StatsFrameTooLongs_Object = MibTableColumn
statsFrameTooLongs = _StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 2, 6, 1, 1, 4),
    _StatsFrameTooLongs_Type()
)
statsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsFrameTooLongs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SK-UPPS-MIB",
    **{"FddiMACLongAddressType": FddiMACLongAddressType,
       "sk": sk,
       "skMibs": skMibs,
       "sk-board": sk_board,
       "sk-board-status": sk_board_status,
       "stTable": stTable,
       "stEntry": stEntry,
       "stIfIndex": stIfIndex,
       "stVersion": stVersion,
       "stLogAddress": stLogAddress,
       "stInterrupt": stInterrupt,
       "stBaseAddress": stBaseAddress,
       "stRAMSize": stRAMSize,
       "stIOPort": stIOPort,
       "stDMALine": stDMALine,
       "stNumMbufs": stNumMbufs,
       "stMaxTxMbufs": stMaxTxMbufs,
       "stMaxRxMbufs": stMaxRxMbufs,
       "stCurrentPacketFilter": stCurrentPacketFilter,
       "stServiceInterrupt": stServiceInterrupt,
       "stOEMSignature": stOEMSignature,
       "stTopology": stTopology,
       "stIORange": stIORange,
       "sk-board-client": sk_board_client,
       "clTable": clTable,
       "clEntry": clEntry,
       "clIfIndex": clIfIndex,
       "clType": clType,
       "clMulticast": clMulticast,
       "clName": clName,
       "clMode": clMode,
       "clPID": clPID,
       "eth": eth,
       "ethStatsTable": ethStatsTable,
       "ethStatsEntry": ethStatsEntry,
       "ethStatsIndex": ethStatsIndex,
       "ethStatsAlignmentErrors": ethStatsAlignmentErrors,
       "ethStatsFCSErrors": ethStatsFCSErrors,
       "ethStatsSingleCollisionFrames": ethStatsSingleCollisionFrames,
       "ethStatsMultipleCollisionFrames": ethStatsMultipleCollisionFrames,
       "ethStatsSQETestErrors": ethStatsSQETestErrors,
       "ethStatsDeferredTransmissions": ethStatsDeferredTransmissions,
       "ethStatsLateCollisions": ethStatsLateCollisions,
       "ethStatsExcessiveCollisions": ethStatsExcessiveCollisions,
       "ethStatsInternalMacTransErrors": ethStatsInternalMacTransErrors,
       "ethStatsCarrierSenseErrors": ethStatsCarrierSenseErrors,
       "ethStatsExcessiveDeferrals": ethStatsExcessiveDeferrals,
       "ethStatsFrameTooLongs": ethStatsFrameTooLongs,
       "ethStatsInRangeLengthErrors": ethStatsInRangeLengthErrors,
       "ethStatsOutOfRangeLengthFields": ethStatsOutOfRangeLengthFields,
       "ethStatsInternalMacRecvErrors": ethStatsInternalMacRecvErrors,
       "tok": tok,
       "tokStatsTable": tokStatsTable,
       "tokStatsEntry": tokStatsEntry,
       "tokStatsIndex": tokStatsIndex,
       "tokStatsUpstreamNbr": tokStatsUpstreamNbr,
       "tokStatsLocalRingNumber": tokStatsLocalRingNumber,
       "tokStatsRingUpCounts": tokStatsRingUpCounts,
       "tokStatsSignalLossErrors": tokStatsSignalLossErrors,
       "tokStatsLobeWireFaults": tokStatsLobeWireFaults,
       "tokStatsRingRecoveryCounts": tokStatsRingRecoveryCounts,
       "tokStatsLineErrors": tokStatsLineErrors,
       "tokStatsBurstErrors": tokStatsBurstErrors,
       "tokStatsARI-FCIErrors": tokStatsARI_FCIErrors,
       "tokStatsLostFrameErrors": tokStatsLostFrameErrors,
       "tokStatsReceiveCongestionErrors": tokStatsReceiveCongestionErrors,
       "tokStatsFrameCopiedErrors": tokStatsFrameCopiedErrors,
       "tokStatsTokenErrors": tokStatsTokenErrors,
       "tokStatsDMABusErrors": tokStatsDMABusErrors,
       "tokStatsDMAParityErrors": tokStatsDMAParityErrors,
       "tokStatsReceiveOverflowErrors": tokStatsReceiveOverflowErrors,
       "fddi": fddi,
       "fddiStatsTable": fddiStatsTable,
       "fddiStatsEntry": fddiStatsEntry,
       "fddiStatsIndex": fddiStatsIndex,
       "fddiSMTOpVersionId": fddiSMTOpVersionId,
       "fddiSMTCFState": fddiSMTCFState,
       "fddiSMTFrameSends": fddiSMTFrameSends,
       "fddiSMTFrameReceives": fddiSMTFrameReceives,
       "fddiSMTRingUps": fddiSMTRingUps,
       "fddiMACUpstreamNbr": fddiMACUpstreamNbr,
       "fddiMACDownstreamNbr": fddiMACDownstreamNbr,
       "fddiMACFrameCts": fddiMACFrameCts,
       "fddiMACErrorCts": fddiMACErrorCts,
       "fddiMACLostCts": fddiMACLostCts,
       "fddiPORT1LerEstimate": fddiPORT1LerEstimate,
       "fddiPORT2LerEstimate": fddiPORT2LerEstimate,
       "fddiATTACHMENTClass": fddiATTACHMENTClass,
       "fddiATTACHOptBypassPresent": fddiATTACHOptBypassPresent,
       "sk-board-statistics": sk_board_statistics,
       "statsTable": statsTable,
       "statsEntry": statsEntry,
       "statsIfIndex": statsIfIndex,
       "statsFCSErrors": statsFCSErrors,
       "statsAlignmentErrors": statsAlignmentErrors,
       "statsFrameTooLongs": statsFrameTooLongs}
)
