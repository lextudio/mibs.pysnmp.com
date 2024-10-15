# SNMP MIB module (ACC-ACCESSPARTITION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ACCESSPARTITION
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
 NotificationType,
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
    "NotificationType",
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

_AccAccessPartition_ObjectIdentity = ObjectIdentity
accAccessPartition = _AccAccessPartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63)
)
_AccAccessPartitionTable_Object = MibTable
accAccessPartitionTable = _AccAccessPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1)
)
if mibBuilder.loadTexts:
    accAccessPartitionTable.setStatus("mandatory")
_AccAccessPartitionEntry_Object = MibTableRow
accAccessPartitionEntry = _AccAccessPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1)
)
accAccessPartitionEntry.setIndexNames(
    (0, "ACC-ACCESSPARTITION", "accAccessPartitionName"),
)
if mibBuilder.loadTexts:
    accAccessPartitionEntry.setStatus("mandatory")
_AccAccessPartitionName_Type = DisplayString
_AccAccessPartitionName_Object = MibTableColumn
accAccessPartitionName = _AccAccessPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 1),
    _AccAccessPartitionName_Type()
)
accAccessPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionName.setStatus("mandatory")
_AccAccessPartitionCustomerId_Type = DisplayString
_AccAccessPartitionCustomerId_Object = MibTableColumn
accAccessPartitionCustomerId = _AccAccessPartitionCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 2),
    _AccAccessPartitionCustomerId_Type()
)
accAccessPartitionCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionCustomerId.setStatus("mandatory")


class _AccAccessPartitionAdminState_Type(Integer32):
    """Custom type accAccessPartitionAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("drained", 3),
          ("enabled", 1))
    )


_AccAccessPartitionAdminState_Type.__name__ = "Integer32"
_AccAccessPartitionAdminState_Object = MibTableColumn
accAccessPartitionAdminState = _AccAccessPartitionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 3),
    _AccAccessPartitionAdminState_Type()
)
accAccessPartitionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionAdminState.setStatus("mandatory")


class _AccAccessPartitionMsgLevel_Type(Integer32):
    """Custom type accAccessPartitionMsgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccAccessPartitionMsgLevel_Type.__name__ = "Integer32"
_AccAccessPartitionMsgLevel_Object = MibTableColumn
accAccessPartitionMsgLevel = _AccAccessPartitionMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 4),
    _AccAccessPartitionMsgLevel_Type()
)
accAccessPartitionMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionMsgLevel.setStatus("mandatory")


class _AccAccessPartitionPortLimit_Type(Integer32):
    """Custom type accAccessPartitionPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccAccessPartitionPortLimit_Type.__name__ = "Integer32"
_AccAccessPartitionPortLimit_Object = MibTableColumn
accAccessPartitionPortLimit = _AccAccessPartitionPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 5),
    _AccAccessPartitionPortLimit_Type()
)
accAccessPartitionPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionPortLimit.setStatus("mandatory")
_AccAccessPartitionIpAddrPri_Type = IpAddress
_AccAccessPartitionIpAddrPri_Object = MibTableColumn
accAccessPartitionIpAddrPri = _AccAccessPartitionIpAddrPri_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 6),
    _AccAccessPartitionIpAddrPri_Type()
)
accAccessPartitionIpAddrPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionIpAddrPri.setStatus("mandatory")
_AccAccessPartitionIpAddrSec_Type = IpAddress
_AccAccessPartitionIpAddrSec_Object = MibTableColumn
accAccessPartitionIpAddrSec = _AccAccessPartitionIpAddrSec_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 7),
    _AccAccessPartitionIpAddrSec_Type()
)
accAccessPartitionIpAddrSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionIpAddrSec.setStatus("mandatory")


class _AccAccessPartitionRoutePolicy_Type(Integer32):
    """Custom type accAccessPartitionRoutePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("funnel", 1))
    )


_AccAccessPartitionRoutePolicy_Type.__name__ = "Integer32"
_AccAccessPartitionRoutePolicy_Object = MibTableColumn
accAccessPartitionRoutePolicy = _AccAccessPartitionRoutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 8),
    _AccAccessPartitionRoutePolicy_Type()
)
accAccessPartitionRoutePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionRoutePolicy.setStatus("mandatory")
_AccAccessPartitionBusyCount_Type = Gauge32
_AccAccessPartitionBusyCount_Object = MibTableColumn
accAccessPartitionBusyCount = _AccAccessPartitionBusyCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 9),
    _AccAccessPartitionBusyCount_Type()
)
accAccessPartitionBusyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionBusyCount.setStatus("mandatory")
_AccAccessPartitionNumAccepts_Type = Counter32
_AccAccessPartitionNumAccepts_Object = MibTableColumn
accAccessPartitionNumAccepts = _AccAccessPartitionNumAccepts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 10),
    _AccAccessPartitionNumAccepts_Type()
)
accAccessPartitionNumAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionNumAccepts.setStatus("mandatory")
_AccAccessPartitionNumRejects_Type = Counter32
_AccAccessPartitionNumRejects_Object = MibTableColumn
accAccessPartitionNumRejects = _AccAccessPartitionNumRejects_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 11),
    _AccAccessPartitionNumRejects_Type()
)
accAccessPartitionNumRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionNumRejects.setStatus("mandatory")
_AccAccessPartitionNumActive_Type = Gauge32
_AccAccessPartitionNumActive_Object = MibTableColumn
accAccessPartitionNumActive = _AccAccessPartitionNumActive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 12),
    _AccAccessPartitionNumActive_Type()
)
accAccessPartitionNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionNumActive.setStatus("mandatory")
_AccAccessPartitionAuthFails_Type = Counter32
_AccAccessPartitionAuthFails_Object = MibTableColumn
accAccessPartitionAuthFails = _AccAccessPartitionAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 13),
    _AccAccessPartitionAuthFails_Type()
)
accAccessPartitionAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionAuthFails.setStatus("mandatory")
_AccAccessPartitionConnectTime_Type = TimeTicks
_AccAccessPartitionConnectTime_Object = MibTableColumn
accAccessPartitionConnectTime = _AccAccessPartitionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 14),
    _AccAccessPartitionConnectTime_Type()
)
accAccessPartitionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionConnectTime.setStatus("mandatory")
_AccAccessPartitionInOctets_Type = Counter32
_AccAccessPartitionInOctets_Object = MibTableColumn
accAccessPartitionInOctets = _AccAccessPartitionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 15),
    _AccAccessPartitionInOctets_Type()
)
accAccessPartitionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionInOctets.setStatus("mandatory")
_AccAccessPartitionOutOctets_Type = Counter32
_AccAccessPartitionOutOctets_Object = MibTableColumn
accAccessPartitionOutOctets = _AccAccessPartitionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 16),
    _AccAccessPartitionOutOctets_Type()
)
accAccessPartitionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionOutOctets.setStatus("mandatory")
_AccAccessPartitionInPackets_Type = Counter32
_AccAccessPartitionInPackets_Object = MibTableColumn
accAccessPartitionInPackets = _AccAccessPartitionInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 17),
    _AccAccessPartitionInPackets_Type()
)
accAccessPartitionInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionInPackets.setStatus("mandatory")
_AccAccessPartitionOutPackets_Type = Counter32
_AccAccessPartitionOutPackets_Object = MibTableColumn
accAccessPartitionOutPackets = _AccAccessPartitionOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 18),
    _AccAccessPartitionOutPackets_Type()
)
accAccessPartitionOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionOutPackets.setStatus("mandatory")


class _AccAccessPartitionEntryStatus_Type(Integer32):
    """Custom type accAccessPartitionEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccAccessPartitionEntryStatus_Type.__name__ = "Integer32"
_AccAccessPartitionEntryStatus_Object = MibTableColumn
accAccessPartitionEntryStatus = _AccAccessPartitionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 19),
    _AccAccessPartitionEntryStatus_Type()
)
accAccessPartitionEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionEntryStatus.setStatus("mandatory")
_AccAccessPartitionNumDiscards_Type = Counter32
_AccAccessPartitionNumDiscards_Object = MibTableColumn
accAccessPartitionNumDiscards = _AccAccessPartitionNumDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 20),
    _AccAccessPartitionNumDiscards_Type()
)
accAccessPartitionNumDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionNumDiscards.setStatus("mandatory")
_AccAccessPartitionNumDirects_Type = Counter32
_AccAccessPartitionNumDirects_Object = MibTableColumn
accAccessPartitionNumDirects = _AccAccessPartitionNumDirects_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 21),
    _AccAccessPartitionNumDirects_Type()
)
accAccessPartitionNumDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionNumDirects.setStatus("mandatory")
_AccAccessPartitionNumFunnels_Type = Counter32
_AccAccessPartitionNumFunnels_Object = MibTableColumn
accAccessPartitionNumFunnels = _AccAccessPartitionNumFunnels_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 22),
    _AccAccessPartitionNumFunnels_Type()
)
accAccessPartitionNumFunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionNumFunnels.setStatus("mandatory")
_AccAccessPartitionProxyServer_Type = DisplayString
_AccAccessPartitionProxyServer_Object = MibTableColumn
accAccessPartitionProxyServer = _AccAccessPartitionProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 23),
    _AccAccessPartitionProxyServer_Type()
)
accAccessPartitionProxyServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionProxyServer.setStatus("mandatory")


class _AccAccessPartitionIngrFiltState_Type(Integer32):
    """Custom type accAccessPartitionIngrFiltState based on Integer32"""
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


_AccAccessPartitionIngrFiltState_Type.__name__ = "Integer32"
_AccAccessPartitionIngrFiltState_Object = MibTableColumn
accAccessPartitionIngrFiltState = _AccAccessPartitionIngrFiltState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 24),
    _AccAccessPartitionIngrFiltState_Type()
)
accAccessPartitionIngrFiltState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionIngrFiltState.setStatus("obsolete")
_AccAccessPartitionDnsServPri_Type = IpAddress
_AccAccessPartitionDnsServPri_Object = MibTableColumn
accAccessPartitionDnsServPri = _AccAccessPartitionDnsServPri_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 25),
    _AccAccessPartitionDnsServPri_Type()
)
accAccessPartitionDnsServPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionDnsServPri.setStatus("obsolete")
_AccAccessPartitionDnsServSec_Type = IpAddress
_AccAccessPartitionDnsServSec_Object = MibTableColumn
accAccessPartitionDnsServSec = _AccAccessPartitionDnsServSec_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 26),
    _AccAccessPartitionDnsServSec_Type()
)
accAccessPartitionDnsServSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionDnsServSec.setStatus("obsolete")
_AccAccessPartitionNbnsServPri_Type = IpAddress
_AccAccessPartitionNbnsServPri_Object = MibTableColumn
accAccessPartitionNbnsServPri = _AccAccessPartitionNbnsServPri_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 27),
    _AccAccessPartitionNbnsServPri_Type()
)
accAccessPartitionNbnsServPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionNbnsServPri.setStatus("obsolete")
_AccAccessPartitionNbnsServSec_Type = IpAddress
_AccAccessPartitionNbnsServSec_Object = MibTableColumn
accAccessPartitionNbnsServSec = _AccAccessPartitionNbnsServSec_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 28),
    _AccAccessPartitionNbnsServSec_Type()
)
accAccessPartitionNbnsServSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionNbnsServSec.setStatus("obsolete")
_AccAccessPartitionIpPool_Type = DisplayString
_AccAccessPartitionIpPool_Object = MibTableColumn
accAccessPartitionIpPool = _AccAccessPartitionIpPool_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 29),
    _AccAccessPartitionIpPool_Type()
)
accAccessPartitionIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionIpPool.setStatus("obsolete")
_AccAccessPartitionProxyIpPool_Type = DisplayString
_AccAccessPartitionProxyIpPool_Object = MibTableColumn
accAccessPartitionProxyIpPool = _AccAccessPartitionProxyIpPool_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 30),
    _AccAccessPartitionProxyIpPool_Type()
)
accAccessPartitionProxyIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionProxyIpPool.setStatus("mandatory")
_AccAccessPartitionProxyIpRouter_Type = DisplayString
_AccAccessPartitionProxyIpRouter_Object = MibTableColumn
accAccessPartitionProxyIpRouter = _AccAccessPartitionProxyIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 1, 1, 31),
    _AccAccessPartitionProxyIpRouter_Type()
)
accAccessPartitionProxyIpRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessPartitionProxyIpRouter.setStatus("mandatory")
_AccAccessPartitionPortTable_Object = MibTable
accAccessPartitionPortTable = _AccAccessPartitionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 2)
)
if mibBuilder.loadTexts:
    accAccessPartitionPortTable.setStatus("mandatory")
_AccAccessPartitionPortEntry_Object = MibTableRow
accAccessPartitionPortEntry = _AccAccessPartitionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 2, 1)
)
accAccessPartitionPortEntry.setIndexNames(
    (0, "ACC-ACCESSPARTITION", "accAccessPartitionIfIndex"),
)
if mibBuilder.loadTexts:
    accAccessPartitionPortEntry.setStatus("mandatory")


class _AccAccessPartitionIfIndex_Type(Integer32):
    """Custom type accAccessPartitionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccAccessPartitionIfIndex_Type.__name__ = "Integer32"
_AccAccessPartitionIfIndex_Object = MibTableColumn
accAccessPartitionIfIndex = _AccAccessPartitionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 2, 1, 1),
    _AccAccessPartitionIfIndex_Type()
)
accAccessPartitionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionIfIndex.setStatus("mandatory")
_AccAccessPartitionConfiguredName_Type = DisplayString
_AccAccessPartitionConfiguredName_Object = MibTableColumn
accAccessPartitionConfiguredName = _AccAccessPartitionConfiguredName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 2, 1, 2),
    _AccAccessPartitionConfiguredName_Type()
)
accAccessPartitionConfiguredName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionConfiguredName.setStatus("mandatory")
_AccAccessPartitionActiveName_Type = DisplayString
_AccAccessPartitionActiveName_Object = MibTableColumn
accAccessPartitionActiveName = _AccAccessPartitionActiveName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 2, 1, 3),
    _AccAccessPartitionActiveName_Type()
)
accAccessPartitionActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionActiveName.setStatus("mandatory")
_AccAccessPartitionActiveCustomer_Type = DisplayString
_AccAccessPartitionActiveCustomer_Object = MibTableColumn
accAccessPartitionActiveCustomer = _AccAccessPartitionActiveCustomer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 2, 1, 4),
    _AccAccessPartitionActiveCustomer_Type()
)
accAccessPartitionActiveCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionActiveCustomer.setStatus("mandatory")
_AccAccessPartitionTraps_ObjectIdentity = ObjectIdentity
accAccessPartitionTraps = _AccAccessPartitionTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 3)
)
_AccAccessPartitionTrapMsg_Type = DisplayString
_AccAccessPartitionTrapMsg_Object = MibScalar
accAccessPartitionTrapMsg = _AccAccessPartitionTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 3, 1),
    _AccAccessPartitionTrapMsg_Type()
)
accAccessPartitionTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessPartitionTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accAPDelApTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 63, 3, 0, 1)
)
accAPDelApTrap.setObjects(
      *(("ACC-ACCESSPARTITION", "accAccessPartitionTrapMsg"),
        ("ACC-ACCESSPARTITION", "accAccessPartitionName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accAPDelApTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ACCESSPARTITION",
    **{"accAccessPartition": accAccessPartition,
       "accAccessPartitionTable": accAccessPartitionTable,
       "accAccessPartitionEntry": accAccessPartitionEntry,
       "accAccessPartitionName": accAccessPartitionName,
       "accAccessPartitionCustomerId": accAccessPartitionCustomerId,
       "accAccessPartitionAdminState": accAccessPartitionAdminState,
       "accAccessPartitionMsgLevel": accAccessPartitionMsgLevel,
       "accAccessPartitionPortLimit": accAccessPartitionPortLimit,
       "accAccessPartitionIpAddrPri": accAccessPartitionIpAddrPri,
       "accAccessPartitionIpAddrSec": accAccessPartitionIpAddrSec,
       "accAccessPartitionRoutePolicy": accAccessPartitionRoutePolicy,
       "accAccessPartitionBusyCount": accAccessPartitionBusyCount,
       "accAccessPartitionNumAccepts": accAccessPartitionNumAccepts,
       "accAccessPartitionNumRejects": accAccessPartitionNumRejects,
       "accAccessPartitionNumActive": accAccessPartitionNumActive,
       "accAccessPartitionAuthFails": accAccessPartitionAuthFails,
       "accAccessPartitionConnectTime": accAccessPartitionConnectTime,
       "accAccessPartitionInOctets": accAccessPartitionInOctets,
       "accAccessPartitionOutOctets": accAccessPartitionOutOctets,
       "accAccessPartitionInPackets": accAccessPartitionInPackets,
       "accAccessPartitionOutPackets": accAccessPartitionOutPackets,
       "accAccessPartitionEntryStatus": accAccessPartitionEntryStatus,
       "accAccessPartitionNumDiscards": accAccessPartitionNumDiscards,
       "accAccessPartitionNumDirects": accAccessPartitionNumDirects,
       "accAccessPartitionNumFunnels": accAccessPartitionNumFunnels,
       "accAccessPartitionProxyServer": accAccessPartitionProxyServer,
       "accAccessPartitionIngrFiltState": accAccessPartitionIngrFiltState,
       "accAccessPartitionDnsServPri": accAccessPartitionDnsServPri,
       "accAccessPartitionDnsServSec": accAccessPartitionDnsServSec,
       "accAccessPartitionNbnsServPri": accAccessPartitionNbnsServPri,
       "accAccessPartitionNbnsServSec": accAccessPartitionNbnsServSec,
       "accAccessPartitionIpPool": accAccessPartitionIpPool,
       "accAccessPartitionProxyIpPool": accAccessPartitionProxyIpPool,
       "accAccessPartitionProxyIpRouter": accAccessPartitionProxyIpRouter,
       "accAccessPartitionPortTable": accAccessPartitionPortTable,
       "accAccessPartitionPortEntry": accAccessPartitionPortEntry,
       "accAccessPartitionIfIndex": accAccessPartitionIfIndex,
       "accAccessPartitionConfiguredName": accAccessPartitionConfiguredName,
       "accAccessPartitionActiveName": accAccessPartitionActiveName,
       "accAccessPartitionActiveCustomer": accAccessPartitionActiveCustomer,
       "accAccessPartitionTraps": accAccessPartitionTraps,
       "accAPDelApTrap": accAPDelApTrap,
       "accAccessPartitionTrapMsg": accAccessPartitionTrapMsg}
)
