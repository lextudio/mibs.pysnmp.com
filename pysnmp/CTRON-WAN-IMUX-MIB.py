# SNMP MIB module (CTRON-WAN-IMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-WAN-IMUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:54 2024
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

(ctWanServices,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctWanServices")

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

_CtWanMux_ObjectIdentity = ObjectIdentity
ctWanMux = _CtWanMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1)
)
_CtWANMuxGeneralGroup_ObjectIdentity = ObjectIdentity
ctWANMuxGeneralGroup = _CtWANMuxGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 1)
)
_CtWANMuxMaxNumGroups_Type = Integer32
_CtWANMuxMaxNumGroups_Object = MibScalar
ctWANMuxMaxNumGroups = _CtWANMuxMaxNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 1, 1),
    _CtWANMuxMaxNumGroups_Type()
)
ctWANMuxMaxNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWANMuxMaxNumGroups.setStatus("mandatory")


class _CtWanMuxAdmin_Type(Integer32):
    """Custom type ctWanMuxAdmin based on Integer32"""
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


_CtWanMuxAdmin_Type.__name__ = "Integer32"
_CtWanMuxAdmin_Object = MibScalar
ctWanMuxAdmin = _CtWanMuxAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 1, 2),
    _CtWanMuxAdmin_Type()
)
ctWanMuxAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMuxAdmin.setStatus("mandatory")
_CtWanMuxGroupTable_Object = MibTable
ctWanMuxGroupTable = _CtWanMuxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ctWanMuxGroupTable.setStatus("mandatory")
_CtWanMuxGroupEntry_Object = MibTableRow
ctWanMuxGroupEntry = _CtWanMuxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1)
)
ctWanMuxGroupEntry.setIndexNames(
    (0, "CTRON-WAN-IMUX-MIB", "ctWanMuxGroupId"),
)
if mibBuilder.loadTexts:
    ctWanMuxGroupEntry.setStatus("mandatory")


class _CtWanMuxGroupId_Type(Integer32):
    """Custom type ctWanMuxGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMuxGroupId_Type.__name__ = "Integer32"
_CtWanMuxGroupId_Object = MibTableColumn
ctWanMuxGroupId = _CtWanMuxGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 1),
    _CtWanMuxGroupId_Type()
)
ctWanMuxGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxGroupId.setStatus("mandatory")


class _CtWanMuxGroupAdmin_Type(Integer32):
    """Custom type ctWanMuxGroupAdmin based on Integer32"""
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


_CtWanMuxGroupAdmin_Type.__name__ = "Integer32"
_CtWanMuxGroupAdmin_Object = MibTableColumn
ctWanMuxGroupAdmin = _CtWanMuxGroupAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 2),
    _CtWanMuxGroupAdmin_Type()
)
ctWanMuxGroupAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMuxGroupAdmin.setStatus("mandatory")
_CtWanMuxGroupNumChannels_Type = Integer32
_CtWanMuxGroupNumChannels_Object = MibTableColumn
ctWanMuxGroupNumChannels = _CtWanMuxGroupNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 3),
    _CtWanMuxGroupNumChannels_Type()
)
ctWanMuxGroupNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxGroupNumChannels.setStatus("mandatory")
_CtWanMuxGroupAddChannel_Type = Integer32
_CtWanMuxGroupAddChannel_Object = MibTableColumn
ctWanMuxGroupAddChannel = _CtWanMuxGroupAddChannel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 4),
    _CtWanMuxGroupAddChannel_Type()
)
ctWanMuxGroupAddChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMuxGroupAddChannel.setStatus("mandatory")
_CtWanMuxGroupDelChannel_Type = Integer32
_CtWanMuxGroupDelChannel_Object = MibTableColumn
ctWanMuxGroupDelChannel = _CtWanMuxGroupDelChannel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 2, 1, 5),
    _CtWanMuxGroupDelChannel_Type()
)
ctWanMuxGroupDelChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMuxGroupDelChannel.setStatus("mandatory")
_CtWanMuxChannelTable_Object = MibTable
ctWanMuxChannelTable = _CtWanMuxChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ctWanMuxChannelTable.setStatus("mandatory")
_CtWanMuxChannelEntry_Object = MibTableRow
ctWanMuxChannelEntry = _CtWanMuxChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1)
)
ctWanMuxChannelEntry.setIndexNames(
    (0, "CTRON-WAN-IMUX-MIB", "ctWanMuxChannelGroupId"),
    (0, "CTRON-WAN-IMUX-MIB", "ctWanMuxChannelId"),
)
if mibBuilder.loadTexts:
    ctWanMuxChannelEntry.setStatus("mandatory")


class _CtWanMuxChannelGroupId_Type(Integer32):
    """Custom type ctWanMuxChannelGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMuxChannelGroupId_Type.__name__ = "Integer32"
_CtWanMuxChannelGroupId_Object = MibTableColumn
ctWanMuxChannelGroupId = _CtWanMuxChannelGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 1),
    _CtWanMuxChannelGroupId_Type()
)
ctWanMuxChannelGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelGroupId.setStatus("mandatory")


class _CtWanMuxChannelId_Type(Integer32):
    """Custom type ctWanMuxChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMuxChannelId_Type.__name__ = "Integer32"
_CtWanMuxChannelId_Object = MibTableColumn
ctWanMuxChannelId = _CtWanMuxChannelId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 2),
    _CtWanMuxChannelId_Type()
)
ctWanMuxChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelId.setStatus("mandatory")
_CtWanMuxChannelIfIndex_Type = Integer32
_CtWanMuxChannelIfIndex_Object = MibTableColumn
ctWanMuxChannelIfIndex = _CtWanMuxChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 3),
    _CtWanMuxChannelIfIndex_Type()
)
ctWanMuxChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelIfIndex.setStatus("mandatory")
_CtWanMuxChannelPhysNum_Type = Integer32
_CtWanMuxChannelPhysNum_Object = MibTableColumn
ctWanMuxChannelPhysNum = _CtWanMuxChannelPhysNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 4),
    _CtWanMuxChannelPhysNum_Type()
)
ctWanMuxChannelPhysNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelPhysNum.setStatus("mandatory")
_CtWanMuxChannelBwAvail_Type = Integer32
_CtWanMuxChannelBwAvail_Object = MibTableColumn
ctWanMuxChannelBwAvail = _CtWanMuxChannelBwAvail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 5),
    _CtWanMuxChannelBwAvail_Type()
)
ctWanMuxChannelBwAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelBwAvail.setStatus("mandatory")
_CtWanMuxChannelByteCount_Type = Integer32
_CtWanMuxChannelByteCount_Object = MibTableColumn
ctWanMuxChannelByteCount = _CtWanMuxChannelByteCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 6),
    _CtWanMuxChannelByteCount_Type()
)
ctWanMuxChannelByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelByteCount.setStatus("mandatory")


class _CtWanMuxChannelStatus_Type(Integer32):
    """Custom type ctWanMuxChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CtWanMuxChannelStatus_Type.__name__ = "Integer32"
_CtWanMuxChannelStatus_Object = MibTableColumn
ctWanMuxChannelStatus = _CtWanMuxChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 1, 3, 1, 7),
    _CtWanMuxChannelStatus_Type()
)
ctWanMuxChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMuxChannelStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-WAN-IMUX-MIB",
    **{"ctWanMux": ctWanMux,
       "ctWANMuxGeneralGroup": ctWANMuxGeneralGroup,
       "ctWANMuxMaxNumGroups": ctWANMuxMaxNumGroups,
       "ctWanMuxAdmin": ctWanMuxAdmin,
       "ctWanMuxGroupTable": ctWanMuxGroupTable,
       "ctWanMuxGroupEntry": ctWanMuxGroupEntry,
       "ctWanMuxGroupId": ctWanMuxGroupId,
       "ctWanMuxGroupAdmin": ctWanMuxGroupAdmin,
       "ctWanMuxGroupNumChannels": ctWanMuxGroupNumChannels,
       "ctWanMuxGroupAddChannel": ctWanMuxGroupAddChannel,
       "ctWanMuxGroupDelChannel": ctWanMuxGroupDelChannel,
       "ctWanMuxChannelTable": ctWanMuxChannelTable,
       "ctWanMuxChannelEntry": ctWanMuxChannelEntry,
       "ctWanMuxChannelGroupId": ctWanMuxChannelGroupId,
       "ctWanMuxChannelId": ctWanMuxChannelId,
       "ctWanMuxChannelIfIndex": ctWanMuxChannelIfIndex,
       "ctWanMuxChannelPhysNum": ctWanMuxChannelPhysNum,
       "ctWanMuxChannelBwAvail": ctWanMuxChannelBwAvail,
       "ctWanMuxChannelByteCount": ctWanMuxChannelByteCount,
       "ctWanMuxChannelStatus": ctWanMuxChannelStatus}
)
