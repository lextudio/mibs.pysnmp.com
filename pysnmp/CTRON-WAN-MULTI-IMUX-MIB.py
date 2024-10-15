# SNMP MIB module (CTRON-WAN-MULTI-IMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-WAN-MULTI-IMUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:56 2024
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

_CtWanMultiMux_ObjectIdentity = ObjectIdentity
ctWanMultiMux = _CtWanMultiMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2)
)
_CtWANMMuxGeneralGroup_ObjectIdentity = ObjectIdentity
ctWANMMuxGeneralGroup = _CtWANMMuxGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1)
)
_CtWANMMuxMaxNum_Type = Integer32
_CtWANMMuxMaxNum_Object = MibScalar
ctWANMMuxMaxNum = _CtWANMMuxMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1, 1),
    _CtWANMMuxMaxNum_Type()
)
ctWANMMuxMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWANMMuxMaxNum.setStatus("mandatory")
_CtWanMMuxTable_Object = MibTable
ctWanMMuxTable = _CtWanMMuxTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ctWanMMuxTable.setStatus("mandatory")
_CtWanMMuxEntry_Object = MibTableRow
ctWanMMuxEntry = _CtWanMMuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1)
)
ctWanMMuxEntry.setIndexNames(
    (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxId"),
)
if mibBuilder.loadTexts:
    ctWanMMuxEntry.setStatus("mandatory")


class _CtWanMMuxId_Type(Integer32):
    """Custom type ctWanMMuxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxId_Type.__name__ = "Integer32"
_CtWanMMuxId_Object = MibTableColumn
ctWanMMuxId = _CtWanMMuxId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 1),
    _CtWanMMuxId_Type()
)
ctWanMMuxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxId.setStatus("mandatory")


class _CtWanMMuxIfIndex_Type(Integer32):
    """Custom type ctWanMMuxIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxIfIndex_Type.__name__ = "Integer32"
_CtWanMMuxIfIndex_Object = MibTableColumn
ctWanMMuxIfIndex = _CtWanMMuxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 2),
    _CtWanMMuxIfIndex_Type()
)
ctWanMMuxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxIfIndex.setStatus("mandatory")
_CtWanMMuxMaxNumGroups_Type = Integer32
_CtWanMMuxMaxNumGroups_Object = MibTableColumn
ctWanMMuxMaxNumGroups = _CtWanMMuxMaxNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 3),
    _CtWanMMuxMaxNumGroups_Type()
)
ctWanMMuxMaxNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxMaxNumGroups.setStatus("mandatory")


class _CtWanMMuxAdmin_Type(Integer32):
    """Custom type ctWanMMuxAdmin based on Integer32"""
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


_CtWanMMuxAdmin_Type.__name__ = "Integer32"
_CtWanMMuxAdmin_Object = MibTableColumn
ctWanMMuxAdmin = _CtWanMMuxAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 4),
    _CtWanMMuxAdmin_Type()
)
ctWanMMuxAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMMuxAdmin.setStatus("mandatory")
_CtWanMMuxGroupTable_Object = MibTable
ctWanMMuxGroupTable = _CtWanMMuxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ctWanMMuxGroupTable.setStatus("mandatory")
_CtWanMMuxGroupEntry_Object = MibTableRow
ctWanMMuxGroupEntry = _CtWanMMuxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1)
)
ctWanMMuxGroupEntry.setIndexNames(
    (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupMMuxId"),
    (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupId"),
)
if mibBuilder.loadTexts:
    ctWanMMuxGroupEntry.setStatus("mandatory")


class _CtWanMMuxGroupMMuxId_Type(Integer32):
    """Custom type ctWanMMuxGroupMMuxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxGroupMMuxId_Type.__name__ = "Integer32"
_CtWanMMuxGroupMMuxId_Object = MibTableColumn
ctWanMMuxGroupMMuxId = _CtWanMMuxGroupMMuxId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 1),
    _CtWanMMuxGroupMMuxId_Type()
)
ctWanMMuxGroupMMuxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxGroupMMuxId.setStatus("mandatory")


class _CtWanMMuxGroupId_Type(Integer32):
    """Custom type ctWanMMuxGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxGroupId_Type.__name__ = "Integer32"
_CtWanMMuxGroupId_Object = MibTableColumn
ctWanMMuxGroupId = _CtWanMMuxGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 2),
    _CtWanMMuxGroupId_Type()
)
ctWanMMuxGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxGroupId.setStatus("mandatory")


class _CtWanMMuxGroupAdmin_Type(Integer32):
    """Custom type ctWanMMuxGroupAdmin based on Integer32"""
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


_CtWanMMuxGroupAdmin_Type.__name__ = "Integer32"
_CtWanMMuxGroupAdmin_Object = MibTableColumn
ctWanMMuxGroupAdmin = _CtWanMMuxGroupAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 3),
    _CtWanMMuxGroupAdmin_Type()
)
ctWanMMuxGroupAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMMuxGroupAdmin.setStatus("mandatory")
_CtWanMMuxGroupNumChannels_Type = Integer32
_CtWanMMuxGroupNumChannels_Object = MibTableColumn
ctWanMMuxGroupNumChannels = _CtWanMMuxGroupNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 4),
    _CtWanMMuxGroupNumChannels_Type()
)
ctWanMMuxGroupNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxGroupNumChannels.setStatus("mandatory")
_CtWanMMuxGroupAddChannel_Type = Integer32
_CtWanMMuxGroupAddChannel_Object = MibTableColumn
ctWanMMuxGroupAddChannel = _CtWanMMuxGroupAddChannel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 5),
    _CtWanMMuxGroupAddChannel_Type()
)
ctWanMMuxGroupAddChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMMuxGroupAddChannel.setStatus("mandatory")
_CtWanMMuxGroupDelChannel_Type = Integer32
_CtWanMMuxGroupDelChannel_Object = MibTableColumn
ctWanMMuxGroupDelChannel = _CtWanMMuxGroupDelChannel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 6),
    _CtWanMMuxGroupDelChannel_Type()
)
ctWanMMuxGroupDelChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanMMuxGroupDelChannel.setStatus("mandatory")
_CtWanMMuxChannelTable_Object = MibTable
ctWanMMuxChannelTable = _CtWanMMuxChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ctWanMMuxChannelTable.setStatus("mandatory")
_CtWanMMuxChannelEntry_Object = MibTableRow
ctWanMMuxChannelEntry = _CtWanMMuxChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1)
)
ctWanMMuxChannelEntry.setIndexNames(
    (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelMMuxId"),
    (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelGroupId"),
    (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelId"),
)
if mibBuilder.loadTexts:
    ctWanMMuxChannelEntry.setStatus("mandatory")


class _CtWanMMuxChannelMMuxId_Type(Integer32):
    """Custom type ctWanMMuxChannelMMuxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxChannelMMuxId_Type.__name__ = "Integer32"
_CtWanMMuxChannelMMuxId_Object = MibTableColumn
ctWanMMuxChannelMMuxId = _CtWanMMuxChannelMMuxId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 1),
    _CtWanMMuxChannelMMuxId_Type()
)
ctWanMMuxChannelMMuxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelMMuxId.setStatus("mandatory")


class _CtWanMMuxChannelGroupId_Type(Integer32):
    """Custom type ctWanMMuxChannelGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxChannelGroupId_Type.__name__ = "Integer32"
_CtWanMMuxChannelGroupId_Object = MibTableColumn
ctWanMMuxChannelGroupId = _CtWanMMuxChannelGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 2),
    _CtWanMMuxChannelGroupId_Type()
)
ctWanMMuxChannelGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelGroupId.setStatus("mandatory")


class _CtWanMMuxChannelId_Type(Integer32):
    """Custom type ctWanMMuxChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtWanMMuxChannelId_Type.__name__ = "Integer32"
_CtWanMMuxChannelId_Object = MibTableColumn
ctWanMMuxChannelId = _CtWanMMuxChannelId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 3),
    _CtWanMMuxChannelId_Type()
)
ctWanMMuxChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelId.setStatus("mandatory")
_CtWanMMuxChannelIfIndex_Type = Integer32
_CtWanMMuxChannelIfIndex_Object = MibTableColumn
ctWanMMuxChannelIfIndex = _CtWanMMuxChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 4),
    _CtWanMMuxChannelIfIndex_Type()
)
ctWanMMuxChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelIfIndex.setStatus("mandatory")
_CtWanMMuxChannelPhysNum_Type = Integer32
_CtWanMMuxChannelPhysNum_Object = MibTableColumn
ctWanMMuxChannelPhysNum = _CtWanMMuxChannelPhysNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 5),
    _CtWanMMuxChannelPhysNum_Type()
)
ctWanMMuxChannelPhysNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelPhysNum.setStatus("mandatory")
_CtWanMMuxChannelBwAvail_Type = Integer32
_CtWanMMuxChannelBwAvail_Object = MibTableColumn
ctWanMMuxChannelBwAvail = _CtWanMMuxChannelBwAvail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 6),
    _CtWanMMuxChannelBwAvail_Type()
)
ctWanMMuxChannelBwAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelBwAvail.setStatus("mandatory")
_CtWanMMuxChannelByteCount_Type = Integer32
_CtWanMMuxChannelByteCount_Object = MibTableColumn
ctWanMMuxChannelByteCount = _CtWanMMuxChannelByteCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 7),
    _CtWanMMuxChannelByteCount_Type()
)
ctWanMMuxChannelByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelByteCount.setStatus("mandatory")


class _CtWanMMuxChannelStatus_Type(Integer32):
    """Custom type ctWanMMuxChannelStatus based on Integer32"""
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


_CtWanMMuxChannelStatus_Type.__name__ = "Integer32"
_CtWanMMuxChannelStatus_Object = MibTableColumn
ctWanMMuxChannelStatus = _CtWanMMuxChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 8),
    _CtWanMMuxChannelStatus_Type()
)
ctWanMMuxChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanMMuxChannelStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-WAN-MULTI-IMUX-MIB",
    **{"ctWanMultiMux": ctWanMultiMux,
       "ctWANMMuxGeneralGroup": ctWANMMuxGeneralGroup,
       "ctWANMMuxMaxNum": ctWANMMuxMaxNum,
       "ctWanMMuxTable": ctWanMMuxTable,
       "ctWanMMuxEntry": ctWanMMuxEntry,
       "ctWanMMuxId": ctWanMMuxId,
       "ctWanMMuxIfIndex": ctWanMMuxIfIndex,
       "ctWanMMuxMaxNumGroups": ctWanMMuxMaxNumGroups,
       "ctWanMMuxAdmin": ctWanMMuxAdmin,
       "ctWanMMuxGroupTable": ctWanMMuxGroupTable,
       "ctWanMMuxGroupEntry": ctWanMMuxGroupEntry,
       "ctWanMMuxGroupMMuxId": ctWanMMuxGroupMMuxId,
       "ctWanMMuxGroupId": ctWanMMuxGroupId,
       "ctWanMMuxGroupAdmin": ctWanMMuxGroupAdmin,
       "ctWanMMuxGroupNumChannels": ctWanMMuxGroupNumChannels,
       "ctWanMMuxGroupAddChannel": ctWanMMuxGroupAddChannel,
       "ctWanMMuxGroupDelChannel": ctWanMMuxGroupDelChannel,
       "ctWanMMuxChannelTable": ctWanMMuxChannelTable,
       "ctWanMMuxChannelEntry": ctWanMMuxChannelEntry,
       "ctWanMMuxChannelMMuxId": ctWanMMuxChannelMMuxId,
       "ctWanMMuxChannelGroupId": ctWanMMuxChannelGroupId,
       "ctWanMMuxChannelId": ctWanMMuxChannelId,
       "ctWanMMuxChannelIfIndex": ctWanMMuxChannelIfIndex,
       "ctWanMMuxChannelPhysNum": ctWanMMuxChannelPhysNum,
       "ctWanMMuxChannelBwAvail": ctWanMMuxChannelBwAvail,
       "ctWanMMuxChannelByteCount": ctWanMMuxChannelByteCount,
       "ctWanMMuxChannelStatus": ctWanMMuxChannelStatus}
)
