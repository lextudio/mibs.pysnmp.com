# SNMP MIB module (CISCO-CACHE-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CACHE-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:44 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCacheEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCacheEngineMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCacheEngineMIBObjects = _CiscoCacheEngineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1)
)
_CiscoCacheEngineConf_ObjectIdentity = ObjectIdentity
ciscoCacheEngineConf = _CiscoCacheEngineConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1)
)
_CceConfigGroup_ObjectIdentity = ObjectIdentity
cceConfigGroup = _CceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1)
)
_CceFarm_ObjectIdentity = ObjectIdentity
cceFarm = _CceFarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 1)
)
_CceFarmTable_Object = MibTable
cceFarmTable = _CceFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cceFarmTable.setStatus("current")
_CceFarmEntry_Object = MibTableRow
cceFarmEntry = _CceFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 1, 1, 1)
)
cceFarmEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceFarmEntryIndex"),
)
if mibBuilder.loadTexts:
    cceFarmEntry.setStatus("current")


class _CceFarmEntryIndex_Type(Integer32):
    """Custom type cceFarmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CceFarmEntryIndex_Type.__name__ = "Integer32"
_CceFarmEntryIndex_Object = MibTableColumn
cceFarmEntryIndex = _CceFarmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 1, 1, 1, 1),
    _CceFarmEntryIndex_Type()
)
cceFarmEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceFarmEntryIndex.setStatus("current")
_CceFarmEntryIpAddress_Type = IpAddress
_CceFarmEntryIpAddress_Object = MibTableColumn
cceFarmEntryIpAddress = _CceFarmEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 1, 1, 1, 2),
    _CceFarmEntryIpAddress_Type()
)
cceFarmEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFarmEntryIpAddress.setStatus("current")
_CceBasic_ObjectIdentity = ObjectIdentity
cceBasic = _CceBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 2)
)
_CceBasicIPAddress_Type = IpAddress
_CceBasicIPAddress_Object = MibScalar
cceBasicIPAddress = _CceBasicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 2, 1),
    _CceBasicIPAddress_Type()
)
cceBasicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceBasicIPAddress.setStatus("current")
_CceBasicNetMask_Type = IpAddress
_CceBasicNetMask_Object = MibScalar
cceBasicNetMask = _CceBasicNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 2, 2),
    _CceBasicNetMask_Type()
)
cceBasicNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceBasicNetMask.setStatus("current")
_CceBasicGatewayIpAddress_Type = IpAddress
_CceBasicGatewayIpAddress_Object = MibScalar
cceBasicGatewayIpAddress = _CceBasicGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 2, 3),
    _CceBasicGatewayIpAddress_Type()
)
cceBasicGatewayIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceBasicGatewayIpAddress.setStatus("current")
_CceBasicCacheName_Type = DisplayString
_CceBasicCacheName_Object = MibScalar
cceBasicCacheName = _CceBasicCacheName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 2, 4),
    _CceBasicCacheName_Type()
)
cceBasicCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceBasicCacheName.setStatus("current")
_CceBasicFarmName_Type = DisplayString
_CceBasicFarmName_Object = MibScalar
cceBasicFarmName = _CceBasicFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 2, 5),
    _CceBasicFarmName_Type()
)
cceBasicFarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceBasicFarmName.setStatus("current")
_CceDns_ObjectIdentity = ObjectIdentity
cceDns = _CceDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 3)
)
_CceDnsDomain_Type = DisplayString
_CceDnsDomain_Object = MibScalar
cceDnsDomain = _CceDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 3, 1),
    _CceDnsDomain_Type()
)
cceDnsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDnsDomain.setStatus("current")
_CceDnsTable_Object = MibTable
cceDnsTable = _CceDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cceDnsTable.setStatus("current")
_CceDnsEntry_Object = MibTableRow
cceDnsEntry = _CceDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 3, 2, 1)
)
cceDnsEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceDnsEntryIndex"),
)
if mibBuilder.loadTexts:
    cceDnsEntry.setStatus("current")


class _CceDnsEntryIndex_Type(Integer32):
    """Custom type cceDnsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CceDnsEntryIndex_Type.__name__ = "Integer32"
_CceDnsEntryIndex_Object = MibTableColumn
cceDnsEntryIndex = _CceDnsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 3, 2, 1, 1),
    _CceDnsEntryIndex_Type()
)
cceDnsEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceDnsEntryIndex.setStatus("current")
_CceDnsEntryIpAddress_Type = IpAddress
_CceDnsEntryIpAddress_Object = MibTableColumn
cceDnsEntryIpAddress = _CceDnsEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 3, 2, 1, 2),
    _CceDnsEntryIpAddress_Type()
)
cceDnsEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDnsEntryIpAddress.setStatus("current")
_CceIcpClient_ObjectIdentity = ObjectIdentity
cceIcpClient = _CceIcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4)
)
_CceIcpClientEnabled_Type = TruthValue
_CceIcpClientEnabled_Object = MibScalar
cceIcpClientEnabled = _CceIcpClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 1),
    _CceIcpClientEnabled_Type()
)
cceIcpClientEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientEnabled.setStatus("current")


class _CceIcpClientWait_Type(Integer32):
    """Custom type cceIcpClientWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CceIcpClientWait_Type.__name__ = "Integer32"
_CceIcpClientWait_Object = MibScalar
cceIcpClientWait = _CceIcpClientWait_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 2),
    _CceIcpClientWait_Type()
)
cceIcpClientWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientWait.setStatus("current")
if mibBuilder.loadTexts:
    cceIcpClientWait.setUnits("seconds")


class _CceIcpClientRetry_Type(Integer32):
    """Custom type cceIcpClientRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CceIcpClientRetry_Type.__name__ = "Integer32"
_CceIcpClientRetry_Object = MibScalar
cceIcpClientRetry = _CceIcpClientRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 3),
    _CceIcpClientRetry_Type()
)
cceIcpClientRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRetry.setStatus("current")
_CceIcpClientLocalDomains_Type = DisplayString
_CceIcpClientLocalDomains_Object = MibScalar
cceIcpClientLocalDomains = _CceIcpClientLocalDomains_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 4),
    _CceIcpClientLocalDomains_Type()
)
cceIcpClientLocalDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientLocalDomains.setStatus("current")
_CceIcpClientRemServTable_Object = MibTable
cceIcpClientRemServTable = _CceIcpClientRemServTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cceIcpClientRemServTable.setStatus("current")
_CceIcpClientRemServEntry_Object = MibTableRow
cceIcpClientRemServEntry = _CceIcpClientRemServEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1)
)
cceIcpClientRemServEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServIndex"),
)
if mibBuilder.loadTexts:
    cceIcpClientRemServEntry.setStatus("current")


class _CceIcpClientRemServIndex_Type(Integer32):
    """Custom type cceIcpClientRemServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CceIcpClientRemServIndex_Type.__name__ = "Integer32"
_CceIcpClientRemServIndex_Object = MibTableColumn
cceIcpClientRemServIndex = _CceIcpClientRemServIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 1),
    _CceIcpClientRemServIndex_Type()
)
cceIcpClientRemServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceIcpClientRemServIndex.setStatus("current")
_CceIcpClientRemServIpAddress_Type = IpAddress
_CceIcpClientRemServIpAddress_Object = MibTableColumn
cceIcpClientRemServIpAddress = _CceIcpClientRemServIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 2),
    _CceIcpClientRemServIpAddress_Type()
)
cceIcpClientRemServIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRemServIpAddress.setStatus("current")


class _CceIcpClientRemServState_Type(Integer32):
    """Custom type cceIcpClientRemServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("normal", 1),
          ("warning", 2))
    )


_CceIcpClientRemServState_Type.__name__ = "Integer32"
_CceIcpClientRemServState_Object = MibTableColumn
cceIcpClientRemServState = _CceIcpClientRemServState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 3),
    _CceIcpClientRemServState_Type()
)
cceIcpClientRemServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRemServState.setStatus("current")


class _CceIcpClientRemServType_Type(Integer32):
    """Custom type cceIcpClientRemServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("parent", 1),
          ("sibling", 2))
    )


_CceIcpClientRemServType_Type.__name__ = "Integer32"
_CceIcpClientRemServType_Object = MibTableColumn
cceIcpClientRemServType = _CceIcpClientRemServType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 4),
    _CceIcpClientRemServType_Type()
)
cceIcpClientRemServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRemServType.setStatus("current")


class _CceIcpClientRemServIcpPort_Type(Integer32):
    """Custom type cceIcpClientRemServIcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CceIcpClientRemServIcpPort_Type.__name__ = "Integer32"
_CceIcpClientRemServIcpPort_Object = MibTableColumn
cceIcpClientRemServIcpPort = _CceIcpClientRemServIcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 5),
    _CceIcpClientRemServIcpPort_Type()
)
cceIcpClientRemServIcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRemServIcpPort.setStatus("current")


class _CceIcpClientRemServHttpPort_Type(Integer32):
    """Custom type cceIcpClientRemServHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CceIcpClientRemServHttpPort_Type.__name__ = "Integer32"
_CceIcpClientRemServHttpPort_Object = MibTableColumn
cceIcpClientRemServHttpPort = _CceIcpClientRemServHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 6),
    _CceIcpClientRemServHttpPort_Type()
)
cceIcpClientRemServHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRemServHttpPort.setStatus("current")
_CceIcpClientRemServSelDomains_Type = DisplayString
_CceIcpClientRemServSelDomains_Object = MibTableColumn
cceIcpClientRemServSelDomains = _CceIcpClientRemServSelDomains_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 4, 5, 1, 7),
    _CceIcpClientRemServSelDomains_Type()
)
cceIcpClientRemServSelDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpClientRemServSelDomains.setStatus("current")
_CceIcpServer_ObjectIdentity = ObjectIdentity
cceIcpServer = _CceIcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5)
)
_CceIcpServerEnabled_Type = TruthValue
_CceIcpServerEnabled_Object = MibScalar
cceIcpServerEnabled = _CceIcpServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 1),
    _CceIcpServerEnabled_Type()
)
cceIcpServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpServerEnabled.setStatus("current")


class _CceIcpServerPort_Type(Integer32):
    """Custom type cceIcpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CceIcpServerPort_Type.__name__ = "Integer32"
_CceIcpServerPort_Object = MibScalar
cceIcpServerPort = _CceIcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 2),
    _CceIcpServerPort_Type()
)
cceIcpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpServerPort.setStatus("current")
_CceIcpServerRemClntTable_Object = MibTable
cceIcpServerRemClntTable = _CceIcpServerRemClntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cceIcpServerRemClntTable.setStatus("current")
_CceIcpServerRemClntEntry_Object = MibTableRow
cceIcpServerRemClntEntry = _CceIcpServerRemClntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 3, 1)
)
cceIcpServerRemClntEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceIcpServerRemClntIndex"),
)
if mibBuilder.loadTexts:
    cceIcpServerRemClntEntry.setStatus("current")


class _CceIcpServerRemClntIndex_Type(Integer32):
    """Custom type cceIcpServerRemClntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CceIcpServerRemClntIndex_Type.__name__ = "Integer32"
_CceIcpServerRemClntIndex_Object = MibTableColumn
cceIcpServerRemClntIndex = _CceIcpServerRemClntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 3, 1, 1),
    _CceIcpServerRemClntIndex_Type()
)
cceIcpServerRemClntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceIcpServerRemClntIndex.setStatus("current")
_CceIcpServerRemClntIPAddress_Type = IpAddress
_CceIcpServerRemClntIPAddress_Object = MibTableColumn
cceIcpServerRemClntIPAddress = _CceIcpServerRemClntIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 3, 1, 2),
    _CceIcpServerRemClntIPAddress_Type()
)
cceIcpServerRemClntIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpServerRemClntIPAddress.setStatus("current")
_CceIcpServerRemClntFetch_Type = TruthValue
_CceIcpServerRemClntFetch_Object = MibTableColumn
cceIcpServerRemClntFetch = _CceIcpServerRemClntFetch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 5, 3, 1, 3),
    _CceIcpServerRemClntFetch_Type()
)
cceIcpServerRemClntFetch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIcpServerRemClntFetch.setStatus("current")
_CceProxy_ObjectIdentity = ObjectIdentity
cceProxy = _CceProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 6)
)


class _CceProxyIncomingPort_Type(Integer32):
    """Custom type cceProxyIncomingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CceProxyIncomingPort_Type.__name__ = "Integer32"
_CceProxyIncomingPort_Object = MibScalar
cceProxyIncomingPort = _CceProxyIncomingPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 6, 1),
    _CceProxyIncomingPort_Type()
)
cceProxyIncomingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceProxyIncomingPort.setStatus("current")
_CceProxyOutgoingAddress_Type = DisplayString
_CceProxyOutgoingAddress_Object = MibScalar
cceProxyOutgoingAddress = _CceProxyOutgoingAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 6, 2),
    _CceProxyOutgoingAddress_Type()
)
cceProxyOutgoingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceProxyOutgoingAddress.setStatus("current")


class _CceProxyOutgoingPort_Type(Integer32):
    """Custom type cceProxyOutgoingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CceProxyOutgoingPort_Type.__name__ = "Integer32"
_CceProxyOutgoingPort_Object = MibScalar
cceProxyOutgoingPort = _CceProxyOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 6, 3),
    _CceProxyOutgoingPort_Type()
)
cceProxyOutgoingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceProxyOutgoingPort.setStatus("current")
_CceTime_ObjectIdentity = ObjectIdentity
cceTime = _CceTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7)
)
_CceTimeGmtTime_Type = DisplayString
_CceTimeGmtTime_Object = MibScalar
cceTimeGmtTime = _CceTimeGmtTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7, 1),
    _CceTimeGmtTime_Type()
)
cceTimeGmtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTimeGmtTime.setStatus("current")
_CceTimeGmtDate_Type = DisplayString
_CceTimeGmtDate_Object = MibScalar
cceTimeGmtDate = _CceTimeGmtDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7, 2),
    _CceTimeGmtDate_Type()
)
cceTimeGmtDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTimeGmtDate.setStatus("current")
_CceTimeTable_Object = MibTable
cceTimeTable = _CceTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cceTimeTable.setStatus("current")
_CceTimeEntry_Object = MibTableRow
cceTimeEntry = _CceTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7, 3, 1)
)
cceTimeEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceTimeEntryIndex"),
)
if mibBuilder.loadTexts:
    cceTimeEntry.setStatus("current")


class _CceTimeEntryIndex_Type(Integer32):
    """Custom type cceTimeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CceTimeEntryIndex_Type.__name__ = "Integer32"
_CceTimeEntryIndex_Object = MibTableColumn
cceTimeEntryIndex = _CceTimeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7, 3, 1, 1),
    _CceTimeEntryIndex_Type()
)
cceTimeEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceTimeEntryIndex.setStatus("current")
_CceTimeEntryIpAddress_Type = IpAddress
_CceTimeEntryIpAddress_Object = MibTableColumn
cceTimeEntryIpAddress = _CceTimeEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 1, 7, 3, 1, 2),
    _CceTimeEntryIpAddress_Type()
)
cceTimeEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTimeEntryIpAddress.setStatus("current")
_CceTuningGroup_ObjectIdentity = ObjectIdentity
cceTuningGroup = _CceTuningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2)
)
_CceCacheFarm_ObjectIdentity = ObjectIdentity
cceCacheFarm = _CceCacheFarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 1)
)


class _CceCacheFarmHealingModeWait_Type(Integer32):
    """Custom type cceCacheFarmHealingModeWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_CceCacheFarmHealingModeWait_Type.__name__ = "Integer32"
_CceCacheFarmHealingModeWait_Object = MibScalar
cceCacheFarmHealingModeWait = _CceCacheFarmHealingModeWait_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 1, 1),
    _CceCacheFarmHealingModeWait_Type()
)
cceCacheFarmHealingModeWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCacheFarmHealingModeWait.setStatus("current")
if mibBuilder.loadTexts:
    cceCacheFarmHealingModeWait.setUnits("milliseconds")


class _CceCacheFarmHealingModeRetry_Type(Integer32):
    """Custom type cceCacheFarmHealingModeRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CceCacheFarmHealingModeRetry_Type.__name__ = "Integer32"
_CceCacheFarmHealingModeRetry_Object = MibScalar
cceCacheFarmHealingModeRetry = _CceCacheFarmHealingModeRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 1, 2),
    _CceCacheFarmHealingModeRetry_Type()
)
cceCacheFarmHealingModeRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCacheFarmHealingModeRetry.setStatus("current")
_CceCacheFarmVersion_Type = DisplayString
_CceCacheFarmVersion_Object = MibScalar
cceCacheFarmVersion = _CceCacheFarmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 1, 3),
    _CceCacheFarmVersion_Type()
)
cceCacheFarmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCacheFarmVersion.setStatus("current")
_CceFreshness_ObjectIdentity = ObjectIdentity
cceFreshness = _CceFreshness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2)
)


class _CceFreshnessTextAgeMultiplier_Type(Integer32):
    """Custom type cceFreshnessTextAgeMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CceFreshnessTextAgeMultiplier_Type.__name__ = "Integer32"
_CceFreshnessTextAgeMultiplier_Object = MibScalar
cceFreshnessTextAgeMultiplier = _CceFreshnessTextAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 1),
    _CceFreshnessTextAgeMultiplier_Type()
)
cceFreshnessTextAgeMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessTextAgeMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    cceFreshnessTextAgeMultiplier.setUnits("percentage")


class _CceFreshnessBinaryAgeMultiplier_Type(Integer32):
    """Custom type cceFreshnessBinaryAgeMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CceFreshnessBinaryAgeMultiplier_Type.__name__ = "Integer32"
_CceFreshnessBinaryAgeMultiplier_Object = MibScalar
cceFreshnessBinaryAgeMultiplier = _CceFreshnessBinaryAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 2),
    _CceFreshnessBinaryAgeMultiplier_Type()
)
cceFreshnessBinaryAgeMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessBinaryAgeMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    cceFreshnessBinaryAgeMultiplier.setUnits("percentage")


class _CceFreshnessTextMaximumTTL_Type(Integer32):
    """Custom type cceFreshnessTextMaximumTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CceFreshnessTextMaximumTTL_Type.__name__ = "Integer32"
_CceFreshnessTextMaximumTTL_Object = MibScalar
cceFreshnessTextMaximumTTL = _CceFreshnessTextMaximumTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 3),
    _CceFreshnessTextMaximumTTL_Type()
)
cceFreshnessTextMaximumTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessTextMaximumTTL.setStatus("current")


class _CceFreshnessBinaryMaximumTTL_Type(Integer32):
    """Custom type cceFreshnessBinaryMaximumTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_CceFreshnessBinaryMaximumTTL_Type.__name__ = "Integer32"
_CceFreshnessBinaryMaximumTTL_Object = MibScalar
cceFreshnessBinaryMaximumTTL = _CceFreshnessBinaryMaximumTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 4),
    _CceFreshnessBinaryMaximumTTL_Type()
)
cceFreshnessBinaryMaximumTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessBinaryMaximumTTL.setStatus("current")


class _CceFreshnessUnitsMaximumTTL_Type(Integer32):
    """Custom type cceFreshnessUnitsMaximumTTL based on Integer32"""
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
        *(("days", 4),
          ("hours", 3),
          ("minutes", 2),
          ("seconds", 1))
    )


_CceFreshnessUnitsMaximumTTL_Type.__name__ = "Integer32"
_CceFreshnessUnitsMaximumTTL_Object = MibScalar
cceFreshnessUnitsMaximumTTL = _CceFreshnessUnitsMaximumTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 5),
    _CceFreshnessUnitsMaximumTTL_Type()
)
cceFreshnessUnitsMaximumTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessUnitsMaximumTTL.setStatus("current")
_CceFreshnessCacheCookies_Type = TruthValue
_CceFreshnessCacheCookies_Object = MibScalar
cceFreshnessCacheCookies = _CceFreshnessCacheCookies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 6),
    _CceFreshnessCacheCookies_Type()
)
cceFreshnessCacheCookies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessCacheCookies.setStatus("current")


class _CceFreshnessTextMaxAge_Type(Integer32):
    """Custom type cceFreshnessTextMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CceFreshnessTextMaxAge_Type.__name__ = "Integer32"
_CceFreshnessTextMaxAge_Object = MibScalar
cceFreshnessTextMaxAge = _CceFreshnessTextMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 7),
    _CceFreshnessTextMaxAge_Type()
)
cceFreshnessTextMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessTextMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    cceFreshnessTextMaxAge.setUnits("percentage")


class _CceFreshnessBinaryMaxAge_Type(Integer32):
    """Custom type cceFreshnessBinaryMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CceFreshnessBinaryMaxAge_Type.__name__ = "Integer32"
_CceFreshnessBinaryMaxAge_Object = MibScalar
cceFreshnessBinaryMaxAge = _CceFreshnessBinaryMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 8),
    _CceFreshnessBinaryMaxAge_Type()
)
cceFreshnessBinaryMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessBinaryMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    cceFreshnessBinaryMaxAge.setUnits("percentage")


class _CceFreshnessForceMiss_Type(Integer32):
    """Custom type cceFreshnessForceMiss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("retrieve", 2),
          ("revalidate", 1))
    )


_CceFreshnessForceMiss_Type.__name__ = "Integer32"
_CceFreshnessForceMiss_Object = MibScalar
cceFreshnessForceMiss = _CceFreshnessForceMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 2, 9),
    _CceFreshnessForceMiss_Type()
)
cceFreshnessForceMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceFreshnessForceMiss.setStatus("current")
_CceTcp_ObjectIdentity = ObjectIdentity
cceTcp = _CceTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3)
)


class _CceTcpServerSendBuffer_Type(Integer32):
    """Custom type cceTcpServerSendBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_CceTcpServerSendBuffer_Type.__name__ = "Integer32"
_CceTcpServerSendBuffer_Object = MibScalar
cceTcpServerSendBuffer = _CceTcpServerSendBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 1),
    _CceTcpServerSendBuffer_Type()
)
cceTcpServerSendBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpServerSendBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpServerSendBuffer.setUnits("kilobytes")


class _CceTcpClientSendBuffer_Type(Integer32):
    """Custom type cceTcpClientSendBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_CceTcpClientSendBuffer_Type.__name__ = "Integer32"
_CceTcpClientSendBuffer_Object = MibScalar
cceTcpClientSendBuffer = _CceTcpClientSendBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 2),
    _CceTcpClientSendBuffer_Type()
)
cceTcpClientSendBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpClientSendBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpClientSendBuffer.setUnits("kilobytes")


class _CceTcpServerRecvBuffer_Type(Integer32):
    """Custom type cceTcpServerRecvBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_CceTcpServerRecvBuffer_Type.__name__ = "Integer32"
_CceTcpServerRecvBuffer_Object = MibScalar
cceTcpServerRecvBuffer = _CceTcpServerRecvBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 3),
    _CceTcpServerRecvBuffer_Type()
)
cceTcpServerRecvBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpServerRecvBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpServerRecvBuffer.setUnits("kilobytes")


class _CceTcpClientRecvBuffer_Type(Integer32):
    """Custom type cceTcpClientRecvBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_CceTcpClientRecvBuffer_Type.__name__ = "Integer32"
_CceTcpClientRecvBuffer_Object = MibScalar
cceTcpClientRecvBuffer = _CceTcpClientRecvBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 4),
    _CceTcpClientRecvBuffer_Type()
)
cceTcpClientRecvBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpClientRecvBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpClientRecvBuffer.setUnits("kilobytes")


class _CceTcpServerReadWriteTimeout_Type(Integer32):
    """Custom type cceTcpServerReadWriteTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CceTcpServerReadWriteTimeout_Type.__name__ = "Integer32"
_CceTcpServerReadWriteTimeout_Object = MibScalar
cceTcpServerReadWriteTimeout = _CceTcpServerReadWriteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 5),
    _CceTcpServerReadWriteTimeout_Type()
)
cceTcpServerReadWriteTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpServerReadWriteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpServerReadWriteTimeout.setUnits("seconds")


class _CceTcpClientReadWriteTimeout_Type(Integer32):
    """Custom type cceTcpClientReadWriteTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CceTcpClientReadWriteTimeout_Type.__name__ = "Integer32"
_CceTcpClientReadWriteTimeout_Object = MibScalar
cceTcpClientReadWriteTimeout = _CceTcpClientReadWriteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 6),
    _CceTcpClientReadWriteTimeout_Type()
)
cceTcpClientReadWriteTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpClientReadWriteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpClientReadWriteTimeout.setUnits("seconds")


class _CceTcpConnectionIdleTimeout_Type(Integer32):
    """Custom type cceTcpConnectionIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_CceTcpConnectionIdleTimeout_Type.__name__ = "Integer32"
_CceTcpConnectionIdleTimeout_Object = MibScalar
cceTcpConnectionIdleTimeout = _CceTcpConnectionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 7),
    _CceTcpConnectionIdleTimeout_Type()
)
cceTcpConnectionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpConnectionIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpConnectionIdleTimeout.setUnits("seconds")


class _CceTcpConnectionWaitTimeout_Type(Integer32):
    """Custom type cceTcpConnectionWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 7200),
    )


_CceTcpConnectionWaitTimeout_Type.__name__ = "Integer32"
_CceTcpConnectionWaitTimeout_Object = MibScalar
cceTcpConnectionWaitTimeout = _CceTcpConnectionWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 8),
    _CceTcpConnectionWaitTimeout_Type()
)
cceTcpConnectionWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpConnectionWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cceTcpConnectionWaitTimeout.setUnits("seconds")


class _CceTcpConnectionRetry_Type(Integer32):
    """Custom type cceTcpConnectionRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CceTcpConnectionRetry_Type.__name__ = "Integer32"
_CceTcpConnectionRetry_Object = MibScalar
cceTcpConnectionRetry = _CceTcpConnectionRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 2, 3, 9),
    _CceTcpConnectionRetry_Type()
)
cceTcpConnectionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceTcpConnectionRetry.setStatus("current")
_CceAccessGroup_ObjectIdentity = ObjectIdentity
cceAccessGroup = _CceAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 3)
)
_CceUrlFilter_ObjectIdentity = ObjectIdentity
cceUrlFilter = _CceUrlFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 3, 1)
)


class _CceUrlFilterState_Type(Integer32):
    """Custom type cceUrlFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowGood", 3),
          ("blockBad", 2),
          ("off", 1))
    )


_CceUrlFilterState_Type.__name__ = "Integer32"
_CceUrlFilterState_Object = MibScalar
cceUrlFilterState = _CceUrlFilterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 3, 1, 1),
    _CceUrlFilterState_Type()
)
cceUrlFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUrlFilterState.setStatus("current")
_CceReportGroup_ObjectIdentity = ObjectIdentity
cceReportGroup = _CceReportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4)
)
_CceEvents_ObjectIdentity = ObjectIdentity
cceEvents = _CceEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1)
)


class _CceEventsTotal_Type(Integer32):
    """Custom type cceEventsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CceEventsTotal_Type.__name__ = "Integer32"
_CceEventsTotal_Object = MibScalar
cceEventsTotal = _CceEventsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 1),
    _CceEventsTotal_Type()
)
cceEventsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsTotal.setStatus("current")
_CceEventsCritical_Type = TruthValue
_CceEventsCritical_Object = MibScalar
cceEventsCritical = _CceEventsCritical_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 2),
    _CceEventsCritical_Type()
)
cceEventsCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsCritical.setStatus("current")
_CceEventsWarning_Type = TruthValue
_CceEventsWarning_Object = MibScalar
cceEventsWarning = _CceEventsWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 3),
    _CceEventsWarning_Type()
)
cceEventsWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsWarning.setStatus("current")
_CceEventsNotice_Type = TruthValue
_CceEventsNotice_Object = MibScalar
cceEventsNotice = _CceEventsNotice_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 4),
    _CceEventsNotice_Type()
)
cceEventsNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsNotice.setStatus("current")
_CceEventsTable_Object = MibTable
cceEventsTable = _CceEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    cceEventsTable.setStatus("current")
_CceEventsEntry_Object = MibTableRow
cceEventsEntry = _CceEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 5, 1)
)
cceEventsEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceEventsEntryIndex"),
)
if mibBuilder.loadTexts:
    cceEventsEntry.setStatus("current")


class _CceEventsEntryIndex_Type(Integer32):
    """Custom type cceEventsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 999),
    )


_CceEventsEntryIndex_Type.__name__ = "Integer32"
_CceEventsEntryIndex_Object = MibTableColumn
cceEventsEntryIndex = _CceEventsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 5, 1, 1),
    _CceEventsEntryIndex_Type()
)
cceEventsEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceEventsEntryIndex.setStatus("current")


class _CceEventsEntryType_Type(Integer32):
    """Custom type cceEventsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("notice", 1),
          ("warning", 2))
    )


_CceEventsEntryType_Type.__name__ = "Integer32"
_CceEventsEntryType_Object = MibTableColumn
cceEventsEntryType = _CceEventsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 5, 1, 2),
    _CceEventsEntryType_Type()
)
cceEventsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsEntryType.setStatus("current")
_CceEventsEntryMessage_Type = DisplayString
_CceEventsEntryMessage_Object = MibTableColumn
cceEventsEntryMessage = _CceEventsEntryMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 5, 1, 3),
    _CceEventsEntryMessage_Type()
)
cceEventsEntryMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsEntryMessage.setStatus("current")
_CceEventsEntryTime_Type = DisplayString
_CceEventsEntryTime_Object = MibTableColumn
cceEventsEntryTime = _CceEventsEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 1, 5, 1, 4),
    _CceEventsEntryTime_Type()
)
cceEventsEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceEventsEntryTime.setStatus("current")
_CceLogging_ObjectIdentity = ObjectIdentity
cceLogging = _CceLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2)
)
_CceLoggingEnabled_Type = TruthValue
_CceLoggingEnabled_Object = MibScalar
cceLoggingEnabled = _CceLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 1),
    _CceLoggingEnabled_Type()
)
cceLoggingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingEnabled.setStatus("current")


class _CceLoggingInterval_Type(Integer32):
    """Custom type cceLoggingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999999),
    )


_CceLoggingInterval_Type.__name__ = "Integer32"
_CceLoggingInterval_Object = MibScalar
cceLoggingInterval = _CceLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 2),
    _CceLoggingInterval_Type()
)
cceLoggingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cceLoggingInterval.setUnits("seconds")
_CceLoggingWorkingLogPresent_Type = TruthValue
_CceLoggingWorkingLogPresent_Object = MibScalar
cceLoggingWorkingLogPresent = _CceLoggingWorkingLogPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 3),
    _CceLoggingWorkingLogPresent_Type()
)
cceLoggingWorkingLogPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingWorkingLogPresent.setStatus("current")


class _CceLoggingSize_Type(Integer32):
    """Custom type cceLoggingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CceLoggingSize_Type.__name__ = "Integer32"
_CceLoggingSize_Object = MibScalar
cceLoggingSize = _CceLoggingSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 4),
    _CceLoggingSize_Type()
)
cceLoggingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingSize.setStatus("current")
if mibBuilder.loadTexts:
    cceLoggingSize.setUnits("Bytes")


class _CceLoggingAge_Type(Integer32):
    """Custom type cceLoggingAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999999),
    )


_CceLoggingAge_Type.__name__ = "Integer32"
_CceLoggingAge_Object = MibScalar
cceLoggingAge = _CceLoggingAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 5),
    _CceLoggingAge_Type()
)
cceLoggingAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingAge.setStatus("current")
if mibBuilder.loadTexts:
    cceLoggingAge.setUnits("seconds")
_CceLoggingArchiveLogPresent_Type = TruthValue
_CceLoggingArchiveLogPresent_Object = MibScalar
cceLoggingArchiveLogPresent = _CceLoggingArchiveLogPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 6),
    _CceLoggingArchiveLogPresent_Type()
)
cceLoggingArchiveLogPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingArchiveLogPresent.setStatus("current")


class _CceLoggingArchiveLogSize_Type(Integer32):
    """Custom type cceLoggingArchiveLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CceLoggingArchiveLogSize_Type.__name__ = "Integer32"
_CceLoggingArchiveLogSize_Object = MibScalar
cceLoggingArchiveLogSize = _CceLoggingArchiveLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 7),
    _CceLoggingArchiveLogSize_Type()
)
cceLoggingArchiveLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingArchiveLogSize.setStatus("current")
if mibBuilder.loadTexts:
    cceLoggingArchiveLogSize.setUnits("Bytes")
_CceLoggingWriteFailReason_Type = DisplayString
_CceLoggingWriteFailReason_Object = MibScalar
cceLoggingWriteFailReason = _CceLoggingWriteFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 4, 2, 8),
    _CceLoggingWriteFailReason_Type()
)
cceLoggingWriteFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceLoggingWriteFailReason.setStatus("current")
_CceStatsGroup_ObjectIdentity = ObjectIdentity
cceStatsGroup = _CceStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5)
)
_CceDiagDump_ObjectIdentity = ObjectIdentity
cceDiagDump = _CceDiagDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1)
)
_CceDiagDumpDiskCreates_Type = Counter32
_CceDiagDumpDiskCreates_Object = MibScalar
cceDiagDumpDiskCreates = _CceDiagDumpDiskCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 1),
    _CceDiagDumpDiskCreates_Type()
)
cceDiagDumpDiskCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskCreates.setStatus("current")
_CceDiagDumpDiskOpens_Type = Counter32
_CceDiagDumpDiskOpens_Object = MibScalar
cceDiagDumpDiskOpens = _CceDiagDumpDiskOpens_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 2),
    _CceDiagDumpDiskOpens_Type()
)
cceDiagDumpDiskOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskOpens.setStatus("current")
_CceDiagDumpDiskCloses_Type = Counter32
_CceDiagDumpDiskCloses_Object = MibScalar
cceDiagDumpDiskCloses = _CceDiagDumpDiskCloses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 3),
    _CceDiagDumpDiskCloses_Type()
)
cceDiagDumpDiskCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskCloses.setStatus("current")
_CceDiagDumpDiskDeletes_Type = Counter32
_CceDiagDumpDiskDeletes_Object = MibScalar
cceDiagDumpDiskDeletes = _CceDiagDumpDiskDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 4),
    _CceDiagDumpDiskDeletes_Type()
)
cceDiagDumpDiskDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskDeletes.setStatus("current")
_CceDiagDumpDiskReads_Type = Counter32
_CceDiagDumpDiskReads_Object = MibScalar
cceDiagDumpDiskReads = _CceDiagDumpDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 5),
    _CceDiagDumpDiskReads_Type()
)
cceDiagDumpDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskReads.setStatus("current")
_CceDiagDumpDiskWrites_Type = Counter32
_CceDiagDumpDiskWrites_Object = MibScalar
cceDiagDumpDiskWrites = _CceDiagDumpDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 6),
    _CceDiagDumpDiskWrites_Type()
)
cceDiagDumpDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskWrites.setStatus("current")
_CceDiagDumpDiskStats_Type = Counter32
_CceDiagDumpDiskStats_Object = MibScalar
cceDiagDumpDiskStats = _CceDiagDumpDiskStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 7),
    _CceDiagDumpDiskStats_Type()
)
cceDiagDumpDiskStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskStats.setStatus("current")
_CceDiagDumpDiskFree_Type = Counter32
_CceDiagDumpDiskFree_Object = MibScalar
cceDiagDumpDiskFree = _CceDiagDumpDiskFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 8),
    _CceDiagDumpDiskFree_Type()
)
cceDiagDumpDiskFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskFree.setStatus("current")
_CceDiagDumpDiskWraps_Type = Counter32
_CceDiagDumpDiskWraps_Object = MibScalar
cceDiagDumpDiskWraps = _CceDiagDumpDiskWraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 9),
    _CceDiagDumpDiskWraps_Type()
)
cceDiagDumpDiskWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskWraps.setStatus("current")
_CceDiagDumpDiskOverWrites_Type = Counter32
_CceDiagDumpDiskOverWrites_Object = MibScalar
cceDiagDumpDiskOverWrites = _CceDiagDumpDiskOverWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 10),
    _CceDiagDumpDiskOverWrites_Type()
)
cceDiagDumpDiskOverWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskOverWrites.setStatus("current")
_CceDiagDumpDiskTruncReads_Type = Counter32
_CceDiagDumpDiskTruncReads_Object = MibScalar
cceDiagDumpDiskTruncReads = _CceDiagDumpDiskTruncReads_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 11),
    _CceDiagDumpDiskTruncReads_Type()
)
cceDiagDumpDiskTruncReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskTruncReads.setStatus("current")
_CceDiagDumpDiskInodeErrors_Type = Counter32
_CceDiagDumpDiskInodeErrors_Object = MibScalar
cceDiagDumpDiskInodeErrors = _CceDiagDumpDiskInodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 12),
    _CceDiagDumpDiskInodeErrors_Type()
)
cceDiagDumpDiskInodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskInodeErrors.setStatus("current")
_CceDiagDumpDiskCrcErrors_Type = Counter32
_CceDiagDumpDiskCrcErrors_Object = MibScalar
cceDiagDumpDiskCrcErrors = _CceDiagDumpDiskCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 13),
    _CceDiagDumpDiskCrcErrors_Type()
)
cceDiagDumpDiskCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskCrcErrors.setStatus("current")
_CceDiagDumpDiskDirCollisions_Type = Counter32
_CceDiagDumpDiskDirCollisions_Object = MibScalar
cceDiagDumpDiskDirCollisions = _CceDiagDumpDiskDirCollisions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 14),
    _CceDiagDumpDiskDirCollisions_Type()
)
cceDiagDumpDiskDirCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpDiskDirCollisions.setStatus("current")
_CceDiagDumpBufferReads_Type = Counter32
_CceDiagDumpBufferReads_Object = MibScalar
cceDiagDumpBufferReads = _CceDiagDumpBufferReads_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 15),
    _CceDiagDumpBufferReads_Type()
)
cceDiagDumpBufferReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferReads.setStatus("current")
_CceDiagDumpBufferReadErrors_Type = Counter32
_CceDiagDumpBufferReadErrors_Object = MibScalar
cceDiagDumpBufferReadErrors = _CceDiagDumpBufferReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 16),
    _CceDiagDumpBufferReadErrors_Type()
)
cceDiagDumpBufferReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferReadErrors.setStatus("current")
_CceDiagDumpBufferWrites_Type = Counter32
_CceDiagDumpBufferWrites_Object = MibScalar
cceDiagDumpBufferWrites = _CceDiagDumpBufferWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 17),
    _CceDiagDumpBufferWrites_Type()
)
cceDiagDumpBufferWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferWrites.setStatus("current")
_CceDiagDumpBufferWriteErrors_Type = Counter32
_CceDiagDumpBufferWriteErrors_Object = MibScalar
cceDiagDumpBufferWriteErrors = _CceDiagDumpBufferWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 18),
    _CceDiagDumpBufferWriteErrors_Type()
)
cceDiagDumpBufferWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferWriteErrors.setStatus("current")
_CceDiagDumpBufferHits_Type = Counter32
_CceDiagDumpBufferHits_Object = MibScalar
cceDiagDumpBufferHits = _CceDiagDumpBufferHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 19),
    _CceDiagDumpBufferHits_Type()
)
cceDiagDumpBufferHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferHits.setStatus("current")
_CceDiagDumpBufferMisses_Type = Counter32
_CceDiagDumpBufferMisses_Object = MibScalar
cceDiagDumpBufferMisses = _CceDiagDumpBufferMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 20),
    _CceDiagDumpBufferMisses_Type()
)
cceDiagDumpBufferMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferMisses.setStatus("current")
_CceDiagDumpBufferSeekErrors_Type = Counter32
_CceDiagDumpBufferSeekErrors_Object = MibScalar
cceDiagDumpBufferSeekErrors = _CceDiagDumpBufferSeekErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 1, 21),
    _CceDiagDumpBufferSeekErrors_Type()
)
cceDiagDumpBufferSeekErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceDiagDumpBufferSeekErrors.setStatus("current")
_CceIms_ObjectIdentity = ObjectIdentity
cceIms = _CceIms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2)
)
_CceImsClientRequestTotal_Type = Counter64
_CceImsClientRequestTotal_Object = MibScalar
cceImsClientRequestTotal = _CceImsClientRequestTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 1),
    _CceImsClientRequestTotal_Type()
)
cceImsClientRequestTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientRequestTotal.setStatus("current")
_CceImsReceived_Type = Counter64
_CceImsReceived_Object = MibScalar
cceImsReceived = _CceImsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 2),
    _CceImsReceived_Type()
)
cceImsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsReceived.setStatus("current")
_CceImsClientTotalFromCache_Type = Counter64
_CceImsClientTotalFromCache_Object = MibScalar
cceImsClientTotalFromCache = _CceImsClientTotalFromCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 3),
    _CceImsClientTotalFromCache_Type()
)
cceImsClientTotalFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientTotalFromCache.setStatus("current")
_CceImsClientFreshFromCache_Type = Counter64
_CceImsClientFreshFromCache_Object = MibScalar
cceImsClientFreshFromCache = _CceImsClientFreshFromCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 4),
    _CceImsClientFreshFromCache_Type()
)
cceImsClientFreshFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientFreshFromCache.setStatus("current")
_CceImsClientStaleFromCache_Type = Counter64
_CceImsClientStaleFromCache_Object = MibScalar
cceImsClientStaleFromCache = _CceImsClientStaleFromCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 5),
    _CceImsClientStaleFromCache_Type()
)
cceImsClientStaleFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientStaleFromCache.setStatus("current")
_CceImsClientTotalCacheMiss_Type = Counter64
_CceImsClientTotalCacheMiss_Object = MibScalar
cceImsClientTotalCacheMiss = _CceImsClientTotalCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 6),
    _CceImsClientTotalCacheMiss_Type()
)
cceImsClientTotalCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientTotalCacheMiss.setStatus("current")
_CceImsClientFreshCacheMiss_Type = Counter64
_CceImsClientFreshCacheMiss_Object = MibScalar
cceImsClientFreshCacheMiss = _CceImsClientFreshCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 7),
    _CceImsClientFreshCacheMiss_Type()
)
cceImsClientFreshCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientFreshCacheMiss.setStatus("current")
_CceImsClientStaleCacheMiss_Type = Counter64
_CceImsClientStaleCacheMiss_Object = MibScalar
cceImsClientStaleCacheMiss = _CceImsClientStaleCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 8),
    _CceImsClientStaleCacheMiss_Type()
)
cceImsClientStaleCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientStaleCacheMiss.setStatus("current")
_CceImsClientTotalReval_Type = Counter64
_CceImsClientTotalReval_Object = MibScalar
cceImsClientTotalReval = _CceImsClientTotalReval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 9),
    _CceImsClientTotalReval_Type()
)
cceImsClientTotalReval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientTotalReval.setStatus("current")
_CceImsClientFreshReval_Type = Counter64
_CceImsClientFreshReval_Object = MibScalar
cceImsClientFreshReval = _CceImsClientFreshReval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 10),
    _CceImsClientFreshReval_Type()
)
cceImsClientFreshReval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientFreshReval.setStatus("current")
_CceImsClientStaleReval_Type = Counter64
_CceImsClientStaleReval_Object = MibScalar
cceImsClientStaleReval = _CceImsClientStaleReval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 11),
    _CceImsClientStaleReval_Type()
)
cceImsClientStaleReval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientStaleReval.setStatus("current")
_CceImsClientRequestToServer_Type = Counter64
_CceImsClientRequestToServer_Object = MibScalar
cceImsClientRequestToServer = _CceImsClientRequestToServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 12),
    _CceImsClientRequestToServer_Type()
)
cceImsClientRequestToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientRequestToServer.setStatus("current")
_CceImsServerTotalIssued_Type = Counter64
_CceImsServerTotalIssued_Object = MibScalar
cceImsServerTotalIssued = _CceImsServerTotalIssued_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 13),
    _CceImsServerTotalIssued_Type()
)
cceImsServerTotalIssued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsServerTotalIssued.setStatus("current")
_CceImsServerTotalDueClient_Type = Counter64
_CceImsServerTotalDueClient_Object = MibScalar
cceImsServerTotalDueClient = _CceImsServerTotalDueClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 14),
    _CceImsServerTotalDueClient_Type()
)
cceImsServerTotalDueClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsServerTotalDueClient.setStatus("current")
_CceImsServerFreshDueClient_Type = Counter64
_CceImsServerFreshDueClient_Object = MibScalar
cceImsServerFreshDueClient = _CceImsServerFreshDueClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 15),
    _CceImsServerFreshDueClient_Type()
)
cceImsServerFreshDueClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsServerFreshDueClient.setStatus("current")
_CceImsServerStaleDueClient_Type = Counter64
_CceImsServerStaleDueClient_Object = MibScalar
cceImsServerStaleDueClient = _CceImsServerStaleDueClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 16),
    _CceImsServerStaleDueClient_Type()
)
cceImsServerStaleDueClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsServerStaleDueClient.setStatus("current")
_CceImsServerTotalDueExpiration_Type = Counter64
_CceImsServerTotalDueExpiration_Object = MibScalar
cceImsServerTotalDueExpiration = _CceImsServerTotalDueExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 17),
    _CceImsServerTotalDueExpiration_Type()
)
cceImsServerTotalDueExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsServerTotalDueExpiration.setStatus("current")
_CceImsClientFreshDueExpiration_Type = Counter64
_CceImsClientFreshDueExpiration_Object = MibScalar
cceImsClientFreshDueExpiration = _CceImsClientFreshDueExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 18),
    _CceImsClientFreshDueExpiration_Type()
)
cceImsClientFreshDueExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsClientFreshDueExpiration.setStatus("current")
_CceImsServerStaleDueExpiration_Type = Counter64
_CceImsServerStaleDueExpiration_Object = MibScalar
cceImsServerStaleDueExpiration = _CceImsServerStaleDueExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 2, 19),
    _CceImsServerStaleDueExpiration_Type()
)
cceImsServerStaleDueExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceImsServerStaleDueExpiration.setStatus("current")
_CcePerformance_ObjectIdentity = ObjectIdentity
ccePerformance = _CcePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3)
)
_CcePerformanceReqPerSecMax_Type = Gauge32
_CcePerformanceReqPerSecMax_Object = MibScalar
ccePerformanceReqPerSecMax = _CcePerformanceReqPerSecMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 1),
    _CcePerformanceReqPerSecMax_Type()
)
ccePerformanceReqPerSecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceReqPerSecMax.setStatus("current")


class _CcePerformanceReqPerSecLast_Type(Integer32):
    """Custom type ccePerformanceReqPerSecLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceReqPerSecLast_Type.__name__ = "Integer32"
_CcePerformanceReqPerSecLast_Object = MibScalar
ccePerformanceReqPerSecLast = _CcePerformanceReqPerSecLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 2),
    _CcePerformanceReqPerSecLast_Type()
)
ccePerformanceReqPerSecLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceReqPerSecLast.setStatus("current")
_CcePerformanceBytesPerSecMax_Type = Gauge32
_CcePerformanceBytesPerSecMax_Object = MibScalar
ccePerformanceBytesPerSecMax = _CcePerformanceBytesPerSecMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 3),
    _CcePerformanceBytesPerSecMax_Type()
)
ccePerformanceBytesPerSecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceBytesPerSecMax.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceBytesPerSecMax.setUnits("Bytes-per-second")


class _CcePerformanceBytesPerSecLast_Type(Integer32):
    """Custom type ccePerformanceBytesPerSecLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceBytesPerSecLast_Type.__name__ = "Integer32"
_CcePerformanceBytesPerSecLast_Object = MibScalar
ccePerformanceBytesPerSecLast = _CcePerformanceBytesPerSecLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 4),
    _CcePerformanceBytesPerSecLast_Type()
)
ccePerformanceBytesPerSecLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceBytesPerSecLast.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceBytesPerSecLast.setUnits("Bytes-per-second")


class _CcePerformanceSecPerReqAvg_Type(Integer32):
    """Custom type ccePerformanceSecPerReqAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceSecPerReqAvg_Type.__name__ = "Integer32"
_CcePerformanceSecPerReqAvg_Object = MibScalar
ccePerformanceSecPerReqAvg = _CcePerformanceSecPerReqAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 5),
    _CcePerformanceSecPerReqAvg_Type()
)
ccePerformanceSecPerReqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqAvg.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqAvg.setUnits("milliseconds-per-req")


class _CcePerformanceSecPerReqMin_Type(Integer32):
    """Custom type ccePerformanceSecPerReqMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceSecPerReqMin_Type.__name__ = "Integer32"
_CcePerformanceSecPerReqMin_Object = MibScalar
ccePerformanceSecPerReqMin = _CcePerformanceSecPerReqMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 6),
    _CcePerformanceSecPerReqMin_Type()
)
ccePerformanceSecPerReqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqMin.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqMin.setUnits("milliseconds-per-req")
_CcePerformanceSecPerReqMax_Type = Gauge32
_CcePerformanceSecPerReqMax_Object = MibScalar
ccePerformanceSecPerReqMax = _CcePerformanceSecPerReqMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 7),
    _CcePerformanceSecPerReqMax_Type()
)
ccePerformanceSecPerReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqMax.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqMax.setUnits("milliseconds-per-req")


class _CcePerformanceSecPerReqLast_Type(Integer32):
    """Custom type ccePerformanceSecPerReqLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceSecPerReqLast_Type.__name__ = "Integer32"
_CcePerformanceSecPerReqLast_Object = MibScalar
ccePerformanceSecPerReqLast = _CcePerformanceSecPerReqLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 8),
    _CcePerformanceSecPerReqLast_Type()
)
ccePerformanceSecPerReqLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqLast.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceSecPerReqLast.setUnits("milliseconds-per-req")


class _CcePerformanceHitsSecPerReqAvg_Type(Integer32):
    """Custom type ccePerformanceHitsSecPerReqAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceHitsSecPerReqAvg_Type.__name__ = "Integer32"
_CcePerformanceHitsSecPerReqAvg_Object = MibScalar
ccePerformanceHitsSecPerReqAvg = _CcePerformanceHitsSecPerReqAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 9),
    _CcePerformanceHitsSecPerReqAvg_Type()
)
ccePerformanceHitsSecPerReqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqAvg.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqAvg.setUnits("milliseconds-per-req")


class _CcePerformanceHitsSecPerReqMin_Type(Integer32):
    """Custom type ccePerformanceHitsSecPerReqMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceHitsSecPerReqMin_Type.__name__ = "Integer32"
_CcePerformanceHitsSecPerReqMin_Object = MibScalar
ccePerformanceHitsSecPerReqMin = _CcePerformanceHitsSecPerReqMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 10),
    _CcePerformanceHitsSecPerReqMin_Type()
)
ccePerformanceHitsSecPerReqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqMin.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqMin.setUnits("milliseconds-per-req")
_CcePerformanceHitsSecPerReqMax_Type = Gauge32
_CcePerformanceHitsSecPerReqMax_Object = MibScalar
ccePerformanceHitsSecPerReqMax = _CcePerformanceHitsSecPerReqMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 11),
    _CcePerformanceHitsSecPerReqMax_Type()
)
ccePerformanceHitsSecPerReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqMax.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqMax.setUnits("milliseconds-per-req")


class _CcePerformanceHitsSecPerReqLast_Type(Integer32):
    """Custom type ccePerformanceHitsSecPerReqLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceHitsSecPerReqLast_Type.__name__ = "Integer32"
_CcePerformanceHitsSecPerReqLast_Object = MibScalar
ccePerformanceHitsSecPerReqLast = _CcePerformanceHitsSecPerReqLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 12),
    _CcePerformanceHitsSecPerReqLast_Type()
)
ccePerformanceHitsSecPerReqLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqLast.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceHitsSecPerReqLast.setUnits("milliseconds-per-req")


class _CcePerformanceMissSecPerReqAvg_Type(Integer32):
    """Custom type ccePerformanceMissSecPerReqAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceMissSecPerReqAvg_Type.__name__ = "Integer32"
_CcePerformanceMissSecPerReqAvg_Object = MibScalar
ccePerformanceMissSecPerReqAvg = _CcePerformanceMissSecPerReqAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 13),
    _CcePerformanceMissSecPerReqAvg_Type()
)
ccePerformanceMissSecPerReqAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqAvg.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqAvg.setUnits("milliseconds-per-req")


class _CcePerformanceMissSecPerReqMin_Type(Integer32):
    """Custom type ccePerformanceMissSecPerReqMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceMissSecPerReqMin_Type.__name__ = "Integer32"
_CcePerformanceMissSecPerReqMin_Object = MibScalar
ccePerformanceMissSecPerReqMin = _CcePerformanceMissSecPerReqMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 14),
    _CcePerformanceMissSecPerReqMin_Type()
)
ccePerformanceMissSecPerReqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqMin.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqMin.setUnits("milliseconds-per-req")
_CcePerformanceMissSecPerReqMax_Type = Gauge32
_CcePerformanceMissSecPerReqMax_Object = MibScalar
ccePerformanceMissSecPerReqMax = _CcePerformanceMissSecPerReqMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 15),
    _CcePerformanceMissSecPerReqMax_Type()
)
ccePerformanceMissSecPerReqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqMax.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqMax.setUnits("milliseconds-per-req")


class _CcePerformanceMissSecPerReqLast_Type(Integer32):
    """Custom type ccePerformanceMissSecPerReqLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceMissSecPerReqLast_Type.__name__ = "Integer32"
_CcePerformanceMissSecPerReqLast_Object = MibScalar
ccePerformanceMissSecPerReqLast = _CcePerformanceMissSecPerReqLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 16),
    _CcePerformanceMissSecPerReqLast_Type()
)
ccePerformanceMissSecPerReqLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqLast.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceMissSecPerReqLast.setUnits("milliseconds-per-req")


class _CcePerformanceObjectSizeAvg_Type(Integer32):
    """Custom type ccePerformanceObjectSizeAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceObjectSizeAvg_Type.__name__ = "Integer32"
_CcePerformanceObjectSizeAvg_Object = MibScalar
ccePerformanceObjectSizeAvg = _CcePerformanceObjectSizeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 17),
    _CcePerformanceObjectSizeAvg_Type()
)
ccePerformanceObjectSizeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeAvg.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeAvg.setUnits("byte/10")


class _CcePerformanceObjectSizeMin_Type(Integer32):
    """Custom type ccePerformanceObjectSizeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceObjectSizeMin_Type.__name__ = "Integer32"
_CcePerformanceObjectSizeMin_Object = MibScalar
ccePerformanceObjectSizeMin = _CcePerformanceObjectSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 18),
    _CcePerformanceObjectSizeMin_Type()
)
ccePerformanceObjectSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeMin.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeMin.setUnits("Bytes")
_CcePerformanceObjectSizeMax_Type = Gauge32
_CcePerformanceObjectSizeMax_Object = MibScalar
ccePerformanceObjectSizeMax = _CcePerformanceObjectSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 19),
    _CcePerformanceObjectSizeMax_Type()
)
ccePerformanceObjectSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeMax.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeMax.setUnits("Bytes")


class _CcePerformanceObjectSizeLast_Type(Integer32):
    """Custom type ccePerformanceObjectSizeLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcePerformanceObjectSizeLast_Type.__name__ = "Integer32"
_CcePerformanceObjectSizeLast_Object = MibScalar
ccePerformanceObjectSizeLast = _CcePerformanceObjectSizeLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 3, 20),
    _CcePerformanceObjectSizeLast_Type()
)
ccePerformanceObjectSizeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeLast.setStatus("current")
if mibBuilder.loadTexts:
    ccePerformanceObjectSizeLast.setUnits("bytes/10")
_CceRequests_ObjectIdentity = ObjectIdentity
cceRequests = _CceRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4)
)
_CceRequestsForcedReloadTotal_Type = Counter64
_CceRequestsForcedReloadTotal_Object = MibScalar
cceRequestsForcedReloadTotal = _CceRequestsForcedReloadTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 1),
    _CceRequestsForcedReloadTotal_Type()
)
cceRequestsForcedReloadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsForcedReloadTotal.setStatus("current")


class _CceRequestsForcedReloadPercent_Type(Integer32):
    """Custom type cceRequestsForcedReloadPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceRequestsForcedReloadPercent_Type.__name__ = "Integer32"
_CceRequestsForcedReloadPercent_Object = MibScalar
cceRequestsForcedReloadPercent = _CceRequestsForcedReloadPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 2),
    _CceRequestsForcedReloadPercent_Type()
)
cceRequestsForcedReloadPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsForcedReloadPercent.setStatus("current")
if mibBuilder.loadTexts:
    cceRequestsForcedReloadPercent.setUnits("percentage/10")
_CceRequestsNearHitsTotal_Type = Counter64
_CceRequestsNearHitsTotal_Object = MibScalar
cceRequestsNearHitsTotal = _CceRequestsNearHitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 3),
    _CceRequestsNearHitsTotal_Type()
)
cceRequestsNearHitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsNearHitsTotal.setStatus("current")


class _CceRequestsNearHitsPercent_Type(Integer32):
    """Custom type cceRequestsNearHitsPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceRequestsNearHitsPercent_Type.__name__ = "Integer32"
_CceRequestsNearHitsPercent_Object = MibScalar
cceRequestsNearHitsPercent = _CceRequestsNearHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 4),
    _CceRequestsNearHitsPercent_Type()
)
cceRequestsNearHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsNearHitsPercent.setStatus("current")
if mibBuilder.loadTexts:
    cceRequestsNearHitsPercent.setUnits("percentage/10")
_CceRequestsServerErrorTotal_Type = Counter64
_CceRequestsServerErrorTotal_Object = MibScalar
cceRequestsServerErrorTotal = _CceRequestsServerErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 5),
    _CceRequestsServerErrorTotal_Type()
)
cceRequestsServerErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsServerErrorTotal.setStatus("current")


class _CceRequestsServerErrorPercent_Type(Integer32):
    """Custom type cceRequestsServerErrorPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceRequestsServerErrorPercent_Type.__name__ = "Integer32"
_CceRequestsServerErrorPercent_Object = MibScalar
cceRequestsServerErrorPercent = _CceRequestsServerErrorPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 6),
    _CceRequestsServerErrorPercent_Type()
)
cceRequestsServerErrorPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsServerErrorPercent.setStatus("current")
if mibBuilder.loadTexts:
    cceRequestsServerErrorPercent.setUnits("percentage/10")
_CceRequestsUrlBlockedTotal_Type = Counter64
_CceRequestsUrlBlockedTotal_Object = MibScalar
cceRequestsUrlBlockedTotal = _CceRequestsUrlBlockedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 7),
    _CceRequestsUrlBlockedTotal_Type()
)
cceRequestsUrlBlockedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsUrlBlockedTotal.setStatus("current")


class _CceRequestsUrlBlockedPercent_Type(Integer32):
    """Custom type cceRequestsUrlBlockedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceRequestsUrlBlockedPercent_Type.__name__ = "Integer32"
_CceRequestsUrlBlockedPercent_Object = MibScalar
cceRequestsUrlBlockedPercent = _CceRequestsUrlBlockedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 8),
    _CceRequestsUrlBlockedPercent_Type()
)
cceRequestsUrlBlockedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsUrlBlockedPercent.setStatus("current")
if mibBuilder.loadTexts:
    cceRequestsUrlBlockedPercent.setUnits("percentage/10")
_CceRequestsIcpClientHits_Type = Counter64
_CceRequestsIcpClientHits_Object = MibScalar
cceRequestsIcpClientHits = _CceRequestsIcpClientHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 9),
    _CceRequestsIcpClientHits_Type()
)
cceRequestsIcpClientHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsIcpClientHits.setStatus("current")


class _CceRequestsIcpClientPercentage_Type(Integer32):
    """Custom type cceRequestsIcpClientPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceRequestsIcpClientPercentage_Type.__name__ = "Integer32"
_CceRequestsIcpClientPercentage_Object = MibScalar
cceRequestsIcpClientPercentage = _CceRequestsIcpClientPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 10),
    _CceRequestsIcpClientPercentage_Type()
)
cceRequestsIcpClientPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsIcpClientPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cceRequestsIcpClientPercentage.setUnits("percentage/10")
_CceRequestsIcpServerHits_Type = Counter64
_CceRequestsIcpServerHits_Object = MibScalar
cceRequestsIcpServerHits = _CceRequestsIcpServerHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 11),
    _CceRequestsIcpServerHits_Type()
)
cceRequestsIcpServerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsIcpServerHits.setStatus("current")


class _CceRequestsIcpServerPercentage_Type(Integer32):
    """Custom type cceRequestsIcpServerPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceRequestsIcpServerPercentage_Type.__name__ = "Integer32"
_CceRequestsIcpServerPercentage_Object = MibScalar
cceRequestsIcpServerPercentage = _CceRequestsIcpServerPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 4, 12),
    _CceRequestsIcpServerPercentage_Type()
)
cceRequestsIcpServerPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRequestsIcpServerPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cceRequestsIcpServerPercentage.setUnits("percentage/10")
_CceSavings_ObjectIdentity = ObjectIdentity
cceSavings = _CceSavings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5)
)
_CceSavingsRequestsTotal_Type = Counter64
_CceSavingsRequestsTotal_Object = MibScalar
cceSavingsRequestsTotal = _CceSavingsRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 1),
    _CceSavingsRequestsTotal_Type()
)
cceSavingsRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsRequestsTotal.setStatus("current")
_CceSavingsRequestsHits_Type = Counter64
_CceSavingsRequestsHits_Object = MibScalar
cceSavingsRequestsHits = _CceSavingsRequestsHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 2),
    _CceSavingsRequestsHits_Type()
)
cceSavingsRequestsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsRequestsHits.setStatus("current")
_CceSavingsRequestsMiss_Type = Counter64
_CceSavingsRequestsMiss_Object = MibScalar
cceSavingsRequestsMiss = _CceSavingsRequestsMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 3),
    _CceSavingsRequestsMiss_Type()
)
cceSavingsRequestsMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsRequestsMiss.setStatus("current")


class _CceSavingsRequestsSavings_Type(Integer32):
    """Custom type cceSavingsRequestsSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceSavingsRequestsSavings_Type.__name__ = "Integer32"
_CceSavingsRequestsSavings_Object = MibScalar
cceSavingsRequestsSavings = _CceSavingsRequestsSavings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 4),
    _CceSavingsRequestsSavings_Type()
)
cceSavingsRequestsSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsRequestsSavings.setStatus("current")
if mibBuilder.loadTexts:
    cceSavingsRequestsSavings.setUnits("percentage/10")
_CceSavingsBytesServedTotal_Type = Counter64
_CceSavingsBytesServedTotal_Object = MibScalar
cceSavingsBytesServedTotal = _CceSavingsBytesServedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 5),
    _CceSavingsBytesServedTotal_Type()
)
cceSavingsBytesServedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsBytesServedTotal.setStatus("current")
_CceSavingsBytesServedHits_Type = Counter64
_CceSavingsBytesServedHits_Object = MibScalar
cceSavingsBytesServedHits = _CceSavingsBytesServedHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 6),
    _CceSavingsBytesServedHits_Type()
)
cceSavingsBytesServedHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsBytesServedHits.setStatus("current")
_CceSavingsBytesServedMiss_Type = Counter64
_CceSavingsBytesServedMiss_Object = MibScalar
cceSavingsBytesServedMiss = _CceSavingsBytesServedMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 7),
    _CceSavingsBytesServedMiss_Type()
)
cceSavingsBytesServedMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsBytesServedMiss.setStatus("current")


class _CceSavingsBytesServedSavings_Type(Integer32):
    """Custom type cceSavingsBytesServedSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CceSavingsBytesServedSavings_Type.__name__ = "Integer32"
_CceSavingsBytesServedSavings_Object = MibScalar
cceSavingsBytesServedSavings = _CceSavingsBytesServedSavings_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 5, 8),
    _CceSavingsBytesServedSavings_Type()
)
cceSavingsBytesServedSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceSavingsBytesServedSavings.setStatus("current")
if mibBuilder.loadTexts:
    cceSavingsBytesServedSavings.setUnits("percentage/10")
_CceUsage_ObjectIdentity = ObjectIdentity
cceUsage = _CceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6)
)


class _CceUsageCPUCurrent_Type(Integer32):
    """Custom type cceUsageCPUCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CceUsageCPUCurrent_Type.__name__ = "Integer32"
_CceUsageCPUCurrent_Object = MibScalar
cceUsageCPUCurrent = _CceUsageCPUCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 1),
    _CceUsageCPUCurrent_Type()
)
cceUsageCPUCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageCPUCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageCPUCurrent.setUnits("percentage")
_CceUsageCPUPeak_Type = Gauge32
_CceUsageCPUPeak_Object = MibScalar
cceUsageCPUPeak = _CceUsageCPUPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 2),
    _CceUsageCPUPeak_Type()
)
cceUsageCPUPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageCPUPeak.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageCPUPeak.setUnits("percentage")


class _CceUsageDiskCurrent_Type(Integer32):
    """Custom type cceUsageDiskCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CceUsageDiskCurrent_Type.__name__ = "Integer32"
_CceUsageDiskCurrent_Object = MibScalar
cceUsageDiskCurrent = _CceUsageDiskCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 3),
    _CceUsageDiskCurrent_Type()
)
cceUsageDiskCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskCurrent.setStatus("obsolete")
if mibBuilder.loadTexts:
    cceUsageDiskCurrent.setUnits("percentage")
_CceUsageDiskPeak_Type = Gauge32
_CceUsageDiskPeak_Object = MibScalar
cceUsageDiskPeak = _CceUsageDiskPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 4),
    _CceUsageDiskPeak_Type()
)
cceUsageDiskPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskPeak.setStatus("obsolete")
if mibBuilder.loadTexts:
    cceUsageDiskPeak.setUnits("percentage")


class _CceUsageNetCurrent_Type(Integer32):
    """Custom type cceUsageNetCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CceUsageNetCurrent_Type.__name__ = "Integer32"
_CceUsageNetCurrent_Object = MibScalar
cceUsageNetCurrent = _CceUsageNetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 5),
    _CceUsageNetCurrent_Type()
)
cceUsageNetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageNetCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageNetCurrent.setUnits("percentage")
_CceUsageNetPeak_Type = Gauge32
_CceUsageNetPeak_Object = MibScalar
cceUsageNetPeak = _CceUsageNetPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 6),
    _CceUsageNetPeak_Type()
)
cceUsageNetPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageNetPeak.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageNetPeak.setUnits("percentage")
_CceUsageConnsCurrent_Type = Integer32
_CceUsageConnsCurrent_Object = MibScalar
cceUsageConnsCurrent = _CceUsageConnsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 7),
    _CceUsageConnsCurrent_Type()
)
cceUsageConnsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageConnsCurrent.setStatus("current")
_CceUsageConnsPeak_Type = Gauge32
_CceUsageConnsPeak_Object = MibScalar
cceUsageConnsPeak = _CceUsageConnsPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 8),
    _CceUsageConnsPeak_Type()
)
cceUsageConnsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageConnsPeak.setStatus("current")
_CceUsageDiskVolumeTable_Object = MibTable
cceUsageDiskVolumeTable = _CceUsageDiskVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9)
)
if mibBuilder.loadTexts:
    cceUsageDiskVolumeTable.setStatus("current")
_CceUsageDiskVolumeEntry_Object = MibTableRow
cceUsageDiskVolumeEntry = _CceUsageDiskVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1)
)
cceUsageDiskVolumeEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeEntryIndex"),
)
if mibBuilder.loadTexts:
    cceUsageDiskVolumeEntry.setStatus("current")


class _CceUsageDiskVolumeEntryIndex_Type(Integer32):
    """Custom type cceUsageDiskVolumeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CceUsageDiskVolumeEntryIndex_Type.__name__ = "Integer32"
_CceUsageDiskVolumeEntryIndex_Object = MibTableColumn
cceUsageDiskVolumeEntryIndex = _CceUsageDiskVolumeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 1),
    _CceUsageDiskVolumeEntryIndex_Type()
)
cceUsageDiskVolumeEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeEntryIndex.setStatus("current")
_CceUsageDiskVolumeName_Type = DisplayString
_CceUsageDiskVolumeName_Object = MibTableColumn
cceUsageDiskVolumeName = _CceUsageDiskVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 2),
    _CceUsageDiskVolumeName_Type()
)
cceUsageDiskVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeName.setStatus("current")
_CceUsageDiskVolumeEverMounted_Type = TruthValue
_CceUsageDiskVolumeEverMounted_Object = MibTableColumn
cceUsageDiskVolumeEverMounted = _CceUsageDiskVolumeEverMounted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 3),
    _CceUsageDiskVolumeEverMounted_Type()
)
cceUsageDiskVolumeEverMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeEverMounted.setStatus("current")
_CceUsageDiskVolumeCurrentlyMounted_Type = TruthValue
_CceUsageDiskVolumeCurrentlyMounted_Object = MibTableColumn
cceUsageDiskVolumeCurrentlyMounted = _CceUsageDiskVolumeCurrentlyMounted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 4),
    _CceUsageDiskVolumeCurrentlyMounted_Type()
)
cceUsageDiskVolumeCurrentlyMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeCurrentlyMounted.setStatus("current")


class _CceUsageDiskVolumeUnmountReason_Type(Integer32):
    """Custom type cceUsageDiskVolumeUnmountReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("normal", 1),
          ("notApplicable", 0))
    )


_CceUsageDiskVolumeUnmountReason_Type.__name__ = "Integer32"
_CceUsageDiskVolumeUnmountReason_Object = MibTableColumn
cceUsageDiskVolumeUnmountReason = _CceUsageDiskVolumeUnmountReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 5),
    _CceUsageDiskVolumeUnmountReason_Type()
)
cceUsageDiskVolumeUnmountReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeUnmountReason.setStatus("current")


class _CceUsageDiskVolumeCurrent_Type(Integer32):
    """Custom type cceUsageDiskVolumeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CceUsageDiskVolumeCurrent_Type.__name__ = "Integer32"
_CceUsageDiskVolumeCurrent_Object = MibTableColumn
cceUsageDiskVolumeCurrent = _CceUsageDiskVolumeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 6),
    _CceUsageDiskVolumeCurrent_Type()
)
cceUsageDiskVolumeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageDiskVolumeCurrent.setUnits("percentage")
_CceUsageDiskVolumePeak_Type = Gauge32
_CceUsageDiskVolumePeak_Object = MibTableColumn
cceUsageDiskVolumePeak = _CceUsageDiskVolumePeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 9, 1, 7),
    _CceUsageDiskVolumePeak_Type()
)
cceUsageDiskVolumePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDiskVolumePeak.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageDiskVolumePeak.setUnits("percentage")
_CceUsageDosfsVolumeTable_Object = MibTable
cceUsageDosfsVolumeTable = _CceUsageDosfsVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10)
)
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeTable.setStatus("current")
_CceUsageDosfsVolumeEntry_Object = MibTableRow
cceUsageDosfsVolumeEntry = _CceUsageDosfsVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10, 1)
)
cceUsageDosfsVolumeEntry.setIndexNames(
    (0, "CISCO-CACHE-ENGINE-MIB", "cceUsageDosfsVolumeEntryIndex"),
)
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeEntry.setStatus("current")


class _CceUsageDosfsVolumeEntryIndex_Type(Integer32):
    """Custom type cceUsageDosfsVolumeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CceUsageDosfsVolumeEntryIndex_Type.__name__ = "Integer32"
_CceUsageDosfsVolumeEntryIndex_Object = MibTableColumn
cceUsageDosfsVolumeEntryIndex = _CceUsageDosfsVolumeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10, 1, 1),
    _CceUsageDosfsVolumeEntryIndex_Type()
)
cceUsageDosfsVolumeEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeEntryIndex.setStatus("current")
_CceUsageDosfsVolumeName_Type = DisplayString
_CceUsageDosfsVolumeName_Object = MibTableColumn
cceUsageDosfsVolumeName = _CceUsageDosfsVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10, 1, 2),
    _CceUsageDosfsVolumeName_Type()
)
cceUsageDosfsVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeName.setStatus("current")


class _CceUsageDosfsVolumeState_Type(Integer32):
    """Custom type cceUsageDosfsVolumeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CceUsageDosfsVolumeState_Type.__name__ = "Integer32"
_CceUsageDosfsVolumeState_Object = MibTableColumn
cceUsageDosfsVolumeState = _CceUsageDosfsVolumeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10, 1, 3),
    _CceUsageDosfsVolumeState_Type()
)
cceUsageDosfsVolumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeState.setStatus("current")
_CceUsageDosfsVolumeFreeSpace_Type = Gauge32
_CceUsageDosfsVolumeFreeSpace_Object = MibTableColumn
cceUsageDosfsVolumeFreeSpace = _CceUsageDosfsVolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10, 1, 4),
    _CceUsageDosfsVolumeFreeSpace_Type()
)
cceUsageDosfsVolumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeFreeSpace.setUnits("Bytes")
_CceUsageDosfsVolumeTotalSpace_Type = Gauge32
_CceUsageDosfsVolumeTotalSpace_Object = MibTableColumn
cceUsageDosfsVolumeTotalSpace = _CceUsageDosfsVolumeTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 5, 6, 10, 1, 5),
    _CceUsageDosfsVolumeTotalSpace_Type()
)
cceUsageDosfsVolumeTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeTotalSpace.setStatus("current")
if mibBuilder.loadTexts:
    cceUsageDosfsVolumeTotalSpace.setUnits("Bytes")
_CceHardwareGroup_ObjectIdentity = ObjectIdentity
cceHardwareGroup = _CceHardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 6)
)
_CceInterfaces_ObjectIdentity = ObjectIdentity
cceInterfaces = _CceInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 6, 1)
)
_CceIfFullDuplex_Type = TruthValue
_CceIfFullDuplex_Object = MibScalar
cceIfFullDuplex = _CceIfFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 1, 1, 6, 1, 1),
    _CceIfFullDuplex_Type()
)
cceIfFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceIfFullDuplex.setStatus("current")
_CiscoCacheEngineMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoCacheEngineMIBTrapPrefix = _CiscoCacheEngineMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2)
)
_CiscoCacheEngineMIBTraps_ObjectIdentity = ObjectIdentity
ciscoCacheEngineMIBTraps = _CiscoCacheEngineMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0)
)
_CiscoCacheEngineMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCacheEngineMIBConformance = _CiscoCacheEngineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3)
)
_CiscoCacheEngineMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCacheEngineMIBCompliances = _CiscoCacheEngineMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 1)
)
_CiscoCacheEngineMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCacheEngineMIBGroups = _CiscoCacheEngineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2)
)

# Managed Objects groups

cceFarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 1)
)
cceFarmGroup.setObjects(
    ("CISCO-CACHE-ENGINE-MIB", "cceFarmEntryIpAddress")
)
if mibBuilder.loadTexts:
    cceFarmGroup.setStatus("current")

cceBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 2)
)
cceBasicGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceBasicIPAddress"),
        ("CISCO-CACHE-ENGINE-MIB", "cceBasicNetMask"),
        ("CISCO-CACHE-ENGINE-MIB", "cceBasicGatewayIpAddress"),
        ("CISCO-CACHE-ENGINE-MIB", "cceBasicCacheName"),
        ("CISCO-CACHE-ENGINE-MIB", "cceBasicFarmName"))
)
if mibBuilder.loadTexts:
    cceBasicGroup.setStatus("current")

cceDnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 3)
)
cceDnsGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceDnsDomain"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDnsEntryIpAddress"))
)
if mibBuilder.loadTexts:
    cceDnsGroup.setStatus("current")

cceIcpClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 4)
)
cceIcpClientGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceIcpClientEnabled"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientWait"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRetry"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientLocalDomains"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServIpAddress"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServState"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServType"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServIcpPort"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServHttpPort"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpClientRemServSelDomains"))
)
if mibBuilder.loadTexts:
    cceIcpClientGroup.setStatus("current")

cceIcpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 5)
)
cceIcpServerGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceIcpServerEnabled"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpServerPort"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpServerRemClntIPAddress"),
        ("CISCO-CACHE-ENGINE-MIB", "cceIcpServerRemClntFetch"))
)
if mibBuilder.loadTexts:
    cceIcpServerGroup.setStatus("current")

cceProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 6)
)
cceProxyGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceProxyIncomingPort"),
        ("CISCO-CACHE-ENGINE-MIB", "cceProxyOutgoingAddress"),
        ("CISCO-CACHE-ENGINE-MIB", "cceProxyOutgoingPort"))
)
if mibBuilder.loadTexts:
    cceProxyGroup.setStatus("current")

cceTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 7)
)
cceTimeGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceTimeGmtTime"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTimeGmtDate"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTimeEntryIpAddress"))
)
if mibBuilder.loadTexts:
    cceTimeGroup.setStatus("current")

cceCacheFarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 8)
)
cceCacheFarmGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceCacheFarmHealingModeWait"),
        ("CISCO-CACHE-ENGINE-MIB", "cceCacheFarmHealingModeRetry"),
        ("CISCO-CACHE-ENGINE-MIB", "cceCacheFarmVersion"))
)
if mibBuilder.loadTexts:
    cceCacheFarmGroup.setStatus("current")

cceFreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 9)
)
cceFreshGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceFreshnessTextAgeMultiplier"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessBinaryAgeMultiplier"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessTextMaximumTTL"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessBinaryMaximumTTL"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessUnitsMaximumTTL"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessCacheCookies"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessTextMaxAge"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessBinaryMaxAge"),
        ("CISCO-CACHE-ENGINE-MIB", "cceFreshnessForceMiss"))
)
if mibBuilder.loadTexts:
    cceFreshGroup.setStatus("current")

cceTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 10)
)
cceTCPGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceTcpServerSendBuffer"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpClientSendBuffer"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpServerRecvBuffer"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpClientRecvBuffer"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpServerReadWriteTimeout"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpClientReadWriteTimeout"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpConnectionIdleTimeout"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpConnectionWaitTimeout"),
        ("CISCO-CACHE-ENGINE-MIB", "cceTcpConnectionRetry"))
)
if mibBuilder.loadTexts:
    cceTCPGroup.setStatus("current")

cceUrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 11)
)
cceUrlGroup.setObjects(
    ("CISCO-CACHE-ENGINE-MIB", "cceUrlFilterState")
)
if mibBuilder.loadTexts:
    cceUrlGroup.setStatus("current")

cceEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 12)
)
cceEventsGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceEventsTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceEventsCritical"),
        ("CISCO-CACHE-ENGINE-MIB", "cceEventsWarning"),
        ("CISCO-CACHE-ENGINE-MIB", "cceEventsNotice"),
        ("CISCO-CACHE-ENGINE-MIB", "cceEventsEntryType"),
        ("CISCO-CACHE-ENGINE-MIB", "cceEventsEntryMessage"),
        ("CISCO-CACHE-ENGINE-MIB", "cceEventsEntryTime"))
)
if mibBuilder.loadTexts:
    cceEventsGroup.setStatus("current")

cceLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 13)
)
cceLogGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceLoggingEnabled"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingInterval"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingWorkingLogPresent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingSize"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingAge"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingArchiveLogPresent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingArchiveLogSize"),
        ("CISCO-CACHE-ENGINE-MIB", "cceLoggingWriteFailReason"))
)
if mibBuilder.loadTexts:
    cceLogGroup.setStatus("current")

cceDiagDumpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 14)
)
cceDiagDumpGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskCreates"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskOpens"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskCloses"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskDeletes"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskReads"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskWrites"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskStats"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskFree"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskWraps"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskOverWrites"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskTruncReads"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskInodeErrors"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskCrcErrors"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpDiskDirCollisions"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferReads"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferReadErrors"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferWrites"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferWriteErrors"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferHits"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferMisses"),
        ("CISCO-CACHE-ENGINE-MIB", "cceDiagDumpBufferSeekErrors"))
)
if mibBuilder.loadTexts:
    cceDiagDumpGroup.setStatus("current")

cceImsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 15)
)
cceImsGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceImsClientRequestTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsReceived"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientTotalFromCache"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientFreshFromCache"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientStaleFromCache"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientTotalCacheMiss"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientFreshCacheMiss"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientStaleCacheMiss"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientTotalReval"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientFreshReval"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientStaleReval"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientRequestToServer"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsServerTotalIssued"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsServerTotalDueClient"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsServerFreshDueClient"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsServerStaleDueClient"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsServerTotalDueExpiration"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsClientFreshDueExpiration"),
        ("CISCO-CACHE-ENGINE-MIB", "cceImsServerStaleDueExpiration"))
)
if mibBuilder.loadTexts:
    cceImsGroup.setStatus("current")

ccePerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 16)
)
ccePerfGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "ccePerformanceReqPerSecMax"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceReqPerSecLast"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceBytesPerSecMax"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceBytesPerSecLast"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceSecPerReqAvg"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceSecPerReqMin"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceSecPerReqMax"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceSecPerReqLast"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceHitsSecPerReqAvg"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceHitsSecPerReqMin"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceHitsSecPerReqMax"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceHitsSecPerReqLast"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceMissSecPerReqAvg"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceMissSecPerReqMin"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceMissSecPerReqMax"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceMissSecPerReqLast"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceObjectSizeAvg"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceObjectSizeMin"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceObjectSizeMax"),
        ("CISCO-CACHE-ENGINE-MIB", "ccePerformanceObjectSizeLast"))
)
if mibBuilder.loadTexts:
    ccePerfGroup.setStatus("current")

cceReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 17)
)
cceReqGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceRequestsForcedReloadTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsForcedReloadPercent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsNearHitsTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsNearHitsPercent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsServerErrorTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsServerErrorPercent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsUrlBlockedTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsUrlBlockedPercent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsIcpClientHits"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsIcpClientPercentage"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsIcpServerHits"),
        ("CISCO-CACHE-ENGINE-MIB", "cceRequestsIcpServerPercentage"))
)
if mibBuilder.loadTexts:
    cceReqGroup.setStatus("current")

cceSaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 18)
)
cceSaveGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceSavingsRequestsTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsRequestsHits"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsRequestsMiss"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsRequestsSavings"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsBytesServedTotal"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsBytesServedHits"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsBytesServedMiss"),
        ("CISCO-CACHE-ENGINE-MIB", "cceSavingsBytesServedSavings"))
)
if mibBuilder.loadTexts:
    cceSaveGroup.setStatus("current")

cceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 19)
)
cceUsageGroup.setObjects(
      *(("CISCO-CACHE-ENGINE-MIB", "cceUsageCPUCurrent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageCPUPeak"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskCurrent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskPeak"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageNetCurrent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageNetPeak"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageConnsCurrent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageConnsPeak"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeName"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeEverMounted"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeCurrentlyMounted"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeUnmountReason"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeCurrent"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumePeak"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDosfsVolumeName"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDosfsVolumeState"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDosfsVolumeFreeSpace"),
        ("CISCO-CACHE-ENGINE-MIB", "cceUsageDosfsVolumeTotalSpace"))
)
if mibBuilder.loadTexts:
    cceUsageGroup.setStatus("current")

cceInterfacesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 2, 20)
)
cceInterfacesGroup.setObjects(
    ("CISCO-CACHE-ENGINE-MIB", "cceIfFullDuplex")
)
if mibBuilder.loadTexts:
    cceInterfacesGroup.setStatus("current")


# Notification objects

cacheTrapReadDiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 1)
)
if mibBuilder.loadTexts:
    cacheTrapReadDiskError.setStatus(
        "current"
    )

cacheTrapWriteDiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 2)
)
if mibBuilder.loadTexts:
    cacheTrapWriteDiskError.setStatus(
        "current"
    )

cacheTrapWriteTransFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 3)
)
if mibBuilder.loadTexts:
    cacheTrapWriteTransFailed.setStatus(
        "current"
    )

cacheTrapTooManyThreadsDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 4)
)
if mibBuilder.loadTexts:
    cacheTrapTooManyThreadsDead.setStatus(
        "current"
    )

cacheTrapWccpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 5)
)
if mibBuilder.loadTexts:
    cacheTrapWccpDisabled.setStatus(
        "current"
    )

cacheTrapDiskVolUnmounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 6)
)
cacheTrapDiskVolUnmounted.setObjects(
    ("CISCO-CACHE-ENGINE-MIB", "cceUsageDiskVolumeName")
)
if mibBuilder.loadTexts:
    cacheTrapDiskVolUnmounted.setStatus(
        "current"
    )

cacheTrapDosfsVolFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 2, 0, 7)
)
cacheTrapDosfsVolFull.setObjects(
    ("CISCO-CACHE-ENGINE-MIB", "cceUsageDosfsVolumeName")
)
if mibBuilder.loadTexts:
    cacheTrapDosfsVolFull.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCacheEngineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 39, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCacheEngineMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CACHE-ENGINE-MIB",
    **{"ciscoCacheEngineMIB": ciscoCacheEngineMIB,
       "ciscoCacheEngineMIBObjects": ciscoCacheEngineMIBObjects,
       "ciscoCacheEngineConf": ciscoCacheEngineConf,
       "cceConfigGroup": cceConfigGroup,
       "cceFarm": cceFarm,
       "cceFarmTable": cceFarmTable,
       "cceFarmEntry": cceFarmEntry,
       "cceFarmEntryIndex": cceFarmEntryIndex,
       "cceFarmEntryIpAddress": cceFarmEntryIpAddress,
       "cceBasic": cceBasic,
       "cceBasicIPAddress": cceBasicIPAddress,
       "cceBasicNetMask": cceBasicNetMask,
       "cceBasicGatewayIpAddress": cceBasicGatewayIpAddress,
       "cceBasicCacheName": cceBasicCacheName,
       "cceBasicFarmName": cceBasicFarmName,
       "cceDns": cceDns,
       "cceDnsDomain": cceDnsDomain,
       "cceDnsTable": cceDnsTable,
       "cceDnsEntry": cceDnsEntry,
       "cceDnsEntryIndex": cceDnsEntryIndex,
       "cceDnsEntryIpAddress": cceDnsEntryIpAddress,
       "cceIcpClient": cceIcpClient,
       "cceIcpClientEnabled": cceIcpClientEnabled,
       "cceIcpClientWait": cceIcpClientWait,
       "cceIcpClientRetry": cceIcpClientRetry,
       "cceIcpClientLocalDomains": cceIcpClientLocalDomains,
       "cceIcpClientRemServTable": cceIcpClientRemServTable,
       "cceIcpClientRemServEntry": cceIcpClientRemServEntry,
       "cceIcpClientRemServIndex": cceIcpClientRemServIndex,
       "cceIcpClientRemServIpAddress": cceIcpClientRemServIpAddress,
       "cceIcpClientRemServState": cceIcpClientRemServState,
       "cceIcpClientRemServType": cceIcpClientRemServType,
       "cceIcpClientRemServIcpPort": cceIcpClientRemServIcpPort,
       "cceIcpClientRemServHttpPort": cceIcpClientRemServHttpPort,
       "cceIcpClientRemServSelDomains": cceIcpClientRemServSelDomains,
       "cceIcpServer": cceIcpServer,
       "cceIcpServerEnabled": cceIcpServerEnabled,
       "cceIcpServerPort": cceIcpServerPort,
       "cceIcpServerRemClntTable": cceIcpServerRemClntTable,
       "cceIcpServerRemClntEntry": cceIcpServerRemClntEntry,
       "cceIcpServerRemClntIndex": cceIcpServerRemClntIndex,
       "cceIcpServerRemClntIPAddress": cceIcpServerRemClntIPAddress,
       "cceIcpServerRemClntFetch": cceIcpServerRemClntFetch,
       "cceProxy": cceProxy,
       "cceProxyIncomingPort": cceProxyIncomingPort,
       "cceProxyOutgoingAddress": cceProxyOutgoingAddress,
       "cceProxyOutgoingPort": cceProxyOutgoingPort,
       "cceTime": cceTime,
       "cceTimeGmtTime": cceTimeGmtTime,
       "cceTimeGmtDate": cceTimeGmtDate,
       "cceTimeTable": cceTimeTable,
       "cceTimeEntry": cceTimeEntry,
       "cceTimeEntryIndex": cceTimeEntryIndex,
       "cceTimeEntryIpAddress": cceTimeEntryIpAddress,
       "cceTuningGroup": cceTuningGroup,
       "cceCacheFarm": cceCacheFarm,
       "cceCacheFarmHealingModeWait": cceCacheFarmHealingModeWait,
       "cceCacheFarmHealingModeRetry": cceCacheFarmHealingModeRetry,
       "cceCacheFarmVersion": cceCacheFarmVersion,
       "cceFreshness": cceFreshness,
       "cceFreshnessTextAgeMultiplier": cceFreshnessTextAgeMultiplier,
       "cceFreshnessBinaryAgeMultiplier": cceFreshnessBinaryAgeMultiplier,
       "cceFreshnessTextMaximumTTL": cceFreshnessTextMaximumTTL,
       "cceFreshnessBinaryMaximumTTL": cceFreshnessBinaryMaximumTTL,
       "cceFreshnessUnitsMaximumTTL": cceFreshnessUnitsMaximumTTL,
       "cceFreshnessCacheCookies": cceFreshnessCacheCookies,
       "cceFreshnessTextMaxAge": cceFreshnessTextMaxAge,
       "cceFreshnessBinaryMaxAge": cceFreshnessBinaryMaxAge,
       "cceFreshnessForceMiss": cceFreshnessForceMiss,
       "cceTcp": cceTcp,
       "cceTcpServerSendBuffer": cceTcpServerSendBuffer,
       "cceTcpClientSendBuffer": cceTcpClientSendBuffer,
       "cceTcpServerRecvBuffer": cceTcpServerRecvBuffer,
       "cceTcpClientRecvBuffer": cceTcpClientRecvBuffer,
       "cceTcpServerReadWriteTimeout": cceTcpServerReadWriteTimeout,
       "cceTcpClientReadWriteTimeout": cceTcpClientReadWriteTimeout,
       "cceTcpConnectionIdleTimeout": cceTcpConnectionIdleTimeout,
       "cceTcpConnectionWaitTimeout": cceTcpConnectionWaitTimeout,
       "cceTcpConnectionRetry": cceTcpConnectionRetry,
       "cceAccessGroup": cceAccessGroup,
       "cceUrlFilter": cceUrlFilter,
       "cceUrlFilterState": cceUrlFilterState,
       "cceReportGroup": cceReportGroup,
       "cceEvents": cceEvents,
       "cceEventsTotal": cceEventsTotal,
       "cceEventsCritical": cceEventsCritical,
       "cceEventsWarning": cceEventsWarning,
       "cceEventsNotice": cceEventsNotice,
       "cceEventsTable": cceEventsTable,
       "cceEventsEntry": cceEventsEntry,
       "cceEventsEntryIndex": cceEventsEntryIndex,
       "cceEventsEntryType": cceEventsEntryType,
       "cceEventsEntryMessage": cceEventsEntryMessage,
       "cceEventsEntryTime": cceEventsEntryTime,
       "cceLogging": cceLogging,
       "cceLoggingEnabled": cceLoggingEnabled,
       "cceLoggingInterval": cceLoggingInterval,
       "cceLoggingWorkingLogPresent": cceLoggingWorkingLogPresent,
       "cceLoggingSize": cceLoggingSize,
       "cceLoggingAge": cceLoggingAge,
       "cceLoggingArchiveLogPresent": cceLoggingArchiveLogPresent,
       "cceLoggingArchiveLogSize": cceLoggingArchiveLogSize,
       "cceLoggingWriteFailReason": cceLoggingWriteFailReason,
       "cceStatsGroup": cceStatsGroup,
       "cceDiagDump": cceDiagDump,
       "cceDiagDumpDiskCreates": cceDiagDumpDiskCreates,
       "cceDiagDumpDiskOpens": cceDiagDumpDiskOpens,
       "cceDiagDumpDiskCloses": cceDiagDumpDiskCloses,
       "cceDiagDumpDiskDeletes": cceDiagDumpDiskDeletes,
       "cceDiagDumpDiskReads": cceDiagDumpDiskReads,
       "cceDiagDumpDiskWrites": cceDiagDumpDiskWrites,
       "cceDiagDumpDiskStats": cceDiagDumpDiskStats,
       "cceDiagDumpDiskFree": cceDiagDumpDiskFree,
       "cceDiagDumpDiskWraps": cceDiagDumpDiskWraps,
       "cceDiagDumpDiskOverWrites": cceDiagDumpDiskOverWrites,
       "cceDiagDumpDiskTruncReads": cceDiagDumpDiskTruncReads,
       "cceDiagDumpDiskInodeErrors": cceDiagDumpDiskInodeErrors,
       "cceDiagDumpDiskCrcErrors": cceDiagDumpDiskCrcErrors,
       "cceDiagDumpDiskDirCollisions": cceDiagDumpDiskDirCollisions,
       "cceDiagDumpBufferReads": cceDiagDumpBufferReads,
       "cceDiagDumpBufferReadErrors": cceDiagDumpBufferReadErrors,
       "cceDiagDumpBufferWrites": cceDiagDumpBufferWrites,
       "cceDiagDumpBufferWriteErrors": cceDiagDumpBufferWriteErrors,
       "cceDiagDumpBufferHits": cceDiagDumpBufferHits,
       "cceDiagDumpBufferMisses": cceDiagDumpBufferMisses,
       "cceDiagDumpBufferSeekErrors": cceDiagDumpBufferSeekErrors,
       "cceIms": cceIms,
       "cceImsClientRequestTotal": cceImsClientRequestTotal,
       "cceImsReceived": cceImsReceived,
       "cceImsClientTotalFromCache": cceImsClientTotalFromCache,
       "cceImsClientFreshFromCache": cceImsClientFreshFromCache,
       "cceImsClientStaleFromCache": cceImsClientStaleFromCache,
       "cceImsClientTotalCacheMiss": cceImsClientTotalCacheMiss,
       "cceImsClientFreshCacheMiss": cceImsClientFreshCacheMiss,
       "cceImsClientStaleCacheMiss": cceImsClientStaleCacheMiss,
       "cceImsClientTotalReval": cceImsClientTotalReval,
       "cceImsClientFreshReval": cceImsClientFreshReval,
       "cceImsClientStaleReval": cceImsClientStaleReval,
       "cceImsClientRequestToServer": cceImsClientRequestToServer,
       "cceImsServerTotalIssued": cceImsServerTotalIssued,
       "cceImsServerTotalDueClient": cceImsServerTotalDueClient,
       "cceImsServerFreshDueClient": cceImsServerFreshDueClient,
       "cceImsServerStaleDueClient": cceImsServerStaleDueClient,
       "cceImsServerTotalDueExpiration": cceImsServerTotalDueExpiration,
       "cceImsClientFreshDueExpiration": cceImsClientFreshDueExpiration,
       "cceImsServerStaleDueExpiration": cceImsServerStaleDueExpiration,
       "ccePerformance": ccePerformance,
       "ccePerformanceReqPerSecMax": ccePerformanceReqPerSecMax,
       "ccePerformanceReqPerSecLast": ccePerformanceReqPerSecLast,
       "ccePerformanceBytesPerSecMax": ccePerformanceBytesPerSecMax,
       "ccePerformanceBytesPerSecLast": ccePerformanceBytesPerSecLast,
       "ccePerformanceSecPerReqAvg": ccePerformanceSecPerReqAvg,
       "ccePerformanceSecPerReqMin": ccePerformanceSecPerReqMin,
       "ccePerformanceSecPerReqMax": ccePerformanceSecPerReqMax,
       "ccePerformanceSecPerReqLast": ccePerformanceSecPerReqLast,
       "ccePerformanceHitsSecPerReqAvg": ccePerformanceHitsSecPerReqAvg,
       "ccePerformanceHitsSecPerReqMin": ccePerformanceHitsSecPerReqMin,
       "ccePerformanceHitsSecPerReqMax": ccePerformanceHitsSecPerReqMax,
       "ccePerformanceHitsSecPerReqLast": ccePerformanceHitsSecPerReqLast,
       "ccePerformanceMissSecPerReqAvg": ccePerformanceMissSecPerReqAvg,
       "ccePerformanceMissSecPerReqMin": ccePerformanceMissSecPerReqMin,
       "ccePerformanceMissSecPerReqMax": ccePerformanceMissSecPerReqMax,
       "ccePerformanceMissSecPerReqLast": ccePerformanceMissSecPerReqLast,
       "ccePerformanceObjectSizeAvg": ccePerformanceObjectSizeAvg,
       "ccePerformanceObjectSizeMin": ccePerformanceObjectSizeMin,
       "ccePerformanceObjectSizeMax": ccePerformanceObjectSizeMax,
       "ccePerformanceObjectSizeLast": ccePerformanceObjectSizeLast,
       "cceRequests": cceRequests,
       "cceRequestsForcedReloadTotal": cceRequestsForcedReloadTotal,
       "cceRequestsForcedReloadPercent": cceRequestsForcedReloadPercent,
       "cceRequestsNearHitsTotal": cceRequestsNearHitsTotal,
       "cceRequestsNearHitsPercent": cceRequestsNearHitsPercent,
       "cceRequestsServerErrorTotal": cceRequestsServerErrorTotal,
       "cceRequestsServerErrorPercent": cceRequestsServerErrorPercent,
       "cceRequestsUrlBlockedTotal": cceRequestsUrlBlockedTotal,
       "cceRequestsUrlBlockedPercent": cceRequestsUrlBlockedPercent,
       "cceRequestsIcpClientHits": cceRequestsIcpClientHits,
       "cceRequestsIcpClientPercentage": cceRequestsIcpClientPercentage,
       "cceRequestsIcpServerHits": cceRequestsIcpServerHits,
       "cceRequestsIcpServerPercentage": cceRequestsIcpServerPercentage,
       "cceSavings": cceSavings,
       "cceSavingsRequestsTotal": cceSavingsRequestsTotal,
       "cceSavingsRequestsHits": cceSavingsRequestsHits,
       "cceSavingsRequestsMiss": cceSavingsRequestsMiss,
       "cceSavingsRequestsSavings": cceSavingsRequestsSavings,
       "cceSavingsBytesServedTotal": cceSavingsBytesServedTotal,
       "cceSavingsBytesServedHits": cceSavingsBytesServedHits,
       "cceSavingsBytesServedMiss": cceSavingsBytesServedMiss,
       "cceSavingsBytesServedSavings": cceSavingsBytesServedSavings,
       "cceUsage": cceUsage,
       "cceUsageCPUCurrent": cceUsageCPUCurrent,
       "cceUsageCPUPeak": cceUsageCPUPeak,
       "cceUsageDiskCurrent": cceUsageDiskCurrent,
       "cceUsageDiskPeak": cceUsageDiskPeak,
       "cceUsageNetCurrent": cceUsageNetCurrent,
       "cceUsageNetPeak": cceUsageNetPeak,
       "cceUsageConnsCurrent": cceUsageConnsCurrent,
       "cceUsageConnsPeak": cceUsageConnsPeak,
       "cceUsageDiskVolumeTable": cceUsageDiskVolumeTable,
       "cceUsageDiskVolumeEntry": cceUsageDiskVolumeEntry,
       "cceUsageDiskVolumeEntryIndex": cceUsageDiskVolumeEntryIndex,
       "cceUsageDiskVolumeName": cceUsageDiskVolumeName,
       "cceUsageDiskVolumeEverMounted": cceUsageDiskVolumeEverMounted,
       "cceUsageDiskVolumeCurrentlyMounted": cceUsageDiskVolumeCurrentlyMounted,
       "cceUsageDiskVolumeUnmountReason": cceUsageDiskVolumeUnmountReason,
       "cceUsageDiskVolumeCurrent": cceUsageDiskVolumeCurrent,
       "cceUsageDiskVolumePeak": cceUsageDiskVolumePeak,
       "cceUsageDosfsVolumeTable": cceUsageDosfsVolumeTable,
       "cceUsageDosfsVolumeEntry": cceUsageDosfsVolumeEntry,
       "cceUsageDosfsVolumeEntryIndex": cceUsageDosfsVolumeEntryIndex,
       "cceUsageDosfsVolumeName": cceUsageDosfsVolumeName,
       "cceUsageDosfsVolumeState": cceUsageDosfsVolumeState,
       "cceUsageDosfsVolumeFreeSpace": cceUsageDosfsVolumeFreeSpace,
       "cceUsageDosfsVolumeTotalSpace": cceUsageDosfsVolumeTotalSpace,
       "cceHardwareGroup": cceHardwareGroup,
       "cceInterfaces": cceInterfaces,
       "cceIfFullDuplex": cceIfFullDuplex,
       "ciscoCacheEngineMIBTrapPrefix": ciscoCacheEngineMIBTrapPrefix,
       "ciscoCacheEngineMIBTraps": ciscoCacheEngineMIBTraps,
       "cacheTrapReadDiskError": cacheTrapReadDiskError,
       "cacheTrapWriteDiskError": cacheTrapWriteDiskError,
       "cacheTrapWriteTransFailed": cacheTrapWriteTransFailed,
       "cacheTrapTooManyThreadsDead": cacheTrapTooManyThreadsDead,
       "cacheTrapWccpDisabled": cacheTrapWccpDisabled,
       "cacheTrapDiskVolUnmounted": cacheTrapDiskVolUnmounted,
       "cacheTrapDosfsVolFull": cacheTrapDosfsVolFull,
       "ciscoCacheEngineMIBConformance": ciscoCacheEngineMIBConformance,
       "ciscoCacheEngineMIBCompliances": ciscoCacheEngineMIBCompliances,
       "ciscoCacheEngineMIBCompliance": ciscoCacheEngineMIBCompliance,
       "ciscoCacheEngineMIBGroups": ciscoCacheEngineMIBGroups,
       "cceFarmGroup": cceFarmGroup,
       "cceBasicGroup": cceBasicGroup,
       "cceDnsGroup": cceDnsGroup,
       "cceIcpClientGroup": cceIcpClientGroup,
       "cceIcpServerGroup": cceIcpServerGroup,
       "cceProxyGroup": cceProxyGroup,
       "cceTimeGroup": cceTimeGroup,
       "cceCacheFarmGroup": cceCacheFarmGroup,
       "cceFreshGroup": cceFreshGroup,
       "cceTCPGroup": cceTCPGroup,
       "cceUrlGroup": cceUrlGroup,
       "cceEventsGroup": cceEventsGroup,
       "cceLogGroup": cceLogGroup,
       "cceDiagDumpGroup": cceDiagDumpGroup,
       "cceImsGroup": cceImsGroup,
       "ccePerfGroup": ccePerfGroup,
       "cceReqGroup": cceReqGroup,
       "cceSaveGroup": cceSaveGroup,
       "cceUsageGroup": cceUsageGroup,
       "cceInterfacesGroup": cceInterfacesGroup}
)
