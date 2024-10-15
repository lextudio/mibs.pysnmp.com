# SNMP MIB module (NETSCREEN-VPN-IAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-IAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:02 2024
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

(netscreenVpn,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn")

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

_NsVpnIas_ObjectIdentity = ObjectIdentity
nsVpnIas = _NsVpnIas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11)
)
_NsVpnIasTable_Object = MibTable
nsVpnIasTable = _NsVpnIasTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 1)
)
if mibBuilder.loadTexts:
    nsVpnIasTable.setStatus("mandatory")
_NsVpnIasEntry_Object = MibTableRow
nsVpnIasEntry = _NsVpnIasEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 1, 1)
)
nsVpnIasEntry.setIndexNames(
    (0, "NETSCREEN-VPN-IAS-MIB", "nsVpnIasType"),
)
if mibBuilder.loadTexts:
    nsVpnIasEntry.setStatus("mandatory")


class _NsVpnIasType_Type(Integer32):
    """Custom type nsVpnIasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_NsVpnIasType_Type.__name__ = "Integer32"
_NsVpnIasType_Object = MibTableColumn
nsVpnIasType = _NsVpnIasType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 1, 1, 1),
    _NsVpnIasType_Type()
)
nsVpnIasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIasType.setStatus("mandatory")
_NsVpnIasTotal_Type = Counter32
_NsVpnIasTotal_Object = MibTableColumn
nsVpnIasTotal = _NsVpnIasTotal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 1, 1, 2),
    _NsVpnIasTotal_Type()
)
nsVpnIasTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIasTotal.setStatus("mandatory")
_NsVpnIasSessTable_Object = MibTable
nsVpnIasSessTable = _NsVpnIasSessTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 2)
)
if mibBuilder.loadTexts:
    nsVpnIasSessTable.setStatus("mandatory")
_NsVpnIasSessEntry_Object = MibTableRow
nsVpnIasSessEntry = _NsVpnIasSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 2, 1)
)
nsVpnIasSessEntry.setIndexNames(
    (0, "NETSCREEN-VPN-IAS-MIB", "nsVpnIasSessIndex"),
)
if mibBuilder.loadTexts:
    nsVpnIasSessEntry.setStatus("mandatory")
_NsVpnIasSessIndex_Type = Integer32
_NsVpnIasSessIndex_Object = MibTableColumn
nsVpnIasSessIndex = _NsVpnIasSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 2, 1, 1),
    _NsVpnIasSessIndex_Type()
)
nsVpnIasSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIasSessIndex.setStatus("mandatory")
_NsVpnIasSessXauthUserName_Type = DisplayString
_NsVpnIasSessXauthUserName_Object = MibTableColumn
nsVpnIasSessXauthUserName = _NsVpnIasSessXauthUserName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 11, 2, 1, 2),
    _NsVpnIasSessXauthUserName_Type()
)
nsVpnIasSessXauthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIasSessXauthUserName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-IAS-MIB",
    **{"nsVpnIas": nsVpnIas,
       "nsVpnIasTable": nsVpnIasTable,
       "nsVpnIasEntry": nsVpnIasEntry,
       "nsVpnIasType": nsVpnIasType,
       "nsVpnIasTotal": nsVpnIasTotal,
       "nsVpnIasSessTable": nsVpnIasSessTable,
       "nsVpnIasSessEntry": nsVpnIasSessEntry,
       "nsVpnIasSessIndex": nsVpnIasSessIndex,
       "nsVpnIasSessXauthUserName": nsVpnIasSessXauthUserName}
)
