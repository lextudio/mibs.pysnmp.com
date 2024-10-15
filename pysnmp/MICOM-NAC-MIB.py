# SNMP MIB module (MICOM-NAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-NAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:46 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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

_Micom_nac_ObjectIdentity = ObjectIdentity
micom_nac = _Micom_nac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15)
)
_Nac_configuration_ObjectIdentity = ObjectIdentity
nac_configuration = _Nac_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1)
)
_NacCfgGroup_ObjectIdentity = ObjectIdentity
nacCfgGroup = _NacCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1)
)


class _NacCfgAddressResolutionTriesNumber_Type(Integer32):
    """Custom type nacCfgAddressResolutionTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NacCfgAddressResolutionTriesNumber_Type.__name__ = "Integer32"
_NacCfgAddressResolutionTriesNumber_Object = MibScalar
nacCfgAddressResolutionTriesNumber = _NacCfgAddressResolutionTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 1),
    _NacCfgAddressResolutionTriesNumber_Type()
)
nacCfgAddressResolutionTriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCfgAddressResolutionTriesNumber.setStatus("mandatory")


class _NacCfgAddressResolutionTimeout_Type(Integer32):
    """Custom type nacCfgAddressResolutionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_NacCfgAddressResolutionTimeout_Type.__name__ = "Integer32"
_NacCfgAddressResolutionTimeout_Object = MibScalar
nacCfgAddressResolutionTimeout = _NacCfgAddressResolutionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 2),
    _NacCfgAddressResolutionTimeout_Type()
)
nacCfgAddressResolutionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCfgAddressResolutionTimeout.setStatus("mandatory")


class _NacCfgCacheStatus_Type(Integer32):
    """Custom type nacCfgCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("flush", 3))
    )


_NacCfgCacheStatus_Type.__name__ = "Integer32"
_NacCfgCacheStatus_Object = MibScalar
nacCfgCacheStatus = _NacCfgCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 3),
    _NacCfgCacheStatus_Type()
)
nacCfgCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCfgCacheStatus.setStatus("mandatory")


class _NacCfgNumberOfCacheEntries_Type(Integer32):
    """Custom type nacCfgNumberOfCacheEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_NacCfgNumberOfCacheEntries_Type.__name__ = "Integer32"
_NacCfgNumberOfCacheEntries_Object = MibScalar
nacCfgNumberOfCacheEntries = _NacCfgNumberOfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 4),
    _NacCfgNumberOfCacheEntries_Type()
)
nacCfgNumberOfCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacCfgNumberOfCacheEntries.setStatus("mandatory")


class _NacCfgCounterReset_Type(Integer32):
    """Custom type nacCfgCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_NacCfgCounterReset_Type.__name__ = "Integer32"
_NacCfgCounterReset_Object = MibScalar
nacCfgCounterReset = _NacCfgCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 5),
    _NacCfgCounterReset_Type()
)
nacCfgCounterReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nacCfgCounterReset.setStatus("obsolete")


class _NacCfgCustomerId_Type(Integer32):
    """Custom type nacCfgCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_NacCfgCustomerId_Type.__name__ = "Integer32"
_NacCfgCustomerId_Object = MibScalar
nacCfgCustomerId = _NacCfgCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 6),
    _NacCfgCustomerId_Type()
)
nacCfgCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacCfgCustomerId.setStatus("mandatory")
_NacCacheTable_Object = MibTable
nacCacheTable = _NacCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2)
)
if mibBuilder.loadTexts:
    nacCacheTable.setStatus("mandatory")
_NacCacheEntry_Object = MibTableRow
nacCacheEntry = _NacCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1)
)
nacCacheEntry.setIndexNames(
    (0, "MICOM-NAC-MIB", "nacCacheEgressString"),
)
if mibBuilder.loadTexts:
    nacCacheEntry.setStatus("mandatory")


class _NacCacheEgressString_Type(DisplayString):
    """Custom type nacCacheEgressString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NacCacheEgressString_Type.__name__ = "DisplayString"
_NacCacheEgressString_Object = MibTableColumn
nacCacheEgressString = _NacCacheEgressString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 1),
    _NacCacheEgressString_Type()
)
nacCacheEgressString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCacheEgressString.setStatus("mandatory")
_NacCacheServerIpAddress_Type = IpAddress
_NacCacheServerIpAddress_Object = MibTableColumn
nacCacheServerIpAddress = _NacCacheServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 2),
    _NacCacheServerIpAddress_Type()
)
nacCacheServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCacheServerIpAddress.setStatus("mandatory")


class _NacCacheDnaAddress_Type(DisplayString):
    """Custom type nacCacheDnaAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NacCacheDnaAddress_Type.__name__ = "DisplayString"
_NacCacheDnaAddress_Object = MibTableColumn
nacCacheDnaAddress = _NacCacheDnaAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 3),
    _NacCacheDnaAddress_Type()
)
nacCacheDnaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCacheDnaAddress.setStatus("mandatory")


class _NacCacheEntryType_Type(Integer32):
    """Custom type nacCacheEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learnt", 1),
          ("static", 2))
    )


_NacCacheEntryType_Type.__name__ = "Integer32"
_NacCacheEntryType_Object = MibTableColumn
nacCacheEntryType = _NacCacheEntryType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 4),
    _NacCacheEntryType_Type()
)
nacCacheEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacCacheEntryType.setStatus("mandatory")
_NacCacheNumberOfHits_Type = Integer32
_NacCacheNumberOfHits_Object = MibTableColumn
nacCacheNumberOfHits = _NacCacheNumberOfHits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 5),
    _NacCacheNumberOfHits_Type()
)
nacCacheNumberOfHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacCacheNumberOfHits.setStatus("mandatory")


class _NacCacheEntryStatus_Type(Integer32):
    """Custom type nacCacheEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NacCacheEntryStatus_Type.__name__ = "Integer32"
_NacCacheEntryStatus_Object = MibTableColumn
nacCacheEntryStatus = _NacCacheEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 6),
    _NacCacheEntryStatus_Type()
)
nacCacheEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacCacheEntryStatus.setStatus("mandatory")
_NacServerTable_Object = MibTable
nacServerTable = _NacServerTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3)
)
if mibBuilder.loadTexts:
    nacServerTable.setStatus("mandatory")
_NacServerEntry_Object = MibTableRow
nacServerEntry = _NacServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1)
)
nacServerEntry.setIndexNames(
    (0, "MICOM-NAC-MIB", "nacServerIpAddress"),
)
if mibBuilder.loadTexts:
    nacServerEntry.setStatus("mandatory")
_NacServerIpAddress_Type = IpAddress
_NacServerIpAddress_Object = MibTableColumn
nacServerIpAddress = _NacServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 1),
    _NacServerIpAddress_Type()
)
nacServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacServerIpAddress.setStatus("mandatory")


class _NacServerName_Type(DisplayString):
    """Custom type nacServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NacServerName_Type.__name__ = "DisplayString"
_NacServerName_Object = MibTableColumn
nacServerName = _NacServerName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 2),
    _NacServerName_Type()
)
nacServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacServerName.setStatus("mandatory")


class _NacServerAvailStatus_Type(Integer32):
    """Custom type nacServerAvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 3),
          ("transition", 2))
    )


_NacServerAvailStatus_Type.__name__ = "Integer32"
_NacServerAvailStatus_Object = MibTableColumn
nacServerAvailStatus = _NacServerAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 3),
    _NacServerAvailStatus_Type()
)
nacServerAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerAvailStatus.setStatus("mandatory")


class _NacServerStatus_Type(Integer32):
    """Custom type nacServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_NacServerStatus_Type.__name__ = "Integer32"
_NacServerStatus_Object = MibTableColumn
nacServerStatus = _NacServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 4),
    _NacServerStatus_Type()
)
nacServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacServerStatus.setStatus("mandatory")


class _NacServerHelloTime_Type(Integer32):
    """Custom type nacServerHelloTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 180),
    )


_NacServerHelloTime_Type.__name__ = "Integer32"
_NacServerHelloTime_Object = MibTableColumn
nacServerHelloTime = _NacServerHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 5),
    _NacServerHelloTime_Type()
)
nacServerHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacServerHelloTime.setStatus("mandatory")


class _NacServerType_Type(Integer32):
    """Custom type nacServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_NacServerType_Type.__name__ = "Integer32"
_NacServerType_Object = MibTableColumn
nacServerType = _NacServerType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 6),
    _NacServerType_Type()
)
nacServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nacServerType.setStatus("mandatory")
_NacServerRegistrationCount_Type = Counter32
_NacServerRegistrationCount_Object = MibTableColumn
nacServerRegistrationCount = _NacServerRegistrationCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 7),
    _NacServerRegistrationCount_Type()
)
nacServerRegistrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerRegistrationCount.setStatus("mandatory")
_NacServerHello1Count_Type = Counter32
_NacServerHello1Count_Object = MibTableColumn
nacServerHello1Count = _NacServerHello1Count_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 8),
    _NacServerHello1Count_Type()
)
nacServerHello1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerHello1Count.setStatus("mandatory")
_NacServerHello2Count_Type = Counter32
_NacServerHello2Count_Object = MibTableColumn
nacServerHello2Count = _NacServerHello2Count_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 9),
    _NacServerHello2Count_Type()
)
nacServerHello2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerHello2Count.setStatus("mandatory")
_NacServerHello3Count_Type = Counter32
_NacServerHello3Count_Object = MibTableColumn
nacServerHello3Count = _NacServerHello3Count_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 10),
    _NacServerHello3Count_Type()
)
nacServerHello3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerHello3Count.setStatus("mandatory")
_NacServerRequestCount_Type = Counter32
_NacServerRequestCount_Object = MibTableColumn
nacServerRequestCount = _NacServerRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 11),
    _NacServerRequestCount_Type()
)
nacServerRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerRequestCount.setStatus("mandatory")
_NacServerResolvedCount_Type = Counter32
_NacServerResolvedCount_Object = MibTableColumn
nacServerResolvedCount = _NacServerResolvedCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 12),
    _NacServerResolvedCount_Type()
)
nacServerResolvedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerResolvedCount.setStatus("mandatory")
_NacServerNoNumberCount_Type = Counter32
_NacServerNoNumberCount_Object = MibTableColumn
nacServerNoNumberCount = _NacServerNoNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 13),
    _NacServerNoNumberCount_Type()
)
nacServerNoNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerNoNumberCount.setStatus("mandatory")
_NacServerTimeoutCount_Type = Counter32
_NacServerTimeoutCount_Object = MibTableColumn
nacServerTimeoutCount = _NacServerTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 14),
    _NacServerTimeoutCount_Type()
)
nacServerTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacServerTimeoutCount.setStatus("mandatory")
_NvmNacCfgGroup_ObjectIdentity = ObjectIdentity
nvmNacCfgGroup = _NvmNacCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4)
)


class _NvmNacCfgAddressResolutionTriesNumber_Type(Integer32):
    """Custom type nvmNacCfgAddressResolutionTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmNacCfgAddressResolutionTriesNumber_Type.__name__ = "Integer32"
_NvmNacCfgAddressResolutionTriesNumber_Object = MibScalar
nvmNacCfgAddressResolutionTriesNumber = _NvmNacCfgAddressResolutionTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 1),
    _NvmNacCfgAddressResolutionTriesNumber_Type()
)
nvmNacCfgAddressResolutionTriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacCfgAddressResolutionTriesNumber.setStatus("mandatory")


class _NvmNacCfgAddressResolutionTimeout_Type(Integer32):
    """Custom type nvmNacCfgAddressResolutionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_NvmNacCfgAddressResolutionTimeout_Type.__name__ = "Integer32"
_NvmNacCfgAddressResolutionTimeout_Object = MibScalar
nvmNacCfgAddressResolutionTimeout = _NvmNacCfgAddressResolutionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 2),
    _NvmNacCfgAddressResolutionTimeout_Type()
)
nvmNacCfgAddressResolutionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacCfgAddressResolutionTimeout.setStatus("mandatory")


class _NvmNacCfgCacheStatus_Type(Integer32):
    """Custom type nvmNacCfgCacheStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmNacCfgCacheStatus_Type.__name__ = "Integer32"
_NvmNacCfgCacheStatus_Object = MibScalar
nvmNacCfgCacheStatus = _NvmNacCfgCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 3),
    _NvmNacCfgCacheStatus_Type()
)
nvmNacCfgCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacCfgCacheStatus.setStatus("mandatory")


class _NvmNacCfgNumberOfCacheEntries_Type(Integer32):
    """Custom type nvmNacCfgNumberOfCacheEntries based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_NvmNacCfgNumberOfCacheEntries_Type.__name__ = "Integer32"
_NvmNacCfgNumberOfCacheEntries_Object = MibScalar
nvmNacCfgNumberOfCacheEntries = _NvmNacCfgNumberOfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 4),
    _NvmNacCfgNumberOfCacheEntries_Type()
)
nvmNacCfgNumberOfCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmNacCfgNumberOfCacheEntries.setStatus("mandatory")


class _NvmNacCfgCustomerId_Type(Integer32):
    """Custom type nvmNacCfgCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_NvmNacCfgCustomerId_Type.__name__ = "Integer32"
_NvmNacCfgCustomerId_Object = MibScalar
nvmNacCfgCustomerId = _NvmNacCfgCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 5),
    _NvmNacCfgCustomerId_Type()
)
nvmNacCfgCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmNacCfgCustomerId.setStatus("mandatory")
_NvmNacCacheTable_Object = MibTable
nvmNacCacheTable = _NvmNacCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5)
)
if mibBuilder.loadTexts:
    nvmNacCacheTable.setStatus("mandatory")
_NvmNacCacheEntry_Object = MibTableRow
nvmNacCacheEntry = _NvmNacCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1)
)
nvmNacCacheEntry.setIndexNames(
    (0, "MICOM-NAC-MIB", "nvmNacCacheEgressNumber"),
)
if mibBuilder.loadTexts:
    nvmNacCacheEntry.setStatus("mandatory")


class _NvmNacCacheEgressNumber_Type(DisplayString):
    """Custom type nvmNacCacheEgressNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NvmNacCacheEgressNumber_Type.__name__ = "DisplayString"
_NvmNacCacheEgressNumber_Object = MibTableColumn
nvmNacCacheEgressNumber = _NvmNacCacheEgressNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1, 1),
    _NvmNacCacheEgressNumber_Type()
)
nvmNacCacheEgressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacCacheEgressNumber.setStatus("mandatory")
_NvmNacCacheServerIpAddress_Type = IpAddress
_NvmNacCacheServerIpAddress_Object = MibTableColumn
nvmNacCacheServerIpAddress = _NvmNacCacheServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1, 2),
    _NvmNacCacheServerIpAddress_Type()
)
nvmNacCacheServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacCacheServerIpAddress.setStatus("mandatory")


class _NvmNacCacheDnaAddress_Type(DisplayString):
    """Custom type nvmNacCacheDnaAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmNacCacheDnaAddress_Type.__name__ = "DisplayString"
_NvmNacCacheDnaAddress_Object = MibTableColumn
nvmNacCacheDnaAddress = _NvmNacCacheDnaAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1, 3),
    _NvmNacCacheDnaAddress_Type()
)
nvmNacCacheDnaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacCacheDnaAddress.setStatus("mandatory")
_NvmNacServerTable_Object = MibTable
nvmNacServerTable = _NvmNacServerTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6)
)
if mibBuilder.loadTexts:
    nvmNacServerTable.setStatus("mandatory")
_NvmNacServerEntry_Object = MibTableRow
nvmNacServerEntry = _NvmNacServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1)
)
nvmNacServerEntry.setIndexNames(
    (0, "MICOM-NAC-MIB", "nvmNacServerIpAddress"),
)
if mibBuilder.loadTexts:
    nvmNacServerEntry.setStatus("mandatory")
_NvmNacServerIpAddress_Type = IpAddress
_NvmNacServerIpAddress_Object = MibTableColumn
nvmNacServerIpAddress = _NvmNacServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 1),
    _NvmNacServerIpAddress_Type()
)
nvmNacServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacServerIpAddress.setStatus("mandatory")


class _NvmNacServerName_Type(DisplayString):
    """Custom type nvmNacServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NvmNacServerName_Type.__name__ = "DisplayString"
_NvmNacServerName_Object = MibTableColumn
nvmNacServerName = _NvmNacServerName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 2),
    _NvmNacServerName_Type()
)
nvmNacServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacServerName.setStatus("mandatory")


class _NvmNacServerStatus_Type(Integer32):
    """Custom type nvmNacServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NvmNacServerStatus_Type.__name__ = "Integer32"
_NvmNacServerStatus_Object = MibTableColumn
nvmNacServerStatus = _NvmNacServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 3),
    _NvmNacServerStatus_Type()
)
nvmNacServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacServerStatus.setStatus("mandatory")


class _NvmNacServerHelloTime_Type(Integer32):
    """Custom type nvmNacServerHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 180),
    )


_NvmNacServerHelloTime_Type.__name__ = "Integer32"
_NvmNacServerHelloTime_Object = MibTableColumn
nvmNacServerHelloTime = _NvmNacServerHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 4),
    _NvmNacServerHelloTime_Type()
)
nvmNacServerHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacServerHelloTime.setStatus("mandatory")


class _NvmNacServerType_Type(Integer32):
    """Custom type nvmNacServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_NvmNacServerType_Type.__name__ = "Integer32"
_NvmNacServerType_Object = MibTableColumn
nvmNacServerType = _NvmNacServerType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 5),
    _NvmNacServerType_Type()
)
nvmNacServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmNacServerType.setStatus("mandatory")
_Nac_statistics_ObjectIdentity = ObjectIdentity
nac_statistics = _Nac_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2)
)
_NacStatisticsGroup_ObjectIdentity = ObjectIdentity
nacStatisticsGroup = _NacStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1)
)
_NacStatisticsCacheCount_Type = Counter32
_NacStatisticsCacheCount_Object = MibScalar
nacStatisticsCacheCount = _NacStatisticsCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 1),
    _NacStatisticsCacheCount_Type()
)
nacStatisticsCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsCacheCount.setStatus("mandatory")
_NacStatisticsStaticCount_Type = Counter32
_NacStatisticsStaticCount_Object = MibScalar
nacStatisticsStaticCount = _NacStatisticsStaticCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 2),
    _NacStatisticsStaticCount_Type()
)
nacStatisticsStaticCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsStaticCount.setStatus("mandatory")
_NacStatisticsRequestAllCount_Type = Counter32
_NacStatisticsRequestAllCount_Object = MibScalar
nacStatisticsRequestAllCount = _NacStatisticsRequestAllCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 3),
    _NacStatisticsRequestAllCount_Type()
)
nacStatisticsRequestAllCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsRequestAllCount.setStatus("mandatory")
_NacStatisticsLocalResolvedCount_Type = Counter32
_NacStatisticsLocalResolvedCount_Object = MibScalar
nacStatisticsLocalResolvedCount = _NacStatisticsLocalResolvedCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 4),
    _NacStatisticsLocalResolvedCount_Type()
)
nacStatisticsLocalResolvedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsLocalResolvedCount.setStatus("mandatory")
_NacStatisticsPurgeCount_Type = Counter32
_NacStatisticsPurgeCount_Object = MibScalar
nacStatisticsPurgeCount = _NacStatisticsPurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 5),
    _NacStatisticsPurgeCount_Type()
)
nacStatisticsPurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsPurgeCount.setStatus("mandatory")
_NacStatisticsVoiceRegCount_Type = Counter32
_NacStatisticsVoiceRegCount_Object = MibScalar
nacStatisticsVoiceRegCount = _NacStatisticsVoiceRegCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 6),
    _NacStatisticsVoiceRegCount_Type()
)
nacStatisticsVoiceRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsVoiceRegCount.setStatus("mandatory")
_NacStatisticsDNAChangeCount_Type = Counter32
_NacStatisticsDNAChangeCount_Object = MibScalar
nacStatisticsDNAChangeCount = _NacStatisticsDNAChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 7),
    _NacStatisticsDNAChangeCount_Type()
)
nacStatisticsDNAChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsDNAChangeCount.setStatus("mandatory")
_NacStatisticsServerCount_Type = Counter32
_NacStatisticsServerCount_Object = MibScalar
nacStatisticsServerCount = _NacStatisticsServerCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 8),
    _NacStatisticsServerCount_Type()
)
nacStatisticsServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsServerCount.setStatus("mandatory")
_NacStatisticsServerRequestCount_Type = Counter32
_NacStatisticsServerRequestCount_Object = MibScalar
nacStatisticsServerRequestCount = _NacStatisticsServerRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 9),
    _NacStatisticsServerRequestCount_Type()
)
nacStatisticsServerRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsServerRequestCount.setStatus("mandatory")
_NacStatisticsServerResolvedCount_Type = Counter32
_NacStatisticsServerResolvedCount_Object = MibScalar
nacStatisticsServerResolvedCount = _NacStatisticsServerResolvedCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 10),
    _NacStatisticsServerResolvedCount_Type()
)
nacStatisticsServerResolvedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsServerResolvedCount.setStatus("mandatory")
_NacStatisticsServerNoNumberCount_Type = Counter32
_NacStatisticsServerNoNumberCount_Object = MibScalar
nacStatisticsServerNoNumberCount = _NacStatisticsServerNoNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 11),
    _NacStatisticsServerNoNumberCount_Type()
)
nacStatisticsServerNoNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsServerNoNumberCount.setStatus("mandatory")
_NacStatisticsTimeoutCount_Type = Counter32
_NacStatisticsTimeoutCount_Object = MibScalar
nacStatisticsTimeoutCount = _NacStatisticsTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 12),
    _NacStatisticsTimeoutCount_Type()
)
nacStatisticsTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsTimeoutCount.setStatus("mandatory")
_NacStatisticsHello1Count_Type = Counter32
_NacStatisticsHello1Count_Object = MibScalar
nacStatisticsHello1Count = _NacStatisticsHello1Count_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 13),
    _NacStatisticsHello1Count_Type()
)
nacStatisticsHello1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsHello1Count.setStatus("mandatory")
_NacStatisticsHello2Count_Type = Counter32
_NacStatisticsHello2Count_Object = MibScalar
nacStatisticsHello2Count = _NacStatisticsHello2Count_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 14),
    _NacStatisticsHello2Count_Type()
)
nacStatisticsHello2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsHello2Count.setStatus("mandatory")
_NacStatisticsHello3Count_Type = Counter32
_NacStatisticsHello3Count_Object = MibScalar
nacStatisticsHello3Count = _NacStatisticsHello3Count_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 15),
    _NacStatisticsHello3Count_Type()
)
nacStatisticsHello3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsHello3Count.setStatus("mandatory")
_NacStatisticsRegistrationCount_Type = Counter32
_NacStatisticsRegistrationCount_Object = MibScalar
nacStatisticsRegistrationCount = _NacStatisticsRegistrationCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 16),
    _NacStatisticsRegistrationCount_Type()
)
nacStatisticsRegistrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nacStatisticsRegistrationCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmAlarmNacFailedToLocateNAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 0, 1)
)
mcmAlarmNacFailedToLocateNAS.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmAlarmNacFailedToLocateNAS.setStatus(
        ""
    )

mcmAlarmNacNASIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 0, 2)
)
mcmAlarmNacNASIsDown.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-NAC-MIB", "nacServerIpAddress"))
)
if mibBuilder.loadTexts:
    mcmAlarmNacNASIsDown.setStatus(
        ""
    )

mcmAlarmNacNASIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 0, 3)
)
mcmAlarmNacNASIsUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-NAC-MIB", "nacServerIpAddress"))
)
if mibBuilder.loadTexts:
    mcmAlarmNacNASIsUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-NAC-MIB",
    **{"micom-nac": micom_nac,
       "mcmAlarmNacFailedToLocateNAS": mcmAlarmNacFailedToLocateNAS,
       "mcmAlarmNacNASIsDown": mcmAlarmNacNASIsDown,
       "mcmAlarmNacNASIsUp": mcmAlarmNacNASIsUp,
       "nac-configuration": nac_configuration,
       "nacCfgGroup": nacCfgGroup,
       "nacCfgAddressResolutionTriesNumber": nacCfgAddressResolutionTriesNumber,
       "nacCfgAddressResolutionTimeout": nacCfgAddressResolutionTimeout,
       "nacCfgCacheStatus": nacCfgCacheStatus,
       "nacCfgNumberOfCacheEntries": nacCfgNumberOfCacheEntries,
       "nacCfgCounterReset": nacCfgCounterReset,
       "nacCfgCustomerId": nacCfgCustomerId,
       "nacCacheTable": nacCacheTable,
       "nacCacheEntry": nacCacheEntry,
       "nacCacheEgressString": nacCacheEgressString,
       "nacCacheServerIpAddress": nacCacheServerIpAddress,
       "nacCacheDnaAddress": nacCacheDnaAddress,
       "nacCacheEntryType": nacCacheEntryType,
       "nacCacheNumberOfHits": nacCacheNumberOfHits,
       "nacCacheEntryStatus": nacCacheEntryStatus,
       "nacServerTable": nacServerTable,
       "nacServerEntry": nacServerEntry,
       "nacServerIpAddress": nacServerIpAddress,
       "nacServerName": nacServerName,
       "nacServerAvailStatus": nacServerAvailStatus,
       "nacServerStatus": nacServerStatus,
       "nacServerHelloTime": nacServerHelloTime,
       "nacServerType": nacServerType,
       "nacServerRegistrationCount": nacServerRegistrationCount,
       "nacServerHello1Count": nacServerHello1Count,
       "nacServerHello2Count": nacServerHello2Count,
       "nacServerHello3Count": nacServerHello3Count,
       "nacServerRequestCount": nacServerRequestCount,
       "nacServerResolvedCount": nacServerResolvedCount,
       "nacServerNoNumberCount": nacServerNoNumberCount,
       "nacServerTimeoutCount": nacServerTimeoutCount,
       "nvmNacCfgGroup": nvmNacCfgGroup,
       "nvmNacCfgAddressResolutionTriesNumber": nvmNacCfgAddressResolutionTriesNumber,
       "nvmNacCfgAddressResolutionTimeout": nvmNacCfgAddressResolutionTimeout,
       "nvmNacCfgCacheStatus": nvmNacCfgCacheStatus,
       "nvmNacCfgNumberOfCacheEntries": nvmNacCfgNumberOfCacheEntries,
       "nvmNacCfgCustomerId": nvmNacCfgCustomerId,
       "nvmNacCacheTable": nvmNacCacheTable,
       "nvmNacCacheEntry": nvmNacCacheEntry,
       "nvmNacCacheEgressNumber": nvmNacCacheEgressNumber,
       "nvmNacCacheServerIpAddress": nvmNacCacheServerIpAddress,
       "nvmNacCacheDnaAddress": nvmNacCacheDnaAddress,
       "nvmNacServerTable": nvmNacServerTable,
       "nvmNacServerEntry": nvmNacServerEntry,
       "nvmNacServerIpAddress": nvmNacServerIpAddress,
       "nvmNacServerName": nvmNacServerName,
       "nvmNacServerStatus": nvmNacServerStatus,
       "nvmNacServerHelloTime": nvmNacServerHelloTime,
       "nvmNacServerType": nvmNacServerType,
       "nac-statistics": nac_statistics,
       "nacStatisticsGroup": nacStatisticsGroup,
       "nacStatisticsCacheCount": nacStatisticsCacheCount,
       "nacStatisticsStaticCount": nacStatisticsStaticCount,
       "nacStatisticsRequestAllCount": nacStatisticsRequestAllCount,
       "nacStatisticsLocalResolvedCount": nacStatisticsLocalResolvedCount,
       "nacStatisticsPurgeCount": nacStatisticsPurgeCount,
       "nacStatisticsVoiceRegCount": nacStatisticsVoiceRegCount,
       "nacStatisticsDNAChangeCount": nacStatisticsDNAChangeCount,
       "nacStatisticsServerCount": nacStatisticsServerCount,
       "nacStatisticsServerRequestCount": nacStatisticsServerRequestCount,
       "nacStatisticsServerResolvedCount": nacStatisticsServerResolvedCount,
       "nacStatisticsServerNoNumberCount": nacStatisticsServerNoNumberCount,
       "nacStatisticsTimeoutCount": nacStatisticsTimeoutCount,
       "nacStatisticsHello1Count": nacStatisticsHello1Count,
       "nacStatisticsHello2Count": nacStatisticsHello2Count,
       "nacStatisticsHello3Count": nacStatisticsHello3Count,
       "nacStatisticsRegistrationCount": nacStatisticsRegistrationCount}
)
