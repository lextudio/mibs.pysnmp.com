# SNMP MIB module (PPP-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PPP-SEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:33 2024
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

(ppp,) = mibBuilder.importSymbols(
    "PPP-LCP-MIB",
    "ppp")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppSecurity_ObjectIdentity = ObjectIdentity
pppSecurity = _PppSecurity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 2)
)
_PppSecurityProtocols_ObjectIdentity = ObjectIdentity
pppSecurityProtocols = _PppSecurityProtocols_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 1)
)
_PppSecurityPapProtocol_ObjectIdentity = ObjectIdentity
pppSecurityPapProtocol = _PppSecurityPapProtocol_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 1)
)
_PppSecurityChapMD5Protocol_ObjectIdentity = ObjectIdentity
pppSecurityChapMD5Protocol = _PppSecurityChapMD5Protocol_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 2)
)
_PppSecurityConfigTable_Object = MibTable
pppSecurityConfigTable = _PppSecurityConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 2)
)
if mibBuilder.loadTexts:
    pppSecurityConfigTable.setStatus("mandatory")
_PppSecurityConfigEntry_Object = MibTableRow
pppSecurityConfigEntry = _PppSecurityConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1)
)
pppSecurityConfigEntry.setIndexNames(
    (0, "PPP-SEC-MIB", "pppSecurityConfigLink"),
    (0, "PPP-SEC-MIB", "pppSecurityConfigPreference"),
)
if mibBuilder.loadTexts:
    pppSecurityConfigEntry.setStatus("mandatory")


class _PppSecurityConfigLink_Type(Integer32):
    """Custom type pppSecurityConfigLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppSecurityConfigLink_Type.__name__ = "Integer32"
_PppSecurityConfigLink_Object = MibTableColumn
pppSecurityConfigLink = _PppSecurityConfigLink_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 1),
    _PppSecurityConfigLink_Type()
)
pppSecurityConfigLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecurityConfigLink.setStatus("mandatory")


class _PppSecurityConfigPreference_Type(Integer32):
    """Custom type pppSecurityConfigPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppSecurityConfigPreference_Type.__name__ = "Integer32"
_PppSecurityConfigPreference_Object = MibTableColumn
pppSecurityConfigPreference = _PppSecurityConfigPreference_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 2),
    _PppSecurityConfigPreference_Type()
)
pppSecurityConfigPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecurityConfigPreference.setStatus("mandatory")
_PppSecurityConfigProtocol_Type = ObjectIdentifier
_PppSecurityConfigProtocol_Object = MibTableColumn
pppSecurityConfigProtocol = _PppSecurityConfigProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 3),
    _PppSecurityConfigProtocol_Type()
)
pppSecurityConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecurityConfigProtocol.setStatus("mandatory")


class _PppSecurityConfigStatus_Type(Integer32):
    """Custom type pppSecurityConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PppSecurityConfigStatus_Type.__name__ = "Integer32"
_PppSecurityConfigStatus_Object = MibTableColumn
pppSecurityConfigStatus = _PppSecurityConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 4),
    _PppSecurityConfigStatus_Type()
)
pppSecurityConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecurityConfigStatus.setStatus("mandatory")
_PppSecuritySecretsTable_Object = MibTable
pppSecuritySecretsTable = _PppSecuritySecretsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3)
)
if mibBuilder.loadTexts:
    pppSecuritySecretsTable.setStatus("mandatory")
_PppSecuritySecretsEntry_Object = MibTableRow
pppSecuritySecretsEntry = _PppSecuritySecretsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1)
)
pppSecuritySecretsEntry.setIndexNames(
    (0, "PPP-SEC-MIB", "pppSecuritySecretsLink"),
    (0, "PPP-SEC-MIB", "pppSecuritySecretsIdIndex"),
)
if mibBuilder.loadTexts:
    pppSecuritySecretsEntry.setStatus("mandatory")


class _PppSecuritySecretsLink_Type(Integer32):
    """Custom type pppSecuritySecretsLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppSecuritySecretsLink_Type.__name__ = "Integer32"
_PppSecuritySecretsLink_Object = MibTableColumn
pppSecuritySecretsLink = _PppSecuritySecretsLink_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 1),
    _PppSecuritySecretsLink_Type()
)
pppSecuritySecretsLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSecuritySecretsLink.setStatus("mandatory")


class _PppSecuritySecretsIdIndex_Type(Integer32):
    """Custom type pppSecuritySecretsIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppSecuritySecretsIdIndex_Type.__name__ = "Integer32"
_PppSecuritySecretsIdIndex_Object = MibTableColumn
pppSecuritySecretsIdIndex = _PppSecuritySecretsIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 2),
    _PppSecuritySecretsIdIndex_Type()
)
pppSecuritySecretsIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSecuritySecretsIdIndex.setStatus("mandatory")


class _PppSecuritySecretsDirection_Type(Integer32):
    """Custom type pppSecuritySecretsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-to-remote", 1),
          ("remote-to-local", 2))
    )


_PppSecuritySecretsDirection_Type.__name__ = "Integer32"
_PppSecuritySecretsDirection_Object = MibTableColumn
pppSecuritySecretsDirection = _PppSecuritySecretsDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 3),
    _PppSecuritySecretsDirection_Type()
)
pppSecuritySecretsDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecuritySecretsDirection.setStatus("mandatory")
_PppSecuritySecretsProtocol_Type = ObjectIdentifier
_PppSecuritySecretsProtocol_Object = MibTableColumn
pppSecuritySecretsProtocol = _PppSecuritySecretsProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 4),
    _PppSecuritySecretsProtocol_Type()
)
pppSecuritySecretsProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecuritySecretsProtocol.setStatus("mandatory")


class _PppSecuritySecretsIdentity_Type(OctetString):
    """Custom type pppSecuritySecretsIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PppSecuritySecretsIdentity_Type.__name__ = "OctetString"
_PppSecuritySecretsIdentity_Object = MibTableColumn
pppSecuritySecretsIdentity = _PppSecuritySecretsIdentity_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 5),
    _PppSecuritySecretsIdentity_Type()
)
pppSecuritySecretsIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecuritySecretsIdentity.setStatus("mandatory")


class _PppSecuritySecretsSecret_Type(OctetString):
    """Custom type pppSecuritySecretsSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PppSecuritySecretsSecret_Type.__name__ = "OctetString"
_PppSecuritySecretsSecret_Object = MibTableColumn
pppSecuritySecretsSecret = _PppSecuritySecretsSecret_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 6),
    _PppSecuritySecretsSecret_Type()
)
pppSecuritySecretsSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecuritySecretsSecret.setStatus("mandatory")


class _PppSecuritySecretsStatus_Type(Integer32):
    """Custom type pppSecuritySecretsStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PppSecuritySecretsStatus_Type.__name__ = "Integer32"
_PppSecuritySecretsStatus_Object = MibTableColumn
pppSecuritySecretsStatus = _PppSecuritySecretsStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 7),
    _PppSecuritySecretsStatus_Type()
)
pppSecuritySecretsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppSecuritySecretsStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPP-SEC-MIB",
    **{"pppSecurity": pppSecurity,
       "pppSecurityProtocols": pppSecurityProtocols,
       "pppSecurityPapProtocol": pppSecurityPapProtocol,
       "pppSecurityChapMD5Protocol": pppSecurityChapMD5Protocol,
       "pppSecurityConfigTable": pppSecurityConfigTable,
       "pppSecurityConfigEntry": pppSecurityConfigEntry,
       "pppSecurityConfigLink": pppSecurityConfigLink,
       "pppSecurityConfigPreference": pppSecurityConfigPreference,
       "pppSecurityConfigProtocol": pppSecurityConfigProtocol,
       "pppSecurityConfigStatus": pppSecurityConfigStatus,
       "pppSecuritySecretsTable": pppSecuritySecretsTable,
       "pppSecuritySecretsEntry": pppSecuritySecretsEntry,
       "pppSecuritySecretsLink": pppSecuritySecretsLink,
       "pppSecuritySecretsIdIndex": pppSecuritySecretsIdIndex,
       "pppSecuritySecretsDirection": pppSecuritySecretsDirection,
       "pppSecuritySecretsProtocol": pppSecuritySecretsProtocol,
       "pppSecuritySecretsIdentity": pppSecuritySecretsIdentity,
       "pppSecuritySecretsSecret": pppSecuritySecretsSecret,
       "pppSecuritySecretsStatus": pppSecuritySecretsStatus}
)
