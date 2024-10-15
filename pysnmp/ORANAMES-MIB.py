# SNMP MIB module (ORANAMES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORANAMES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:39 2024
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

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

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



class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oracle_ObjectIdentity = ObjectIdentity
oracle = _Oracle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111)
)
_OraNamesMIB_ObjectIdentity = ObjectIdentity
oraNamesMIB = _OraNamesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 6)
)
_OraNamesObjects_ObjectIdentity = ObjectIdentity
oraNamesObjects = _OraNamesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 6, 1)
)
_OraNamesTNSTable_Object = MibTable
oraNamesTNSTable = _OraNamesTNSTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1)
)
if mibBuilder.loadTexts:
    oraNamesTNSTable.setStatus("mandatory")
_OraNamesTNSEntry_Object = MibTableRow
oraNamesTNSEntry = _OraNamesTNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1)
)
oraNamesTNSEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    oraNamesTNSEntry.setStatus("mandatory")
_OraNamesTNSstartDate_Type = DateAndTime
_OraNamesTNSstartDate_Object = MibTableColumn
oraNamesTNSstartDate = _OraNamesTNSstartDate_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 1),
    _OraNamesTNSstartDate_Type()
)
oraNamesTNSstartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesTNSstartDate.setStatus("mandatory")


class _OraNamesTNStraceLevel_Type(Integer32):
    """Custom type oraNamesTNStraceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesTNStraceLevel_Type.__name__ = "Integer32"
_OraNamesTNStraceLevel_Object = MibTableColumn
oraNamesTNStraceLevel = _OraNamesTNStraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 2),
    _OraNamesTNStraceLevel_Type()
)
oraNamesTNStraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesTNStraceLevel.setStatus("mandatory")


class _OraNamesTNSsecurityLevel_Type(Integer32):
    """Custom type oraNamesTNSsecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesTNSsecurityLevel_Type.__name__ = "Integer32"
_OraNamesTNSsecurityLevel_Object = MibTableColumn
oraNamesTNSsecurityLevel = _OraNamesTNSsecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 3),
    _OraNamesTNSsecurityLevel_Type()
)
oraNamesTNSsecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesTNSsecurityLevel.setStatus("mandatory")
_OraNamesTNSparameterFile_Type = DisplayString
_OraNamesTNSparameterFile_Object = MibTableColumn
oraNamesTNSparameterFile = _OraNamesTNSparameterFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 4),
    _OraNamesTNSparameterFile_Type()
)
oraNamesTNSparameterFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesTNSparameterFile.setStatus("mandatory")
_OraNamesTNSlogFile_Type = DisplayString
_OraNamesTNSlogFile_Object = MibTableColumn
oraNamesTNSlogFile = _OraNamesTNSlogFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 5),
    _OraNamesTNSlogFile_Type()
)
oraNamesTNSlogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesTNSlogFile.setStatus("mandatory")
_OraNamesTNStraceFile_Type = DisplayString
_OraNamesTNStraceFile_Object = MibTableColumn
oraNamesTNStraceFile = _OraNamesTNStraceFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 6),
    _OraNamesTNStraceFile_Type()
)
oraNamesTNStraceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesTNStraceFile.setStatus("mandatory")


class _OraNamesTNSstate_Type(Integer32):
    """Custom type oraNamesTNSstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesTNSstate_Type.__name__ = "Integer32"
_OraNamesTNSstate_Object = MibTableColumn
oraNamesTNSstate = _OraNamesTNSstate_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 7),
    _OraNamesTNSstate_Type()
)
oraNamesTNSstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesTNSstate.setStatus("mandatory")
_OraNamesTNScontact_Type = DisplayString
_OraNamesTNScontact_Object = MibTableColumn
oraNamesTNScontact = _OraNamesTNScontact_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 8),
    _OraNamesTNScontact_Type()
)
oraNamesTNScontact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesTNScontact.setStatus("mandatory")
_OraNamesTNSlistenAddresses_Type = DisplayString
_OraNamesTNSlistenAddresses_Object = MibTableColumn
oraNamesTNSlistenAddresses = _OraNamesTNSlistenAddresses_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 9),
    _OraNamesTNSlistenAddresses_Type()
)
oraNamesTNSlistenAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesTNSlistenAddresses.setStatus("mandatory")
_OraNamesTNSfailedListenAddresses_Type = DisplayString
_OraNamesTNSfailedListenAddresses_Object = MibTableColumn
oraNamesTNSfailedListenAddresses = _OraNamesTNSfailedListenAddresses_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 10),
    _OraNamesTNSfailedListenAddresses_Type()
)
oraNamesTNSfailedListenAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesTNSfailedListenAddresses.setStatus("mandatory")
_OraNamesTNSreload_Type = TimeTicks
_OraNamesTNSreload_Object = MibTableColumn
oraNamesTNSreload = _OraNamesTNSreload_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 11),
    _OraNamesTNSreload_Type()
)
oraNamesTNSreload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesTNSreload.setStatus("mandatory")


class _OraNamesTNSrunningTime_Type(Integer32):
    """Custom type oraNamesTNSrunningTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesTNSrunningTime_Type.__name__ = "Integer32"
_OraNamesTNSrunningTime_Object = MibTableColumn
oraNamesTNSrunningTime = _OraNamesTNSrunningTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 12),
    _OraNamesTNSrunningTime_Type()
)
oraNamesTNSrunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesTNSrunningTime.setStatus("mandatory")
_OraNamesConfigTable_Object = MibTable
oraNamesConfigTable = _OraNamesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2)
)
if mibBuilder.loadTexts:
    oraNamesConfigTable.setStatus("mandatory")
_OraNamesConfigEntry_Object = MibTableRow
oraNamesConfigEntry = _OraNamesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1)
)
oraNamesConfigEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    oraNamesConfigEntry.setStatus("mandatory")
_OraNamesConfigAdminRegion_Type = DisplayString
_OraNamesConfigAdminRegion_Object = MibTableColumn
oraNamesConfigAdminRegion = _OraNamesConfigAdminRegion_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 1),
    _OraNamesConfigAdminRegion_Type()
)
oraNamesConfigAdminRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigAdminRegion.setStatus("mandatory")
_OraNamesConfigAuthorityRequired_Type = TruthValue
_OraNamesConfigAuthorityRequired_Object = MibTableColumn
oraNamesConfigAuthorityRequired = _OraNamesConfigAuthorityRequired_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 2),
    _OraNamesConfigAuthorityRequired_Type()
)
oraNamesConfigAuthorityRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigAuthorityRequired.setStatus("mandatory")
_OraNamesConfigAutoRefreshExpire_Type = TimeTicks
_OraNamesConfigAutoRefreshExpire_Object = MibTableColumn
oraNamesConfigAutoRefreshExpire = _OraNamesConfigAutoRefreshExpire_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 3),
    _OraNamesConfigAutoRefreshExpire_Type()
)
oraNamesConfigAutoRefreshExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigAutoRefreshExpire.setStatus("mandatory")
_OraNamesConfigAutoRefreshRetry_Type = TimeTicks
_OraNamesConfigAutoRefreshRetry_Object = MibTableColumn
oraNamesConfigAutoRefreshRetry = _OraNamesConfigAutoRefreshRetry_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 4),
    _OraNamesConfigAutoRefreshRetry_Type()
)
oraNamesConfigAutoRefreshRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigAutoRefreshRetry.setStatus("mandatory")
_OraNamesConfigCacheCheckpointFile_Type = DisplayString
_OraNamesConfigCacheCheckpointFile_Object = MibTableColumn
oraNamesConfigCacheCheckpointFile = _OraNamesConfigCacheCheckpointFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 5),
    _OraNamesConfigCacheCheckpointFile_Type()
)
oraNamesConfigCacheCheckpointFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigCacheCheckpointFile.setStatus("mandatory")
_OraNamesConfigCacheCheckpointInterval_Type = TimeTicks
_OraNamesConfigCacheCheckpointInterval_Object = MibTableColumn
oraNamesConfigCacheCheckpointInterval = _OraNamesConfigCacheCheckpointInterval_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 6),
    _OraNamesConfigCacheCheckpointInterval_Type()
)
oraNamesConfigCacheCheckpointInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigCacheCheckpointInterval.setStatus("mandatory")
_OraNamesConfigConfigCheckpointFile_Type = DisplayString
_OraNamesConfigConfigCheckpointFile_Object = MibTableColumn
oraNamesConfigConfigCheckpointFile = _OraNamesConfigConfigCheckpointFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 7),
    _OraNamesConfigConfigCheckpointFile_Type()
)
oraNamesConfigConfigCheckpointFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigConfigCheckpointFile.setStatus("mandatory")
_OraNamesConfigDefaultForwarders_Type = DisplayString
_OraNamesConfigDefaultForwarders_Object = MibTableColumn
oraNamesConfigDefaultForwarders = _OraNamesConfigDefaultForwarders_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 8),
    _OraNamesConfigDefaultForwarders_Type()
)
oraNamesConfigDefaultForwarders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigDefaultForwarders.setStatus("mandatory")
_OraNamesConfigDefaultForwardersOnly_Type = TruthValue
_OraNamesConfigDefaultForwardersOnly_Object = MibTableColumn
oraNamesConfigDefaultForwardersOnly = _OraNamesConfigDefaultForwardersOnly_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 9),
    _OraNamesConfigDefaultForwardersOnly_Type()
)
oraNamesConfigDefaultForwardersOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigDefaultForwardersOnly.setStatus("mandatory")
_OraNamesConfigDomainCheckpointFile_Type = DisplayString
_OraNamesConfigDomainCheckpointFile_Object = MibTableColumn
oraNamesConfigDomainCheckpointFile = _OraNamesConfigDomainCheckpointFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 10),
    _OraNamesConfigDomainCheckpointFile_Type()
)
oraNamesConfigDomainCheckpointFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigDomainCheckpointFile.setStatus("mandatory")
_OraNamesConfigDomainHints_Type = DisplayString
_OraNamesConfigDomainHints_Object = MibTableColumn
oraNamesConfigDomainHints = _OraNamesConfigDomainHints_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 11),
    _OraNamesConfigDomainHints_Type()
)
oraNamesConfigDomainHints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigDomainHints.setStatus("mandatory")
_OraNamesConfigDomains_Type = DisplayString
_OraNamesConfigDomains_Object = MibTableColumn
oraNamesConfigDomains = _OraNamesConfigDomains_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 12),
    _OraNamesConfigDomains_Type()
)
oraNamesConfigDomains.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigDomains.setStatus("mandatory")
_OraNamesConfigForwardingAvailable_Type = TruthValue
_OraNamesConfigForwardingAvailable_Object = MibTableColumn
oraNamesConfigForwardingAvailable = _OraNamesConfigForwardingAvailable_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 13),
    _OraNamesConfigForwardingAvailable_Type()
)
oraNamesConfigForwardingAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigForwardingAvailable.setStatus("mandatory")
_OraNamesConfigForwardingDesired_Type = TruthValue
_OraNamesConfigForwardingDesired_Object = MibTableColumn
oraNamesConfigForwardingDesired = _OraNamesConfigForwardingDesired_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 14),
    _OraNamesConfigForwardingDesired_Type()
)
oraNamesConfigForwardingDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigForwardingDesired.setStatus("mandatory")
_OraNamesConfigLogDirectory_Type = DisplayString
_OraNamesConfigLogDirectory_Object = MibTableColumn
oraNamesConfigLogDirectory = _OraNamesConfigLogDirectory_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 15),
    _OraNamesConfigLogDirectory_Type()
)
oraNamesConfigLogDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigLogDirectory.setStatus("mandatory")
_OraNamesConfigLogStatsInterval_Type = TimeTicks
_OraNamesConfigLogStatsInterval_Object = MibTableColumn
oraNamesConfigLogStatsInterval = _OraNamesConfigLogStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 16),
    _OraNamesConfigLogStatsInterval_Type()
)
oraNamesConfigLogStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigLogStatsInterval.setStatus("mandatory")
_OraNamesConfigLogUnique_Type = TruthValue
_OraNamesConfigLogUnique_Object = MibTableColumn
oraNamesConfigLogUnique = _OraNamesConfigLogUnique_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 17),
    _OraNamesConfigLogUnique_Type()
)
oraNamesConfigLogUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigLogUnique.setStatus("mandatory")


class _OraNamesConfigMaxOpenConnections_Type(Integer32):
    """Custom type oraNamesConfigMaxOpenConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesConfigMaxOpenConnections_Type.__name__ = "Integer32"
_OraNamesConfigMaxOpenConnections_Object = MibTableColumn
oraNamesConfigMaxOpenConnections = _OraNamesConfigMaxOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 18),
    _OraNamesConfigMaxOpenConnections_Type()
)
oraNamesConfigMaxOpenConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigMaxOpenConnections.setStatus("mandatory")


class _OraNamesConfigMaxReforwards_Type(Integer32):
    """Custom type oraNamesConfigMaxReforwards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesConfigMaxReforwards_Type.__name__ = "Integer32"
_OraNamesConfigMaxReforwards_Object = MibTableColumn
oraNamesConfigMaxReforwards = _OraNamesConfigMaxReforwards_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 19),
    _OraNamesConfigMaxReforwards_Type()
)
oraNamesConfigMaxReforwards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigMaxReforwards.setStatus("mandatory")


class _OraNamesConfigMessagePoolStartSize_Type(Integer32):
    """Custom type oraNamesConfigMessagePoolStartSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesConfigMessagePoolStartSize_Type.__name__ = "Integer32"
_OraNamesConfigMessagePoolStartSize_Object = MibTableColumn
oraNamesConfigMessagePoolStartSize = _OraNamesConfigMessagePoolStartSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 20),
    _OraNamesConfigMessagePoolStartSize_Type()
)
oraNamesConfigMessagePoolStartSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigMessagePoolStartSize.setStatus("mandatory")
_OraNamesConfigNoModifyRequests_Type = TruthValue
_OraNamesConfigNoModifyRequests_Object = MibTableColumn
oraNamesConfigNoModifyRequests = _OraNamesConfigNoModifyRequests_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 21),
    _OraNamesConfigNoModifyRequests_Type()
)
oraNamesConfigNoModifyRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigNoModifyRequests.setStatus("mandatory")
_OraNamesConfigNoRegionDatabase_Type = TruthValue
_OraNamesConfigNoRegionDatabase_Object = MibTableColumn
oraNamesConfigNoRegionDatabase = _OraNamesConfigNoRegionDatabase_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 22),
    _OraNamesConfigNoRegionDatabase_Type()
)
oraNamesConfigNoRegionDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigNoRegionDatabase.setStatus("mandatory")
_OraNamesConfigResetStatsInterval_Type = TimeTicks
_OraNamesConfigResetStatsInterval_Object = MibTableColumn
oraNamesConfigResetStatsInterval = _OraNamesConfigResetStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 23),
    _OraNamesConfigResetStatsInterval_Type()
)
oraNamesConfigResetStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigResetStatsInterval.setStatus("mandatory")
_OraNamesConfigServerName_Type = DisplayString
_OraNamesConfigServerName_Object = MibTableColumn
oraNamesConfigServerName = _OraNamesConfigServerName_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 24),
    _OraNamesConfigServerName_Type()
)
oraNamesConfigServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigServerName.setStatus("mandatory")
_OraNamesConfigTopologyCheckpointFile_Type = DisplayString
_OraNamesConfigTopologyCheckpointFile_Object = MibTableColumn
oraNamesConfigTopologyCheckpointFile = _OraNamesConfigTopologyCheckpointFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 25),
    _OraNamesConfigTopologyCheckpointFile_Type()
)
oraNamesConfigTopologyCheckpointFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigTopologyCheckpointFile.setStatus("mandatory")
_OraNamesConfigTraceDirectory_Type = DisplayString
_OraNamesConfigTraceDirectory_Object = MibTableColumn
oraNamesConfigTraceDirectory = _OraNamesConfigTraceDirectory_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 26),
    _OraNamesConfigTraceDirectory_Type()
)
oraNamesConfigTraceDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigTraceDirectory.setStatus("mandatory")
_OraNamesConfigTraceFunc_Type = DisplayString
_OraNamesConfigTraceFunc_Object = MibTableColumn
oraNamesConfigTraceFunc = _OraNamesConfigTraceFunc_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 27),
    _OraNamesConfigTraceFunc_Type()
)
oraNamesConfigTraceFunc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigTraceFunc.setStatus("mandatory")


class _OraNamesConfigTraceMask_Type(Integer32):
    """Custom type oraNamesConfigTraceMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraNamesConfigTraceMask_Type.__name__ = "Integer32"
_OraNamesConfigTraceMask_Object = MibTableColumn
oraNamesConfigTraceMask = _OraNamesConfigTraceMask_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 28),
    _OraNamesConfigTraceMask_Type()
)
oraNamesConfigTraceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigTraceMask.setStatus("mandatory")
_OraNamesConfigTraceUnique_Type = TruthValue
_OraNamesConfigTraceUnique_Object = MibTableColumn
oraNamesConfigTraceUnique = _OraNamesConfigTraceUnique_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 29),
    _OraNamesConfigTraceUnique_Type()
)
oraNamesConfigTraceUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNamesConfigTraceUnique.setStatus("mandatory")
_OraNamesServerTable_Object = MibTable
oraNamesServerTable = _OraNamesServerTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3)
)
if mibBuilder.loadTexts:
    oraNamesServerTable.setStatus("mandatory")
_OraNamesServerEntry_Object = MibTableRow
oraNamesServerEntry = _OraNamesServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1)
)
oraNamesServerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    oraNamesServerEntry.setStatus("mandatory")
_OraNamesServerQueriesReceived_Type = Counter32
_OraNamesServerQueriesReceived_Object = MibTableColumn
oraNamesServerQueriesReceived = _OraNamesServerQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 1),
    _OraNamesServerQueriesReceived_Type()
)
oraNamesServerQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerQueriesReceived.setStatus("mandatory")
_OraNamesServerLastNnamesNotFound_Type = DisplayString
_OraNamesServerLastNnamesNotFound_Object = MibTableColumn
oraNamesServerLastNnamesNotFound = _OraNamesServerLastNnamesNotFound_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 2),
    _OraNamesServerLastNnamesNotFound_Type()
)
oraNamesServerLastNnamesNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerLastNnamesNotFound.setStatus("mandatory")
_OraNamesServerQueriesTotalTime_Type = TimeTicks
_OraNamesServerQueriesTotalTime_Object = MibTableColumn
oraNamesServerQueriesTotalTime = _OraNamesServerQueriesTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 3),
    _OraNamesServerQueriesTotalTime_Type()
)
oraNamesServerQueriesTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerQueriesTotalTime.setStatus("mandatory")
_OraNamesServerDeletesReceived_Type = Counter32
_OraNamesServerDeletesReceived_Object = MibTableColumn
oraNamesServerDeletesReceived = _OraNamesServerDeletesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 4),
    _OraNamesServerDeletesReceived_Type()
)
oraNamesServerDeletesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerDeletesReceived.setStatus("mandatory")
_OraNamesServerDeletesRefused_Type = Counter32
_OraNamesServerDeletesRefused_Object = MibTableColumn
oraNamesServerDeletesRefused = _OraNamesServerDeletesRefused_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 5),
    _OraNamesServerDeletesRefused_Type()
)
oraNamesServerDeletesRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerDeletesRefused.setStatus("mandatory")
_OraNamesServerDeletesTotalTime_Type = TimeTicks
_OraNamesServerDeletesTotalTime_Object = MibTableColumn
oraNamesServerDeletesTotalTime = _OraNamesServerDeletesTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 6),
    _OraNamesServerDeletesTotalTime_Type()
)
oraNamesServerDeletesTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerDeletesTotalTime.setStatus("mandatory")
_OraNamesServerRenamesReceived_Type = Counter32
_OraNamesServerRenamesReceived_Object = MibTableColumn
oraNamesServerRenamesReceived = _OraNamesServerRenamesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 7),
    _OraNamesServerRenamesReceived_Type()
)
oraNamesServerRenamesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerRenamesReceived.setStatus("mandatory")
_OraNamesServerRenamesRefused_Type = Counter32
_OraNamesServerRenamesRefused_Object = MibTableColumn
oraNamesServerRenamesRefused = _OraNamesServerRenamesRefused_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 8),
    _OraNamesServerRenamesRefused_Type()
)
oraNamesServerRenamesRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerRenamesRefused.setStatus("mandatory")
_OraNamesServerRenamesTotalTime_Type = TimeTicks
_OraNamesServerRenamesTotalTime_Object = MibTableColumn
oraNamesServerRenamesTotalTime = _OraNamesServerRenamesTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 9),
    _OraNamesServerRenamesTotalTime_Type()
)
oraNamesServerRenamesTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerRenamesTotalTime.setStatus("mandatory")
_OraNamesServerUpdatesReceived_Type = Counter32
_OraNamesServerUpdatesReceived_Object = MibTableColumn
oraNamesServerUpdatesReceived = _OraNamesServerUpdatesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 10),
    _OraNamesServerUpdatesReceived_Type()
)
oraNamesServerUpdatesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerUpdatesReceived.setStatus("mandatory")
_OraNamesServerUpdatesRefused_Type = Counter32
_OraNamesServerUpdatesRefused_Object = MibTableColumn
oraNamesServerUpdatesRefused = _OraNamesServerUpdatesRefused_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 11),
    _OraNamesServerUpdatesRefused_Type()
)
oraNamesServerUpdatesRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerUpdatesRefused.setStatus("mandatory")
_OraNamesServerUpdatesTotalTime_Type = TimeTicks
_OraNamesServerUpdatesTotalTime_Object = MibTableColumn
oraNamesServerUpdatesTotalTime = _OraNamesServerUpdatesTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 12),
    _OraNamesServerUpdatesTotalTime_Type()
)
oraNamesServerUpdatesTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerUpdatesTotalTime.setStatus("mandatory")
_OraNamesServerCorruptMessagesReceived_Type = Counter32
_OraNamesServerCorruptMessagesReceived_Object = MibTableColumn
oraNamesServerCorruptMessagesReceived = _OraNamesServerCorruptMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 13),
    _OraNamesServerCorruptMessagesReceived_Type()
)
oraNamesServerCorruptMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerCorruptMessagesReceived.setStatus("mandatory")
_OraNamesServerResponsesSent_Type = Counter32
_OraNamesServerResponsesSent_Object = MibTableColumn
oraNamesServerResponsesSent = _OraNamesServerResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 14),
    _OraNamesServerResponsesSent_Type()
)
oraNamesServerResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerResponsesSent.setStatus("mandatory")
_OraNamesServerErrorResponsesSent_Type = Counter32
_OraNamesServerErrorResponsesSent_Object = MibTableColumn
oraNamesServerErrorResponsesSent = _OraNamesServerErrorResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 15),
    _OraNamesServerErrorResponsesSent_Type()
)
oraNamesServerErrorResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerErrorResponsesSent.setStatus("mandatory")
_OraNamesServerAliasLoopsDetected_Type = Counter32
_OraNamesServerAliasLoopsDetected_Object = MibTableColumn
oraNamesServerAliasLoopsDetected = _OraNamesServerAliasLoopsDetected_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 16),
    _OraNamesServerAliasLoopsDetected_Type()
)
oraNamesServerAliasLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerAliasLoopsDetected.setStatus("mandatory")
_OraNamesServerLookupsAttempted_Type = Counter32
_OraNamesServerLookupsAttempted_Object = MibTableColumn
oraNamesServerLookupsAttempted = _OraNamesServerLookupsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 17),
    _OraNamesServerLookupsAttempted_Type()
)
oraNamesServerLookupsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerLookupsAttempted.setStatus("mandatory")
_OraNamesServerCreatedOnLookup_Type = Counter32
_OraNamesServerCreatedOnLookup_Object = MibTableColumn
oraNamesServerCreatedOnLookup = _OraNamesServerCreatedOnLookup_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 18),
    _OraNamesServerCreatedOnLookup_Type()
)
oraNamesServerCreatedOnLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerCreatedOnLookup.setStatus("mandatory")
_OraNamesServerLookupFailures_Type = Counter32
_OraNamesServerLookupFailures_Object = MibTableColumn
oraNamesServerLookupFailures = _OraNamesServerLookupFailures_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 19),
    _OraNamesServerLookupFailures_Type()
)
oraNamesServerLookupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerLookupFailures.setStatus("mandatory")
_OraNamesServerExactMatches_Type = Counter32
_OraNamesServerExactMatches_Object = MibTableColumn
oraNamesServerExactMatches = _OraNamesServerExactMatches_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 20),
    _OraNamesServerExactMatches_Type()
)
oraNamesServerExactMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerExactMatches.setStatus("mandatory")
_OraNamesServerForwardFailures_Type = Counter32
_OraNamesServerForwardFailures_Object = MibTableColumn
oraNamesServerForwardFailures = _OraNamesServerForwardFailures_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 21),
    _OraNamesServerForwardFailures_Type()
)
oraNamesServerForwardFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerForwardFailures.setStatus("mandatory")
_OraNamesServerForwardTimeouts_Type = Counter32
_OraNamesServerForwardTimeouts_Object = MibTableColumn
oraNamesServerForwardTimeouts = _OraNamesServerForwardTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 22),
    _OraNamesServerForwardTimeouts_Type()
)
oraNamesServerForwardTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerForwardTimeouts.setStatus("mandatory")
_OraNamesServerResponsesReceived_Type = Counter32
_OraNamesServerResponsesReceived_Object = MibTableColumn
oraNamesServerResponsesReceived = _OraNamesServerResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 23),
    _OraNamesServerResponsesReceived_Type()
)
oraNamesServerResponsesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerResponsesReceived.setStatus("mandatory")
_OraNamesServerErrorResponsesReceived_Type = Counter32
_OraNamesServerErrorResponsesReceived_Object = MibTableColumn
oraNamesServerErrorResponsesReceived = _OraNamesServerErrorResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 24),
    _OraNamesServerErrorResponsesReceived_Type()
)
oraNamesServerErrorResponsesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerErrorResponsesReceived.setStatus("mandatory")
_OraNamesServerRequestsForwarded_Type = Counter32
_OraNamesServerRequestsForwarded_Object = MibTableColumn
oraNamesServerRequestsForwarded = _OraNamesServerRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 25),
    _OraNamesServerRequestsForwarded_Type()
)
oraNamesServerRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerRequestsForwarded.setStatus("mandatory")
_OraNamesServerLastReload_Type = DateAndTime
_OraNamesServerLastReload_Object = MibTableColumn
oraNamesServerLastReload = _OraNamesServerLastReload_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 26),
    _OraNamesServerLastReload_Type()
)
oraNamesServerLastReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerLastReload.setStatus("mandatory")
_OraNamesServerReloadCheckFailures_Type = Counter32
_OraNamesServerReloadCheckFailures_Object = MibTableColumn
oraNamesServerReloadCheckFailures = _OraNamesServerReloadCheckFailures_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 27),
    _OraNamesServerReloadCheckFailures_Type()
)
oraNamesServerReloadCheckFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerReloadCheckFailures.setStatus("mandatory")
_OraNamesServerLastCheckpoint_Type = DateAndTime
_OraNamesServerLastCheckpoint_Object = MibTableColumn
oraNamesServerLastCheckpoint = _OraNamesServerLastCheckpoint_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 28),
    _OraNamesServerLastCheckpoint_Type()
)
oraNamesServerLastCheckpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerLastCheckpoint.setStatus("mandatory")
_OraNamesServerName_Type = DisplayString
_OraNamesServerName_Object = MibTableColumn
oraNamesServerName = _OraNamesServerName_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 29),
    _OraNamesServerName_Type()
)
oraNamesServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerName.setStatus("mandatory")
_OraNamesServerAdminRegion_Type = DisplayString
_OraNamesServerAdminRegion_Object = MibTableColumn
oraNamesServerAdminRegion = _OraNamesServerAdminRegion_Object(
    (1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 30),
    _OraNamesServerAdminRegion_Type()
)
oraNamesServerAdminRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNamesServerAdminRegion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORANAMES-MIB",
    **{"DateAndTime": DateAndTime,
       "TruthValue": TruthValue,
       "oracle": oracle,
       "oraNamesMIB": oraNamesMIB,
       "oraNamesObjects": oraNamesObjects,
       "oraNamesTNSTable": oraNamesTNSTable,
       "oraNamesTNSEntry": oraNamesTNSEntry,
       "oraNamesTNSstartDate": oraNamesTNSstartDate,
       "oraNamesTNStraceLevel": oraNamesTNStraceLevel,
       "oraNamesTNSsecurityLevel": oraNamesTNSsecurityLevel,
       "oraNamesTNSparameterFile": oraNamesTNSparameterFile,
       "oraNamesTNSlogFile": oraNamesTNSlogFile,
       "oraNamesTNStraceFile": oraNamesTNStraceFile,
       "oraNamesTNSstate": oraNamesTNSstate,
       "oraNamesTNScontact": oraNamesTNScontact,
       "oraNamesTNSlistenAddresses": oraNamesTNSlistenAddresses,
       "oraNamesTNSfailedListenAddresses": oraNamesTNSfailedListenAddresses,
       "oraNamesTNSreload": oraNamesTNSreload,
       "oraNamesTNSrunningTime": oraNamesTNSrunningTime,
       "oraNamesConfigTable": oraNamesConfigTable,
       "oraNamesConfigEntry": oraNamesConfigEntry,
       "oraNamesConfigAdminRegion": oraNamesConfigAdminRegion,
       "oraNamesConfigAuthorityRequired": oraNamesConfigAuthorityRequired,
       "oraNamesConfigAutoRefreshExpire": oraNamesConfigAutoRefreshExpire,
       "oraNamesConfigAutoRefreshRetry": oraNamesConfigAutoRefreshRetry,
       "oraNamesConfigCacheCheckpointFile": oraNamesConfigCacheCheckpointFile,
       "oraNamesConfigCacheCheckpointInterval": oraNamesConfigCacheCheckpointInterval,
       "oraNamesConfigConfigCheckpointFile": oraNamesConfigConfigCheckpointFile,
       "oraNamesConfigDefaultForwarders": oraNamesConfigDefaultForwarders,
       "oraNamesConfigDefaultForwardersOnly": oraNamesConfigDefaultForwardersOnly,
       "oraNamesConfigDomainCheckpointFile": oraNamesConfigDomainCheckpointFile,
       "oraNamesConfigDomainHints": oraNamesConfigDomainHints,
       "oraNamesConfigDomains": oraNamesConfigDomains,
       "oraNamesConfigForwardingAvailable": oraNamesConfigForwardingAvailable,
       "oraNamesConfigForwardingDesired": oraNamesConfigForwardingDesired,
       "oraNamesConfigLogDirectory": oraNamesConfigLogDirectory,
       "oraNamesConfigLogStatsInterval": oraNamesConfigLogStatsInterval,
       "oraNamesConfigLogUnique": oraNamesConfigLogUnique,
       "oraNamesConfigMaxOpenConnections": oraNamesConfigMaxOpenConnections,
       "oraNamesConfigMaxReforwards": oraNamesConfigMaxReforwards,
       "oraNamesConfigMessagePoolStartSize": oraNamesConfigMessagePoolStartSize,
       "oraNamesConfigNoModifyRequests": oraNamesConfigNoModifyRequests,
       "oraNamesConfigNoRegionDatabase": oraNamesConfigNoRegionDatabase,
       "oraNamesConfigResetStatsInterval": oraNamesConfigResetStatsInterval,
       "oraNamesConfigServerName": oraNamesConfigServerName,
       "oraNamesConfigTopologyCheckpointFile": oraNamesConfigTopologyCheckpointFile,
       "oraNamesConfigTraceDirectory": oraNamesConfigTraceDirectory,
       "oraNamesConfigTraceFunc": oraNamesConfigTraceFunc,
       "oraNamesConfigTraceMask": oraNamesConfigTraceMask,
       "oraNamesConfigTraceUnique": oraNamesConfigTraceUnique,
       "oraNamesServerTable": oraNamesServerTable,
       "oraNamesServerEntry": oraNamesServerEntry,
       "oraNamesServerQueriesReceived": oraNamesServerQueriesReceived,
       "oraNamesServerLastNnamesNotFound": oraNamesServerLastNnamesNotFound,
       "oraNamesServerQueriesTotalTime": oraNamesServerQueriesTotalTime,
       "oraNamesServerDeletesReceived": oraNamesServerDeletesReceived,
       "oraNamesServerDeletesRefused": oraNamesServerDeletesRefused,
       "oraNamesServerDeletesTotalTime": oraNamesServerDeletesTotalTime,
       "oraNamesServerRenamesReceived": oraNamesServerRenamesReceived,
       "oraNamesServerRenamesRefused": oraNamesServerRenamesRefused,
       "oraNamesServerRenamesTotalTime": oraNamesServerRenamesTotalTime,
       "oraNamesServerUpdatesReceived": oraNamesServerUpdatesReceived,
       "oraNamesServerUpdatesRefused": oraNamesServerUpdatesRefused,
       "oraNamesServerUpdatesTotalTime": oraNamesServerUpdatesTotalTime,
       "oraNamesServerCorruptMessagesReceived": oraNamesServerCorruptMessagesReceived,
       "oraNamesServerResponsesSent": oraNamesServerResponsesSent,
       "oraNamesServerErrorResponsesSent": oraNamesServerErrorResponsesSent,
       "oraNamesServerAliasLoopsDetected": oraNamesServerAliasLoopsDetected,
       "oraNamesServerLookupsAttempted": oraNamesServerLookupsAttempted,
       "oraNamesServerCreatedOnLookup": oraNamesServerCreatedOnLookup,
       "oraNamesServerLookupFailures": oraNamesServerLookupFailures,
       "oraNamesServerExactMatches": oraNamesServerExactMatches,
       "oraNamesServerForwardFailures": oraNamesServerForwardFailures,
       "oraNamesServerForwardTimeouts": oraNamesServerForwardTimeouts,
       "oraNamesServerResponsesReceived": oraNamesServerResponsesReceived,
       "oraNamesServerErrorResponsesReceived": oraNamesServerErrorResponsesReceived,
       "oraNamesServerRequestsForwarded": oraNamesServerRequestsForwarded,
       "oraNamesServerLastReload": oraNamesServerLastReload,
       "oraNamesServerReloadCheckFailures": oraNamesServerReloadCheckFailures,
       "oraNamesServerLastCheckpoint": oraNamesServerLastCheckpoint,
       "oraNamesServerName": oraNamesServerName,
       "oraNamesServerAdminRegion": oraNamesServerAdminRegion}
)
