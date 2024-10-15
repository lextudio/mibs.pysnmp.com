# SNMP MIB module (INFORMANT-WMI-CITRIX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-WMI-CITRIX
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:21 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(WtcsDisplayString,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "WtcsDisplayString",
    "informant")


# MODULE-IDENTITY

citrixWmi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42)
)
citrixWmi.setRevisions(
        ("2008-06-02 17:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CitrixWmiCitrix_ObjectIdentity = ObjectIdentity
citrixWmiCitrix = _CitrixWmiCitrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1)
)
if mibBuilder.loadTexts:
    citrixWmiCitrix.setStatus("current")
_CitrixAccountAuthorityTable_Object = MibTable
citrixAccountAuthorityTable = _CitrixAccountAuthorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 1)
)
if mibBuilder.loadTexts:
    citrixAccountAuthorityTable.setStatus("current")
_CitrixAccountAuthorityEntry_Object = MibTableRow
citrixAccountAuthorityEntry = _CitrixAccountAuthorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 1, 1)
)
citrixAccountAuthorityEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxAccountAuthorityIndex"),
)
if mibBuilder.loadTexts:
    citrixAccountAuthorityEntry.setStatus("current")


class _CtxAccountAuthorityIndex_Type(Integer32):
    """Custom type ctxAccountAuthorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxAccountAuthorityIndex_Type.__name__ = "Integer32"
_CtxAccountAuthorityIndex_Object = MibTableColumn
ctxAccountAuthorityIndex = _CtxAccountAuthorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 1, 1, 1),
    _CtxAccountAuthorityIndex_Type()
)
ctxAccountAuthorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAccountAuthorityIndex.setStatus("current")
_CtxAccountAuthorityName_Type = WtcsDisplayString
_CtxAccountAuthorityName_Object = MibTableColumn
ctxAccountAuthorityName = _CtxAccountAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 1, 1, 2),
    _CtxAccountAuthorityName_Type()
)
ctxAccountAuthorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAccountAuthorityName.setStatus("current")


class _CtxAccountAuthorityType_Type(Integer32):
    """Custom type ctxAccountAuthorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknownAccountAuthority", 0),
          ("windowsNTDomainOrADS", 1))
    )


_CtxAccountAuthorityType_Type.__name__ = "Integer32"
_CtxAccountAuthorityType_Object = MibTableColumn
ctxAccountAuthorityType = _CtxAccountAuthorityType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 1, 1, 3),
    _CtxAccountAuthorityType_Type()
)
ctxAccountAuthorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAccountAuthorityType.setStatus("current")
_CitrixApplicationFolderTable_Object = MibTable
citrixApplicationFolderTable = _CitrixApplicationFolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 2)
)
if mibBuilder.loadTexts:
    citrixApplicationFolderTable.setStatus("current")
_CitrixApplicationFolderEntry_Object = MibTableRow
citrixApplicationFolderEntry = _CitrixApplicationFolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 2, 1)
)
citrixApplicationFolderEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxApplicationFolderIndex"),
)
if mibBuilder.loadTexts:
    citrixApplicationFolderEntry.setStatus("current")


class _CtxApplicationFolderIndex_Type(Integer32):
    """Custom type ctxApplicationFolderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxApplicationFolderIndex_Type.__name__ = "Integer32"
_CtxApplicationFolderIndex_Object = MibTableColumn
ctxApplicationFolderIndex = _CtxApplicationFolderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 2, 1, 1),
    _CtxApplicationFolderIndex_Type()
)
ctxApplicationFolderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxApplicationFolderIndex.setStatus("current")
_CtxApplicationFolderFolderDN_Type = WtcsDisplayString
_CtxApplicationFolderFolderDN_Object = MibTableColumn
ctxApplicationFolderFolderDN = _CtxApplicationFolderFolderDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 2, 1, 2),
    _CtxApplicationFolderFolderDN_Type()
)
ctxApplicationFolderFolderDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxApplicationFolderFolderDN.setStatus("current")
_CtxApplicationFolderFolderName_Type = WtcsDisplayString
_CtxApplicationFolderFolderName_Object = MibTableColumn
ctxApplicationFolderFolderName = _CtxApplicationFolderFolderName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 2, 1, 3),
    _CtxApplicationFolderFolderName_Type()
)
ctxApplicationFolderFolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxApplicationFolderFolderName.setStatus("current")
_CitrixGroupTable_Object = MibTable
citrixGroupTable = _CitrixGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 3)
)
if mibBuilder.loadTexts:
    citrixGroupTable.setStatus("current")
_CitrixGroupEntry_Object = MibTableRow
citrixGroupEntry = _CitrixGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 3, 1)
)
citrixGroupEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxGroupIndex"),
)
if mibBuilder.loadTexts:
    citrixGroupEntry.setStatus("current")


class _CtxGroupIndex_Type(Integer32):
    """Custom type ctxGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxGroupIndex_Type.__name__ = "Integer32"
_CtxGroupIndex_Object = MibTableColumn
ctxGroupIndex = _CtxGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 3, 1, 1),
    _CtxGroupIndex_Type()
)
ctxGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGroupIndex.setStatus("current")
_CtxGroupAccAuthority_Type = WtcsDisplayString
_CtxGroupAccAuthority_Object = MibTableColumn
ctxGroupAccAuthority = _CtxGroupAccAuthority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 3, 1, 2),
    _CtxGroupAccAuthority_Type()
)
ctxGroupAccAuthority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGroupAccAuthority.setStatus("current")


class _CtxGroupAccountType_Type(Integer32):
    """Custom type ctxGroupAccountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("domainLocalGroup", 4),
          ("globalGroup", 2),
          ("localGroup", 1),
          ("universalGroup", 3),
          ("unknownAccountType", 0))
    )


_CtxGroupAccountType_Type.__name__ = "Integer32"
_CtxGroupAccountType_Object = MibTableColumn
ctxGroupAccountType = _CtxGroupAccountType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 3, 1, 3),
    _CtxGroupAccountType_Type()
)
ctxGroupAccountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGroupAccountType.setStatus("current")
_CtxGroupGroupName_Type = WtcsDisplayString
_CtxGroupGroupName_Object = MibTableColumn
ctxGroupGroupName = _CtxGroupGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 3, 1, 4),
    _CtxGroupGroupName_Type()
)
ctxGroupGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGroupGroupName.setStatus("current")
_CitrixServerFolderTable_Object = MibTable
citrixServerFolderTable = _CitrixServerFolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 4)
)
if mibBuilder.loadTexts:
    citrixServerFolderTable.setStatus("current")
_CitrixServerFolderEntry_Object = MibTableRow
citrixServerFolderEntry = _CitrixServerFolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 4, 1)
)
citrixServerFolderEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxServerFolderIndex"),
)
if mibBuilder.loadTexts:
    citrixServerFolderEntry.setStatus("current")


class _CtxServerFolderIndex_Type(Integer32):
    """Custom type ctxServerFolderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxServerFolderIndex_Type.__name__ = "Integer32"
_CtxServerFolderIndex_Object = MibTableColumn
ctxServerFolderIndex = _CtxServerFolderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 4, 1, 1),
    _CtxServerFolderIndex_Type()
)
ctxServerFolderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServerFolderIndex.setStatus("current")
_CtxServerFolderFolderDN_Type = WtcsDisplayString
_CtxServerFolderFolderDN_Object = MibTableColumn
ctxServerFolderFolderDN = _CtxServerFolderFolderDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 4, 1, 2),
    _CtxServerFolderFolderDN_Type()
)
ctxServerFolderFolderDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServerFolderFolderDN.setStatus("current")
_CtxServerFolderFolderName_Type = WtcsDisplayString
_CtxServerFolderFolderName_Object = MibTableColumn
ctxServerFolderFolderName = _CtxServerFolderFolderName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 4, 1, 3),
    _CtxServerFolderFolderName_Type()
)
ctxServerFolderFolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServerFolderFolderName.setStatus("current")
_CitrixServersInFolderTable_Object = MibTable
citrixServersInFolderTable = _CitrixServersInFolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 5)
)
if mibBuilder.loadTexts:
    citrixServersInFolderTable.setStatus("current")
_CitrixServersInFolderEntry_Object = MibTableRow
citrixServersInFolderEntry = _CitrixServersInFolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 5, 1)
)
citrixServersInFolderEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxServersInFolderIndex"),
)
if mibBuilder.loadTexts:
    citrixServersInFolderEntry.setStatus("current")


class _CtxServersInFolderIndex_Type(Integer32):
    """Custom type ctxServersInFolderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxServersInFolderIndex_Type.__name__ = "Integer32"
_CtxServersInFolderIndex_Object = MibTableColumn
ctxServersInFolderIndex = _CtxServersInFolderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 5, 1, 1),
    _CtxServersInFolderIndex_Type()
)
ctxServersInFolderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServersInFolderIndex.setStatus("current")
_CtxServersInFolderAntecedent_Type = WtcsDisplayString
_CtxServersInFolderAntecedent_Object = MibTableColumn
ctxServersInFolderAntecedent = _CtxServersInFolderAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 5, 1, 2),
    _CtxServersInFolderAntecedent_Type()
)
ctxServersInFolderAntecedent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServersInFolderAntecedent.setStatus("current")
_CtxServersInFolderDependent_Type = WtcsDisplayString
_CtxServersInFolderDependent_Object = MibTableColumn
ctxServersInFolderDependent = _CtxServersInFolderDependent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 5, 1, 3),
    _CtxServersInFolderDependent_Type()
)
ctxServersInFolderDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServersInFolderDependent.setStatus("current")
_CitrixServersInZoneTable_Object = MibTable
citrixServersInZoneTable = _CitrixServersInZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 6)
)
if mibBuilder.loadTexts:
    citrixServersInZoneTable.setStatus("current")
_CitrixServersInZoneEntry_Object = MibTableRow
citrixServersInZoneEntry = _CitrixServersInZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 6, 1)
)
citrixServersInZoneEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxServersInZoneIndex"),
)
if mibBuilder.loadTexts:
    citrixServersInZoneEntry.setStatus("current")


class _CtxServersInZoneIndex_Type(Integer32):
    """Custom type ctxServersInZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxServersInZoneIndex_Type.__name__ = "Integer32"
_CtxServersInZoneIndex_Object = MibTableColumn
ctxServersInZoneIndex = _CtxServersInZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 6, 1, 1),
    _CtxServersInZoneIndex_Type()
)
ctxServersInZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServersInZoneIndex.setStatus("current")
_CtxServersInZoneServer_Type = WtcsDisplayString
_CtxServersInZoneServer_Object = MibTableColumn
ctxServersInZoneServer = _CtxServersInZoneServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 6, 1, 2),
    _CtxServersInZoneServer_Type()
)
ctxServersInZoneServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServersInZoneServer.setStatus("current")
_CtxServersInZoneZone_Type = WtcsDisplayString
_CtxServersInZoneZone_Object = MibTableColumn
ctxServersInZoneZone = _CtxServersInZoneZone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 6, 1, 3),
    _CtxServersInZoneZone_Type()
)
ctxServersInZoneZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServersInZoneZone.setStatus("current")
_CitrixUserTable_Object = MibTable
citrixUserTable = _CitrixUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 7)
)
if mibBuilder.loadTexts:
    citrixUserTable.setStatus("current")
_CitrixUserEntry_Object = MibTableRow
citrixUserEntry = _CitrixUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 7, 1)
)
citrixUserEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxUserIndex"),
)
if mibBuilder.loadTexts:
    citrixUserEntry.setStatus("current")


class _CtxUserIndex_Type(Integer32):
    """Custom type ctxUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxUserIndex_Type.__name__ = "Integer32"
_CtxUserIndex_Object = MibTableColumn
ctxUserIndex = _CtxUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 7, 1, 1),
    _CtxUserIndex_Type()
)
ctxUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUserIndex.setStatus("current")
_CtxUserAccAuthority_Type = WtcsDisplayString
_CtxUserAccAuthority_Object = MibTableColumn
ctxUserAccAuthority = _CtxUserAccAuthority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 7, 1, 2),
    _CtxUserAccAuthority_Type()
)
ctxUserAccAuthority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUserAccAuthority.setStatus("current")


class _CtxUserAccountType_Type(Integer32):
    """Custom type ctxUserAccountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domainUser", 2),
          ("localUser", 1),
          ("unknownAccountType", 0))
    )


_CtxUserAccountType_Type.__name__ = "Integer32"
_CtxUserAccountType_Object = MibTableColumn
ctxUserAccountType = _CtxUserAccountType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 7, 1, 3),
    _CtxUserAccountType_Type()
)
ctxUserAccountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUserAccountType.setStatus("current")
_CtxUserUserName_Type = WtcsDisplayString
_CtxUserUserName_Object = MibTableColumn
ctxUserUserName = _CtxUserUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 7, 1, 4),
    _CtxUserUserName_Type()
)
ctxUserUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUserUserName.setStatus("current")
_CitrixUsersInGroupTable_Object = MibTable
citrixUsersInGroupTable = _CitrixUsersInGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 8)
)
if mibBuilder.loadTexts:
    citrixUsersInGroupTable.setStatus("current")
_CitrixUsersInGroupEntry_Object = MibTableRow
citrixUsersInGroupEntry = _CitrixUsersInGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 8, 1)
)
citrixUsersInGroupEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxUsersInGroupIndex"),
)
if mibBuilder.loadTexts:
    citrixUsersInGroupEntry.setStatus("current")


class _CtxUsersInGroupIndex_Type(Integer32):
    """Custom type ctxUsersInGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxUsersInGroupIndex_Type.__name__ = "Integer32"
_CtxUsersInGroupIndex_Object = MibTableColumn
ctxUsersInGroupIndex = _CtxUsersInGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 8, 1, 1),
    _CtxUsersInGroupIndex_Type()
)
ctxUsersInGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUsersInGroupIndex.setStatus("current")
_CtxUsersInGroupAntecedent_Type = WtcsDisplayString
_CtxUsersInGroupAntecedent_Object = MibTableColumn
ctxUsersInGroupAntecedent = _CtxUsersInGroupAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 8, 1, 2),
    _CtxUsersInGroupAntecedent_Type()
)
ctxUsersInGroupAntecedent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUsersInGroupAntecedent.setStatus("current")
_CtxUsersInGroupDependent_Type = WtcsDisplayString
_CtxUsersInGroupDependent_Object = MibTableColumn
ctxUsersInGroupDependent = _CtxUsersInGroupDependent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 8, 1, 3),
    _CtxUsersInGroupDependent_Type()
)
ctxUsersInGroupDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxUsersInGroupDependent.setStatus("current")
_CitrixZoneTable_Object = MibTable
citrixZoneTable = _CitrixZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 9)
)
if mibBuilder.loadTexts:
    citrixZoneTable.setStatus("current")
_CitrixZoneEntry_Object = MibTableRow
citrixZoneEntry = _CitrixZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 9, 1)
)
citrixZoneEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxZoneIndex"),
)
if mibBuilder.loadTexts:
    citrixZoneEntry.setStatus("current")


class _CtxZoneIndex_Type(Integer32):
    """Custom type ctxZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxZoneIndex_Type.__name__ = "Integer32"
_CtxZoneIndex_Object = MibTableColumn
ctxZoneIndex = _CtxZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 9, 1, 1),
    _CtxZoneIndex_Type()
)
ctxZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxZoneIndex.setStatus("current")
_CtxZoneDataCollector_Type = WtcsDisplayString
_CtxZoneDataCollector_Object = MibTableColumn
ctxZoneDataCollector = _CtxZoneDataCollector_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 9, 1, 2),
    _CtxZoneDataCollector_Type()
)
ctxZoneDataCollector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxZoneDataCollector.setStatus("current")
_CtxZoneNumServersInZone_Type = Gauge32
_CtxZoneNumServersInZone_Object = MibTableColumn
ctxZoneNumServersInZone = _CtxZoneNumServersInZone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 9, 1, 3),
    _CtxZoneNumServersInZone_Type()
)
ctxZoneNumServersInZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxZoneNumServersInZone.setStatus("current")
_CtxZoneZoneName_Type = WtcsDisplayString
_CtxZoneZoneName_Object = MibTableColumn
ctxZoneZoneName = _CtxZoneZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 9, 1, 4),
    _CtxZoneZoneName_Type()
)
ctxZoneZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxZoneZoneName.setStatus("current")
_MetaframeApplLoadLevelTable_Object = MibTable
metaframeApplLoadLevelTable = _MetaframeApplLoadLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 10)
)
if mibBuilder.loadTexts:
    metaframeApplLoadLevelTable.setStatus("current")
_MetaframeApplLoadLevelEntry_Object = MibTableRow
metaframeApplLoadLevelEntry = _MetaframeApplLoadLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 10, 1)
)
metaframeApplLoadLevelEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfApplicationLoadLevelIndex"),
)
if mibBuilder.loadTexts:
    metaframeApplLoadLevelEntry.setStatus("current")


class _MfApplicationLoadLevelIndex_Type(Integer32):
    """Custom type mfApplicationLoadLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfApplicationLoadLevelIndex_Type.__name__ = "Integer32"
_MfApplicationLoadLevelIndex_Object = MibTableColumn
mfApplicationLoadLevelIndex = _MfApplicationLoadLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 10, 1, 1),
    _MfApplicationLoadLevelIndex_Type()
)
mfApplicationLoadLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfApplicationLoadLevelIndex.setStatus("current")
_MfApplicationLoadLevelAppName_Type = WtcsDisplayString
_MfApplicationLoadLevelAppName_Object = MibTableColumn
mfApplicationLoadLevelAppName = _MfApplicationLoadLevelAppName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 10, 1, 2),
    _MfApplicationLoadLevelAppName_Type()
)
mfApplicationLoadLevelAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfApplicationLoadLevelAppName.setStatus("current")
_MfApplicationLoadLevelLoadLevel_Type = Gauge32
_MfApplicationLoadLevelLoadLevel_Object = MibTableColumn
mfApplicationLoadLevelLoadLevel = _MfApplicationLoadLevelLoadLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 10, 1, 3),
    _MfApplicationLoadLevelLoadLevel_Type()
)
mfApplicationLoadLevelLoadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfApplicationLoadLevelLoadLevel.setStatus("current")
_MfApplicationLoadLevelServerName_Type = WtcsDisplayString
_MfApplicationLoadLevelServerName_Object = MibTableColumn
mfApplicationLoadLevelServerName = _MfApplicationLoadLevelServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 10, 1, 4),
    _MfApplicationLoadLevelServerName_Type()
)
mfApplicationLoadLevelServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfApplicationLoadLevelServerName.setStatus("current")
_MetaframeApplPublishOnSvrTable_Object = MibTable
metaframeApplPublishOnSvrTable = _MetaframeApplPublishOnSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 11)
)
if mibBuilder.loadTexts:
    metaframeApplPublishOnSvrTable.setStatus("current")
_MetaframeApplPublishOnSvrEntry_Object = MibTableRow
metaframeApplPublishOnSvrEntry = _MetaframeApplPublishOnSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 11, 1)
)
metaframeApplPublishOnSvrEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfaposIndex"),
)
if mibBuilder.loadTexts:
    metaframeApplPublishOnSvrEntry.setStatus("current")


class _MfaposIndex_Type(Integer32):
    """Custom type mfaposIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfaposIndex_Type.__name__ = "Integer32"
_MfaposIndex_Object = MibTableColumn
mfaposIndex = _MfaposIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 11, 1, 1),
    _MfaposIndex_Type()
)
mfaposIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfaposIndex.setStatus("current")
_MfaposCtxServer_Type = WtcsDisplayString
_MfaposCtxServer_Object = MibTableColumn
mfaposCtxServer = _MfaposCtxServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 11, 1, 2),
    _MfaposCtxServer_Type()
)
mfaposCtxServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfaposCtxServer.setStatus("current")
_MfaposWinApp_Type = WtcsDisplayString
_MfaposWinApp_Object = MibTableColumn
mfaposWinApp = _MfaposWinApp_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 11, 1, 3),
    _MfaposWinApp_Type()
)
mfaposWinApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfaposWinApp.setStatus("current")
_MetaframeApplRunOnServerTable_Object = MibTable
metaframeApplRunOnServerTable = _MetaframeApplRunOnServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 12)
)
if mibBuilder.loadTexts:
    metaframeApplRunOnServerTable.setStatus("current")
_MetaframeApplRunOnServerEntry_Object = MibTableRow
metaframeApplRunOnServerEntry = _MetaframeApplRunOnServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 12, 1)
)
metaframeApplRunOnServerEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfarosIndex"),
)
if mibBuilder.loadTexts:
    metaframeApplRunOnServerEntry.setStatus("current")


class _MfarosIndex_Type(Integer32):
    """Custom type mfarosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfarosIndex_Type.__name__ = "Integer32"
_MfarosIndex_Object = MibTableColumn
mfarosIndex = _MfarosIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 12, 1, 1),
    _MfarosIndex_Type()
)
mfarosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfarosIndex.setStatus("current")
_MfarosApplication_Type = WtcsDisplayString
_MfarosApplication_Object = MibTableColumn
mfarosApplication = _MfarosApplication_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 12, 1, 2),
    _MfarosApplication_Type()
)
mfarosApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfarosApplication.setStatus("current")
_MfarosProcessId_Type = Integer32
_MfarosProcessId_Object = MibTableColumn
mfarosProcessId = _MfarosProcessId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 12, 1, 3),
    _MfarosProcessId_Type()
)
mfarosProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfarosProcessId.setStatus("current")
_MfarosServer_Type = WtcsDisplayString
_MfarosServer_Object = MibTableColumn
mfarosServer = _MfarosServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 12, 1, 4),
    _MfarosServer_Type()
)
mfarosServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfarosServer.setStatus("current")
_MetaframeAppsForGroupTable_Object = MibTable
metaframeAppsForGroupTable = _MetaframeAppsForGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 13)
)
if mibBuilder.loadTexts:
    metaframeAppsForGroupTable.setStatus("current")
_MetaframeAppsForGroupEntry_Object = MibTableRow
metaframeAppsForGroupEntry = _MetaframeAppsForGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 13, 1)
)
metaframeAppsForGroupEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfAppsForGroupIndex"),
)
if mibBuilder.loadTexts:
    metaframeAppsForGroupEntry.setStatus("current")


class _MfAppsForGroupIndex_Type(Integer32):
    """Custom type mfAppsForGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfAppsForGroupIndex_Type.__name__ = "Integer32"
_MfAppsForGroupIndex_Object = MibTableColumn
mfAppsForGroupIndex = _MfAppsForGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 13, 1, 1),
    _MfAppsForGroupIndex_Type()
)
mfAppsForGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsForGroupIndex.setStatus("current")
_MfAppsForGroupAntecedent_Type = WtcsDisplayString
_MfAppsForGroupAntecedent_Object = MibTableColumn
mfAppsForGroupAntecedent = _MfAppsForGroupAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 13, 1, 2),
    _MfAppsForGroupAntecedent_Type()
)
mfAppsForGroupAntecedent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsForGroupAntecedent.setStatus("current")
_MfAppsForGroupDependent_Type = WtcsDisplayString
_MfAppsForGroupDependent_Object = MibTableColumn
mfAppsForGroupDependent = _MfAppsForGroupDependent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 13, 1, 3),
    _MfAppsForGroupDependent_Type()
)
mfAppsForGroupDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsForGroupDependent.setStatus("current")
_MetaframeAppsInFolderTable_Object = MibTable
metaframeAppsInFolderTable = _MetaframeAppsInFolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 14)
)
if mibBuilder.loadTexts:
    metaframeAppsInFolderTable.setStatus("current")
_MetaframeAppsInFolderEntry_Object = MibTableRow
metaframeAppsInFolderEntry = _MetaframeAppsInFolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 14, 1)
)
metaframeAppsInFolderEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfAppsInFolderIndex"),
)
if mibBuilder.loadTexts:
    metaframeAppsInFolderEntry.setStatus("current")


class _MfAppsInFolderIndex_Type(Integer32):
    """Custom type mfAppsInFolderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfAppsInFolderIndex_Type.__name__ = "Integer32"
_MfAppsInFolderIndex_Object = MibTableColumn
mfAppsInFolderIndex = _MfAppsInFolderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 14, 1, 1),
    _MfAppsInFolderIndex_Type()
)
mfAppsInFolderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsInFolderIndex.setStatus("current")
_MfAppsInFolderAntecedent_Type = WtcsDisplayString
_MfAppsInFolderAntecedent_Object = MibTableColumn
mfAppsInFolderAntecedent = _MfAppsInFolderAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 14, 1, 2),
    _MfAppsInFolderAntecedent_Type()
)
mfAppsInFolderAntecedent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsInFolderAntecedent.setStatus("current")
_MfAppsInFolderDependent_Type = WtcsDisplayString
_MfAppsInFolderDependent_Object = MibTableColumn
mfAppsInFolderDependent = _MfAppsInFolderDependent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 14, 1, 3),
    _MfAppsInFolderDependent_Type()
)
mfAppsInFolderDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsInFolderDependent.setStatus("current")
_MetaframeAppsInSessionTable_Object = MibTable
metaframeAppsInSessionTable = _MetaframeAppsInSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 15)
)
if mibBuilder.loadTexts:
    metaframeAppsInSessionTable.setStatus("current")
_MetaframeAppsInSessionEntry_Object = MibTableRow
metaframeAppsInSessionEntry = _MetaframeAppsInSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 15, 1)
)
metaframeAppsInSessionEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfAppsInSessionIndex"),
)
if mibBuilder.loadTexts:
    metaframeAppsInSessionEntry.setStatus("current")


class _MfAppsInSessionIndex_Type(Integer32):
    """Custom type mfAppsInSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfAppsInSessionIndex_Type.__name__ = "Integer32"
_MfAppsInSessionIndex_Object = MibTableColumn
mfAppsInSessionIndex = _MfAppsInSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 15, 1, 1),
    _MfAppsInSessionIndex_Type()
)
mfAppsInSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsInSessionIndex.setStatus("current")
_MfAppsInSessionAntecedent_Type = WtcsDisplayString
_MfAppsInSessionAntecedent_Object = MibTableColumn
mfAppsInSessionAntecedent = _MfAppsInSessionAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 15, 1, 2),
    _MfAppsInSessionAntecedent_Type()
)
mfAppsInSessionAntecedent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsInSessionAntecedent.setStatus("current")
_MfAppsInSessionDependent_Type = WtcsDisplayString
_MfAppsInSessionDependent_Object = MibTableColumn
mfAppsInSessionDependent = _MfAppsInSessionDependent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 15, 1, 3),
    _MfAppsInSessionDependent_Type()
)
mfAppsInSessionDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfAppsInSessionDependent.setStatus("current")
_MetaframeDisconnectSessionTable_Object = MibTable
metaframeDisconnectSessionTable = _MetaframeDisconnectSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 16)
)
if mibBuilder.loadTexts:
    metaframeDisconnectSessionTable.setStatus("current")
_MetaframeDisconnectSessionEntry_Object = MibTableRow
metaframeDisconnectSessionEntry = _MetaframeDisconnectSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 16, 1)
)
metaframeDisconnectSessionEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfdshIndex"),
)
if mibBuilder.loadTexts:
    metaframeDisconnectSessionEntry.setStatus("current")


class _MfdshIndex_Type(Integer32):
    """Custom type mfdshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfdshIndex_Type.__name__ = "Integer32"
_MfdshIndex_Object = MibTableColumn
mfdshIndex = _MfdshIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 16, 1, 1),
    _MfdshIndex_Type()
)
mfdshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfdshIndex.setStatus("current")
_MfdshHowMany_Type = Integer32
_MfdshHowMany_Object = MibTableColumn
mfdshHowMany = _MfdshHowMany_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 16, 1, 2),
    _MfdshHowMany_Type()
)
mfdshHowMany.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfdshHowMany.setStatus("current")
_MfdshWhen_Type = DateAndTime
_MfdshWhen_Object = MibTableColumn
mfdshWhen = _MfdshWhen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 16, 1, 3),
    _MfdshWhen_Type()
)
mfdshWhen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfdshWhen.setStatus("current")
_MetaframeICAClientTable_Object = MibTable
metaframeICAClientTable = _MetaframeICAClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17)
)
if mibBuilder.loadTexts:
    metaframeICAClientTable.setStatus("current")
_MetaframeICAClientEntry_Object = MibTableRow
metaframeICAClientEntry = _MetaframeICAClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1)
)
metaframeICAClientEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfICAClientIndex"),
)
if mibBuilder.loadTexts:
    metaframeICAClientEntry.setStatus("current")


class _MfICAClientIndex_Type(Integer32):
    """Custom type mfICAClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfICAClientIndex_Type.__name__ = "Integer32"
_MfICAClientIndex_Object = MibTableColumn
mfICAClientIndex = _MfICAClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 1),
    _MfICAClientIndex_Type()
)
mfICAClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientIndex.setStatus("current")
_MfICAClientClientAddress_Type = WtcsDisplayString
_MfICAClientClientAddress_Object = MibTableColumn
mfICAClientClientAddress = _MfICAClientClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 2),
    _MfICAClientClientAddress_Type()
)
mfICAClientClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientAddress.setStatus("current")


class _MfICAClientClientAddrFamily_Type(Integer32):
    """Custom type mfICAClientClientAddrFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internetProtocolIP", 1),
          ("microsoftNetBIOS", 3),
          ("novellIPXSPX", 2),
          ("unspecifiedProtocol", 0))
    )


_MfICAClientClientAddrFamily_Type.__name__ = "Integer32"
_MfICAClientClientAddrFamily_Object = MibTableColumn
mfICAClientClientAddrFamily = _MfICAClientClientAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 3),
    _MfICAClientClientAddrFamily_Type()
)
mfICAClientClientAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientAddrFamily.setStatus("current")
_MfICAClientClientBuild_Type = Integer32
_MfICAClientClientBuild_Object = MibTableColumn
mfICAClientClientBuild = _MfICAClientClientBuild_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 4),
    _MfICAClientClientBuild_Type()
)
mfICAClientClientBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientBuild.setStatus("current")
_MfICAClientClientCacheDisk_Type = Integer32
_MfICAClientClientCacheDisk_Object = MibTableColumn
mfICAClientClientCacheDisk = _MfICAClientClientCacheDisk_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 5),
    _MfICAClientClientCacheDisk_Type()
)
mfICAClientClientCacheDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientCacheDisk.setStatus("current")
_MfICAClientClientCacheLowMem_Type = Integer32
_MfICAClientClientCacheLowMem_Object = MibTableColumn
mfICAClientClientCacheLowMem = _MfICAClientClientCacheLowMem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 6),
    _MfICAClientClientCacheLowMem_Type()
)
mfICAClientClientCacheLowMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientCacheLowMem.setStatus("current")
_MfICAClientClientCacheTiny_Type = Integer32
_MfICAClientClientCacheTiny_Object = MibTableColumn
mfICAClientClientCacheTiny = _MfICAClientClientCacheTiny_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 7),
    _MfICAClientClientCacheTiny_Type()
)
mfICAClientClientCacheTiny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientCacheTiny.setStatus("current")
_MfICAClientClientCacheXms_Type = Integer32
_MfICAClientClientCacheXms_Object = MibTableColumn
mfICAClientClientCacheXms = _MfICAClientClientCacheXms_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 8),
    _MfICAClientClientCacheXms_Type()
)
mfICAClientClientCacheXms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientCacheXms.setStatus("current")
_MfICAClientClientColorDepth_Type = Integer32
_MfICAClientClientColorDepth_Object = MibTableColumn
mfICAClientClientColorDepth = _MfICAClientClientColorDepth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 9),
    _MfICAClientClientColorDepth_Type()
)
mfICAClientClientColorDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientColorDepth.setStatus("current")
_MfICAClientClientDimBitmapMin_Type = Integer32
_MfICAClientClientDimBitmapMin_Object = MibTableColumn
mfICAClientClientDimBitmapMin = _MfICAClientClientDimBitmapMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 10),
    _MfICAClientClientDimBitmapMin_Type()
)
mfICAClientClientDimBitmapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientDimBitmapMin.setStatus("current")
_MfICAClientClientDimCacheSize_Type = Integer32
_MfICAClientClientDimCacheSize_Object = MibTableColumn
mfICAClientClientDimCacheSize = _MfICAClientClientDimCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 11),
    _MfICAClientClientDimCacheSize_Type()
)
mfICAClientClientDimCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientDimCacheSize.setStatus("current")
_MfICAClientClientDimVersion_Type = Integer32
_MfICAClientClientDimVersion_Object = MibTableColumn
mfICAClientClientDimVersion = _MfICAClientClientDimVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 12),
    _MfICAClientClientDimVersion_Type()
)
mfICAClientClientDimVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientDimVersion.setStatus("current")
_MfICAClientClientDirectory_Type = WtcsDisplayString
_MfICAClientClientDirectory_Object = MibTableColumn
mfICAClientClientDirectory = _MfICAClientClientDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 13),
    _MfICAClientClientDirectory_Type()
)
mfICAClientClientDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientDirectory.setStatus("current")
_MfICAClientClientEncryption_Type = WtcsDisplayString
_MfICAClientClientEncryption_Object = MibTableColumn
mfICAClientClientEncryption = _MfICAClientClientEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 14),
    _MfICAClientClientEncryption_Type()
)
mfICAClientClientEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientEncryption.setStatus("current")
_MfICAClientClientHardwareID_Type = Gauge32
_MfICAClientClientHardwareID_Object = MibTableColumn
mfICAClientClientHardwareID = _MfICAClientClientHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 15),
    _MfICAClientClientHardwareID_Type()
)
mfICAClientClientHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientHardwareID.setStatus("current")
_MfICAClientClientHRes_Type = Integer32
_MfICAClientClientHRes_Object = MibTableColumn
mfICAClientClientHRes = _MfICAClientClientHRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 16),
    _MfICAClientClientHRes_Type()
)
mfICAClientClientHRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientHRes.setStatus("current")
_MfICAClientClientLicense_Type = WtcsDisplayString
_MfICAClientClientLicense_Object = MibTableColumn
mfICAClientClientLicense = _MfICAClientClientLicense_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 17),
    _MfICAClientClientLicense_Type()
)
mfICAClientClientLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientLicense.setStatus("current")
_MfICAClientClientModemName_Type = WtcsDisplayString
_MfICAClientClientModemName_Object = MibTableColumn
mfICAClientClientModemName = _MfICAClientClientModemName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 18),
    _MfICAClientClientModemName_Type()
)
mfICAClientClientModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientModemName.setStatus("current")
_MfICAClientClientName_Type = WtcsDisplayString
_MfICAClientClientName_Object = MibTableColumn
mfICAClientClientName = _MfICAClientClientName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 19),
    _MfICAClientClientName_Type()
)
mfICAClientClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientName.setStatus("current")


class _MfICAClientClientProductID_Type(Integer32):
    """Custom type mfICAClientClientProductID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("citrixConsole", 11),
          ("citrixDirectICAStation", 9),
          ("citrixMacClient", 12),
          ("citrixTextTerminal", 10),
          ("dos32Bit", 3),
          ("dos32Bit2", 4),
          ("java", 7),
          ("oemAndOther", 13),
          ("unix", 6),
          ("unknownClient", 0),
          ("web", 8),
          ("windows16Bit", 2),
          ("windows32Bit", 1),
          ("windowsCE", 5))
    )


_MfICAClientClientProductID_Type.__name__ = "Integer32"
_MfICAClientClientProductID_Object = MibTableColumn
mfICAClientClientProductID = _MfICAClientClientProductID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 20),
    _MfICAClientClientProductID_Type()
)
mfICAClientClientProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientProductID.setStatus("current")
_MfICAClientClientProductIDValue_Type = Integer32
_MfICAClientClientProductIDValue_Object = MibTableColumn
mfICAClientClientProductIDValue = _MfICAClientClientProductIDValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 21),
    _MfICAClientClientProductIDValue_Type()
)
mfICAClientClientProductIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientProductIDValue.setStatus("current")
_MfICAClientClientVRes_Type = Integer32
_MfICAClientClientVRes_Object = MibTableColumn
mfICAClientClientVRes = _MfICAClientClientVRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 22),
    _MfICAClientClientVRes_Type()
)
mfICAClientClientVRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientClientVRes.setStatus("current")
_MfICAClientICABufLen_Type = Integer32
_MfICAClientICABufLen_Object = MibTableColumn
mfICAClientICABufLen = _MfICAClientICABufLen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 17, 1, 23),
    _MfICAClientICABufLen_Type()
)
mfICAClientICABufLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfICAClientICABufLen.setStatus("current")
_MetaframeInstalledSoftwareTable_Object = MibTable
metaframeInstalledSoftwareTable = _MetaframeInstalledSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 18)
)
if mibBuilder.loadTexts:
    metaframeInstalledSoftwareTable.setStatus("current")
_MetaframeInstalledSoftwareEntry_Object = MibTableRow
metaframeInstalledSoftwareEntry = _MetaframeInstalledSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 18, 1)
)
metaframeInstalledSoftwareEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfInstalledSoftwareIndex"),
)
if mibBuilder.loadTexts:
    metaframeInstalledSoftwareEntry.setStatus("current")


class _MfInstalledSoftwareIndex_Type(Integer32):
    """Custom type mfInstalledSoftwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfInstalledSoftwareIndex_Type.__name__ = "Integer32"
_MfInstalledSoftwareIndex_Object = MibTableColumn
mfInstalledSoftwareIndex = _MfInstalledSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 18, 1, 1),
    _MfInstalledSoftwareIndex_Type()
)
mfInstalledSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfInstalledSoftwareIndex.setStatus("current")
_MfInstalledSoftwareServer_Type = WtcsDisplayString
_MfInstalledSoftwareServer_Object = MibTableColumn
mfInstalledSoftwareServer = _MfInstalledSoftwareServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 18, 1, 2),
    _MfInstalledSoftwareServer_Type()
)
mfInstalledSoftwareServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfInstalledSoftwareServer.setStatus("current")
_MfInstalledSoftwareSoftware_Type = WtcsDisplayString
_MfInstalledSoftwareSoftware_Object = MibTableColumn
mfInstalledSoftwareSoftware = _MfInstalledSoftwareSoftware_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 18, 1, 3),
    _MfInstalledSoftwareSoftware_Type()
)
mfInstalledSoftwareSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfInstalledSoftwareSoftware.setStatus("current")
_MetaframeProcessTable_Object = MibTable
metaframeProcessTable = _MetaframeProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19)
)
if mibBuilder.loadTexts:
    metaframeProcessTable.setStatus("current")
_MetaframeProcessEntry_Object = MibTableRow
metaframeProcessEntry = _MetaframeProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1)
)
metaframeProcessEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfProcessIndex"),
)
if mibBuilder.loadTexts:
    metaframeProcessEntry.setStatus("current")


class _MfProcessIndex_Type(Integer32):
    """Custom type mfProcessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfProcessIndex_Type.__name__ = "Integer32"
_MfProcessIndex_Object = MibTableColumn
mfProcessIndex = _MfProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 1),
    _MfProcessIndex_Type()
)
mfProcessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessIndex.setStatus("current")
_MfProcessProcessID_Type = Gauge32
_MfProcessProcessID_Object = MibTableColumn
mfProcessProcessID = _MfProcessProcessID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 2),
    _MfProcessProcessID_Type()
)
mfProcessProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessProcessID.setStatus("current")
_MfProcessProcessName_Type = WtcsDisplayString
_MfProcessProcessName_Object = MibTableColumn
mfProcessProcessName = _MfProcessProcessName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 3),
    _MfProcessProcessName_Type()
)
mfProcessProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessProcessName.setStatus("current")


class _MfProcessProcessState_Type(Integer32):
    """Custom type mfProcessProcessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("eventPairHigh", 14),
          ("eventPairLow", 15),
          ("executionDelayed", 11),
          ("lpcReceive", 16),
          ("lpcReply", 17),
          ("processInTransit", 6),
          ("processInitialized", 1),
          ("processIsPagedOut", 19),
          ("processIsReadyToRun", 2),
          ("processIsRunning", 3),
          ("processIsStandingBy", 4),
          ("processSuspended", 12),
          ("processTerminated", 5),
          ("unknownState", 0),
          ("waitForOtherReasons", 20),
          ("waitForVirtualMemory", 18),
          ("waitingForMemory", 10),
          ("waitingOnExecutive", 7),
          ("waitingOnFreePage", 8),
          ("waitingOnUserRequest", 13),
          ("waitingToBePagedIn", 9))
    )


_MfProcessProcessState_Type.__name__ = "Integer32"
_MfProcessProcessState_Object = MibTableColumn
mfProcessProcessState = _MfProcessProcessState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 4),
    _MfProcessProcessState_Type()
)
mfProcessProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessProcessState.setStatus("current")
_MfProcessServerName_Type = WtcsDisplayString
_MfProcessServerName_Object = MibTableColumn
mfProcessServerName = _MfProcessServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 5),
    _MfProcessServerName_Type()
)
mfProcessServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessServerName.setStatus("current")
_MfProcessSessionID_Type = Gauge32
_MfProcessSessionID_Object = MibTableColumn
mfProcessSessionID = _MfProcessSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 6),
    _MfProcessSessionID_Type()
)
mfProcessSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessSessionID.setStatus("current")
_MfProcessUserName_Type = WtcsDisplayString
_MfProcessUserName_Object = MibTableColumn
mfProcessUserName = _MfProcessUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 19, 1, 7),
    _MfProcessUserName_Type()
)
mfProcessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessUserName.setStatus("current")
_MetaframeProcessesInSessionTable_Object = MibTable
metaframeProcessesInSessionTable = _MetaframeProcessesInSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 20)
)
if mibBuilder.loadTexts:
    metaframeProcessesInSessionTable.setStatus("current")
_MetaframeProcessesInSessionEntry_Object = MibTableRow
metaframeProcessesInSessionEntry = _MetaframeProcessesInSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 20, 1)
)
metaframeProcessesInSessionEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfProcessesInSessionIndex"),
)
if mibBuilder.loadTexts:
    metaframeProcessesInSessionEntry.setStatus("current")


class _MfProcessesInSessionIndex_Type(Integer32):
    """Custom type mfProcessesInSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfProcessesInSessionIndex_Type.__name__ = "Integer32"
_MfProcessesInSessionIndex_Object = MibTableColumn
mfProcessesInSessionIndex = _MfProcessesInSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 20, 1, 1),
    _MfProcessesInSessionIndex_Type()
)
mfProcessesInSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessesInSessionIndex.setStatus("current")
_MfProcessesInSessionAntecedent_Type = WtcsDisplayString
_MfProcessesInSessionAntecedent_Object = MibTableColumn
mfProcessesInSessionAntecedent = _MfProcessesInSessionAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 20, 1, 2),
    _MfProcessesInSessionAntecedent_Type()
)
mfProcessesInSessionAntecedent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessesInSessionAntecedent.setStatus("current")
_MfProcessesInSessionDependent_Type = WtcsDisplayString
_MfProcessesInSessionDependent_Object = MibTableColumn
mfProcessesInSessionDependent = _MfProcessesInSessionDependent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 20, 1, 3),
    _MfProcessesInSessionDependent_Type()
)
mfProcessesInSessionDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfProcessesInSessionDependent.setStatus("current")
_MetaframeSchemaVersionTable_Object = MibTable
metaframeSchemaVersionTable = _MetaframeSchemaVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 21)
)
if mibBuilder.loadTexts:
    metaframeSchemaVersionTable.setStatus("current")
_MetaframeSchemaVersionEntry_Object = MibTableRow
metaframeSchemaVersionEntry = _MetaframeSchemaVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 21, 1)
)
metaframeSchemaVersionEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfSchemaVersionIndex"),
)
if mibBuilder.loadTexts:
    metaframeSchemaVersionEntry.setStatus("current")


class _MfSchemaVersionIndex_Type(Integer32):
    """Custom type mfSchemaVersionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfSchemaVersionIndex_Type.__name__ = "Integer32"
_MfSchemaVersionIndex_Object = MibTableColumn
mfSchemaVersionIndex = _MfSchemaVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 21, 1, 1),
    _MfSchemaVersionIndex_Type()
)
mfSchemaVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSchemaVersionIndex.setStatus("current")
_MfSchemaVersionVersion_Type = WtcsDisplayString
_MfSchemaVersionVersion_Object = MibTableColumn
mfSchemaVersionVersion = _MfSchemaVersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 21, 1, 2),
    _MfSchemaVersionVersion_Type()
)
mfSchemaVersionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSchemaVersionVersion.setStatus("current")
_MetaframeServerTable_Object = MibTable
metaframeServerTable = _MetaframeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22)
)
if mibBuilder.loadTexts:
    metaframeServerTable.setStatus("current")
_MetaframeServerEntry_Object = MibTableRow
metaframeServerEntry = _MetaframeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1)
)
metaframeServerEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfServerIndex"),
)
if mibBuilder.loadTexts:
    metaframeServerEntry.setStatus("current")


class _MfServerIndex_Type(Integer32):
    """Custom type mfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfServerIndex_Type.__name__ = "Integer32"
_MfServerIndex_Object = MibTableColumn
mfServerIndex = _MfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 1),
    _MfServerIndex_Type()
)
mfServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerIndex.setStatus("current")
_MfServerDomain_Type = WtcsDisplayString
_MfServerDomain_Object = MibTableColumn
mfServerDomain = _MfServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 2),
    _MfServerDomain_Type()
)
mfServerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerDomain.setStatus("current")
_MfServerFarmName_Type = WtcsDisplayString
_MfServerFarmName_Object = MibTableColumn
mfServerFarmName = _MfServerFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 3),
    _MfServerFarmName_Type()
)
mfServerFarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerFarmName.setStatus("current")
_MfServerIPAddress_Type = WtcsDisplayString
_MfServerIPAddress_Object = MibTableColumn
mfServerIPAddress = _MfServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 4),
    _MfServerIPAddress_Type()
)
mfServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerIPAddress.setStatus("current")
_MfServerLoginsEnabled_Type = TruthValue
_MfServerLoginsEnabled_Object = MibTableColumn
mfServerLoginsEnabled = _MfServerLoginsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 5),
    _MfServerLoginsEnabled_Type()
)
mfServerLoginsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerLoginsEnabled.setStatus("current")
_MfServerNumberOfActiveSessions_Type = Integer32
_MfServerNumberOfActiveSessions_Object = MibTableColumn
mfServerNumberOfActiveSessions = _MfServerNumberOfActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 6),
    _MfServerNumberOfActiveSessions_Type()
)
mfServerNumberOfActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerNumberOfActiveSessions.setStatus("current")
_MfServerNumOfDisconnectSessions_Type = Integer32
_MfServerNumOfDisconnectSessions_Object = MibTableColumn
mfServerNumOfDisconnectSessions = _MfServerNumOfDisconnectSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 7),
    _MfServerNumOfDisconnectSessions_Type()
)
mfServerNumOfDisconnectSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerNumOfDisconnectSessions.setStatus("current")
_MfServerNumberOfSessions_Type = Integer32
_MfServerNumberOfSessions_Object = MibTableColumn
mfServerNumberOfSessions = _MfServerNumberOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 8),
    _MfServerNumberOfSessions_Type()
)
mfServerNumberOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerNumberOfSessions.setStatus("current")
_MfServerServerName_Type = WtcsDisplayString
_MfServerServerName_Object = MibTableColumn
mfServerServerName = _MfServerServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 9),
    _MfServerServerName_Type()
)
mfServerServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerServerName.setStatus("current")


class _MfServerServerType_Type(Integer32):
    """Custom type mfServerServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknownObject", 0),
          ("windowsServer", 1))
    )


_MfServerServerType_Type.__name__ = "Integer32"
_MfServerServerType_Object = MibTableColumn
mfServerServerType = _MfServerServerType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 10),
    _MfServerServerType_Type()
)
mfServerServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerServerType.setStatus("current")
_MfServerZoneName_Type = WtcsDisplayString
_MfServerZoneName_Object = MibTableColumn
mfServerZoneName = _MfServerZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 11),
    _MfServerZoneName_Type()
)
mfServerZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerZoneName.setStatus("current")


class _MfServerZoneRanking_Type(Integer32):
    """Custom type mfServerZoneRanking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backupDataCollector", 2),
          ("cannotBeDataCollector", 4),
          ("serverIsAZoneMember", 3),
          ("unknownRank", 0),
          ("zoneDataCollector", 1))
    )


_MfServerZoneRanking_Type.__name__ = "Integer32"
_MfServerZoneRanking_Object = MibTableColumn
mfServerZoneRanking = _MfServerZoneRanking_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 22, 1, 12),
    _MfServerZoneRanking_Type()
)
mfServerZoneRanking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerZoneRanking.setStatus("current")
_MetaframeServerLoadLevelTable_Object = MibTable
metaframeServerLoadLevelTable = _MetaframeServerLoadLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 23)
)
if mibBuilder.loadTexts:
    metaframeServerLoadLevelTable.setStatus("current")
_MetaframeServerLoadLevelEntry_Object = MibTableRow
metaframeServerLoadLevelEntry = _MetaframeServerLoadLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 23, 1)
)
metaframeServerLoadLevelEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfServerLoadLevelIndex"),
)
if mibBuilder.loadTexts:
    metaframeServerLoadLevelEntry.setStatus("current")


class _MfServerLoadLevelIndex_Type(Integer32):
    """Custom type mfServerLoadLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfServerLoadLevelIndex_Type.__name__ = "Integer32"
_MfServerLoadLevelIndex_Object = MibTableColumn
mfServerLoadLevelIndex = _MfServerLoadLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 23, 1, 1),
    _MfServerLoadLevelIndex_Type()
)
mfServerLoadLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerLoadLevelIndex.setStatus("current")
_MfServerLoadLevelLoadLevel_Type = Gauge32
_MfServerLoadLevelLoadLevel_Object = MibTableColumn
mfServerLoadLevelLoadLevel = _MfServerLoadLevelLoadLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 23, 1, 2),
    _MfServerLoadLevelLoadLevel_Type()
)
mfServerLoadLevelLoadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerLoadLevelLoadLevel.setStatus("current")
_MfServerLoadLevelServerName_Type = WtcsDisplayString
_MfServerLoadLevelServerName_Object = MibTableColumn
mfServerLoadLevelServerName = _MfServerLoadLevelServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 23, 1, 3),
    _MfServerLoadLevelServerName_Type()
)
mfServerLoadLevelServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfServerLoadLevelServerName.setStatus("current")
_MetaframeSessionTable_Object = MibTable
metaframeSessionTable = _MetaframeSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24)
)
if mibBuilder.loadTexts:
    metaframeSessionTable.setStatus("current")
_MetaframeSessionEntry_Object = MibTableRow
metaframeSessionEntry = _MetaframeSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1)
)
metaframeSessionEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfSessionIndex"),
)
if mibBuilder.loadTexts:
    metaframeSessionEntry.setStatus("current")


class _MfSessionIndex_Type(Integer32):
    """Custom type mfSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfSessionIndex_Type.__name__ = "Integer32"
_MfSessionIndex_Object = MibTableColumn
mfSessionIndex = _MfSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 1),
    _MfSessionIndex_Type()
)
mfSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionIndex.setStatus("current")
_MfSessionClient_Type = WtcsDisplayString
_MfSessionClient_Object = MibTableColumn
mfSessionClient = _MfSessionClient_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 2),
    _MfSessionClient_Type()
)
mfSessionClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionClient.setStatus("current")
_MfSessionConnectTime_Type = DateAndTime
_MfSessionConnectTime_Object = MibTableColumn
mfSessionConnectTime = _MfSessionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 3),
    _MfSessionConnectTime_Type()
)
mfSessionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionConnectTime.setStatus("current")
_MfSessionCurrentTime_Type = DateAndTime
_MfSessionCurrentTime_Object = MibTableColumn
mfSessionCurrentTime = _MfSessionCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 4),
    _MfSessionCurrentTime_Type()
)
mfSessionCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionCurrentTime.setStatus("current")
_MfSessionDisconnectTime_Type = DateAndTime
_MfSessionDisconnectTime_Object = MibTableColumn
mfSessionDisconnectTime = _MfSessionDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 5),
    _MfSessionDisconnectTime_Type()
)
mfSessionDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionDisconnectTime.setStatus("current")
_MfSessionLastInputTime_Type = DateAndTime
_MfSessionLastInputTime_Object = MibTableColumn
mfSessionLastInputTime = _MfSessionLastInputTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 6),
    _MfSessionLastInputTime_Type()
)
mfSessionLastInputTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionLastInputTime.setStatus("current")
_MfSessionLogonTime_Type = DateAndTime
_MfSessionLogonTime_Object = MibTableColumn
mfSessionLogonTime = _MfSessionLogonTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 7),
    _MfSessionLogonTime_Type()
)
mfSessionLogonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionLogonTime.setStatus("current")
_MfSessionNumberOfApps_Type = Integer32
_MfSessionNumberOfApps_Object = MibTableColumn
mfSessionNumberOfApps = _MfSessionNumberOfApps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 8),
    _MfSessionNumberOfApps_Type()
)
mfSessionNumberOfApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionNumberOfApps.setStatus("current")
_MfSessionServerName_Type = WtcsDisplayString
_MfSessionServerName_Object = MibTableColumn
mfSessionServerName = _MfSessionServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 9),
    _MfSessionServerName_Type()
)
mfSessionServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionServerName.setStatus("current")
_MfSessionSessionID_Type = Integer32
_MfSessionSessionID_Object = MibTableColumn
mfSessionSessionID = _MfSessionSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 10),
    _MfSessionSessionID_Type()
)
mfSessionSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionSessionID.setStatus("current")
_MfSessionSessionName_Type = WtcsDisplayString
_MfSessionSessionName_Object = MibTableColumn
mfSessionSessionName = _MfSessionSessionName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 11),
    _MfSessionSessionName_Type()
)
mfSessionSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionSessionName.setStatus("current")


class _MfSessionSessionState_Type(Integer32):
    """Custom type mfSessionSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("connectedToClient", 1),
          ("connectingToClient", 2),
          ("downDueToError", 8),
          ("initializing", 9),
          ("listeningForConnection", 6),
          ("loggedOnButNoClient", 4),
          ("resetInProgress", 7),
          ("shadowingOtherSession", 3),
          ("userLoggedOn", 0),
          ("waitingForConnection", 5))
    )


_MfSessionSessionState_Type.__name__ = "Integer32"
_MfSessionSessionState_Object = MibTableColumn
mfSessionSessionState = _MfSessionSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 12),
    _MfSessionSessionState_Type()
)
mfSessionSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionSessionState.setStatus("current")
_MfSessionSessionUser_Type = WtcsDisplayString
_MfSessionSessionUser_Object = MibTableColumn
mfSessionSessionUser = _MfSessionSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 24, 1, 13),
    _MfSessionSessionUser_Type()
)
mfSessionSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSessionSessionUser.setStatus("current")
_MetaframeSoftwareTable_Object = MibTable
metaframeSoftwareTable = _MetaframeSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25)
)
if mibBuilder.loadTexts:
    metaframeSoftwareTable.setStatus("current")
_MetaframeSoftwareEntry_Object = MibTableRow
metaframeSoftwareEntry = _MetaframeSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1)
)
metaframeSoftwareEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfSoftwareIndex"),
)
if mibBuilder.loadTexts:
    metaframeSoftwareEntry.setStatus("current")


class _MfSoftwareIndex_Type(Integer32):
    """Custom type mfSoftwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfSoftwareIndex_Type.__name__ = "Integer32"
_MfSoftwareIndex_Object = MibTableColumn
mfSoftwareIndex = _MfSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 1),
    _MfSoftwareIndex_Type()
)
mfSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareIndex.setStatus("current")
_MfSoftwareFeatureReleaseLevel_Type = Gauge32
_MfSoftwareFeatureReleaseLevel_Object = MibTableColumn
mfSoftwareFeatureReleaseLevel = _MfSoftwareFeatureReleaseLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 2),
    _MfSoftwareFeatureReleaseLevel_Type()
)
mfSoftwareFeatureReleaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareFeatureReleaseLevel.setStatus("current")
_MfSoftwareInstallDate_Type = DateAndTime
_MfSoftwareInstallDate_Object = MibTableColumn
mfSoftwareInstallDate = _MfSoftwareInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 3),
    _MfSoftwareInstallDate_Type()
)
mfSoftwareInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareInstallDate.setStatus("current")
_MfSoftwareMFWinProductCode_Type = WtcsDisplayString
_MfSoftwareMFWinProductCode_Object = MibTableColumn
mfSoftwareMFWinProductCode = _MfSoftwareMFWinProductCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 4),
    _MfSoftwareMFWinProductCode_Type()
)
mfSoftwareMFWinProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareMFWinProductCode.setStatus("current")
_MfSoftwareProductName_Type = WtcsDisplayString
_MfSoftwareProductName_Object = MibTableColumn
mfSoftwareProductName = _MfSoftwareProductName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 5),
    _MfSoftwareProductName_Type()
)
mfSoftwareProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareProductName.setStatus("current")
_MfSoftwareReleaseLevel_Type = WtcsDisplayString
_MfSoftwareReleaseLevel_Object = MibTableColumn
mfSoftwareReleaseLevel = _MfSoftwareReleaseLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 6),
    _MfSoftwareReleaseLevel_Type()
)
mfSoftwareReleaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareReleaseLevel.setStatus("current")
_MfSoftwareVersion_Type = WtcsDisplayString
_MfSoftwareVersion_Object = MibTableColumn
mfSoftwareVersion = _MfSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 25, 1, 7),
    _MfSoftwareVersion_Type()
)
mfSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfSoftwareVersion.setStatus("current")
_MetaframeWinApplicationTable_Object = MibTable
metaframeWinApplicationTable = _MetaframeWinApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26)
)
if mibBuilder.loadTexts:
    metaframeWinApplicationTable.setStatus("current")
_MetaframeWinApplicationEntry_Object = MibTableRow
metaframeWinApplicationEntry = _MetaframeWinApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1)
)
metaframeWinApplicationEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfWinApplIndex"),
)
if mibBuilder.loadTexts:
    metaframeWinApplicationEntry.setStatus("current")


class _MfWinApplIndex_Type(Integer32):
    """Custom type mfWinApplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfWinApplIndex_Type.__name__ = "Integer32"
_MfWinApplIndex_Object = MibTableColumn
mfWinApplIndex = _MfWinApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 1),
    _MfWinApplIndex_Type()
)
mfWinApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplIndex.setStatus("current")
_MfWinApplApplicationID_Type = WtcsDisplayString
_MfWinApplApplicationID_Object = MibTableColumn
mfWinApplApplicationID = _MfWinApplApplicationID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 2),
    _MfWinApplApplicationID_Type()
)
mfWinApplApplicationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplApplicationID.setStatus("current")
_MfWinApplAppVersion_Type = Integer32
_MfWinApplAppVersion_Object = MibTableColumn
mfWinApplAppVersion = _MfWinApplAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 3),
    _MfWinApplAppVersion_Type()
)
mfWinApplAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplAppVersion.setStatus("current")
_MfWinApplBrowserName_Type = WtcsDisplayString
_MfWinApplBrowserName_Object = MibTableColumn
mfWinApplBrowserName = _MfWinApplBrowserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 4),
    _MfWinApplBrowserName_Type()
)
mfWinApplBrowserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplBrowserName.setStatus("current")


class _MfWinApplDefaultEncryption_Type(Integer32):
    """Custom type mfWinApplDefaultEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("basicEncryptionRC5Logon", 1),
          ("rc5128Bit", 4),
          ("rc540Bit", 2),
          ("rc556Bit", 3),
          ("unknownEncryption", 0))
    )


_MfWinApplDefaultEncryption_Type.__name__ = "Integer32"
_MfWinApplDefaultEncryption_Object = MibTableColumn
mfWinApplDefaultEncryption = _MfWinApplDefaultEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 5),
    _MfWinApplDefaultEncryption_Type()
)
mfWinApplDefaultEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultEncryption.setStatus("current")
_MfWinApplDefaultInitProg_Type = WtcsDisplayString
_MfWinApplDefaultInitProg_Object = MibTableColumn
mfWinApplDefaultInitProg = _MfWinApplDefaultInitProg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 6),
    _MfWinApplDefaultInitProg_Type()
)
mfWinApplDefaultInitProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultInitProg.setStatus("current")


class _MfWinApplDefaultSoundType_Type(Integer32):
    """Custom type mfWinApplDefaultSoundType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicSound", 2),
          ("noSound", 1),
          ("unknownSoundType", 0))
    )


_MfWinApplDefaultSoundType_Type.__name__ = "Integer32"
_MfWinApplDefaultSoundType_Object = MibTableColumn
mfWinApplDefaultSoundType = _MfWinApplDefaultSoundType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 7),
    _MfWinApplDefaultSoundType_Type()
)
mfWinApplDefaultSoundType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultSoundType.setStatus("current")


class _MfWinApplDefaultWindowColor_Type(Integer32):
    """Custom type mfWinApplDefaultWindowColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("a16Colors", 1),
          ("a16MillionColors", 4),
          ("a256Colors", 2),
          ("a65536Colors", 3),
          ("unknownWindowColor", 0))
    )


_MfWinApplDefaultWindowColor_Type.__name__ = "Integer32"
_MfWinApplDefaultWindowColor_Object = MibTableColumn
mfWinApplDefaultWindowColor = _MfWinApplDefaultWindowColor_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 8),
    _MfWinApplDefaultWindowColor_Type()
)
mfWinApplDefaultWindowColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultWindowColor.setStatus("current")
_MfWinApplDefaultWindowHeight_Type = Integer32
_MfWinApplDefaultWindowHeight_Object = MibTableColumn
mfWinApplDefaultWindowHeight = _MfWinApplDefaultWindowHeight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 9),
    _MfWinApplDefaultWindowHeight_Type()
)
mfWinApplDefaultWindowHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultWindowHeight.setStatus("current")
_MfWinApplDefaultWindowScale_Type = Integer32
_MfWinApplDefaultWindowScale_Object = MibTableColumn
mfWinApplDefaultWindowScale = _MfWinApplDefaultWindowScale_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 10),
    _MfWinApplDefaultWindowScale_Type()
)
mfWinApplDefaultWindowScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultWindowScale.setStatus("current")


class _MfWinApplDefaultWindowType_Type(Integer32):
    """Custom type mfWinApplDefaultWindowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("a1024x768", 3),
          ("a1280x1024", 4),
          ("a1600x1200", 5),
          ("a640x480", 1),
          ("a800x600", 2),
          ("custom", 6),
          ("fullscreen", 8),
          ("percent", 7),
          ("unknownWindowType", 0))
    )


_MfWinApplDefaultWindowType_Type.__name__ = "Integer32"
_MfWinApplDefaultWindowType_Object = MibTableColumn
mfWinApplDefaultWindowType = _MfWinApplDefaultWindowType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 11),
    _MfWinApplDefaultWindowType_Type()
)
mfWinApplDefaultWindowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultWindowType.setStatus("current")
_MfWinApplDefaultWindowWidth_Type = Integer32
_MfWinApplDefaultWindowWidth_Object = MibTableColumn
mfWinApplDefaultWindowWidth = _MfWinApplDefaultWindowWidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 12),
    _MfWinApplDefaultWindowWidth_Type()
)
mfWinApplDefaultWindowWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultWindowWidth.setStatus("current")
_MfWinApplDefaultWorkDir_Type = WtcsDisplayString
_MfWinApplDefaultWorkDir_Object = MibTableColumn
mfWinApplDefaultWorkDir = _MfWinApplDefaultWorkDir_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 13),
    _MfWinApplDefaultWorkDir_Type()
)
mfWinApplDefaultWorkDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDefaultWorkDir.setStatus("current")
_MfWinApplDescription_Type = WtcsDisplayString
_MfWinApplDescription_Object = MibTableColumn
mfWinApplDescription = _MfWinApplDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 14),
    _MfWinApplDescription_Type()
)
mfWinApplDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDescription.setStatus("current")


class _MfWinApplDesktopIntegrate_Type(Integer32):
    """Custom type mfWinApplDesktopIntegrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("desktop", 2),
          ("noDesktopIntegrate", 0),
          ("startMenu", 1))
    )


_MfWinApplDesktopIntegrate_Type.__name__ = "Integer32"
_MfWinApplDesktopIntegrate_Object = MibTableColumn
mfWinApplDesktopIntegrate = _MfWinApplDesktopIntegrate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 15),
    _MfWinApplDesktopIntegrate_Type()
)
mfWinApplDesktopIntegrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDesktopIntegrate.setStatus("current")
_MfWinApplDistinguishedName_Type = WtcsDisplayString
_MfWinApplDistinguishedName_Object = MibTableColumn
mfWinApplDistinguishedName = _MfWinApplDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 16),
    _MfWinApplDistinguishedName_Type()
)
mfWinApplDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplDistinguishedName.setStatus("current")
_MfWinApplEnableApp_Type = TruthValue
_MfWinApplEnableApp_Object = MibTableColumn
mfWinApplEnableApp = _MfWinApplEnableApp_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 17),
    _MfWinApplEnableApp_Type()
)
mfWinApplEnableApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplEnableApp.setStatus("current")
_MfWinApplFarmName_Type = WtcsDisplayString
_MfWinApplFarmName_Object = MibTableColumn
mfWinApplFarmName = _MfWinApplFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 18),
    _MfWinApplFarmName_Type()
)
mfWinApplFarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplFarmName.setStatus("current")


class _MfWinApplMFAttributes_Type(Integer32):
    """Custom type mfWinApplMFAttributes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hideTitleBar", 2),
          ("maximizeOnStartup", 1),
          ("noMetaFrameAttribute", 0))
    )


_MfWinApplMFAttributes_Type.__name__ = "Integer32"
_MfWinApplMFAttributes_Object = MibTableColumn
mfWinApplMFAttributes = _MfWinApplMFAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 19),
    _MfWinApplMFAttributes_Type()
)
mfWinApplMFAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplMFAttributes.setStatus("current")
_MfWinApplName_Type = WtcsDisplayString
_MfWinApplName_Object = MibTableColumn
mfWinApplName = _MfWinApplName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 20),
    _MfWinApplName_Type()
)
mfWinApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplName.setStatus("current")
_MfWinApplParentFolderDN_Type = WtcsDisplayString
_MfWinApplParentFolderDN_Object = MibTableColumn
mfWinApplParentFolderDN = _MfWinApplParentFolderDN_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 21),
    _MfWinApplParentFolderDN_Type()
)
mfWinApplParentFolderDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplParentFolderDN.setStatus("current")
_MfWinApplPNAttributes_Type = Integer32
_MfWinApplPNAttributes_Object = MibTableColumn
mfWinApplPNAttributes = _MfWinApplPNAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 22),
    _MfWinApplPNAttributes_Type()
)
mfWinApplPNAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplPNAttributes.setStatus("current")
_MfWinApplPNFolder_Type = WtcsDisplayString
_MfWinApplPNFolder_Object = MibTableColumn
mfWinApplPNFolder = _MfWinApplPNFolder_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 23),
    _MfWinApplPNFolder_Type()
)
mfWinApplPNFolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplPNFolder.setStatus("current")


class _MfWinApplPublishingFlags_Type(Integer32):
    """Custom type mfWinApplPublishingFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("browserEnumeration", 1),
          ("noEnumerationMask", 0),
          ("pnEnumeration", 2))
    )


_MfWinApplPublishingFlags_Type.__name__ = "Integer32"
_MfWinApplPublishingFlags_Object = MibTableColumn
mfWinApplPublishingFlags = _MfWinApplPublishingFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 24),
    _MfWinApplPublishingFlags_Type()
)
mfWinApplPublishingFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplPublishingFlags.setStatus("current")
_MfWinApplReadOnly_Type = TruthValue
_MfWinApplReadOnly_Object = MibTableColumn
mfWinApplReadOnly = _MfWinApplReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 26, 1, 25),
    _MfWinApplReadOnly_Type()
)
mfWinApplReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinApplReadOnly.setStatus("current")
_MetaframeWinFarmTable_Object = MibTable
metaframeWinFarmTable = _MetaframeWinFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27)
)
if mibBuilder.loadTexts:
    metaframeWinFarmTable.setStatus("current")
_MetaframeWinFarmEntry_Object = MibTableRow
metaframeWinFarmEntry = _MetaframeWinFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1)
)
metaframeWinFarmEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "mfWinFarmIndex"),
)
if mibBuilder.loadTexts:
    metaframeWinFarmEntry.setStatus("current")


class _MfWinFarmIndex_Type(Integer32):
    """Custom type mfWinFarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfWinFarmIndex_Type.__name__ = "Integer32"
_MfWinFarmIndex_Object = MibTableColumn
mfWinFarmIndex = _MfWinFarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 1),
    _MfWinFarmIndex_Type()
)
mfWinFarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmIndex.setStatus("current")
_MfWinFarmAlternateCachingMethod_Type = TruthValue
_MfWinFarmAlternateCachingMethod_Object = MibTableColumn
mfWinFarmAlternateCachingMethod = _MfWinFarmAlternateCachingMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 2),
    _MfWinFarmAlternateCachingMethod_Type()
)
mfWinFarmAlternateCachingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmAlternateCachingMethod.setStatus("current")
_MfWinFarmDCRespondToClientBdcst_Type = TruthValue
_MfWinFarmDCRespondToClientBdcst_Object = MibTableColumn
mfWinFarmDCRespondToClientBdcst = _MfWinFarmDCRespondToClientBdcst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 3),
    _MfWinFarmDCRespondToClientBdcst_Type()
)
mfWinFarmDCRespondToClientBdcst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmDCRespondToClientBdcst.setStatus("current")


class _MfWinFarmDegradationBias_Type(Integer32):
    """Custom type mfWinFarmDegradationBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degradeColorDepthFirst", 2),
          ("degradeResolutionFirst", 1))
    )


_MfWinFarmDegradationBias_Type.__name__ = "Integer32"
_MfWinFarmDegradationBias_Object = MibTableColumn
mfWinFarmDegradationBias = _MfWinFarmDegradationBias_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 4),
    _MfWinFarmDegradationBias_Type()
)
mfWinFarmDegradationBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmDegradationBias.setStatus("current")
_MfWinFarmDisableClientLocalTmEst_Type = TruthValue
_MfWinFarmDisableClientLocalTmEst_Object = MibTableColumn
mfWinFarmDisableClientLocalTmEst = _MfWinFarmDisableClientLocalTmEst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 5),
    _MfWinFarmDisableClientLocalTmEst_Type()
)
mfWinFarmDisableClientLocalTmEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmDisableClientLocalTmEst.setStatus("current")
_MfWinFarmDiscardRedundantGraphic_Type = TruthValue
_MfWinFarmDiscardRedundantGraphic_Object = MibTableColumn
mfWinFarmDiscardRedundantGraphic = _MfWinFarmDiscardRedundantGraphic_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 6),
    _MfWinFarmDiscardRedundantGraphic_Type()
)
mfWinFarmDiscardRedundantGraphic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmDiscardRedundantGraphic.setStatus("current")
_MfWinFarmEnableAutoClientReconn_Type = TruthValue
_MfWinFarmEnableAutoClientReconn_Object = MibTableColumn
mfWinFarmEnableAutoClientReconn = _MfWinFarmEnableAutoClientReconn_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 7),
    _MfWinFarmEnableAutoClientReconn_Type()
)
mfWinFarmEnableAutoClientReconn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmEnableAutoClientReconn.setStatus("current")
_MfWinFarmEnableDNSAddrResolution_Type = TruthValue
_MfWinFarmEnableDNSAddrResolution_Object = MibTableColumn
mfWinFarmEnableDNSAddrResolution = _MfWinFarmEnableDNSAddrResolution_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 8),
    _MfWinFarmEnableDNSAddrResolution_Type()
)
mfWinFarmEnableDNSAddrResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmEnableDNSAddrResolution.setStatus("current")
_MfWinFarmEnableSNMPAgent_Type = TruthValue
_MfWinFarmEnableSNMPAgent_Object = MibTableColumn
mfWinFarmEnableSNMPAgent = _MfWinFarmEnableSNMPAgent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 9),
    _MfWinFarmEnableSNMPAgent_Type()
)
mfWinFarmEnableSNMPAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmEnableSNMPAgent.setStatus("current")
_MfWinFarmFarmName_Type = WtcsDisplayString
_MfWinFarmFarmName_Object = MibTableColumn
mfWinFarmFarmName = _MfWinFarmFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 10),
    _MfWinFarmFarmName_Type()
)
mfWinFarmFarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmFarmName.setStatus("current")
_MfWinFarmICAVideoBufferSize_Type = Integer32
_MfWinFarmICAVideoBufferSize_Object = MibTableColumn
mfWinFarmICAVideoBufferSize = _MfWinFarmICAVideoBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 11),
    _MfWinFarmICAVideoBufferSize_Type()
)
mfWinFarmICAVideoBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmICAVideoBufferSize.setStatus("current")
_MfWinFarmLegacyDisplayCompatMode_Type = TruthValue
_MfWinFarmLegacyDisplayCompatMode_Object = MibTableColumn
mfWinFarmLegacyDisplayCompatMode = _MfWinFarmLegacyDisplayCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 12),
    _MfWinFarmLegacyDisplayCompatMode_Type()
)
mfWinFarmLegacyDisplayCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmLegacyDisplayCompatMode.setStatus("current")
_MfWinFarmLegacyServerCompatMode_Type = TruthValue
_MfWinFarmLegacyServerCompatMode_Object = MibTableColumn
mfWinFarmLegacyServerCompatMode = _MfWinFarmLegacyServerCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 13),
    _MfWinFarmLegacyServerCompatMode_Type()
)
mfWinFarmLegacyServerCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmLegacyServerCompatMode.setStatus("current")
_MfWinFarmLogAutoReconnectAttempt_Type = TruthValue
_MfWinFarmLogAutoReconnectAttempt_Object = MibTableColumn
mfWinFarmLogAutoReconnectAttempt = _MfWinFarmLogAutoReconnectAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 14),
    _MfWinFarmLogAutoReconnectAttempt_Type()
)
mfWinFarmLogAutoReconnectAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmLogAutoReconnectAttempt.setStatus("current")
_MfWinFarmLogOverLimitDenials_Type = TruthValue
_MfWinFarmLogOverLimitDenials_Object = MibTableColumn
mfWinFarmLogOverLimitDenials = _MfWinFarmLogOverLimitDenials_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 15),
    _MfWinFarmLogOverLimitDenials_Type()
)
mfWinFarmLogOverLimitDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmLogOverLimitDenials.setStatus("current")
_MfWinFarmMaxConnectionsPerUser_Type = Integer32
_MfWinFarmMaxConnectionsPerUser_Object = MibTableColumn
mfWinFarmMaxConnectionsPerUser = _MfWinFarmMaxConnectionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 16),
    _MfWinFarmMaxConnectionsPerUser_Type()
)
mfWinFarmMaxConnectionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmMaxConnectionsPerUser.setStatus("current")
_MfWinFarmNotifyDegradation_Type = TruthValue
_MfWinFarmNotifyDegradation_Object = MibTableColumn
mfWinFarmNotifyDegradation = _MfWinFarmNotifyDegradation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 17),
    _MfWinFarmNotifyDegradation_Type()
)
mfWinFarmNotifyDegradation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmNotifyDegradation.setStatus("current")
_MfWinFarmRASRespondToClientBdcst_Type = TruthValue
_MfWinFarmRASRespondToClientBdcst_Object = MibTableColumn
mfWinFarmRASRespondToClientBdcst = _MfWinFarmRASRespondToClientBdcst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 18),
    _MfWinFarmRASRespondToClientBdcst_Type()
)
mfWinFarmRASRespondToClientBdcst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmRASRespondToClientBdcst.setStatus("current")
_MfWinFarmSNMPDisconnectTrap_Type = TruthValue
_MfWinFarmSNMPDisconnectTrap_Object = MibTableColumn
mfWinFarmSNMPDisconnectTrap = _MfWinFarmSNMPDisconnectTrap_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 19),
    _MfWinFarmSNMPDisconnectTrap_Type()
)
mfWinFarmSNMPDisconnectTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmSNMPDisconnectTrap.setStatus("current")
_MfWinFarmSNMPLogoffTrap_Type = TruthValue
_MfWinFarmSNMPLogoffTrap_Object = MibTableColumn
mfWinFarmSNMPLogoffTrap = _MfWinFarmSNMPLogoffTrap_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 20),
    _MfWinFarmSNMPLogoffTrap_Type()
)
mfWinFarmSNMPLogoffTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmSNMPLogoffTrap.setStatus("current")
_MfWinFarmSNMPLogonTrap_Type = TruthValue
_MfWinFarmSNMPLogonTrap_Object = MibTableColumn
mfWinFarmSNMPLogonTrap = _MfWinFarmSNMPLogonTrap_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 21),
    _MfWinFarmSNMPLogonTrap_Type()
)
mfWinFarmSNMPLogonTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmSNMPLogonTrap.setStatus("current")
_MfWinFarmSNMPThresholdExceedTrap_Type = TruthValue
_MfWinFarmSNMPThresholdExceedTrap_Object = MibTableColumn
mfWinFarmSNMPThresholdExceedTrap = _MfWinFarmSNMPThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 22),
    _MfWinFarmSNMPThresholdExceedTrap_Type()
)
mfWinFarmSNMPThresholdExceedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmSNMPThresholdExceedTrap.setStatus("current")
_MfWinFarmSNMPThresholdValue_Type = Integer32
_MfWinFarmSNMPThresholdValue_Object = MibTableColumn
mfWinFarmSNMPThresholdValue = _MfWinFarmSNMPThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 23),
    _MfWinFarmSNMPThresholdValue_Type()
)
mfWinFarmSNMPThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmSNMPThresholdValue.setStatus("current")
_MfWinFarmUseClientLocalTime_Type = TruthValue
_MfWinFarmUseClientLocalTime_Object = MibTableColumn
mfWinFarmUseClientLocalTime = _MfWinFarmUseClientLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 1, 27, 1, 24),
    _MfWinFarmUseClientLocalTime_Type()
)
mfWinFarmUseClientLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfWinFarmUseClientLocalTime.setStatus("current")
_CiitrixWmiCitrixLicensing_ObjectIdentity = ObjectIdentity
ciitrixWmiCitrixLicensing = _CiitrixWmiCitrixLicensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2)
)
if mibBuilder.loadTexts:
    ciitrixWmiCitrixLicensing.setStatus("current")
_CitrixGTLicenseTable_Object = MibTable
citrixGTLicenseTable = _CitrixGTLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1)
)
if mibBuilder.loadTexts:
    citrixGTLicenseTable.setStatus("current")
_CitrixGTLicenseEntry_Object = MibTableRow
citrixGTLicenseEntry = _CitrixGTLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1)
)
citrixGTLicenseEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxGTLicenseIndex"),
)
if mibBuilder.loadTexts:
    citrixGTLicenseEntry.setStatus("current")


class _CtxGTLicenseIndex_Type(Integer32):
    """Custom type ctxGTLicenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxGTLicenseIndex_Type.__name__ = "Integer32"
_CtxGTLicenseIndex_Object = MibTableColumn
ctxGTLicenseIndex = _CtxGTLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 1),
    _CtxGTLicenseIndex_Type()
)
ctxGTLicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseIndex.setStatus("current")
_CtxGTLicenseCount_Type = Gauge32
_CtxGTLicenseCount_Object = MibTableColumn
ctxGTLicenseCount = _CtxGTLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 2),
    _CtxGTLicenseCount_Type()
)
ctxGTLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseCount.setStatus("current")
_CtxGTLicenseExpirationDate_Type = DateAndTime
_CtxGTLicenseExpirationDate_Object = MibTableColumn
ctxGTLicenseExpirationDate = _CtxGTLicenseExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 3),
    _CtxGTLicenseExpirationDate_Type()
)
ctxGTLicenseExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseExpirationDate.setStatus("current")
_CtxGTLicenseLicenseType_Type = WtcsDisplayString
_CtxGTLicenseLicenseType_Object = MibTableColumn
ctxGTLicenseLicenseType = _CtxGTLicenseLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 4),
    _CtxGTLicenseLicenseType_Type()
)
ctxGTLicenseLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseLicenseType.setStatus("current")
_CtxGTLicenseOverdraft_Type = Gauge32
_CtxGTLicenseOverdraft_Object = MibTableColumn
ctxGTLicenseOverdraft = _CtxGTLicenseOverdraft_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 5),
    _CtxGTLicenseOverdraft_Type()
)
ctxGTLicenseOverdraft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseOverdraft.setStatus("current")
_CtxGTLicensePLD_Type = WtcsDisplayString
_CtxGTLicensePLD_Object = MibTableColumn
ctxGTLicensePLD = _CtxGTLicensePLD_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 6),
    _CtxGTLicensePLD_Type()
)
ctxGTLicensePLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePLD.setStatus("current")
_CtxGTLicensePLDFullName_Type = WtcsDisplayString
_CtxGTLicensePLDFullName_Object = MibTableColumn
ctxGTLicensePLDFullName = _CtxGTLicensePLDFullName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 7),
    _CtxGTLicensePLDFullName_Type()
)
ctxGTLicensePLDFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePLDFullName.setStatus("current")
_CtxGTLicenseSerialNumber_Type = WtcsDisplayString
_CtxGTLicenseSerialNumber_Object = MibTableColumn
ctxGTLicenseSerialNumber = _CtxGTLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 8),
    _CtxGTLicenseSerialNumber_Type()
)
ctxGTLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseSerialNumber.setStatus("current")
_CtxGTLicenseSubscriptionDate_Type = DateAndTime
_CtxGTLicenseSubscriptionDate_Object = MibTableColumn
ctxGTLicenseSubscriptionDate = _CtxGTLicenseSubscriptionDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 1, 1, 9),
    _CtxGTLicenseSubscriptionDate_Type()
)
ctxGTLicenseSubscriptionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicenseSubscriptionDate.setStatus("current")
_CitrixGTLicensePoolTable_Object = MibTable
citrixGTLicensePoolTable = _CitrixGTLicensePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2)
)
if mibBuilder.loadTexts:
    citrixGTLicensePoolTable.setStatus("current")
_CitrixGTLicensePoolEntry_Object = MibTableRow
citrixGTLicensePoolEntry = _CitrixGTLicensePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1)
)
citrixGTLicensePoolEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxGTLicensePoolIndex"),
)
if mibBuilder.loadTexts:
    citrixGTLicensePoolEntry.setStatus("current")


class _CtxGTLicensePoolIndex_Type(Integer32):
    """Custom type ctxGTLicensePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxGTLicensePoolIndex_Type.__name__ = "Integer32"
_CtxGTLicensePoolIndex_Object = MibTableColumn
ctxGTLicensePoolIndex = _CtxGTLicensePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 1),
    _CtxGTLicensePoolIndex_Type()
)
ctxGTLicensePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolIndex.setStatus("current")
_CtxGTLicensePoolCount_Type = Gauge32
_CtxGTLicensePoolCount_Object = MibTableColumn
ctxGTLicensePoolCount = _CtxGTLicensePoolCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 2),
    _CtxGTLicensePoolCount_Type()
)
ctxGTLicensePoolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolCount.setStatus("current")
_CtxGTLicensePoolDUPGROUP_Type = Gauge32
_CtxGTLicensePoolDUPGROUP_Object = MibTableColumn
ctxGTLicensePoolDUPGROUP = _CtxGTLicensePoolDUPGROUP_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 3),
    _CtxGTLicensePoolDUPGROUP_Type()
)
ctxGTLicensePoolDUPGROUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolDUPGROUP.setStatus("current")
_CtxGTLicensePoolFLOATOK_Type = TruthValue
_CtxGTLicensePoolFLOATOK_Object = MibTableColumn
ctxGTLicensePoolFLOATOK = _CtxGTLicensePoolFLOATOK_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 4),
    _CtxGTLicensePoolFLOATOK_Type()
)
ctxGTLicensePoolFLOATOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolFLOATOK.setStatus("current")
_CtxGTLicensePoolHOSTBASED_Type = Gauge32
_CtxGTLicensePoolHOSTBASED_Object = MibTableColumn
ctxGTLicensePoolHOSTBASED = _CtxGTLicensePoolHOSTBASED_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 5),
    _CtxGTLicensePoolHOSTBASED_Type()
)
ctxGTLicensePoolHOSTBASED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolHOSTBASED.setStatus("current")
_CtxGTLicensePoolHOSTID_Type = WtcsDisplayString
_CtxGTLicensePoolHOSTID_Object = MibTableColumn
ctxGTLicensePoolHOSTID = _CtxGTLicensePoolHOSTID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 6),
    _CtxGTLicensePoolHOSTID_Type()
)
ctxGTLicensePoolHOSTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolHOSTID.setStatus("current")
_CtxGTLicensePoolInUseCount_Type = Gauge32
_CtxGTLicensePoolInUseCount_Object = MibTableColumn
ctxGTLicensePoolInUseCount = _CtxGTLicensePoolInUseCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 7),
    _CtxGTLicensePoolInUseCount_Type()
)
ctxGTLicensePoolInUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolInUseCount.setStatus("current")
_CtxGTLicensePoolLicenseType_Type = WtcsDisplayString
_CtxGTLicensePoolLicenseType_Object = MibTableColumn
ctxGTLicensePoolLicenseType = _CtxGTLicensePoolLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 8),
    _CtxGTLicensePoolLicenseType_Type()
)
ctxGTLicensePoolLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolLicenseType.setStatus("current")
_CtxGTLicensePoolOverdraft_Type = Gauge32
_CtxGTLicensePoolOverdraft_Object = MibTableColumn
ctxGTLicensePoolOverdraft = _CtxGTLicensePoolOverdraft_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 9),
    _CtxGTLicensePoolOverdraft_Type()
)
ctxGTLicensePoolOverdraft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolOverdraft.setStatus("current")
_CtxGTLicensePoolPLATFORMS_Type = WtcsDisplayString
_CtxGTLicensePoolPLATFORMS_Object = MibTableColumn
ctxGTLicensePoolPLATFORMS = _CtxGTLicensePoolPLATFORMS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 10),
    _CtxGTLicensePoolPLATFORMS_Type()
)
ctxGTLicensePoolPLATFORMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolPLATFORMS.setStatus("current")
_CtxGTLicensePoolPLD_Type = WtcsDisplayString
_CtxGTLicensePoolPLD_Object = MibTableColumn
ctxGTLicensePoolPLD = _CtxGTLicensePoolPLD_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 11),
    _CtxGTLicensePoolPLD_Type()
)
ctxGTLicensePoolPLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolPLD.setStatus("current")
_CtxGTLicensePoolPLDFullName_Type = WtcsDisplayString
_CtxGTLicensePoolPLDFullName_Object = MibTableColumn
ctxGTLicensePoolPLDFullName = _CtxGTLicensePoolPLDFullName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 12),
    _CtxGTLicensePoolPLDFullName_Type()
)
ctxGTLicensePoolPLDFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolPLDFullName.setStatus("current")
_CtxGTLicensePoolPooledAvailable_Type = Gauge32
_CtxGTLicensePoolPooledAvailable_Object = MibTableColumn
ctxGTLicensePoolPooledAvailable = _CtxGTLicensePoolPooledAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 13),
    _CtxGTLicensePoolPooledAvailable_Type()
)
ctxGTLicensePoolPooledAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolPooledAvailable.setStatus("current")
_CtxGTLicensePoolSubscriptionDate_Type = DateAndTime
_CtxGTLicensePoolSubscriptionDate_Object = MibTableColumn
ctxGTLicensePoolSubscriptionDate = _CtxGTLicensePoolSubscriptionDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 14),
    _CtxGTLicensePoolSubscriptionDate_Type()
)
ctxGTLicensePoolSubscriptionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolSubscriptionDate.setStatus("current")
_CtxGTLicensePoolUSERBASED_Type = Gauge32
_CtxGTLicensePoolUSERBASED_Object = MibTableColumn
ctxGTLicensePoolUSERBASED = _CtxGTLicensePoolUSERBASED_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 15),
    _CtxGTLicensePoolUSERBASED_Type()
)
ctxGTLicensePoolUSERBASED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolUSERBASED.setStatus("current")
_CtxGTLicensePoolVendorString_Type = WtcsDisplayString
_CtxGTLicensePoolVendorString_Object = MibTableColumn
ctxGTLicensePoolVendorString = _CtxGTLicensePoolVendorString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 2, 1, 16),
    _CtxGTLicensePoolVendorString_Type()
)
ctxGTLicensePoolVendorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxGTLicensePoolVendorString.setStatus("current")
_CitrixGTLicensesInLicensePlTable_Object = MibTable
citrixGTLicensesInLicensePlTable = _CitrixGTLicensesInLicensePlTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 3)
)
if mibBuilder.loadTexts:
    citrixGTLicensesInLicensePlTable.setStatus("current")
_CitrixGTLicensesInLicensePlEntry_Object = MibTableRow
citrixGTLicensesInLicensePlEntry = _CitrixGTLicensesInLicensePlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 3, 1)
)
citrixGTLicensesInLicensePlEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxgtllpIndex"),
)
if mibBuilder.loadTexts:
    citrixGTLicensesInLicensePlEntry.setStatus("current")


class _CtxgtllpIndex_Type(Integer32):
    """Custom type ctxgtllpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxgtllpIndex_Type.__name__ = "Integer32"
_CtxgtllpIndex_Object = MibTableColumn
ctxgtllpIndex = _CtxgtllpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 3, 1, 1),
    _CtxgtllpIndex_Type()
)
ctxgtllpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxgtllpIndex.setStatus("current")
_CtxgtllpLicense_Type = WtcsDisplayString
_CtxgtllpLicense_Object = MibTableColumn
ctxgtllpLicense = _CtxgtllpLicense_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 3, 1, 2),
    _CtxgtllpLicense_Type()
)
ctxgtllpLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxgtllpLicense.setStatus("current")
_CtxgtllpPool_Type = WtcsDisplayString
_CtxgtllpPool_Object = MibTableColumn
ctxgtllpPool = _CtxgtllpPool_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 3, 1, 3),
    _CtxgtllpPool_Type()
)
ctxgtllpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxgtllpPool.setStatus("current")
_CitrixLicenseSchemaVersionTable_Object = MibTable
citrixLicenseSchemaVersionTable = _CitrixLicenseSchemaVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 4)
)
if mibBuilder.loadTexts:
    citrixLicenseSchemaVersionTable.setStatus("current")
_CitrixLicenseSchemaVersionEntry_Object = MibTableRow
citrixLicenseSchemaVersionEntry = _CitrixLicenseSchemaVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 4, 1)
)
citrixLicenseSchemaVersionEntry.setIndexNames(
    (0, "INFORMANT-WMI-CITRIX", "ctxLicensingSchemaVersionIndex"),
)
if mibBuilder.loadTexts:
    citrixLicenseSchemaVersionEntry.setStatus("current")


class _CtxLicensingSchemaVersionIndex_Type(Integer32):
    """Custom type ctxLicensingSchemaVersionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxLicensingSchemaVersionIndex_Type.__name__ = "Integer32"
_CtxLicensingSchemaVersionIndex_Object = MibTableColumn
ctxLicensingSchemaVersionIndex = _CtxLicensingSchemaVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 4, 1, 1),
    _CtxLicensingSchemaVersionIndex_Type()
)
ctxLicensingSchemaVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxLicensingSchemaVersionIndex.setStatus("current")
_CtxLicensingSchemaVersionVersion_Type = WtcsDisplayString
_CtxLicensingSchemaVersionVersion_Object = MibTableColumn
ctxLicensingSchemaVersionVersion = _CtxLicensingSchemaVersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 42, 2, 4, 1, 2),
    _CtxLicensingSchemaVersionVersion_Type()
)
ctxLicensingSchemaVersionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxLicensingSchemaVersionVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-WMI-CITRIX",
    **{"citrixWmi": citrixWmi,
       "citrixWmiCitrix": citrixWmiCitrix,
       "citrixAccountAuthorityTable": citrixAccountAuthorityTable,
       "citrixAccountAuthorityEntry": citrixAccountAuthorityEntry,
       "ctxAccountAuthorityIndex": ctxAccountAuthorityIndex,
       "ctxAccountAuthorityName": ctxAccountAuthorityName,
       "ctxAccountAuthorityType": ctxAccountAuthorityType,
       "citrixApplicationFolderTable": citrixApplicationFolderTable,
       "citrixApplicationFolderEntry": citrixApplicationFolderEntry,
       "ctxApplicationFolderIndex": ctxApplicationFolderIndex,
       "ctxApplicationFolderFolderDN": ctxApplicationFolderFolderDN,
       "ctxApplicationFolderFolderName": ctxApplicationFolderFolderName,
       "citrixGroupTable": citrixGroupTable,
       "citrixGroupEntry": citrixGroupEntry,
       "ctxGroupIndex": ctxGroupIndex,
       "ctxGroupAccAuthority": ctxGroupAccAuthority,
       "ctxGroupAccountType": ctxGroupAccountType,
       "ctxGroupGroupName": ctxGroupGroupName,
       "citrixServerFolderTable": citrixServerFolderTable,
       "citrixServerFolderEntry": citrixServerFolderEntry,
       "ctxServerFolderIndex": ctxServerFolderIndex,
       "ctxServerFolderFolderDN": ctxServerFolderFolderDN,
       "ctxServerFolderFolderName": ctxServerFolderFolderName,
       "citrixServersInFolderTable": citrixServersInFolderTable,
       "citrixServersInFolderEntry": citrixServersInFolderEntry,
       "ctxServersInFolderIndex": ctxServersInFolderIndex,
       "ctxServersInFolderAntecedent": ctxServersInFolderAntecedent,
       "ctxServersInFolderDependent": ctxServersInFolderDependent,
       "citrixServersInZoneTable": citrixServersInZoneTable,
       "citrixServersInZoneEntry": citrixServersInZoneEntry,
       "ctxServersInZoneIndex": ctxServersInZoneIndex,
       "ctxServersInZoneServer": ctxServersInZoneServer,
       "ctxServersInZoneZone": ctxServersInZoneZone,
       "citrixUserTable": citrixUserTable,
       "citrixUserEntry": citrixUserEntry,
       "ctxUserIndex": ctxUserIndex,
       "ctxUserAccAuthority": ctxUserAccAuthority,
       "ctxUserAccountType": ctxUserAccountType,
       "ctxUserUserName": ctxUserUserName,
       "citrixUsersInGroupTable": citrixUsersInGroupTable,
       "citrixUsersInGroupEntry": citrixUsersInGroupEntry,
       "ctxUsersInGroupIndex": ctxUsersInGroupIndex,
       "ctxUsersInGroupAntecedent": ctxUsersInGroupAntecedent,
       "ctxUsersInGroupDependent": ctxUsersInGroupDependent,
       "citrixZoneTable": citrixZoneTable,
       "citrixZoneEntry": citrixZoneEntry,
       "ctxZoneIndex": ctxZoneIndex,
       "ctxZoneDataCollector": ctxZoneDataCollector,
       "ctxZoneNumServersInZone": ctxZoneNumServersInZone,
       "ctxZoneZoneName": ctxZoneZoneName,
       "metaframeApplLoadLevelTable": metaframeApplLoadLevelTable,
       "metaframeApplLoadLevelEntry": metaframeApplLoadLevelEntry,
       "mfApplicationLoadLevelIndex": mfApplicationLoadLevelIndex,
       "mfApplicationLoadLevelAppName": mfApplicationLoadLevelAppName,
       "mfApplicationLoadLevelLoadLevel": mfApplicationLoadLevelLoadLevel,
       "mfApplicationLoadLevelServerName": mfApplicationLoadLevelServerName,
       "metaframeApplPublishOnSvrTable": metaframeApplPublishOnSvrTable,
       "metaframeApplPublishOnSvrEntry": metaframeApplPublishOnSvrEntry,
       "mfaposIndex": mfaposIndex,
       "mfaposCtxServer": mfaposCtxServer,
       "mfaposWinApp": mfaposWinApp,
       "metaframeApplRunOnServerTable": metaframeApplRunOnServerTable,
       "metaframeApplRunOnServerEntry": metaframeApplRunOnServerEntry,
       "mfarosIndex": mfarosIndex,
       "mfarosApplication": mfarosApplication,
       "mfarosProcessId": mfarosProcessId,
       "mfarosServer": mfarosServer,
       "metaframeAppsForGroupTable": metaframeAppsForGroupTable,
       "metaframeAppsForGroupEntry": metaframeAppsForGroupEntry,
       "mfAppsForGroupIndex": mfAppsForGroupIndex,
       "mfAppsForGroupAntecedent": mfAppsForGroupAntecedent,
       "mfAppsForGroupDependent": mfAppsForGroupDependent,
       "metaframeAppsInFolderTable": metaframeAppsInFolderTable,
       "metaframeAppsInFolderEntry": metaframeAppsInFolderEntry,
       "mfAppsInFolderIndex": mfAppsInFolderIndex,
       "mfAppsInFolderAntecedent": mfAppsInFolderAntecedent,
       "mfAppsInFolderDependent": mfAppsInFolderDependent,
       "metaframeAppsInSessionTable": metaframeAppsInSessionTable,
       "metaframeAppsInSessionEntry": metaframeAppsInSessionEntry,
       "mfAppsInSessionIndex": mfAppsInSessionIndex,
       "mfAppsInSessionAntecedent": mfAppsInSessionAntecedent,
       "mfAppsInSessionDependent": mfAppsInSessionDependent,
       "metaframeDisconnectSessionTable": metaframeDisconnectSessionTable,
       "metaframeDisconnectSessionEntry": metaframeDisconnectSessionEntry,
       "mfdshIndex": mfdshIndex,
       "mfdshHowMany": mfdshHowMany,
       "mfdshWhen": mfdshWhen,
       "metaframeICAClientTable": metaframeICAClientTable,
       "metaframeICAClientEntry": metaframeICAClientEntry,
       "mfICAClientIndex": mfICAClientIndex,
       "mfICAClientClientAddress": mfICAClientClientAddress,
       "mfICAClientClientAddrFamily": mfICAClientClientAddrFamily,
       "mfICAClientClientBuild": mfICAClientClientBuild,
       "mfICAClientClientCacheDisk": mfICAClientClientCacheDisk,
       "mfICAClientClientCacheLowMem": mfICAClientClientCacheLowMem,
       "mfICAClientClientCacheTiny": mfICAClientClientCacheTiny,
       "mfICAClientClientCacheXms": mfICAClientClientCacheXms,
       "mfICAClientClientColorDepth": mfICAClientClientColorDepth,
       "mfICAClientClientDimBitmapMin": mfICAClientClientDimBitmapMin,
       "mfICAClientClientDimCacheSize": mfICAClientClientDimCacheSize,
       "mfICAClientClientDimVersion": mfICAClientClientDimVersion,
       "mfICAClientClientDirectory": mfICAClientClientDirectory,
       "mfICAClientClientEncryption": mfICAClientClientEncryption,
       "mfICAClientClientHardwareID": mfICAClientClientHardwareID,
       "mfICAClientClientHRes": mfICAClientClientHRes,
       "mfICAClientClientLicense": mfICAClientClientLicense,
       "mfICAClientClientModemName": mfICAClientClientModemName,
       "mfICAClientClientName": mfICAClientClientName,
       "mfICAClientClientProductID": mfICAClientClientProductID,
       "mfICAClientClientProductIDValue": mfICAClientClientProductIDValue,
       "mfICAClientClientVRes": mfICAClientClientVRes,
       "mfICAClientICABufLen": mfICAClientICABufLen,
       "metaframeInstalledSoftwareTable": metaframeInstalledSoftwareTable,
       "metaframeInstalledSoftwareEntry": metaframeInstalledSoftwareEntry,
       "mfInstalledSoftwareIndex": mfInstalledSoftwareIndex,
       "mfInstalledSoftwareServer": mfInstalledSoftwareServer,
       "mfInstalledSoftwareSoftware": mfInstalledSoftwareSoftware,
       "metaframeProcessTable": metaframeProcessTable,
       "metaframeProcessEntry": metaframeProcessEntry,
       "mfProcessIndex": mfProcessIndex,
       "mfProcessProcessID": mfProcessProcessID,
       "mfProcessProcessName": mfProcessProcessName,
       "mfProcessProcessState": mfProcessProcessState,
       "mfProcessServerName": mfProcessServerName,
       "mfProcessSessionID": mfProcessSessionID,
       "mfProcessUserName": mfProcessUserName,
       "metaframeProcessesInSessionTable": metaframeProcessesInSessionTable,
       "metaframeProcessesInSessionEntry": metaframeProcessesInSessionEntry,
       "mfProcessesInSessionIndex": mfProcessesInSessionIndex,
       "mfProcessesInSessionAntecedent": mfProcessesInSessionAntecedent,
       "mfProcessesInSessionDependent": mfProcessesInSessionDependent,
       "metaframeSchemaVersionTable": metaframeSchemaVersionTable,
       "metaframeSchemaVersionEntry": metaframeSchemaVersionEntry,
       "mfSchemaVersionIndex": mfSchemaVersionIndex,
       "mfSchemaVersionVersion": mfSchemaVersionVersion,
       "metaframeServerTable": metaframeServerTable,
       "metaframeServerEntry": metaframeServerEntry,
       "mfServerIndex": mfServerIndex,
       "mfServerDomain": mfServerDomain,
       "mfServerFarmName": mfServerFarmName,
       "mfServerIPAddress": mfServerIPAddress,
       "mfServerLoginsEnabled": mfServerLoginsEnabled,
       "mfServerNumberOfActiveSessions": mfServerNumberOfActiveSessions,
       "mfServerNumOfDisconnectSessions": mfServerNumOfDisconnectSessions,
       "mfServerNumberOfSessions": mfServerNumberOfSessions,
       "mfServerServerName": mfServerServerName,
       "mfServerServerType": mfServerServerType,
       "mfServerZoneName": mfServerZoneName,
       "mfServerZoneRanking": mfServerZoneRanking,
       "metaframeServerLoadLevelTable": metaframeServerLoadLevelTable,
       "metaframeServerLoadLevelEntry": metaframeServerLoadLevelEntry,
       "mfServerLoadLevelIndex": mfServerLoadLevelIndex,
       "mfServerLoadLevelLoadLevel": mfServerLoadLevelLoadLevel,
       "mfServerLoadLevelServerName": mfServerLoadLevelServerName,
       "metaframeSessionTable": metaframeSessionTable,
       "metaframeSessionEntry": metaframeSessionEntry,
       "mfSessionIndex": mfSessionIndex,
       "mfSessionClient": mfSessionClient,
       "mfSessionConnectTime": mfSessionConnectTime,
       "mfSessionCurrentTime": mfSessionCurrentTime,
       "mfSessionDisconnectTime": mfSessionDisconnectTime,
       "mfSessionLastInputTime": mfSessionLastInputTime,
       "mfSessionLogonTime": mfSessionLogonTime,
       "mfSessionNumberOfApps": mfSessionNumberOfApps,
       "mfSessionServerName": mfSessionServerName,
       "mfSessionSessionID": mfSessionSessionID,
       "mfSessionSessionName": mfSessionSessionName,
       "mfSessionSessionState": mfSessionSessionState,
       "mfSessionSessionUser": mfSessionSessionUser,
       "metaframeSoftwareTable": metaframeSoftwareTable,
       "metaframeSoftwareEntry": metaframeSoftwareEntry,
       "mfSoftwareIndex": mfSoftwareIndex,
       "mfSoftwareFeatureReleaseLevel": mfSoftwareFeatureReleaseLevel,
       "mfSoftwareInstallDate": mfSoftwareInstallDate,
       "mfSoftwareMFWinProductCode": mfSoftwareMFWinProductCode,
       "mfSoftwareProductName": mfSoftwareProductName,
       "mfSoftwareReleaseLevel": mfSoftwareReleaseLevel,
       "mfSoftwareVersion": mfSoftwareVersion,
       "metaframeWinApplicationTable": metaframeWinApplicationTable,
       "metaframeWinApplicationEntry": metaframeWinApplicationEntry,
       "mfWinApplIndex": mfWinApplIndex,
       "mfWinApplApplicationID": mfWinApplApplicationID,
       "mfWinApplAppVersion": mfWinApplAppVersion,
       "mfWinApplBrowserName": mfWinApplBrowserName,
       "mfWinApplDefaultEncryption": mfWinApplDefaultEncryption,
       "mfWinApplDefaultInitProg": mfWinApplDefaultInitProg,
       "mfWinApplDefaultSoundType": mfWinApplDefaultSoundType,
       "mfWinApplDefaultWindowColor": mfWinApplDefaultWindowColor,
       "mfWinApplDefaultWindowHeight": mfWinApplDefaultWindowHeight,
       "mfWinApplDefaultWindowScale": mfWinApplDefaultWindowScale,
       "mfWinApplDefaultWindowType": mfWinApplDefaultWindowType,
       "mfWinApplDefaultWindowWidth": mfWinApplDefaultWindowWidth,
       "mfWinApplDefaultWorkDir": mfWinApplDefaultWorkDir,
       "mfWinApplDescription": mfWinApplDescription,
       "mfWinApplDesktopIntegrate": mfWinApplDesktopIntegrate,
       "mfWinApplDistinguishedName": mfWinApplDistinguishedName,
       "mfWinApplEnableApp": mfWinApplEnableApp,
       "mfWinApplFarmName": mfWinApplFarmName,
       "mfWinApplMFAttributes": mfWinApplMFAttributes,
       "mfWinApplName": mfWinApplName,
       "mfWinApplParentFolderDN": mfWinApplParentFolderDN,
       "mfWinApplPNAttributes": mfWinApplPNAttributes,
       "mfWinApplPNFolder": mfWinApplPNFolder,
       "mfWinApplPublishingFlags": mfWinApplPublishingFlags,
       "mfWinApplReadOnly": mfWinApplReadOnly,
       "metaframeWinFarmTable": metaframeWinFarmTable,
       "metaframeWinFarmEntry": metaframeWinFarmEntry,
       "mfWinFarmIndex": mfWinFarmIndex,
       "mfWinFarmAlternateCachingMethod": mfWinFarmAlternateCachingMethod,
       "mfWinFarmDCRespondToClientBdcst": mfWinFarmDCRespondToClientBdcst,
       "mfWinFarmDegradationBias": mfWinFarmDegradationBias,
       "mfWinFarmDisableClientLocalTmEst": mfWinFarmDisableClientLocalTmEst,
       "mfWinFarmDiscardRedundantGraphic": mfWinFarmDiscardRedundantGraphic,
       "mfWinFarmEnableAutoClientReconn": mfWinFarmEnableAutoClientReconn,
       "mfWinFarmEnableDNSAddrResolution": mfWinFarmEnableDNSAddrResolution,
       "mfWinFarmEnableSNMPAgent": mfWinFarmEnableSNMPAgent,
       "mfWinFarmFarmName": mfWinFarmFarmName,
       "mfWinFarmICAVideoBufferSize": mfWinFarmICAVideoBufferSize,
       "mfWinFarmLegacyDisplayCompatMode": mfWinFarmLegacyDisplayCompatMode,
       "mfWinFarmLegacyServerCompatMode": mfWinFarmLegacyServerCompatMode,
       "mfWinFarmLogAutoReconnectAttempt": mfWinFarmLogAutoReconnectAttempt,
       "mfWinFarmLogOverLimitDenials": mfWinFarmLogOverLimitDenials,
       "mfWinFarmMaxConnectionsPerUser": mfWinFarmMaxConnectionsPerUser,
       "mfWinFarmNotifyDegradation": mfWinFarmNotifyDegradation,
       "mfWinFarmRASRespondToClientBdcst": mfWinFarmRASRespondToClientBdcst,
       "mfWinFarmSNMPDisconnectTrap": mfWinFarmSNMPDisconnectTrap,
       "mfWinFarmSNMPLogoffTrap": mfWinFarmSNMPLogoffTrap,
       "mfWinFarmSNMPLogonTrap": mfWinFarmSNMPLogonTrap,
       "mfWinFarmSNMPThresholdExceedTrap": mfWinFarmSNMPThresholdExceedTrap,
       "mfWinFarmSNMPThresholdValue": mfWinFarmSNMPThresholdValue,
       "mfWinFarmUseClientLocalTime": mfWinFarmUseClientLocalTime,
       "ciitrixWmiCitrixLicensing": ciitrixWmiCitrixLicensing,
       "citrixGTLicenseTable": citrixGTLicenseTable,
       "citrixGTLicenseEntry": citrixGTLicenseEntry,
       "ctxGTLicenseIndex": ctxGTLicenseIndex,
       "ctxGTLicenseCount": ctxGTLicenseCount,
       "ctxGTLicenseExpirationDate": ctxGTLicenseExpirationDate,
       "ctxGTLicenseLicenseType": ctxGTLicenseLicenseType,
       "ctxGTLicenseOverdraft": ctxGTLicenseOverdraft,
       "ctxGTLicensePLD": ctxGTLicensePLD,
       "ctxGTLicensePLDFullName": ctxGTLicensePLDFullName,
       "ctxGTLicenseSerialNumber": ctxGTLicenseSerialNumber,
       "ctxGTLicenseSubscriptionDate": ctxGTLicenseSubscriptionDate,
       "citrixGTLicensePoolTable": citrixGTLicensePoolTable,
       "citrixGTLicensePoolEntry": citrixGTLicensePoolEntry,
       "ctxGTLicensePoolIndex": ctxGTLicensePoolIndex,
       "ctxGTLicensePoolCount": ctxGTLicensePoolCount,
       "ctxGTLicensePoolDUPGROUP": ctxGTLicensePoolDUPGROUP,
       "ctxGTLicensePoolFLOATOK": ctxGTLicensePoolFLOATOK,
       "ctxGTLicensePoolHOSTBASED": ctxGTLicensePoolHOSTBASED,
       "ctxGTLicensePoolHOSTID": ctxGTLicensePoolHOSTID,
       "ctxGTLicensePoolInUseCount": ctxGTLicensePoolInUseCount,
       "ctxGTLicensePoolLicenseType": ctxGTLicensePoolLicenseType,
       "ctxGTLicensePoolOverdraft": ctxGTLicensePoolOverdraft,
       "ctxGTLicensePoolPLATFORMS": ctxGTLicensePoolPLATFORMS,
       "ctxGTLicensePoolPLD": ctxGTLicensePoolPLD,
       "ctxGTLicensePoolPLDFullName": ctxGTLicensePoolPLDFullName,
       "ctxGTLicensePoolPooledAvailable": ctxGTLicensePoolPooledAvailable,
       "ctxGTLicensePoolSubscriptionDate": ctxGTLicensePoolSubscriptionDate,
       "ctxGTLicensePoolUSERBASED": ctxGTLicensePoolUSERBASED,
       "ctxGTLicensePoolVendorString": ctxGTLicensePoolVendorString,
       "citrixGTLicensesInLicensePlTable": citrixGTLicensesInLicensePlTable,
       "citrixGTLicensesInLicensePlEntry": citrixGTLicensesInLicensePlEntry,
       "ctxgtllpIndex": ctxgtllpIndex,
       "ctxgtllpLicense": ctxgtllpLicense,
       "ctxgtllpPool": ctxgtllpPool,
       "citrixLicenseSchemaVersionTable": citrixLicenseSchemaVersionTable,
       "citrixLicenseSchemaVersionEntry": citrixLicenseSchemaVersionEntry,
       "ctxLicensingSchemaVersionIndex": ctxLicensingSchemaVersionIndex,
       "ctxLicensingSchemaVersionVersion": ctxLicensingSchemaVersionVersion}
)
