# SNMP MIB module (MARVELL-FIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-FIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:09 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlFip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 205)
)
rlFip.setRevisions(
        ("2007-11-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlFipIfType(Integer32, TextualConvention):
    status = "current"
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
        *(("enode", 4),
          ("fcoe", 3),
          ("non-fcoe", 2),
          ("non-snooping", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlFipIfTable_Object = MibTable
rlFipIfTable = _RlFipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 1)
)
if mibBuilder.loadTexts:
    rlFipIfTable.setStatus("current")
_RlFipIfEntry_Object = MibTableRow
rlFipIfEntry = _RlFipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 1, 1)
)
rlFipIfEntry.setIndexNames(
    (0, "MARVELL-FIP-MIB", "rlFipIfIndex"),
)
if mibBuilder.loadTexts:
    rlFipIfEntry.setStatus("current")
_RlFipIfIndex_Type = Integer32
_RlFipIfIndex_Object = MibTableColumn
rlFipIfIndex = _RlFipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 1, 1, 1),
    _RlFipIfIndex_Type()
)
rlFipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipIfIndex.setStatus("current")


class _RlFipIfType_Type(RlFipIfType):
    """Custom type rlFipIfType based on RlFipIfType"""


_RlFipIfType_Object = MibTableColumn
rlFipIfType = _RlFipIfType_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 1, 1, 2),
    _RlFipIfType_Type()
)
rlFipIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFipIfType.setStatus("current")
_RlFipIfRowStatus_Type = RowStatus
_RlFipIfRowStatus_Object = MibTableColumn
rlFipIfRowStatus = _RlFipIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 1, 1, 3),
    _RlFipIfRowStatus_Type()
)
rlFipIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFipIfRowStatus.setStatus("current")
_RlFipGlobalFcfListTable_Object = MibTable
rlFipGlobalFcfListTable = _RlFipGlobalFcfListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 2)
)
if mibBuilder.loadTexts:
    rlFipGlobalFcfListTable.setStatus("current")
_RlFipGlobalFcfListEntry_Object = MibTableRow
rlFipGlobalFcfListEntry = _RlFipGlobalFcfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 2, 1)
)
rlFipGlobalFcfListEntry.setIndexNames(
    (0, "MARVELL-FIP-MIB", "rlFipGlobalFcfListMac"),
)
if mibBuilder.loadTexts:
    rlFipGlobalFcfListEntry.setStatus("current")
_RlFipGlobalFcfListMac_Type = MacAddress
_RlFipGlobalFcfListMac_Object = MibTableColumn
rlFipGlobalFcfListMac = _RlFipGlobalFcfListMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 2, 1, 1),
    _RlFipGlobalFcfListMac_Type()
)
rlFipGlobalFcfListMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipGlobalFcfListMac.setStatus("current")
_RlFipGlobalFcfListStatus_Type = RowStatus
_RlFipGlobalFcfListStatus_Object = MibTableColumn
rlFipGlobalFcfListStatus = _RlFipGlobalFcfListStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 2, 1, 2),
    _RlFipGlobalFcfListStatus_Type()
)
rlFipGlobalFcfListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFipGlobalFcfListStatus.setStatus("current")
_RlFipStaticFcoeTunnelTable_Object = MibTable
rlFipStaticFcoeTunnelTable = _RlFipStaticFcoeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 3)
)
if mibBuilder.loadTexts:
    rlFipStaticFcoeTunnelTable.setStatus("current")
_RlFipStaticFcoeTunnelEntry_Object = MibTableRow
rlFipStaticFcoeTunnelEntry = _RlFipStaticFcoeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 3, 1)
)
rlFipStaticFcoeTunnelEntry.setIndexNames(
    (0, "MARVELL-FIP-MIB", "rlFipStaticFcoeTunnelPort"),
    (0, "MARVELL-FIP-MIB", "rlFipStaticFcoeTunnelSrcMac"),
    (0, "MARVELL-FIP-MIB", "rlFipStaticFcoeTunnelDstMac"),
)
if mibBuilder.loadTexts:
    rlFipStaticFcoeTunnelEntry.setStatus("current")
_RlFipStaticFcoeTunnelPort_Type = Integer32
_RlFipStaticFcoeTunnelPort_Object = MibTableColumn
rlFipStaticFcoeTunnelPort = _RlFipStaticFcoeTunnelPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 3, 1, 1),
    _RlFipStaticFcoeTunnelPort_Type()
)
rlFipStaticFcoeTunnelPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipStaticFcoeTunnelPort.setStatus("current")
_RlFipStaticFcoeTunnelSrcMac_Type = MacAddress
_RlFipStaticFcoeTunnelSrcMac_Object = MibTableColumn
rlFipStaticFcoeTunnelSrcMac = _RlFipStaticFcoeTunnelSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 3, 1, 2),
    _RlFipStaticFcoeTunnelSrcMac_Type()
)
rlFipStaticFcoeTunnelSrcMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipStaticFcoeTunnelSrcMac.setStatus("current")
_RlFipStaticFcoeTunnelDstMac_Type = MacAddress
_RlFipStaticFcoeTunnelDstMac_Object = MibTableColumn
rlFipStaticFcoeTunnelDstMac = _RlFipStaticFcoeTunnelDstMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 3, 1, 3),
    _RlFipStaticFcoeTunnelDstMac_Type()
)
rlFipStaticFcoeTunnelDstMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipStaticFcoeTunnelDstMac.setStatus("current")
_RlFipStaticFcoeTunnelStatus_Type = RowStatus
_RlFipStaticFcoeTunnelStatus_Object = MibTableColumn
rlFipStaticFcoeTunnelStatus = _RlFipStaticFcoeTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 3, 1, 4),
    _RlFipStaticFcoeTunnelStatus_Type()
)
rlFipStaticFcoeTunnelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFipStaticFcoeTunnelStatus.setStatus("current")
_RlFipActiveFcoeTunnelTable_Object = MibTable
rlFipActiveFcoeTunnelTable = _RlFipActiveFcoeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4)
)
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelTable.setStatus("current")
_RlFipActiveFcoeTunnelEntry_Object = MibTableRow
rlFipActiveFcoeTunnelEntry = _RlFipActiveFcoeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4, 1)
)
rlFipActiveFcoeTunnelEntry.setIndexNames(
    (0, "MARVELL-FIP-MIB", "rlFipActiveFcoeTunnelPort"),
    (0, "MARVELL-FIP-MIB", "rlFipActiveFcoeTunnelSrcMac"),
    (0, "MARVELL-FIP-MIB", "rlFipActiveFcoeTunnelDstMac"),
    (0, "MARVELL-FIP-MIB", "rlFipActiveFcoeTunnelSid"),
)
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelEntry.setStatus("current")
_RlFipActiveFcoeTunnelPort_Type = Integer32
_RlFipActiveFcoeTunnelPort_Object = MibTableColumn
rlFipActiveFcoeTunnelPort = _RlFipActiveFcoeTunnelPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4, 1, 1),
    _RlFipActiveFcoeTunnelPort_Type()
)
rlFipActiveFcoeTunnelPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelPort.setStatus("current")
_RlFipActiveFcoeTunnelSrcMac_Type = MacAddress
_RlFipActiveFcoeTunnelSrcMac_Object = MibTableColumn
rlFipActiveFcoeTunnelSrcMac = _RlFipActiveFcoeTunnelSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4, 1, 2),
    _RlFipActiveFcoeTunnelSrcMac_Type()
)
rlFipActiveFcoeTunnelSrcMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelSrcMac.setStatus("current")
_RlFipActiveFcoeTunnelDstMac_Type = MacAddress
_RlFipActiveFcoeTunnelDstMac_Object = MibTableColumn
rlFipActiveFcoeTunnelDstMac = _RlFipActiveFcoeTunnelDstMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4, 1, 3),
    _RlFipActiveFcoeTunnelDstMac_Type()
)
rlFipActiveFcoeTunnelDstMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelDstMac.setStatus("current")


class _RlFipActiveFcoeTunnelSid_Type(OctetString):
    """Custom type rlFipActiveFcoeTunnelSid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_RlFipActiveFcoeTunnelSid_Type.__name__ = "OctetString"
_RlFipActiveFcoeTunnelSid_Object = MibTableColumn
rlFipActiveFcoeTunnelSid = _RlFipActiveFcoeTunnelSid_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4, 1, 4),
    _RlFipActiveFcoeTunnelSid_Type()
)
rlFipActiveFcoeTunnelSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelSid.setStatus("current")
_RlFipActiveFcoeTunnelStatus_Type = RowStatus
_RlFipActiveFcoeTunnelStatus_Object = MibTableColumn
rlFipActiveFcoeTunnelStatus = _RlFipActiveFcoeTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 4, 1, 5),
    _RlFipActiveFcoeTunnelStatus_Type()
)
rlFipActiveFcoeTunnelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFipActiveFcoeTunnelStatus.setStatus("current")
_RlFipEnableScalar_Type = TruthValue
_RlFipEnableScalar_Object = MibScalar
rlFipEnableScalar = _RlFipEnableScalar_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 5),
    _RlFipEnableScalar_Type()
)
rlFipEnableScalar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFipEnableScalar.setStatus("current")
_RlFipClearDynamicEntiesScalar_Type = Integer32
_RlFipClearDynamicEntiesScalar_Object = MibScalar
rlFipClearDynamicEntiesScalar = _RlFipClearDynamicEntiesScalar_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 6),
    _RlFipClearDynamicEntiesScalar_Type()
)
rlFipClearDynamicEntiesScalar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFipClearDynamicEntiesScalar.setStatus("current")
_RlFipGlobalFcfFilteringEnableScalar_Type = TruthValue
_RlFipGlobalFcfFilteringEnableScalar_Object = MibScalar
rlFipGlobalFcfFilteringEnableScalar = _RlFipGlobalFcfFilteringEnableScalar_Object(
    (1, 3, 6, 1, 4, 1, 89, 205, 7),
    _RlFipGlobalFcfFilteringEnableScalar_Type()
)
rlFipGlobalFcfFilteringEnableScalar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFipGlobalFcfFilteringEnableScalar.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-FIP-MIB",
    **{"RlFipIfType": RlFipIfType,
       "rlFip": rlFip,
       "rlFipIfTable": rlFipIfTable,
       "rlFipIfEntry": rlFipIfEntry,
       "rlFipIfIndex": rlFipIfIndex,
       "rlFipIfType": rlFipIfType,
       "rlFipIfRowStatus": rlFipIfRowStatus,
       "rlFipGlobalFcfListTable": rlFipGlobalFcfListTable,
       "rlFipGlobalFcfListEntry": rlFipGlobalFcfListEntry,
       "rlFipGlobalFcfListMac": rlFipGlobalFcfListMac,
       "rlFipGlobalFcfListStatus": rlFipGlobalFcfListStatus,
       "rlFipStaticFcoeTunnelTable": rlFipStaticFcoeTunnelTable,
       "rlFipStaticFcoeTunnelEntry": rlFipStaticFcoeTunnelEntry,
       "rlFipStaticFcoeTunnelPort": rlFipStaticFcoeTunnelPort,
       "rlFipStaticFcoeTunnelSrcMac": rlFipStaticFcoeTunnelSrcMac,
       "rlFipStaticFcoeTunnelDstMac": rlFipStaticFcoeTunnelDstMac,
       "rlFipStaticFcoeTunnelStatus": rlFipStaticFcoeTunnelStatus,
       "rlFipActiveFcoeTunnelTable": rlFipActiveFcoeTunnelTable,
       "rlFipActiveFcoeTunnelEntry": rlFipActiveFcoeTunnelEntry,
       "rlFipActiveFcoeTunnelPort": rlFipActiveFcoeTunnelPort,
       "rlFipActiveFcoeTunnelSrcMac": rlFipActiveFcoeTunnelSrcMac,
       "rlFipActiveFcoeTunnelDstMac": rlFipActiveFcoeTunnelDstMac,
       "rlFipActiveFcoeTunnelSid": rlFipActiveFcoeTunnelSid,
       "rlFipActiveFcoeTunnelStatus": rlFipActiveFcoeTunnelStatus,
       "rlFipEnableScalar": rlFipEnableScalar,
       "rlFipClearDynamicEntiesScalar": rlFipClearDynamicEntiesScalar,
       "rlFipGlobalFcfFilteringEnableScalar": rlFipGlobalFcfFilteringEnableScalar}
)
