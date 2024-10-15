# SNMP MIB module (JUNIPER-IPv4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IPv4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:11 2024
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

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxIpv4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12)
)
jnxIpv4.setRevisions(
        ("2001-08-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxIpv4Config_ObjectIdentity = ObjectIdentity
jnxIpv4Config = _JnxIpv4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1)
)
_JnxIpv4AddrTable_Object = MibTable
jnxIpv4AddrTable = _JnxIpv4AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1)
)
if mibBuilder.loadTexts:
    jnxIpv4AddrTable.setStatus("current")
_JnxIpv4AddrEntry_Object = MibTableRow
jnxIpv4AddrEntry = _JnxIpv4AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1)
)
jnxIpv4AddrEntry.setIndexNames(
    (0, "JUNIPER-IPv4-MIB", "jnxIpv4AdEntIfIndex"),
    (0, "JUNIPER-IPv4-MIB", "jnxIpv4AdEntAddr"),
)
if mibBuilder.loadTexts:
    jnxIpv4AddrEntry.setStatus("current")


class _JnxIpv4AdEntIfIndex_Type(Integer32):
    """Custom type jnxIpv4AdEntIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIpv4AdEntIfIndex_Type.__name__ = "Integer32"
_JnxIpv4AdEntIfIndex_Object = MibTableColumn
jnxIpv4AdEntIfIndex = _JnxIpv4AdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 1),
    _JnxIpv4AdEntIfIndex_Type()
)
jnxIpv4AdEntIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpv4AdEntIfIndex.setStatus("current")
_JnxIpv4AdEntAddr_Type = IpAddress
_JnxIpv4AdEntAddr_Object = MibTableColumn
jnxIpv4AdEntAddr = _JnxIpv4AdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 2),
    _JnxIpv4AdEntAddr_Type()
)
jnxIpv4AdEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpv4AdEntAddr.setStatus("current")
_JnxIpv4AdEntNetMask_Type = IpAddress
_JnxIpv4AdEntNetMask_Object = MibTableColumn
jnxIpv4AdEntNetMask = _JnxIpv4AdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 3),
    _JnxIpv4AdEntNetMask_Type()
)
jnxIpv4AdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv4AdEntNetMask.setStatus("current")


class _JnxIpv4AdEntBcastAddr_Type(Integer32):
    """Custom type jnxIpv4AdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_JnxIpv4AdEntBcastAddr_Type.__name__ = "Integer32"
_JnxIpv4AdEntBcastAddr_Object = MibTableColumn
jnxIpv4AdEntBcastAddr = _JnxIpv4AdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 4),
    _JnxIpv4AdEntBcastAddr_Type()
)
jnxIpv4AdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv4AdEntBcastAddr.setStatus("current")


class _JnxIpv4AdEntReasmMaxSize_Type(Integer32):
    """Custom type jnxIpv4AdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxIpv4AdEntReasmMaxSize_Type.__name__ = "Integer32"
_JnxIpv4AdEntReasmMaxSize_Object = MibTableColumn
jnxIpv4AdEntReasmMaxSize = _JnxIpv4AdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 5),
    _JnxIpv4AdEntReasmMaxSize_Type()
)
jnxIpv4AdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv4AdEntReasmMaxSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IPv4-MIB",
    **{"jnxIpv4": jnxIpv4,
       "jnxIpv4Config": jnxIpv4Config,
       "jnxIpv4AddrTable": jnxIpv4AddrTable,
       "jnxIpv4AddrEntry": jnxIpv4AddrEntry,
       "jnxIpv4AdEntIfIndex": jnxIpv4AdEntIfIndex,
       "jnxIpv4AdEntAddr": jnxIpv4AdEntAddr,
       "jnxIpv4AdEntNetMask": jnxIpv4AdEntNetMask,
       "jnxIpv4AdEntBcastAddr": jnxIpv4AdEntBcastAddr,
       "jnxIpv4AdEntReasmMaxSize": jnxIpv4AdEntReasmMaxSize}
)
