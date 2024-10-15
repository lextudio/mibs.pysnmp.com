# SNMP MIB module (RFC1353-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1353-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:31 2024
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

(system,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "system")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Party(ObjectIdentifier):
    """Custom type Party based on ObjectIdentifier"""




class Clock(Integer32):
    """Custom type Clock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class TAddress(OctetString):
    """Custom type TAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpParties_ObjectIdentity = ObjectIdentity
snmpParties = _SnmpParties_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20)
)
_PartyAdmin_ObjectIdentity = ObjectIdentity
partyAdmin = _PartyAdmin_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1)
)
_PartyProtocols_ObjectIdentity = ObjectIdentity
partyProtocols = _PartyProtocols_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 1)
)
_NoAuth_ObjectIdentity = ObjectIdentity
noAuth = _NoAuth_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 1, 1)
)
_NoPriv_ObjectIdentity = ObjectIdentity
noPriv = _NoPriv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 1, 3)
)
_DesPrivProtocol_ObjectIdentity = ObjectIdentity
desPrivProtocol = _DesPrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 1, 4)
)
_Md5AuthProtocol_ObjectIdentity = ObjectIdentity
md5AuthProtocol = _Md5AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 1, 5)
)
_TransportDomains_ObjectIdentity = ObjectIdentity
transportDomains = _TransportDomains_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 2)
)
_Rfc1351Domain_ObjectIdentity = ObjectIdentity
rfc1351Domain = _Rfc1351Domain_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 2, 1)
)
_ProxyDomains_ObjectIdentity = ObjectIdentity
proxyDomains = _ProxyDomains_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 3)
)
_NoProxy_ObjectIdentity = ObjectIdentity
noProxy = _NoProxy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 3, 1)
)
_InitialPartyId_ObjectIdentity = ObjectIdentity
initialPartyId = _InitialPartyId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 1, 4)
)
_PartyPublic_ObjectIdentity = ObjectIdentity
partyPublic = _PartyPublic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 20, 2)
)
_PartyTable_Object = MibTable
partyTable = _PartyTable_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    partyTable.setStatus("mandatory")
_PartyEntry_Object = MibTableRow
partyEntry = _PartyEntry_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1)
)
partyEntry.setIndexNames(
    (0, "RFC1353-MIB", "partyIdentity"),
)
if mibBuilder.loadTexts:
    partyEntry.setStatus("mandatory")
_PartyIdentity_Type = Party
_PartyIdentity_Object = MibTableColumn
partyIdentity = _PartyIdentity_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 1),
    _PartyIdentity_Type()
)
partyIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyIdentity.setStatus("mandatory")


class _PartyTDomain_Type(ObjectIdentifier):
    """Custom type partyTDomain based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 20, 1, 2, 1)


_PartyTDomain_Object = MibTableColumn
partyTDomain = _PartyTDomain_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 2),
    _PartyTDomain_Type()
)
partyTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyTDomain.setStatus("mandatory")


class _PartyTAddress_Type(TAddress):
    """Custom type partyTAddress based on TAddress"""
    defaultHexValue = "000000000000"


_PartyTAddress_Object = MibTableColumn
partyTAddress = _PartyTAddress_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 3),
    _PartyTAddress_Type()
)
partyTAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyTAddress.setStatus("mandatory")


class _PartyProxyFor_Type(Party):
    """Custom type partyProxyFor based on Party"""
    defaultValue = (1, 3, 6, 1, 2, 1, 20, 1, 3, 1)


_PartyProxyFor_Object = MibTableColumn
partyProxyFor = _PartyProxyFor_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 4),
    _PartyProxyFor_Type()
)
partyProxyFor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyProxyFor.setStatus("mandatory")


class _PartyAuthProtocol_Type(ObjectIdentifier):
    """Custom type partyAuthProtocol based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 20, 1, 1, 5)


_PartyAuthProtocol_Object = MibTableColumn
partyAuthProtocol = _PartyAuthProtocol_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 5),
    _PartyAuthProtocol_Type()
)
partyAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyAuthProtocol.setStatus("mandatory")


class _PartyAuthClock_Type(Clock):
    """Custom type partyAuthClock based on Clock"""
    defaultValue = 0


_PartyAuthClock_Object = MibTableColumn
partyAuthClock = _PartyAuthClock_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 6),
    _PartyAuthClock_Type()
)
partyAuthClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyAuthClock.setStatus("mandatory")


class _PartyAuthPublic_Type(OctetString):
    """Custom type partyAuthPublic based on OctetString"""
    defaultHexValue = ""


_PartyAuthPublic_Object = MibTableColumn
partyAuthPublic = _PartyAuthPublic_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 7),
    _PartyAuthPublic_Type()
)
partyAuthPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyAuthPublic.setStatus("mandatory")


class _PartyAuthLifetime_Type(Integer32):
    """Custom type partyAuthLifetime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PartyAuthLifetime_Type.__name__ = "Integer32"
_PartyAuthLifetime_Object = MibTableColumn
partyAuthLifetime = _PartyAuthLifetime_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 8),
    _PartyAuthLifetime_Type()
)
partyAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyAuthLifetime.setStatus("mandatory")


class _PartyPrivProtocol_Type(ObjectIdentifier):
    """Custom type partyPrivProtocol based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 20, 1, 1, 3)


_PartyPrivProtocol_Object = MibTableColumn
partyPrivProtocol = _PartyPrivProtocol_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 9),
    _PartyPrivProtocol_Type()
)
partyPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyPrivProtocol.setStatus("mandatory")


class _PartyPrivPublic_Type(OctetString):
    """Custom type partyPrivPublic based on OctetString"""
    defaultHexValue = ""


_PartyPrivPublic_Object = MibTableColumn
partyPrivPublic = _PartyPrivPublic_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 10),
    _PartyPrivPublic_Type()
)
partyPrivPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyPrivPublic.setStatus("mandatory")


class _PartyMaxMessageSize_Type(Integer32):
    """Custom type partyMaxMessageSize based on Integer32"""
    defaultValue = 484

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65507),
    )


_PartyMaxMessageSize_Type.__name__ = "Integer32"
_PartyMaxMessageSize_Object = MibTableColumn
partyMaxMessageSize = _PartyMaxMessageSize_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 11),
    _PartyMaxMessageSize_Type()
)
partyMaxMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partyMaxMessageSize.setStatus("mandatory")


class _PartyStatus_Type(Integer32):
    """Custom type partyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_PartyStatus_Type.__name__ = "Integer32"
_PartyStatus_Object = MibTableColumn
partyStatus = _PartyStatus_Object(
    (1, 3, 6, 1, 2, 1, 20, 2, 1, 1, 12),
    _PartyStatus_Type()
)
partyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partyStatus.setStatus("mandatory")
_SnmpSecrets_ObjectIdentity = ObjectIdentity
snmpSecrets = _SnmpSecrets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 21)
)
_PartyPrivate_ObjectIdentity = ObjectIdentity
partyPrivate = _PartyPrivate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 21, 1)
)
_PartySecretsTable_Object = MibTable
partySecretsTable = _PartySecretsTable_Object(
    (1, 3, 6, 1, 2, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    partySecretsTable.setStatus("mandatory")
_PartySecretsEntry_Object = MibTableRow
partySecretsEntry = _PartySecretsEntry_Object(
    (1, 3, 6, 1, 2, 1, 21, 1, 1, 1)
)
partySecretsEntry.setIndexNames(
    (0, "RFC1353-MIB", "partySecretsIdentity"),
)
if mibBuilder.loadTexts:
    partySecretsEntry.setStatus("mandatory")
_PartySecretsIdentity_Type = Party
_PartySecretsIdentity_Object = MibTableColumn
partySecretsIdentity = _PartySecretsIdentity_Object(
    (1, 3, 6, 1, 2, 1, 21, 1, 1, 1, 1),
    _PartySecretsIdentity_Type()
)
partySecretsIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partySecretsIdentity.setStatus("mandatory")


class _PartySecretsAuthPrivate_Type(OctetString):
    """Custom type partySecretsAuthPrivate based on OctetString"""
    defaultHexValue = ""


_PartySecretsAuthPrivate_Object = MibTableColumn
partySecretsAuthPrivate = _PartySecretsAuthPrivate_Object(
    (1, 3, 6, 1, 2, 1, 21, 1, 1, 1, 2),
    _PartySecretsAuthPrivate_Type()
)
partySecretsAuthPrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partySecretsAuthPrivate.setStatus("mandatory")


class _PartySecretsPrivPrivate_Type(OctetString):
    """Custom type partySecretsPrivPrivate based on OctetString"""
    defaultHexValue = ""


_PartySecretsPrivPrivate_Object = MibTableColumn
partySecretsPrivPrivate = _PartySecretsPrivPrivate_Object(
    (1, 3, 6, 1, 2, 1, 21, 1, 1, 1, 3),
    _PartySecretsPrivPrivate_Type()
)
partySecretsPrivPrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partySecretsPrivPrivate.setStatus("mandatory")


class _PartySecretsStatus_Type(Integer32):
    """Custom type partySecretsStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_PartySecretsStatus_Type.__name__ = "Integer32"
_PartySecretsStatus_Object = MibTableColumn
partySecretsStatus = _PartySecretsStatus_Object(
    (1, 3, 6, 1, 2, 1, 21, 1, 1, 1, 4),
    _PartySecretsStatus_Type()
)
partySecretsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    partySecretsStatus.setStatus("mandatory")
_PartyAccess_ObjectIdentity = ObjectIdentity
partyAccess = _PartyAccess_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 21, 2)
)
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 2, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("mandatory")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 2, 1, 21, 2, 1, 1)
)
aclEntry.setIndexNames(
    (0, "RFC1353-MIB", "aclTarget"),
    (0, "RFC1353-MIB", "aclSubject"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("mandatory")
_AclTarget_Type = Party
_AclTarget_Object = MibTableColumn
aclTarget = _AclTarget_Object(
    (1, 3, 6, 1, 2, 1, 21, 2, 1, 1, 1),
    _AclTarget_Type()
)
aclTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclTarget.setStatus("mandatory")
_AclSubject_Type = Party
_AclSubject_Object = MibTableColumn
aclSubject = _AclSubject_Object(
    (1, 3, 6, 1, 2, 1, 21, 2, 1, 1, 2),
    _AclSubject_Type()
)
aclSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSubject.setStatus("mandatory")


class _AclPrivileges_Type(Integer32):
    """Custom type aclPrivileges based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AclPrivileges_Type.__name__ = "Integer32"
_AclPrivileges_Object = MibTableColumn
aclPrivileges = _AclPrivileges_Object(
    (1, 3, 6, 1, 2, 1, 21, 2, 1, 1, 3),
    _AclPrivileges_Type()
)
aclPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPrivileges.setStatus("mandatory")


class _AclStatus_Type(Integer32):
    """Custom type aclStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AclStatus_Type.__name__ = "Integer32"
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 2, 1, 21, 2, 1, 1, 4),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStatus.setStatus("mandatory")
_PartyViews_ObjectIdentity = ObjectIdentity
partyViews = _PartyViews_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 21, 3)
)
_ViewTable_Object = MibTable
viewTable = _ViewTable_Object(
    (1, 3, 6, 1, 2, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    viewTable.setStatus("mandatory")
_ViewEntry_Object = MibTableRow
viewEntry = _ViewEntry_Object(
    (1, 3, 6, 1, 2, 1, 21, 3, 1, 1)
)
viewEntry.setIndexNames(
    (0, "RFC1353-MIB", "viewParty"),
    (0, "RFC1353-MIB", "viewSubtree"),
)
if mibBuilder.loadTexts:
    viewEntry.setStatus("mandatory")
_ViewParty_Type = Party
_ViewParty_Object = MibTableColumn
viewParty = _ViewParty_Object(
    (1, 3, 6, 1, 2, 1, 21, 3, 1, 1, 1),
    _ViewParty_Type()
)
viewParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewParty.setStatus("mandatory")
_ViewSubtree_Type = ObjectIdentifier
_ViewSubtree_Object = MibTableColumn
viewSubtree = _ViewSubtree_Object(
    (1, 3, 6, 1, 2, 1, 21, 3, 1, 1, 2),
    _ViewSubtree_Type()
)
viewSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewSubtree.setStatus("mandatory")


class _ViewStatus_Type(Integer32):
    """Custom type viewStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1),
          ("invalid", 3))
    )


_ViewStatus_Type.__name__ = "Integer32"
_ViewStatus_Object = MibTableColumn
viewStatus = _ViewStatus_Object(
    (1, 3, 6, 1, 2, 1, 21, 3, 1, 1, 3),
    _ViewStatus_Type()
)
viewStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewStatus.setStatus("mandatory")


class _ViewMask_Type(OctetString):
    """Custom type viewMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ViewMask_Type.__name__ = "OctetString"
_ViewMask_Object = MibTableColumn
viewMask = _ViewMask_Object(
    (1, 3, 6, 1, 2, 1, 21, 3, 1, 1, 4),
    _ViewMask_Type()
)
viewMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1353-MIB",
    **{"Party": Party,
       "Clock": Clock,
       "TAddress": TAddress,
       "snmpParties": snmpParties,
       "partyAdmin": partyAdmin,
       "partyProtocols": partyProtocols,
       "noAuth": noAuth,
       "noPriv": noPriv,
       "desPrivProtocol": desPrivProtocol,
       "md5AuthProtocol": md5AuthProtocol,
       "transportDomains": transportDomains,
       "rfc1351Domain": rfc1351Domain,
       "proxyDomains": proxyDomains,
       "noProxy": noProxy,
       "initialPartyId": initialPartyId,
       "partyPublic": partyPublic,
       "partyTable": partyTable,
       "partyEntry": partyEntry,
       "partyIdentity": partyIdentity,
       "partyTDomain": partyTDomain,
       "partyTAddress": partyTAddress,
       "partyProxyFor": partyProxyFor,
       "partyAuthProtocol": partyAuthProtocol,
       "partyAuthClock": partyAuthClock,
       "partyAuthPublic": partyAuthPublic,
       "partyAuthLifetime": partyAuthLifetime,
       "partyPrivProtocol": partyPrivProtocol,
       "partyPrivPublic": partyPrivPublic,
       "partyMaxMessageSize": partyMaxMessageSize,
       "partyStatus": partyStatus,
       "snmpSecrets": snmpSecrets,
       "partyPrivate": partyPrivate,
       "partySecretsTable": partySecretsTable,
       "partySecretsEntry": partySecretsEntry,
       "partySecretsIdentity": partySecretsIdentity,
       "partySecretsAuthPrivate": partySecretsAuthPrivate,
       "partySecretsPrivPrivate": partySecretsPrivPrivate,
       "partySecretsStatus": partySecretsStatus,
       "partyAccess": partyAccess,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclTarget": aclTarget,
       "aclSubject": aclSubject,
       "aclPrivileges": aclPrivileges,
       "aclStatus": aclStatus,
       "partyViews": partyViews,
       "viewTable": viewTable,
       "viewEntry": viewEntry,
       "viewParty": viewParty,
       "viewSubtree": viewSubtree,
       "viewStatus": viewStatus,
       "viewMask": viewMask}
)
