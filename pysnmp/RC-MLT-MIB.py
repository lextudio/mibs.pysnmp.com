# SNMP MIB module (RC-MLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RC-MLT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:34 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnableValue,
 IdList,
 PortSet,
 rcL2Redundancy,
 rcLinkFlapDetect,
 rcMlt,
 rcStat) = mibBuilder.importSymbols(
    "RAPID-CITY",
    "EnableValue",
    "IdList",
    "PortSet",
    "rcL2Redundancy",
    "rcLinkFlapDetect",
    "rcMlt",
    "rcStat")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcMltMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 0)
)
rcMltMib.setRevisions(
        ("2010-10-20 00:00",
         "2010-09-21 00:00",
         "2010-09-14 00:00",
         "2009-12-16 00:00",
         "2009-11-16 00:00",
         "2009-03-20 00:00",
         "2007-12-20 00:00",
         "2007-04-16 00:00",
         "2006-07-05 00:00",
         "2005-12-06 00:00",
         "2005-09-01 00:00",
         "2005-08-10 00:00",
         "2005-07-11 00:00",
         "2005-05-27 00:00",
         "2005-02-02 00:00",
         "2005-01-04 00:00",
         "2004-12-21 00:00",
         "2004-09-30 00:00",
         "2004-09-23 00:00",
         "2004-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcStatMlt_ObjectIdentity = ObjectIdentity
rcStatMlt = _RcStatMlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6)
)
_RcStatMltIfExtnTable_Object = MibTable
rcStatMltIfExtnTable = _RcStatMltIfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1)
)
if mibBuilder.loadTexts:
    rcStatMltIfExtnTable.setStatus("current")
_RcStatMltIfExtnEntry_Object = MibTableRow
rcStatMltIfExtnEntry = _RcStatMltIfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1)
)
rcStatMltIfExtnEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcStatMltIfExtnMltId"),
)
if mibBuilder.loadTexts:
    rcStatMltIfExtnEntry.setStatus("current")


class _RcStatMltIfExtnMltId_Type(Integer32):
    """Custom type rcStatMltIfExtnMltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RcStatMltIfExtnMltId_Type.__name__ = "Integer32"
_RcStatMltIfExtnMltId_Object = MibTableColumn
rcStatMltIfExtnMltId = _RcStatMltIfExtnMltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 1),
    _RcStatMltIfExtnMltId_Type()
)
rcStatMltIfExtnMltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnMltId.setStatus("current")
_RcStatMltIfExtnIfInMulticastPkts_Type = Counter32
_RcStatMltIfExtnIfInMulticastPkts_Object = MibTableColumn
rcStatMltIfExtnIfInMulticastPkts = _RcStatMltIfExtnIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 2),
    _RcStatMltIfExtnIfInMulticastPkts_Type()
)
rcStatMltIfExtnIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfInMulticastPkts.setStatus("current")
_RcStatMltIfExtnIfInBroadcastPkts_Type = Counter32
_RcStatMltIfExtnIfInBroadcastPkts_Object = MibTableColumn
rcStatMltIfExtnIfInBroadcastPkts = _RcStatMltIfExtnIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 3),
    _RcStatMltIfExtnIfInBroadcastPkts_Type()
)
rcStatMltIfExtnIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfInBroadcastPkts.setStatus("current")
_RcStatMltIfExtnIfOutMulticastPkts_Type = Counter32
_RcStatMltIfExtnIfOutMulticastPkts_Object = MibTableColumn
rcStatMltIfExtnIfOutMulticastPkts = _RcStatMltIfExtnIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 4),
    _RcStatMltIfExtnIfOutMulticastPkts_Type()
)
rcStatMltIfExtnIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfOutMulticastPkts.setStatus("current")
_RcStatMltIfExtnIfOutBroadcastPkts_Type = Counter32
_RcStatMltIfExtnIfOutBroadcastPkts_Object = MibTableColumn
rcStatMltIfExtnIfOutBroadcastPkts = _RcStatMltIfExtnIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 5),
    _RcStatMltIfExtnIfOutBroadcastPkts_Type()
)
rcStatMltIfExtnIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfOutBroadcastPkts.setStatus("current")
_RcStatMltIfExtnIfHCInOctets_Type = Counter64
_RcStatMltIfExtnIfHCInOctets_Object = MibTableColumn
rcStatMltIfExtnIfHCInOctets = _RcStatMltIfExtnIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 6),
    _RcStatMltIfExtnIfHCInOctets_Type()
)
rcStatMltIfExtnIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCInOctets.setStatus("current")
_RcStatMltIfExtnIfHCInUcastPkts_Type = Counter64
_RcStatMltIfExtnIfHCInUcastPkts_Object = MibTableColumn
rcStatMltIfExtnIfHCInUcastPkts = _RcStatMltIfExtnIfHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 7),
    _RcStatMltIfExtnIfHCInUcastPkts_Type()
)
rcStatMltIfExtnIfHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCInUcastPkts.setStatus("current")
_RcStatMltIfExtnIfHCInMulticastPkt_Type = Counter64
_RcStatMltIfExtnIfHCInMulticastPkt_Object = MibTableColumn
rcStatMltIfExtnIfHCInMulticastPkt = _RcStatMltIfExtnIfHCInMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 8),
    _RcStatMltIfExtnIfHCInMulticastPkt_Type()
)
rcStatMltIfExtnIfHCInMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCInMulticastPkt.setStatus("current")
_RcStatMltIfExtnIfHCInBroadcastPkt_Type = Counter64
_RcStatMltIfExtnIfHCInBroadcastPkt_Object = MibTableColumn
rcStatMltIfExtnIfHCInBroadcastPkt = _RcStatMltIfExtnIfHCInBroadcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 9),
    _RcStatMltIfExtnIfHCInBroadcastPkt_Type()
)
rcStatMltIfExtnIfHCInBroadcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCInBroadcastPkt.setStatus("current")
_RcStatMltIfExtnIfHCOutOctets_Type = Counter64
_RcStatMltIfExtnIfHCOutOctets_Object = MibTableColumn
rcStatMltIfExtnIfHCOutOctets = _RcStatMltIfExtnIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 10),
    _RcStatMltIfExtnIfHCOutOctets_Type()
)
rcStatMltIfExtnIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCOutOctets.setStatus("current")
_RcStatMltIfExtnIfHCOutUcastPkts_Type = Counter64
_RcStatMltIfExtnIfHCOutUcastPkts_Object = MibTableColumn
rcStatMltIfExtnIfHCOutUcastPkts = _RcStatMltIfExtnIfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 11),
    _RcStatMltIfExtnIfHCOutUcastPkts_Type()
)
rcStatMltIfExtnIfHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCOutUcastPkts.setStatus("current")
_RcStatMltIfExtnIfHCOutMulticast_Type = Counter64
_RcStatMltIfExtnIfHCOutMulticast_Object = MibTableColumn
rcStatMltIfExtnIfHCOutMulticast = _RcStatMltIfExtnIfHCOutMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 12),
    _RcStatMltIfExtnIfHCOutMulticast_Type()
)
rcStatMltIfExtnIfHCOutMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCOutMulticast.setStatus("current")
_RcStatMltIfExtnIfHCOutBroadcast_Type = Counter64
_RcStatMltIfExtnIfHCOutBroadcast_Object = MibTableColumn
rcStatMltIfExtnIfHCOutBroadcast = _RcStatMltIfExtnIfHCOutBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 1, 1, 13),
    _RcStatMltIfExtnIfHCOutBroadcast_Type()
)
rcStatMltIfExtnIfHCOutBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfExtnIfHCOutBroadcast.setStatus("current")
_RcStatMltEtherTable_Object = MibTable
rcStatMltEtherTable = _RcStatMltEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2)
)
if mibBuilder.loadTexts:
    rcStatMltEtherTable.setStatus("current")
_RcStatMltEtherEntry_Object = MibTableRow
rcStatMltEtherEntry = _RcStatMltEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1)
)
rcStatMltEtherEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcStatMltEtherMltId"),
)
if mibBuilder.loadTexts:
    rcStatMltEtherEntry.setStatus("current")


class _RcStatMltEtherMltId_Type(Integer32):
    """Custom type rcStatMltEtherMltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RcStatMltEtherMltId_Type.__name__ = "Integer32"
_RcStatMltEtherMltId_Object = MibTableColumn
rcStatMltEtherMltId = _RcStatMltEtherMltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 1),
    _RcStatMltEtherMltId_Type()
)
rcStatMltEtherMltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherMltId.setStatus("current")
_RcStatMltEtherAlignmentErrors_Type = Counter32
_RcStatMltEtherAlignmentErrors_Object = MibTableColumn
rcStatMltEtherAlignmentErrors = _RcStatMltEtherAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 2),
    _RcStatMltEtherAlignmentErrors_Type()
)
rcStatMltEtherAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherAlignmentErrors.setStatus("current")
_RcStatMltEtherFCSErrors_Type = Counter32
_RcStatMltEtherFCSErrors_Object = MibTableColumn
rcStatMltEtherFCSErrors = _RcStatMltEtherFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 3),
    _RcStatMltEtherFCSErrors_Type()
)
rcStatMltEtherFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherFCSErrors.setStatus("current")
_RcStatMltEtherSingleCollFrames_Type = Counter32
_RcStatMltEtherSingleCollFrames_Object = MibTableColumn
rcStatMltEtherSingleCollFrames = _RcStatMltEtherSingleCollFrames_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 4),
    _RcStatMltEtherSingleCollFrames_Type()
)
rcStatMltEtherSingleCollFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherSingleCollFrames.setStatus("current")
_RcStatMltEtherMultipleCollFrames_Type = Counter32
_RcStatMltEtherMultipleCollFrames_Object = MibTableColumn
rcStatMltEtherMultipleCollFrames = _RcStatMltEtherMultipleCollFrames_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 5),
    _RcStatMltEtherMultipleCollFrames_Type()
)
rcStatMltEtherMultipleCollFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherMultipleCollFrames.setStatus("current")
_RcStatMltEtherSQETestError_Type = Counter32
_RcStatMltEtherSQETestError_Object = MibTableColumn
rcStatMltEtherSQETestError = _RcStatMltEtherSQETestError_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 6),
    _RcStatMltEtherSQETestError_Type()
)
rcStatMltEtherSQETestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherSQETestError.setStatus("current")
_RcStatMltEtherDeferredTransmiss_Type = Counter32
_RcStatMltEtherDeferredTransmiss_Object = MibTableColumn
rcStatMltEtherDeferredTransmiss = _RcStatMltEtherDeferredTransmiss_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 7),
    _RcStatMltEtherDeferredTransmiss_Type()
)
rcStatMltEtherDeferredTransmiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherDeferredTransmiss.setStatus("current")
_RcStatMltEtherLateCollisions_Type = Counter32
_RcStatMltEtherLateCollisions_Object = MibTableColumn
rcStatMltEtherLateCollisions = _RcStatMltEtherLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 8),
    _RcStatMltEtherLateCollisions_Type()
)
rcStatMltEtherLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherLateCollisions.setStatus("current")
_RcStatMltEtherExcessiveCollis_Type = Counter32
_RcStatMltEtherExcessiveCollis_Object = MibTableColumn
rcStatMltEtherExcessiveCollis = _RcStatMltEtherExcessiveCollis_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 9),
    _RcStatMltEtherExcessiveCollis_Type()
)
rcStatMltEtherExcessiveCollis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherExcessiveCollis.setStatus("current")
_RcStatMltEtherIMacTransmitError_Type = Counter32
_RcStatMltEtherIMacTransmitError_Object = MibTableColumn
rcStatMltEtherIMacTransmitError = _RcStatMltEtherIMacTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 10),
    _RcStatMltEtherIMacTransmitError_Type()
)
rcStatMltEtherIMacTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherIMacTransmitError.setStatus("current")
_RcStatMltEtherCarrierSenseError_Type = Counter32
_RcStatMltEtherCarrierSenseError_Object = MibTableColumn
rcStatMltEtherCarrierSenseError = _RcStatMltEtherCarrierSenseError_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 11),
    _RcStatMltEtherCarrierSenseError_Type()
)
rcStatMltEtherCarrierSenseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherCarrierSenseError.setStatus("current")
_RcStatMltEtherFrameTooLong_Type = Counter32
_RcStatMltEtherFrameTooLong_Object = MibTableColumn
rcStatMltEtherFrameTooLong = _RcStatMltEtherFrameTooLong_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 12),
    _RcStatMltEtherFrameTooLong_Type()
)
rcStatMltEtherFrameTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherFrameTooLong.setStatus("current")
_RcStatMltEtherIMacReceiveError_Type = Counter32
_RcStatMltEtherIMacReceiveError_Object = MibTableColumn
rcStatMltEtherIMacReceiveError = _RcStatMltEtherIMacReceiveError_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 2, 1, 13),
    _RcStatMltEtherIMacReceiveError_Type()
)
rcStatMltEtherIMacReceiveError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltEtherIMacReceiveError.setStatus("current")
_RcStatMltIpTable_Object = MibTable
rcStatMltIpTable = _RcStatMltIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3)
)
if mibBuilder.loadTexts:
    rcStatMltIpTable.setStatus("deprecated")
_RcStatMltIpEntry_Object = MibTableRow
rcStatMltIpEntry = _RcStatMltIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1)
)
rcStatMltIpEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcStatMltIpMltId"),
)
if mibBuilder.loadTexts:
    rcStatMltIpEntry.setStatus("deprecated")


class _RcStatMltIpMltId_Type(Integer32):
    """Custom type rcStatMltIpMltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcStatMltIpMltId_Type.__name__ = "Integer32"
_RcStatMltIpMltId_Object = MibTableColumn
rcStatMltIpMltId = _RcStatMltIpMltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 1),
    _RcStatMltIpMltId_Type()
)
rcStatMltIpMltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpMltId.setStatus("deprecated")
_RcStatMltIpInReceives_Type = Counter32
_RcStatMltIpInReceives_Object = MibTableColumn
rcStatMltIpInReceives = _RcStatMltIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 2),
    _RcStatMltIpInReceives_Type()
)
rcStatMltIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpInReceives.setStatus("deprecated")
_RcStatMltIpInHdrErrors_Type = Counter32
_RcStatMltIpInHdrErrors_Object = MibTableColumn
rcStatMltIpInHdrErrors = _RcStatMltIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 3),
    _RcStatMltIpInHdrErrors_Type()
)
rcStatMltIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpInHdrErrors.setStatus("deprecated")
_RcStatMltIpInAddrErrors_Type = Counter32
_RcStatMltIpInAddrErrors_Object = MibTableColumn
rcStatMltIpInAddrErrors = _RcStatMltIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 4),
    _RcStatMltIpInAddrErrors_Type()
)
rcStatMltIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpInAddrErrors.setStatus("deprecated")
_RcStatMltIpForwDatagrams_Type = Counter32
_RcStatMltIpForwDatagrams_Object = MibTableColumn
rcStatMltIpForwDatagrams = _RcStatMltIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 5),
    _RcStatMltIpForwDatagrams_Type()
)
rcStatMltIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpForwDatagrams.setStatus("deprecated")
_RcStatMltIpInUnknownProtos_Type = Counter32
_RcStatMltIpInUnknownProtos_Object = MibTableColumn
rcStatMltIpInUnknownProtos = _RcStatMltIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 6),
    _RcStatMltIpInUnknownProtos_Type()
)
rcStatMltIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpInUnknownProtos.setStatus("deprecated")
_RcStatMltIpInDiscards_Type = Counter32
_RcStatMltIpInDiscards_Object = MibTableColumn
rcStatMltIpInDiscards = _RcStatMltIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 7),
    _RcStatMltIpInDiscards_Type()
)
rcStatMltIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpInDiscards.setStatus("deprecated")
_RcStatMltIpInDelivers_Type = Counter32
_RcStatMltIpInDelivers_Object = MibTableColumn
rcStatMltIpInDelivers = _RcStatMltIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 8),
    _RcStatMltIpInDelivers_Type()
)
rcStatMltIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpInDelivers.setStatus("deprecated")
_RcStatMltIpOutRequest_Type = Counter32
_RcStatMltIpOutRequest_Object = MibTableColumn
rcStatMltIpOutRequest = _RcStatMltIpOutRequest_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 9),
    _RcStatMltIpOutRequest_Type()
)
rcStatMltIpOutRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpOutRequest.setStatus("deprecated")
_RcStatMltIpOutDiscards_Type = Counter32
_RcStatMltIpOutDiscards_Object = MibTableColumn
rcStatMltIpOutDiscards = _RcStatMltIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 10),
    _RcStatMltIpOutDiscards_Type()
)
rcStatMltIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpOutDiscards.setStatus("deprecated")
_RcStatMltIpOutNoRoutes_Type = Counter32
_RcStatMltIpOutNoRoutes_Object = MibTableColumn
rcStatMltIpOutNoRoutes = _RcStatMltIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 11),
    _RcStatMltIpOutNoRoutes_Type()
)
rcStatMltIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpOutNoRoutes.setStatus("deprecated")
_RcStatMltIpReasmReqds_Type = Counter32
_RcStatMltIpReasmReqds_Object = MibTableColumn
rcStatMltIpReasmReqds = _RcStatMltIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 12),
    _RcStatMltIpReasmReqds_Type()
)
rcStatMltIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpReasmReqds.setStatus("deprecated")
_RcStatMltIpReasmOKs_Type = Counter32
_RcStatMltIpReasmOKs_Object = MibTableColumn
rcStatMltIpReasmOKs = _RcStatMltIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 13),
    _RcStatMltIpReasmOKs_Type()
)
rcStatMltIpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpReasmOKs.setStatus("deprecated")
_RcStatMltIpReasmFails_Type = Counter32
_RcStatMltIpReasmFails_Object = MibTableColumn
rcStatMltIpReasmFails = _RcStatMltIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 14),
    _RcStatMltIpReasmFails_Type()
)
rcStatMltIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpReasmFails.setStatus("deprecated")
_RcStatMltIpFragOKs_Type = Counter32
_RcStatMltIpFragOKs_Object = MibTableColumn
rcStatMltIpFragOKs = _RcStatMltIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 15),
    _RcStatMltIpFragOKs_Type()
)
rcStatMltIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpFragOKs.setStatus("deprecated")
_RcStatMltIpFragFails_Type = Counter32
_RcStatMltIpFragFails_Object = MibTableColumn
rcStatMltIpFragFails = _RcStatMltIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 16),
    _RcStatMltIpFragFails_Type()
)
rcStatMltIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpFragFails.setStatus("deprecated")
_RcStatMltIpFragCreates_Type = Counter32
_RcStatMltIpFragCreates_Object = MibTableColumn
rcStatMltIpFragCreates = _RcStatMltIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 17),
    _RcStatMltIpFragCreates_Type()
)
rcStatMltIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpFragCreates.setStatus("deprecated")
_RcStatMltIpRoutingDiscards_Type = Counter32
_RcStatMltIpRoutingDiscards_Object = MibTableColumn
rcStatMltIpRoutingDiscards = _RcStatMltIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 3, 1, 18),
    _RcStatMltIpRoutingDiscards_Type()
)
rcStatMltIpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIpRoutingDiscards.setStatus("deprecated")
_RcStatSmltIstDownCnt_Type = Counter32
_RcStatSmltIstDownCnt_Object = MibScalar
rcStatSmltIstDownCnt = _RcStatSmltIstDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 4),
    _RcStatSmltIstDownCnt_Type()
)
rcStatSmltIstDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltIstDownCnt.setStatus("current")
_RcStatSmltHelloTxMsgCnt_Type = Counter32
_RcStatSmltHelloTxMsgCnt_Object = MibScalar
rcStatSmltHelloTxMsgCnt = _RcStatSmltHelloTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 5),
    _RcStatSmltHelloTxMsgCnt_Type()
)
rcStatSmltHelloTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltHelloTxMsgCnt.setStatus("current")
_RcStatSmltHelloRxMsgCnt_Type = Counter32
_RcStatSmltHelloRxMsgCnt_Object = MibScalar
rcStatSmltHelloRxMsgCnt = _RcStatSmltHelloRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 6),
    _RcStatSmltHelloRxMsgCnt_Type()
)
rcStatSmltHelloRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltHelloRxMsgCnt.setStatus("current")
_RcStatSmltLearnMacAddrTxMsgCnt_Type = Counter32
_RcStatSmltLearnMacAddrTxMsgCnt_Object = MibScalar
rcStatSmltLearnMacAddrTxMsgCnt = _RcStatSmltLearnMacAddrTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 7),
    _RcStatSmltLearnMacAddrTxMsgCnt_Type()
)
rcStatSmltLearnMacAddrTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltLearnMacAddrTxMsgCnt.setStatus("current")
_RcStatSmltLearnMacAddrRxMsgCnt_Type = Counter32
_RcStatSmltLearnMacAddrRxMsgCnt_Object = MibScalar
rcStatSmltLearnMacAddrRxMsgCnt = _RcStatSmltLearnMacAddrRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 8),
    _RcStatSmltLearnMacAddrRxMsgCnt_Type()
)
rcStatSmltLearnMacAddrRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltLearnMacAddrRxMsgCnt.setStatus("current")
_RcStatSmltMacAddrAgeOutTxMsgCnt_Type = Counter32
_RcStatSmltMacAddrAgeOutTxMsgCnt_Object = MibScalar
rcStatSmltMacAddrAgeOutTxMsgCnt = _RcStatSmltMacAddrAgeOutTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 9),
    _RcStatSmltMacAddrAgeOutTxMsgCnt_Type()
)
rcStatSmltMacAddrAgeOutTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltMacAddrAgeOutTxMsgCnt.setStatus("current")
_RcStatSmltMacAddrAgeOutRxMsgCnt_Type = Counter32
_RcStatSmltMacAddrAgeOutRxMsgCnt_Object = MibScalar
rcStatSmltMacAddrAgeOutRxMsgCnt = _RcStatSmltMacAddrAgeOutRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 10),
    _RcStatSmltMacAddrAgeOutRxMsgCnt_Type()
)
rcStatSmltMacAddrAgeOutRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltMacAddrAgeOutRxMsgCnt.setStatus("current")
_RcStatSmltMacAddrAgeExpTxMsgCnt_Type = Counter32
_RcStatSmltMacAddrAgeExpTxMsgCnt_Object = MibScalar
rcStatSmltMacAddrAgeExpTxMsgCnt = _RcStatSmltMacAddrAgeExpTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 11),
    _RcStatSmltMacAddrAgeExpTxMsgCnt_Type()
)
rcStatSmltMacAddrAgeExpTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltMacAddrAgeExpTxMsgCnt.setStatus("current")
_RcStatSmltMacAddrAgeExpRxMsgCnt_Type = Counter32
_RcStatSmltMacAddrAgeExpRxMsgCnt_Object = MibScalar
rcStatSmltMacAddrAgeExpRxMsgCnt = _RcStatSmltMacAddrAgeExpRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 12),
    _RcStatSmltMacAddrAgeExpRxMsgCnt_Type()
)
rcStatSmltMacAddrAgeExpRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltMacAddrAgeExpRxMsgCnt.setStatus("current")
_RcStatSmltStgInfoTxMsgCnt_Type = Counter32
_RcStatSmltStgInfoTxMsgCnt_Object = MibScalar
rcStatSmltStgInfoTxMsgCnt = _RcStatSmltStgInfoTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 13),
    _RcStatSmltStgInfoTxMsgCnt_Type()
)
rcStatSmltStgInfoTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltStgInfoTxMsgCnt.setStatus("current")
_RcStatSmltStgInfoRxMsgCnt_Type = Counter32
_RcStatSmltStgInfoRxMsgCnt_Object = MibScalar
rcStatSmltStgInfoRxMsgCnt = _RcStatSmltStgInfoRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 14),
    _RcStatSmltStgInfoRxMsgCnt_Type()
)
rcStatSmltStgInfoRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltStgInfoRxMsgCnt.setStatus("current")
_RcStatSmltDelMacAddrTxMsgCnt_Type = Counter32
_RcStatSmltDelMacAddrTxMsgCnt_Object = MibScalar
rcStatSmltDelMacAddrTxMsgCnt = _RcStatSmltDelMacAddrTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 15),
    _RcStatSmltDelMacAddrTxMsgCnt_Type()
)
rcStatSmltDelMacAddrTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltDelMacAddrTxMsgCnt.setStatus("current")
_RcStatSmltDelMacAddrRxMsgCnt_Type = Counter32
_RcStatSmltDelMacAddrRxMsgCnt_Object = MibScalar
rcStatSmltDelMacAddrRxMsgCnt = _RcStatSmltDelMacAddrRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 16),
    _RcStatSmltDelMacAddrRxMsgCnt_Type()
)
rcStatSmltDelMacAddrRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltDelMacAddrRxMsgCnt.setStatus("current")
_RcStatSmltSmltDownTxMsgCnt_Type = Counter32
_RcStatSmltSmltDownTxMsgCnt_Object = MibScalar
rcStatSmltSmltDownTxMsgCnt = _RcStatSmltSmltDownTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 17),
    _RcStatSmltSmltDownTxMsgCnt_Type()
)
rcStatSmltSmltDownTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltSmltDownTxMsgCnt.setStatus("current")
_RcStatSmltSmltDownRxMsgCnt_Type = Counter32
_RcStatSmltSmltDownRxMsgCnt_Object = MibScalar
rcStatSmltSmltDownRxMsgCnt = _RcStatSmltSmltDownRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 18),
    _RcStatSmltSmltDownRxMsgCnt_Type()
)
rcStatSmltSmltDownRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltSmltDownRxMsgCnt.setStatus("current")
_RcStatSmltSmltUpTxMsgCnt_Type = Counter32
_RcStatSmltSmltUpTxMsgCnt_Object = MibScalar
rcStatSmltSmltUpTxMsgCnt = _RcStatSmltSmltUpTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 19),
    _RcStatSmltSmltUpTxMsgCnt_Type()
)
rcStatSmltSmltUpTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltSmltUpTxMsgCnt.setStatus("current")
_RcStatSmltSmltUpRxMsgCnt_Type = Counter32
_RcStatSmltSmltUpRxMsgCnt_Object = MibScalar
rcStatSmltSmltUpRxMsgCnt = _RcStatSmltSmltUpRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 20),
    _RcStatSmltSmltUpRxMsgCnt_Type()
)
rcStatSmltSmltUpRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltSmltUpRxMsgCnt.setStatus("current")
_RcStatSmltSendMacTblTxMsgCnt_Type = Counter32
_RcStatSmltSendMacTblTxMsgCnt_Object = MibScalar
rcStatSmltSendMacTblTxMsgCnt = _RcStatSmltSendMacTblTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 21),
    _RcStatSmltSendMacTblTxMsgCnt_Type()
)
rcStatSmltSendMacTblTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltSendMacTblTxMsgCnt.setStatus("current")
_RcStatSmltSendMacTblRxMsgCnt_Type = Counter32
_RcStatSmltSendMacTblRxMsgCnt_Object = MibScalar
rcStatSmltSendMacTblRxMsgCnt = _RcStatSmltSendMacTblRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 22),
    _RcStatSmltSendMacTblRxMsgCnt_Type()
)
rcStatSmltSendMacTblRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltSendMacTblRxMsgCnt.setStatus("current")
_RcStatSmltIgmpTxMsgCnt_Type = Counter32
_RcStatSmltIgmpTxMsgCnt_Object = MibScalar
rcStatSmltIgmpTxMsgCnt = _RcStatSmltIgmpTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 23),
    _RcStatSmltIgmpTxMsgCnt_Type()
)
rcStatSmltIgmpTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltIgmpTxMsgCnt.setStatus("current")
_RcStatSmltIgmpRxMsgCnt_Type = Counter32
_RcStatSmltIgmpRxMsgCnt_Object = MibScalar
rcStatSmltIgmpRxMsgCnt = _RcStatSmltIgmpRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 24),
    _RcStatSmltIgmpRxMsgCnt_Type()
)
rcStatSmltIgmpRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltIgmpRxMsgCnt.setStatus("current")
_RcStatSmltPortDownTxMsgCnt_Type = Counter32
_RcStatSmltPortDownTxMsgCnt_Object = MibScalar
rcStatSmltPortDownTxMsgCnt = _RcStatSmltPortDownTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 25),
    _RcStatSmltPortDownTxMsgCnt_Type()
)
rcStatSmltPortDownTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltPortDownTxMsgCnt.setStatus("current")
_RcStatSmltPortDownRxMsgCnt_Type = Counter32
_RcStatSmltPortDownRxMsgCnt_Object = MibScalar
rcStatSmltPortDownRxMsgCnt = _RcStatSmltPortDownRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 26),
    _RcStatSmltPortDownRxMsgCnt_Type()
)
rcStatSmltPortDownRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltPortDownRxMsgCnt.setStatus("current")
_RcStatSmltReqMacTblTxMsgCnt_Type = Counter32
_RcStatSmltReqMacTblTxMsgCnt_Object = MibScalar
rcStatSmltReqMacTblTxMsgCnt = _RcStatSmltReqMacTblTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 27),
    _RcStatSmltReqMacTblTxMsgCnt_Type()
)
rcStatSmltReqMacTblTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltReqMacTblTxMsgCnt.setStatus("current")
_RcStatSmltReqMacTblRxMsgCnt_Type = Counter32
_RcStatSmltReqMacTblRxMsgCnt_Object = MibScalar
rcStatSmltReqMacTblRxMsgCnt = _RcStatSmltReqMacTblRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 28),
    _RcStatSmltReqMacTblRxMsgCnt_Type()
)
rcStatSmltReqMacTblRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltReqMacTblRxMsgCnt.setStatus("current")
_RcStatSmltRxUnknownMsgTypeCnt_Type = Counter32
_RcStatSmltRxUnknownMsgTypeCnt_Object = MibScalar
rcStatSmltRxUnknownMsgTypeCnt = _RcStatSmltRxUnknownMsgTypeCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 29),
    _RcStatSmltRxUnknownMsgTypeCnt_Type()
)
rcStatSmltRxUnknownMsgTypeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltRxUnknownMsgTypeCnt.setStatus("current")
_RcStatMltIfUtilTable_Object = MibTable
rcStatMltIfUtilTable = _RcStatMltIfUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30)
)
if mibBuilder.loadTexts:
    rcStatMltIfUtilTable.setStatus("current")
_RcStatMltIfUtilEntry_Object = MibTableRow
rcStatMltIfUtilEntry = _RcStatMltIfUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30, 1)
)
rcStatMltIfUtilEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcStatMltIfUtilMltId"),
)
if mibBuilder.loadTexts:
    rcStatMltIfUtilEntry.setStatus("current")


class _RcStatMltIfUtilMltId_Type(Integer32):
    """Custom type rcStatMltIfUtilMltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RcStatMltIfUtilMltId_Type.__name__ = "Integer32"
_RcStatMltIfUtilMltId_Object = MibTableColumn
rcStatMltIfUtilMltId = _RcStatMltIfUtilMltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30, 1, 1),
    _RcStatMltIfUtilMltId_Type()
)
rcStatMltIfUtilMltId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcStatMltIfUtilMltId.setStatus("current")
_RcStatMltIfUtilIfHCInOctets_Type = Counter64
_RcStatMltIfUtilIfHCInOctets_Object = MibTableColumn
rcStatMltIfUtilIfHCInOctets = _RcStatMltIfUtilIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30, 1, 2),
    _RcStatMltIfUtilIfHCInOctets_Type()
)
rcStatMltIfUtilIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfUtilIfHCInOctets.setStatus("current")
_RcStatMltIfUtilIfHCInUtil_Type = Gauge32
_RcStatMltIfUtilIfHCInUtil_Object = MibTableColumn
rcStatMltIfUtilIfHCInUtil = _RcStatMltIfUtilIfHCInUtil_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30, 1, 3),
    _RcStatMltIfUtilIfHCInUtil_Type()
)
rcStatMltIfUtilIfHCInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfUtilIfHCInUtil.setStatus("current")
_RcStatMltIfUtilIfHCOutOctets_Type = Counter64
_RcStatMltIfUtilIfHCOutOctets_Object = MibTableColumn
rcStatMltIfUtilIfHCOutOctets = _RcStatMltIfUtilIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30, 1, 4),
    _RcStatMltIfUtilIfHCOutOctets_Type()
)
rcStatMltIfUtilIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfUtilIfHCOutOctets.setStatus("current")
_RcStatMltIfUtilIfHCOutUtil_Type = Gauge32
_RcStatMltIfUtilIfHCOutUtil_Object = MibTableColumn
rcStatMltIfUtilIfHCOutUtil = _RcStatMltIfUtilIfHCOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 30, 1, 5),
    _RcStatMltIfUtilIfHCOutUtil_Type()
)
rcStatMltIfUtilIfHCOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltIfUtilIfHCOutUtil.setStatus("current")
_RcStatSmltLacpInfoRxMsgCnt_Type = Counter32
_RcStatSmltLacpInfoRxMsgCnt_Object = MibScalar
rcStatSmltLacpInfoRxMsgCnt = _RcStatSmltLacpInfoRxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 31),
    _RcStatSmltLacpInfoRxMsgCnt_Type()
)
rcStatSmltLacpInfoRxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltLacpInfoRxMsgCnt.setStatus("current")
_RcStatSmltLacpInfoTxMsgCnt_Type = Counter32
_RcStatSmltLacpInfoTxMsgCnt_Object = MibScalar
rcStatSmltLacpInfoTxMsgCnt = _RcStatSmltLacpInfoTxMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 32),
    _RcStatSmltLacpInfoTxMsgCnt_Type()
)
rcStatSmltLacpInfoTxMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatSmltLacpInfoTxMsgCnt.setStatus("current")
_RcStatMltUtilTable_Object = MibTable
rcStatMltUtilTable = _RcStatMltUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33)
)
if mibBuilder.loadTexts:
    rcStatMltUtilTable.setStatus("current")
_RcStatMltUtilEntry_Object = MibTableRow
rcStatMltUtilEntry = _RcStatMltUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33, 1)
)
rcStatMltUtilEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcMltId"),
    (0, "RC-MLT-MIB", "rcStatMltUtilPortIfIndex"),
    (0, "RC-MLT-MIB", "rcStatMltUtilTrafficType"),
)
if mibBuilder.loadTexts:
    rcStatMltUtilEntry.setStatus("current")
_RcStatMltUtilPortIfIndex_Type = InterfaceIndex
_RcStatMltUtilPortIfIndex_Object = MibTableColumn
rcStatMltUtilPortIfIndex = _RcStatMltUtilPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33, 1, 1),
    _RcStatMltUtilPortIfIndex_Type()
)
rcStatMltUtilPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcStatMltUtilPortIfIndex.setStatus("current")


class _RcStatMltUtilTrafficType_Type(Integer32):
    """Custom type rcStatMltUtilTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("rxTx", 3),
          ("tx", 2))
    )


_RcStatMltUtilTrafficType_Type.__name__ = "Integer32"
_RcStatMltUtilTrafficType_Object = MibTableColumn
rcStatMltUtilTrafficType = _RcStatMltUtilTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33, 1, 2),
    _RcStatMltUtilTrafficType_Type()
)
rcStatMltUtilTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcStatMltUtilTrafficType.setStatus("current")


class _RcStatMltUtilTrafficLast5Min_Type(Gauge32):
    """Custom type rcStatMltUtilTrafficLast5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RcStatMltUtilTrafficLast5Min_Type.__name__ = "Gauge32"
_RcStatMltUtilTrafficLast5Min_Object = MibTableColumn
rcStatMltUtilTrafficLast5Min = _RcStatMltUtilTrafficLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33, 1, 3),
    _RcStatMltUtilTrafficLast5Min_Type()
)
rcStatMltUtilTrafficLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltUtilTrafficLast5Min.setStatus("current")


class _RcStatMltUtilTrafficLast30Min_Type(Gauge32):
    """Custom type rcStatMltUtilTrafficLast30Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RcStatMltUtilTrafficLast30Min_Type.__name__ = "Gauge32"
_RcStatMltUtilTrafficLast30Min_Object = MibTableColumn
rcStatMltUtilTrafficLast30Min = _RcStatMltUtilTrafficLast30Min_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33, 1, 4),
    _RcStatMltUtilTrafficLast30Min_Type()
)
rcStatMltUtilTrafficLast30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltUtilTrafficLast30Min.setStatus("current")


class _RcStatMltUtilTrafficLast1Hour_Type(Gauge32):
    """Custom type rcStatMltUtilTrafficLast1Hour based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RcStatMltUtilTrafficLast1Hour_Type.__name__ = "Gauge32"
_RcStatMltUtilTrafficLast1Hour_Object = MibTableColumn
rcStatMltUtilTrafficLast1Hour = _RcStatMltUtilTrafficLast1Hour_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 12, 6, 33, 1, 5),
    _RcStatMltUtilTrafficLast1Hour_Type()
)
rcStatMltUtilTrafficLast1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcStatMltUtilTrafficLast1Hour.setStatus("current")
_RcMltNumMlts_Type = Integer32
_RcMltNumMlts_Object = MibScalar
rcMltNumMlts = _RcMltNumMlts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 1),
    _RcMltNumMlts_Type()
)
rcMltNumMlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltNumMlts.setStatus("current")
_RcMltPotentialMembers_Type = PortSet
_RcMltPotentialMembers_Object = MibScalar
rcMltPotentialMembers = _RcMltPotentialMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 2),
    _RcMltPotentialMembers_Type()
)
rcMltPotentialMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltPotentialMembers.setStatus("current")
_RcMltIstSessionEnable_Type = EnableValue
_RcMltIstSessionEnable_Object = MibScalar
rcMltIstSessionEnable = _RcMltIstSessionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 3),
    _RcMltIstSessionEnable_Type()
)
rcMltIstSessionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltIstSessionEnable.setStatus("current")


class _RcMltIstSessionStatus_Type(Integer32):
    """Custom type rcMltIstSessionStatus based on Integer32"""
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


_RcMltIstSessionStatus_Type.__name__ = "Integer32"
_RcMltIstSessionStatus_Object = MibScalar
rcMltIstSessionStatus = _RcMltIstSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 4),
    _RcMltIstSessionStatus_Type()
)
rcMltIstSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltIstSessionStatus.setStatus("current")
_RcMltIstPeerIp_Type = IpAddress
_RcMltIstPeerIp_Object = MibScalar
rcMltIstPeerIp = _RcMltIstPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 5),
    _RcMltIstPeerIp_Type()
)
rcMltIstPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltIstPeerIp.setStatus("current")


class _RcMltIstVlanId_Type(Integer32):
    """Custom type rcMltIstVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RcMltIstVlanId_Type.__name__ = "Integer32"
_RcMltIstVlanId_Object = MibScalar
rcMltIstVlanId = _RcMltIstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 6),
    _RcMltIstVlanId_Type()
)
rcMltIstVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltIstVlanId.setStatus("current")
_RcMltDisablePortsOnShutdown_Type = TruthValue
_RcMltDisablePortsOnShutdown_Object = MibScalar
rcMltDisablePortsOnShutdown = _RcMltDisablePortsOnShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 7),
    _RcMltDisablePortsOnShutdown_Type()
)
rcMltDisablePortsOnShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltDisablePortsOnShutdown.setStatus("current")
_RcMltTable_Object = MibTable
rcMltTable = _RcMltTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10)
)
if mibBuilder.loadTexts:
    rcMltTable.setStatus("current")
_RcMltEntry_Object = MibTableRow
rcMltEntry = _RcMltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1)
)
rcMltEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcMltId"),
)
if mibBuilder.loadTexts:
    rcMltEntry.setStatus("current")


class _RcMltId_Type(Integer32):
    """Custom type rcMltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RcMltId_Type.__name__ = "Integer32"
_RcMltId_Object = MibTableColumn
rcMltId = _RcMltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 1),
    _RcMltId_Type()
)
rcMltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltId.setStatus("current")


class _RcMltName_Type(DisplayString):
    """Custom type rcMltName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcMltName_Type.__name__ = "DisplayString"
_RcMltName_Object = MibTableColumn
rcMltName = _RcMltName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 2),
    _RcMltName_Type()
)
rcMltName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltName.setStatus("current")
_RcMltPortMembers_Type = PortSet
_RcMltPortMembers_Object = MibTableColumn
rcMltPortMembers = _RcMltPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 3),
    _RcMltPortMembers_Type()
)
rcMltPortMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltPortMembers.setStatus("current")


class _RcMltPortType_Type(Integer32):
    """Custom type rcMltPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2))
    )


_RcMltPortType_Type.__name__ = "Integer32"
_RcMltPortType_Object = MibTableColumn
rcMltPortType = _RcMltPortType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 4),
    _RcMltPortType_Type()
)
rcMltPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltPortType.setStatus("current")
_RcMltNumVlanIds_Type = Integer32
_RcMltNumVlanIds_Object = MibTableColumn
rcMltNumVlanIds = _RcMltNumVlanIds_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 5),
    _RcMltNumVlanIds_Type()
)
rcMltNumVlanIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltNumVlanIds.setStatus("current")


class _RcMltVlanIds_Type(IdList):
    """Custom type rcMltVlanIds based on IdList"""
    subtypeSpec = IdList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_RcMltVlanIds_Type.__name__ = "IdList"
_RcMltVlanIds_Object = MibTableColumn
rcMltVlanIds = _RcMltVlanIds_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 6),
    _RcMltVlanIds_Type()
)
rcMltVlanIds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltVlanIds.setStatus("current")
_RcMltRowStatus_Type = RowStatus
_RcMltRowStatus_Object = MibTableColumn
rcMltRowStatus = _RcMltRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 7),
    _RcMltRowStatus_Type()
)
rcMltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltRowStatus.setStatus("current")


class _RcMltEnable_Type(TruthValue):
    """Custom type rcMltEnable based on TruthValue"""


_RcMltEnable_Object = MibTableColumn
rcMltEnable = _RcMltEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 8),
    _RcMltEnable_Type()
)
rcMltEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltEnable.setStatus("current")


class _RcMltLoadBalance_Type(TruthValue):
    """Custom type rcMltLoadBalance based on TruthValue"""


_RcMltLoadBalance_Object = MibTableColumn
rcMltLoadBalance = _RcMltLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 9),
    _RcMltLoadBalance_Type()
)
rcMltLoadBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltLoadBalance.setStatus("current")


class _RcMltDistributionAlgorithm_Type(Integer32):
    """Custom type rcMltDistributionAlgorithm based on Integer32"""
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
        *(("advanced", 3),
          ("basic", 2),
          ("none", 1))
    )


_RcMltDistributionAlgorithm_Type.__name__ = "Integer32"
_RcMltDistributionAlgorithm_Object = MibTableColumn
rcMltDistributionAlgorithm = _RcMltDistributionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 10),
    _RcMltDistributionAlgorithm_Type()
)
rcMltDistributionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltDistributionAlgorithm.setStatus("current")
_RcMltIfIndex_Type = InterfaceIndexOrZero
_RcMltIfIndex_Object = MibTableColumn
rcMltIfIndex = _RcMltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 11),
    _RcMltIfIndex_Type()
)
rcMltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltIfIndex.setStatus("current")


class _RcMltMltType_Type(Integer32):
    """Custom type rcMltMltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("istMLT", 2),
          ("normalMLT", 1),
          ("splitMLT", 3))
    )


_RcMltMltType_Type.__name__ = "Integer32"
_RcMltMltType_Object = MibTableColumn
rcMltMltType = _RcMltMltType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 12),
    _RcMltMltType_Type()
)
rcMltMltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltMltType.setStatus("current")


class _RcMltSmltId_Type(Integer32):
    """Custom type rcMltSmltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RcMltSmltId_Type.__name__ = "Integer32"
_RcMltSmltId_Object = MibTableColumn
rcMltSmltId = _RcMltSmltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 13),
    _RcMltSmltId_Type()
)
rcMltSmltId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltSmltId.setStatus("current")


class _RcMltRunningType_Type(Integer32):
    """Custom type rcMltRunningType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("istMLT", 2),
          ("normalMLT", 1),
          ("splitMLT", 3))
    )


_RcMltRunningType_Type.__name__ = "Integer32"
_RcMltRunningType_Object = MibTableColumn
rcMltRunningType = _RcMltRunningType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 14),
    _RcMltRunningType_Type()
)
rcMltRunningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltRunningType.setStatus("current")


class _RcMltSvlanPortType_Type(Integer32):
    """Custom type rcMltSvlanPortType based on Integer32"""
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
        *(("nni", 3),
          ("normal", 1),
          ("uni", 2))
    )


_RcMltSvlanPortType_Type.__name__ = "Integer32"
_RcMltSvlanPortType_Object = MibTableColumn
rcMltSvlanPortType = _RcMltSvlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 15),
    _RcMltSvlanPortType_Type()
)
rcMltSvlanPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltSvlanPortType.setStatus("current")


class _RcMltMulticastDistribution_Type(EnableValue):
    """Custom type rcMltMulticastDistribution based on EnableValue"""


_RcMltMulticastDistribution_Object = MibTableColumn
rcMltMulticastDistribution = _RcMltMulticastDistribution_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 16),
    _RcMltMulticastDistribution_Type()
)
rcMltMulticastDistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltMulticastDistribution.setStatus("current")


class _RcMltLacp10gBackup_Type(EnableValue):
    """Custom type rcMltLacp10gBackup based on EnableValue"""


_RcMltLacp10gBackup_Object = MibTableColumn
rcMltLacp10gBackup = _RcMltLacp10gBackup_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 17),
    _RcMltLacp10gBackup_Type()
)
rcMltLacp10gBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltLacp10gBackup.setStatus("current")


class _RcMltAggregatable_Type(EnableValue):
    """Custom type rcMltAggregatable based on EnableValue"""


_RcMltAggregatable_Object = MibTableColumn
rcMltAggregatable = _RcMltAggregatable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 18),
    _RcMltAggregatable_Type()
)
rcMltAggregatable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltAggregatable.setStatus("current")


class _RcMltClearLinkAggregate_Type(Integer32):
    """Custom type rcMltClearLinkAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_RcMltClearLinkAggregate_Type.__name__ = "Integer32"
_RcMltClearLinkAggregate_Object = MibTableColumn
rcMltClearLinkAggregate = _RcMltClearLinkAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 19),
    _RcMltClearLinkAggregate_Type()
)
rcMltClearLinkAggregate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltClearLinkAggregate.setStatus("current")


class _RcMltNtStgEnable_Type(TruthValue):
    """Custom type rcMltNtStgEnable based on TruthValue"""


_RcMltNtStgEnable_Object = MibTableColumn
rcMltNtStgEnable = _RcMltNtStgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 20),
    _RcMltNtStgEnable_Type()
)
rcMltNtStgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltNtStgEnable.setStatus("current")
_RcMltDesignatedPort_Type = InterfaceIndex
_RcMltDesignatedPort_Object = MibTableColumn
rcMltDesignatedPort = _RcMltDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 21),
    _RcMltDesignatedPort_Type()
)
rcMltDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltDesignatedPort.setStatus("current")
_RcMltAggOperState_Type = EnableValue
_RcMltAggOperState_Object = MibTableColumn
rcMltAggOperState = _RcMltAggOperState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 22),
    _RcMltAggOperState_Type()
)
rcMltAggOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltAggOperState.setStatus("current")
_RcMltAggTimeOfLastOperChange_Type = TimeTicks
_RcMltAggTimeOfLastOperChange_Object = MibTableColumn
rcMltAggTimeOfLastOperChange = _RcMltAggTimeOfLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 23),
    _RcMltAggTimeOfLastOperChange_Type()
)
rcMltAggTimeOfLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltAggTimeOfLastOperChange.setStatus("current")


class _RcMltVplsMgmtVlan_Type(EnableValue):
    """Custom type rcMltVplsMgmtVlan based on EnableValue"""


_RcMltVplsMgmtVlan_Object = MibTableColumn
rcMltVplsMgmtVlan = _RcMltVplsMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 24),
    _RcMltVplsMgmtVlan_Type()
)
rcMltVplsMgmtVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltVplsMgmtVlan.setStatus("current")


class _RcMltLoadDistributionOption_Type(Integer32):
    """Custom type rcMltLoadDistributionOption based on Integer32"""
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
        *(("bmac", 1),
          ("bvid", 3),
          ("cmac", 2),
          ("isid", 4))
    )


_RcMltLoadDistributionOption_Type.__name__ = "Integer32"
_RcMltLoadDistributionOption_Object = MibTableColumn
rcMltLoadDistributionOption = _RcMltLoadDistributionOption_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 25),
    _RcMltLoadDistributionOption_Type()
)
rcMltLoadDistributionOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltLoadDistributionOption.setStatus("current")


class _RcMltUniAggrMacIdx_Type(Integer32):
    """Custom type rcMltUniAggrMacIdx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 448),
    )


_RcMltUniAggrMacIdx_Type.__name__ = "Integer32"
_RcMltUniAggrMacIdx_Object = MibTableColumn
rcMltUniAggrMacIdx = _RcMltUniAggrMacIdx_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 26),
    _RcMltUniAggrMacIdx_Type()
)
rcMltUniAggrMacIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltUniAggrMacIdx.setStatus("current")
_RcMltUniAggrMacAddress_Type = MacAddress
_RcMltUniAggrMacAddress_Object = MibTableColumn
rcMltUniAggrMacAddress = _RcMltUniAggrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 27),
    _RcMltUniAggrMacAddress_Type()
)
rcMltUniAggrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltUniAggrMacAddress.setStatus("current")


class _RcMltQinqEtherType_Type(Integer32):
    """Custom type rcMltQinqEtherType based on Integer32"""
    defaultHexValue = 32800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMltQinqEtherType_Type.__name__ = "Integer32"
_RcMltQinqEtherType_Object = MibTableColumn
rcMltQinqEtherType = _RcMltQinqEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 28),
    _RcMltQinqEtherType_Type()
)
rcMltQinqEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltQinqEtherType.setStatus("current")


class _RcMltEgressCosProfileName_Type(DisplayString):
    """Custom type rcMltEgressCosProfileName based on DisplayString"""
    defaultValue = OctetString("DEFAULT_PORT_PROFILE")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RcMltEgressCosProfileName_Type.__name__ = "DisplayString"
_RcMltEgressCosProfileName_Object = MibTableColumn
rcMltEgressCosProfileName = _RcMltEgressCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 29),
    _RcMltEgressCosProfileName_Type()
)
rcMltEgressCosProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltEgressCosProfileName.setStatus("current")


class _RcMltEgressPolicerAdminState_Type(EnableValue):
    """Custom type rcMltEgressPolicerAdminState based on EnableValue"""


_RcMltEgressPolicerAdminState_Object = MibTableColumn
rcMltEgressPolicerAdminState = _RcMltEgressPolicerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 30),
    _RcMltEgressPolicerAdminState_Type()
)
rcMltEgressPolicerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltEgressPolicerAdminState.setStatus("current")


class _RcMltAggrEgressBandwidth_Type(EnableValue):
    """Custom type rcMltAggrEgressBandwidth based on EnableValue"""


_RcMltAggrEgressBandwidth_Object = MibTableColumn
rcMltAggrEgressBandwidth = _RcMltAggrEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 31),
    _RcMltAggrEgressBandwidth_Type()
)
rcMltAggrEgressBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltAggrEgressBandwidth.setStatus("current")


class _RcMltAggrIngressBandwidth_Type(EnableValue):
    """Custom type rcMltAggrIngressBandwidth based on EnableValue"""


_RcMltAggrIngressBandwidth_Object = MibTableColumn
rcMltAggrIngressBandwidth = _RcMltAggrIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 32),
    _RcMltAggrIngressBandwidth_Type()
)
rcMltAggrIngressBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltAggrIngressBandwidth.setStatus("current")


class _RcMltAggrMacAlloc_Type(EnableValue):
    """Custom type rcMltAggrMacAlloc based on EnableValue"""


_RcMltAggrMacAlloc_Object = MibTableColumn
rcMltAggrMacAlloc = _RcMltAggrMacAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 33),
    _RcMltAggrMacAlloc_Type()
)
rcMltAggrMacAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltAggrMacAlloc.setStatus("current")


class _RcMltAggMinLink_Type(Integer32):
    """Custom type rcMltAggMinLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcMltAggMinLink_Type.__name__ = "Integer32"
_RcMltAggMinLink_Object = MibTableColumn
rcMltAggMinLink = _RcMltAggMinLink_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 34),
    _RcMltAggMinLink_Type()
)
rcMltAggMinLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltAggMinLink.setStatus("current")


class _RcMltMtu_Type(Integer32):
    """Custom type rcMltMtu based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_RcMltMtu_Type.__name__ = "Integer32"
_RcMltMtu_Object = MibTableColumn
rcMltMtu = _RcMltMtu_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 35),
    _RcMltMtu_Type()
)
rcMltMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltMtu.setStatus("current")


class _RcMltInterfaceType_Type(Integer32):
    """Custom type rcMltInterfaceType based on Integer32"""
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
        *(("normal", 1),
          ("silent", 2),
          ("uni", 3))
    )


_RcMltInterfaceType_Type.__name__ = "Integer32"
_RcMltInterfaceType_Object = MibTableColumn
rcMltInterfaceType = _RcMltInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 36),
    _RcMltInterfaceType_Type()
)
rcMltInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltInterfaceType.setStatus("current")
_RcMltConfiguredMembers_Type = PortSet
_RcMltConfiguredMembers_Object = MibTableColumn
rcMltConfiguredMembers = _RcMltConfiguredMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 37),
    _RcMltConfiguredMembers_Type()
)
rcMltConfiguredMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltConfiguredMembers.setStatus("current")


class _RcMltMtuAdminState_Type(EnableValue):
    """Custom type rcMltMtuAdminState based on EnableValue"""


_RcMltMtuAdminState_Object = MibTableColumn
rcMltMtuAdminState = _RcMltMtuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 38),
    _RcMltMtuAdminState_Type()
)
rcMltMtuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltMtuAdminState.setStatus("current")
_RcMltPeerPortMembers_Type = PortSet
_RcMltPeerPortMembers_Object = MibTableColumn
rcMltPeerPortMembers = _RcMltPeerPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 39),
    _RcMltPeerPortMembers_Type()
)
rcMltPeerPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltPeerPortMembers.setStatus("current")


class _RcMltCpLimitPktRate_Type(Integer32):
    """Custom type rcMltCpLimitPktRate based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_RcMltCpLimitPktRate_Type.__name__ = "Integer32"
_RcMltCpLimitPktRate_Object = MibTableColumn
rcMltCpLimitPktRate = _RcMltCpLimitPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 40),
    _RcMltCpLimitPktRate_Type()
)
rcMltCpLimitPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltCpLimitPktRate.setStatus("current")


class _RcMltCpLimitShutDownEnable_Type(TruthValue):
    """Custom type rcMltCpLimitShutDownEnable based on TruthValue"""


_RcMltCpLimitShutDownEnable_Object = MibTableColumn
rcMltCpLimitShutDownEnable = _RcMltCpLimitShutDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 41),
    _RcMltCpLimitShutDownEnable_Type()
)
rcMltCpLimitShutDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltCpLimitShutDownEnable.setStatus("current")


class _RcMltVlanIdList_Type(OctetString):
    """Custom type rcMltVlanIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RcMltVlanIdList_Type.__name__ = "OctetString"
_RcMltVlanIdList_Object = MibTableColumn
rcMltVlanIdList = _RcMltVlanIdList_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 42),
    _RcMltVlanIdList_Type()
)
rcMltVlanIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltVlanIdList.setStatus("current")


class _RcMltEntryOwner_Type(Integer32):
    """Custom type rcMltEntryOwner based on Integer32"""
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
        *(("local", 2),
          ("localAndRemote", 4),
          ("none", 1),
          ("remote", 3))
    )


_RcMltEntryOwner_Type.__name__ = "Integer32"
_RcMltEntryOwner_Object = MibTableColumn
rcMltEntryOwner = _RcMltEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 43),
    _RcMltEntryOwner_Type()
)
rcMltEntryOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltEntryOwner.setStatus("current")


class _RcMltDatapathProgrammingState_Type(Integer32):
    """Custom type rcMltDatapathProgrammingState based on Integer32"""
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
        *(("local", 2),
          ("localAndRemote", 4),
          ("none", 1),
          ("remote", 3))
    )


_RcMltDatapathProgrammingState_Type.__name__ = "Integer32"
_RcMltDatapathProgrammingState_Object = MibTableColumn
rcMltDatapathProgrammingState = _RcMltDatapathProgrammingState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 10, 1, 44),
    _RcMltDatapathProgrammingState_Type()
)
rcMltDatapathProgrammingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMltDatapathProgrammingState.setStatus("current")
_RcMltMcastDistribution_ObjectIdentity = ObjectIdentity
rcMltMcastDistribution = _RcMltMcastDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 11)
)
_RcMltMcastDistributionEnable_Type = TruthValue
_RcMltMcastDistributionEnable_Object = MibScalar
rcMltMcastDistributionEnable = _RcMltMcastDistributionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 11, 1),
    _RcMltMcastDistributionEnable_Type()
)
rcMltMcastDistributionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltMcastDistributionEnable.setStatus("current")
_RcMltMcastDistributionGrpMask_Type = IpAddress
_RcMltMcastDistributionGrpMask_Object = MibScalar
rcMltMcastDistributionGrpMask = _RcMltMcastDistributionGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 11, 2),
    _RcMltMcastDistributionGrpMask_Type()
)
rcMltMcastDistributionGrpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltMcastDistributionGrpMask.setStatus("current")
_RcMltMcastDistributionSrcMask_Type = IpAddress
_RcMltMcastDistributionSrcMask_Object = MibScalar
rcMltMcastDistributionSrcMask = _RcMltMcastDistributionSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 11, 3),
    _RcMltMcastDistributionSrcMask_Type()
)
rcMltMcastDistributionSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltMcastDistributionSrcMask.setStatus("current")
_RcMltMcastDistributionRedistributionEnable_Type = TruthValue
_RcMltMcastDistributionRedistributionEnable_Object = MibScalar
rcMltMcastDistributionRedistributionEnable = _RcMltMcastDistributionRedistributionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 11, 4),
    _RcMltMcastDistributionRedistributionEnable_Type()
)
rcMltMcastDistributionRedistributionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltMcastDistributionRedistributionEnable.setStatus("current")
_RcSltPortTable_Object = MibTable
rcSltPortTable = _RcSltPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 12)
)
if mibBuilder.loadTexts:
    rcSltPortTable.setStatus("current")
_RcSltPortEntry_Object = MibTableRow
rcSltPortEntry = _RcSltPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 12, 1)
)
rcSltPortEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcSltPortIfIndex"),
)
if mibBuilder.loadTexts:
    rcSltPortEntry.setStatus("current")
_RcSltPortIfIndex_Type = InterfaceIndex
_RcSltPortIfIndex_Object = MibTableColumn
rcSltPortIfIndex = _RcSltPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 12, 1, 1),
    _RcSltPortIfIndex_Type()
)
rcSltPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSltPortIfIndex.setStatus("current")


class _RcSltPortSmltId_Type(Integer32):
    """Custom type rcSltPortSmltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RcSltPortSmltId_Type.__name__ = "Integer32"
_RcSltPortSmltId_Object = MibTableColumn
rcSltPortSmltId = _RcSltPortSmltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 12, 1, 2),
    _RcSltPortSmltId_Type()
)
rcSltPortSmltId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcSltPortSmltId.setStatus("current")


class _RcSltPortOperType_Type(Integer32):
    """Custom type rcSltPortOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("smlt", 2))
    )


_RcSltPortOperType_Type.__name__ = "Integer32"
_RcSltPortOperType_Object = MibTableColumn
rcSltPortOperType = _RcSltPortOperType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 12, 1, 3),
    _RcSltPortOperType_Type()
)
rcSltPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSltPortOperType.setStatus("current")
_RcSltPortRowStatus_Type = RowStatus
_RcSltPortRowStatus_Object = MibTableColumn
rcSltPortRowStatus = _RcSltPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 12, 1, 4),
    _RcSltPortRowStatus_Type()
)
rcSltPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcSltPortRowStatus.setStatus("current")
_RcMltVlacpTable_Object = MibTable
rcMltVlacpTable = _RcMltVlacpTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13)
)
if mibBuilder.loadTexts:
    rcMltVlacpTable.setStatus("current")
_RcMltVlacpEntry_Object = MibTableRow
rcMltVlacpEntry = _RcMltVlacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13, 1)
)
rcMltVlacpEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcMltId"),
)
if mibBuilder.loadTexts:
    rcMltVlacpEntry.setStatus("current")


class _RcMltVlacpAdminEnable_Type(TruthValue):
    """Custom type rcMltVlacpAdminEnable based on TruthValue"""


_RcMltVlacpAdminEnable_Object = MibTableColumn
rcMltVlacpAdminEnable = _RcMltVlacpAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13, 1, 1),
    _RcMltVlacpAdminEnable_Type()
)
rcMltVlacpAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltVlacpAdminEnable.setStatus("current")


class _RcMltVlacpFastPeriodicTimer_Type(Integer32):
    """Custom type rcMltVlacpFastPeriodicTimer based on Integer32"""
    defaultValue = 250


_RcMltVlacpFastPeriodicTimer_Object = MibTableColumn
rcMltVlacpFastPeriodicTimer = _RcMltVlacpFastPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13, 1, 2),
    _RcMltVlacpFastPeriodicTimer_Type()
)
rcMltVlacpFastPeriodicTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltVlacpFastPeriodicTimer.setStatus("current")


class _RcMltVlacpTimeoutScale_Type(Integer32):
    """Custom type rcMltVlacpTimeoutScale based on Integer32"""
    defaultValue = 3


_RcMltVlacpTimeoutScale_Object = MibTableColumn
rcMltVlacpTimeoutScale = _RcMltVlacpTimeoutScale_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13, 1, 3),
    _RcMltVlacpTimeoutScale_Type()
)
rcMltVlacpTimeoutScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltVlacpTimeoutScale.setStatus("current")
_RcMltVlacpEtherMacAddress_Type = MacAddress
_RcMltVlacpEtherMacAddress_Object = MibTableColumn
rcMltVlacpEtherMacAddress = _RcMltVlacpEtherMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13, 1, 4),
    _RcMltVlacpEtherMacAddress_Type()
)
rcMltVlacpEtherMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltVlacpEtherMacAddress.setStatus("current")


class _RcMltVlacpDualHomingEnable_Type(TruthValue):
    """Custom type rcMltVlacpDualHomingEnable based on TruthValue"""


_RcMltVlacpDualHomingEnable_Object = MibTableColumn
rcMltVlacpDualHomingEnable = _RcMltVlacpDualHomingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 13, 1, 5),
    _RcMltVlacpDualHomingEnable_Type()
)
rcMltVlacpDualHomingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMltVlacpDualHomingEnable.setStatus("current")
_RcMltBvidPortTable_Object = MibTable
rcMltBvidPortTable = _RcMltBvidPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14)
)
if mibBuilder.loadTexts:
    rcMltBvidPortTable.setStatus("current")
_RcMltBvidPortEntry_Object = MibTableRow
rcMltBvidPortEntry = _RcMltBvidPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14, 1)
)
rcMltBvidPortEntry.setIndexNames(
    (0, "RC-MLT-MIB", "rcMltBvidMltId"),
    (0, "RC-MLT-MIB", "rcMltBvidVlanId"),
)
if mibBuilder.loadTexts:
    rcMltBvidPortEntry.setStatus("current")


class _RcMltBvidMltId_Type(Integer32):
    """Custom type rcMltBvidMltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RcMltBvidMltId_Type.__name__ = "Integer32"
_RcMltBvidMltId_Object = MibTableColumn
rcMltBvidMltId = _RcMltBvidMltId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14, 1, 1),
    _RcMltBvidMltId_Type()
)
rcMltBvidMltId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMltBvidMltId.setStatus("current")


class _RcMltBvidVlanId_Type(Integer32):
    """Custom type rcMltBvidVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_RcMltBvidVlanId_Type.__name__ = "Integer32"
_RcMltBvidVlanId_Object = MibTableColumn
rcMltBvidVlanId = _RcMltBvidVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14, 1, 2),
    _RcMltBvidVlanId_Type()
)
rcMltBvidVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMltBvidVlanId.setStatus("current")
_RcMltBvidPrimaryPort_Type = InterfaceIndex
_RcMltBvidPrimaryPort_Object = MibTableColumn
rcMltBvidPrimaryPort = _RcMltBvidPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14, 1, 3),
    _RcMltBvidPrimaryPort_Type()
)
rcMltBvidPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltBvidPrimaryPort.setStatus("current")
_RcMltBvidSecondaryPort_Type = InterfaceIndex
_RcMltBvidSecondaryPort_Object = MibTableColumn
rcMltBvidSecondaryPort = _RcMltBvidSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14, 1, 4),
    _RcMltBvidSecondaryPort_Type()
)
rcMltBvidSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltBvidSecondaryPort.setStatus("current")
_RcMltBvidRowStatus_Type = RowStatus
_RcMltBvidRowStatus_Object = MibTableColumn
rcMltBvidRowStatus = _RcMltBvidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 14, 1, 5),
    _RcMltBvidRowStatus_Type()
)
rcMltBvidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMltBvidRowStatus.setStatus("current")
_RcMltNotificationObjects_ObjectIdentity = ObjectIdentity
rcMltNotificationObjects = _RcMltNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 15)
)


class _RcMltAggTrapEvent_Type(Integer32):
    """Custom type rcMltAggTrapEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localdown", 1),
          ("remotedown", 2),
          ("up", 3))
    )


_RcMltAggTrapEvent_Type.__name__ = "Integer32"
_RcMltAggTrapEvent_Object = MibScalar
rcMltAggTrapEvent = _RcMltAggTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 17, 15, 1),
    _RcMltAggTrapEvent_Type()
)
rcMltAggTrapEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rcMltAggTrapEvent.setStatus("current")
_RcLinkFlapDetectAutoPortDownEnable_Type = TruthValue
_RcLinkFlapDetectAutoPortDownEnable_Object = MibScalar
rcLinkFlapDetectAutoPortDownEnable = _RcLinkFlapDetectAutoPortDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 27, 1),
    _RcLinkFlapDetectAutoPortDownEnable_Type()
)
rcLinkFlapDetectAutoPortDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkFlapDetectAutoPortDownEnable.setStatus("current")
_RcLinkFlapDetectSendTrap_Type = TruthValue
_RcLinkFlapDetectSendTrap_Object = MibScalar
rcLinkFlapDetectSendTrap = _RcLinkFlapDetectSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 27, 2),
    _RcLinkFlapDetectSendTrap_Type()
)
rcLinkFlapDetectSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkFlapDetectSendTrap.setStatus("current")


class _RcLinkFlapDetectFrequency_Type(Integer32):
    """Custom type rcLinkFlapDetectFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_RcLinkFlapDetectFrequency_Type.__name__ = "Integer32"
_RcLinkFlapDetectFrequency_Object = MibScalar
rcLinkFlapDetectFrequency = _RcLinkFlapDetectFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 27, 3),
    _RcLinkFlapDetectFrequency_Type()
)
rcLinkFlapDetectFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkFlapDetectFrequency.setStatus("current")


class _RcLinkFlapDetectInterval_Type(Integer32):
    """Custom type rcLinkFlapDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 600),
    )


_RcLinkFlapDetectInterval_Type.__name__ = "Integer32"
_RcLinkFlapDetectInterval_Object = MibScalar
rcLinkFlapDetectInterval = _RcLinkFlapDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 27, 4),
    _RcLinkFlapDetectInterval_Type()
)
rcLinkFlapDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkFlapDetectInterval.setStatus("current")


class _RcL2RedundancyHaCpuState_Type(Integer32):
    """Custom type rcL2RedundancyHaCpuState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("disabled", 6),
          ("error", 5),
          ("initialization", 0),
          ("lostPeerConnection", 9),
          ("notSynchronized", 10),
          ("oneWayActive", 1),
          ("peerConnected", 8),
          ("peerNotConnected", 7),
          ("remoteIncompatible", 4),
          ("synchronizeInProgress", 11),
          ("synchronized", 3),
          ("twoWayActive", 2))
    )


_RcL2RedundancyHaCpuState_Type.__name__ = "Integer32"
_RcL2RedundancyHaCpuState_Object = MibScalar
rcL2RedundancyHaCpuState = _RcL2RedundancyHaCpuState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 32, 1),
    _RcL2RedundancyHaCpuState_Type()
)
rcL2RedundancyHaCpuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL2RedundancyHaCpuState.setStatus("current")


class _RcL2RedundancyHaEvent_Type(Integer32):
    """Custom type rcL2RedundancyHaEvent based on Integer32"""
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
        *(("noEvent", 4),
          ("restart", 0),
          ("systemRegistrationDone", 1),
          ("tableSynchronizationDone", 2),
          ("versionIncompatible", 3))
    )


_RcL2RedundancyHaEvent_Type.__name__ = "Integer32"
_RcL2RedundancyHaEvent_Object = MibScalar
rcL2RedundancyHaEvent = _RcL2RedundancyHaEvent_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 32, 2),
    _RcL2RedundancyHaEvent_Type()
)
rcL2RedundancyHaEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL2RedundancyHaEvent.setStatus("current")
_RcL2RedundancyEnable_Type = EnableValue
_RcL2RedundancyEnable_Object = MibScalar
rcL2RedundancyEnable = _RcL2RedundancyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 32, 3),
    _RcL2RedundancyEnable_Type()
)
rcL2RedundancyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2RedundancyEnable.setStatus("current")


class _RcL2RedundancyStandbyCpu_Type(Integer32):
    """Custom type rcL2RedundancyStandbyCpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotStandbyCPU", 1),
          ("standbyCPUNotPresent", 3),
          ("warmStandbyCPU", 2))
    )


_RcL2RedundancyStandbyCpu_Type.__name__ = "Integer32"
_RcL2RedundancyStandbyCpu_Object = MibScalar
rcL2RedundancyStandbyCpu = _RcL2RedundancyStandbyCpu_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 32, 4),
    _RcL2RedundancyStandbyCpu_Type()
)
rcL2RedundancyStandbyCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL2RedundancyStandbyCpu.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-MLT-MIB",
    **{"rcStatMlt": rcStatMlt,
       "rcStatMltIfExtnTable": rcStatMltIfExtnTable,
       "rcStatMltIfExtnEntry": rcStatMltIfExtnEntry,
       "rcStatMltIfExtnMltId": rcStatMltIfExtnMltId,
       "rcStatMltIfExtnIfInMulticastPkts": rcStatMltIfExtnIfInMulticastPkts,
       "rcStatMltIfExtnIfInBroadcastPkts": rcStatMltIfExtnIfInBroadcastPkts,
       "rcStatMltIfExtnIfOutMulticastPkts": rcStatMltIfExtnIfOutMulticastPkts,
       "rcStatMltIfExtnIfOutBroadcastPkts": rcStatMltIfExtnIfOutBroadcastPkts,
       "rcStatMltIfExtnIfHCInOctets": rcStatMltIfExtnIfHCInOctets,
       "rcStatMltIfExtnIfHCInUcastPkts": rcStatMltIfExtnIfHCInUcastPkts,
       "rcStatMltIfExtnIfHCInMulticastPkt": rcStatMltIfExtnIfHCInMulticastPkt,
       "rcStatMltIfExtnIfHCInBroadcastPkt": rcStatMltIfExtnIfHCInBroadcastPkt,
       "rcStatMltIfExtnIfHCOutOctets": rcStatMltIfExtnIfHCOutOctets,
       "rcStatMltIfExtnIfHCOutUcastPkts": rcStatMltIfExtnIfHCOutUcastPkts,
       "rcStatMltIfExtnIfHCOutMulticast": rcStatMltIfExtnIfHCOutMulticast,
       "rcStatMltIfExtnIfHCOutBroadcast": rcStatMltIfExtnIfHCOutBroadcast,
       "rcStatMltEtherTable": rcStatMltEtherTable,
       "rcStatMltEtherEntry": rcStatMltEtherEntry,
       "rcStatMltEtherMltId": rcStatMltEtherMltId,
       "rcStatMltEtherAlignmentErrors": rcStatMltEtherAlignmentErrors,
       "rcStatMltEtherFCSErrors": rcStatMltEtherFCSErrors,
       "rcStatMltEtherSingleCollFrames": rcStatMltEtherSingleCollFrames,
       "rcStatMltEtherMultipleCollFrames": rcStatMltEtherMultipleCollFrames,
       "rcStatMltEtherSQETestError": rcStatMltEtherSQETestError,
       "rcStatMltEtherDeferredTransmiss": rcStatMltEtherDeferredTransmiss,
       "rcStatMltEtherLateCollisions": rcStatMltEtherLateCollisions,
       "rcStatMltEtherExcessiveCollis": rcStatMltEtherExcessiveCollis,
       "rcStatMltEtherIMacTransmitError": rcStatMltEtherIMacTransmitError,
       "rcStatMltEtherCarrierSenseError": rcStatMltEtherCarrierSenseError,
       "rcStatMltEtherFrameTooLong": rcStatMltEtherFrameTooLong,
       "rcStatMltEtherIMacReceiveError": rcStatMltEtherIMacReceiveError,
       "rcStatMltIpTable": rcStatMltIpTable,
       "rcStatMltIpEntry": rcStatMltIpEntry,
       "rcStatMltIpMltId": rcStatMltIpMltId,
       "rcStatMltIpInReceives": rcStatMltIpInReceives,
       "rcStatMltIpInHdrErrors": rcStatMltIpInHdrErrors,
       "rcStatMltIpInAddrErrors": rcStatMltIpInAddrErrors,
       "rcStatMltIpForwDatagrams": rcStatMltIpForwDatagrams,
       "rcStatMltIpInUnknownProtos": rcStatMltIpInUnknownProtos,
       "rcStatMltIpInDiscards": rcStatMltIpInDiscards,
       "rcStatMltIpInDelivers": rcStatMltIpInDelivers,
       "rcStatMltIpOutRequest": rcStatMltIpOutRequest,
       "rcStatMltIpOutDiscards": rcStatMltIpOutDiscards,
       "rcStatMltIpOutNoRoutes": rcStatMltIpOutNoRoutes,
       "rcStatMltIpReasmReqds": rcStatMltIpReasmReqds,
       "rcStatMltIpReasmOKs": rcStatMltIpReasmOKs,
       "rcStatMltIpReasmFails": rcStatMltIpReasmFails,
       "rcStatMltIpFragOKs": rcStatMltIpFragOKs,
       "rcStatMltIpFragFails": rcStatMltIpFragFails,
       "rcStatMltIpFragCreates": rcStatMltIpFragCreates,
       "rcStatMltIpRoutingDiscards": rcStatMltIpRoutingDiscards,
       "rcStatSmltIstDownCnt": rcStatSmltIstDownCnt,
       "rcStatSmltHelloTxMsgCnt": rcStatSmltHelloTxMsgCnt,
       "rcStatSmltHelloRxMsgCnt": rcStatSmltHelloRxMsgCnt,
       "rcStatSmltLearnMacAddrTxMsgCnt": rcStatSmltLearnMacAddrTxMsgCnt,
       "rcStatSmltLearnMacAddrRxMsgCnt": rcStatSmltLearnMacAddrRxMsgCnt,
       "rcStatSmltMacAddrAgeOutTxMsgCnt": rcStatSmltMacAddrAgeOutTxMsgCnt,
       "rcStatSmltMacAddrAgeOutRxMsgCnt": rcStatSmltMacAddrAgeOutRxMsgCnt,
       "rcStatSmltMacAddrAgeExpTxMsgCnt": rcStatSmltMacAddrAgeExpTxMsgCnt,
       "rcStatSmltMacAddrAgeExpRxMsgCnt": rcStatSmltMacAddrAgeExpRxMsgCnt,
       "rcStatSmltStgInfoTxMsgCnt": rcStatSmltStgInfoTxMsgCnt,
       "rcStatSmltStgInfoRxMsgCnt": rcStatSmltStgInfoRxMsgCnt,
       "rcStatSmltDelMacAddrTxMsgCnt": rcStatSmltDelMacAddrTxMsgCnt,
       "rcStatSmltDelMacAddrRxMsgCnt": rcStatSmltDelMacAddrRxMsgCnt,
       "rcStatSmltSmltDownTxMsgCnt": rcStatSmltSmltDownTxMsgCnt,
       "rcStatSmltSmltDownRxMsgCnt": rcStatSmltSmltDownRxMsgCnt,
       "rcStatSmltSmltUpTxMsgCnt": rcStatSmltSmltUpTxMsgCnt,
       "rcStatSmltSmltUpRxMsgCnt": rcStatSmltSmltUpRxMsgCnt,
       "rcStatSmltSendMacTblTxMsgCnt": rcStatSmltSendMacTblTxMsgCnt,
       "rcStatSmltSendMacTblRxMsgCnt": rcStatSmltSendMacTblRxMsgCnt,
       "rcStatSmltIgmpTxMsgCnt": rcStatSmltIgmpTxMsgCnt,
       "rcStatSmltIgmpRxMsgCnt": rcStatSmltIgmpRxMsgCnt,
       "rcStatSmltPortDownTxMsgCnt": rcStatSmltPortDownTxMsgCnt,
       "rcStatSmltPortDownRxMsgCnt": rcStatSmltPortDownRxMsgCnt,
       "rcStatSmltReqMacTblTxMsgCnt": rcStatSmltReqMacTblTxMsgCnt,
       "rcStatSmltReqMacTblRxMsgCnt": rcStatSmltReqMacTblRxMsgCnt,
       "rcStatSmltRxUnknownMsgTypeCnt": rcStatSmltRxUnknownMsgTypeCnt,
       "rcStatMltIfUtilTable": rcStatMltIfUtilTable,
       "rcStatMltIfUtilEntry": rcStatMltIfUtilEntry,
       "rcStatMltIfUtilMltId": rcStatMltIfUtilMltId,
       "rcStatMltIfUtilIfHCInOctets": rcStatMltIfUtilIfHCInOctets,
       "rcStatMltIfUtilIfHCInUtil": rcStatMltIfUtilIfHCInUtil,
       "rcStatMltIfUtilIfHCOutOctets": rcStatMltIfUtilIfHCOutOctets,
       "rcStatMltIfUtilIfHCOutUtil": rcStatMltIfUtilIfHCOutUtil,
       "rcStatSmltLacpInfoRxMsgCnt": rcStatSmltLacpInfoRxMsgCnt,
       "rcStatSmltLacpInfoTxMsgCnt": rcStatSmltLacpInfoTxMsgCnt,
       "rcStatMltUtilTable": rcStatMltUtilTable,
       "rcStatMltUtilEntry": rcStatMltUtilEntry,
       "rcStatMltUtilPortIfIndex": rcStatMltUtilPortIfIndex,
       "rcStatMltUtilTrafficType": rcStatMltUtilTrafficType,
       "rcStatMltUtilTrafficLast5Min": rcStatMltUtilTrafficLast5Min,
       "rcStatMltUtilTrafficLast30Min": rcStatMltUtilTrafficLast30Min,
       "rcStatMltUtilTrafficLast1Hour": rcStatMltUtilTrafficLast1Hour,
       "rcMltMib": rcMltMib,
       "rcMltNumMlts": rcMltNumMlts,
       "rcMltPotentialMembers": rcMltPotentialMembers,
       "rcMltIstSessionEnable": rcMltIstSessionEnable,
       "rcMltIstSessionStatus": rcMltIstSessionStatus,
       "rcMltIstPeerIp": rcMltIstPeerIp,
       "rcMltIstVlanId": rcMltIstVlanId,
       "rcMltDisablePortsOnShutdown": rcMltDisablePortsOnShutdown,
       "rcMltTable": rcMltTable,
       "rcMltEntry": rcMltEntry,
       "rcMltId": rcMltId,
       "rcMltName": rcMltName,
       "rcMltPortMembers": rcMltPortMembers,
       "rcMltPortType": rcMltPortType,
       "rcMltNumVlanIds": rcMltNumVlanIds,
       "rcMltVlanIds": rcMltVlanIds,
       "rcMltRowStatus": rcMltRowStatus,
       "rcMltEnable": rcMltEnable,
       "rcMltLoadBalance": rcMltLoadBalance,
       "rcMltDistributionAlgorithm": rcMltDistributionAlgorithm,
       "rcMltIfIndex": rcMltIfIndex,
       "rcMltMltType": rcMltMltType,
       "rcMltSmltId": rcMltSmltId,
       "rcMltRunningType": rcMltRunningType,
       "rcMltSvlanPortType": rcMltSvlanPortType,
       "rcMltMulticastDistribution": rcMltMulticastDistribution,
       "rcMltLacp10gBackup": rcMltLacp10gBackup,
       "rcMltAggregatable": rcMltAggregatable,
       "rcMltClearLinkAggregate": rcMltClearLinkAggregate,
       "rcMltNtStgEnable": rcMltNtStgEnable,
       "rcMltDesignatedPort": rcMltDesignatedPort,
       "rcMltAggOperState": rcMltAggOperState,
       "rcMltAggTimeOfLastOperChange": rcMltAggTimeOfLastOperChange,
       "rcMltVplsMgmtVlan": rcMltVplsMgmtVlan,
       "rcMltLoadDistributionOption": rcMltLoadDistributionOption,
       "rcMltUniAggrMacIdx": rcMltUniAggrMacIdx,
       "rcMltUniAggrMacAddress": rcMltUniAggrMacAddress,
       "rcMltQinqEtherType": rcMltQinqEtherType,
       "rcMltEgressCosProfileName": rcMltEgressCosProfileName,
       "rcMltEgressPolicerAdminState": rcMltEgressPolicerAdminState,
       "rcMltAggrEgressBandwidth": rcMltAggrEgressBandwidth,
       "rcMltAggrIngressBandwidth": rcMltAggrIngressBandwidth,
       "rcMltAggrMacAlloc": rcMltAggrMacAlloc,
       "rcMltAggMinLink": rcMltAggMinLink,
       "rcMltMtu": rcMltMtu,
       "rcMltInterfaceType": rcMltInterfaceType,
       "rcMltConfiguredMembers": rcMltConfiguredMembers,
       "rcMltMtuAdminState": rcMltMtuAdminState,
       "rcMltPeerPortMembers": rcMltPeerPortMembers,
       "rcMltCpLimitPktRate": rcMltCpLimitPktRate,
       "rcMltCpLimitShutDownEnable": rcMltCpLimitShutDownEnable,
       "rcMltVlanIdList": rcMltVlanIdList,
       "rcMltEntryOwner": rcMltEntryOwner,
       "rcMltDatapathProgrammingState": rcMltDatapathProgrammingState,
       "rcMltMcastDistribution": rcMltMcastDistribution,
       "rcMltMcastDistributionEnable": rcMltMcastDistributionEnable,
       "rcMltMcastDistributionGrpMask": rcMltMcastDistributionGrpMask,
       "rcMltMcastDistributionSrcMask": rcMltMcastDistributionSrcMask,
       "rcMltMcastDistributionRedistributionEnable": rcMltMcastDistributionRedistributionEnable,
       "rcSltPortTable": rcSltPortTable,
       "rcSltPortEntry": rcSltPortEntry,
       "rcSltPortIfIndex": rcSltPortIfIndex,
       "rcSltPortSmltId": rcSltPortSmltId,
       "rcSltPortOperType": rcSltPortOperType,
       "rcSltPortRowStatus": rcSltPortRowStatus,
       "rcMltVlacpTable": rcMltVlacpTable,
       "rcMltVlacpEntry": rcMltVlacpEntry,
       "rcMltVlacpAdminEnable": rcMltVlacpAdminEnable,
       "rcMltVlacpFastPeriodicTimer": rcMltVlacpFastPeriodicTimer,
       "rcMltVlacpTimeoutScale": rcMltVlacpTimeoutScale,
       "rcMltVlacpEtherMacAddress": rcMltVlacpEtherMacAddress,
       "rcMltVlacpDualHomingEnable": rcMltVlacpDualHomingEnable,
       "rcMltBvidPortTable": rcMltBvidPortTable,
       "rcMltBvidPortEntry": rcMltBvidPortEntry,
       "rcMltBvidMltId": rcMltBvidMltId,
       "rcMltBvidVlanId": rcMltBvidVlanId,
       "rcMltBvidPrimaryPort": rcMltBvidPrimaryPort,
       "rcMltBvidSecondaryPort": rcMltBvidSecondaryPort,
       "rcMltBvidRowStatus": rcMltBvidRowStatus,
       "rcMltNotificationObjects": rcMltNotificationObjects,
       "rcMltAggTrapEvent": rcMltAggTrapEvent,
       "rcLinkFlapDetectAutoPortDownEnable": rcLinkFlapDetectAutoPortDownEnable,
       "rcLinkFlapDetectSendTrap": rcLinkFlapDetectSendTrap,
       "rcLinkFlapDetectFrequency": rcLinkFlapDetectFrequency,
       "rcLinkFlapDetectInterval": rcLinkFlapDetectInterval,
       "rcL2RedundancyHaCpuState": rcL2RedundancyHaCpuState,
       "rcL2RedundancyHaEvent": rcL2RedundancyHaEvent,
       "rcL2RedundancyEnable": rcL2RedundancyEnable,
       "rcL2RedundancyStandbyCpu": rcL2RedundancyStandbyCpu}
)
