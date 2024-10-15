# SNMP MIB module (HPN-ICF-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:38 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfDHCPServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101)
)
hpnicfDHCPServer.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDHCPServerObjects_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerObjects = _HpnicfDHCPServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1)
)
_HpnicfDHCPServerIPPoolUsage_Type = Integer32
_HpnicfDHCPServerIPPoolUsage_Object = MibScalar
hpnicfDHCPServerIPPoolUsage = _HpnicfDHCPServerIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1, 1),
    _HpnicfDHCPServerIPPoolUsage_Type()
)
hpnicfDHCPServerIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPServerIPPoolUsage.setStatus("current")
_HpnicfDHCPServerReqTimes_Type = Counter32
_HpnicfDHCPServerReqTimes_Object = MibScalar
hpnicfDHCPServerReqTimes = _HpnicfDHCPServerReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1, 2),
    _HpnicfDHCPServerReqTimes_Type()
)
hpnicfDHCPServerReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPServerReqTimes.setStatus("current")
_HpnicfDHCPServerReqSuccessTimes_Type = Counter32
_HpnicfDHCPServerReqSuccessTimes_Object = MibScalar
hpnicfDHCPServerReqSuccessTimes = _HpnicfDHCPServerReqSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1, 3),
    _HpnicfDHCPServerReqSuccessTimes_Type()
)
hpnicfDHCPServerReqSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPServerReqSuccessTimes.setStatus("current")


class _HpnicfDHCPServerAvgIpUseThreshold_Type(Integer32):
    """Custom type hpnicfDHCPServerAvgIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDHCPServerAvgIpUseThreshold_Type.__name__ = "Integer32"
_HpnicfDHCPServerAvgIpUseThreshold_Object = MibScalar
hpnicfDHCPServerAvgIpUseThreshold = _HpnicfDHCPServerAvgIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1, 4),
    _HpnicfDHCPServerAvgIpUseThreshold_Type()
)
hpnicfDHCPServerAvgIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPServerAvgIpUseThreshold.setStatus("current")


class _HpnicfDHCPServerMaxIpUseThreshold_Type(Integer32):
    """Custom type hpnicfDHCPServerMaxIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDHCPServerMaxIpUseThreshold_Type.__name__ = "Integer32"
_HpnicfDHCPServerMaxIpUseThreshold_Object = MibScalar
hpnicfDHCPServerMaxIpUseThreshold = _HpnicfDHCPServerMaxIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1, 5),
    _HpnicfDHCPServerMaxIpUseThreshold_Type()
)
hpnicfDHCPServerMaxIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPServerMaxIpUseThreshold.setStatus("current")


class _HpnicfDHCPServerAllocateThreshold_Type(Integer32):
    """Custom type hpnicfDHCPServerAllocateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDHCPServerAllocateThreshold_Type.__name__ = "Integer32"
_HpnicfDHCPServerAllocateThreshold_Object = MibScalar
hpnicfDHCPServerAllocateThreshold = _HpnicfDHCPServerAllocateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 1, 6),
    _HpnicfDHCPServerAllocateThreshold_Type()
)
hpnicfDHCPServerAllocateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPServerAllocateThreshold.setStatus("current")
_HpnicfDHCPServerTables_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerTables = _HpnicfDHCPServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2)
)


class _HpnicfDHCPServerPoolName_Type(OctetString):
    """Custom type hpnicfDHCPServerPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPServerPoolName_Type.__name__ = "OctetString"
_HpnicfDHCPServerPoolName_Object = MibScalar
hpnicfDHCPServerPoolName = _HpnicfDHCPServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 1),
    _HpnicfDHCPServerPoolName_Type()
)
hpnicfDHCPServerPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDHCPServerPoolName.setStatus("current")
_HpnicfDHCPSrvGlobalPoolTable_Object = MibTable
hpnicfDHCPSrvGlobalPoolTable = _HpnicfDHCPSrvGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolTable.setStatus("current")
_HpnicfDHCPSrvGlobalPoolEntry_Object = MibTableRow
hpnicfDHCPSrvGlobalPoolEntry = _HpnicfDHCPSrvGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 2, 1)
)
hpnicfDHCPSrvGlobalPoolEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolEntry.setStatus("current")


class _HpnicfDHCPSrvGlobalPoolName_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSrvGlobalPoolName_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlobalPoolName_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolName = _HpnicfDHCPSrvGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 2, 1, 1),
    _HpnicfDHCPSrvGlobalPoolName_Type()
)
hpnicfDHCPSrvGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolName.setStatus("current")
_HpnicfDHCPSrvGlobalPoolRowStatus_Type = RowStatus
_HpnicfDHCPSrvGlobalPoolRowStatus_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolRowStatus = _HpnicfDHCPSrvGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 2, 1, 2),
    _HpnicfDHCPSrvGlobalPoolRowStatus_Type()
)
hpnicfDHCPSrvGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolRowStatus.setStatus("current")
_HpnicfDHCPSrvGlobalPoolConfigTable_Object = MibTable
hpnicfDHCPSrvGlobalPoolConfigTable = _HpnicfDHCPSrvGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolConfigTable.setStatus("current")
_HpnicfDHCPSrvGlobalPoolConfigEntry_Object = MibTableRow
hpnicfDHCPSrvGlobalPoolConfigEntry = _HpnicfDHCPSrvGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1)
)
hpnicfDHCPSrvGlobalPoolConfigEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolConfigEntry.setStatus("current")


class _HpnicfDHCPSrvGlobalPoolType_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlobalPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("network", 2),
          ("null", 0))
    )


_HpnicfDHCPSrvGlobalPoolType_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlobalPoolType_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolType = _HpnicfDHCPSrvGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 1),
    _HpnicfDHCPSrvGlobalPoolType_Type()
)
hpnicfDHCPSrvGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolType.setStatus("current")
_HpnicfDHCPSrvGlobalPoolNetwork_Type = IpAddress
_HpnicfDHCPSrvGlobalPoolNetwork_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolNetwork = _HpnicfDHCPSrvGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 2),
    _HpnicfDHCPSrvGlobalPoolNetwork_Type()
)
hpnicfDHCPSrvGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolNetwork.setStatus("current")
_HpnicfDHCPSrvGlobalPoolNetworkMask_Type = IpAddress
_HpnicfDHCPSrvGlobalPoolNetworkMask_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolNetworkMask = _HpnicfDHCPSrvGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 3),
    _HpnicfDHCPSrvGlobalPoolNetworkMask_Type()
)
hpnicfDHCPSrvGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolNetworkMask.setStatus("current")
_HpnicfDHCPSrvGlobalPoolHostIPAddr_Type = IpAddress
_HpnicfDHCPSrvGlobalPoolHostIPAddr_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolHostIPAddr = _HpnicfDHCPSrvGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 4),
    _HpnicfDHCPSrvGlobalPoolHostIPAddr_Type()
)
hpnicfDHCPSrvGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolHostIPAddr.setStatus("current")
_HpnicfDHCPSrvGlobalPoolHostMask_Type = IpAddress
_HpnicfDHCPSrvGlobalPoolHostMask_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolHostMask = _HpnicfDHCPSrvGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 5),
    _HpnicfDHCPSrvGlobalPoolHostMask_Type()
)
hpnicfDHCPSrvGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolHostMask.setStatus("current")
_HpnicfDHCPSrvGlobalPoolHostHAddr_Type = MacAddress
_HpnicfDHCPSrvGlobalPoolHostHAddr_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolHostHAddr = _HpnicfDHCPSrvGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 6),
    _HpnicfDHCPSrvGlobalPoolHostHAddr_Type()
)
hpnicfDHCPSrvGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolHostHAddr.setStatus("current")


class _HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlobalPoolCfgUndoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undohosthaddr", 3),
          ("undohostip", 2),
          ("undonetworkip", 1))
    )


_HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolCfgUndoFlag = _HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 7),
    _HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Type()
)
hpnicfDHCPSrvGlobalPoolCfgUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolCfgUndoFlag.setStatus("current")
_HpnicfDHCPSrvGlobalPoolStartAddr_Type = IpAddress
_HpnicfDHCPSrvGlobalPoolStartAddr_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolStartAddr = _HpnicfDHCPSrvGlobalPoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 8),
    _HpnicfDHCPSrvGlobalPoolStartAddr_Type()
)
hpnicfDHCPSrvGlobalPoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolStartAddr.setStatus("current")
_HpnicfDHCPSrvGlobalPoolEndAddr_Type = IpAddress
_HpnicfDHCPSrvGlobalPoolEndAddr_Object = MibTableColumn
hpnicfDHCPSrvGlobalPoolEndAddr = _HpnicfDHCPSrvGlobalPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 3, 1, 9),
    _HpnicfDHCPSrvGlobalPoolEndAddr_Type()
)
hpnicfDHCPSrvGlobalPoolEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolEndAddr.setStatus("current")
_HpnicfDHCPSrvGlobalPoolParaTable_Object = MibTable
hpnicfDHCPSrvGlobalPoolParaTable = _HpnicfDHCPSrvGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolParaTable.setStatus("current")
_HpnicfDHCPSrvGlobalPoolParaEntry_Object = MibTableRow
hpnicfDHCPSrvGlobalPoolParaEntry = _HpnicfDHCPSrvGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1)
)
hpnicfDHCPSrvGlobalPoolParaEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolParaEntry.setStatus("current")


class _HpnicfDHCPSrvGlbPoolLeaseDay_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpnicfDHCPSrvGlbPoolLeaseDay_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolLeaseDay_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseDay = _HpnicfDHCPSrvGlbPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 1),
    _HpnicfDHCPSrvGlbPoolLeaseDay_Type()
)
hpnicfDHCPSrvGlbPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolLeaseDay.setStatus("current")


class _HpnicfDHCPSrvGlbPoolLeaseHour_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HpnicfDHCPSrvGlbPoolLeaseHour_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolLeaseHour_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseHour = _HpnicfDHCPSrvGlbPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 2),
    _HpnicfDHCPSrvGlbPoolLeaseHour_Type()
)
hpnicfDHCPSrvGlbPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolLeaseHour.setStatus("current")


class _HpnicfDHCPSrvGlbPoolLeaseMinute_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpnicfDHCPSrvGlbPoolLeaseMinute_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolLeaseMinute_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseMinute = _HpnicfDHCPSrvGlbPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 3),
    _HpnicfDHCPSrvGlbPoolLeaseMinute_Type()
)
hpnicfDHCPSrvGlbPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolLeaseMinute.setStatus("current")


class _HpnicfDHCPSrvGlbPoolLeaseUnlimited_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolLeaseUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unlimited", 1))
    )


_HpnicfDHCPSrvGlbPoolLeaseUnlimited_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolLeaseUnlimited_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseUnlimited = _HpnicfDHCPSrvGlbPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 4),
    _HpnicfDHCPSrvGlbPoolLeaseUnlimited_Type()
)
hpnicfDHCPSrvGlbPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolLeaseUnlimited.setStatus("current")


class _HpnicfDHCPSrvGlbPoolDomainName_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSrvGlbPoolDomainName_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolDomainName_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolDomainName = _HpnicfDHCPSrvGlbPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 5),
    _HpnicfDHCPSrvGlbPoolDomainName_Type()
)
hpnicfDHCPSrvGlbPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolDomainName.setStatus("current")


class _HpnicfDHCPSrvGlbPoolCliGWIPStr_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolCliGWIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSrvGlbPoolCliGWIPStr_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolCliGWIPStr_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliGWIPStr = _HpnicfDHCPSrvGlbPoolCliGWIPStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 6),
    _HpnicfDHCPSrvGlbPoolCliGWIPStr_Type()
)
hpnicfDHCPSrvGlbPoolCliGWIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliGWIPStr.setStatus("current")
_HpnicfDHCPSrvGlbPoolCliGWIPUndo_Type = IpAddress
_HpnicfDHCPSrvGlbPoolCliGWIPUndo_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliGWIPUndo = _HpnicfDHCPSrvGlbPoolCliGWIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 7),
    _HpnicfDHCPSrvGlbPoolCliGWIPUndo_Type()
)
hpnicfDHCPSrvGlbPoolCliGWIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliGWIPUndo.setStatus("current")


class _HpnicfDHCPSrvGlbPoolCliDNSIPStr_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolCliDNSIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSrvGlbPoolCliDNSIPStr_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolCliDNSIPStr_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliDNSIPStr = _HpnicfDHCPSrvGlbPoolCliDNSIPStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 8),
    _HpnicfDHCPSrvGlbPoolCliDNSIPStr_Type()
)
hpnicfDHCPSrvGlbPoolCliDNSIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliDNSIPStr.setStatus("current")
_HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Type = IpAddress
_HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliDNSIPUndo = _HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 9),
    _HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Type()
)
hpnicfDHCPSrvGlbPoolCliDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliDNSIPUndo.setStatus("current")


class _HpnicfDHCPSrvGlbPoolCliNetbiosType_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolCliNetbiosType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bnode", 1),
          ("hnode", 8),
          ("mnode", 4),
          ("null", 0),
          ("pnode", 2))
    )


_HpnicfDHCPSrvGlbPoolCliNetbiosType_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolCliNetbiosType_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliNetbiosType = _HpnicfDHCPSrvGlbPoolCliNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 10),
    _HpnicfDHCPSrvGlbPoolCliNetbiosType_Type()
)
hpnicfDHCPSrvGlbPoolCliNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliNetbiosType.setStatus("current")


class _HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolCliNbnsIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliNbnsIPStr = _HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 11),
    _HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Type()
)
hpnicfDHCPSrvGlbPoolCliNbnsIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliNbnsIPStr.setStatus("current")
_HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Type = IpAddress
_HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolCliNbnsIPUndo = _HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 12),
    _HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Type()
)
hpnicfDHCPSrvGlbPoolCliNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolCliNbnsIPUndo.setStatus("current")


class _HpnicfDHCPSrvGlbPoolParaUndoFlag_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolParaUndoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undoDns", 4),
          ("undoDomain", 1),
          ("undoGateway", 3),
          ("undoLease", 2),
          ("undoNbType", 6),
          ("undoNbns", 5))
    )


_HpnicfDHCPSrvGlbPoolParaUndoFlag_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolParaUndoFlag_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolParaUndoFlag = _HpnicfDHCPSrvGlbPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 13),
    _HpnicfDHCPSrvGlbPoolParaUndoFlag_Type()
)
hpnicfDHCPSrvGlbPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolParaUndoFlag.setStatus("current")


class _HpnicfDHCPSrvGlbPoolIPInUseReset_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDHCPSrvGlbPoolIPInUseReset_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolIPInUseReset_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolIPInUseReset = _HpnicfDHCPSrvGlbPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 14),
    _HpnicfDHCPSrvGlbPoolIPInUseReset_Type()
)
hpnicfDHCPSrvGlbPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolIPInUseReset.setStatus("current")
_HpnicfDHCPSrvGlbPoolLeaseTime_Type = TimeTicks
_HpnicfDHCPSrvGlbPoolLeaseTime_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseTime = _HpnicfDHCPSrvGlbPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 15),
    _HpnicfDHCPSrvGlbPoolLeaseTime_Type()
)
hpnicfDHCPSrvGlbPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolLeaseTime.setStatus("current")
_HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Type = IpAddress
_HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolPrimaryDNSIP = _HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 16),
    _HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Type()
)
hpnicfDHCPSrvGlbPoolPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolPrimaryDNSIP.setStatus("current")
_HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Type = IpAddress
_HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolSecondaryDNSIP = _HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 17),
    _HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Type()
)
hpnicfDHCPSrvGlbPoolSecondaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolSecondaryDNSIP.setStatus("current")


class _HpnicfDHCPSrvGlbPoolLeaseSecond_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolLeaseSecond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpnicfDHCPSrvGlbPoolLeaseSecond_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolLeaseSecond_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseSecond = _HpnicfDHCPSrvGlbPoolLeaseSecond_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 4, 1, 18),
    _HpnicfDHCPSrvGlbPoolLeaseSecond_Type()
)
hpnicfDHCPSrvGlbPoolLeaseSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolLeaseSecond.setStatus("current")
_HpnicfDHCPSrvGlobalPoolOptionTable_Object = MibTable
hpnicfDHCPSrvGlobalPoolOptionTable = _HpnicfDHCPSrvGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolOptionTable.setStatus("current")
_HpnicfDHCPSrvGlobalPoolOptionEntry_Object = MibTableRow
hpnicfDHCPSrvGlobalPoolOptionEntry = _HpnicfDHCPSrvGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1)
)
hpnicfDHCPSrvGlobalPoolOptionEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlbPoolOptCode"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolOptionEntry.setStatus("current")


class _HpnicfDHCPSrvGlbPoolOptCode_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpnicfDHCPSrvGlbPoolOptCode_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolOptCode_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOptCode = _HpnicfDHCPSrvGlbPoolOptCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1, 1),
    _HpnicfDHCPSrvGlbPoolOptCode_Type()
)
hpnicfDHCPSrvGlbPoolOptCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOptCode.setStatus("current")


class _HpnicfDHCPSrvGlbPoolOptType_Type(Integer32):
    """Custom type hpnicfDHCPSrvGlbPoolOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_HpnicfDHCPSrvGlbPoolOptType_Type.__name__ = "Integer32"
_HpnicfDHCPSrvGlbPoolOptType_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOptType = _HpnicfDHCPSrvGlbPoolOptType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1, 2),
    _HpnicfDHCPSrvGlbPoolOptType_Type()
)
hpnicfDHCPSrvGlbPoolOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOptType.setStatus("current")


class _HpnicfDHCPSrvGlbPoolOptAscii_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolOptAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDHCPSrvGlbPoolOptAscii_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolOptAscii_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOptAscii = _HpnicfDHCPSrvGlbPoolOptAscii_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1, 3),
    _HpnicfDHCPSrvGlbPoolOptAscii_Type()
)
hpnicfDHCPSrvGlbPoolOptAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOptAscii.setStatus("current")


class _HpnicfDHCPSrvGlbPoolOptHexString_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolOptHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 573),
    )


_HpnicfDHCPSrvGlbPoolOptHexString_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolOptHexString_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOptHexString = _HpnicfDHCPSrvGlbPoolOptHexString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1, 4),
    _HpnicfDHCPSrvGlbPoolOptHexString_Type()
)
hpnicfDHCPSrvGlbPoolOptHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOptHexString.setStatus("current")


class _HpnicfDHCPSrvGlbPoolOptIPString_Type(OctetString):
    """Custom type hpnicfDHCPSrvGlbPoolOptIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSrvGlbPoolOptIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSrvGlbPoolOptIPString_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOptIPString = _HpnicfDHCPSrvGlbPoolOptIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1, 5),
    _HpnicfDHCPSrvGlbPoolOptIPString_Type()
)
hpnicfDHCPSrvGlbPoolOptIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOptIPString.setStatus("current")
_HpnicfDHCPSrvGlbPoolOptRowStatus_Type = RowStatus
_HpnicfDHCPSrvGlbPoolOptRowStatus_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOptRowStatus = _HpnicfDHCPSrvGlbPoolOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 5, 1, 6),
    _HpnicfDHCPSrvGlbPoolOptRowStatus_Type()
)
hpnicfDHCPSrvGlbPoolOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOptRowStatus.setStatus("current")
_HpnicfDHCPSrvGlobalPoolStatTable_Object = MibTable
hpnicfDHCPSrvGlobalPoolStatTable = _HpnicfDHCPSrvGlobalPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolStatTable.setStatus("current")
_HpnicfDHCPSrvGlobalPoolStatEntry_Object = MibTableRow
hpnicfDHCPSrvGlobalPoolStatEntry = _HpnicfDHCPSrvGlobalPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1)
)
hpnicfDHCPSrvGlobalPoolStatEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlobalPoolStatEntry.setStatus("current")
_HpnicfDHCPSrvGlbPoolIPPoolUsage_Type = Integer32
_HpnicfDHCPSrvGlbPoolIPPoolUsage_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolIPPoolUsage = _HpnicfDHCPSrvGlbPoolIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 1),
    _HpnicfDHCPSrvGlbPoolIPPoolUsage_Type()
)
hpnicfDHCPSrvGlbPoolIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolIPPoolUsage.setStatus("current")
_HpnicfDHCPSrvGlbPoolReqTimes_Type = Counter32
_HpnicfDHCPSrvGlbPoolReqTimes_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolReqTimes = _HpnicfDHCPSrvGlbPoolReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 2),
    _HpnicfDHCPSrvGlbPoolReqTimes_Type()
)
hpnicfDHCPSrvGlbPoolReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolReqTimes.setStatus("current")
_HpnicfDHCPSrvGlbPoolSuccessTimes_Type = Counter32
_HpnicfDHCPSrvGlbPoolSuccessTimes_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolSuccessTimes = _HpnicfDHCPSrvGlbPoolSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 3),
    _HpnicfDHCPSrvGlbPoolSuccessTimes_Type()
)
hpnicfDHCPSrvGlbPoolSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolSuccessTimes.setStatus("current")
_HpnicfDHCPSrvGlbPoolDiscoverTimes_Type = Counter32
_HpnicfDHCPSrvGlbPoolDiscoverTimes_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolDiscoverTimes = _HpnicfDHCPSrvGlbPoolDiscoverTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 4),
    _HpnicfDHCPSrvGlbPoolDiscoverTimes_Type()
)
hpnicfDHCPSrvGlbPoolDiscoverTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolDiscoverTimes.setStatus("current")
_HpnicfDHCPSrvGlbPoolOfferTimes_Type = Counter32
_HpnicfDHCPSrvGlbPoolOfferTimes_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolOfferTimes = _HpnicfDHCPSrvGlbPoolOfferTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 5),
    _HpnicfDHCPSrvGlbPoolOfferTimes_Type()
)
hpnicfDHCPSrvGlbPoolOfferTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolOfferTimes.setStatus("current")
_HpnicfDHCPSrvGlbPoolACKTimes_Type = Counter32
_HpnicfDHCPSrvGlbPoolACKTimes_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolACKTimes = _HpnicfDHCPSrvGlbPoolACKTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 6),
    _HpnicfDHCPSrvGlbPoolACKTimes_Type()
)
hpnicfDHCPSrvGlbPoolACKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolACKTimes.setStatus("current")
_HpnicfDHCPSrvGlbPoolTotalIpNum_Type = Counter32
_HpnicfDHCPSrvGlbPoolTotalIpNum_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolTotalIpNum = _HpnicfDHCPSrvGlbPoolTotalIpNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 7),
    _HpnicfDHCPSrvGlbPoolTotalIpNum_Type()
)
hpnicfDHCPSrvGlbPoolTotalIpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolTotalIpNum.setStatus("current")
_HpnicfDHCPSrvGlbPoolInUsedIpNum_Type = Counter32
_HpnicfDHCPSrvGlbPoolInUsedIpNum_Object = MibTableColumn
hpnicfDHCPSrvGlbPoolInUsedIpNum = _HpnicfDHCPSrvGlbPoolInUsedIpNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 6, 1, 8),
    _HpnicfDHCPSrvGlbPoolInUsedIpNum_Type()
)
hpnicfDHCPSrvGlbPoolInUsedIpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSrvGlbPoolInUsedIpNum.setStatus("current")
_HpnicfDHCPSvrOptionGroupTable_Object = MibTable
hpnicfDHCPSvrOptionGroupTable = _HpnicfDHCPSvrOptionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionGroupTable.setStatus("current")
_HpnicfDHCPSvrOptionGroupEntry_Object = MibTableRow
hpnicfDHCPSvrOptionGroupEntry = _HpnicfDHCPSvrOptionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 7, 1)
)
hpnicfDHCPSvrOptionGroupEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSvrOptionGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionGroupEntry.setStatus("current")


class _HpnicfDHCPSvrOptionGroupIndex_Type(Integer32):
    """Custom type hpnicfDHCPSvrOptionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDHCPSvrOptionGroupIndex_Type.__name__ = "Integer32"
_HpnicfDHCPSvrOptionGroupIndex_Object = MibTableColumn
hpnicfDHCPSvrOptionGroupIndex = _HpnicfDHCPSvrOptionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 7, 1, 1),
    _HpnicfDHCPSvrOptionGroupIndex_Type()
)
hpnicfDHCPSvrOptionGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionGroupIndex.setStatus("current")
_HpnicfDHCPSvrOptionGroupRowstatus_Type = RowStatus
_HpnicfDHCPSvrOptionGroupRowstatus_Object = MibTableColumn
hpnicfDHCPSvrOptionGroupRowstatus = _HpnicfDHCPSvrOptionGroupRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 7, 1, 2),
    _HpnicfDHCPSvrOptionGroupRowstatus_Type()
)
hpnicfDHCPSvrOptionGroupRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionGroupRowstatus.setStatus("current")
_HpnicfDHCPSvrOptionTable_Object = MibTable
hpnicfDHCPSvrOptionTable = _HpnicfDHCPSvrOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionTable.setStatus("current")
_HpnicfDHCPSvrOptionEntry_Object = MibTableRow
hpnicfDHCPSvrOptionEntry = _HpnicfDHCPSvrOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1)
)
hpnicfDHCPSvrOptionEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSvrOptionGroupIndex"),
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSvrOptionCode"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionEntry.setStatus("current")


class _HpnicfDHCPSvrOptionCode_Type(Integer32):
    """Custom type hpnicfDHCPSvrOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpnicfDHCPSvrOptionCode_Type.__name__ = "Integer32"
_HpnicfDHCPSvrOptionCode_Object = MibTableColumn
hpnicfDHCPSvrOptionCode = _HpnicfDHCPSvrOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1, 1),
    _HpnicfDHCPSvrOptionCode_Type()
)
hpnicfDHCPSvrOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionCode.setStatus("current")


class _HpnicfDHCPSvrOptionType_Type(Integer32):
    """Custom type hpnicfDHCPSvrOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_HpnicfDHCPSvrOptionType_Type.__name__ = "Integer32"
_HpnicfDHCPSvrOptionType_Object = MibTableColumn
hpnicfDHCPSvrOptionType = _HpnicfDHCPSvrOptionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1, 2),
    _HpnicfDHCPSvrOptionType_Type()
)
hpnicfDHCPSvrOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionType.setStatus("current")


class _HpnicfDHCPSvrOptionAsciiString_Type(OctetString):
    """Custom type hpnicfDHCPSvrOptionAsciiString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSvrOptionAsciiString_Type.__name__ = "OctetString"
_HpnicfDHCPSvrOptionAsciiString_Object = MibTableColumn
hpnicfDHCPSvrOptionAsciiString = _HpnicfDHCPSvrOptionAsciiString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1, 3),
    _HpnicfDHCPSvrOptionAsciiString_Type()
)
hpnicfDHCPSvrOptionAsciiString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionAsciiString.setStatus("current")


class _HpnicfDHCPSvrOptionHexString_Type(OctetString):
    """Custom type hpnicfDHCPSvrOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 573),
    )


_HpnicfDHCPSvrOptionHexString_Type.__name__ = "OctetString"
_HpnicfDHCPSvrOptionHexString_Object = MibTableColumn
hpnicfDHCPSvrOptionHexString = _HpnicfDHCPSvrOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1, 4),
    _HpnicfDHCPSvrOptionHexString_Type()
)
hpnicfDHCPSvrOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionHexString.setStatus("current")


class _HpnicfDHCPSvrOptionIPString_Type(OctetString):
    """Custom type hpnicfDHCPSvrOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSvrOptionIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSvrOptionIPString_Object = MibTableColumn
hpnicfDHCPSvrOptionIPString = _HpnicfDHCPSvrOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1, 5),
    _HpnicfDHCPSvrOptionIPString_Type()
)
hpnicfDHCPSvrOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionIPString.setStatus("current")
_HpnicfDHCPSvrOptionRowstatus_Type = RowStatus
_HpnicfDHCPSvrOptionRowstatus_Object = MibTableColumn
hpnicfDHCPSvrOptionRowstatus = _HpnicfDHCPSvrOptionRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 8, 1, 6),
    _HpnicfDHCPSvrOptionRowstatus_Type()
)
hpnicfDHCPSvrOptionRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrOptionRowstatus.setStatus("current")
_HpnicfDHCPSvrVerifyMacTable_Object = MibTable
hpnicfDHCPSvrVerifyMacTable = _HpnicfDHCPSvrVerifyMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrVerifyMacTable.setStatus("current")
_HpnicfDHCPSvrVerifyMacEntry_Object = MibTableRow
hpnicfDHCPSvrVerifyMacEntry = _HpnicfDHCPSvrVerifyMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 9, 1)
)
hpnicfDHCPSvrVerifyMacEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrVerifyMacEntry.setStatus("current")


class _HpnicfDHCPSvrVerifyMacSwitch_Type(Integer32):
    """Custom type hpnicfDHCPSvrVerifyMacSwitch based on Integer32"""
    defaultValue = 2

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


_HpnicfDHCPSvrVerifyMacSwitch_Type.__name__ = "Integer32"
_HpnicfDHCPSvrVerifyMacSwitch_Object = MibTableColumn
hpnicfDHCPSvrVerifyMacSwitch = _HpnicfDHCPSvrVerifyMacSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 9, 1, 1),
    _HpnicfDHCPSvrVerifyMacSwitch_Type()
)
hpnicfDHCPSvrVerifyMacSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrVerifyMacSwitch.setStatus("current")
_HpnicfDHCPSvrPoolMacTable_Object = MibTable
hpnicfDHCPSvrPoolMacTable = _HpnicfDHCPSvrPoolMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrPoolMacTable.setStatus("current")
_HpnicfDHCPSvrPoolMacEntry_Object = MibTableRow
hpnicfDHCPSvrPoolMacEntry = _HpnicfDHCPSvrPoolMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 10, 1)
)
hpnicfDHCPSvrPoolMacEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSrvGlobalPoolName"),
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSvrPoolMac"),
    (0, "HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPSvrPoolMacMask"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSvrPoolMacEntry.setStatus("current")
_HpnicfDHCPSvrPoolMac_Type = MacAddress
_HpnicfDHCPSvrPoolMac_Object = MibTableColumn
hpnicfDHCPSvrPoolMac = _HpnicfDHCPSvrPoolMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 10, 1, 1),
    _HpnicfDHCPSvrPoolMac_Type()
)
hpnicfDHCPSvrPoolMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrPoolMac.setStatus("current")
_HpnicfDHCPSvrPoolMacMask_Type = MacAddress
_HpnicfDHCPSvrPoolMacMask_Object = MibTableColumn
hpnicfDHCPSvrPoolMacMask = _HpnicfDHCPSvrPoolMacMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 10, 1, 2),
    _HpnicfDHCPSvrPoolMacMask_Type()
)
hpnicfDHCPSvrPoolMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrPoolMacMask.setStatus("current")


class _HpnicfDHCPSvrPoolMacOptIndex_Type(Integer32):
    """Custom type hpnicfDHCPSvrPoolMacOptIndex based on Integer32"""
    defaultValue = 0


_HpnicfDHCPSvrPoolMacOptIndex_Object = MibTableColumn
hpnicfDHCPSvrPoolMacOptIndex = _HpnicfDHCPSvrPoolMacOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 10, 1, 3),
    _HpnicfDHCPSvrPoolMacOptIndex_Type()
)
hpnicfDHCPSvrPoolMacOptIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrPoolMacOptIndex.setStatus("current")
_HpnicfDHCPSvrPoolMacRowstatus_Type = RowStatus
_HpnicfDHCPSvrPoolMacRowstatus_Object = MibTableColumn
hpnicfDHCPSvrPoolMacRowstatus = _HpnicfDHCPSvrPoolMacRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 2, 10, 1, 4),
    _HpnicfDHCPSvrPoolMacRowstatus_Type()
)
hpnicfDHCPSvrPoolMacRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSvrPoolMacRowstatus.setStatus("current")
_HpnicfDHCPServerTraps_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerTraps = _HpnicfDHCPServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3)
)
_HpnicfDHCPServerTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerTrapPrefix = _HpnicfDHCPServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 0)
)
_HpnicfDHCPServerTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerTrapObjects = _HpnicfDHCPServerTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 1)
)
_HpnicfDHCPServerFirstTrapTime_Type = TimeTicks
_HpnicfDHCPServerFirstTrapTime_Object = MibScalar
hpnicfDHCPServerFirstTrapTime = _HpnicfDHCPServerFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 1, 1),
    _HpnicfDHCPServerFirstTrapTime_Type()
)
hpnicfDHCPServerFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDHCPServerFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDHCPServerAddrExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 0, 1)
)
hpnicfDHCPServerAddrExhaust.setObjects(
      *(("HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPServerPoolName"),
        ("HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDHCPServerAddrExhaust.setStatus(
        "current"
    )

hpnicfDHCPServerAddrExhaustRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 0, 2)
)
hpnicfDHCPServerAddrExhaustRecover.setObjects(
      *(("HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPServerPoolName"),
        ("HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDHCPServerAddrExhaustRecover.setStatus(
        "current"
    )

hpnicfDHCPServerAvgIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 0, 3)
)
hpnicfDHCPServerAvgIpUsageOverflow.setObjects(
    ("HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hpnicfDHCPServerAvgIpUsageOverflow.setStatus(
        "current"
    )

hpnicfDHCPServerMaxIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 0, 4)
)
hpnicfDHCPServerMaxIpUsageOverflow.setObjects(
    ("HPN-ICF-DHCP-SERVER-MIB", "hpnicfDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hpnicfDHCPServerMaxIpUsageOverflow.setStatus(
        "current"
    )

hpnicfDHCPServerAllocateOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101, 3, 0, 5)
)
if mibBuilder.loadTexts:
    hpnicfDHCPServerAllocateOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCP-SERVER-MIB",
    **{"hpnicfDHCPServer": hpnicfDHCPServer,
       "hpnicfDHCPServerObjects": hpnicfDHCPServerObjects,
       "hpnicfDHCPServerIPPoolUsage": hpnicfDHCPServerIPPoolUsage,
       "hpnicfDHCPServerReqTimes": hpnicfDHCPServerReqTimes,
       "hpnicfDHCPServerReqSuccessTimes": hpnicfDHCPServerReqSuccessTimes,
       "hpnicfDHCPServerAvgIpUseThreshold": hpnicfDHCPServerAvgIpUseThreshold,
       "hpnicfDHCPServerMaxIpUseThreshold": hpnicfDHCPServerMaxIpUseThreshold,
       "hpnicfDHCPServerAllocateThreshold": hpnicfDHCPServerAllocateThreshold,
       "hpnicfDHCPServerTables": hpnicfDHCPServerTables,
       "hpnicfDHCPServerPoolName": hpnicfDHCPServerPoolName,
       "hpnicfDHCPSrvGlobalPoolTable": hpnicfDHCPSrvGlobalPoolTable,
       "hpnicfDHCPSrvGlobalPoolEntry": hpnicfDHCPSrvGlobalPoolEntry,
       "hpnicfDHCPSrvGlobalPoolName": hpnicfDHCPSrvGlobalPoolName,
       "hpnicfDHCPSrvGlobalPoolRowStatus": hpnicfDHCPSrvGlobalPoolRowStatus,
       "hpnicfDHCPSrvGlobalPoolConfigTable": hpnicfDHCPSrvGlobalPoolConfigTable,
       "hpnicfDHCPSrvGlobalPoolConfigEntry": hpnicfDHCPSrvGlobalPoolConfigEntry,
       "hpnicfDHCPSrvGlobalPoolType": hpnicfDHCPSrvGlobalPoolType,
       "hpnicfDHCPSrvGlobalPoolNetwork": hpnicfDHCPSrvGlobalPoolNetwork,
       "hpnicfDHCPSrvGlobalPoolNetworkMask": hpnicfDHCPSrvGlobalPoolNetworkMask,
       "hpnicfDHCPSrvGlobalPoolHostIPAddr": hpnicfDHCPSrvGlobalPoolHostIPAddr,
       "hpnicfDHCPSrvGlobalPoolHostMask": hpnicfDHCPSrvGlobalPoolHostMask,
       "hpnicfDHCPSrvGlobalPoolHostHAddr": hpnicfDHCPSrvGlobalPoolHostHAddr,
       "hpnicfDHCPSrvGlobalPoolCfgUndoFlag": hpnicfDHCPSrvGlobalPoolCfgUndoFlag,
       "hpnicfDHCPSrvGlobalPoolStartAddr": hpnicfDHCPSrvGlobalPoolStartAddr,
       "hpnicfDHCPSrvGlobalPoolEndAddr": hpnicfDHCPSrvGlobalPoolEndAddr,
       "hpnicfDHCPSrvGlobalPoolParaTable": hpnicfDHCPSrvGlobalPoolParaTable,
       "hpnicfDHCPSrvGlobalPoolParaEntry": hpnicfDHCPSrvGlobalPoolParaEntry,
       "hpnicfDHCPSrvGlbPoolLeaseDay": hpnicfDHCPSrvGlbPoolLeaseDay,
       "hpnicfDHCPSrvGlbPoolLeaseHour": hpnicfDHCPSrvGlbPoolLeaseHour,
       "hpnicfDHCPSrvGlbPoolLeaseMinute": hpnicfDHCPSrvGlbPoolLeaseMinute,
       "hpnicfDHCPSrvGlbPoolLeaseUnlimited": hpnicfDHCPSrvGlbPoolLeaseUnlimited,
       "hpnicfDHCPSrvGlbPoolDomainName": hpnicfDHCPSrvGlbPoolDomainName,
       "hpnicfDHCPSrvGlbPoolCliGWIPStr": hpnicfDHCPSrvGlbPoolCliGWIPStr,
       "hpnicfDHCPSrvGlbPoolCliGWIPUndo": hpnicfDHCPSrvGlbPoolCliGWIPUndo,
       "hpnicfDHCPSrvGlbPoolCliDNSIPStr": hpnicfDHCPSrvGlbPoolCliDNSIPStr,
       "hpnicfDHCPSrvGlbPoolCliDNSIPUndo": hpnicfDHCPSrvGlbPoolCliDNSIPUndo,
       "hpnicfDHCPSrvGlbPoolCliNetbiosType": hpnicfDHCPSrvGlbPoolCliNetbiosType,
       "hpnicfDHCPSrvGlbPoolCliNbnsIPStr": hpnicfDHCPSrvGlbPoolCliNbnsIPStr,
       "hpnicfDHCPSrvGlbPoolCliNbnsIPUndo": hpnicfDHCPSrvGlbPoolCliNbnsIPUndo,
       "hpnicfDHCPSrvGlbPoolParaUndoFlag": hpnicfDHCPSrvGlbPoolParaUndoFlag,
       "hpnicfDHCPSrvGlbPoolIPInUseReset": hpnicfDHCPSrvGlbPoolIPInUseReset,
       "hpnicfDHCPSrvGlbPoolLeaseTime": hpnicfDHCPSrvGlbPoolLeaseTime,
       "hpnicfDHCPSrvGlbPoolPrimaryDNSIP": hpnicfDHCPSrvGlbPoolPrimaryDNSIP,
       "hpnicfDHCPSrvGlbPoolSecondaryDNSIP": hpnicfDHCPSrvGlbPoolSecondaryDNSIP,
       "hpnicfDHCPSrvGlbPoolLeaseSecond": hpnicfDHCPSrvGlbPoolLeaseSecond,
       "hpnicfDHCPSrvGlobalPoolOptionTable": hpnicfDHCPSrvGlobalPoolOptionTable,
       "hpnicfDHCPSrvGlobalPoolOptionEntry": hpnicfDHCPSrvGlobalPoolOptionEntry,
       "hpnicfDHCPSrvGlbPoolOptCode": hpnicfDHCPSrvGlbPoolOptCode,
       "hpnicfDHCPSrvGlbPoolOptType": hpnicfDHCPSrvGlbPoolOptType,
       "hpnicfDHCPSrvGlbPoolOptAscii": hpnicfDHCPSrvGlbPoolOptAscii,
       "hpnicfDHCPSrvGlbPoolOptHexString": hpnicfDHCPSrvGlbPoolOptHexString,
       "hpnicfDHCPSrvGlbPoolOptIPString": hpnicfDHCPSrvGlbPoolOptIPString,
       "hpnicfDHCPSrvGlbPoolOptRowStatus": hpnicfDHCPSrvGlbPoolOptRowStatus,
       "hpnicfDHCPSrvGlobalPoolStatTable": hpnicfDHCPSrvGlobalPoolStatTable,
       "hpnicfDHCPSrvGlobalPoolStatEntry": hpnicfDHCPSrvGlobalPoolStatEntry,
       "hpnicfDHCPSrvGlbPoolIPPoolUsage": hpnicfDHCPSrvGlbPoolIPPoolUsage,
       "hpnicfDHCPSrvGlbPoolReqTimes": hpnicfDHCPSrvGlbPoolReqTimes,
       "hpnicfDHCPSrvGlbPoolSuccessTimes": hpnicfDHCPSrvGlbPoolSuccessTimes,
       "hpnicfDHCPSrvGlbPoolDiscoverTimes": hpnicfDHCPSrvGlbPoolDiscoverTimes,
       "hpnicfDHCPSrvGlbPoolOfferTimes": hpnicfDHCPSrvGlbPoolOfferTimes,
       "hpnicfDHCPSrvGlbPoolACKTimes": hpnicfDHCPSrvGlbPoolACKTimes,
       "hpnicfDHCPSrvGlbPoolTotalIpNum": hpnicfDHCPSrvGlbPoolTotalIpNum,
       "hpnicfDHCPSrvGlbPoolInUsedIpNum": hpnicfDHCPSrvGlbPoolInUsedIpNum,
       "hpnicfDHCPSvrOptionGroupTable": hpnicfDHCPSvrOptionGroupTable,
       "hpnicfDHCPSvrOptionGroupEntry": hpnicfDHCPSvrOptionGroupEntry,
       "hpnicfDHCPSvrOptionGroupIndex": hpnicfDHCPSvrOptionGroupIndex,
       "hpnicfDHCPSvrOptionGroupRowstatus": hpnicfDHCPSvrOptionGroupRowstatus,
       "hpnicfDHCPSvrOptionTable": hpnicfDHCPSvrOptionTable,
       "hpnicfDHCPSvrOptionEntry": hpnicfDHCPSvrOptionEntry,
       "hpnicfDHCPSvrOptionCode": hpnicfDHCPSvrOptionCode,
       "hpnicfDHCPSvrOptionType": hpnicfDHCPSvrOptionType,
       "hpnicfDHCPSvrOptionAsciiString": hpnicfDHCPSvrOptionAsciiString,
       "hpnicfDHCPSvrOptionHexString": hpnicfDHCPSvrOptionHexString,
       "hpnicfDHCPSvrOptionIPString": hpnicfDHCPSvrOptionIPString,
       "hpnicfDHCPSvrOptionRowstatus": hpnicfDHCPSvrOptionRowstatus,
       "hpnicfDHCPSvrVerifyMacTable": hpnicfDHCPSvrVerifyMacTable,
       "hpnicfDHCPSvrVerifyMacEntry": hpnicfDHCPSvrVerifyMacEntry,
       "hpnicfDHCPSvrVerifyMacSwitch": hpnicfDHCPSvrVerifyMacSwitch,
       "hpnicfDHCPSvrPoolMacTable": hpnicfDHCPSvrPoolMacTable,
       "hpnicfDHCPSvrPoolMacEntry": hpnicfDHCPSvrPoolMacEntry,
       "hpnicfDHCPSvrPoolMac": hpnicfDHCPSvrPoolMac,
       "hpnicfDHCPSvrPoolMacMask": hpnicfDHCPSvrPoolMacMask,
       "hpnicfDHCPSvrPoolMacOptIndex": hpnicfDHCPSvrPoolMacOptIndex,
       "hpnicfDHCPSvrPoolMacRowstatus": hpnicfDHCPSvrPoolMacRowstatus,
       "hpnicfDHCPServerTraps": hpnicfDHCPServerTraps,
       "hpnicfDHCPServerTrapPrefix": hpnicfDHCPServerTrapPrefix,
       "hpnicfDHCPServerAddrExhaust": hpnicfDHCPServerAddrExhaust,
       "hpnicfDHCPServerAddrExhaustRecover": hpnicfDHCPServerAddrExhaustRecover,
       "hpnicfDHCPServerAvgIpUsageOverflow": hpnicfDHCPServerAvgIpUsageOverflow,
       "hpnicfDHCPServerMaxIpUsageOverflow": hpnicfDHCPServerMaxIpUsageOverflow,
       "hpnicfDHCPServerAllocateOverflow": hpnicfDHCPServerAllocateOverflow,
       "hpnicfDHCPServerTrapObjects": hpnicfDHCPServerTrapObjects,
       "hpnicfDHCPServerFirstTrapTime": hpnicfDHCPServerFirstTrapTime}
)
