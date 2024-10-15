# SNMP MIB module (BASP-Statistics-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BASP-Statistics-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:46 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadcom_ObjectIdentity = ObjectIdentity
broadcom = _Broadcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413)
)
_Enet_ObjectIdentity = ObjectIdentity
enet = _Enet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1)
)
_Basp_ObjectIdentity = ObjectIdentity
basp = _Basp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2)
)
_BaspStat_ObjectIdentity = ObjectIdentity
baspStat = _BaspStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2)
)
_BaspTeamStat_ObjectIdentity = ObjectIdentity
baspTeamStat = _BaspTeamStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1)
)
_BtsTeamNumber_Type = Integer32
_BtsTeamNumber_Object = MibScalar
btsTeamNumber = _BtsTeamNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 1),
    _BtsTeamNumber_Type()
)
btsTeamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsTeamNumber.setStatus("mandatory")
_BtsTeamTable_Object = MibTable
btsTeamTable = _BtsTeamTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    btsTeamTable.setStatus("mandatory")
_BtsTeamEntry_Object = MibTableRow
btsTeamEntry = _BtsTeamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1)
)
btsTeamEntry.setIndexNames(
    (0, "BASP-Statistics-MIB", "btsTeamIndex"),
)
if mibBuilder.loadTexts:
    btsTeamEntry.setStatus("mandatory")


class _BtsTeamIndex_Type(Integer32):
    """Custom type btsTeamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtsTeamIndex_Type.__name__ = "Integer32"
_BtsTeamIndex_Object = MibTableColumn
btsTeamIndex = _BtsTeamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 1),
    _BtsTeamIndex_Type()
)
btsTeamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btsTeamIndex.setStatus("mandatory")
_BtsTeamName_Type = DisplayString
_BtsTeamName_Object = MibTableColumn
btsTeamName = _BtsTeamName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 2),
    _BtsTeamName_Type()
)
btsTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsTeamName.setStatus("mandatory")
_BtsPhyNumber_Type = Integer32
_BtsPhyNumber_Object = MibTableColumn
btsPhyNumber = _BtsPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 3),
    _BtsPhyNumber_Type()
)
btsPhyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPhyNumber.setStatus("mandatory")
_BtsVirNumber_Type = Integer32
_BtsVirNumber_Object = MibTableColumn
btsVirNumber = _BtsVirNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 4),
    _BtsVirNumber_Type()
)
btsVirNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsVirNumber.setStatus("mandatory")
_BtsPacketSends_Type = Counter32
_BtsPacketSends_Object = MibTableColumn
btsPacketSends = _BtsPacketSends_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 5),
    _BtsPacketSends_Type()
)
btsPacketSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPacketSends.setStatus("mandatory")
_BtsPacketSendDiscardeds_Type = Counter32
_BtsPacketSendDiscardeds_Object = MibTableColumn
btsPacketSendDiscardeds = _BtsPacketSendDiscardeds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 6),
    _BtsPacketSendDiscardeds_Type()
)
btsPacketSendDiscardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPacketSendDiscardeds.setStatus("mandatory")
_BtsPacketSendQueueds_Type = Counter32
_BtsPacketSendQueueds_Object = MibTableColumn
btsPacketSendQueueds = _BtsPacketSendQueueds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 7),
    _BtsPacketSendQueueds_Type()
)
btsPacketSendQueueds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPacketSendQueueds.setStatus("mandatory")
_BtsPacketRecvs_Type = Counter32
_BtsPacketRecvs_Object = MibTableColumn
btsPacketRecvs = _BtsPacketRecvs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 8),
    _BtsPacketRecvs_Type()
)
btsPacketRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPacketRecvs.setStatus("mandatory")
_BtsPacketRecvDiscardeds_Type = Counter32
_BtsPacketRecvDiscardeds_Object = MibTableColumn
btsPacketRecvDiscardeds = _BtsPacketRecvDiscardeds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 9),
    _BtsPacketRecvDiscardeds_Type()
)
btsPacketRecvDiscardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPacketRecvDiscardeds.setStatus("mandatory")
_BtsLinkPacketsSents_Type = Counter32
_BtsLinkPacketsSents_Object = MibTableColumn
btsLinkPacketsSents = _BtsLinkPacketsSents_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 10),
    _BtsLinkPacketsSents_Type()
)
btsLinkPacketsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsLinkPacketsSents.setStatus("mandatory")
_BtsLinkPacketsRetrieds_Type = Counter32
_BtsLinkPacketsRetrieds_Object = MibTableColumn
btsLinkPacketsRetrieds = _BtsLinkPacketsRetrieds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 11),
    _BtsLinkPacketsRetrieds_Type()
)
btsLinkPacketsRetrieds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsLinkPacketsRetrieds.setStatus("mandatory")
_BaspPhyAdapterStat_ObjectIdentity = ObjectIdentity
baspPhyAdapterStat = _BaspPhyAdapterStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2)
)
_BtsPhyAdapterNumber_Type = Integer32
_BtsPhyAdapterNumber_Object = MibScalar
btsPhyAdapterNumber = _BtsPhyAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 1),
    _BtsPhyAdapterNumber_Type()
)
btsPhyAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsPhyAdapterNumber.setStatus("mandatory")
_BtsPhyAdapterStatTable_Object = MibTable
btsPhyAdapterStatTable = _BtsPhyAdapterStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    btsPhyAdapterStatTable.setStatus("mandatory")
_BtsPhyAdapterStatEntry_Object = MibTableRow
btsPhyAdapterStatEntry = _BtsPhyAdapterStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1)
)
btsPhyAdapterStatEntry.setIndexNames(
    (0, "BASP-Statistics-MIB", "btspTeamIndex"),
    (0, "BASP-Statistics-MIB", "btspAdapterIndex"),
)
if mibBuilder.loadTexts:
    btsPhyAdapterStatEntry.setStatus("mandatory")


class _BtspTeamIndex_Type(Integer32):
    """Custom type btspTeamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtspTeamIndex_Type.__name__ = "Integer32"
_BtspTeamIndex_Object = MibTableColumn
btspTeamIndex = _BtspTeamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 1),
    _BtspTeamIndex_Type()
)
btspTeamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btspTeamIndex.setStatus("mandatory")


class _BtspAdapterIndex_Type(Integer32):
    """Custom type btspAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtspAdapterIndex_Type.__name__ = "Integer32"
_BtspAdapterIndex_Object = MibTableColumn
btspAdapterIndex = _BtspAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 2),
    _BtspAdapterIndex_Type()
)
btspAdapterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btspAdapterIndex.setStatus("mandatory")
_BtspAdapterDesc_Type = DisplayString
_BtspAdapterDesc_Object = MibTableColumn
btspAdapterDesc = _BtspAdapterDesc_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 3),
    _BtspAdapterDesc_Type()
)
btspAdapterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspAdapterDesc.setStatus("mandatory")
_BtspPacketSends_Type = Counter32
_BtspPacketSends_Object = MibTableColumn
btspPacketSends = _BtspPacketSends_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 4),
    _BtspPacketSends_Type()
)
btspPacketSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspPacketSends.setStatus("mandatory")
_BtspPacketSendDiscardeds_Type = Counter32
_BtspPacketSendDiscardeds_Object = MibTableColumn
btspPacketSendDiscardeds = _BtspPacketSendDiscardeds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 5),
    _BtspPacketSendDiscardeds_Type()
)
btspPacketSendDiscardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspPacketSendDiscardeds.setStatus("mandatory")
_BtspPacketRecvs_Type = Counter32
_BtspPacketRecvs_Object = MibTableColumn
btspPacketRecvs = _BtspPacketRecvs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 6),
    _BtspPacketRecvs_Type()
)
btspPacketRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspPacketRecvs.setStatus("mandatory")
_BtspPacketRecvDiscardeds_Type = Counter32
_BtspPacketRecvDiscardeds_Object = MibTableColumn
btspPacketRecvDiscardeds = _BtspPacketRecvDiscardeds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 7),
    _BtspPacketRecvDiscardeds_Type()
)
btspPacketRecvDiscardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspPacketRecvDiscardeds.setStatus("mandatory")
_BtspLinkPacketsSents_Type = Counter32
_BtspLinkPacketsSents_Object = MibTableColumn
btspLinkPacketsSents = _BtspLinkPacketsSents_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 8),
    _BtspLinkPacketsSents_Type()
)
btspLinkPacketsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspLinkPacketsSents.setStatus("mandatory")
_BtspLinkPacketsRetrieds_Type = Counter32
_BtspLinkPacketsRetrieds_Object = MibTableColumn
btspLinkPacketsRetrieds = _BtspLinkPacketsRetrieds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 9),
    _BtspLinkPacketsRetrieds_Type()
)
btspLinkPacketsRetrieds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btspLinkPacketsRetrieds.setStatus("mandatory")
_BaspVirAdapterStat_ObjectIdentity = ObjectIdentity
baspVirAdapterStat = _BaspVirAdapterStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3)
)
_BtsVirAdapterNumber_Type = Integer32
_BtsVirAdapterNumber_Object = MibScalar
btsVirAdapterNumber = _BtsVirAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 1),
    _BtsVirAdapterNumber_Type()
)
btsVirAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsVirAdapterNumber.setStatus("mandatory")
_BtsVirAdapterStatTable_Object = MibTable
btsVirAdapterStatTable = _BtsVirAdapterStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    btsVirAdapterStatTable.setStatus("mandatory")
_BtsVirAdapterStatEntry_Object = MibTableRow
btsVirAdapterStatEntry = _BtsVirAdapterStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1)
)
btsVirAdapterStatEntry.setIndexNames(
    (0, "BASP-Statistics-MIB", "btsvTeamIndex"),
    (0, "BASP-Statistics-MIB", "btsvAdapterIndex"),
)
if mibBuilder.loadTexts:
    btsVirAdapterStatEntry.setStatus("mandatory")


class _BtsvTeamIndex_Type(Integer32):
    """Custom type btsvTeamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtsvTeamIndex_Type.__name__ = "Integer32"
_BtsvTeamIndex_Object = MibTableColumn
btsvTeamIndex = _BtsvTeamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 1),
    _BtsvTeamIndex_Type()
)
btsvTeamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btsvTeamIndex.setStatus("mandatory")


class _BtsvAdapterIndex_Type(Integer32):
    """Custom type btsvAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtsvAdapterIndex_Type.__name__ = "Integer32"
_BtsvAdapterIndex_Object = MibTableColumn
btsvAdapterIndex = _BtsvAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 2),
    _BtsvAdapterIndex_Type()
)
btsvAdapterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btsvAdapterIndex.setStatus("mandatory")
_BtsvAdapterDesc_Type = DisplayString
_BtsvAdapterDesc_Object = MibTableColumn
btsvAdapterDesc = _BtsvAdapterDesc_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 3),
    _BtsvAdapterDesc_Type()
)
btsvAdapterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsvAdapterDesc.setStatus("mandatory")
_BtsvPacketSends_Type = Counter32
_BtsvPacketSends_Object = MibTableColumn
btsvPacketSends = _BtsvPacketSends_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 4),
    _BtsvPacketSends_Type()
)
btsvPacketSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsvPacketSends.setStatus("mandatory")
_BtsvPacketSendQueueds_Type = Counter32
_BtsvPacketSendQueueds_Object = MibTableColumn
btsvPacketSendQueueds = _BtsvPacketSendQueueds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 5),
    _BtsvPacketSendQueueds_Type()
)
btsvPacketSendQueueds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsvPacketSendQueueds.setStatus("mandatory")
_BtsvPacketRecvs_Type = Counter32
_BtsvPacketRecvs_Object = MibTableColumn
btsvPacketRecvs = _BtsvPacketRecvs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 6),
    _BtsvPacketRecvs_Type()
)
btsvPacketRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsvPacketRecvs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASP-Statistics-MIB",
    **{"broadcom": broadcom,
       "enet": enet,
       "basp": basp,
       "baspStat": baspStat,
       "baspTeamStat": baspTeamStat,
       "btsTeamNumber": btsTeamNumber,
       "btsTeamTable": btsTeamTable,
       "btsTeamEntry": btsTeamEntry,
       "btsTeamIndex": btsTeamIndex,
       "btsTeamName": btsTeamName,
       "btsPhyNumber": btsPhyNumber,
       "btsVirNumber": btsVirNumber,
       "btsPacketSends": btsPacketSends,
       "btsPacketSendDiscardeds": btsPacketSendDiscardeds,
       "btsPacketSendQueueds": btsPacketSendQueueds,
       "btsPacketRecvs": btsPacketRecvs,
       "btsPacketRecvDiscardeds": btsPacketRecvDiscardeds,
       "btsLinkPacketsSents": btsLinkPacketsSents,
       "btsLinkPacketsRetrieds": btsLinkPacketsRetrieds,
       "baspPhyAdapterStat": baspPhyAdapterStat,
       "btsPhyAdapterNumber": btsPhyAdapterNumber,
       "btsPhyAdapterStatTable": btsPhyAdapterStatTable,
       "btsPhyAdapterStatEntry": btsPhyAdapterStatEntry,
       "btspTeamIndex": btspTeamIndex,
       "btspAdapterIndex": btspAdapterIndex,
       "btspAdapterDesc": btspAdapterDesc,
       "btspPacketSends": btspPacketSends,
       "btspPacketSendDiscardeds": btspPacketSendDiscardeds,
       "btspPacketRecvs": btspPacketRecvs,
       "btspPacketRecvDiscardeds": btspPacketRecvDiscardeds,
       "btspLinkPacketsSents": btspLinkPacketsSents,
       "btspLinkPacketsRetrieds": btspLinkPacketsRetrieds,
       "baspVirAdapterStat": baspVirAdapterStat,
       "btsVirAdapterNumber": btsVirAdapterNumber,
       "btsVirAdapterStatTable": btsVirAdapterStatTable,
       "btsVirAdapterStatEntry": btsVirAdapterStatEntry,
       "btsvTeamIndex": btsvTeamIndex,
       "btsvAdapterIndex": btsvAdapterIndex,
       "btsvAdapterDesc": btsvAdapterDesc,
       "btsvPacketSends": btsvPacketSends,
       "btsvPacketSendQueueds": btsvPacketSendQueueds,
       "btsvPacketRecvs": btsvPacketRecvs}
)
