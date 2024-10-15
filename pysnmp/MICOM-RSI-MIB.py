# SNMP MIB module (MICOM-RSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-RSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:50 2024
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

_Micom_rsi_ObjectIdentity = ObjectIdentity
micom_rsi = _Micom_rsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23)
)
_Rsi_configuration_ObjectIdentity = ObjectIdentity
rsi_configuration = _Rsi_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1)
)
_McmRSISysCfgDefGroup_ObjectIdentity = ObjectIdentity
mcmRSISysCfgDefGroup = _McmRSISysCfgDefGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 1)
)


class _McmRSISysCfgDefVNCSInstance_Type(Integer32):
    """Custom type mcmRSISysCfgDefVNCSInstance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmRSISysCfgDefVNCSInstance_Type.__name__ = "Integer32"
_McmRSISysCfgDefVNCSInstance_Object = MibScalar
mcmRSISysCfgDefVNCSInstance = _McmRSISysCfgDefVNCSInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 1, 1),
    _McmRSISysCfgDefVNCSInstance_Type()
)
mcmRSISysCfgDefVNCSInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSISysCfgDefVNCSInstance.setStatus("mandatory")


class _McmRSISysCfgDefNumCacheEntries_Type(Integer32):
    """Custom type mcmRSISysCfgDefNumCacheEntries based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_McmRSISysCfgDefNumCacheEntries_Type.__name__ = "Integer32"
_McmRSISysCfgDefNumCacheEntries_Object = MibScalar
mcmRSISysCfgDefNumCacheEntries = _McmRSISysCfgDefNumCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 1, 2),
    _McmRSISysCfgDefNumCacheEntries_Type()
)
mcmRSISysCfgDefNumCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSISysCfgDefNumCacheEntries.setStatus("mandatory")
_McmRSISysCfgSetGroup_ObjectIdentity = ObjectIdentity
mcmRSISysCfgSetGroup = _McmRSISysCfgSetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 2)
)


class _McmRSISysCfgSetAddrResRetries_Type(Integer32):
    """Custom type mcmRSISysCfgSetAddrResRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmRSISysCfgSetAddrResRetries_Type.__name__ = "Integer32"
_McmRSISysCfgSetAddrResRetries_Object = MibScalar
mcmRSISysCfgSetAddrResRetries = _McmRSISysCfgSetAddrResRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 2, 1),
    _McmRSISysCfgSetAddrResRetries_Type()
)
mcmRSISysCfgSetAddrResRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmRSISysCfgSetAddrResRetries.setStatus("mandatory")


class _McmRSISysCfgSetAddrResTimeout_Type(Integer32):
    """Custom type mcmRSISysCfgSetAddrResTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_McmRSISysCfgSetAddrResTimeout_Type.__name__ = "Integer32"
_McmRSISysCfgSetAddrResTimeout_Object = MibScalar
mcmRSISysCfgSetAddrResTimeout = _McmRSISysCfgSetAddrResTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 2, 2),
    _McmRSISysCfgSetAddrResTimeout_Type()
)
mcmRSISysCfgSetAddrResTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmRSISysCfgSetAddrResTimeout.setStatus("mandatory")


class _McmRSISysCfgSetAddrCacheStatus_Type(Integer32):
    """Custom type mcmRSISysCfgSetAddrCacheStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("flush", 3))
    )


_McmRSISysCfgSetAddrCacheStatus_Type.__name__ = "Integer32"
_McmRSISysCfgSetAddrCacheStatus_Object = MibScalar
mcmRSISysCfgSetAddrCacheStatus = _McmRSISysCfgSetAddrCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 2, 3),
    _McmRSISysCfgSetAddrCacheStatus_Type()
)
mcmRSISysCfgSetAddrCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmRSISysCfgSetAddrCacheStatus.setStatus("mandatory")
_McmRSICacheCfgTable_Object = MibTable
mcmRSICacheCfgTable = _McmRSICacheCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3)
)
if mibBuilder.loadTexts:
    mcmRSICacheCfgTable.setStatus("mandatory")
_McmRSICacheCfgEntry_Object = MibTableRow
mcmRSICacheCfgEntry = _McmRSICacheCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3, 1)
)
mcmRSICacheCfgEntry.setIndexNames(
    (0, "MICOM-RSI-MIB", "mcmRSICacheCfgDNDigits"),
)
if mibBuilder.loadTexts:
    mcmRSICacheCfgEntry.setStatus("mandatory")


class _McmRSICacheCfgDNDigits_Type(DisplayString):
    """Custom type mcmRSICacheCfgDNDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_McmRSICacheCfgDNDigits_Type.__name__ = "DisplayString"
_McmRSICacheCfgDNDigits_Object = MibTableColumn
mcmRSICacheCfgDNDigits = _McmRSICacheCfgDNDigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3, 1, 1),
    _McmRSICacheCfgDNDigits_Type()
)
mcmRSICacheCfgDNDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSICacheCfgDNDigits.setStatus("mandatory")


class _McmRSICacheCfgDNAAddr_Type(DisplayString):
    """Custom type mcmRSICacheCfgDNAAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_McmRSICacheCfgDNAAddr_Type.__name__ = "DisplayString"
_McmRSICacheCfgDNAAddr_Object = MibTableColumn
mcmRSICacheCfgDNAAddr = _McmRSICacheCfgDNAAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3, 1, 2),
    _McmRSICacheCfgDNAAddr_Type()
)
mcmRSICacheCfgDNAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSICacheCfgDNAAddr.setStatus("mandatory")


class _McmRSICacheCfgProfileNumber_Type(Integer32):
    """Custom type mcmRSICacheCfgProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmRSICacheCfgProfileNumber_Type.__name__ = "Integer32"
_McmRSICacheCfgProfileNumber_Object = MibTableColumn
mcmRSICacheCfgProfileNumber = _McmRSICacheCfgProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3, 1, 3),
    _McmRSICacheCfgProfileNumber_Type()
)
mcmRSICacheCfgProfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSICacheCfgProfileNumber.setStatus("mandatory")
_McmRSICacheCfgNumberOfHits_Type = Counter32
_McmRSICacheCfgNumberOfHits_Object = MibTableColumn
mcmRSICacheCfgNumberOfHits = _McmRSICacheCfgNumberOfHits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3, 1, 4),
    _McmRSICacheCfgNumberOfHits_Type()
)
mcmRSICacheCfgNumberOfHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSICacheCfgNumberOfHits.setStatus("mandatory")


class _McmRSICacheCfgServerDNA_Type(DisplayString):
    """Custom type mcmRSICacheCfgServerDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_McmRSICacheCfgServerDNA_Type.__name__ = "DisplayString"
_McmRSICacheCfgServerDNA_Object = MibTableColumn
mcmRSICacheCfgServerDNA = _McmRSICacheCfgServerDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 3, 1, 5),
    _McmRSICacheCfgServerDNA_Type()
)
mcmRSICacheCfgServerDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSICacheCfgServerDNA.setStatus("mandatory")
_McmRSIServerTable_Object = MibTable
mcmRSIServerTable = _McmRSIServerTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4)
)
if mibBuilder.loadTexts:
    mcmRSIServerTable.setStatus("mandatory")
_McmRSIServerEntry_Object = MibTableRow
mcmRSIServerEntry = _McmRSIServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1)
)
mcmRSIServerEntry.setIndexNames(
    (0, "MICOM-RSI-MIB", "mcmRSIServerDNAAddr"),
)
if mibBuilder.loadTexts:
    mcmRSIServerEntry.setStatus("mandatory")


class _McmRSIServerDNAAddr_Type(DisplayString):
    """Custom type mcmRSIServerDNAAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_McmRSIServerDNAAddr_Type.__name__ = "DisplayString"
_McmRSIServerDNAAddr_Object = MibTableColumn
mcmRSIServerDNAAddr = _McmRSIServerDNAAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 1),
    _McmRSIServerDNAAddr_Type()
)
mcmRSIServerDNAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerDNAAddr.setStatus("mandatory")


class _McmRSIServerName_Type(DisplayString):
    """Custom type mcmRSIServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_McmRSIServerName_Type.__name__ = "DisplayString"
_McmRSIServerName_Object = MibTableColumn
mcmRSIServerName = _McmRSIServerName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 2),
    _McmRSIServerName_Type()
)
mcmRSIServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerName.setStatus("mandatory")


class _McmRSIServerType_Type(Integer32):
    """Custom type mcmRSIServerType based on Integer32"""
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


_McmRSIServerType_Type.__name__ = "Integer32"
_McmRSIServerType_Object = MibTableColumn
mcmRSIServerType = _McmRSIServerType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 3),
    _McmRSIServerType_Type()
)
mcmRSIServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerType.setStatus("mandatory")
_McmRSIServerPortID_Type = Integer32
_McmRSIServerPortID_Object = MibTableColumn
mcmRSIServerPortID = _McmRSIServerPortID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 4),
    _McmRSIServerPortID_Type()
)
mcmRSIServerPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerPortID.setStatus("mandatory")


class _McmRSIServerDLCI_Type(Integer32):
    """Custom type mcmRSIServerDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmRSIServerDLCI_Type.__name__ = "Integer32"
_McmRSIServerDLCI_Object = MibTableColumn
mcmRSIServerDLCI = _McmRSIServerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 5),
    _McmRSIServerDLCI_Type()
)
mcmRSIServerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerDLCI.setStatus("mandatory")


class _McmRSIServerAvailStatus_Type(Integer32):
    """Custom type mcmRSIServerAvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_McmRSIServerAvailStatus_Type.__name__ = "Integer32"
_McmRSIServerAvailStatus_Object = MibTableColumn
mcmRSIServerAvailStatus = _McmRSIServerAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 6),
    _McmRSIServerAvailStatus_Type()
)
mcmRSIServerAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerAvailStatus.setStatus("mandatory")


class _McmRSIServerLastDisconnectCause_Type(DisplayString):
    """Custom type mcmRSIServerLastDisconnectCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_McmRSIServerLastDisconnectCause_Type.__name__ = "DisplayString"
_McmRSIServerLastDisconnectCause_Object = MibTableColumn
mcmRSIServerLastDisconnectCause = _McmRSIServerLastDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 7),
    _McmRSIServerLastDisconnectCause_Type()
)
mcmRSIServerLastDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerLastDisconnectCause.setStatus("mandatory")
_McmRSIServerRequestCount_Type = Counter32
_McmRSIServerRequestCount_Object = MibTableColumn
mcmRSIServerRequestCount = _McmRSIServerRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 8),
    _McmRSIServerRequestCount_Type()
)
mcmRSIServerRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerRequestCount.setStatus("mandatory")
_McmRSIServerResolvedCount_Type = Counter32
_McmRSIServerResolvedCount_Object = MibTableColumn
mcmRSIServerResolvedCount = _McmRSIServerResolvedCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 9),
    _McmRSIServerResolvedCount_Type()
)
mcmRSIServerResolvedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerResolvedCount.setStatus("mandatory")
_McmRSIServerNoNumberCount_Type = Counter32
_McmRSIServerNoNumberCount_Object = MibTableColumn
mcmRSIServerNoNumberCount = _McmRSIServerNoNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 10),
    _McmRSIServerNoNumberCount_Type()
)
mcmRSIServerNoNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerNoNumberCount.setStatus("mandatory")
_McmRSIServerTimeoutCount_Type = Counter32
_McmRSIServerTimeoutCount_Object = MibTableColumn
mcmRSIServerTimeoutCount = _McmRSIServerTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 11),
    _McmRSIServerTimeoutCount_Type()
)
mcmRSIServerTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerTimeoutCount.setStatus("mandatory")
_McmRSIServerRecoveryCount_Type = Counter32
_McmRSIServerRecoveryCount_Object = MibTableColumn
mcmRSIServerRecoveryCount = _McmRSIServerRecoveryCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 4, 1, 12),
    _McmRSIServerRecoveryCount_Type()
)
mcmRSIServerRecoveryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIServerRecoveryCount.setStatus("mandatory")
_NvmRSISysCfgDefGroup_ObjectIdentity = ObjectIdentity
nvmRSISysCfgDefGroup = _NvmRSISysCfgDefGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 5)
)


class _NvmRSISysCfgDefVNCSInstance_Type(Integer32):
    """Custom type nvmRSISysCfgDefVNCSInstance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmRSISysCfgDefVNCSInstance_Type.__name__ = "Integer32"
_NvmRSISysCfgDefVNCSInstance_Object = MibScalar
nvmRSISysCfgDefVNCSInstance = _NvmRSISysCfgDefVNCSInstance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 5, 1),
    _NvmRSISysCfgDefVNCSInstance_Type()
)
nvmRSISysCfgDefVNCSInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmRSISysCfgDefVNCSInstance.setStatus("mandatory")


class _NvmRSISysCfgDefNumCacheEntries_Type(Integer32):
    """Custom type nvmRSISysCfgDefNumCacheEntries based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_NvmRSISysCfgDefNumCacheEntries_Type.__name__ = "Integer32"
_NvmRSISysCfgDefNumCacheEntries_Object = MibScalar
nvmRSISysCfgDefNumCacheEntries = _NvmRSISysCfgDefNumCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 5, 2),
    _NvmRSISysCfgDefNumCacheEntries_Type()
)
nvmRSISysCfgDefNumCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmRSISysCfgDefNumCacheEntries.setStatus("mandatory")
_NvmRSISysCfgSetGroup_ObjectIdentity = ObjectIdentity
nvmRSISysCfgSetGroup = _NvmRSISysCfgSetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 6)
)


class _NvmRSISysCfgSetAddrResRetries_Type(Integer32):
    """Custom type nvmRSISysCfgSetAddrResRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmRSISysCfgSetAddrResRetries_Type.__name__ = "Integer32"
_NvmRSISysCfgSetAddrResRetries_Object = MibScalar
nvmRSISysCfgSetAddrResRetries = _NvmRSISysCfgSetAddrResRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 6, 1),
    _NvmRSISysCfgSetAddrResRetries_Type()
)
nvmRSISysCfgSetAddrResRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmRSISysCfgSetAddrResRetries.setStatus("mandatory")


class _NvmRSISysCfgSetAddrResTimeout_Type(Integer32):
    """Custom type nvmRSISysCfgSetAddrResTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_NvmRSISysCfgSetAddrResTimeout_Type.__name__ = "Integer32"
_NvmRSISysCfgSetAddrResTimeout_Object = MibScalar
nvmRSISysCfgSetAddrResTimeout = _NvmRSISysCfgSetAddrResTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 6, 2),
    _NvmRSISysCfgSetAddrResTimeout_Type()
)
nvmRSISysCfgSetAddrResTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmRSISysCfgSetAddrResTimeout.setStatus("mandatory")


class _NvmRSISysCfgSetAddrCacheStatus_Type(Integer32):
    """Custom type nvmRSISysCfgSetAddrCacheStatus based on Integer32"""
    defaultValue = 2

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


_NvmRSISysCfgSetAddrCacheStatus_Type.__name__ = "Integer32"
_NvmRSISysCfgSetAddrCacheStatus_Object = MibScalar
nvmRSISysCfgSetAddrCacheStatus = _NvmRSISysCfgSetAddrCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 6, 3),
    _NvmRSISysCfgSetAddrCacheStatus_Type()
)
nvmRSISysCfgSetAddrCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmRSISysCfgSetAddrCacheStatus.setStatus("mandatory")
_NvmRSIServerTable_Object = MibTable
nvmRSIServerTable = _NvmRSIServerTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 7)
)
if mibBuilder.loadTexts:
    nvmRSIServerTable.setStatus("mandatory")
_NvmRSIServerEntry_Object = MibTableRow
nvmRSIServerEntry = _NvmRSIServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 7, 1)
)
nvmRSIServerEntry.setIndexNames(
    (0, "MICOM-RSI-MIB", "nvmRSIServerDNAAddr"),
)
if mibBuilder.loadTexts:
    nvmRSIServerEntry.setStatus("mandatory")


class _NvmRSIServerDNAAddr_Type(DisplayString):
    """Custom type nvmRSIServerDNAAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NvmRSIServerDNAAddr_Type.__name__ = "DisplayString"
_NvmRSIServerDNAAddr_Object = MibTableColumn
nvmRSIServerDNAAddr = _NvmRSIServerDNAAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 7, 1, 1),
    _NvmRSIServerDNAAddr_Type()
)
nvmRSIServerDNAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmRSIServerDNAAddr.setStatus("mandatory")


class _NvmRSIServerName_Type(DisplayString):
    """Custom type nvmRSIServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NvmRSIServerName_Type.__name__ = "DisplayString"
_NvmRSIServerName_Object = MibTableColumn
nvmRSIServerName = _NvmRSIServerName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 7, 1, 2),
    _NvmRSIServerName_Type()
)
nvmRSIServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmRSIServerName.setStatus("mandatory")


class _NvmRSIServerType_Type(Integer32):
    """Custom type nvmRSIServerType based on Integer32"""
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


_NvmRSIServerType_Type.__name__ = "Integer32"
_NvmRSIServerType_Object = MibTableColumn
nvmRSIServerType = _NvmRSIServerType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 7, 1, 3),
    _NvmRSIServerType_Type()
)
nvmRSIServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmRSIServerType.setStatus("mandatory")


class _NvmRSIServerEntryRowStatus_Type(Integer32):
    """Custom type nvmRSIServerEntryRowStatus based on Integer32"""
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


_NvmRSIServerEntryRowStatus_Type.__name__ = "Integer32"
_NvmRSIServerEntryRowStatus_Object = MibTableColumn
nvmRSIServerEntryRowStatus = _NvmRSIServerEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 1, 7, 1, 4),
    _NvmRSIServerEntryRowStatus_Type()
)
nvmRSIServerEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmRSIServerEntryRowStatus.setStatus("mandatory")
_Rsi_control_ObjectIdentity = ObjectIdentity
rsi_control = _Rsi_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 2)
)


class _McmRSICounterResetCmd_Type(Integer32):
    """Custom type mcmRSICounterResetCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmRSICounterResetCmd_Type.__name__ = "Integer32"
_McmRSICounterResetCmd_Object = MibScalar
mcmRSICounterResetCmd = _McmRSICounterResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 2, 1),
    _McmRSICounterResetCmd_Type()
)
mcmRSICounterResetCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmRSICounterResetCmd.setStatus("obsolete")
_Rsi_statistics_ObjectIdentity = ObjectIdentity
rsi_statistics = _Rsi_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3)
)
_McmRSIStatisticsGroup_ObjectIdentity = ObjectIdentity
mcmRSIStatisticsGroup = _McmRSIStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1)
)
_McmRSIStatisticsCacheCount_Type = Counter32
_McmRSIStatisticsCacheCount_Object = MibScalar
mcmRSIStatisticsCacheCount = _McmRSIStatisticsCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 1),
    _McmRSIStatisticsCacheCount_Type()
)
mcmRSIStatisticsCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsCacheCount.setStatus("mandatory")
_McmRSIStatisticsRequestAllCount_Type = Counter32
_McmRSIStatisticsRequestAllCount_Object = MibScalar
mcmRSIStatisticsRequestAllCount = _McmRSIStatisticsRequestAllCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 2),
    _McmRSIStatisticsRequestAllCount_Type()
)
mcmRSIStatisticsRequestAllCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsRequestAllCount.setStatus("mandatory")
_McmRSIStatisticsLocalResolvedCount_Type = Counter32
_McmRSIStatisticsLocalResolvedCount_Object = MibScalar
mcmRSIStatisticsLocalResolvedCount = _McmRSIStatisticsLocalResolvedCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 3),
    _McmRSIStatisticsLocalResolvedCount_Type()
)
mcmRSIStatisticsLocalResolvedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsLocalResolvedCount.setStatus("mandatory")
_McmRSIStatisticsPurgeCount_Type = Counter32
_McmRSIStatisticsPurgeCount_Object = MibScalar
mcmRSIStatisticsPurgeCount = _McmRSIStatisticsPurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 4),
    _McmRSIStatisticsPurgeCount_Type()
)
mcmRSIStatisticsPurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsPurgeCount.setStatus("mandatory")
_McmRSIStatisticsServerCount_Type = Counter32
_McmRSIStatisticsServerCount_Object = MibScalar
mcmRSIStatisticsServerCount = _McmRSIStatisticsServerCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 5),
    _McmRSIStatisticsServerCount_Type()
)
mcmRSIStatisticsServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsServerCount.setStatus("mandatory")
_McmRSIStatisticsServerRequestCount_Type = Counter32
_McmRSIStatisticsServerRequestCount_Object = MibScalar
mcmRSIStatisticsServerRequestCount = _McmRSIStatisticsServerRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 6),
    _McmRSIStatisticsServerRequestCount_Type()
)
mcmRSIStatisticsServerRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsServerRequestCount.setStatus("mandatory")
_McmRSIStatisticsServerResolvedCount_Type = Counter32
_McmRSIStatisticsServerResolvedCount_Object = MibScalar
mcmRSIStatisticsServerResolvedCount = _McmRSIStatisticsServerResolvedCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 7),
    _McmRSIStatisticsServerResolvedCount_Type()
)
mcmRSIStatisticsServerResolvedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsServerResolvedCount.setStatus("mandatory")
_McmRSIStatisticsServerNoNumberCount_Type = Counter32
_McmRSIStatisticsServerNoNumberCount_Object = MibScalar
mcmRSIStatisticsServerNoNumberCount = _McmRSIStatisticsServerNoNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 8),
    _McmRSIStatisticsServerNoNumberCount_Type()
)
mcmRSIStatisticsServerNoNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsServerNoNumberCount.setStatus("mandatory")
_McmRSIStatisticsTimeoutCount_Type = Counter32
_McmRSIStatisticsTimeoutCount_Object = MibScalar
mcmRSIStatisticsTimeoutCount = _McmRSIStatisticsTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 9),
    _McmRSIStatisticsTimeoutCount_Type()
)
mcmRSIStatisticsTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsTimeoutCount.setStatus("mandatory")
_McmRSIStatisticsRecoveryCount_Type = Counter32
_McmRSIStatisticsRecoveryCount_Object = MibScalar
mcmRSIStatisticsRecoveryCount = _McmRSIStatisticsRecoveryCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 3, 1, 10),
    _McmRSIStatisticsRecoveryCount_Type()
)
mcmRSIStatisticsRecoveryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRSIStatisticsRecoveryCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmAlarmRsiFailedToLocateRSA = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 0, 1)
)
mcmAlarmRsiFailedToLocateRSA.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmAlarmRsiFailedToLocateRSA.setStatus(
        ""
    )

mcmAlarmRsiRSAIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 0, 2)
)
mcmAlarmRsiRSAIsDown.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-RSI-MIB", "mcmRSIServerDNAAddr"))
)
if mibBuilder.loadTexts:
    mcmAlarmRsiRSAIsDown.setStatus(
        ""
    )

mcmAlarmRsiRSAIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 23, 0, 3)
)
mcmAlarmRsiRSAIsUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-RSI-MIB", "mcmRSIServerDNAAddr"))
)
if mibBuilder.loadTexts:
    mcmAlarmRsiRSAIsUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-RSI-MIB",
    **{"micom-rsi": micom_rsi,
       "mcmAlarmRsiFailedToLocateRSA": mcmAlarmRsiFailedToLocateRSA,
       "mcmAlarmRsiRSAIsDown": mcmAlarmRsiRSAIsDown,
       "mcmAlarmRsiRSAIsUp": mcmAlarmRsiRSAIsUp,
       "rsi-configuration": rsi_configuration,
       "mcmRSISysCfgDefGroup": mcmRSISysCfgDefGroup,
       "mcmRSISysCfgDefVNCSInstance": mcmRSISysCfgDefVNCSInstance,
       "mcmRSISysCfgDefNumCacheEntries": mcmRSISysCfgDefNumCacheEntries,
       "mcmRSISysCfgSetGroup": mcmRSISysCfgSetGroup,
       "mcmRSISysCfgSetAddrResRetries": mcmRSISysCfgSetAddrResRetries,
       "mcmRSISysCfgSetAddrResTimeout": mcmRSISysCfgSetAddrResTimeout,
       "mcmRSISysCfgSetAddrCacheStatus": mcmRSISysCfgSetAddrCacheStatus,
       "mcmRSICacheCfgTable": mcmRSICacheCfgTable,
       "mcmRSICacheCfgEntry": mcmRSICacheCfgEntry,
       "mcmRSICacheCfgDNDigits": mcmRSICacheCfgDNDigits,
       "mcmRSICacheCfgDNAAddr": mcmRSICacheCfgDNAAddr,
       "mcmRSICacheCfgProfileNumber": mcmRSICacheCfgProfileNumber,
       "mcmRSICacheCfgNumberOfHits": mcmRSICacheCfgNumberOfHits,
       "mcmRSICacheCfgServerDNA": mcmRSICacheCfgServerDNA,
       "mcmRSIServerTable": mcmRSIServerTable,
       "mcmRSIServerEntry": mcmRSIServerEntry,
       "mcmRSIServerDNAAddr": mcmRSIServerDNAAddr,
       "mcmRSIServerName": mcmRSIServerName,
       "mcmRSIServerType": mcmRSIServerType,
       "mcmRSIServerPortID": mcmRSIServerPortID,
       "mcmRSIServerDLCI": mcmRSIServerDLCI,
       "mcmRSIServerAvailStatus": mcmRSIServerAvailStatus,
       "mcmRSIServerLastDisconnectCause": mcmRSIServerLastDisconnectCause,
       "mcmRSIServerRequestCount": mcmRSIServerRequestCount,
       "mcmRSIServerResolvedCount": mcmRSIServerResolvedCount,
       "mcmRSIServerNoNumberCount": mcmRSIServerNoNumberCount,
       "mcmRSIServerTimeoutCount": mcmRSIServerTimeoutCount,
       "mcmRSIServerRecoveryCount": mcmRSIServerRecoveryCount,
       "nvmRSISysCfgDefGroup": nvmRSISysCfgDefGroup,
       "nvmRSISysCfgDefVNCSInstance": nvmRSISysCfgDefVNCSInstance,
       "nvmRSISysCfgDefNumCacheEntries": nvmRSISysCfgDefNumCacheEntries,
       "nvmRSISysCfgSetGroup": nvmRSISysCfgSetGroup,
       "nvmRSISysCfgSetAddrResRetries": nvmRSISysCfgSetAddrResRetries,
       "nvmRSISysCfgSetAddrResTimeout": nvmRSISysCfgSetAddrResTimeout,
       "nvmRSISysCfgSetAddrCacheStatus": nvmRSISysCfgSetAddrCacheStatus,
       "nvmRSIServerTable": nvmRSIServerTable,
       "nvmRSIServerEntry": nvmRSIServerEntry,
       "nvmRSIServerDNAAddr": nvmRSIServerDNAAddr,
       "nvmRSIServerName": nvmRSIServerName,
       "nvmRSIServerType": nvmRSIServerType,
       "nvmRSIServerEntryRowStatus": nvmRSIServerEntryRowStatus,
       "rsi-control": rsi_control,
       "mcmRSICounterResetCmd": mcmRSICounterResetCmd,
       "rsi-statistics": rsi_statistics,
       "mcmRSIStatisticsGroup": mcmRSIStatisticsGroup,
       "mcmRSIStatisticsCacheCount": mcmRSIStatisticsCacheCount,
       "mcmRSIStatisticsRequestAllCount": mcmRSIStatisticsRequestAllCount,
       "mcmRSIStatisticsLocalResolvedCount": mcmRSIStatisticsLocalResolvedCount,
       "mcmRSIStatisticsPurgeCount": mcmRSIStatisticsPurgeCount,
       "mcmRSIStatisticsServerCount": mcmRSIStatisticsServerCount,
       "mcmRSIStatisticsServerRequestCount": mcmRSIStatisticsServerRequestCount,
       "mcmRSIStatisticsServerResolvedCount": mcmRSIStatisticsServerResolvedCount,
       "mcmRSIStatisticsServerNoNumberCount": mcmRSIStatisticsServerNoNumberCount,
       "mcmRSIStatisticsTimeoutCount": mcmRSIStatisticsTimeoutCount,
       "mcmRSIStatisticsRecoveryCount": mcmRSIStatisticsRecoveryCount}
)
