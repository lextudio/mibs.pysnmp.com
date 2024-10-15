# SNMP MIB module (DIRECTORY-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DIRECTORY-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:13 2024
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

(DistinguishedName,
 URLString,
 applIndex) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "DistinguishedName",
    "URLString",
    "applIndex")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

dsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 66)
)
dsMIB.setRevisions(
        ("1999-06-07 00:00",
         "1993-11-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsTable_Object = MibTable
dsTable = _DsTable_Object(
    (1, 3, 6, 1, 2, 1, 66, 1)
)
if mibBuilder.loadTexts:
    dsTable.setStatus("current")
_DsTableEntry_Object = MibTableRow
dsTableEntry = _DsTableEntry_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1)
)
dsTableEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    dsTableEntry.setStatus("current")


class _DsServerType_Type(Bits):
    """Custom type dsServerType based on Bits"""
    namedValues = NamedValues(
        *(("backEndDirectoryServer", 1),
          ("frontEndDirectoryServer", 0))
    )

_DsServerType_Type.__name__ = "Bits"
_DsServerType_Object = MibTableColumn
dsServerType = _DsServerType_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 1),
    _DsServerType_Type()
)
dsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsServerType.setStatus("current")
_DsServerDescription_Type = DisplayString
_DsServerDescription_Object = MibTableColumn
dsServerDescription = _DsServerDescription_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 2),
    _DsServerDescription_Type()
)
dsServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsServerDescription.setStatus("current")
_DsMasterEntries_Type = Gauge32
_DsMasterEntries_Object = MibTableColumn
dsMasterEntries = _DsMasterEntries_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 3),
    _DsMasterEntries_Type()
)
dsMasterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMasterEntries.setStatus("current")
_DsCopyEntries_Type = Gauge32
_DsCopyEntries_Object = MibTableColumn
dsCopyEntries = _DsCopyEntries_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 4),
    _DsCopyEntries_Type()
)
dsCopyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCopyEntries.setStatus("current")
_DsCacheEntries_Type = Gauge32
_DsCacheEntries_Object = MibTableColumn
dsCacheEntries = _DsCacheEntries_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 5),
    _DsCacheEntries_Type()
)
dsCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCacheEntries.setStatus("current")
_DsCacheHits_Type = Counter32
_DsCacheHits_Object = MibTableColumn
dsCacheHits = _DsCacheHits_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 6),
    _DsCacheHits_Type()
)
dsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCacheHits.setStatus("current")
_DsSlaveHits_Type = Counter32
_DsSlaveHits_Object = MibTableColumn
dsSlaveHits = _DsSlaveHits_Object(
    (1, 3, 6, 1, 2, 1, 66, 1, 1, 7),
    _DsSlaveHits_Type()
)
dsSlaveHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlaveHits.setStatus("current")
_DsApplIfOpsTable_Object = MibTable
dsApplIfOpsTable = _DsApplIfOpsTable_Object(
    (1, 3, 6, 1, 2, 1, 66, 2)
)
if mibBuilder.loadTexts:
    dsApplIfOpsTable.setStatus("current")
_DsApplIfOpsEntry_Object = MibTableRow
dsApplIfOpsEntry = _DsApplIfOpsEntry_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1)
)
dsApplIfOpsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"),
)
if mibBuilder.loadTexts:
    dsApplIfOpsEntry.setStatus("current")


class _DsApplIfProtocolIndex_Type(Integer32):
    """Custom type dsApplIfProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsApplIfProtocolIndex_Type.__name__ = "Integer32"
_DsApplIfProtocolIndex_Object = MibTableColumn
dsApplIfProtocolIndex = _DsApplIfProtocolIndex_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 1),
    _DsApplIfProtocolIndex_Type()
)
dsApplIfProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfProtocolIndex.setStatus("current")
_DsApplIfProtocol_Type = ObjectIdentifier
_DsApplIfProtocol_Object = MibTableColumn
dsApplIfProtocol = _DsApplIfProtocol_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 2),
    _DsApplIfProtocol_Type()
)
dsApplIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfProtocol.setStatus("current")
_DsApplIfUnauthBinds_Type = Counter32
_DsApplIfUnauthBinds_Object = MibTableColumn
dsApplIfUnauthBinds = _DsApplIfUnauthBinds_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 3),
    _DsApplIfUnauthBinds_Type()
)
dsApplIfUnauthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfUnauthBinds.setStatus("current")
_DsApplIfSimpleAuthBinds_Type = Counter32
_DsApplIfSimpleAuthBinds_Object = MibTableColumn
dsApplIfSimpleAuthBinds = _DsApplIfSimpleAuthBinds_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 4),
    _DsApplIfSimpleAuthBinds_Type()
)
dsApplIfSimpleAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfSimpleAuthBinds.setStatus("current")
_DsApplIfStrongAuthBinds_Type = Counter32
_DsApplIfStrongAuthBinds_Object = MibTableColumn
dsApplIfStrongAuthBinds = _DsApplIfStrongAuthBinds_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 5),
    _DsApplIfStrongAuthBinds_Type()
)
dsApplIfStrongAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfStrongAuthBinds.setStatus("current")
_DsApplIfBindSecurityErrors_Type = Counter32
_DsApplIfBindSecurityErrors_Object = MibTableColumn
dsApplIfBindSecurityErrors = _DsApplIfBindSecurityErrors_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 6),
    _DsApplIfBindSecurityErrors_Type()
)
dsApplIfBindSecurityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfBindSecurityErrors.setStatus("current")
_DsApplIfInOps_Type = Counter32
_DsApplIfInOps_Object = MibTableColumn
dsApplIfInOps = _DsApplIfInOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 7),
    _DsApplIfInOps_Type()
)
dsApplIfInOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfInOps.setStatus("current")
_DsApplIfReadOps_Type = Counter32
_DsApplIfReadOps_Object = MibTableColumn
dsApplIfReadOps = _DsApplIfReadOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 8),
    _DsApplIfReadOps_Type()
)
dsApplIfReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfReadOps.setStatus("current")
_DsApplIfCompareOps_Type = Counter32
_DsApplIfCompareOps_Object = MibTableColumn
dsApplIfCompareOps = _DsApplIfCompareOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 9),
    _DsApplIfCompareOps_Type()
)
dsApplIfCompareOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfCompareOps.setStatus("current")
_DsApplIfAddEntryOps_Type = Counter32
_DsApplIfAddEntryOps_Object = MibTableColumn
dsApplIfAddEntryOps = _DsApplIfAddEntryOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 10),
    _DsApplIfAddEntryOps_Type()
)
dsApplIfAddEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfAddEntryOps.setStatus("current")
_DsApplIfRemoveEntryOps_Type = Counter32
_DsApplIfRemoveEntryOps_Object = MibTableColumn
dsApplIfRemoveEntryOps = _DsApplIfRemoveEntryOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 11),
    _DsApplIfRemoveEntryOps_Type()
)
dsApplIfRemoveEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfRemoveEntryOps.setStatus("current")
_DsApplIfModifyEntryOps_Type = Counter32
_DsApplIfModifyEntryOps_Object = MibTableColumn
dsApplIfModifyEntryOps = _DsApplIfModifyEntryOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 12),
    _DsApplIfModifyEntryOps_Type()
)
dsApplIfModifyEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfModifyEntryOps.setStatus("current")
_DsApplIfModifyRDNOps_Type = Counter32
_DsApplIfModifyRDNOps_Object = MibTableColumn
dsApplIfModifyRDNOps = _DsApplIfModifyRDNOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 13),
    _DsApplIfModifyRDNOps_Type()
)
dsApplIfModifyRDNOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfModifyRDNOps.setStatus("current")
_DsApplIfListOps_Type = Counter32
_DsApplIfListOps_Object = MibTableColumn
dsApplIfListOps = _DsApplIfListOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 14),
    _DsApplIfListOps_Type()
)
dsApplIfListOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfListOps.setStatus("current")
_DsApplIfSearchOps_Type = Counter32
_DsApplIfSearchOps_Object = MibTableColumn
dsApplIfSearchOps = _DsApplIfSearchOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 15),
    _DsApplIfSearchOps_Type()
)
dsApplIfSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfSearchOps.setStatus("current")
_DsApplIfOneLevelSearchOps_Type = Counter32
_DsApplIfOneLevelSearchOps_Object = MibTableColumn
dsApplIfOneLevelSearchOps = _DsApplIfOneLevelSearchOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 16),
    _DsApplIfOneLevelSearchOps_Type()
)
dsApplIfOneLevelSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfOneLevelSearchOps.setStatus("current")
_DsApplIfWholeSubtreeSearchOps_Type = Counter32
_DsApplIfWholeSubtreeSearchOps_Object = MibTableColumn
dsApplIfWholeSubtreeSearchOps = _DsApplIfWholeSubtreeSearchOps_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 17),
    _DsApplIfWholeSubtreeSearchOps_Type()
)
dsApplIfWholeSubtreeSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfWholeSubtreeSearchOps.setStatus("current")
_DsApplIfReferrals_Type = Counter32
_DsApplIfReferrals_Object = MibTableColumn
dsApplIfReferrals = _DsApplIfReferrals_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 18),
    _DsApplIfReferrals_Type()
)
dsApplIfReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfReferrals.setStatus("current")
_DsApplIfChainings_Type = Counter32
_DsApplIfChainings_Object = MibTableColumn
dsApplIfChainings = _DsApplIfChainings_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 19),
    _DsApplIfChainings_Type()
)
dsApplIfChainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfChainings.setStatus("current")
_DsApplIfSecurityErrors_Type = Counter32
_DsApplIfSecurityErrors_Object = MibTableColumn
dsApplIfSecurityErrors = _DsApplIfSecurityErrors_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 20),
    _DsApplIfSecurityErrors_Type()
)
dsApplIfSecurityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfSecurityErrors.setStatus("current")
_DsApplIfErrors_Type = Counter32
_DsApplIfErrors_Object = MibTableColumn
dsApplIfErrors = _DsApplIfErrors_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 21),
    _DsApplIfErrors_Type()
)
dsApplIfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfErrors.setStatus("current")
_DsApplIfReplicationUpdatesIn_Type = Counter32
_DsApplIfReplicationUpdatesIn_Object = MibTableColumn
dsApplIfReplicationUpdatesIn = _DsApplIfReplicationUpdatesIn_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 22),
    _DsApplIfReplicationUpdatesIn_Type()
)
dsApplIfReplicationUpdatesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfReplicationUpdatesIn.setStatus("current")
_DsApplIfReplicationUpdatesOut_Type = Counter32
_DsApplIfReplicationUpdatesOut_Object = MibTableColumn
dsApplIfReplicationUpdatesOut = _DsApplIfReplicationUpdatesOut_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 23),
    _DsApplIfReplicationUpdatesOut_Type()
)
dsApplIfReplicationUpdatesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfReplicationUpdatesOut.setStatus("current")
_DsApplIfInBytes_Type = Counter32
_DsApplIfInBytes_Object = MibTableColumn
dsApplIfInBytes = _DsApplIfInBytes_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 24),
    _DsApplIfInBytes_Type()
)
dsApplIfInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfInBytes.setStatus("current")
_DsApplIfOutBytes_Type = Counter32
_DsApplIfOutBytes_Object = MibTableColumn
dsApplIfOutBytes = _DsApplIfOutBytes_Object(
    (1, 3, 6, 1, 2, 1, 66, 2, 1, 25),
    _DsApplIfOutBytes_Type()
)
dsApplIfOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsApplIfOutBytes.setStatus("current")
_DsIntTable_Object = MibTable
dsIntTable = _DsIntTable_Object(
    (1, 3, 6, 1, 2, 1, 66, 3)
)
if mibBuilder.loadTexts:
    dsIntTable.setStatus("current")
_DsIntEntry_Object = MibTableRow
dsIntEntry = _DsIntEntry_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1)
)
dsIntEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "DIRECTORY-SERVER-MIB", "dsIntEntIndex"),
    (0, "DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"),
)
if mibBuilder.loadTexts:
    dsIntEntry.setStatus("current")


class _DsIntEntIndex_Type(Integer32):
    """Custom type dsIntEntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsIntEntIndex_Type.__name__ = "Integer32"
_DsIntEntIndex_Object = MibTableColumn
dsIntEntIndex = _DsIntEntIndex_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 1),
    _DsIntEntIndex_Type()
)
dsIntEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsIntEntIndex.setStatus("current")
_DsIntEntDirectoryName_Type = DistinguishedName
_DsIntEntDirectoryName_Object = MibTableColumn
dsIntEntDirectoryName = _DsIntEntDirectoryName_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 2),
    _DsIntEntDirectoryName_Type()
)
dsIntEntDirectoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntDirectoryName.setStatus("current")
_DsIntEntTimeOfCreation_Type = TimeStamp
_DsIntEntTimeOfCreation_Object = MibTableColumn
dsIntEntTimeOfCreation = _DsIntEntTimeOfCreation_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 3),
    _DsIntEntTimeOfCreation_Type()
)
dsIntEntTimeOfCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntTimeOfCreation.setStatus("current")
_DsIntEntTimeOfLastAttempt_Type = TimeStamp
_DsIntEntTimeOfLastAttempt_Object = MibTableColumn
dsIntEntTimeOfLastAttempt = _DsIntEntTimeOfLastAttempt_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 4),
    _DsIntEntTimeOfLastAttempt_Type()
)
dsIntEntTimeOfLastAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntTimeOfLastAttempt.setStatus("current")
_DsIntEntTimeOfLastSuccess_Type = TimeStamp
_DsIntEntTimeOfLastSuccess_Object = MibTableColumn
dsIntEntTimeOfLastSuccess = _DsIntEntTimeOfLastSuccess_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 5),
    _DsIntEntTimeOfLastSuccess_Type()
)
dsIntEntTimeOfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntTimeOfLastSuccess.setStatus("current")
_DsIntEntFailuresSinceLastSuccess_Type = Gauge32
_DsIntEntFailuresSinceLastSuccess_Object = MibTableColumn
dsIntEntFailuresSinceLastSuccess = _DsIntEntFailuresSinceLastSuccess_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 6),
    _DsIntEntFailuresSinceLastSuccess_Type()
)
dsIntEntFailuresSinceLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntFailuresSinceLastSuccess.setStatus("current")
_DsIntEntFailures_Type = ZeroBasedCounter32
_DsIntEntFailures_Object = MibTableColumn
dsIntEntFailures = _DsIntEntFailures_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 7),
    _DsIntEntFailures_Type()
)
dsIntEntFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntFailures.setStatus("current")
_DsIntEntSuccesses_Type = ZeroBasedCounter32
_DsIntEntSuccesses_Object = MibTableColumn
dsIntEntSuccesses = _DsIntEntSuccesses_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 8),
    _DsIntEntSuccesses_Type()
)
dsIntEntSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntSuccesses.setStatus("current")
_DsIntEntURL_Type = URLString
_DsIntEntURL_Object = MibTableColumn
dsIntEntURL = _DsIntEntURL_Object(
    (1, 3, 6, 1, 2, 1, 66, 3, 1, 9),
    _DsIntEntURL_Type()
)
dsIntEntURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsIntEntURL.setStatus("current")
_DsConformance_ObjectIdentity = ObjectIdentity
dsConformance = _DsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 66, 4)
)
_DsGroups_ObjectIdentity = ObjectIdentity
dsGroups = _DsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 66, 4, 1)
)
_DsCompliances_ObjectIdentity = ObjectIdentity
dsCompliances = _DsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 66, 4, 2)
)

# Managed Objects groups

dsEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 66, 4, 1, 1)
)
dsEntryGroup.setObjects(
      *(("DIRECTORY-SERVER-MIB", "dsServerType"),
        ("DIRECTORY-SERVER-MIB", "dsServerDescription"),
        ("DIRECTORY-SERVER-MIB", "dsMasterEntries"),
        ("DIRECTORY-SERVER-MIB", "dsCopyEntries"),
        ("DIRECTORY-SERVER-MIB", "dsCacheEntries"),
        ("DIRECTORY-SERVER-MIB", "dsCacheHits"),
        ("DIRECTORY-SERVER-MIB", "dsSlaveHits"))
)
if mibBuilder.loadTexts:
    dsEntryGroup.setStatus("current")

dsOpsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 66, 4, 1, 2)
)
dsOpsGroup.setObjects(
      *(("DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfProtocol"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfUnauthBinds"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfSimpleAuthBinds"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfStrongAuthBinds"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfBindSecurityErrors"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfInOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfReadOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfCompareOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfAddEntryOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfRemoveEntryOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfModifyEntryOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfModifyRDNOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfListOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfSearchOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfOneLevelSearchOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfWholeSubtreeSearchOps"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfReferrals"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfChainings"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfSecurityErrors"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfErrors"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfReplicationUpdatesIn"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfReplicationUpdatesOut"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfInBytes"),
        ("DIRECTORY-SERVER-MIB", "dsApplIfOutBytes"))
)
if mibBuilder.loadTexts:
    dsOpsGroup.setStatus("current")

dsIntGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 66, 4, 1, 3)
)
dsIntGroup.setObjects(
      *(("DIRECTORY-SERVER-MIB", "dsIntEntDirectoryName"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfCreation"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfLastAttempt"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfLastSuccess"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntFailuresSinceLastSuccess"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntFailures"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntSuccesses"),
        ("DIRECTORY-SERVER-MIB", "dsIntEntURL"))
)
if mibBuilder.loadTexts:
    dsIntGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsEntryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 66, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dsEntryCompliance.setStatus(
        "current"
    )

dsOpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 66, 4, 2, 2)
)
if mibBuilder.loadTexts:
    dsOpsCompliance.setStatus(
        "current"
    )

dsIntCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 66, 4, 2, 3)
)
if mibBuilder.loadTexts:
    dsIntCompliance.setStatus(
        "current"
    )

dsOpsIntCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 66, 4, 2, 4)
)
if mibBuilder.loadTexts:
    dsOpsIntCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIRECTORY-SERVER-MIB",
    **{"dsMIB": dsMIB,
       "dsTable": dsTable,
       "dsTableEntry": dsTableEntry,
       "dsServerType": dsServerType,
       "dsServerDescription": dsServerDescription,
       "dsMasterEntries": dsMasterEntries,
       "dsCopyEntries": dsCopyEntries,
       "dsCacheEntries": dsCacheEntries,
       "dsCacheHits": dsCacheHits,
       "dsSlaveHits": dsSlaveHits,
       "dsApplIfOpsTable": dsApplIfOpsTable,
       "dsApplIfOpsEntry": dsApplIfOpsEntry,
       "dsApplIfProtocolIndex": dsApplIfProtocolIndex,
       "dsApplIfProtocol": dsApplIfProtocol,
       "dsApplIfUnauthBinds": dsApplIfUnauthBinds,
       "dsApplIfSimpleAuthBinds": dsApplIfSimpleAuthBinds,
       "dsApplIfStrongAuthBinds": dsApplIfStrongAuthBinds,
       "dsApplIfBindSecurityErrors": dsApplIfBindSecurityErrors,
       "dsApplIfInOps": dsApplIfInOps,
       "dsApplIfReadOps": dsApplIfReadOps,
       "dsApplIfCompareOps": dsApplIfCompareOps,
       "dsApplIfAddEntryOps": dsApplIfAddEntryOps,
       "dsApplIfRemoveEntryOps": dsApplIfRemoveEntryOps,
       "dsApplIfModifyEntryOps": dsApplIfModifyEntryOps,
       "dsApplIfModifyRDNOps": dsApplIfModifyRDNOps,
       "dsApplIfListOps": dsApplIfListOps,
       "dsApplIfSearchOps": dsApplIfSearchOps,
       "dsApplIfOneLevelSearchOps": dsApplIfOneLevelSearchOps,
       "dsApplIfWholeSubtreeSearchOps": dsApplIfWholeSubtreeSearchOps,
       "dsApplIfReferrals": dsApplIfReferrals,
       "dsApplIfChainings": dsApplIfChainings,
       "dsApplIfSecurityErrors": dsApplIfSecurityErrors,
       "dsApplIfErrors": dsApplIfErrors,
       "dsApplIfReplicationUpdatesIn": dsApplIfReplicationUpdatesIn,
       "dsApplIfReplicationUpdatesOut": dsApplIfReplicationUpdatesOut,
       "dsApplIfInBytes": dsApplIfInBytes,
       "dsApplIfOutBytes": dsApplIfOutBytes,
       "dsIntTable": dsIntTable,
       "dsIntEntry": dsIntEntry,
       "dsIntEntIndex": dsIntEntIndex,
       "dsIntEntDirectoryName": dsIntEntDirectoryName,
       "dsIntEntTimeOfCreation": dsIntEntTimeOfCreation,
       "dsIntEntTimeOfLastAttempt": dsIntEntTimeOfLastAttempt,
       "dsIntEntTimeOfLastSuccess": dsIntEntTimeOfLastSuccess,
       "dsIntEntFailuresSinceLastSuccess": dsIntEntFailuresSinceLastSuccess,
       "dsIntEntFailures": dsIntEntFailures,
       "dsIntEntSuccesses": dsIntEntSuccesses,
       "dsIntEntURL": dsIntEntURL,
       "dsConformance": dsConformance,
       "dsGroups": dsGroups,
       "dsEntryGroup": dsEntryGroup,
       "dsOpsGroup": dsOpsGroup,
       "dsIntGroup": dsIntGroup,
       "dsCompliances": dsCompliances,
       "dsEntryCompliance": dsEntryCompliance,
       "dsOpsCompliance": dsOpsCompliance,
       "dsIntCompliance": dsIntCompliance,
       "dsOpsIntCompliance": dsOpsIntCompliance}
)
