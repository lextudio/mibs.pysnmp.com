# SNMP MIB module (RADLAN-rlBrgMcMngr-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-rlBrgMcMngr-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:06 2024
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlBrgMcMngr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 117)
)
rlBrgMcMngr.setRevisions(
        ("2006-02-12 00:00",
         "2004-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlBrgMulticastManagerTable_Object = MibTable
rlBrgMulticastManagerTable = _RlBrgMulticastManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 1)
)
if mibBuilder.loadTexts:
    rlBrgMulticastManagerTable.setStatus("current")
_RlBrgMulticastManagerEntry_Object = MibTableRow
rlBrgMulticastManagerEntry = _RlBrgMulticastManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 1, 1)
)
rlBrgMulticastManagerEntry.setIndexNames(
    (0, "RADLAN-rlBrgMcMngr-MIB", "rlBrgMulticastManagerVlanTag"),
)
if mibBuilder.loadTexts:
    rlBrgMulticastManagerEntry.setStatus("current")
_RlBrgMulticastManagerVlanTag_Type = VlanIndex
_RlBrgMulticastManagerVlanTag_Object = MibTableColumn
rlBrgMulticastManagerVlanTag = _RlBrgMulticastManagerVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 1, 1, 1),
    _RlBrgMulticastManagerVlanTag_Type()
)
rlBrgMulticastManagerVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgMulticastManagerVlanTag.setStatus("current")


class _RlBrgMulticastManagerAdminVlanMode_Type(Integer32):
    """Custom type rlBrgMulticastManagerAdminVlanMode based on Integer32"""
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
        *(("ip-group", 2),
          ("ip-src-group", 3),
          ("mac-group", 1))
    )


_RlBrgMulticastManagerAdminVlanMode_Type.__name__ = "Integer32"
_RlBrgMulticastManagerAdminVlanMode_Object = MibTableColumn
rlBrgMulticastManagerAdminVlanMode = _RlBrgMulticastManagerAdminVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 1, 1, 2),
    _RlBrgMulticastManagerAdminVlanMode_Type()
)
rlBrgMulticastManagerAdminVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMulticastManagerAdminVlanMode.setStatus("current")


class _RlBrgMulticastManagerOperVlanMode_Type(Integer32):
    """Custom type rlBrgMulticastManagerOperVlanMode based on Integer32"""
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
        *(("ip-group", 2),
          ("ip-src-group", 3),
          ("mac-group", 1))
    )


_RlBrgMulticastManagerOperVlanMode_Type.__name__ = "Integer32"
_RlBrgMulticastManagerOperVlanMode_Object = MibTableColumn
rlBrgMulticastManagerOperVlanMode = _RlBrgMulticastManagerOperVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 1, 1, 3),
    _RlBrgMulticastManagerOperVlanMode_Type()
)
rlBrgMulticastManagerOperVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMulticastManagerOperVlanMode.setStatus("current")
_RlBrgMulticastInetManagerTable_Object = MibTable
rlBrgMulticastInetManagerTable = _RlBrgMulticastInetManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 2)
)
if mibBuilder.loadTexts:
    rlBrgMulticastInetManagerTable.setStatus("current")
_RlBrgMulticastInetManagerEntry_Object = MibTableRow
rlBrgMulticastInetManagerEntry = _RlBrgMulticastInetManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 2, 1)
)
rlBrgMulticastInetManagerEntry.setIndexNames(
    (0, "RADLAN-rlBrgMcMngr-MIB", "rlBrgMulticastInetManagerIpType"),
    (0, "RADLAN-rlBrgMcMngr-MIB", "rlBrgMulticastInetManagerVlanTag"),
)
if mibBuilder.loadTexts:
    rlBrgMulticastInetManagerEntry.setStatus("current")


class _RlBrgMulticastInetManagerIpType_Type(Integer32):
    """Custom type rlBrgMulticastInetManagerIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv6", 2),
          ("unknown", 0))
    )


_RlBrgMulticastInetManagerIpType_Type.__name__ = "Integer32"
_RlBrgMulticastInetManagerIpType_Object = MibTableColumn
rlBrgMulticastInetManagerIpType = _RlBrgMulticastInetManagerIpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 2, 1, 1),
    _RlBrgMulticastInetManagerIpType_Type()
)
rlBrgMulticastInetManagerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgMulticastInetManagerIpType.setStatus("current")
_RlBrgMulticastInetManagerVlanTag_Type = VlanIndex
_RlBrgMulticastInetManagerVlanTag_Object = MibTableColumn
rlBrgMulticastInetManagerVlanTag = _RlBrgMulticastInetManagerVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 2, 1, 2),
    _RlBrgMulticastInetManagerVlanTag_Type()
)
rlBrgMulticastInetManagerVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgMulticastInetManagerVlanTag.setStatus("current")


class _RlBrgMulticastInetManagerAdminVlanMode_Type(Integer32):
    """Custom type rlBrgMulticastInetManagerAdminVlanMode based on Integer32"""
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
        *(("ip-group", 2),
          ("ip-src-group", 3),
          ("mac-group", 1))
    )


_RlBrgMulticastInetManagerAdminVlanMode_Type.__name__ = "Integer32"
_RlBrgMulticastInetManagerAdminVlanMode_Object = MibTableColumn
rlBrgMulticastInetManagerAdminVlanMode = _RlBrgMulticastInetManagerAdminVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 2, 1, 3),
    _RlBrgMulticastInetManagerAdminVlanMode_Type()
)
rlBrgMulticastInetManagerAdminVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMulticastInetManagerAdminVlanMode.setStatus("current")


class _RlBrgMulticastInetManagerOperVlanMode_Type(Integer32):
    """Custom type rlBrgMulticastInetManagerOperVlanMode based on Integer32"""
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
        *(("ip-group", 2),
          ("ip-src-group", 3),
          ("mac-group", 1))
    )


_RlBrgMulticastInetManagerOperVlanMode_Type.__name__ = "Integer32"
_RlBrgMulticastInetManagerOperVlanMode_Object = MibTableColumn
rlBrgMulticastInetManagerOperVlanMode = _RlBrgMulticastInetManagerOperVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 117, 2, 1, 4),
    _RlBrgMulticastInetManagerOperVlanMode_Type()
)
rlBrgMulticastInetManagerOperVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMulticastInetManagerOperVlanMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-rlBrgMcMngr-MIB",
    **{"rlBrgMcMngr": rlBrgMcMngr,
       "rlBrgMulticastManagerTable": rlBrgMulticastManagerTable,
       "rlBrgMulticastManagerEntry": rlBrgMulticastManagerEntry,
       "rlBrgMulticastManagerVlanTag": rlBrgMulticastManagerVlanTag,
       "rlBrgMulticastManagerAdminVlanMode": rlBrgMulticastManagerAdminVlanMode,
       "rlBrgMulticastManagerOperVlanMode": rlBrgMulticastManagerOperVlanMode,
       "rlBrgMulticastInetManagerTable": rlBrgMulticastInetManagerTable,
       "rlBrgMulticastInetManagerEntry": rlBrgMulticastInetManagerEntry,
       "rlBrgMulticastInetManagerIpType": rlBrgMulticastInetManagerIpType,
       "rlBrgMulticastInetManagerVlanTag": rlBrgMulticastInetManagerVlanTag,
       "rlBrgMulticastInetManagerAdminVlanMode": rlBrgMulticastInetManagerAdminVlanMode,
       "rlBrgMulticastInetManagerOperVlanMode": rlBrgMulticastInetManagerOperVlanMode}
)
