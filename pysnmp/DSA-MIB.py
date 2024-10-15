# SNMP MIB module (DSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:34 2024
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
 applIndex) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "DistinguishedName",
    "applIndex")

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

dsaMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsaOpsTable_Object = MibTable
dsaOpsTable = _DsaOpsTable_Object(
    (1, 3, 6, 1, 2, 1, 29, 1)
)
if mibBuilder.loadTexts:
    dsaOpsTable.setStatus("current")
_DsaOpsEntry_Object = MibTableRow
dsaOpsEntry = _DsaOpsEntry_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1)
)
dsaOpsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    dsaOpsEntry.setStatus("current")
_DsaAnonymousBinds_Type = Counter32
_DsaAnonymousBinds_Object = MibTableColumn
dsaAnonymousBinds = _DsaAnonymousBinds_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 1),
    _DsaAnonymousBinds_Type()
)
dsaAnonymousBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaAnonymousBinds.setStatus("current")
_DsaUnauthBinds_Type = Counter32
_DsaUnauthBinds_Object = MibTableColumn
dsaUnauthBinds = _DsaUnauthBinds_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 2),
    _DsaUnauthBinds_Type()
)
dsaUnauthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaUnauthBinds.setStatus("current")
_DsaSimpleAuthBinds_Type = Counter32
_DsaSimpleAuthBinds_Object = MibTableColumn
dsaSimpleAuthBinds = _DsaSimpleAuthBinds_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 3),
    _DsaSimpleAuthBinds_Type()
)
dsaSimpleAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaSimpleAuthBinds.setStatus("current")
_DsaStrongAuthBinds_Type = Counter32
_DsaStrongAuthBinds_Object = MibTableColumn
dsaStrongAuthBinds = _DsaStrongAuthBinds_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 4),
    _DsaStrongAuthBinds_Type()
)
dsaStrongAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaStrongAuthBinds.setStatus("current")
_DsaBindSecurityErrors_Type = Counter32
_DsaBindSecurityErrors_Object = MibTableColumn
dsaBindSecurityErrors = _DsaBindSecurityErrors_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 5),
    _DsaBindSecurityErrors_Type()
)
dsaBindSecurityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaBindSecurityErrors.setStatus("current")
_DsaInOps_Type = Counter32
_DsaInOps_Object = MibTableColumn
dsaInOps = _DsaInOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 6),
    _DsaInOps_Type()
)
dsaInOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaInOps.setStatus("current")
_DsaReadOps_Type = Counter32
_DsaReadOps_Object = MibTableColumn
dsaReadOps = _DsaReadOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 7),
    _DsaReadOps_Type()
)
dsaReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaReadOps.setStatus("current")
_DsaCompareOps_Type = Counter32
_DsaCompareOps_Object = MibTableColumn
dsaCompareOps = _DsaCompareOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 8),
    _DsaCompareOps_Type()
)
dsaCompareOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaCompareOps.setStatus("current")
_DsaAddEntryOps_Type = Counter32
_DsaAddEntryOps_Object = MibTableColumn
dsaAddEntryOps = _DsaAddEntryOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 9),
    _DsaAddEntryOps_Type()
)
dsaAddEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaAddEntryOps.setStatus("current")
_DsaRemoveEntryOps_Type = Counter32
_DsaRemoveEntryOps_Object = MibTableColumn
dsaRemoveEntryOps = _DsaRemoveEntryOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 10),
    _DsaRemoveEntryOps_Type()
)
dsaRemoveEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaRemoveEntryOps.setStatus("current")
_DsaModifyEntryOps_Type = Counter32
_DsaModifyEntryOps_Object = MibTableColumn
dsaModifyEntryOps = _DsaModifyEntryOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 11),
    _DsaModifyEntryOps_Type()
)
dsaModifyEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaModifyEntryOps.setStatus("current")
_DsaModifyRDNOps_Type = Counter32
_DsaModifyRDNOps_Object = MibTableColumn
dsaModifyRDNOps = _DsaModifyRDNOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 12),
    _DsaModifyRDNOps_Type()
)
dsaModifyRDNOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaModifyRDNOps.setStatus("current")
_DsaListOps_Type = Counter32
_DsaListOps_Object = MibTableColumn
dsaListOps = _DsaListOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 13),
    _DsaListOps_Type()
)
dsaListOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaListOps.setStatus("current")
_DsaSearchOps_Type = Counter32
_DsaSearchOps_Object = MibTableColumn
dsaSearchOps = _DsaSearchOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 14),
    _DsaSearchOps_Type()
)
dsaSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaSearchOps.setStatus("current")
_DsaOneLevelSearchOps_Type = Counter32
_DsaOneLevelSearchOps_Object = MibTableColumn
dsaOneLevelSearchOps = _DsaOneLevelSearchOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 15),
    _DsaOneLevelSearchOps_Type()
)
dsaOneLevelSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaOneLevelSearchOps.setStatus("current")
_DsaWholeTreeSearchOps_Type = Counter32
_DsaWholeTreeSearchOps_Object = MibTableColumn
dsaWholeTreeSearchOps = _DsaWholeTreeSearchOps_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 16),
    _DsaWholeTreeSearchOps_Type()
)
dsaWholeTreeSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaWholeTreeSearchOps.setStatus("current")
_DsaReferrals_Type = Counter32
_DsaReferrals_Object = MibTableColumn
dsaReferrals = _DsaReferrals_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 17),
    _DsaReferrals_Type()
)
dsaReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaReferrals.setStatus("current")
_DsaChainings_Type = Counter32
_DsaChainings_Object = MibTableColumn
dsaChainings = _DsaChainings_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 18),
    _DsaChainings_Type()
)
dsaChainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaChainings.setStatus("current")
_DsaSecurityErrors_Type = Counter32
_DsaSecurityErrors_Object = MibTableColumn
dsaSecurityErrors = _DsaSecurityErrors_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 19),
    _DsaSecurityErrors_Type()
)
dsaSecurityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaSecurityErrors.setStatus("current")
_DsaErrors_Type = Counter32
_DsaErrors_Object = MibTableColumn
dsaErrors = _DsaErrors_Object(
    (1, 3, 6, 1, 2, 1, 29, 1, 1, 20),
    _DsaErrors_Type()
)
dsaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaErrors.setStatus("current")
_DsaEntriesTable_Object = MibTable
dsaEntriesTable = _DsaEntriesTable_Object(
    (1, 3, 6, 1, 2, 1, 29, 2)
)
if mibBuilder.loadTexts:
    dsaEntriesTable.setStatus("current")
_DsaEntriesEntry_Object = MibTableRow
dsaEntriesEntry = _DsaEntriesEntry_Object(
    (1, 3, 6, 1, 2, 1, 29, 2, 1)
)
dsaEntriesEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    dsaEntriesEntry.setStatus("current")
_DsaMasterEntries_Type = Gauge32
_DsaMasterEntries_Object = MibTableColumn
dsaMasterEntries = _DsaMasterEntries_Object(
    (1, 3, 6, 1, 2, 1, 29, 2, 1, 1),
    _DsaMasterEntries_Type()
)
dsaMasterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaMasterEntries.setStatus("current")
_DsaCopyEntries_Type = Gauge32
_DsaCopyEntries_Object = MibTableColumn
dsaCopyEntries = _DsaCopyEntries_Object(
    (1, 3, 6, 1, 2, 1, 29, 2, 1, 2),
    _DsaCopyEntries_Type()
)
dsaCopyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaCopyEntries.setStatus("current")
_DsaCacheEntries_Type = Gauge32
_DsaCacheEntries_Object = MibTableColumn
dsaCacheEntries = _DsaCacheEntries_Object(
    (1, 3, 6, 1, 2, 1, 29, 2, 1, 3),
    _DsaCacheEntries_Type()
)
dsaCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaCacheEntries.setStatus("current")
_DsaCacheHits_Type = Counter32
_DsaCacheHits_Object = MibTableColumn
dsaCacheHits = _DsaCacheHits_Object(
    (1, 3, 6, 1, 2, 1, 29, 2, 1, 4),
    _DsaCacheHits_Type()
)
dsaCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaCacheHits.setStatus("current")
_DsaSlaveHits_Type = Counter32
_DsaSlaveHits_Object = MibTableColumn
dsaSlaveHits = _DsaSlaveHits_Object(
    (1, 3, 6, 1, 2, 1, 29, 2, 1, 5),
    _DsaSlaveHits_Type()
)
dsaSlaveHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaSlaveHits.setStatus("current")
_DsaIntTable_Object = MibTable
dsaIntTable = _DsaIntTable_Object(
    (1, 3, 6, 1, 2, 1, 29, 3)
)
if mibBuilder.loadTexts:
    dsaIntTable.setStatus("current")
_DsaIntEntry_Object = MibTableRow
dsaIntEntry = _DsaIntEntry_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1)
)
dsaIntEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "DSA-MIB", "dsaIntIndex"),
)
if mibBuilder.loadTexts:
    dsaIntEntry.setStatus("current")


class _DsaIntIndex_Type(Integer32):
    """Custom type dsaIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsaIntIndex_Type.__name__ = "Integer32"
_DsaIntIndex_Object = MibTableColumn
dsaIntIndex = _DsaIntIndex_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 1),
    _DsaIntIndex_Type()
)
dsaIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsaIntIndex.setStatus("current")
_DsaName_Type = DistinguishedName
_DsaName_Object = MibTableColumn
dsaName = _DsaName_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 2),
    _DsaName_Type()
)
dsaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaName.setStatus("current")
_DsaTimeOfCreation_Type = TimeStamp
_DsaTimeOfCreation_Object = MibTableColumn
dsaTimeOfCreation = _DsaTimeOfCreation_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 3),
    _DsaTimeOfCreation_Type()
)
dsaTimeOfCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaTimeOfCreation.setStatus("current")
_DsaTimeOfLastAttempt_Type = TimeStamp
_DsaTimeOfLastAttempt_Object = MibTableColumn
dsaTimeOfLastAttempt = _DsaTimeOfLastAttempt_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 4),
    _DsaTimeOfLastAttempt_Type()
)
dsaTimeOfLastAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaTimeOfLastAttempt.setStatus("current")
_DsaTimeOfLastSuccess_Type = TimeStamp
_DsaTimeOfLastSuccess_Object = MibTableColumn
dsaTimeOfLastSuccess = _DsaTimeOfLastSuccess_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 5),
    _DsaTimeOfLastSuccess_Type()
)
dsaTimeOfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaTimeOfLastSuccess.setStatus("current")
_DsaFailuresSinceLastSuccess_Type = Counter32
_DsaFailuresSinceLastSuccess_Object = MibTableColumn
dsaFailuresSinceLastSuccess = _DsaFailuresSinceLastSuccess_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 6),
    _DsaFailuresSinceLastSuccess_Type()
)
dsaFailuresSinceLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaFailuresSinceLastSuccess.setStatus("current")
_DsaFailures_Type = Counter32
_DsaFailures_Object = MibTableColumn
dsaFailures = _DsaFailures_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 7),
    _DsaFailures_Type()
)
dsaFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaFailures.setStatus("current")
_DsaSuccesses_Type = Counter32
_DsaSuccesses_Object = MibTableColumn
dsaSuccesses = _DsaSuccesses_Object(
    (1, 3, 6, 1, 2, 1, 29, 3, 1, 8),
    _DsaSuccesses_Type()
)
dsaSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaSuccesses.setStatus("current")
_DsaConformance_ObjectIdentity = ObjectIdentity
dsaConformance = _DsaConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 29, 4)
)
_DsaGroups_ObjectIdentity = ObjectIdentity
dsaGroups = _DsaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 29, 4, 1)
)
_DsaCompliances_ObjectIdentity = ObjectIdentity
dsaCompliances = _DsaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 29, 4, 2)
)

# Managed Objects groups

dsaOpsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 29, 4, 1, 1)
)
dsaOpsGroup.setObjects(
      *(("DSA-MIB", "dsaAnonymousBinds"),
        ("DSA-MIB", "dsaUnauthBinds"),
        ("DSA-MIB", "dsaSimpleAuthBinds"),
        ("DSA-MIB", "dsaStrongAuthBinds"),
        ("DSA-MIB", "dsaBindSecurityErrors"),
        ("DSA-MIB", "dsaInOps"),
        ("DSA-MIB", "dsaReadOps"),
        ("DSA-MIB", "dsaCompareOps"),
        ("DSA-MIB", "dsaAddEntryOps"),
        ("DSA-MIB", "dsaRemoveEntryOps"),
        ("DSA-MIB", "dsaModifyEntryOps"),
        ("DSA-MIB", "dsaModifyRDNOps"),
        ("DSA-MIB", "dsaListOps"),
        ("DSA-MIB", "dsaSearchOps"),
        ("DSA-MIB", "dsaOneLevelSearchOps"),
        ("DSA-MIB", "dsaWholeTreeSearchOps"),
        ("DSA-MIB", "dsaReferrals"),
        ("DSA-MIB", "dsaChainings"),
        ("DSA-MIB", "dsaSecurityErrors"),
        ("DSA-MIB", "dsaErrors"))
)
if mibBuilder.loadTexts:
    dsaOpsGroup.setStatus("current")

dsaEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 29, 4, 1, 2)
)
dsaEntryGroup.setObjects(
      *(("DSA-MIB", "dsaMasterEntries"),
        ("DSA-MIB", "dsaCopyEntries"),
        ("DSA-MIB", "dsaCacheEntries"),
        ("DSA-MIB", "dsaCacheHits"),
        ("DSA-MIB", "dsaSlaveHits"))
)
if mibBuilder.loadTexts:
    dsaEntryGroup.setStatus("current")

dsaIntGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 29, 4, 1, 3)
)
dsaIntGroup.setObjects(
      *(("DSA-MIB", "dsaName"),
        ("DSA-MIB", "dsaTimeOfCreation"),
        ("DSA-MIB", "dsaTimeOfLastAttempt"),
        ("DSA-MIB", "dsaTimeOfLastSuccess"),
        ("DSA-MIB", "dsaFailuresSinceLastSuccess"),
        ("DSA-MIB", "dsaFailures"),
        ("DSA-MIB", "dsaSuccesses"))
)
if mibBuilder.loadTexts:
    dsaIntGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsaOpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 29, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dsaOpsCompliance.setStatus(
        "current"
    )

dsaEntryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 29, 4, 2, 2)
)
if mibBuilder.loadTexts:
    dsaEntryCompliance.setStatus(
        "current"
    )

dsaIntCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 29, 4, 2, 3)
)
if mibBuilder.loadTexts:
    dsaIntCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSA-MIB",
    **{"dsaMIB": dsaMIB,
       "dsaOpsTable": dsaOpsTable,
       "dsaOpsEntry": dsaOpsEntry,
       "dsaAnonymousBinds": dsaAnonymousBinds,
       "dsaUnauthBinds": dsaUnauthBinds,
       "dsaSimpleAuthBinds": dsaSimpleAuthBinds,
       "dsaStrongAuthBinds": dsaStrongAuthBinds,
       "dsaBindSecurityErrors": dsaBindSecurityErrors,
       "dsaInOps": dsaInOps,
       "dsaReadOps": dsaReadOps,
       "dsaCompareOps": dsaCompareOps,
       "dsaAddEntryOps": dsaAddEntryOps,
       "dsaRemoveEntryOps": dsaRemoveEntryOps,
       "dsaModifyEntryOps": dsaModifyEntryOps,
       "dsaModifyRDNOps": dsaModifyRDNOps,
       "dsaListOps": dsaListOps,
       "dsaSearchOps": dsaSearchOps,
       "dsaOneLevelSearchOps": dsaOneLevelSearchOps,
       "dsaWholeTreeSearchOps": dsaWholeTreeSearchOps,
       "dsaReferrals": dsaReferrals,
       "dsaChainings": dsaChainings,
       "dsaSecurityErrors": dsaSecurityErrors,
       "dsaErrors": dsaErrors,
       "dsaEntriesTable": dsaEntriesTable,
       "dsaEntriesEntry": dsaEntriesEntry,
       "dsaMasterEntries": dsaMasterEntries,
       "dsaCopyEntries": dsaCopyEntries,
       "dsaCacheEntries": dsaCacheEntries,
       "dsaCacheHits": dsaCacheHits,
       "dsaSlaveHits": dsaSlaveHits,
       "dsaIntTable": dsaIntTable,
       "dsaIntEntry": dsaIntEntry,
       "dsaIntIndex": dsaIntIndex,
       "dsaName": dsaName,
       "dsaTimeOfCreation": dsaTimeOfCreation,
       "dsaTimeOfLastAttempt": dsaTimeOfLastAttempt,
       "dsaTimeOfLastSuccess": dsaTimeOfLastSuccess,
       "dsaFailuresSinceLastSuccess": dsaFailuresSinceLastSuccess,
       "dsaFailures": dsaFailures,
       "dsaSuccesses": dsaSuccesses,
       "dsaConformance": dsaConformance,
       "dsaGroups": dsaGroups,
       "dsaOpsGroup": dsaOpsGroup,
       "dsaEntryGroup": dsaEntryGroup,
       "dsaIntGroup": dsaIntGroup,
       "dsaCompliances": dsaCompliances,
       "dsaOpsCompliance": dsaOpsCompliance,
       "dsaEntryCompliance": dsaEntryCompliance,
       "dsaIntCompliance": dsaIntCompliance}
)
