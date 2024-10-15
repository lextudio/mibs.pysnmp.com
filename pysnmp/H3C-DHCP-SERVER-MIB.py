# SNMP MIB module (H3C-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:01 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cDHCPServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101)
)
h3cDHCPServer.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDHCPServerObjects_ObjectIdentity = ObjectIdentity
h3cDHCPServerObjects = _H3cDHCPServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1)
)
_H3cDHCPServerIPPoolUsage_Type = Integer32
_H3cDHCPServerIPPoolUsage_Object = MibScalar
h3cDHCPServerIPPoolUsage = _H3cDHCPServerIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 1),
    _H3cDHCPServerIPPoolUsage_Type()
)
h3cDHCPServerIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPServerIPPoolUsage.setStatus("current")
_H3cDHCPServerReqTimes_Type = Counter32
_H3cDHCPServerReqTimes_Object = MibScalar
h3cDHCPServerReqTimes = _H3cDHCPServerReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 2),
    _H3cDHCPServerReqTimes_Type()
)
h3cDHCPServerReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPServerReqTimes.setStatus("current")
_H3cDHCPServerReqSuccessTimes_Type = Counter32
_H3cDHCPServerReqSuccessTimes_Object = MibScalar
h3cDHCPServerReqSuccessTimes = _H3cDHCPServerReqSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 3),
    _H3cDHCPServerReqSuccessTimes_Type()
)
h3cDHCPServerReqSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPServerReqSuccessTimes.setStatus("current")


class _H3cDHCPServerAvgIpUseThreshold_Type(Integer32):
    """Custom type h3cDHCPServerAvgIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDHCPServerAvgIpUseThreshold_Type.__name__ = "Integer32"
_H3cDHCPServerAvgIpUseThreshold_Object = MibScalar
h3cDHCPServerAvgIpUseThreshold = _H3cDHCPServerAvgIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 4),
    _H3cDHCPServerAvgIpUseThreshold_Type()
)
h3cDHCPServerAvgIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPServerAvgIpUseThreshold.setStatus("current")


class _H3cDHCPServerMaxIpUseThreshold_Type(Integer32):
    """Custom type h3cDHCPServerMaxIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDHCPServerMaxIpUseThreshold_Type.__name__ = "Integer32"
_H3cDHCPServerMaxIpUseThreshold_Object = MibScalar
h3cDHCPServerMaxIpUseThreshold = _H3cDHCPServerMaxIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 5),
    _H3cDHCPServerMaxIpUseThreshold_Type()
)
h3cDHCPServerMaxIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPServerMaxIpUseThreshold.setStatus("current")


class _H3cDHCPServerAllocateThreshold_Type(Integer32):
    """Custom type h3cDHCPServerAllocateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDHCPServerAllocateThreshold_Type.__name__ = "Integer32"
_H3cDHCPServerAllocateThreshold_Object = MibScalar
h3cDHCPServerAllocateThreshold = _H3cDHCPServerAllocateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 6),
    _H3cDHCPServerAllocateThreshold_Type()
)
h3cDHCPServerAllocateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPServerAllocateThreshold.setStatus("current")
_H3cDHCPServerTables_ObjectIdentity = ObjectIdentity
h3cDHCPServerTables = _H3cDHCPServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2)
)


class _H3cDHCPServerPoolName_Type(OctetString):
    """Custom type h3cDHCPServerPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDHCPServerPoolName_Type.__name__ = "OctetString"
_H3cDHCPServerPoolName_Object = MibScalar
h3cDHCPServerPoolName = _H3cDHCPServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 1),
    _H3cDHCPServerPoolName_Type()
)
h3cDHCPServerPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDHCPServerPoolName.setStatus("current")
_H3cDHCPSrvGlobalPoolTable_Object = MibTable
h3cDHCPSrvGlobalPoolTable = _H3cDHCPSrvGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolTable.setStatus("current")
_H3cDHCPSrvGlobalPoolEntry_Object = MibTableRow
h3cDHCPSrvGlobalPoolEntry = _H3cDHCPSrvGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2, 1)
)
h3cDHCPSrvGlobalPoolEntry.setIndexNames(
    (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolEntry.setStatus("current")


class _H3cDHCPSrvGlobalPoolName_Type(OctetString):
    """Custom type h3cDHCPSrvGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDHCPSrvGlobalPoolName_Type.__name__ = "OctetString"
_H3cDHCPSrvGlobalPoolName_Object = MibTableColumn
h3cDHCPSrvGlobalPoolName = _H3cDHCPSrvGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2, 1, 1),
    _H3cDHCPSrvGlobalPoolName_Type()
)
h3cDHCPSrvGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolName.setStatus("current")
_H3cDHCPSrvGlobalPoolRowStatus_Type = RowStatus
_H3cDHCPSrvGlobalPoolRowStatus_Object = MibTableColumn
h3cDHCPSrvGlobalPoolRowStatus = _H3cDHCPSrvGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2, 1, 2),
    _H3cDHCPSrvGlobalPoolRowStatus_Type()
)
h3cDHCPSrvGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolRowStatus.setStatus("current")
_H3cDHCPSrvGlobalPoolConfigTable_Object = MibTable
h3cDHCPSrvGlobalPoolConfigTable = _H3cDHCPSrvGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolConfigTable.setStatus("current")
_H3cDHCPSrvGlobalPoolConfigEntry_Object = MibTableRow
h3cDHCPSrvGlobalPoolConfigEntry = _H3cDHCPSrvGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1)
)
h3cDHCPSrvGlobalPoolConfigEntry.setIndexNames(
    (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolConfigEntry.setStatus("current")


class _H3cDHCPSrvGlobalPoolType_Type(Integer32):
    """Custom type h3cDHCPSrvGlobalPoolType based on Integer32"""
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


_H3cDHCPSrvGlobalPoolType_Type.__name__ = "Integer32"
_H3cDHCPSrvGlobalPoolType_Object = MibTableColumn
h3cDHCPSrvGlobalPoolType = _H3cDHCPSrvGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 1),
    _H3cDHCPSrvGlobalPoolType_Type()
)
h3cDHCPSrvGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolType.setStatus("current")
_H3cDHCPSrvGlobalPoolNetwork_Type = IpAddress
_H3cDHCPSrvGlobalPoolNetwork_Object = MibTableColumn
h3cDHCPSrvGlobalPoolNetwork = _H3cDHCPSrvGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 2),
    _H3cDHCPSrvGlobalPoolNetwork_Type()
)
h3cDHCPSrvGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolNetwork.setStatus("current")
_H3cDHCPSrvGlobalPoolNetworkMask_Type = IpAddress
_H3cDHCPSrvGlobalPoolNetworkMask_Object = MibTableColumn
h3cDHCPSrvGlobalPoolNetworkMask = _H3cDHCPSrvGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 3),
    _H3cDHCPSrvGlobalPoolNetworkMask_Type()
)
h3cDHCPSrvGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolNetworkMask.setStatus("current")
_H3cDHCPSrvGlobalPoolHostIPAddr_Type = IpAddress
_H3cDHCPSrvGlobalPoolHostIPAddr_Object = MibTableColumn
h3cDHCPSrvGlobalPoolHostIPAddr = _H3cDHCPSrvGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 4),
    _H3cDHCPSrvGlobalPoolHostIPAddr_Type()
)
h3cDHCPSrvGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolHostIPAddr.setStatus("current")
_H3cDHCPSrvGlobalPoolHostMask_Type = IpAddress
_H3cDHCPSrvGlobalPoolHostMask_Object = MibTableColumn
h3cDHCPSrvGlobalPoolHostMask = _H3cDHCPSrvGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 5),
    _H3cDHCPSrvGlobalPoolHostMask_Type()
)
h3cDHCPSrvGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolHostMask.setStatus("current")
_H3cDHCPSrvGlobalPoolHostHAddr_Type = MacAddress
_H3cDHCPSrvGlobalPoolHostHAddr_Object = MibTableColumn
h3cDHCPSrvGlobalPoolHostHAddr = _H3cDHCPSrvGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 6),
    _H3cDHCPSrvGlobalPoolHostHAddr_Type()
)
h3cDHCPSrvGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolHostHAddr.setStatus("current")


class _H3cDHCPSrvGlobalPoolCfgUndoFlag_Type(Integer32):
    """Custom type h3cDHCPSrvGlobalPoolCfgUndoFlag based on Integer32"""
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


_H3cDHCPSrvGlobalPoolCfgUndoFlag_Type.__name__ = "Integer32"
_H3cDHCPSrvGlobalPoolCfgUndoFlag_Object = MibTableColumn
h3cDHCPSrvGlobalPoolCfgUndoFlag = _H3cDHCPSrvGlobalPoolCfgUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 7),
    _H3cDHCPSrvGlobalPoolCfgUndoFlag_Type()
)
h3cDHCPSrvGlobalPoolCfgUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus("current")
_H3cDHCPSrvGlobalPoolStartAddr_Type = IpAddress
_H3cDHCPSrvGlobalPoolStartAddr_Object = MibTableColumn
h3cDHCPSrvGlobalPoolStartAddr = _H3cDHCPSrvGlobalPoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 8),
    _H3cDHCPSrvGlobalPoolStartAddr_Type()
)
h3cDHCPSrvGlobalPoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolStartAddr.setStatus("current")
_H3cDHCPSrvGlobalPoolEndAddr_Type = IpAddress
_H3cDHCPSrvGlobalPoolEndAddr_Object = MibTableColumn
h3cDHCPSrvGlobalPoolEndAddr = _H3cDHCPSrvGlobalPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 9),
    _H3cDHCPSrvGlobalPoolEndAddr_Type()
)
h3cDHCPSrvGlobalPoolEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolEndAddr.setStatus("current")
_H3cDHCPSrvGlobalPoolParaTable_Object = MibTable
h3cDHCPSrvGlobalPoolParaTable = _H3cDHCPSrvGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4)
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolParaTable.setStatus("current")
_H3cDHCPSrvGlobalPoolParaEntry_Object = MibTableRow
h3cDHCPSrvGlobalPoolParaEntry = _H3cDHCPSrvGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1)
)
h3cDHCPSrvGlobalPoolParaEntry.setIndexNames(
    (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolParaEntry.setStatus("current")


class _H3cDHCPSrvGlbPoolLeaseDay_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_H3cDHCPSrvGlbPoolLeaseDay_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolLeaseDay_Object = MibTableColumn
h3cDHCPSrvGlbPoolLeaseDay = _H3cDHCPSrvGlbPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 1),
    _H3cDHCPSrvGlbPoolLeaseDay_Type()
)
h3cDHCPSrvGlbPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolLeaseDay.setStatus("current")


class _H3cDHCPSrvGlbPoolLeaseHour_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_H3cDHCPSrvGlbPoolLeaseHour_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolLeaseHour_Object = MibTableColumn
h3cDHCPSrvGlbPoolLeaseHour = _H3cDHCPSrvGlbPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 2),
    _H3cDHCPSrvGlbPoolLeaseHour_Type()
)
h3cDHCPSrvGlbPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolLeaseHour.setStatus("current")


class _H3cDHCPSrvGlbPoolLeaseMinute_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_H3cDHCPSrvGlbPoolLeaseMinute_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolLeaseMinute_Object = MibTableColumn
h3cDHCPSrvGlbPoolLeaseMinute = _H3cDHCPSrvGlbPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 3),
    _H3cDHCPSrvGlbPoolLeaseMinute_Type()
)
h3cDHCPSrvGlbPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolLeaseMinute.setStatus("current")


class _H3cDHCPSrvGlbPoolLeaseUnlimited_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolLeaseUnlimited based on Integer32"""
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


_H3cDHCPSrvGlbPoolLeaseUnlimited_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolLeaseUnlimited_Object = MibTableColumn
h3cDHCPSrvGlbPoolLeaseUnlimited = _H3cDHCPSrvGlbPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 4),
    _H3cDHCPSrvGlbPoolLeaseUnlimited_Type()
)
h3cDHCPSrvGlbPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolLeaseUnlimited.setStatus("current")


class _H3cDHCPSrvGlbPoolDomainName_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDHCPSrvGlbPoolDomainName_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolDomainName_Object = MibTableColumn
h3cDHCPSrvGlbPoolDomainName = _H3cDHCPSrvGlbPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 5),
    _H3cDHCPSrvGlbPoolDomainName_Type()
)
h3cDHCPSrvGlbPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolDomainName.setStatus("current")


class _H3cDHCPSrvGlbPoolCliGWIPStr_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolCliGWIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_H3cDHCPSrvGlbPoolCliGWIPStr_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolCliGWIPStr_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliGWIPStr = _H3cDHCPSrvGlbPoolCliGWIPStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 6),
    _H3cDHCPSrvGlbPoolCliGWIPStr_Type()
)
h3cDHCPSrvGlbPoolCliGWIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliGWIPStr.setStatus("current")
_H3cDHCPSrvGlbPoolCliGWIPUndo_Type = IpAddress
_H3cDHCPSrvGlbPoolCliGWIPUndo_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliGWIPUndo = _H3cDHCPSrvGlbPoolCliGWIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 7),
    _H3cDHCPSrvGlbPoolCliGWIPUndo_Type()
)
h3cDHCPSrvGlbPoolCliGWIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliGWIPUndo.setStatus("current")


class _H3cDHCPSrvGlbPoolCliDNSIPStr_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolCliDNSIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_H3cDHCPSrvGlbPoolCliDNSIPStr_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolCliDNSIPStr_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliDNSIPStr = _H3cDHCPSrvGlbPoolCliDNSIPStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 8),
    _H3cDHCPSrvGlbPoolCliDNSIPStr_Type()
)
h3cDHCPSrvGlbPoolCliDNSIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliDNSIPStr.setStatus("current")
_H3cDHCPSrvGlbPoolCliDNSIPUndo_Type = IpAddress
_H3cDHCPSrvGlbPoolCliDNSIPUndo_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliDNSIPUndo = _H3cDHCPSrvGlbPoolCliDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 9),
    _H3cDHCPSrvGlbPoolCliDNSIPUndo_Type()
)
h3cDHCPSrvGlbPoolCliDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus("current")


class _H3cDHCPSrvGlbPoolCliNetbiosType_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolCliNetbiosType based on Integer32"""
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


_H3cDHCPSrvGlbPoolCliNetbiosType_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolCliNetbiosType_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliNetbiosType = _H3cDHCPSrvGlbPoolCliNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 10),
    _H3cDHCPSrvGlbPoolCliNetbiosType_Type()
)
h3cDHCPSrvGlbPoolCliNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliNetbiosType.setStatus("current")


class _H3cDHCPSrvGlbPoolCliNbnsIPStr_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolCliNbnsIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_H3cDHCPSrvGlbPoolCliNbnsIPStr_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolCliNbnsIPStr_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliNbnsIPStr = _H3cDHCPSrvGlbPoolCliNbnsIPStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 11),
    _H3cDHCPSrvGlbPoolCliNbnsIPStr_Type()
)
h3cDHCPSrvGlbPoolCliNbnsIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus("current")
_H3cDHCPSrvGlbPoolCliNbnsIPUndo_Type = IpAddress
_H3cDHCPSrvGlbPoolCliNbnsIPUndo_Object = MibTableColumn
h3cDHCPSrvGlbPoolCliNbnsIPUndo = _H3cDHCPSrvGlbPoolCliNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 12),
    _H3cDHCPSrvGlbPoolCliNbnsIPUndo_Type()
)
h3cDHCPSrvGlbPoolCliNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus("current")


class _H3cDHCPSrvGlbPoolParaUndoFlag_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolParaUndoFlag based on Integer32"""
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


_H3cDHCPSrvGlbPoolParaUndoFlag_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolParaUndoFlag_Object = MibTableColumn
h3cDHCPSrvGlbPoolParaUndoFlag = _H3cDHCPSrvGlbPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 13),
    _H3cDHCPSrvGlbPoolParaUndoFlag_Type()
)
h3cDHCPSrvGlbPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolParaUndoFlag.setStatus("current")


class _H3cDHCPSrvGlbPoolIPInUseReset_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_H3cDHCPSrvGlbPoolIPInUseReset_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolIPInUseReset_Object = MibTableColumn
h3cDHCPSrvGlbPoolIPInUseReset = _H3cDHCPSrvGlbPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 14),
    _H3cDHCPSrvGlbPoolIPInUseReset_Type()
)
h3cDHCPSrvGlbPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolIPInUseReset.setStatus("current")
_H3cDHCPSrvGlbPoolLeaseTime_Type = TimeTicks
_H3cDHCPSrvGlbPoolLeaseTime_Object = MibTableColumn
h3cDHCPSrvGlbPoolLeaseTime = _H3cDHCPSrvGlbPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 15),
    _H3cDHCPSrvGlbPoolLeaseTime_Type()
)
h3cDHCPSrvGlbPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolLeaseTime.setStatus("current")
_H3cDHCPSrvGlbPoolPrimaryDNSIP_Type = IpAddress
_H3cDHCPSrvGlbPoolPrimaryDNSIP_Object = MibTableColumn
h3cDHCPSrvGlbPoolPrimaryDNSIP = _H3cDHCPSrvGlbPoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 16),
    _H3cDHCPSrvGlbPoolPrimaryDNSIP_Type()
)
h3cDHCPSrvGlbPoolPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus("current")
_H3cDHCPSrvGlbPoolSecondaryDNSIP_Type = IpAddress
_H3cDHCPSrvGlbPoolSecondaryDNSIP_Object = MibTableColumn
h3cDHCPSrvGlbPoolSecondaryDNSIP = _H3cDHCPSrvGlbPoolSecondaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 17),
    _H3cDHCPSrvGlbPoolSecondaryDNSIP_Type()
)
h3cDHCPSrvGlbPoolSecondaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus("current")


class _H3cDHCPSrvGlbPoolLeaseSecond_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolLeaseSecond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_H3cDHCPSrvGlbPoolLeaseSecond_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolLeaseSecond_Object = MibTableColumn
h3cDHCPSrvGlbPoolLeaseSecond = _H3cDHCPSrvGlbPoolLeaseSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 18),
    _H3cDHCPSrvGlbPoolLeaseSecond_Type()
)
h3cDHCPSrvGlbPoolLeaseSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolLeaseSecond.setStatus("current")
_H3cDHCPSrvGlobalPoolOptionTable_Object = MibTable
h3cDHCPSrvGlobalPoolOptionTable = _H3cDHCPSrvGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5)
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolOptionTable.setStatus("current")
_H3cDHCPSrvGlobalPoolOptionEntry_Object = MibTableRow
h3cDHCPSrvGlobalPoolOptionEntry = _H3cDHCPSrvGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1)
)
h3cDHCPSrvGlobalPoolOptionEntry.setIndexNames(
    (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"),
    (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlbPoolOptCode"),
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolOptionEntry.setStatus("current")


class _H3cDHCPSrvGlbPoolOptCode_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_H3cDHCPSrvGlbPoolOptCode_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolOptCode_Object = MibTableColumn
h3cDHCPSrvGlbPoolOptCode = _H3cDHCPSrvGlbPoolOptCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 1),
    _H3cDHCPSrvGlbPoolOptCode_Type()
)
h3cDHCPSrvGlbPoolOptCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolOptCode.setStatus("current")


class _H3cDHCPSrvGlbPoolOptType_Type(Integer32):
    """Custom type h3cDHCPSrvGlbPoolOptType based on Integer32"""
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


_H3cDHCPSrvGlbPoolOptType_Type.__name__ = "Integer32"
_H3cDHCPSrvGlbPoolOptType_Object = MibTableColumn
h3cDHCPSrvGlbPoolOptType = _H3cDHCPSrvGlbPoolOptType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 2),
    _H3cDHCPSrvGlbPoolOptType_Type()
)
h3cDHCPSrvGlbPoolOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolOptType.setStatus("current")


class _H3cDHCPSrvGlbPoolOptAscii_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolOptAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cDHCPSrvGlbPoolOptAscii_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolOptAscii_Object = MibTableColumn
h3cDHCPSrvGlbPoolOptAscii = _H3cDHCPSrvGlbPoolOptAscii_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 3),
    _H3cDHCPSrvGlbPoolOptAscii_Type()
)
h3cDHCPSrvGlbPoolOptAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolOptAscii.setStatus("current")


class _H3cDHCPSrvGlbPoolOptHexString_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolOptHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_H3cDHCPSrvGlbPoolOptHexString_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolOptHexString_Object = MibTableColumn
h3cDHCPSrvGlbPoolOptHexString = _H3cDHCPSrvGlbPoolOptHexString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 4),
    _H3cDHCPSrvGlbPoolOptHexString_Type()
)
h3cDHCPSrvGlbPoolOptHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolOptHexString.setStatus("current")


class _H3cDHCPSrvGlbPoolOptIPString_Type(OctetString):
    """Custom type h3cDHCPSrvGlbPoolOptIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_H3cDHCPSrvGlbPoolOptIPString_Type.__name__ = "OctetString"
_H3cDHCPSrvGlbPoolOptIPString_Object = MibTableColumn
h3cDHCPSrvGlbPoolOptIPString = _H3cDHCPSrvGlbPoolOptIPString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 5),
    _H3cDHCPSrvGlbPoolOptIPString_Type()
)
h3cDHCPSrvGlbPoolOptIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolOptIPString.setStatus("current")
_H3cDHCPSrvGlbPoolOptRowStatus_Type = RowStatus
_H3cDHCPSrvGlbPoolOptRowStatus_Object = MibTableColumn
h3cDHCPSrvGlbPoolOptRowStatus = _H3cDHCPSrvGlbPoolOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 6),
    _H3cDHCPSrvGlbPoolOptRowStatus_Type()
)
h3cDHCPSrvGlbPoolOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolOptRowStatus.setStatus("current")
_H3cDHCPSrvGlobalPoolStatTable_Object = MibTable
h3cDHCPSrvGlobalPoolStatTable = _H3cDHCPSrvGlobalPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6)
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolStatTable.setStatus("current")
_H3cDHCPSrvGlobalPoolStatEntry_Object = MibTableRow
h3cDHCPSrvGlobalPoolStatEntry = _H3cDHCPSrvGlobalPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1)
)
h3cDHCPSrvGlobalPoolStatEntry.setIndexNames(
    (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    h3cDHCPSrvGlobalPoolStatEntry.setStatus("current")
_H3cDHCPSrvGlbPoolIPPoolUsage_Type = Integer32
_H3cDHCPSrvGlbPoolIPPoolUsage_Object = MibTableColumn
h3cDHCPSrvGlbPoolIPPoolUsage = _H3cDHCPSrvGlbPoolIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1, 1),
    _H3cDHCPSrvGlbPoolIPPoolUsage_Type()
)
h3cDHCPSrvGlbPoolIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolIPPoolUsage.setStatus("current")
_H3cDHCPSrvGlbPoolReqTimes_Type = Counter32
_H3cDHCPSrvGlbPoolReqTimes_Object = MibTableColumn
h3cDHCPSrvGlbPoolReqTimes = _H3cDHCPSrvGlbPoolReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1, 2),
    _H3cDHCPSrvGlbPoolReqTimes_Type()
)
h3cDHCPSrvGlbPoolReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolReqTimes.setStatus("current")
_H3cDHCPSrvGlbPoolSuccessTimes_Type = Counter32
_H3cDHCPSrvGlbPoolSuccessTimes_Object = MibTableColumn
h3cDHCPSrvGlbPoolSuccessTimes = _H3cDHCPSrvGlbPoolSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1, 3),
    _H3cDHCPSrvGlbPoolSuccessTimes_Type()
)
h3cDHCPSrvGlbPoolSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPSrvGlbPoolSuccessTimes.setStatus("current")
_H3cDHCPServerTraps_ObjectIdentity = ObjectIdentity
h3cDHCPServerTraps = _H3cDHCPServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3)
)
_H3cDHCPServerTrapPrefix_ObjectIdentity = ObjectIdentity
h3cDHCPServerTrapPrefix = _H3cDHCPServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cDHCPServerAddrExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 1)
)
h3cDHCPServerAddrExhaust.setObjects(
    ("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    h3cDHCPServerAddrExhaust.setStatus(
        "current"
    )

h3cDHCPServerAddrExhaustRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 2)
)
h3cDHCPServerAddrExhaustRecover.setObjects(
    ("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    h3cDHCPServerAddrExhaustRecover.setStatus(
        "current"
    )

h3cDHCPServerAvgIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 3)
)
h3cDHCPServerAvgIpUsageOverflow.setObjects(
    ("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    h3cDHCPServerAvgIpUsageOverflow.setStatus(
        "current"
    )

h3cDHCPServerMaxIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 4)
)
h3cDHCPServerMaxIpUsageOverflow.setObjects(
    ("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    h3cDHCPServerMaxIpUsageOverflow.setStatus(
        "current"
    )

h3cDHCPServerAllocateOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 5)
)
if mibBuilder.loadTexts:
    h3cDHCPServerAllocateOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DHCP-SERVER-MIB",
    **{"h3cDHCPServer": h3cDHCPServer,
       "h3cDHCPServerObjects": h3cDHCPServerObjects,
       "h3cDHCPServerIPPoolUsage": h3cDHCPServerIPPoolUsage,
       "h3cDHCPServerReqTimes": h3cDHCPServerReqTimes,
       "h3cDHCPServerReqSuccessTimes": h3cDHCPServerReqSuccessTimes,
       "h3cDHCPServerAvgIpUseThreshold": h3cDHCPServerAvgIpUseThreshold,
       "h3cDHCPServerMaxIpUseThreshold": h3cDHCPServerMaxIpUseThreshold,
       "h3cDHCPServerAllocateThreshold": h3cDHCPServerAllocateThreshold,
       "h3cDHCPServerTables": h3cDHCPServerTables,
       "h3cDHCPServerPoolName": h3cDHCPServerPoolName,
       "h3cDHCPSrvGlobalPoolTable": h3cDHCPSrvGlobalPoolTable,
       "h3cDHCPSrvGlobalPoolEntry": h3cDHCPSrvGlobalPoolEntry,
       "h3cDHCPSrvGlobalPoolName": h3cDHCPSrvGlobalPoolName,
       "h3cDHCPSrvGlobalPoolRowStatus": h3cDHCPSrvGlobalPoolRowStatus,
       "h3cDHCPSrvGlobalPoolConfigTable": h3cDHCPSrvGlobalPoolConfigTable,
       "h3cDHCPSrvGlobalPoolConfigEntry": h3cDHCPSrvGlobalPoolConfigEntry,
       "h3cDHCPSrvGlobalPoolType": h3cDHCPSrvGlobalPoolType,
       "h3cDHCPSrvGlobalPoolNetwork": h3cDHCPSrvGlobalPoolNetwork,
       "h3cDHCPSrvGlobalPoolNetworkMask": h3cDHCPSrvGlobalPoolNetworkMask,
       "h3cDHCPSrvGlobalPoolHostIPAddr": h3cDHCPSrvGlobalPoolHostIPAddr,
       "h3cDHCPSrvGlobalPoolHostMask": h3cDHCPSrvGlobalPoolHostMask,
       "h3cDHCPSrvGlobalPoolHostHAddr": h3cDHCPSrvGlobalPoolHostHAddr,
       "h3cDHCPSrvGlobalPoolCfgUndoFlag": h3cDHCPSrvGlobalPoolCfgUndoFlag,
       "h3cDHCPSrvGlobalPoolStartAddr": h3cDHCPSrvGlobalPoolStartAddr,
       "h3cDHCPSrvGlobalPoolEndAddr": h3cDHCPSrvGlobalPoolEndAddr,
       "h3cDHCPSrvGlobalPoolParaTable": h3cDHCPSrvGlobalPoolParaTable,
       "h3cDHCPSrvGlobalPoolParaEntry": h3cDHCPSrvGlobalPoolParaEntry,
       "h3cDHCPSrvGlbPoolLeaseDay": h3cDHCPSrvGlbPoolLeaseDay,
       "h3cDHCPSrvGlbPoolLeaseHour": h3cDHCPSrvGlbPoolLeaseHour,
       "h3cDHCPSrvGlbPoolLeaseMinute": h3cDHCPSrvGlbPoolLeaseMinute,
       "h3cDHCPSrvGlbPoolLeaseUnlimited": h3cDHCPSrvGlbPoolLeaseUnlimited,
       "h3cDHCPSrvGlbPoolDomainName": h3cDHCPSrvGlbPoolDomainName,
       "h3cDHCPSrvGlbPoolCliGWIPStr": h3cDHCPSrvGlbPoolCliGWIPStr,
       "h3cDHCPSrvGlbPoolCliGWIPUndo": h3cDHCPSrvGlbPoolCliGWIPUndo,
       "h3cDHCPSrvGlbPoolCliDNSIPStr": h3cDHCPSrvGlbPoolCliDNSIPStr,
       "h3cDHCPSrvGlbPoolCliDNSIPUndo": h3cDHCPSrvGlbPoolCliDNSIPUndo,
       "h3cDHCPSrvGlbPoolCliNetbiosType": h3cDHCPSrvGlbPoolCliNetbiosType,
       "h3cDHCPSrvGlbPoolCliNbnsIPStr": h3cDHCPSrvGlbPoolCliNbnsIPStr,
       "h3cDHCPSrvGlbPoolCliNbnsIPUndo": h3cDHCPSrvGlbPoolCliNbnsIPUndo,
       "h3cDHCPSrvGlbPoolParaUndoFlag": h3cDHCPSrvGlbPoolParaUndoFlag,
       "h3cDHCPSrvGlbPoolIPInUseReset": h3cDHCPSrvGlbPoolIPInUseReset,
       "h3cDHCPSrvGlbPoolLeaseTime": h3cDHCPSrvGlbPoolLeaseTime,
       "h3cDHCPSrvGlbPoolPrimaryDNSIP": h3cDHCPSrvGlbPoolPrimaryDNSIP,
       "h3cDHCPSrvGlbPoolSecondaryDNSIP": h3cDHCPSrvGlbPoolSecondaryDNSIP,
       "h3cDHCPSrvGlbPoolLeaseSecond": h3cDHCPSrvGlbPoolLeaseSecond,
       "h3cDHCPSrvGlobalPoolOptionTable": h3cDHCPSrvGlobalPoolOptionTable,
       "h3cDHCPSrvGlobalPoolOptionEntry": h3cDHCPSrvGlobalPoolOptionEntry,
       "h3cDHCPSrvGlbPoolOptCode": h3cDHCPSrvGlbPoolOptCode,
       "h3cDHCPSrvGlbPoolOptType": h3cDHCPSrvGlbPoolOptType,
       "h3cDHCPSrvGlbPoolOptAscii": h3cDHCPSrvGlbPoolOptAscii,
       "h3cDHCPSrvGlbPoolOptHexString": h3cDHCPSrvGlbPoolOptHexString,
       "h3cDHCPSrvGlbPoolOptIPString": h3cDHCPSrvGlbPoolOptIPString,
       "h3cDHCPSrvGlbPoolOptRowStatus": h3cDHCPSrvGlbPoolOptRowStatus,
       "h3cDHCPSrvGlobalPoolStatTable": h3cDHCPSrvGlobalPoolStatTable,
       "h3cDHCPSrvGlobalPoolStatEntry": h3cDHCPSrvGlobalPoolStatEntry,
       "h3cDHCPSrvGlbPoolIPPoolUsage": h3cDHCPSrvGlbPoolIPPoolUsage,
       "h3cDHCPSrvGlbPoolReqTimes": h3cDHCPSrvGlbPoolReqTimes,
       "h3cDHCPSrvGlbPoolSuccessTimes": h3cDHCPSrvGlbPoolSuccessTimes,
       "h3cDHCPServerTraps": h3cDHCPServerTraps,
       "h3cDHCPServerTrapPrefix": h3cDHCPServerTrapPrefix,
       "h3cDHCPServerAddrExhaust": h3cDHCPServerAddrExhaust,
       "h3cDHCPServerAddrExhaustRecover": h3cDHCPServerAddrExhaustRecover,
       "h3cDHCPServerAvgIpUsageOverflow": h3cDHCPServerAvgIpUsageOverflow,
       "h3cDHCPServerMaxIpUsageOverflow": h3cDHCPServerMaxIpUsageOverflow,
       "h3cDHCPServerAllocateOverflow": h3cDHCPServerAllocateOverflow}
)
