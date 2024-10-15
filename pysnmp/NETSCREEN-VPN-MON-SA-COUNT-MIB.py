# SNMP MIB module (NETSCREEN-VPN-MON-SA-COUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-MON-SA-COUNT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:05 2024
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

(netscreenVpnMon,) = mibBuilder.importSymbols(
    "NETSCREEN-VPN-MON-MIB",
    "netscreenVpnMon")

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

_NsVpnMonSACountTable_Object = MibTable
nsVpnMonSACountTable = _NsVpnMonSACountTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2)
)
if mibBuilder.loadTexts:
    nsVpnMonSACountTable.setStatus("mandatory")
_NsVpnMonSACountEntry_Object = MibTableRow
nsVpnMonSACountEntry = _NsVpnMonSACountEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1)
)
nsVpnMonSACountEntry.setIndexNames(
    (0, "NETSCREEN-VPN-MON-SA-COUNT-MIB", "nsVpnMonSACountType"),
)
if mibBuilder.loadTexts:
    nsVpnMonSACountEntry.setStatus("mandatory")


class _NsVpnMonSACountType_Type(Integer32):
    """Custom type nsVpnMonSACountType based on Integer32"""
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


_NsVpnMonSACountType_Type.__name__ = "Integer32"
_NsVpnMonSACountType_Object = MibTableColumn
nsVpnMonSACountType = _NsVpnMonSACountType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 1),
    _NsVpnMonSACountType_Type()
)
nsVpnMonSACountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountType.setStatus("mandatory")
_NsVpnMonSACountTotal_Type = Counter32
_NsVpnMonSACountTotal_Object = MibTableColumn
nsVpnMonSACountTotal = _NsVpnMonSACountTotal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 2),
    _NsVpnMonSACountTotal_Type()
)
nsVpnMonSACountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountTotal.setStatus("mandatory")
_NsVpnMonSACountAct_Type = Counter32
_NsVpnMonSACountAct_Object = MibTableColumn
nsVpnMonSACountAct = _NsVpnMonSACountAct_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 3),
    _NsVpnMonSACountAct_Type()
)
nsVpnMonSACountAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountAct.setStatus("mandatory")
_NsVpnMonSACountInTotal_Type = Counter32
_NsVpnMonSACountInTotal_Object = MibTableColumn
nsVpnMonSACountInTotal = _NsVpnMonSACountInTotal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 4),
    _NsVpnMonSACountInTotal_Type()
)
nsVpnMonSACountInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountInTotal.setStatus("mandatory")
_NsVpnMonSACountInAct_Type = Counter32
_NsVpnMonSACountInAct_Object = MibTableColumn
nsVpnMonSACountInAct = _NsVpnMonSACountInAct_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 5),
    _NsVpnMonSACountInAct_Type()
)
nsVpnMonSACountInAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountInAct.setStatus("mandatory")
_NsVpnMonSACountOutTotal_Type = Counter32
_NsVpnMonSACountOutTotal_Object = MibTableColumn
nsVpnMonSACountOutTotal = _NsVpnMonSACountOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 6),
    _NsVpnMonSACountOutTotal_Type()
)
nsVpnMonSACountOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountOutTotal.setStatus("mandatory")
_NsVpnMonSACountOutAct_Type = Counter32
_NsVpnMonSACountOutAct_Object = MibTableColumn
nsVpnMonSACountOutAct = _NsVpnMonSACountOutAct_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 7),
    _NsVpnMonSACountOutAct_Type()
)
nsVpnMonSACountOutAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSACountOutAct.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-MON-SA-COUNT-MIB",
    **{"nsVpnMonSACountTable": nsVpnMonSACountTable,
       "nsVpnMonSACountEntry": nsVpnMonSACountEntry,
       "nsVpnMonSACountType": nsVpnMonSACountType,
       "nsVpnMonSACountTotal": nsVpnMonSACountTotal,
       "nsVpnMonSACountAct": nsVpnMonSACountAct,
       "nsVpnMonSACountInTotal": nsVpnMonSACountInTotal,
       "nsVpnMonSACountInAct": nsVpnMonSACountInAct,
       "nsVpnMonSACountOutTotal": nsVpnMonSACountOutTotal,
       "nsVpnMonSACountOutAct": nsVpnMonSACountOutAct}
)
