# SNMP MIB module (HH3C-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:38 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cDHCPServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101)
)
hh3cDHCPServer.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDHCPServerObjects_ObjectIdentity = ObjectIdentity
hh3cDHCPServerObjects = _Hh3cDHCPServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1)
)
_Hh3cDHCPServerIPPoolUsage_Type = Integer32
_Hh3cDHCPServerIPPoolUsage_Object = MibScalar
hh3cDHCPServerIPPoolUsage = _Hh3cDHCPServerIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 1),
    _Hh3cDHCPServerIPPoolUsage_Type()
)
hh3cDHCPServerIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPServerIPPoolUsage.setStatus("current")
_Hh3cDHCPServerReqTimes_Type = Counter32
_Hh3cDHCPServerReqTimes_Object = MibScalar
hh3cDHCPServerReqTimes = _Hh3cDHCPServerReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 2),
    _Hh3cDHCPServerReqTimes_Type()
)
hh3cDHCPServerReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPServerReqTimes.setStatus("current")
_Hh3cDHCPServerReqSuccessTimes_Type = Counter32
_Hh3cDHCPServerReqSuccessTimes_Object = MibScalar
hh3cDHCPServerReqSuccessTimes = _Hh3cDHCPServerReqSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 3),
    _Hh3cDHCPServerReqSuccessTimes_Type()
)
hh3cDHCPServerReqSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPServerReqSuccessTimes.setStatus("current")


class _Hh3cDHCPServerAvgIpUseThreshold_Type(Integer32):
    """Custom type hh3cDHCPServerAvgIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDHCPServerAvgIpUseThreshold_Type.__name__ = "Integer32"
_Hh3cDHCPServerAvgIpUseThreshold_Object = MibScalar
hh3cDHCPServerAvgIpUseThreshold = _Hh3cDHCPServerAvgIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 4),
    _Hh3cDHCPServerAvgIpUseThreshold_Type()
)
hh3cDHCPServerAvgIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPServerAvgIpUseThreshold.setStatus("current")


class _Hh3cDHCPServerMaxIpUseThreshold_Type(Integer32):
    """Custom type hh3cDHCPServerMaxIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDHCPServerMaxIpUseThreshold_Type.__name__ = "Integer32"
_Hh3cDHCPServerMaxIpUseThreshold_Object = MibScalar
hh3cDHCPServerMaxIpUseThreshold = _Hh3cDHCPServerMaxIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 5),
    _Hh3cDHCPServerMaxIpUseThreshold_Type()
)
hh3cDHCPServerMaxIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPServerMaxIpUseThreshold.setStatus("current")


class _Hh3cDHCPServerAllocateThreshold_Type(Integer32):
    """Custom type hh3cDHCPServerAllocateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDHCPServerAllocateThreshold_Type.__name__ = "Integer32"
_Hh3cDHCPServerAllocateThreshold_Object = MibScalar
hh3cDHCPServerAllocateThreshold = _Hh3cDHCPServerAllocateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 6),
    _Hh3cDHCPServerAllocateThreshold_Type()
)
hh3cDHCPServerAllocateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPServerAllocateThreshold.setStatus("current")
_Hh3cDHCPServerTables_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTables = _Hh3cDHCPServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2)
)


class _Hh3cDHCPServerPoolName_Type(OctetString):
    """Custom type hh3cDHCPServerPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPServerPoolName_Type.__name__ = "OctetString"
_Hh3cDHCPServerPoolName_Object = MibScalar
hh3cDHCPServerPoolName = _Hh3cDHCPServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 1),
    _Hh3cDHCPServerPoolName_Type()
)
hh3cDHCPServerPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDHCPServerPoolName.setStatus("current")
_Hh3cDHCPSrvGlobalPoolTable_Object = MibTable
hh3cDHCPSrvGlobalPoolTable = _Hh3cDHCPSrvGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolEntry = _Hh3cDHCPSrvGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1)
)
hh3cDHCPSrvGlobalPoolEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolEntry.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolName_Type(OctetString):
    """Custom type hh3cDHCPSrvGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSrvGlobalPoolName_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlobalPoolName_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolName = _Hh3cDHCPSrvGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 1),
    _Hh3cDHCPSrvGlobalPoolName_Type()
)
hh3cDHCPSrvGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolName.setStatus("current")
_Hh3cDHCPSrvGlobalPoolRowStatus_Type = RowStatus
_Hh3cDHCPSrvGlobalPoolRowStatus_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolRowStatus = _Hh3cDHCPSrvGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 2),
    _Hh3cDHCPSrvGlobalPoolRowStatus_Type()
)
hh3cDHCPSrvGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolRowStatus.setStatus("current")
_Hh3cDHCPSrvGlobalPoolConfigTable_Object = MibTable
hh3cDHCPSrvGlobalPoolConfigTable = _Hh3cDHCPSrvGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolConfigTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolConfigEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolConfigEntry = _Hh3cDHCPSrvGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1)
)
hh3cDHCPSrvGlobalPoolConfigEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolConfigEntry.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolType_Type(Integer32):
    """Custom type hh3cDHCPSrvGlobalPoolType based on Integer32"""
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


_Hh3cDHCPSrvGlobalPoolType_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlobalPoolType_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolType = _Hh3cDHCPSrvGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 1),
    _Hh3cDHCPSrvGlobalPoolType_Type()
)
hh3cDHCPSrvGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolType.setStatus("current")
_Hh3cDHCPSrvGlobalPoolNetwork_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolNetwork_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolNetwork = _Hh3cDHCPSrvGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 2),
    _Hh3cDHCPSrvGlobalPoolNetwork_Type()
)
hh3cDHCPSrvGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolNetwork.setStatus("current")
_Hh3cDHCPSrvGlobalPoolNetworkMask_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolNetworkMask_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolNetworkMask = _Hh3cDHCPSrvGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 3),
    _Hh3cDHCPSrvGlobalPoolNetworkMask_Type()
)
hh3cDHCPSrvGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolNetworkMask.setStatus("current")
_Hh3cDHCPSrvGlobalPoolHostIPAddr_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolHostIPAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolHostIPAddr = _Hh3cDHCPSrvGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 4),
    _Hh3cDHCPSrvGlobalPoolHostIPAddr_Type()
)
hh3cDHCPSrvGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolHostIPAddr.setStatus("current")
_Hh3cDHCPSrvGlobalPoolHostMask_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolHostMask_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolHostMask = _Hh3cDHCPSrvGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 5),
    _Hh3cDHCPSrvGlobalPoolHostMask_Type()
)
hh3cDHCPSrvGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolHostMask.setStatus("current")
_Hh3cDHCPSrvGlobalPoolHostHAddr_Type = MacAddress
_Hh3cDHCPSrvGlobalPoolHostHAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolHostHAddr = _Hh3cDHCPSrvGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 6),
    _Hh3cDHCPSrvGlobalPoolHostHAddr_Type()
)
hh3cDHCPSrvGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolHostHAddr.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSrvGlobalPoolCfgUndoFlag based on Integer32"""
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


_Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolCfgUndoFlag = _Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 7),
    _Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Type()
)
hh3cDHCPSrvGlobalPoolCfgUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus("current")
_Hh3cDHCPSrvGlobalPoolStartAddr_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolStartAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolStartAddr = _Hh3cDHCPSrvGlobalPoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 8),
    _Hh3cDHCPSrvGlobalPoolStartAddr_Type()
)
hh3cDHCPSrvGlobalPoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolStartAddr.setStatus("current")
_Hh3cDHCPSrvGlobalPoolEndAddr_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolEndAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolEndAddr = _Hh3cDHCPSrvGlobalPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 9),
    _Hh3cDHCPSrvGlobalPoolEndAddr_Type()
)
hh3cDHCPSrvGlobalPoolEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolEndAddr.setStatus("current")
_Hh3cDHCPSrvGlobalPoolParaTable_Object = MibTable
hh3cDHCPSrvGlobalPoolParaTable = _Hh3cDHCPSrvGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolParaTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolParaEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolParaEntry = _Hh3cDHCPSrvGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1)
)
hh3cDHCPSrvGlobalPoolParaEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolParaEntry.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseDay_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_Hh3cDHCPSrvGlbPoolLeaseDay_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseDay_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseDay = _Hh3cDHCPSrvGlbPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 1),
    _Hh3cDHCPSrvGlbPoolLeaseDay_Type()
)
hh3cDHCPSrvGlbPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseDay.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseHour_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh3cDHCPSrvGlbPoolLeaseHour_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseHour_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseHour = _Hh3cDHCPSrvGlbPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 2),
    _Hh3cDHCPSrvGlbPoolLeaseHour_Type()
)
hh3cDHCPSrvGlbPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseHour.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseMinute_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDHCPSrvGlbPoolLeaseMinute_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseMinute_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseMinute = _Hh3cDHCPSrvGlbPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 3),
    _Hh3cDHCPSrvGlbPoolLeaseMinute_Type()
)
hh3cDHCPSrvGlbPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseMinute.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseUnlimited_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseUnlimited based on Integer32"""
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


_Hh3cDHCPSrvGlbPoolLeaseUnlimited_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseUnlimited_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseUnlimited = _Hh3cDHCPSrvGlbPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 4),
    _Hh3cDHCPSrvGlbPoolLeaseUnlimited_Type()
)
hh3cDHCPSrvGlbPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseUnlimited.setStatus("current")


class _Hh3cDHCPSrvGlbPoolDomainName_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSrvGlbPoolDomainName_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolDomainName_Object = MibTableColumn
hh3cDHCPSrvGlbPoolDomainName = _Hh3cDHCPSrvGlbPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 5),
    _Hh3cDHCPSrvGlbPoolDomainName_Type()
)
hh3cDHCPSrvGlbPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolDomainName.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliGWIPStr_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolCliGWIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolCliGWIPStr_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolCliGWIPStr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliGWIPStr = _Hh3cDHCPSrvGlbPoolCliGWIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 6),
    _Hh3cDHCPSrvGlbPoolCliGWIPStr_Type()
)
hh3cDHCPSrvGlbPoolCliGWIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliGWIPStr.setStatus("current")
_Hh3cDHCPSrvGlbPoolCliGWIPUndo_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliGWIPUndo_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliGWIPUndo = _Hh3cDHCPSrvGlbPoolCliGWIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 7),
    _Hh3cDHCPSrvGlbPoolCliGWIPUndo_Type()
)
hh3cDHCPSrvGlbPoolCliGWIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliGWIPUndo.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliDNSIPStr_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolCliDNSIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolCliDNSIPStr_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolCliDNSIPStr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliDNSIPStr = _Hh3cDHCPSrvGlbPoolCliDNSIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 8),
    _Hh3cDHCPSrvGlbPoolCliDNSIPStr_Type()
)
hh3cDHCPSrvGlbPoolCliDNSIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliDNSIPStr.setStatus("current")
_Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliDNSIPUndo = _Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 9),
    _Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Type()
)
hh3cDHCPSrvGlbPoolCliDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliNetbiosType_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolCliNetbiosType based on Integer32"""
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


_Hh3cDHCPSrvGlbPoolCliNetbiosType_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolCliNetbiosType_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliNetbiosType = _Hh3cDHCPSrvGlbPoolCliNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 10),
    _Hh3cDHCPSrvGlbPoolCliNetbiosType_Type()
)
hh3cDHCPSrvGlbPoolCliNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliNetbiosType.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolCliNbnsIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliNbnsIPStr = _Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 11),
    _Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Type()
)
hh3cDHCPSrvGlbPoolCliNbnsIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus("current")
_Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliNbnsIPUndo = _Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 12),
    _Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Type()
)
hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus("current")


class _Hh3cDHCPSrvGlbPoolParaUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolParaUndoFlag based on Integer32"""
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


_Hh3cDHCPSrvGlbPoolParaUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolParaUndoFlag_Object = MibTableColumn
hh3cDHCPSrvGlbPoolParaUndoFlag = _Hh3cDHCPSrvGlbPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 13),
    _Hh3cDHCPSrvGlbPoolParaUndoFlag_Type()
)
hh3cDHCPSrvGlbPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolParaUndoFlag.setStatus("current")


class _Hh3cDHCPSrvGlbPoolIPInUseReset_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDHCPSrvGlbPoolIPInUseReset_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolIPInUseReset_Object = MibTableColumn
hh3cDHCPSrvGlbPoolIPInUseReset = _Hh3cDHCPSrvGlbPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 14),
    _Hh3cDHCPSrvGlbPoolIPInUseReset_Type()
)
hh3cDHCPSrvGlbPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolIPInUseReset.setStatus("current")
_Hh3cDHCPSrvGlbPoolLeaseTime_Type = TimeTicks
_Hh3cDHCPSrvGlbPoolLeaseTime_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseTime = _Hh3cDHCPSrvGlbPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 15),
    _Hh3cDHCPSrvGlbPoolLeaseTime_Type()
)
hh3cDHCPSrvGlbPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseTime.setStatus("current")
_Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Type = IpAddress
_Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Object = MibTableColumn
hh3cDHCPSrvGlbPoolPrimaryDNSIP = _Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 16),
    _Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Type()
)
hh3cDHCPSrvGlbPoolPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus("current")
_Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Type = IpAddress
_Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Object = MibTableColumn
hh3cDHCPSrvGlbPoolSecondaryDNSIP = _Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 17),
    _Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Type()
)
hh3cDHCPSrvGlbPoolSecondaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseSecond_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseSecond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDHCPSrvGlbPoolLeaseSecond_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseSecond_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseSecond = _Hh3cDHCPSrvGlbPoolLeaseSecond_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 18),
    _Hh3cDHCPSrvGlbPoolLeaseSecond_Type()
)
hh3cDHCPSrvGlbPoolLeaseSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseSecond.setStatus("current")
_Hh3cDHCPSrvGlobalPoolOptionTable_Object = MibTable
hh3cDHCPSrvGlobalPoolOptionTable = _Hh3cDHCPSrvGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolOptionTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolOptionEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolOptionEntry = _Hh3cDHCPSrvGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1)
)
hh3cDHCPSrvGlobalPoolOptionEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlbPoolOptCode"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolOptionEntry.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptCode_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cDHCPSrvGlbPoolOptCode_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolOptCode_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptCode = _Hh3cDHCPSrvGlbPoolOptCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 1),
    _Hh3cDHCPSrvGlbPoolOptCode_Type()
)
hh3cDHCPSrvGlbPoolOptCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptCode.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptType_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolOptType based on Integer32"""
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


_Hh3cDHCPSrvGlbPoolOptType_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolOptType_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptType = _Hh3cDHCPSrvGlbPoolOptType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 2),
    _Hh3cDHCPSrvGlbPoolOptType_Type()
)
hh3cDHCPSrvGlbPoolOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptType.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptAscii_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolOptAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDHCPSrvGlbPoolOptAscii_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolOptAscii_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptAscii = _Hh3cDHCPSrvGlbPoolOptAscii_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 3),
    _Hh3cDHCPSrvGlbPoolOptAscii_Type()
)
hh3cDHCPSrvGlbPoolOptAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptAscii.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptHexString_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolOptHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_Hh3cDHCPSrvGlbPoolOptHexString_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolOptHexString_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptHexString = _Hh3cDHCPSrvGlbPoolOptHexString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 4),
    _Hh3cDHCPSrvGlbPoolOptHexString_Type()
)
hh3cDHCPSrvGlbPoolOptHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptHexString.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptIPString_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolOptIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolOptIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolOptIPString_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptIPString = _Hh3cDHCPSrvGlbPoolOptIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 5),
    _Hh3cDHCPSrvGlbPoolOptIPString_Type()
)
hh3cDHCPSrvGlbPoolOptIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptIPString.setStatus("current")
_Hh3cDHCPSrvGlbPoolOptRowStatus_Type = RowStatus
_Hh3cDHCPSrvGlbPoolOptRowStatus_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptRowStatus = _Hh3cDHCPSrvGlbPoolOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 6),
    _Hh3cDHCPSrvGlbPoolOptRowStatus_Type()
)
hh3cDHCPSrvGlbPoolOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptRowStatus.setStatus("current")
_Hh3cDHCPSrvGlobalPoolStatTable_Object = MibTable
hh3cDHCPSrvGlobalPoolStatTable = _Hh3cDHCPSrvGlobalPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolStatTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolStatEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolStatEntry = _Hh3cDHCPSrvGlobalPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1)
)
hh3cDHCPSrvGlobalPoolStatEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolStatEntry.setStatus("current")
_Hh3cDHCPSrvGlbPoolIPPoolUsage_Type = Integer32
_Hh3cDHCPSrvGlbPoolIPPoolUsage_Object = MibTableColumn
hh3cDHCPSrvGlbPoolIPPoolUsage = _Hh3cDHCPSrvGlbPoolIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 1),
    _Hh3cDHCPSrvGlbPoolIPPoolUsage_Type()
)
hh3cDHCPSrvGlbPoolIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolIPPoolUsage.setStatus("current")
_Hh3cDHCPSrvGlbPoolReqTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolReqTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolReqTimes = _Hh3cDHCPSrvGlbPoolReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 2),
    _Hh3cDHCPSrvGlbPoolReqTimes_Type()
)
hh3cDHCPSrvGlbPoolReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolReqTimes.setStatus("current")
_Hh3cDHCPSrvGlbPoolSuccessTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolSuccessTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolSuccessTimes = _Hh3cDHCPSrvGlbPoolSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 3),
    _Hh3cDHCPSrvGlbPoolSuccessTimes_Type()
)
hh3cDHCPSrvGlbPoolSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolSuccessTimes.setStatus("current")
_Hh3cDHCPServerTraps_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTraps = _Hh3cDHCPServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3)
)
_Hh3cDHCPServerTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTrapPrefix = _Hh3cDHCPServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cDHCPServerAddrExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 1)
)
hh3cDHCPServerAddrExhaust.setObjects(
    ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAddrExhaust.setStatus(
        "current"
    )

hh3cDHCPServerAddrExhaustRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 2)
)
hh3cDHCPServerAddrExhaustRecover.setObjects(
    ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAddrExhaustRecover.setStatus(
        "current"
    )

hh3cDHCPServerAvgIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 3)
)
hh3cDHCPServerAvgIpUsageOverflow.setObjects(
    ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAvgIpUsageOverflow.setStatus(
        "current"
    )

hh3cDHCPServerMaxIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 4)
)
hh3cDHCPServerMaxIpUsageOverflow.setObjects(
    ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hh3cDHCPServerMaxIpUsageOverflow.setStatus(
        "current"
    )

hh3cDHCPServerAllocateOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 5)
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAllocateOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCP-SERVER-MIB",
    **{"hh3cDHCPServer": hh3cDHCPServer,
       "hh3cDHCPServerObjects": hh3cDHCPServerObjects,
       "hh3cDHCPServerIPPoolUsage": hh3cDHCPServerIPPoolUsage,
       "hh3cDHCPServerReqTimes": hh3cDHCPServerReqTimes,
       "hh3cDHCPServerReqSuccessTimes": hh3cDHCPServerReqSuccessTimes,
       "hh3cDHCPServerAvgIpUseThreshold": hh3cDHCPServerAvgIpUseThreshold,
       "hh3cDHCPServerMaxIpUseThreshold": hh3cDHCPServerMaxIpUseThreshold,
       "hh3cDHCPServerAllocateThreshold": hh3cDHCPServerAllocateThreshold,
       "hh3cDHCPServerTables": hh3cDHCPServerTables,
       "hh3cDHCPServerPoolName": hh3cDHCPServerPoolName,
       "hh3cDHCPSrvGlobalPoolTable": hh3cDHCPSrvGlobalPoolTable,
       "hh3cDHCPSrvGlobalPoolEntry": hh3cDHCPSrvGlobalPoolEntry,
       "hh3cDHCPSrvGlobalPoolName": hh3cDHCPSrvGlobalPoolName,
       "hh3cDHCPSrvGlobalPoolRowStatus": hh3cDHCPSrvGlobalPoolRowStatus,
       "hh3cDHCPSrvGlobalPoolConfigTable": hh3cDHCPSrvGlobalPoolConfigTable,
       "hh3cDHCPSrvGlobalPoolConfigEntry": hh3cDHCPSrvGlobalPoolConfigEntry,
       "hh3cDHCPSrvGlobalPoolType": hh3cDHCPSrvGlobalPoolType,
       "hh3cDHCPSrvGlobalPoolNetwork": hh3cDHCPSrvGlobalPoolNetwork,
       "hh3cDHCPSrvGlobalPoolNetworkMask": hh3cDHCPSrvGlobalPoolNetworkMask,
       "hh3cDHCPSrvGlobalPoolHostIPAddr": hh3cDHCPSrvGlobalPoolHostIPAddr,
       "hh3cDHCPSrvGlobalPoolHostMask": hh3cDHCPSrvGlobalPoolHostMask,
       "hh3cDHCPSrvGlobalPoolHostHAddr": hh3cDHCPSrvGlobalPoolHostHAddr,
       "hh3cDHCPSrvGlobalPoolCfgUndoFlag": hh3cDHCPSrvGlobalPoolCfgUndoFlag,
       "hh3cDHCPSrvGlobalPoolStartAddr": hh3cDHCPSrvGlobalPoolStartAddr,
       "hh3cDHCPSrvGlobalPoolEndAddr": hh3cDHCPSrvGlobalPoolEndAddr,
       "hh3cDHCPSrvGlobalPoolParaTable": hh3cDHCPSrvGlobalPoolParaTable,
       "hh3cDHCPSrvGlobalPoolParaEntry": hh3cDHCPSrvGlobalPoolParaEntry,
       "hh3cDHCPSrvGlbPoolLeaseDay": hh3cDHCPSrvGlbPoolLeaseDay,
       "hh3cDHCPSrvGlbPoolLeaseHour": hh3cDHCPSrvGlbPoolLeaseHour,
       "hh3cDHCPSrvGlbPoolLeaseMinute": hh3cDHCPSrvGlbPoolLeaseMinute,
       "hh3cDHCPSrvGlbPoolLeaseUnlimited": hh3cDHCPSrvGlbPoolLeaseUnlimited,
       "hh3cDHCPSrvGlbPoolDomainName": hh3cDHCPSrvGlbPoolDomainName,
       "hh3cDHCPSrvGlbPoolCliGWIPStr": hh3cDHCPSrvGlbPoolCliGWIPStr,
       "hh3cDHCPSrvGlbPoolCliGWIPUndo": hh3cDHCPSrvGlbPoolCliGWIPUndo,
       "hh3cDHCPSrvGlbPoolCliDNSIPStr": hh3cDHCPSrvGlbPoolCliDNSIPStr,
       "hh3cDHCPSrvGlbPoolCliDNSIPUndo": hh3cDHCPSrvGlbPoolCliDNSIPUndo,
       "hh3cDHCPSrvGlbPoolCliNetbiosType": hh3cDHCPSrvGlbPoolCliNetbiosType,
       "hh3cDHCPSrvGlbPoolCliNbnsIPStr": hh3cDHCPSrvGlbPoolCliNbnsIPStr,
       "hh3cDHCPSrvGlbPoolCliNbnsIPUndo": hh3cDHCPSrvGlbPoolCliNbnsIPUndo,
       "hh3cDHCPSrvGlbPoolParaUndoFlag": hh3cDHCPSrvGlbPoolParaUndoFlag,
       "hh3cDHCPSrvGlbPoolIPInUseReset": hh3cDHCPSrvGlbPoolIPInUseReset,
       "hh3cDHCPSrvGlbPoolLeaseTime": hh3cDHCPSrvGlbPoolLeaseTime,
       "hh3cDHCPSrvGlbPoolPrimaryDNSIP": hh3cDHCPSrvGlbPoolPrimaryDNSIP,
       "hh3cDHCPSrvGlbPoolSecondaryDNSIP": hh3cDHCPSrvGlbPoolSecondaryDNSIP,
       "hh3cDHCPSrvGlbPoolLeaseSecond": hh3cDHCPSrvGlbPoolLeaseSecond,
       "hh3cDHCPSrvGlobalPoolOptionTable": hh3cDHCPSrvGlobalPoolOptionTable,
       "hh3cDHCPSrvGlobalPoolOptionEntry": hh3cDHCPSrvGlobalPoolOptionEntry,
       "hh3cDHCPSrvGlbPoolOptCode": hh3cDHCPSrvGlbPoolOptCode,
       "hh3cDHCPSrvGlbPoolOptType": hh3cDHCPSrvGlbPoolOptType,
       "hh3cDHCPSrvGlbPoolOptAscii": hh3cDHCPSrvGlbPoolOptAscii,
       "hh3cDHCPSrvGlbPoolOptHexString": hh3cDHCPSrvGlbPoolOptHexString,
       "hh3cDHCPSrvGlbPoolOptIPString": hh3cDHCPSrvGlbPoolOptIPString,
       "hh3cDHCPSrvGlbPoolOptRowStatus": hh3cDHCPSrvGlbPoolOptRowStatus,
       "hh3cDHCPSrvGlobalPoolStatTable": hh3cDHCPSrvGlobalPoolStatTable,
       "hh3cDHCPSrvGlobalPoolStatEntry": hh3cDHCPSrvGlobalPoolStatEntry,
       "hh3cDHCPSrvGlbPoolIPPoolUsage": hh3cDHCPSrvGlbPoolIPPoolUsage,
       "hh3cDHCPSrvGlbPoolReqTimes": hh3cDHCPSrvGlbPoolReqTimes,
       "hh3cDHCPSrvGlbPoolSuccessTimes": hh3cDHCPSrvGlbPoolSuccessTimes,
       "hh3cDHCPServerTraps": hh3cDHCPServerTraps,
       "hh3cDHCPServerTrapPrefix": hh3cDHCPServerTrapPrefix,
       "hh3cDHCPServerAddrExhaust": hh3cDHCPServerAddrExhaust,
       "hh3cDHCPServerAddrExhaustRecover": hh3cDHCPServerAddrExhaustRecover,
       "hh3cDHCPServerAvgIpUsageOverflow": hh3cDHCPServerAvgIpUsageOverflow,
       "hh3cDHCPServerMaxIpUsageOverflow": hh3cDHCPServerMaxIpUsageOverflow,
       "hh3cDHCPServerAllocateOverflow": hh3cDHCPServerAllocateOverflow}
)
