# SNMP MIB module (NSLDAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSLDAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:33 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

nsldap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1450, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netscape_ObjectIdentity = ObjectIdentity
netscape = _Netscape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1450)
)
_DsOpsTable_Object = MibTable
dsOpsTable = _DsOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1)
)
if mibBuilder.loadTexts:
    dsOpsTable.setStatus("current")
_DsOpsEntry_Object = MibTableRow
dsOpsEntry = _DsOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1)
)
dsOpsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    dsOpsEntry.setStatus("current")
_DsAnonymousBinds_Type = Counter32
_DsAnonymousBinds_Object = MibTableColumn
dsAnonymousBinds = _DsAnonymousBinds_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 1),
    _DsAnonymousBinds_Type()
)
dsAnonymousBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAnonymousBinds.setStatus("current")
_DsUnAuthBinds_Type = Counter32
_DsUnAuthBinds_Object = MibTableColumn
dsUnAuthBinds = _DsUnAuthBinds_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 2),
    _DsUnAuthBinds_Type()
)
dsUnAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsUnAuthBinds.setStatus("current")
_DsSimpleAuthBinds_Type = Counter32
_DsSimpleAuthBinds_Object = MibTableColumn
dsSimpleAuthBinds = _DsSimpleAuthBinds_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 3),
    _DsSimpleAuthBinds_Type()
)
dsSimpleAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSimpleAuthBinds.setStatus("current")
_DsStrongAuthBinds_Type = Counter32
_DsStrongAuthBinds_Object = MibTableColumn
dsStrongAuthBinds = _DsStrongAuthBinds_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 4),
    _DsStrongAuthBinds_Type()
)
dsStrongAuthBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsStrongAuthBinds.setStatus("current")
_DsBindSecurityErrors_Type = Counter32
_DsBindSecurityErrors_Object = MibTableColumn
dsBindSecurityErrors = _DsBindSecurityErrors_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 5),
    _DsBindSecurityErrors_Type()
)
dsBindSecurityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBindSecurityErrors.setStatus("current")
_DsInOps_Type = Counter32
_DsInOps_Object = MibTableColumn
dsInOps = _DsInOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 6),
    _DsInOps_Type()
)
dsInOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsInOps.setStatus("current")
_DsReadOps_Type = Counter32
_DsReadOps_Object = MibTableColumn
dsReadOps = _DsReadOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 7),
    _DsReadOps_Type()
)
dsReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsReadOps.setStatus("current")
_DsCompareOps_Type = Counter32
_DsCompareOps_Object = MibTableColumn
dsCompareOps = _DsCompareOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 8),
    _DsCompareOps_Type()
)
dsCompareOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCompareOps.setStatus("current")
_DsAddEntryOps_Type = Counter32
_DsAddEntryOps_Object = MibTableColumn
dsAddEntryOps = _DsAddEntryOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 9),
    _DsAddEntryOps_Type()
)
dsAddEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAddEntryOps.setStatus("current")
_DsRemoveEntryOps_Type = Counter32
_DsRemoveEntryOps_Object = MibTableColumn
dsRemoveEntryOps = _DsRemoveEntryOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 10),
    _DsRemoveEntryOps_Type()
)
dsRemoveEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRemoveEntryOps.setStatus("current")
_DsModifyEntryOps_Type = Counter32
_DsModifyEntryOps_Object = MibTableColumn
dsModifyEntryOps = _DsModifyEntryOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 11),
    _DsModifyEntryOps_Type()
)
dsModifyEntryOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsModifyEntryOps.setStatus("current")
_DsModifyRDNOps_Type = Counter32
_DsModifyRDNOps_Object = MibTableColumn
dsModifyRDNOps = _DsModifyRDNOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 12),
    _DsModifyRDNOps_Type()
)
dsModifyRDNOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsModifyRDNOps.setStatus("current")
_DsListOps_Type = Counter32
_DsListOps_Object = MibTableColumn
dsListOps = _DsListOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 13),
    _DsListOps_Type()
)
dsListOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsListOps.setStatus("current")
_DsSearchOps_Type = Counter32
_DsSearchOps_Object = MibTableColumn
dsSearchOps = _DsSearchOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 14),
    _DsSearchOps_Type()
)
dsSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSearchOps.setStatus("current")
_DsOneLevelSearchOps_Type = Counter32
_DsOneLevelSearchOps_Object = MibTableColumn
dsOneLevelSearchOps = _DsOneLevelSearchOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 15),
    _DsOneLevelSearchOps_Type()
)
dsOneLevelSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsOneLevelSearchOps.setStatus("current")
_DsWholeSubtreeSearchOps_Type = Counter32
_DsWholeSubtreeSearchOps_Object = MibTableColumn
dsWholeSubtreeSearchOps = _DsWholeSubtreeSearchOps_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 16),
    _DsWholeSubtreeSearchOps_Type()
)
dsWholeSubtreeSearchOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsWholeSubtreeSearchOps.setStatus("current")
_DsReferrals_Type = Counter32
_DsReferrals_Object = MibTableColumn
dsReferrals = _DsReferrals_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 17),
    _DsReferrals_Type()
)
dsReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsReferrals.setStatus("current")
_DsChainings_Type = Counter32
_DsChainings_Object = MibTableColumn
dsChainings = _DsChainings_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 18),
    _DsChainings_Type()
)
dsChainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsChainings.setStatus("current")
_DsSecurityErrors_Type = Counter32
_DsSecurityErrors_Object = MibTableColumn
dsSecurityErrors = _DsSecurityErrors_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 19),
    _DsSecurityErrors_Type()
)
dsSecurityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSecurityErrors.setStatus("current")
_DsErrors_Type = Counter32
_DsErrors_Object = MibTableColumn
dsErrors = _DsErrors_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 20),
    _DsErrors_Type()
)
dsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsErrors.setStatus("current")
_DsEntriesTable_Object = MibTable
dsEntriesTable = _DsEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2)
)
if mibBuilder.loadTexts:
    dsEntriesTable.setStatus("current")
_DsEntriesEntry_Object = MibTableRow
dsEntriesEntry = _DsEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2, 1)
)
dsEntriesEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    dsEntriesEntry.setStatus("current")
_DsMasterEntries_Type = Gauge32
_DsMasterEntries_Object = MibTableColumn
dsMasterEntries = _DsMasterEntries_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 1),
    _DsMasterEntries_Type()
)
dsMasterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMasterEntries.setStatus("current")
_DsCopyEntries_Type = Gauge32
_DsCopyEntries_Object = MibTableColumn
dsCopyEntries = _DsCopyEntries_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 2),
    _DsCopyEntries_Type()
)
dsCopyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCopyEntries.setStatus("current")
_DsCacheEntries_Type = Gauge32
_DsCacheEntries_Object = MibTableColumn
dsCacheEntries = _DsCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 3),
    _DsCacheEntries_Type()
)
dsCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCacheEntries.setStatus("current")
_DsCacheHits_Type = Counter32
_DsCacheHits_Object = MibTableColumn
dsCacheHits = _DsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 4),
    _DsCacheHits_Type()
)
dsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCacheHits.setStatus("current")
_DsSlaveHits_Type = Counter32
_DsSlaveHits_Object = MibTableColumn
dsSlaveHits = _DsSlaveHits_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 5),
    _DsSlaveHits_Type()
)
dsSlaveHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlaveHits.setStatus("current")
_DsIntTable_Object = MibTable
dsIntTable = _DsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3)
)
if mibBuilder.loadTexts:
    dsIntTable.setStatus("current")
_DsIntEntry_Object = MibTableRow
dsIntEntry = _DsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1)
)
dsIntEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "NSLDAP-MIB", "dsIntIndex"),
)
if mibBuilder.loadTexts:
    dsIntEntry.setStatus("current")


class _DsIntIndex_Type(Integer32):
    """Custom type dsIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsIntIndex_Type.__name__ = "Integer32"
_DsIntIndex_Object = MibTableColumn
dsIntIndex = _DsIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 1),
    _DsIntIndex_Type()
)
dsIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsIntIndex.setStatus("current")
_DsName_Type = DistinguishedName
_DsName_Object = MibTableColumn
dsName = _DsName_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 2),
    _DsName_Type()
)
dsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsName.setStatus("current")
_DsTimeOfCreation_Type = TimeStamp
_DsTimeOfCreation_Object = MibTableColumn
dsTimeOfCreation = _DsTimeOfCreation_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 3),
    _DsTimeOfCreation_Type()
)
dsTimeOfCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsTimeOfCreation.setStatus("current")
_DsTimeOfLastAttempt_Type = TimeStamp
_DsTimeOfLastAttempt_Object = MibTableColumn
dsTimeOfLastAttempt = _DsTimeOfLastAttempt_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 4),
    _DsTimeOfLastAttempt_Type()
)
dsTimeOfLastAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsTimeOfLastAttempt.setStatus("current")
_DsTimeOfLastSuccess_Type = TimeStamp
_DsTimeOfLastSuccess_Object = MibTableColumn
dsTimeOfLastSuccess = _DsTimeOfLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 5),
    _DsTimeOfLastSuccess_Type()
)
dsTimeOfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsTimeOfLastSuccess.setStatus("current")
_DsFailuresSinceLastSuccess_Type = Counter32
_DsFailuresSinceLastSuccess_Object = MibTableColumn
dsFailuresSinceLastSuccess = _DsFailuresSinceLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 6),
    _DsFailuresSinceLastSuccess_Type()
)
dsFailuresSinceLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFailuresSinceLastSuccess.setStatus("current")
_DsFailures_Type = Counter32
_DsFailures_Object = MibTableColumn
dsFailures = _DsFailures_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 7),
    _DsFailures_Type()
)
dsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFailures.setStatus("current")
_DsSuccesses_Type = Counter32
_DsSuccesses_Object = MibTableColumn
dsSuccesses = _DsSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 8),
    _DsSuccesses_Type()
)
dsSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSuccesses.setStatus("current")
_DsURL_Type = URLString
_DsURL_Object = MibTableColumn
dsURL = _DsURL_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 9),
    _DsURL_Type()
)
dsURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsURL.setStatus("current")
_DsEntityTable_Object = MibTable
dsEntityTable = _DsEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5)
)
if mibBuilder.loadTexts:
    dsEntityTable.setStatus("current")
_DsEntityEntry_Object = MibTableRow
dsEntityEntry = _DsEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1)
)
dsEntityEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    dsEntityEntry.setStatus("current")


class _DsEntityDescr_Type(DisplayString):
    """Custom type dsEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsEntityDescr_Type.__name__ = "DisplayString"
_DsEntityDescr_Object = MibTableColumn
dsEntityDescr = _DsEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 1),
    _DsEntityDescr_Type()
)
dsEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsEntityDescr.setStatus("mandatory")


class _DsEntityVers_Type(DisplayString):
    """Custom type dsEntityVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsEntityVers_Type.__name__ = "DisplayString"
_DsEntityVers_Object = MibTableColumn
dsEntityVers = _DsEntityVers_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 2),
    _DsEntityVers_Type()
)
dsEntityVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsEntityVers.setStatus("mandatory")


class _DsEntityOrg_Type(DisplayString):
    """Custom type dsEntityOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsEntityOrg_Type.__name__ = "DisplayString"
_DsEntityOrg_Object = MibTableColumn
dsEntityOrg = _DsEntityOrg_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 3),
    _DsEntityOrg_Type()
)
dsEntityOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsEntityOrg.setStatus("mandatory")


class _DsEntityLocation_Type(DisplayString):
    """Custom type dsEntityLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsEntityLocation_Type.__name__ = "DisplayString"
_DsEntityLocation_Object = MibTableColumn
dsEntityLocation = _DsEntityLocation_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 4),
    _DsEntityLocation_Type()
)
dsEntityLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsEntityLocation.setStatus("mandatory")


class _DsEntityContact_Type(DisplayString):
    """Custom type dsEntityContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsEntityContact_Type.__name__ = "DisplayString"
_DsEntityContact_Object = MibTableColumn
dsEntityContact = _DsEntityContact_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 5),
    _DsEntityContact_Type()
)
dsEntityContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsEntityContact.setStatus("mandatory")


class _DsEntityName_Type(DisplayString):
    """Custom type dsEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsEntityName_Type.__name__ = "DisplayString"
_DsEntityName_Object = MibTableColumn
dsEntityName = _DsEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 6),
    _DsEntityName_Type()
)
dsEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsEntityName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nsDirectoryServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1450, 0, 7001)
)
nsDirectoryServerDown.setObjects(
      *(("NSLDAP-MIB", "dsEntityDescr"),
        ("NSLDAP-MIB", "dsEntityVers"),
        ("NSLDAP-MIB", "dsEntityLocation"),
        ("NSLDAP-MIB", "dsEntityContact"))
)
if mibBuilder.loadTexts:
    nsDirectoryServerDown.setStatus(
        ""
    )

nsDirectoryServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1450, 0, 7002)
)
nsDirectoryServerStart.setObjects(
      *(("NSLDAP-MIB", "dsEntityDescr"),
        ("NSLDAP-MIB", "dsEntityVers"),
        ("NSLDAP-MIB", "dsEntityLocation"))
)
if mibBuilder.loadTexts:
    nsDirectoryServerStart.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSLDAP-MIB",
    **{"netscape": netscape,
       "nsDirectoryServerDown": nsDirectoryServerDown,
       "nsDirectoryServerStart": nsDirectoryServerStart,
       "nsldap": nsldap,
       "dsOpsTable": dsOpsTable,
       "dsOpsEntry": dsOpsEntry,
       "dsAnonymousBinds": dsAnonymousBinds,
       "dsUnAuthBinds": dsUnAuthBinds,
       "dsSimpleAuthBinds": dsSimpleAuthBinds,
       "dsStrongAuthBinds": dsStrongAuthBinds,
       "dsBindSecurityErrors": dsBindSecurityErrors,
       "dsInOps": dsInOps,
       "dsReadOps": dsReadOps,
       "dsCompareOps": dsCompareOps,
       "dsAddEntryOps": dsAddEntryOps,
       "dsRemoveEntryOps": dsRemoveEntryOps,
       "dsModifyEntryOps": dsModifyEntryOps,
       "dsModifyRDNOps": dsModifyRDNOps,
       "dsListOps": dsListOps,
       "dsSearchOps": dsSearchOps,
       "dsOneLevelSearchOps": dsOneLevelSearchOps,
       "dsWholeSubtreeSearchOps": dsWholeSubtreeSearchOps,
       "dsReferrals": dsReferrals,
       "dsChainings": dsChainings,
       "dsSecurityErrors": dsSecurityErrors,
       "dsErrors": dsErrors,
       "dsEntriesTable": dsEntriesTable,
       "dsEntriesEntry": dsEntriesEntry,
       "dsMasterEntries": dsMasterEntries,
       "dsCopyEntries": dsCopyEntries,
       "dsCacheEntries": dsCacheEntries,
       "dsCacheHits": dsCacheHits,
       "dsSlaveHits": dsSlaveHits,
       "dsIntTable": dsIntTable,
       "dsIntEntry": dsIntEntry,
       "dsIntIndex": dsIntIndex,
       "dsName": dsName,
       "dsTimeOfCreation": dsTimeOfCreation,
       "dsTimeOfLastAttempt": dsTimeOfLastAttempt,
       "dsTimeOfLastSuccess": dsTimeOfLastSuccess,
       "dsFailuresSinceLastSuccess": dsFailuresSinceLastSuccess,
       "dsFailures": dsFailures,
       "dsSuccesses": dsSuccesses,
       "dsURL": dsURL,
       "dsEntityTable": dsEntityTable,
       "dsEntityEntry": dsEntityEntry,
       "dsEntityDescr": dsEntityDescr,
       "dsEntityVers": dsEntityVers,
       "dsEntityOrg": dsEntityOrg,
       "dsEntityLocation": dsEntityLocation,
       "dsEntityContact": dsEntityContact,
       "dsEntityName": dsEntityName}
)
