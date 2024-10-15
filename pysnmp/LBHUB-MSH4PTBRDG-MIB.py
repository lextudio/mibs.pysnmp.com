# SNMP MIB module (LBHUB-MSH4PTBRDG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LBHUB-MSH4PTBRDG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:28 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 experimental,
 internet,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "experimental",
    "internet",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5)
)
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7)
)
_Dot3Table_Object = MibTable
dot3Table = _Dot3Table_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1)
)
if mibBuilder.loadTexts:
    dot3Table.setStatus("mandatory")
_Dot3Entry_Object = MibTableRow
dot3Entry = _Dot3Entry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1)
)
dot3Entry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "dot3Index"),
)
if mibBuilder.loadTexts:
    dot3Entry.setStatus("mandatory")
_Dot3Index_Type = Integer32
_Dot3Index_Object = MibTableColumn
dot3Index = _Dot3Index_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 1),
    _Dot3Index_Type()
)
dot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3Index.setStatus("mandatory")


class _Dot3InitializeMac_Type(Integer32):
    """Custom type dot3InitializeMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 1),
          ("uninitialized", 2))
    )


_Dot3InitializeMac_Type.__name__ = "Integer32"
_Dot3InitializeMac_Object = MibTableColumn
dot3InitializeMac = _Dot3InitializeMac_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 2),
    _Dot3InitializeMac_Type()
)
dot3InitializeMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3InitializeMac.setStatus("mandatory")


class _Dot3MacSubLayerStatus_Type(Integer32):
    """Custom type dot3MacSubLayerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Dot3MacSubLayerStatus_Type.__name__ = "Integer32"
_Dot3MacSubLayerStatus_Object = MibTableColumn
dot3MacSubLayerStatus = _Dot3MacSubLayerStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 3),
    _Dot3MacSubLayerStatus_Type()
)
dot3MacSubLayerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MacSubLayerStatus.setStatus("mandatory")


class _Dot3MulticastReceiveStatus_Type(Integer32):
    """Custom type dot3MulticastReceiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Dot3MulticastReceiveStatus_Type.__name__ = "Integer32"
_Dot3MulticastReceiveStatus_Object = MibTableColumn
dot3MulticastReceiveStatus = _Dot3MulticastReceiveStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 4),
    _Dot3MulticastReceiveStatus_Type()
)
dot3MulticastReceiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MulticastReceiveStatus.setStatus("mandatory")


class _Dot3TxEnabled_Type(Integer32):
    """Custom type dot3TxEnabled based on Integer32"""
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


_Dot3TxEnabled_Type.__name__ = "Integer32"
_Dot3TxEnabled_Object = MibTableColumn
dot3TxEnabled = _Dot3TxEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 5),
    _Dot3TxEnabled_Type()
)
dot3TxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3TxEnabled.setStatus("mandatory")
_Dot3TestTdrValue_Type = Gauge32
_Dot3TestTdrValue_Object = MibTableColumn
dot3TestTdrValue = _Dot3TestTdrValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 6),
    _Dot3TestTdrValue_Type()
)
dot3TestTdrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TestTdrValue.setStatus("mandatory")
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("mandatory")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("mandatory")
_Dot3StatsIndex_Type = Integer32
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("mandatory")
_Dot3StatsAlignmentErrors_Type = Counter32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("mandatory")
_Dot3StatsFCSErrors_Type = Counter32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("mandatory")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("mandatory")
_Dot3StatsMultipleCollisionFrames_Type = Counter32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("mandatory")
_Dot3StatsSQETestErrors_Type = Counter32
_Dot3StatsSQETestErrors_Object = MibTableColumn
dot3StatsSQETestErrors = _Dot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6),
    _Dot3StatsSQETestErrors_Type()
)
dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setStatus("mandatory")
_Dot3StatsDeferredTransmissions_Type = Counter32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("mandatory")
_Dot3StatsLateCollisions_Type = Counter32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("mandatory")
_Dot3StatsExcessiveCollisions_Type = Counter32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("mandatory")
_Dot3StatsInternalMacTransmitErrors_Type = Counter32
_Dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
dot3StatsInternalMacTransmitErrors = _Dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10),
    _Dot3StatsInternalMacTransmitErrors_Type()
)
dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setStatus("mandatory")
_Dot3StatsCarrierSenseErrors_Type = Counter32
_Dot3StatsCarrierSenseErrors_Object = MibTableColumn
dot3StatsCarrierSenseErrors = _Dot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11),
    _Dot3StatsCarrierSenseErrors_Type()
)
dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setStatus("mandatory")
_Dot3StatsExcessiveDeferrals_Type = Counter32
_Dot3StatsExcessiveDeferrals_Object = MibTableColumn
dot3StatsExcessiveDeferrals = _Dot3StatsExcessiveDeferrals_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 12),
    _Dot3StatsExcessiveDeferrals_Type()
)
dot3StatsExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveDeferrals.setStatus("mandatory")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("mandatory")
_Dot3StatsInRangeLengthErrors_Type = Counter32
_Dot3StatsInRangeLengthErrors_Object = MibTableColumn
dot3StatsInRangeLengthErrors = _Dot3StatsInRangeLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 14),
    _Dot3StatsInRangeLengthErrors_Type()
)
dot3StatsInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInRangeLengthErrors.setStatus("mandatory")
_Dot3StatsOutOfRangeLengthFields_Type = Counter32
_Dot3StatsOutOfRangeLengthFields_Object = MibTableColumn
dot3StatsOutOfRangeLengthFields = _Dot3StatsOutOfRangeLengthFields_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 15),
    _Dot3StatsOutOfRangeLengthFields_Type()
)
dot3StatsOutOfRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsOutOfRangeLengthFields.setStatus("mandatory")
_Dot3StatsInternalMacReceiveErrors_Type = Counter32
_Dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
dot3StatsInternalMacReceiveErrors = _Dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16),
    _Dot3StatsInternalMacReceiveErrors_Type()
)
dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setStatus("mandatory")
_Dot3ChipSets_ObjectIdentity = ObjectIdentity
dot3ChipSets = _Dot3ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8)
)
_Dot3ChipSetAMD_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD = _Dot3ChipSetAMD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1)
)
_Dot3ChipSetAMD7990_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD7990 = _Dot3ChipSetAMD7990_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 1)
)
_Dot3ChipSetAMD79900_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79900 = _Dot3ChipSetAMD79900_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 2)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12)
)
_IfExtnsTable_Object = MibTable
ifExtnsTable = _IfExtnsTable_Object(
    (1, 3, 6, 1, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ifExtnsTable.setStatus("mandatory")
_IfExtnsEntry_Object = MibTableRow
ifExtnsEntry = _IfExtnsEntry_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1)
)
ifExtnsEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "ifExtnsIfIndex"),
)
if mibBuilder.loadTexts:
    ifExtnsEntry.setStatus("mandatory")
_IfExtnsIfIndex_Type = Integer32
_IfExtnsIfIndex_Object = MibTableColumn
ifExtnsIfIndex = _IfExtnsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 1),
    _IfExtnsIfIndex_Type()
)
ifExtnsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsIfIndex.setStatus("mandatory")
_IfExtnsChipSet_Type = ObjectIdentifier
_IfExtnsChipSet_Object = MibTableColumn
ifExtnsChipSet = _IfExtnsChipSet_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 2),
    _IfExtnsChipSet_Type()
)
ifExtnsChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsChipSet.setStatus("mandatory")


class _IfExtnsRevWare_Type(DisplayString):
    """Custom type ifExtnsRevWare based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfExtnsRevWare_Type.__name__ = "DisplayString"
_IfExtnsRevWare_Object = MibTableColumn
ifExtnsRevWare = _IfExtnsRevWare_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 3),
    _IfExtnsRevWare_Type()
)
ifExtnsRevWare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsRevWare.setStatus("mandatory")
_IfExtnsMulticastsTransmittedOks_Type = Counter32
_IfExtnsMulticastsTransmittedOks_Object = MibTableColumn
ifExtnsMulticastsTransmittedOks = _IfExtnsMulticastsTransmittedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 4),
    _IfExtnsMulticastsTransmittedOks_Type()
)
ifExtnsMulticastsTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsMulticastsTransmittedOks.setStatus("mandatory")
_IfExtnsBroadcastsTransmittedOks_Type = Counter32
_IfExtnsBroadcastsTransmittedOks_Object = MibTableColumn
ifExtnsBroadcastsTransmittedOks = _IfExtnsBroadcastsTransmittedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 5),
    _IfExtnsBroadcastsTransmittedOks_Type()
)
ifExtnsBroadcastsTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsBroadcastsTransmittedOks.setStatus("mandatory")
_IfExtnsMulticastsReceivedOks_Type = Counter32
_IfExtnsMulticastsReceivedOks_Object = MibTableColumn
ifExtnsMulticastsReceivedOks = _IfExtnsMulticastsReceivedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 6),
    _IfExtnsMulticastsReceivedOks_Type()
)
ifExtnsMulticastsReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsMulticastsReceivedOks.setStatus("mandatory")
_IfExtnsBroadcastsReceivedOks_Type = Counter32
_IfExtnsBroadcastsReceivedOks_Object = MibTableColumn
ifExtnsBroadcastsReceivedOks = _IfExtnsBroadcastsReceivedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 7),
    _IfExtnsBroadcastsReceivedOks_Type()
)
ifExtnsBroadcastsReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsBroadcastsReceivedOks.setStatus("mandatory")


class _IfExtnsPromiscuous_Type(Integer32):
    """Custom type ifExtnsPromiscuous based on Integer32"""
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


_IfExtnsPromiscuous_Type.__name__ = "Integer32"
_IfExtnsPromiscuous_Object = MibTableColumn
ifExtnsPromiscuous = _IfExtnsPromiscuous_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 8),
    _IfExtnsPromiscuous_Type()
)
ifExtnsPromiscuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsPromiscuous.setStatus("mandatory")
_IfExtnsRcvAddrTable_Object = MibTable
ifExtnsRcvAddrTable = _IfExtnsRcvAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 12, 3)
)
if mibBuilder.loadTexts:
    ifExtnsRcvAddrTable.setStatus("mandatory")
_IfExtnsRcvAddrEntry_Object = MibTableRow
ifExtnsRcvAddrEntry = _IfExtnsRcvAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1)
)
ifExtnsRcvAddrEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "ifExtnsRcvAddrIfIndex"),
    (0, "LBHUB-MSH4PTBRDG-MIB", "ifExtnsRcvAddress"),
)
if mibBuilder.loadTexts:
    ifExtnsRcvAddrEntry.setStatus("mandatory")
_IfExtnsRcvAddrIfIndex_Type = Integer32
_IfExtnsRcvAddrIfIndex_Object = MibTableColumn
ifExtnsRcvAddrIfIndex = _IfExtnsRcvAddrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1, 1),
    _IfExtnsRcvAddrIfIndex_Type()
)
ifExtnsRcvAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsRcvAddrIfIndex.setStatus("mandatory")
_IfExtnsRcvAddress_Type = PhysAddress
_IfExtnsRcvAddress_Object = MibTableColumn
ifExtnsRcvAddress = _IfExtnsRcvAddress_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1, 2),
    _IfExtnsRcvAddress_Type()
)
ifExtnsRcvAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsRcvAddress.setStatus("mandatory")


class _IfExtnsRcvAddrStatus_Type(Integer32):
    """Custom type ifExtnsRcvAddrStatus based on Integer32"""
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
        *(("invalid", 2),
          ("nonVolatile", 4),
          ("other", 1),
          ("volatile", 3))
    )


_IfExtnsRcvAddrStatus_Type.__name__ = "Integer32"
_IfExtnsRcvAddrStatus_Object = MibTableColumn
ifExtnsRcvAddrStatus = _IfExtnsRcvAddrStatus_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1, 3),
    _IfExtnsRcvAddrStatus_Type()
)
ifExtnsRcvAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtnsRcvAddrStatus.setStatus("mandatory")
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Constellation_ObjectIdentity = ObjectIdentity
constellation = _Constellation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187)
)
_CExper_ObjectIdentity = ObjectIdentity
cExper = _CExper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 1)
)
_CProducts_ObjectIdentity = ObjectIdentity
cProducts = _CProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2)
)
_CLittleDipper_ObjectIdentity = ObjectIdentity
cLittleDipper = _CLittleDipper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 1)
)
_CAuriga_ObjectIdentity = ObjectIdentity
cAuriga = _CAuriga_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 3)
)
_CCarina_ObjectIdentity = ObjectIdentity
cCarina = _CCarina_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 4)
)
_CCarinaAui_ObjectIdentity = ObjectIdentity
cCarinaAui = _CCarinaAui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 4, 1)
)
_CCarinaBnc_ObjectIdentity = ObjectIdentity
cCarinaBnc = _CCarinaBnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 4, 2)
)
_CDuPont_ObjectIdentity = ObjectIdentity
cDuPont = _CDuPont_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 5)
)
_CDuPontAui_ObjectIdentity = ObjectIdentity
cDuPontAui = _CDuPontAui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 5, 1)
)
_CDatabil_ObjectIdentity = ObjectIdentity
cDatabil = _CDatabil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 6)
)
_CDatability_ObjectIdentity = ObjectIdentity
cDatability = _CDatability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 6, 1)
)
_CPenr_ObjectIdentity = ObjectIdentity
cPenr = _CPenr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 7)
)
_CPenril_ObjectIdentity = ObjectIdentity
cPenril = _CPenril_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 7, 1)
)
_CThreeCom_ObjectIdentity = ObjectIdentity
cThreeCom = _CThreeCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 8)
)
_CThreeComMSH_ObjectIdentity = ObjectIdentity
cThreeComMSH = _CThreeComMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 2, 8, 1)
)
_CStdExtensions_ObjectIdentity = ObjectIdentity
cStdExtensions = _CStdExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3)
)
_CSystem_ObjectIdentity = ObjectIdentity
cSystem = _CSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 1)
)
_CInterfaces_ObjectIdentity = ObjectIdentity
cInterfaces = _CInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 2)
)
_CIp_ObjectIdentity = ObjectIdentity
cIp = _CIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 4)
)
_CIpInLenErrors_Type = Counter32
_CIpInLenErrors_Object = MibScalar
cIpInLenErrors = _CIpInLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 1),
    _CIpInLenErrors_Type()
)
cIpInLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpInLenErrors.setStatus("mandatory")
_CIpInVersionErrors_Type = Counter32
_CIpInVersionErrors_Object = MibScalar
cIpInVersionErrors = _CIpInVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 2),
    _CIpInVersionErrors_Type()
)
cIpInVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpInVersionErrors.setStatus("mandatory")
_CIpInCSErrors_Type = Counter32
_CIpInCSErrors_Object = MibScalar
cIpInCSErrors = _CIpInCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 3),
    _CIpInCSErrors_Type()
)
cIpInCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpInCSErrors.setStatus("mandatory")
_CIpTTLZero_Type = Counter32
_CIpTTLZero_Object = MibScalar
cIpTTLZero = _CIpTTLZero_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 4),
    _CIpTTLZero_Type()
)
cIpTTLZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpTTLZero.setStatus("mandatory")
_CIpReasmTimeOuts_Type = Counter32
_CIpReasmTimeOuts_Object = MibScalar
cIpReasmTimeOuts = _CIpReasmTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 5),
    _CIpReasmTimeOuts_Type()
)
cIpReasmTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpReasmTimeOuts.setStatus("mandatory")
_CIpNetToMedia_ObjectIdentity = ObjectIdentity
cIpNetToMedia = _CIpNetToMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7)
)
_CIpNetToMediaTableSize_Type = Integer32
_CIpNetToMediaTableSize_Object = MibScalar
cIpNetToMediaTableSize = _CIpNetToMediaTableSize_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 1),
    _CIpNetToMediaTableSize_Type()
)
cIpNetToMediaTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaTableSize.setStatus("mandatory")
_CIpNetToMediaCompleteTimeOut_Type = Integer32
_CIpNetToMediaCompleteTimeOut_Object = MibScalar
cIpNetToMediaCompleteTimeOut = _CIpNetToMediaCompleteTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 2),
    _CIpNetToMediaCompleteTimeOut_Type()
)
cIpNetToMediaCompleteTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetToMediaCompleteTimeOut.setStatus("mandatory")
_CIpNetToMediaInCompleteTimeOut_Type = Integer32
_CIpNetToMediaInCompleteTimeOut_Object = MibScalar
cIpNetToMediaInCompleteTimeOut = _CIpNetToMediaInCompleteTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 3),
    _CIpNetToMediaInCompleteTimeOut_Type()
)
cIpNetToMediaInCompleteTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetToMediaInCompleteTimeOut.setStatus("mandatory")
_CIpNetToMediaIns_Type = Counter32
_CIpNetToMediaIns_Object = MibScalar
cIpNetToMediaIns = _CIpNetToMediaIns_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 4),
    _CIpNetToMediaIns_Type()
)
cIpNetToMediaIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaIns.setStatus("mandatory")
_CIpNetToMediaInLenErrs_Type = Counter32
_CIpNetToMediaInLenErrs_Object = MibScalar
cIpNetToMediaInLenErrs = _CIpNetToMediaInLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 5),
    _CIpNetToMediaInLenErrs_Type()
)
cIpNetToMediaInLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInLenErrs.setStatus("mandatory")
_CIpNetToMediaInNotEther_Type = Counter32
_CIpNetToMediaInNotEther_Object = MibScalar
cIpNetToMediaInNotEther = _CIpNetToMediaInNotEther_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 6),
    _CIpNetToMediaInNotEther_Type()
)
cIpNetToMediaInNotEther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInNotEther.setStatus("mandatory")
_CIpNetToMediaInNoArpOnIf_Type = Counter32
_CIpNetToMediaInNoArpOnIf_Object = MibScalar
cIpNetToMediaInNoArpOnIf = _CIpNetToMediaInNoArpOnIf_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 7),
    _CIpNetToMediaInNoArpOnIf_Type()
)
cIpNetToMediaInNoArpOnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInNoArpOnIf.setStatus("mandatory")
_CIpNetToMediaInIp_Type = Counter32
_CIpNetToMediaInIp_Object = MibScalar
cIpNetToMediaInIp = _CIpNetToMediaInIp_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 8),
    _CIpNetToMediaInIp_Type()
)
cIpNetToMediaInIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInIp.setStatus("mandatory")
_CIpNetToMediaInIpTrailers_Type = Counter32
_CIpNetToMediaInIpTrailers_Object = MibScalar
cIpNetToMediaInIpTrailers = _CIpNetToMediaInIpTrailers_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 9),
    _CIpNetToMediaInIpTrailers_Type()
)
cIpNetToMediaInIpTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInIpTrailers.setStatus("mandatory")
_CIpNetToMediaInUnkProtos_Type = Counter32
_CIpNetToMediaInUnkProtos_Object = MibScalar
cIpNetToMediaInUnkProtos = _CIpNetToMediaInUnkProtos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 10),
    _CIpNetToMediaInUnkProtos_Type()
)
cIpNetToMediaInUnkProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInUnkProtos.setStatus("mandatory")
_CIpNetToMediaInSourceBcast_Type = Counter32
_CIpNetToMediaInSourceBcast_Object = MibScalar
cIpNetToMediaInSourceBcast = _CIpNetToMediaInSourceBcast_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 11),
    _CIpNetToMediaInSourceBcast_Type()
)
cIpNetToMediaInSourceBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInSourceBcast.setStatus("mandatory")
_CIpNetToMediaInDups_Type = Counter32
_CIpNetToMediaInDups_Object = MibScalar
cIpNetToMediaInDups = _CIpNetToMediaInDups_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 12),
    _CIpNetToMediaInDups_Type()
)
cIpNetToMediaInDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInDups.setStatus("mandatory")
_CIpNetToMediaInRequests_Type = Counter32
_CIpNetToMediaInRequests_Object = MibScalar
cIpNetToMediaInRequests = _CIpNetToMediaInRequests_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 13),
    _CIpNetToMediaInRequests_Type()
)
cIpNetToMediaInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInRequests.setStatus("mandatory")
_CIpNetToMediaInResponses_Type = Counter32
_CIpNetToMediaInResponses_Object = MibScalar
cIpNetToMediaInResponses = _CIpNetToMediaInResponses_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 14),
    _CIpNetToMediaInResponses_Type()
)
cIpNetToMediaInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInResponses.setStatus("mandatory")
_CIpNetToMediaInProxyOks_Type = Counter32
_CIpNetToMediaInProxyOks_Object = MibScalar
cIpNetToMediaInProxyOks = _CIpNetToMediaInProxyOks_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 15),
    _CIpNetToMediaInProxyOks_Type()
)
cIpNetToMediaInProxyOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaInProxyOks.setStatus("mandatory")
_CIpNetToMediaOutReplys_Type = Counter32
_CIpNetToMediaOutReplys_Object = MibScalar
cIpNetToMediaOutReplys = _CIpNetToMediaOutReplys_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 16),
    _CIpNetToMediaOutReplys_Type()
)
cIpNetToMediaOutReplys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaOutReplys.setStatus("mandatory")
_CIpNetToMediaOutRequests_Type = Counter32
_CIpNetToMediaOutRequests_Object = MibScalar
cIpNetToMediaOutRequests = _CIpNetToMediaOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 17),
    _CIpNetToMediaOutRequests_Type()
)
cIpNetToMediaOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaOutRequests.setStatus("mandatory")
_CIpNetToMediaReqBadAddrs_Type = Counter32
_CIpNetToMediaReqBadAddrs_Object = MibScalar
cIpNetToMediaReqBadAddrs = _CIpNetToMediaReqBadAddrs_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 18),
    _CIpNetToMediaReqBadAddrs_Type()
)
cIpNetToMediaReqBadAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaReqBadAddrs.setStatus("mandatory")
_CIpNetToMediaNoResponses_Type = Counter32
_CIpNetToMediaNoResponses_Object = MibScalar
cIpNetToMediaNoResponses = _CIpNetToMediaNoResponses_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 19),
    _CIpNetToMediaNoResponses_Type()
)
cIpNetToMediaNoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaNoResponses.setStatus("mandatory")
_CIpNetToMediaAgeOuts_Type = Counter32
_CIpNetToMediaAgeOuts_Object = MibScalar
cIpNetToMediaAgeOuts = _CIpNetToMediaAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 20),
    _CIpNetToMediaAgeOuts_Type()
)
cIpNetToMediaAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaAgeOuts.setStatus("mandatory")
_CIpNetToMediaTable_Object = MibTable
cIpNetToMediaTable = _CIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21)
)
if mibBuilder.loadTexts:
    cIpNetToMediaTable.setStatus("mandatory")
_CIpNetToMediaEntry_Object = MibTableRow
cIpNetToMediaEntry = _CIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1)
)
cIpNetToMediaEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cIpNetToMediaIfIndex"),
    (0, "LBHUB-MSH4PTBRDG-MIB", "cIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    cIpNetToMediaEntry.setStatus("mandatory")
_CIpNetToMediaIfIndex_Type = Integer32
_CIpNetToMediaIfIndex_Object = MibTableColumn
cIpNetToMediaIfIndex = _CIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1, 1),
    _CIpNetToMediaIfIndex_Type()
)
cIpNetToMediaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetToMediaIfIndex.setStatus("mandatory")
_CIpNetToMediaNetAddress_Type = IpAddress
_CIpNetToMediaNetAddress_Object = MibTableColumn
cIpNetToMediaNetAddress = _CIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1, 2),
    _CIpNetToMediaNetAddress_Type()
)
cIpNetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetToMediaNetAddress.setStatus("mandatory")
_CIpNetToMediaRefTime_Type = TimeTicks
_CIpNetToMediaRefTime_Object = MibTableColumn
cIpNetToMediaRefTime = _CIpNetToMediaRefTime_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1, 3),
    _CIpNetToMediaRefTime_Type()
)
cIpNetToMediaRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaRefTime.setStatus("mandatory")


class _CIpNetToMediaProxyRespond_Type(Integer32):
    """Custom type cIpNetToMediaProxyRespond based on Integer32"""
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


_CIpNetToMediaProxyRespond_Type.__name__ = "Integer32"
_CIpNetToMediaProxyRespond_Object = MibTableColumn
cIpNetToMediaProxyRespond = _CIpNetToMediaProxyRespond_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1, 4),
    _CIpNetToMediaProxyRespond_Type()
)
cIpNetToMediaProxyRespond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaProxyRespond.setStatus("mandatory")


class _CIpNetToMediaComplete_Type(Integer32):
    """Custom type cIpNetToMediaComplete based on Integer32"""
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


_CIpNetToMediaComplete_Type.__name__ = "Integer32"
_CIpNetToMediaComplete_Object = MibTableColumn
cIpNetToMediaComplete = _CIpNetToMediaComplete_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1, 5),
    _CIpNetToMediaComplete_Type()
)
cIpNetToMediaComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaComplete.setStatus("mandatory")


class _CIpNetToMediaUseTrailers_Type(Integer32):
    """Custom type cIpNetToMediaUseTrailers based on Integer32"""
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


_CIpNetToMediaUseTrailers_Type.__name__ = "Integer32"
_CIpNetToMediaUseTrailers_Object = MibTableColumn
cIpNetToMediaUseTrailers = _CIpNetToMediaUseTrailers_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 4, 7, 21, 1, 6),
    _CIpNetToMediaUseTrailers_Type()
)
cIpNetToMediaUseTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetToMediaUseTrailers.setStatus("mandatory")
_CIcmp_ObjectIdentity = ObjectIdentity
cIcmp = _CIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 5)
)
_CIcmpInRedirectNet_Type = Counter32
_CIcmpInRedirectNet_Object = MibScalar
cIcmpInRedirectNet = _CIcmpInRedirectNet_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 1),
    _CIcmpInRedirectNet_Type()
)
cIcmpInRedirectNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInRedirectNet.setStatus("mandatory")
_CIcmpInRedirectHost_Type = Counter32
_CIcmpInRedirectHost_Object = MibScalar
cIcmpInRedirectHost = _CIcmpInRedirectHost_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 2),
    _CIcmpInRedirectHost_Type()
)
cIcmpInRedirectHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInRedirectHost.setStatus("mandatory")
_CIcmpInRedirectNetTos_Type = Counter32
_CIcmpInRedirectNetTos_Object = MibScalar
cIcmpInRedirectNetTos = _CIcmpInRedirectNetTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 3),
    _CIcmpInRedirectNetTos_Type()
)
cIcmpInRedirectNetTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInRedirectNetTos.setStatus("mandatory")
_CIcmpInRedirectHostTos_Type = Counter32
_CIcmpInRedirectHostTos_Object = MibScalar
cIcmpInRedirectHostTos = _CIcmpInRedirectHostTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 4),
    _CIcmpInRedirectHostTos_Type()
)
cIcmpInRedirectHostTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInRedirectHostTos.setStatus("mandatory")
_CIcmpInTimeExcTTL_Type = Counter32
_CIcmpInTimeExcTTL_Object = MibScalar
cIcmpInTimeExcTTL = _CIcmpInTimeExcTTL_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 5),
    _CIcmpInTimeExcTTL_Type()
)
cIcmpInTimeExcTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInTimeExcTTL.setStatus("mandatory")
_CIcmpInTimeExcReAsm_Type = Counter32
_CIcmpInTimeExcReAsm_Object = MibScalar
cIcmpInTimeExcReAsm = _CIcmpInTimeExcReAsm_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 6),
    _CIcmpInTimeExcReAsm_Type()
)
cIcmpInTimeExcReAsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInTimeExcReAsm.setStatus("mandatory")
_CIcmpInDestUnNet_Type = Counter32
_CIcmpInDestUnNet_Object = MibScalar
cIcmpInDestUnNet = _CIcmpInDestUnNet_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 7),
    _CIcmpInDestUnNet_Type()
)
cIcmpInDestUnNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnNet.setStatus("mandatory")
_CIcmpInDestUnHost_Type = Counter32
_CIcmpInDestUnHost_Object = MibScalar
cIcmpInDestUnHost = _CIcmpInDestUnHost_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 8),
    _CIcmpInDestUnHost_Type()
)
cIcmpInDestUnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnHost.setStatus("mandatory")
_CIcmpInDestUnProtocol_Type = Counter32
_CIcmpInDestUnProtocol_Object = MibScalar
cIcmpInDestUnProtocol = _CIcmpInDestUnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 9),
    _CIcmpInDestUnProtocol_Type()
)
cIcmpInDestUnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnProtocol.setStatus("mandatory")
_CIcmpInDestUnPort_Type = Counter32
_CIcmpInDestUnPort_Object = MibScalar
cIcmpInDestUnPort = _CIcmpInDestUnPort_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 10),
    _CIcmpInDestUnPort_Type()
)
cIcmpInDestUnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnPort.setStatus("mandatory")
_CIcmpInDestUnFragNeeded_Type = Counter32
_CIcmpInDestUnFragNeeded_Object = MibScalar
cIcmpInDestUnFragNeeded = _CIcmpInDestUnFragNeeded_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 11),
    _CIcmpInDestUnFragNeeded_Type()
)
cIcmpInDestUnFragNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnFragNeeded.setStatus("mandatory")
_CIcmpInDestUnSourceRoute_Type = Counter32
_CIcmpInDestUnSourceRoute_Object = MibScalar
cIcmpInDestUnSourceRoute = _CIcmpInDestUnSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 12),
    _CIcmpInDestUnSourceRoute_Type()
)
cIcmpInDestUnSourceRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnSourceRoute.setStatus("mandatory")
_CIcmpOutRedirectNet_Type = Counter32
_CIcmpOutRedirectNet_Object = MibScalar
cIcmpOutRedirectNet = _CIcmpOutRedirectNet_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 13),
    _CIcmpOutRedirectNet_Type()
)
cIcmpOutRedirectNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutRedirectNet.setStatus("mandatory")
_CIcmpOutRedirectHost_Type = Counter32
_CIcmpOutRedirectHost_Object = MibScalar
cIcmpOutRedirectHost = _CIcmpOutRedirectHost_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 14),
    _CIcmpOutRedirectHost_Type()
)
cIcmpOutRedirectHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutRedirectHost.setStatus("mandatory")
_CIcmpOutRedirectNetTos_Type = Counter32
_CIcmpOutRedirectNetTos_Object = MibScalar
cIcmpOutRedirectNetTos = _CIcmpOutRedirectNetTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 15),
    _CIcmpOutRedirectNetTos_Type()
)
cIcmpOutRedirectNetTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutRedirectNetTos.setStatus("mandatory")
_CIcmpOutRedirectHostTos_Type = Counter32
_CIcmpOutRedirectHostTos_Object = MibScalar
cIcmpOutRedirectHostTos = _CIcmpOutRedirectHostTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 16),
    _CIcmpOutRedirectHostTos_Type()
)
cIcmpOutRedirectHostTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutRedirectHostTos.setStatus("mandatory")
_CIcmpOutTimeExcTTL_Type = Counter32
_CIcmpOutTimeExcTTL_Object = MibScalar
cIcmpOutTimeExcTTL = _CIcmpOutTimeExcTTL_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 17),
    _CIcmpOutTimeExcTTL_Type()
)
cIcmpOutTimeExcTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutTimeExcTTL.setStatus("mandatory")
_CIcmpOutTimeExcReAsm_Type = Counter32
_CIcmpOutTimeExcReAsm_Object = MibScalar
cIcmpOutTimeExcReAsm = _CIcmpOutTimeExcReAsm_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 18),
    _CIcmpOutTimeExcReAsm_Type()
)
cIcmpOutTimeExcReAsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutTimeExcReAsm.setStatus("mandatory")
_CIcmpOutDestUnNet_Type = Counter32
_CIcmpOutDestUnNet_Object = MibScalar
cIcmpOutDestUnNet = _CIcmpOutDestUnNet_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 19),
    _CIcmpOutDestUnNet_Type()
)
cIcmpOutDestUnNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnNet.setStatus("mandatory")
_CIcmpOutDestUnHost_Type = Counter32
_CIcmpOutDestUnHost_Object = MibScalar
cIcmpOutDestUnHost = _CIcmpOutDestUnHost_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 20),
    _CIcmpOutDestUnHost_Type()
)
cIcmpOutDestUnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnHost.setStatus("mandatory")
_CIcmpOutDestUnProtocol_Type = Counter32
_CIcmpOutDestUnProtocol_Object = MibScalar
cIcmpOutDestUnProtocol = _CIcmpOutDestUnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 21),
    _CIcmpOutDestUnProtocol_Type()
)
cIcmpOutDestUnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnProtocol.setStatus("mandatory")
_CIcmpOutDestUnPort_Type = Counter32
_CIcmpOutDestUnPort_Object = MibScalar
cIcmpOutDestUnPort = _CIcmpOutDestUnPort_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 22),
    _CIcmpOutDestUnPort_Type()
)
cIcmpOutDestUnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnPort.setStatus("mandatory")
_CIcmpOutDestUnFragNeeded_Type = Counter32
_CIcmpOutDestUnFragNeeded_Object = MibScalar
cIcmpOutDestUnFragNeeded = _CIcmpOutDestUnFragNeeded_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 23),
    _CIcmpOutDestUnFragNeeded_Type()
)
cIcmpOutDestUnFragNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnFragNeeded.setStatus("mandatory")
_CIcmpOutDestUnSourceRoute_Type = Counter32
_CIcmpOutDestUnSourceRoute_Object = MibScalar
cIcmpOutDestUnSourceRoute = _CIcmpOutDestUnSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 24),
    _CIcmpOutDestUnSourceRoute_Type()
)
cIcmpOutDestUnSourceRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnSourceRoute.setStatus("mandatory")
_CIcmpInLengthErrors_Type = Counter32
_CIcmpInLengthErrors_Object = MibScalar
cIcmpInLengthErrors = _CIcmpInLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 25),
    _CIcmpInLengthErrors_Type()
)
cIcmpInLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInLengthErrors.setStatus("mandatory")
_CIcmpInChecksumErrors_Type = Counter32
_CIcmpInChecksumErrors_Object = MibScalar
cIcmpInChecksumErrors = _CIcmpInChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 26),
    _CIcmpInChecksumErrors_Type()
)
cIcmpInChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInChecksumErrors.setStatus("mandatory")
_CIcmpInUnkTypes_Type = Counter32
_CIcmpInUnkTypes_Object = MibScalar
cIcmpInUnkTypes = _CIcmpInUnkTypes_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 27),
    _CIcmpInUnkTypes_Type()
)
cIcmpInUnkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInUnkTypes.setStatus("mandatory")
_CIcmpInDestUnNetUnknown_Type = Counter32
_CIcmpInDestUnNetUnknown_Object = MibScalar
cIcmpInDestUnNetUnknown = _CIcmpInDestUnNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 28),
    _CIcmpInDestUnNetUnknown_Type()
)
cIcmpInDestUnNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnNetUnknown.setStatus("mandatory")
_CIcmpInDestUnHostUnknown_Type = Counter32
_CIcmpInDestUnHostUnknown_Object = MibScalar
cIcmpInDestUnHostUnknown = _CIcmpInDestUnHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 29),
    _CIcmpInDestUnHostUnknown_Type()
)
cIcmpInDestUnHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnHostUnknown.setStatus("mandatory")
_CIcmpInDestUnSrcIsolated_Type = Counter32
_CIcmpInDestUnSrcIsolated_Object = MibScalar
cIcmpInDestUnSrcIsolated = _CIcmpInDestUnSrcIsolated_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 30),
    _CIcmpInDestUnSrcIsolated_Type()
)
cIcmpInDestUnSrcIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnSrcIsolated.setStatus("mandatory")
_CIcmpInDestUnHostProhib_Type = Counter32
_CIcmpInDestUnHostProhib_Object = MibScalar
cIcmpInDestUnHostProhib = _CIcmpInDestUnHostProhib_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 31),
    _CIcmpInDestUnHostProhib_Type()
)
cIcmpInDestUnHostProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnHostProhib.setStatus("mandatory")
_CIcmpInDestUnNetProhib_Type = Counter32
_CIcmpInDestUnNetProhib_Object = MibScalar
cIcmpInDestUnNetProhib = _CIcmpInDestUnNetProhib_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 32),
    _CIcmpInDestUnNetProhib_Type()
)
cIcmpInDestUnNetProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnNetProhib.setStatus("mandatory")
_CIcmpInDestUnNetTos_Type = Counter32
_CIcmpInDestUnNetTos_Object = MibScalar
cIcmpInDestUnNetTos = _CIcmpInDestUnNetTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 33),
    _CIcmpInDestUnNetTos_Type()
)
cIcmpInDestUnNetTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnNetTos.setStatus("mandatory")
_CIcmpInDestUnHostTos_Type = Counter32
_CIcmpInDestUnHostTos_Object = MibScalar
cIcmpInDestUnHostTos = _CIcmpInDestUnHostTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 34),
    _CIcmpInDestUnHostTos_Type()
)
cIcmpInDestUnHostTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInDestUnHostTos.setStatus("mandatory")
_CIcmpOutDestUnNetUnknown_Type = Counter32
_CIcmpOutDestUnNetUnknown_Object = MibScalar
cIcmpOutDestUnNetUnknown = _CIcmpOutDestUnNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 35),
    _CIcmpOutDestUnNetUnknown_Type()
)
cIcmpOutDestUnNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnNetUnknown.setStatus("mandatory")
_CIcmpOutDestUnHostUnknown_Type = Counter32
_CIcmpOutDestUnHostUnknown_Object = MibScalar
cIcmpOutDestUnHostUnknown = _CIcmpOutDestUnHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 36),
    _CIcmpOutDestUnHostUnknown_Type()
)
cIcmpOutDestUnHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnHostUnknown.setStatus("mandatory")
_CIcmpOutDestUnSrcIsolated_Type = Counter32
_CIcmpOutDestUnSrcIsolated_Object = MibScalar
cIcmpOutDestUnSrcIsolated = _CIcmpOutDestUnSrcIsolated_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 37),
    _CIcmpOutDestUnSrcIsolated_Type()
)
cIcmpOutDestUnSrcIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnSrcIsolated.setStatus("mandatory")
_CIcmpOutDestUnHostProhib_Type = Counter32
_CIcmpOutDestUnHostProhib_Object = MibScalar
cIcmpOutDestUnHostProhib = _CIcmpOutDestUnHostProhib_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 38),
    _CIcmpOutDestUnHostProhib_Type()
)
cIcmpOutDestUnHostProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnHostProhib.setStatus("mandatory")
_CIcmpOutDestUnNetProhib_Type = Counter32
_CIcmpOutDestUnNetProhib_Object = MibScalar
cIcmpOutDestUnNetProhib = _CIcmpOutDestUnNetProhib_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 39),
    _CIcmpOutDestUnNetProhib_Type()
)
cIcmpOutDestUnNetProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnNetProhib.setStatus("mandatory")
_CIcmpOutDestUnNetTos_Type = Counter32
_CIcmpOutDestUnNetTos_Object = MibScalar
cIcmpOutDestUnNetTos = _CIcmpOutDestUnNetTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 40),
    _CIcmpOutDestUnNetTos_Type()
)
cIcmpOutDestUnNetTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnNetTos.setStatus("mandatory")
_CIcmpOutDestUnHostTos_Type = Counter32
_CIcmpOutDestUnHostTos_Object = MibScalar
cIcmpOutDestUnHostTos = _CIcmpOutDestUnHostTos_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 41),
    _CIcmpOutDestUnHostTos_Type()
)
cIcmpOutDestUnHostTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutDestUnHostTos.setStatus("mandatory")
_CIcmpInParmProbMissingOpt_Type = Counter32
_CIcmpInParmProbMissingOpt_Object = MibScalar
cIcmpInParmProbMissingOpt = _CIcmpInParmProbMissingOpt_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 42),
    _CIcmpInParmProbMissingOpt_Type()
)
cIcmpInParmProbMissingOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpInParmProbMissingOpt.setStatus("mandatory")
_CIcmpOutParmProbMissingOpt_Type = Counter32
_CIcmpOutParmProbMissingOpt_Object = MibScalar
cIcmpOutParmProbMissingOpt = _CIcmpOutParmProbMissingOpt_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 5, 43),
    _CIcmpOutParmProbMissingOpt_Type()
)
cIcmpOutParmProbMissingOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIcmpOutParmProbMissingOpt.setStatus("mandatory")
_CTcp_ObjectIdentity = ObjectIdentity
cTcp = _CTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 6)
)
_CUdp_ObjectIdentity = ObjectIdentity
cUdp = _CUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 7)
)
_CUdpHdrDrops_Type = Counter32
_CUdpHdrDrops_Object = MibScalar
cUdpHdrDrops = _CUdpHdrDrops_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 7, 1),
    _CUdpHdrDrops_Type()
)
cUdpHdrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUdpHdrDrops.setStatus("mandatory")
_CUdpBadCheckSum_Type = Counter32
_CUdpBadCheckSum_Object = MibScalar
cUdpBadCheckSum = _CUdpBadCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 7, 2),
    _CUdpBadCheckSum_Type()
)
cUdpBadCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUdpBadCheckSum.setStatus("mandatory")
_CUdpBadLength_Type = Counter32
_CUdpBadLength_Object = MibScalar
cUdpBadLength = _CUdpBadLength_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 7, 3),
    _CUdpBadLength_Type()
)
cUdpBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUdpBadLength.setStatus("mandatory")
_CUdpOtherErrors_Type = Counter32
_CUdpOtherErrors_Object = MibScalar
cUdpOtherErrors = _CUdpOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 7, 4),
    _CUdpOtherErrors_Type()
)
cUdpOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUdpOtherErrors.setStatus("mandatory")
_CUdpNoChecksum_Type = Counter32
_CUdpNoChecksum_Object = MibScalar
cUdpNoChecksum = _CUdpNoChecksum_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 7, 5),
    _CUdpNoChecksum_Type()
)
cUdpNoChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUdpNoChecksum.setStatus("mandatory")
_CTransmission_ObjectIdentity = ObjectIdentity
cTransmission = _CTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 10)
)
_CDot3_ObjectIdentity = ObjectIdentity
cDot3 = _CDot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7)
)
_CDot3Table_Object = MibTable
cDot3Table = _CDot3Table_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1)
)
if mibBuilder.loadTexts:
    cDot3Table.setStatus("mandatory")
_CDot3Entry_Object = MibTableRow
cDot3Entry = _CDot3Entry_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1)
)
cDot3Entry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cDot3Index"),
)
if mibBuilder.loadTexts:
    cDot3Entry.setStatus("mandatory")
_CDot3Index_Type = Integer32
_CDot3Index_Object = MibTableColumn
cDot3Index = _CDot3Index_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 1),
    _CDot3Index_Type()
)
cDot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3Index.setStatus("mandatory")
_CDot3Disables_Type = Counter32
_CDot3Disables_Object = MibTableColumn
cDot3Disables = _CDot3Disables_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 2),
    _CDot3Disables_Type()
)
cDot3Disables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3Disables.setStatus("mandatory")
_CDot3MauDisconnect_Type = Counter32
_CDot3MauDisconnect_Object = MibTableColumn
cDot3MauDisconnect = _CDot3MauDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 3),
    _CDot3MauDisconnect_Type()
)
cDot3MauDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3MauDisconnect.setStatus("mandatory")
_CDot3Babbles_Type = Counter32
_CDot3Babbles_Object = MibTableColumn
cDot3Babbles = _CDot3Babbles_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 4),
    _CDot3Babbles_Type()
)
cDot3Babbles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3Babbles.setStatus("mandatory")
_CDot3MerrDisconnect_Type = Counter32
_CDot3MerrDisconnect_Object = MibTableColumn
cDot3MerrDisconnect = _CDot3MerrDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 5),
    _CDot3MerrDisconnect_Type()
)
cDot3MerrDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3MerrDisconnect.setStatus("mandatory")
_CDot3TxonDisconnect_Type = Counter32
_CDot3TxonDisconnect_Object = MibTableColumn
cDot3TxonDisconnect = _CDot3TxonDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 6),
    _CDot3TxonDisconnect_Type()
)
cDot3TxonDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3TxonDisconnect.setStatus("mandatory")
_CDot3RxonDisconnect_Type = Counter32
_CDot3RxonDisconnect_Object = MibTableColumn
cDot3RxonDisconnect = _CDot3RxonDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 7),
    _CDot3RxonDisconnect_Type()
)
cDot3RxonDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3RxonDisconnect.setStatus("mandatory")
_CDot3XmitFailure_Type = Counter32
_CDot3XmitFailure_Object = MibTableColumn
cDot3XmitFailure = _CDot3XmitFailure_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 8),
    _CDot3XmitFailure_Type()
)
cDot3XmitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3XmitFailure.setStatus("mandatory")
_CDot3XmitBuffErr_Type = Counter32
_CDot3XmitBuffErr_Object = MibTableColumn
cDot3XmitBuffErr = _CDot3XmitBuffErr_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 9),
    _CDot3XmitBuffErr_Type()
)
cDot3XmitBuffErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3XmitBuffErr.setStatus("mandatory")
_CDot3XmitUflo_Type = Counter32
_CDot3XmitUflo_Object = MibTableColumn
cDot3XmitUflo = _CDot3XmitUflo_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 10),
    _CDot3XmitUflo_Type()
)
cDot3XmitUflo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3XmitUflo.setStatus("mandatory")
_CDot3RcvBuffErr_Type = Counter32
_CDot3RcvBuffErr_Object = MibTableColumn
cDot3RcvBuffErr = _CDot3RcvBuffErr_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 11),
    _CDot3RcvBuffErr_Type()
)
cDot3RcvBuffErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3RcvBuffErr.setStatus("mandatory")
_CDot3RcvOflo_Type = Counter32
_CDot3RcvOflo_Object = MibTableColumn
cDot3RcvOflo = _CDot3RcvOflo_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 12),
    _CDot3RcvOflo_Type()
)
cDot3RcvOflo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3RcvOflo.setStatus("mandatory")
_CDot3Startless_Type = Counter32
_CDot3Startless_Object = MibTableColumn
cDot3Startless = _CDot3Startless_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 13),
    _CDot3Startless_Type()
)
cDot3Startless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3Startless.setStatus("mandatory")
_CDot3Endless_Type = Counter32
_CDot3Endless_Object = MibTableColumn
cDot3Endless = _CDot3Endless_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 10, 7, 1, 1, 14),
    _CDot3Endless_Type()
)
cDot3Endless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot3Endless.setStatus("mandatory")
_CSnmp_ObjectIdentity = ObjectIdentity
cSnmp = _CSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 11)
)
_CSnmpCommunities_ObjectIdentity = ObjectIdentity
cSnmpCommunities = _CSnmpCommunities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 3, 11, 1)
)
_CSnmpInCommunityMessages_Type = Counter32
_CSnmpInCommunityMessages_Object = MibScalar
cSnmpInCommunityMessages = _CSnmpInCommunityMessages_Object(
    (1, 3, 6, 1, 4, 1, 187, 3, 11, 1, 1),
    _CSnmpInCommunityMessages_Type()
)
cSnmpInCommunityMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnmpInCommunityMessages.setStatus("mandatory")
_CConstellation_ObjectIdentity = ObjectIdentity
cConstellation = _CConstellation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 4)
)
_CConstellationAvailableBuffers_Type = Gauge32
_CConstellationAvailableBuffers_Object = MibScalar
cConstellationAvailableBuffers = _CConstellationAvailableBuffers_Object(
    (1, 3, 6, 1, 4, 1, 187, 4, 1),
    _CConstellationAvailableBuffers_Type()
)
cConstellationAvailableBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cConstellationAvailableBuffers.setStatus("mandatory")
_CConstellationInitialBuffers_Type = Integer32
_CConstellationInitialBuffers_Object = MibScalar
cConstellationInitialBuffers = _CConstellationInitialBuffers_Object(
    (1, 3, 6, 1, 4, 1, 187, 4, 2),
    _CConstellationInitialBuffers_Type()
)
cConstellationInitialBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cConstellationInitialBuffers.setStatus("mandatory")


class _CConstallationBufferDataLength_Type(Integer32):
    """Custom type cConstallationBufferDataLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65535),
    )


_CConstallationBufferDataLength_Type.__name__ = "Integer32"
_CConstallationBufferDataLength_Object = MibScalar
cConstallationBufferDataLength = _CConstallationBufferDataLength_Object(
    (1, 3, 6, 1, 4, 1, 187, 4, 3),
    _CConstallationBufferDataLength_Type()
)
cConstallationBufferDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cConstallationBufferDataLength.setStatus("mandatory")
_CConstellationInstructionRam_Type = Integer32
_CConstellationInstructionRam_Object = MibScalar
cConstellationInstructionRam = _CConstellationInstructionRam_Object(
    (1, 3, 6, 1, 4, 1, 187, 4, 4),
    _CConstellationInstructionRam_Type()
)
cConstellationInstructionRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cConstellationInstructionRam.setStatus("mandatory")
_CConstellationGlobalDataRam_Type = Integer32
_CConstellationGlobalDataRam_Object = MibScalar
cConstellationGlobalDataRam = _CConstellationGlobalDataRam_Object(
    (1, 3, 6, 1, 4, 1, 187, 4, 5),
    _CConstellationGlobalDataRam_Type()
)
cConstellationGlobalDataRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cConstellationGlobalDataRam.setStatus("mandatory")
_CConstellationFastDataRam_Type = Integer32
_CConstellationFastDataRam_Object = MibScalar
cConstellationFastDataRam = _CConstellationFastDataRam_Object(
    (1, 3, 6, 1, 4, 1, 187, 4, 6),
    _CConstellationFastDataRam_Type()
)
cConstellationFastDataRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cConstellationFastDataRam.setStatus("mandatory")
_CProxys_ObjectIdentity = ObjectIdentity
cProxys = _CProxys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5)
)
_CProxyLb_ObjectIdentity = ObjectIdentity
cProxyLb = _CProxyLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 1)
)
_CProxyLb0_ObjectIdentity = ObjectIdentity
cProxyLb0 = _CProxyLb0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 1, 1)
)
_CProxyLb1_ObjectIdentity = ObjectIdentity
cProxyLb1 = _CProxyLb1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 1, 2)
)
_CProxyLb2_ObjectIdentity = ObjectIdentity
cProxyLb2 = _CProxyLb2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 1, 3)
)
_CProxyLb3_ObjectIdentity = ObjectIdentity
cProxyLb3 = _CProxyLb3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 1, 4)
)
_CProxyLr_ObjectIdentity = ObjectIdentity
cProxyLr = _CProxyLr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 2)
)
_CProxyLr0_ObjectIdentity = ObjectIdentity
cProxyLr0 = _CProxyLr0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 5, 2, 1)
)
_CConfig_ObjectIdentity = ObjectIdentity
cConfig = _CConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6)
)
_CConfigSystem_ObjectIdentity = ObjectIdentity
cConfigSystem = _CConfigSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 1)
)
_CConfSysInfo_ObjectIdentity = ObjectIdentity
cConfSysInfo = _CConfSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1)
)
_CLocalTime_Type = OctetString
_CLocalTime_Object = MibScalar
cLocalTime = _CLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1, 1),
    _CLocalTime_Type()
)
cLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLocalTime.setStatus("mandatory")
_CLocalDate_Type = OctetString
_CLocalDate_Object = MibScalar
cLocalDate = _CLocalDate_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1, 2),
    _CLocalDate_Type()
)
cLocalDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLocalDate.setStatus("mandatory")


class _CLocalCtpMode_Type(Integer32):
    """Custom type cLocalCtpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_CLocalCtpMode_Type.__name__ = "Integer32"
_CLocalCtpMode_Object = MibScalar
cLocalCtpMode = _CLocalCtpMode_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1, 4),
    _CLocalCtpMode_Type()
)
cLocalCtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLocalCtpMode.setStatus("mandatory")


class _CRemoteCtpMode_Type(Integer32):
    """Custom type cRemoteCtpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_CRemoteCtpMode_Type.__name__ = "Integer32"
_CRemoteCtpMode_Object = MibScalar
cRemoteCtpMode = _CRemoteCtpMode_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1, 5),
    _CRemoteCtpMode_Type()
)
cRemoteCtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRemoteCtpMode.setStatus("mandatory")


class _CBridgeStatsAveraging_Type(Integer32):
    """Custom type cBridgeStatsAveraging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CBridgeStatsAveraging_Type.__name__ = "Integer32"
_CBridgeStatsAveraging_Object = MibScalar
cBridgeStatsAveraging = _CBridgeStatsAveraging_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1, 6),
    _CBridgeStatsAveraging_Type()
)
cBridgeStatsAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBridgeStatsAveraging.setStatus("mandatory")


class _CBranchTargetCache_Type(Integer32):
    """Custom type cBranchTargetCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CBranchTargetCache_Type.__name__ = "Integer32"
_CBranchTargetCache_Object = MibScalar
cBranchTargetCache = _CBranchTargetCache_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 1, 7),
    _CBranchTargetCache_Type()
)
cBranchTargetCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBranchTargetCache.setStatus("mandatory")
_CConfOperAcct_ObjectIdentity = ObjectIdentity
cConfOperAcct = _CConfOperAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2)
)
_COperAcctTable_Object = MibTable
cOperAcctTable = _COperAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cOperAcctTable.setStatus("mandatory")
_COperAcctEntry_Object = MibTableRow
cOperAcctEntry = _COperAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1, 1)
)
cOperAcctEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cOperIndex"),
)
if mibBuilder.loadTexts:
    cOperAcctEntry.setStatus("mandatory")


class _COperIndex_Type(Integer32):
    """Custom type cOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_COperIndex_Type.__name__ = "Integer32"
_COperIndex_Object = MibTableColumn
cOperIndex = _COperIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1, 1, 1),
    _COperIndex_Type()
)
cOperIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOperIndex.setStatus("mandatory")


class _COperID_Type(OctetString):
    """Custom type cOperID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_COperID_Type.__name__ = "OctetString"
_COperID_Object = MibTableColumn
cOperID = _COperID_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1, 1, 2),
    _COperID_Type()
)
cOperID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOperID.setStatus("mandatory")


class _COperPriv_Type(Integer32):
    """Custom type cOperPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("privAdmin", 3),
          ("privNone", 1),
          ("privOper", 2))
    )


_COperPriv_Type.__name__ = "Integer32"
_COperPriv_Object = MibTableColumn
cOperPriv = _COperPriv_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1, 1, 3),
    _COperPriv_Type()
)
cOperPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOperPriv.setStatus("mandatory")


class _COperPasswd_Type(OctetString):
    """Custom type cOperPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_COperPasswd_Type.__name__ = "OctetString"
_COperPasswd_Object = MibTableColumn
cOperPasswd = _COperPasswd_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1, 1, 4),
    _COperPasswd_Type()
)
cOperPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOperPasswd.setStatus("mandatory")


class _COperStatus_Type(Integer32):
    """Custom type cOperStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_COperStatus_Type.__name__ = "Integer32"
_COperStatus_Object = MibTableColumn
cOperStatus = _COperStatus_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 1, 2, 1, 1, 5),
    _COperStatus_Type()
)
cOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOperStatus.setStatus("mandatory")
_CConfigLan_ObjectIdentity = ObjectIdentity
cConfigLan = _CConfigLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 2)
)
_CConfigEther_ObjectIdentity = ObjectIdentity
cConfigEther = _CConfigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 2, 1)
)
_CConfigTwp_ObjectIdentity = ObjectIdentity
cConfigTwp = _CConfigTwp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 2, 2)
)
_CConfigWan_ObjectIdentity = ObjectIdentity
cConfigWan = _CConfigWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 3)
)
_CConfigSerChan_ObjectIdentity = ObjectIdentity
cConfigSerChan = _CConfigSerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 3, 1)
)
_CConfigWideAreaGroups_ObjectIdentity = ObjectIdentity
cConfigWideAreaGroups = _CConfigWideAreaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 3, 3)
)
_CConfigBridge_ObjectIdentity = ObjectIdentity
cConfigBridge = _CConfigBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 5)
)
_CConfigLogicalBridge_ObjectIdentity = ObjectIdentity
cConfigLogicalBridge = _CConfigLogicalBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 5, 1)
)
_CIpAddress_ObjectIdentity = ObjectIdentity
cIpAddress = _CIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 6)
)
_CConfigIpRouter_ObjectIdentity = ObjectIdentity
cConfigIpRouter = _CConfigIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 7)
)
_CConfigAcceptLists_ObjectIdentity = ObjectIdentity
cConfigAcceptLists = _CConfigAcceptLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 7, 5)
)
_CConfigPropagateLists_ObjectIdentity = ObjectIdentity
cConfigPropagateLists = _CConfigPropagateLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 7, 6)
)
_CIpFilters_ObjectIdentity = ObjectIdentity
cIpFilters = _CIpFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 7, 9)
)
_CConfigIpxRouter_ObjectIdentity = ObjectIdentity
cConfigIpxRouter = _CConfigIpxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 8)
)
_CConfigIpxBridgeIf_ObjectIdentity = ObjectIdentity
cConfigIpxBridgeIf = _CConfigIpxBridgeIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 8, 1)
)
_CConfigIpxRouterFilters_ObjectIdentity = ObjectIdentity
cConfigIpxRouterFilters = _CConfigIpxRouterFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 8, 2)
)
_CConfigAppleTalk_ObjectIdentity = ObjectIdentity
cConfigAppleTalk = _CConfigAppleTalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 9)
)
_CConfigAtIf_ObjectIdentity = ObjectIdentity
cConfigAtIf = _CConfigAtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 9, 1)
)
_CConfigNetProtocol_ObjectIdentity = ObjectIdentity
cConfigNetProtocol = _CConfigNetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 10)
)
_CConfigSnmp_ObjectIdentity = ObjectIdentity
cConfigSnmp = _CConfigSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1)
)
_CSnmpCommunityTable_Object = MibTable
cSnmpCommunityTable = _CSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1)
)
if mibBuilder.loadTexts:
    cSnmpCommunityTable.setStatus("mandatory")
_CSnmpCommunityEntry_Object = MibTableRow
cSnmpCommunityEntry = _CSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1)
)
cSnmpCommunityEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cSnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    cSnmpCommunityEntry.setStatus("mandatory")
_CSnmpCommunityIndex_Type = Integer32
_CSnmpCommunityIndex_Object = MibTableColumn
cSnmpCommunityIndex = _CSnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 1),
    _CSnmpCommunityIndex_Type()
)
cSnmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnmpCommunityIndex.setStatus("mandatory")


class _CSnmpCommunity_Type(OctetString):
    """Custom type cSnmpCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CSnmpCommunity_Type.__name__ = "OctetString"
_CSnmpCommunity_Object = MibTableColumn
cSnmpCommunity = _CSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 2),
    _CSnmpCommunity_Type()
)
cSnmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSnmpCommunity.setStatus("mandatory")


class _CSnmpCommunityIf_Type(Integer32):
    """Custom type cSnmpCommunityIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("lb0", 1),
          ("lb1", 2),
          ("lb2", 3),
          ("lb3", 4),
          ("router", 1024),
          ("wa0", 5),
          ("wa1", 6))
    )


_CSnmpCommunityIf_Type.__name__ = "Integer32"
_CSnmpCommunityIf_Object = MibTableColumn
cSnmpCommunityIf = _CSnmpCommunityIf_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 3),
    _CSnmpCommunityIf_Type()
)
cSnmpCommunityIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSnmpCommunityIf.setStatus("mandatory")


class _CSnmpCommunityAccess_Type(Integer32):
    """Custom type cSnmpCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CSnmpCommunityAccess_Type.__name__ = "Integer32"
_CSnmpCommunityAccess_Object = MibTableColumn
cSnmpCommunityAccess = _CSnmpCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 4),
    _CSnmpCommunityAccess_Type()
)
cSnmpCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSnmpCommunityAccess.setStatus("mandatory")
_CSnmpCommunityTrapAddress_Type = IpAddress
_CSnmpCommunityTrapAddress_Object = MibTableColumn
cSnmpCommunityTrapAddress = _CSnmpCommunityTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 5),
    _CSnmpCommunityTrapAddress_Type()
)
cSnmpCommunityTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSnmpCommunityTrapAddress.setStatus("mandatory")
_CSnmpCommunityTrapPort_Type = Integer32
_CSnmpCommunityTrapPort_Object = MibTableColumn
cSnmpCommunityTrapPort = _CSnmpCommunityTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 6),
    _CSnmpCommunityTrapPort_Type()
)
cSnmpCommunityTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSnmpCommunityTrapPort.setStatus("mandatory")


class _CSnmpCommunityTrapEnabled_Type(Integer32):
    """Custom type cSnmpCommunityTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CSnmpCommunityTrapEnabled_Type.__name__ = "Integer32"
_CSnmpCommunityTrapEnabled_Object = MibTableColumn
cSnmpCommunityTrapEnabled = _CSnmpCommunityTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 1, 1, 1, 7),
    _CSnmpCommunityTrapEnabled_Type()
)
cSnmpCommunityTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSnmpCommunityTrapEnabled.setStatus("mandatory")
_CConfigArp_ObjectIdentity = ObjectIdentity
cConfigArp = _CConfigArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 2)
)
_CConfigTcp_ObjectIdentity = ObjectIdentity
cConfigTcp = _CConfigTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 3)
)
_CTcpKeepalive_Type = Integer32
_CTcpKeepalive_Object = MibScalar
cTcpKeepalive = _CTcpKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 3, 1),
    _CTcpKeepalive_Type()
)
cTcpKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTcpKeepalive.setStatus("mandatory")
_CConfigTelnet_ObjectIdentity = ObjectIdentity
cConfigTelnet = _CConfigTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 4)
)
_CTelnetPort_Type = Integer32
_CTelnetPort_Object = MibScalar
cTelnetPort = _CTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 4, 1),
    _CTelnetPort_Type()
)
cTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTelnetPort.setStatus("mandatory")


class _CTelnetNegotiate_Type(Integer32):
    """Custom type cTelnetNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CTelnetNegotiate_Type.__name__ = "Integer32"
_CTelnetNegotiate_Object = MibScalar
cTelnetNegotiate = _CTelnetNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 4, 2),
    _CTelnetNegotiate_Type()
)
cTelnetNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTelnetNegotiate.setStatus("mandatory")
_CConfigHostTable_ObjectIdentity = ObjectIdentity
cConfigHostTable = _CConfigHostTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 10, 5)
)
_CConfigSoftwareQueues_ObjectIdentity = ObjectIdentity
cConfigSoftwareQueues = _CConfigSoftwareQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 11)
)
_CEtherSWQTable_Object = MibTable
cEtherSWQTable = _CEtherSWQTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 11, 1)
)
if mibBuilder.loadTexts:
    cEtherSWQTable.setStatus("mandatory")
_CEtherSWQEntry_Object = MibTableRow
cEtherSWQEntry = _CEtherSWQEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 11, 1, 1)
)
cEtherSWQEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cEtherSWQIndex"),
)
if mibBuilder.loadTexts:
    cEtherSWQEntry.setStatus("mandatory")


class _CEtherSWQIndex_Type(Integer32):
    """Custom type cEtherSWQIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CEtherSWQIndex_Type.__name__ = "Integer32"
_CEtherSWQIndex_Object = MibTableColumn
cEtherSWQIndex = _CEtherSWQIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 11, 1, 1, 1),
    _CEtherSWQIndex_Type()
)
cEtherSWQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEtherSWQIndex.setStatus("mandatory")


class _CEtherSWQMaxSize_Type(Integer32):
    """Custom type cEtherSWQMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CEtherSWQMaxSize_Type.__name__ = "Integer32"
_CEtherSWQMaxSize_Object = MibTableColumn
cEtherSWQMaxSize = _CEtherSWQMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 11, 1, 1, 2),
    _CEtherSWQMaxSize_Type()
)
cEtherSWQMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cEtherSWQMaxSize.setStatus("mandatory")


class _CEtherSWQMaxTtl_Type(Integer32):
    """Custom type cEtherSWQMaxTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_CEtherSWQMaxTtl_Type.__name__ = "Integer32"
_CEtherSWQMaxTtl_Object = MibTableColumn
cEtherSWQMaxTtl = _CEtherSWQMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 11, 1, 1, 3),
    _CEtherSWQMaxTtl_Type()
)
cEtherSWQMaxTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cEtherSWQMaxTtl.setStatus("mandatory")
_CResetNovram_Type = Integer32
_CResetNovram_Object = MibScalar
cResetNovram = _CResetNovram_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 12),
    _CResetNovram_Type()
)
cResetNovram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cResetNovram.setStatus("mandatory")
_CRestartSystem_Type = Integer32
_CRestartSystem_Object = MibScalar
cRestartSystem = _CRestartSystem_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 13),
    _CRestartSystem_Type()
)
cRestartSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRestartSystem.setStatus("mandatory")
_CConfigFlashDnld_ObjectIdentity = ObjectIdentity
cConfigFlashDnld = _CConfigFlashDnld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 6, 14)
)
_CFlashIpAddress_Type = IpAddress
_CFlashIpAddress_Object = MibScalar
cFlashIpAddress = _CFlashIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 14, 1),
    _CFlashIpAddress_Type()
)
cFlashIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFlashIpAddress.setStatus("mandatory")


class _CFlashFileName_Type(OctetString):
    """Custom type cFlashFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CFlashFileName_Type.__name__ = "OctetString"
_CFlashFileName_Object = MibScalar
cFlashFileName = _CFlashFileName_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 14, 2),
    _CFlashFileName_Type()
)
cFlashFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFlashFileName.setStatus("mandatory")


class _CFlashBootFlag_Type(Integer32):
    """Custom type cFlashBootFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CFlashBootFlag_Type.__name__ = "Integer32"
_CFlashBootFlag_Object = MibScalar
cFlashBootFlag = _CFlashBootFlag_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 14, 3),
    _CFlashBootFlag_Type()
)
cFlashBootFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFlashBootFlag.setStatus("mandatory")
_CFlashGatewayIpAddr_Type = IpAddress
_CFlashGatewayIpAddr_Object = MibScalar
cFlashGatewayIpAddr = _CFlashGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 187, 6, 14, 4),
    _CFlashGatewayIpAddr_Type()
)
cFlashGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFlashGatewayIpAddr.setStatus("mandatory")
_CMonitor_ObjectIdentity = ObjectIdentity
cMonitor = _CMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7)
)
_CMonitorSystem_ObjectIdentity = ObjectIdentity
cMonitorSystem = _CMonitorSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 1)
)
_CMonitorSystemInfo_ObjectIdentity = ObjectIdentity
cMonitorSystemInfo = _CMonitorSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 1)
)
_CMonitorHeapStats_ObjectIdentity = ObjectIdentity
cMonitorHeapStats = _CMonitorHeapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 2)
)
_CMonitorLoginHistory_ObjectIdentity = ObjectIdentity
cMonitorLoginHistory = _CMonitorLoginHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3)
)
_CLoginTable_Object = MibTable
cLoginTable = _CLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLoginTable.setStatus("mandatory")
_CLoginEntry_Object = MibTableRow
cLoginEntry = _CLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 1, 1)
)
cLoginEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cLoginIndex"),
)
if mibBuilder.loadTexts:
    cLoginEntry.setStatus("mandatory")
_CLoginIndex_Type = Integer32
_CLoginIndex_Object = MibTableColumn
cLoginIndex = _CLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 1, 1, 1),
    _CLoginIndex_Type()
)
cLoginIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLoginIndex.setStatus("mandatory")


class _CLoginUser_Type(OctetString):
    """Custom type cLoginUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CLoginUser_Type.__name__ = "OctetString"
_CLoginUser_Object = MibTableColumn
cLoginUser = _CLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 1, 1, 2),
    _CLoginUser_Type()
)
cLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLoginUser.setStatus("mandatory")


class _CLoginLocal_Type(Integer32):
    """Custom type cLoginLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CLoginLocal_Type.__name__ = "Integer32"
_CLoginLocal_Object = MibTableColumn
cLoginLocal = _CLoginLocal_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 1, 1, 3),
    _CLoginLocal_Type()
)
cLoginLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLoginLocal.setStatus("mandatory")
_CLoginRemote_Type = IpAddress
_CLoginRemote_Object = MibTableColumn
cLoginRemote = _CLoginRemote_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 1, 1, 4),
    _CLoginRemote_Type()
)
cLoginRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLoginRemote.setStatus("mandatory")
_CLoginFails_Type = Counter32
_CLoginFails_Object = MibScalar
cLoginFails = _CLoginFails_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 1, 3, 2),
    _CLoginFails_Type()
)
cLoginFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLoginFails.setStatus("mandatory")
_CMonitorBridges_ObjectIdentity = ObjectIdentity
cMonitorBridges = _CMonitorBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 2)
)
_CNodeByAddressTable_Object = MibTable
cNodeByAddressTable = _CNodeByAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 3)
)
if mibBuilder.loadTexts:
    cNodeByAddressTable.setStatus("mandatory")
_CNodeByAddressEntry_Object = MibTableRow
cNodeByAddressEntry = _CNodeByAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 3, 1)
)
cNodeByAddressEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cNodeByAddressAddr"),
)
if mibBuilder.loadTexts:
    cNodeByAddressEntry.setStatus("mandatory")


class _CNodeByAddressAddr_Type(OctetString):
    """Custom type cNodeByAddressAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CNodeByAddressAddr_Type.__name__ = "OctetString"
_CNodeByAddressAddr_Object = MibTableColumn
cNodeByAddressAddr = _CNodeByAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 3, 1, 1),
    _CNodeByAddressAddr_Type()
)
cNodeByAddressAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByAddressAddr.setStatus("mandatory")


class _CNodeByAddressBridge_Type(Integer32):
    """Custom type cNodeByAddressBridge based on Integer32"""
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
        *(("lb0", 1),
          ("lb1", 2),
          ("lb2", 3),
          ("lb3", 4))
    )


_CNodeByAddressBridge_Type.__name__ = "Integer32"
_CNodeByAddressBridge_Object = MibTableColumn
cNodeByAddressBridge = _CNodeByAddressBridge_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 3, 1, 2),
    _CNodeByAddressBridge_Type()
)
cNodeByAddressBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByAddressBridge.setStatus("mandatory")
_CNodeByAddressPort_Type = Integer32
_CNodeByAddressPort_Object = MibTableColumn
cNodeByAddressPort = _CNodeByAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 3, 1, 3),
    _CNodeByAddressPort_Type()
)
cNodeByAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByAddressPort.setStatus("mandatory")


class _CNodeByAddressStatus_Type(Integer32):
    """Custom type cNodeByAddressStatus based on Integer32"""
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
        *(("appeared", 3),
          ("notAppeared", 4),
          ("permanent", 1),
          ("port", 2))
    )


_CNodeByAddressStatus_Type.__name__ = "Integer32"
_CNodeByAddressStatus_Object = MibTableColumn
cNodeByAddressStatus = _CNodeByAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 3, 1, 4),
    _CNodeByAddressStatus_Type()
)
cNodeByAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByAddressStatus.setStatus("mandatory")
_CNodeByHashTable_Object = MibTable
cNodeByHashTable = _CNodeByHashTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4)
)
if mibBuilder.loadTexts:
    cNodeByHashTable.setStatus("mandatory")
_CNodeByHashEntry_Object = MibTableRow
cNodeByHashEntry = _CNodeByHashEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1)
)
cNodeByHashEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cNodeByHashIndex"),
)
if mibBuilder.loadTexts:
    cNodeByHashEntry.setStatus("mandatory")
_CNodeByHashIndex_Type = Integer32
_CNodeByHashIndex_Object = MibTableColumn
cNodeByHashIndex = _CNodeByHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1, 1),
    _CNodeByHashIndex_Type()
)
cNodeByHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByHashIndex.setStatus("mandatory")


class _CNodeByHashBucket_Type(Integer32):
    """Custom type cNodeByHashBucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CNodeByHashBucket_Type.__name__ = "Integer32"
_CNodeByHashBucket_Object = MibTableColumn
cNodeByHashBucket = _CNodeByHashBucket_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1, 2),
    _CNodeByHashBucket_Type()
)
cNodeByHashBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByHashBucket.setStatus("mandatory")


class _CNodeByHashAddress_Type(OctetString):
    """Custom type cNodeByHashAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CNodeByHashAddress_Type.__name__ = "OctetString"
_CNodeByHashAddress_Object = MibTableColumn
cNodeByHashAddress = _CNodeByHashAddress_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1, 3),
    _CNodeByHashAddress_Type()
)
cNodeByHashAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByHashAddress.setStatus("mandatory")


class _CNodeByHashBridge_Type(Integer32):
    """Custom type cNodeByHashBridge based on Integer32"""
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
        *(("lb0", 1),
          ("lb1", 2),
          ("lb2", 3),
          ("lb3", 4))
    )


_CNodeByHashBridge_Type.__name__ = "Integer32"
_CNodeByHashBridge_Object = MibTableColumn
cNodeByHashBridge = _CNodeByHashBridge_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1, 4),
    _CNodeByHashBridge_Type()
)
cNodeByHashBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByHashBridge.setStatus("mandatory")
_CNodeByHashPort_Type = Integer32
_CNodeByHashPort_Object = MibTableColumn
cNodeByHashPort = _CNodeByHashPort_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1, 5),
    _CNodeByHashPort_Type()
)
cNodeByHashPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByHashPort.setStatus("mandatory")


class _CNodeByHashStatus_Type(Integer32):
    """Custom type cNodeByHashStatus based on Integer32"""
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
        *(("appeared", 3),
          ("notAppeared", 4),
          ("permanent", 1),
          ("port", 2))
    )


_CNodeByHashStatus_Type.__name__ = "Integer32"
_CNodeByHashStatus_Object = MibTableColumn
cNodeByHashStatus = _CNodeByHashStatus_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 2, 4, 1, 6),
    _CNodeByHashStatus_Type()
)
cNodeByHashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNodeByHashStatus.setStatus("mandatory")
_CMonitorPhysInterfaces_ObjectIdentity = ObjectIdentity
cMonitorPhysInterfaces = _CMonitorPhysInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 3)
)
_CHardwareStatusTable_Object = MibTable
cHardwareStatusTable = _CHardwareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1)
)
if mibBuilder.loadTexts:
    cHardwareStatusTable.setStatus("mandatory")
_CHardwareStatusEntry_Object = MibTableRow
cHardwareStatusEntry = _CHardwareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1)
)
cHardwareStatusEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cHardwareStatusIndex"),
)
if mibBuilder.loadTexts:
    cHardwareStatusEntry.setStatus("mandatory")


class _CHardwareStatusIndex_Type(Integer32):
    """Custom type cHardwareStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CHardwareStatusIndex_Type.__name__ = "Integer32"
_CHardwareStatusIndex_Object = MibTableColumn
cHardwareStatusIndex = _CHardwareStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 1),
    _CHardwareStatusIndex_Type()
)
cHardwareStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusIndex.setStatus("mandatory")


class _CHardwareStatusSlot_Type(Integer32):
    """Custom type cHardwareStatusSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_CHardwareStatusSlot_Type.__name__ = "Integer32"
_CHardwareStatusSlot_Object = MibTableColumn
cHardwareStatusSlot = _CHardwareStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 2),
    _CHardwareStatusSlot_Type()
)
cHardwareStatusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusSlot.setStatus("mandatory")
_CHardwareStatusContents_Type = DisplayString
_CHardwareStatusContents_Object = MibTableColumn
cHardwareStatusContents = _CHardwareStatusContents_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 3),
    _CHardwareStatusContents_Type()
)
cHardwareStatusContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusContents.setStatus("mandatory")


class _CHardwareStatusMacAddr_Type(OctetString):
    """Custom type cHardwareStatusMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CHardwareStatusMacAddr_Type.__name__ = "OctetString"
_CHardwareStatusMacAddr_Object = MibTableColumn
cHardwareStatusMacAddr = _CHardwareStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 4),
    _CHardwareStatusMacAddr_Type()
)
cHardwareStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusMacAddr.setStatus("mandatory")
_CHardwareStatusSerialNo_Type = OctetString
_CHardwareStatusSerialNo_Object = MibTableColumn
cHardwareStatusSerialNo = _CHardwareStatusSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 5),
    _CHardwareStatusSerialNo_Type()
)
cHardwareStatusSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusSerialNo.setStatus("mandatory")
_CHardwareStatusRevision_Type = OctetString
_CHardwareStatusRevision_Object = MibTableColumn
cHardwareStatusRevision = _CHardwareStatusRevision_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 6),
    _CHardwareStatusRevision_Type()
)
cHardwareStatusRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusRevision.setStatus("mandatory")
_CHardwareStatusStatus_Type = DisplayString
_CHardwareStatusStatus_Object = MibTableColumn
cHardwareStatusStatus = _CHardwareStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 3, 1, 1, 7),
    _CHardwareStatusStatus_Type()
)
cHardwareStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHardwareStatusStatus.setStatus("mandatory")
_CMonitorProto_ObjectIdentity = ObjectIdentity
cMonitorProto = _CMonitorProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 4)
)
_CTcpStats_ObjectIdentity = ObjectIdentity
cTcpStats = _CTcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 4, 3)
)
_CIpStats_ObjectIdentity = ObjectIdentity
cIpStats = _CIpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 4, 4)
)
_CIcmpStats_ObjectIdentity = ObjectIdentity
cIcmpStats = _CIcmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 4, 5)
)
_CWanStats_ObjectIdentity = ObjectIdentity
cWanStats = _CWanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 4, 9)
)
_CMonitorIpRouter_ObjectIdentity = ObjectIdentity
cMonitorIpRouter = _CMonitorIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 5)
)
_CIpRoutingStats_ObjectIdentity = ObjectIdentity
cIpRoutingStats = _CIpRoutingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 5, 1)
)
_CEgpStats_ObjectIdentity = ObjectIdentity
cEgpStats = _CEgpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 5, 3)
)
_CRipStats_ObjectIdentity = ObjectIdentity
cRipStats = _CRipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 5, 5)
)
_CHelloStats_ObjectIdentity = ObjectIdentity
cHelloStats = _CHelloStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 5, 6)
)
_CMonitorIpxRouter_ObjectIdentity = ObjectIdentity
cMonitorIpxRouter = _CMonitorIpxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 6)
)
_CIpxStats_ObjectIdentity = ObjectIdentity
cIpxStats = _CIpxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 6, 1)
)
_CMonitorAtRouter_ObjectIdentity = ObjectIdentity
cMonitorAtRouter = _CMonitorAtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 7)
)
_CAtRouterStats_ObjectIdentity = ObjectIdentity
cAtRouterStats = _CAtRouterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 7, 1)
)
_CDiagnostics_ObjectIdentity = ObjectIdentity
cDiagnostics = _CDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 187, 7, 8)
)
_CClearErrorLog_Type = Integer32
_CClearErrorLog_Object = MibScalar
cClearErrorLog = _CClearErrorLog_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 8, 1),
    _CClearErrorLog_Type()
)
cClearErrorLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cClearErrorLog.setStatus("mandatory")
_CErrorLogTable_Object = MibTable
cErrorLogTable = _CErrorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 8, 2)
)
if mibBuilder.loadTexts:
    cErrorLogTable.setStatus("mandatory")
_CErrorLogEntry_Object = MibTableRow
cErrorLogEntry = _CErrorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 8, 2, 1)
)
cErrorLogEntry.setIndexNames(
    (0, "LBHUB-MSH4PTBRDG-MIB", "cErrorLogIndex"),
)
if mibBuilder.loadTexts:
    cErrorLogEntry.setStatus("mandatory")
_CErrorLogIndex_Type = Integer32
_CErrorLogIndex_Object = MibTableColumn
cErrorLogIndex = _CErrorLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 8, 2, 1, 1),
    _CErrorLogIndex_Type()
)
cErrorLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cErrorLogIndex.setStatus("mandatory")


class _CErrorLogMessage_Type(OctetString):
    """Custom type cErrorLogMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CErrorLogMessage_Type.__name__ = "OctetString"
_CErrorLogMessage_Object = MibTableColumn
cErrorLogMessage = _CErrorLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 187, 7, 8, 2, 1, 2),
    _CErrorLogMessage_Type()
)
cErrorLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cErrorLogMessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 1)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        ""
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 2)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LBHUB-MSH4PTBRDG-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "Timeout": Timeout,
       "mib-2": mib_2,
       "system": system,
       "interfaces": interfaces,
       "ip": ip,
       "icmp": icmp,
       "tcp": tcp,
       "udp": udp,
       "egp": egp,
       "transmission": transmission,
       "dot3": dot3,
       "dot3Table": dot3Table,
       "dot3Entry": dot3Entry,
       "dot3Index": dot3Index,
       "dot3InitializeMac": dot3InitializeMac,
       "dot3MacSubLayerStatus": dot3MacSubLayerStatus,
       "dot3MulticastReceiveStatus": dot3MulticastReceiveStatus,
       "dot3TxEnabled": dot3TxEnabled,
       "dot3TestTdrValue": dot3TestTdrValue,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsSQETestErrors": dot3StatsSQETestErrors,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsInternalMacTransmitErrors": dot3StatsInternalMacTransmitErrors,
       "dot3StatsCarrierSenseErrors": dot3StatsCarrierSenseErrors,
       "dot3StatsExcessiveDeferrals": dot3StatsExcessiveDeferrals,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsInRangeLengthErrors": dot3StatsInRangeLengthErrors,
       "dot3StatsOutOfRangeLengthFields": dot3StatsOutOfRangeLengthFields,
       "dot3StatsInternalMacReceiveErrors": dot3StatsInternalMacReceiveErrors,
       "dot3ChipSets": dot3ChipSets,
       "dot3ChipSetAMD": dot3ChipSetAMD,
       "dot3ChipSetAMD7990": dot3ChipSetAMD7990,
       "dot3ChipSetAMD79900": dot3ChipSetAMD79900,
       "snmp": snmp,
       "ifExtensions": ifExtensions,
       "ifExtnsTable": ifExtnsTable,
       "ifExtnsEntry": ifExtnsEntry,
       "ifExtnsIfIndex": ifExtnsIfIndex,
       "ifExtnsChipSet": ifExtnsChipSet,
       "ifExtnsRevWare": ifExtnsRevWare,
       "ifExtnsMulticastsTransmittedOks": ifExtnsMulticastsTransmittedOks,
       "ifExtnsBroadcastsTransmittedOks": ifExtnsBroadcastsTransmittedOks,
       "ifExtnsMulticastsReceivedOks": ifExtnsMulticastsReceivedOks,
       "ifExtnsBroadcastsReceivedOks": ifExtnsBroadcastsReceivedOks,
       "ifExtnsPromiscuous": ifExtnsPromiscuous,
       "ifExtnsRcvAddrTable": ifExtnsRcvAddrTable,
       "ifExtnsRcvAddrEntry": ifExtnsRcvAddrEntry,
       "ifExtnsRcvAddrIfIndex": ifExtnsRcvAddrIfIndex,
       "ifExtnsRcvAddress": ifExtnsRcvAddress,
       "ifExtnsRcvAddrStatus": ifExtnsRcvAddrStatus,
       "dot1dBridge": dot1dBridge,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "private": private,
       "enterprises": enterprises,
       "constellation": constellation,
       "cExper": cExper,
       "cProducts": cProducts,
       "cLittleDipper": cLittleDipper,
       "cAuriga": cAuriga,
       "cCarina": cCarina,
       "cCarinaAui": cCarinaAui,
       "cCarinaBnc": cCarinaBnc,
       "cDuPont": cDuPont,
       "cDuPontAui": cDuPontAui,
       "cDatabil": cDatabil,
       "cDatability": cDatability,
       "cPenr": cPenr,
       "cPenril": cPenril,
       "cThreeCom": cThreeCom,
       "cThreeComMSH": cThreeComMSH,
       "cStdExtensions": cStdExtensions,
       "cSystem": cSystem,
       "cInterfaces": cInterfaces,
       "cIp": cIp,
       "cIpInLenErrors": cIpInLenErrors,
       "cIpInVersionErrors": cIpInVersionErrors,
       "cIpInCSErrors": cIpInCSErrors,
       "cIpTTLZero": cIpTTLZero,
       "cIpReasmTimeOuts": cIpReasmTimeOuts,
       "cIpNetToMedia": cIpNetToMedia,
       "cIpNetToMediaTableSize": cIpNetToMediaTableSize,
       "cIpNetToMediaCompleteTimeOut": cIpNetToMediaCompleteTimeOut,
       "cIpNetToMediaInCompleteTimeOut": cIpNetToMediaInCompleteTimeOut,
       "cIpNetToMediaIns": cIpNetToMediaIns,
       "cIpNetToMediaInLenErrs": cIpNetToMediaInLenErrs,
       "cIpNetToMediaInNotEther": cIpNetToMediaInNotEther,
       "cIpNetToMediaInNoArpOnIf": cIpNetToMediaInNoArpOnIf,
       "cIpNetToMediaInIp": cIpNetToMediaInIp,
       "cIpNetToMediaInIpTrailers": cIpNetToMediaInIpTrailers,
       "cIpNetToMediaInUnkProtos": cIpNetToMediaInUnkProtos,
       "cIpNetToMediaInSourceBcast": cIpNetToMediaInSourceBcast,
       "cIpNetToMediaInDups": cIpNetToMediaInDups,
       "cIpNetToMediaInRequests": cIpNetToMediaInRequests,
       "cIpNetToMediaInResponses": cIpNetToMediaInResponses,
       "cIpNetToMediaInProxyOks": cIpNetToMediaInProxyOks,
       "cIpNetToMediaOutReplys": cIpNetToMediaOutReplys,
       "cIpNetToMediaOutRequests": cIpNetToMediaOutRequests,
       "cIpNetToMediaReqBadAddrs": cIpNetToMediaReqBadAddrs,
       "cIpNetToMediaNoResponses": cIpNetToMediaNoResponses,
       "cIpNetToMediaAgeOuts": cIpNetToMediaAgeOuts,
       "cIpNetToMediaTable": cIpNetToMediaTable,
       "cIpNetToMediaEntry": cIpNetToMediaEntry,
       "cIpNetToMediaIfIndex": cIpNetToMediaIfIndex,
       "cIpNetToMediaNetAddress": cIpNetToMediaNetAddress,
       "cIpNetToMediaRefTime": cIpNetToMediaRefTime,
       "cIpNetToMediaProxyRespond": cIpNetToMediaProxyRespond,
       "cIpNetToMediaComplete": cIpNetToMediaComplete,
       "cIpNetToMediaUseTrailers": cIpNetToMediaUseTrailers,
       "cIcmp": cIcmp,
       "cIcmpInRedirectNet": cIcmpInRedirectNet,
       "cIcmpInRedirectHost": cIcmpInRedirectHost,
       "cIcmpInRedirectNetTos": cIcmpInRedirectNetTos,
       "cIcmpInRedirectHostTos": cIcmpInRedirectHostTos,
       "cIcmpInTimeExcTTL": cIcmpInTimeExcTTL,
       "cIcmpInTimeExcReAsm": cIcmpInTimeExcReAsm,
       "cIcmpInDestUnNet": cIcmpInDestUnNet,
       "cIcmpInDestUnHost": cIcmpInDestUnHost,
       "cIcmpInDestUnProtocol": cIcmpInDestUnProtocol,
       "cIcmpInDestUnPort": cIcmpInDestUnPort,
       "cIcmpInDestUnFragNeeded": cIcmpInDestUnFragNeeded,
       "cIcmpInDestUnSourceRoute": cIcmpInDestUnSourceRoute,
       "cIcmpOutRedirectNet": cIcmpOutRedirectNet,
       "cIcmpOutRedirectHost": cIcmpOutRedirectHost,
       "cIcmpOutRedirectNetTos": cIcmpOutRedirectNetTos,
       "cIcmpOutRedirectHostTos": cIcmpOutRedirectHostTos,
       "cIcmpOutTimeExcTTL": cIcmpOutTimeExcTTL,
       "cIcmpOutTimeExcReAsm": cIcmpOutTimeExcReAsm,
       "cIcmpOutDestUnNet": cIcmpOutDestUnNet,
       "cIcmpOutDestUnHost": cIcmpOutDestUnHost,
       "cIcmpOutDestUnProtocol": cIcmpOutDestUnProtocol,
       "cIcmpOutDestUnPort": cIcmpOutDestUnPort,
       "cIcmpOutDestUnFragNeeded": cIcmpOutDestUnFragNeeded,
       "cIcmpOutDestUnSourceRoute": cIcmpOutDestUnSourceRoute,
       "cIcmpInLengthErrors": cIcmpInLengthErrors,
       "cIcmpInChecksumErrors": cIcmpInChecksumErrors,
       "cIcmpInUnkTypes": cIcmpInUnkTypes,
       "cIcmpInDestUnNetUnknown": cIcmpInDestUnNetUnknown,
       "cIcmpInDestUnHostUnknown": cIcmpInDestUnHostUnknown,
       "cIcmpInDestUnSrcIsolated": cIcmpInDestUnSrcIsolated,
       "cIcmpInDestUnHostProhib": cIcmpInDestUnHostProhib,
       "cIcmpInDestUnNetProhib": cIcmpInDestUnNetProhib,
       "cIcmpInDestUnNetTos": cIcmpInDestUnNetTos,
       "cIcmpInDestUnHostTos": cIcmpInDestUnHostTos,
       "cIcmpOutDestUnNetUnknown": cIcmpOutDestUnNetUnknown,
       "cIcmpOutDestUnHostUnknown": cIcmpOutDestUnHostUnknown,
       "cIcmpOutDestUnSrcIsolated": cIcmpOutDestUnSrcIsolated,
       "cIcmpOutDestUnHostProhib": cIcmpOutDestUnHostProhib,
       "cIcmpOutDestUnNetProhib": cIcmpOutDestUnNetProhib,
       "cIcmpOutDestUnNetTos": cIcmpOutDestUnNetTos,
       "cIcmpOutDestUnHostTos": cIcmpOutDestUnHostTos,
       "cIcmpInParmProbMissingOpt": cIcmpInParmProbMissingOpt,
       "cIcmpOutParmProbMissingOpt": cIcmpOutParmProbMissingOpt,
       "cTcp": cTcp,
       "cUdp": cUdp,
       "cUdpHdrDrops": cUdpHdrDrops,
       "cUdpBadCheckSum": cUdpBadCheckSum,
       "cUdpBadLength": cUdpBadLength,
       "cUdpOtherErrors": cUdpOtherErrors,
       "cUdpNoChecksum": cUdpNoChecksum,
       "cTransmission": cTransmission,
       "cDot3": cDot3,
       "cDot3Table": cDot3Table,
       "cDot3Entry": cDot3Entry,
       "cDot3Index": cDot3Index,
       "cDot3Disables": cDot3Disables,
       "cDot3MauDisconnect": cDot3MauDisconnect,
       "cDot3Babbles": cDot3Babbles,
       "cDot3MerrDisconnect": cDot3MerrDisconnect,
       "cDot3TxonDisconnect": cDot3TxonDisconnect,
       "cDot3RxonDisconnect": cDot3RxonDisconnect,
       "cDot3XmitFailure": cDot3XmitFailure,
       "cDot3XmitBuffErr": cDot3XmitBuffErr,
       "cDot3XmitUflo": cDot3XmitUflo,
       "cDot3RcvBuffErr": cDot3RcvBuffErr,
       "cDot3RcvOflo": cDot3RcvOflo,
       "cDot3Startless": cDot3Startless,
       "cDot3Endless": cDot3Endless,
       "cSnmp": cSnmp,
       "cSnmpCommunities": cSnmpCommunities,
       "cSnmpInCommunityMessages": cSnmpInCommunityMessages,
       "cConstellation": cConstellation,
       "cConstellationAvailableBuffers": cConstellationAvailableBuffers,
       "cConstellationInitialBuffers": cConstellationInitialBuffers,
       "cConstallationBufferDataLength": cConstallationBufferDataLength,
       "cConstellationInstructionRam": cConstellationInstructionRam,
       "cConstellationGlobalDataRam": cConstellationGlobalDataRam,
       "cConstellationFastDataRam": cConstellationFastDataRam,
       "cProxys": cProxys,
       "cProxyLb": cProxyLb,
       "cProxyLb0": cProxyLb0,
       "cProxyLb1": cProxyLb1,
       "cProxyLb2": cProxyLb2,
       "cProxyLb3": cProxyLb3,
       "cProxyLr": cProxyLr,
       "cProxyLr0": cProxyLr0,
       "cConfig": cConfig,
       "cConfigSystem": cConfigSystem,
       "cConfSysInfo": cConfSysInfo,
       "cLocalTime": cLocalTime,
       "cLocalDate": cLocalDate,
       "cLocalCtpMode": cLocalCtpMode,
       "cRemoteCtpMode": cRemoteCtpMode,
       "cBridgeStatsAveraging": cBridgeStatsAveraging,
       "cBranchTargetCache": cBranchTargetCache,
       "cConfOperAcct": cConfOperAcct,
       "cOperAcctTable": cOperAcctTable,
       "cOperAcctEntry": cOperAcctEntry,
       "cOperIndex": cOperIndex,
       "cOperID": cOperID,
       "cOperPriv": cOperPriv,
       "cOperPasswd": cOperPasswd,
       "cOperStatus": cOperStatus,
       "cConfigLan": cConfigLan,
       "cConfigEther": cConfigEther,
       "cConfigTwp": cConfigTwp,
       "cConfigWan": cConfigWan,
       "cConfigSerChan": cConfigSerChan,
       "cConfigWideAreaGroups": cConfigWideAreaGroups,
       "cConfigBridge": cConfigBridge,
       "cConfigLogicalBridge": cConfigLogicalBridge,
       "cIpAddress": cIpAddress,
       "cConfigIpRouter": cConfigIpRouter,
       "cConfigAcceptLists": cConfigAcceptLists,
       "cConfigPropagateLists": cConfigPropagateLists,
       "cIpFilters": cIpFilters,
       "cConfigIpxRouter": cConfigIpxRouter,
       "cConfigIpxBridgeIf": cConfigIpxBridgeIf,
       "cConfigIpxRouterFilters": cConfigIpxRouterFilters,
       "cConfigAppleTalk": cConfigAppleTalk,
       "cConfigAtIf": cConfigAtIf,
       "cConfigNetProtocol": cConfigNetProtocol,
       "cConfigSnmp": cConfigSnmp,
       "cSnmpCommunityTable": cSnmpCommunityTable,
       "cSnmpCommunityEntry": cSnmpCommunityEntry,
       "cSnmpCommunityIndex": cSnmpCommunityIndex,
       "cSnmpCommunity": cSnmpCommunity,
       "cSnmpCommunityIf": cSnmpCommunityIf,
       "cSnmpCommunityAccess": cSnmpCommunityAccess,
       "cSnmpCommunityTrapAddress": cSnmpCommunityTrapAddress,
       "cSnmpCommunityTrapPort": cSnmpCommunityTrapPort,
       "cSnmpCommunityTrapEnabled": cSnmpCommunityTrapEnabled,
       "cConfigArp": cConfigArp,
       "cConfigTcp": cConfigTcp,
       "cTcpKeepalive": cTcpKeepalive,
       "cConfigTelnet": cConfigTelnet,
       "cTelnetPort": cTelnetPort,
       "cTelnetNegotiate": cTelnetNegotiate,
       "cConfigHostTable": cConfigHostTable,
       "cConfigSoftwareQueues": cConfigSoftwareQueues,
       "cEtherSWQTable": cEtherSWQTable,
       "cEtherSWQEntry": cEtherSWQEntry,
       "cEtherSWQIndex": cEtherSWQIndex,
       "cEtherSWQMaxSize": cEtherSWQMaxSize,
       "cEtherSWQMaxTtl": cEtherSWQMaxTtl,
       "cResetNovram": cResetNovram,
       "cRestartSystem": cRestartSystem,
       "cConfigFlashDnld": cConfigFlashDnld,
       "cFlashIpAddress": cFlashIpAddress,
       "cFlashFileName": cFlashFileName,
       "cFlashBootFlag": cFlashBootFlag,
       "cFlashGatewayIpAddr": cFlashGatewayIpAddr,
       "cMonitor": cMonitor,
       "cMonitorSystem": cMonitorSystem,
       "cMonitorSystemInfo": cMonitorSystemInfo,
       "cMonitorHeapStats": cMonitorHeapStats,
       "cMonitorLoginHistory": cMonitorLoginHistory,
       "cLoginTable": cLoginTable,
       "cLoginEntry": cLoginEntry,
       "cLoginIndex": cLoginIndex,
       "cLoginUser": cLoginUser,
       "cLoginLocal": cLoginLocal,
       "cLoginRemote": cLoginRemote,
       "cLoginFails": cLoginFails,
       "cMonitorBridges": cMonitorBridges,
       "cNodeByAddressTable": cNodeByAddressTable,
       "cNodeByAddressEntry": cNodeByAddressEntry,
       "cNodeByAddressAddr": cNodeByAddressAddr,
       "cNodeByAddressBridge": cNodeByAddressBridge,
       "cNodeByAddressPort": cNodeByAddressPort,
       "cNodeByAddressStatus": cNodeByAddressStatus,
       "cNodeByHashTable": cNodeByHashTable,
       "cNodeByHashEntry": cNodeByHashEntry,
       "cNodeByHashIndex": cNodeByHashIndex,
       "cNodeByHashBucket": cNodeByHashBucket,
       "cNodeByHashAddress": cNodeByHashAddress,
       "cNodeByHashBridge": cNodeByHashBridge,
       "cNodeByHashPort": cNodeByHashPort,
       "cNodeByHashStatus": cNodeByHashStatus,
       "cMonitorPhysInterfaces": cMonitorPhysInterfaces,
       "cHardwareStatusTable": cHardwareStatusTable,
       "cHardwareStatusEntry": cHardwareStatusEntry,
       "cHardwareStatusIndex": cHardwareStatusIndex,
       "cHardwareStatusSlot": cHardwareStatusSlot,
       "cHardwareStatusContents": cHardwareStatusContents,
       "cHardwareStatusMacAddr": cHardwareStatusMacAddr,
       "cHardwareStatusSerialNo": cHardwareStatusSerialNo,
       "cHardwareStatusRevision": cHardwareStatusRevision,
       "cHardwareStatusStatus": cHardwareStatusStatus,
       "cMonitorProto": cMonitorProto,
       "cTcpStats": cTcpStats,
       "cIpStats": cIpStats,
       "cIcmpStats": cIcmpStats,
       "cWanStats": cWanStats,
       "cMonitorIpRouter": cMonitorIpRouter,
       "cIpRoutingStats": cIpRoutingStats,
       "cEgpStats": cEgpStats,
       "cRipStats": cRipStats,
       "cHelloStats": cHelloStats,
       "cMonitorIpxRouter": cMonitorIpxRouter,
       "cIpxStats": cIpxStats,
       "cMonitorAtRouter": cMonitorAtRouter,
       "cAtRouterStats": cAtRouterStats,
       "cDiagnostics": cDiagnostics,
       "cClearErrorLog": cClearErrorLog,
       "cErrorLogTable": cErrorLogTable,
       "cErrorLogEntry": cErrorLogEntry,
       "cErrorLogIndex": cErrorLogIndex,
       "cErrorLogMessage": cErrorLogMessage}
)
