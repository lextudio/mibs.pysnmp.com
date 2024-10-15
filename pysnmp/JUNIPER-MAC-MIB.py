# SNMP MIB module (JUNIPER-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:41 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxMac = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23)
)
jnxMac.setRevisions(
        ("2002-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxVlanIndex(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxMacStats_ObjectIdentity = ObjectIdentity
jnxMacStats = _JnxMacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1)
)
_JnxMacStatsTable_Object = MibTable
jnxMacStatsTable = _JnxMacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMacStatsTable.setStatus("current")
_JnxMacStatsEntry_Object = MibTableRow
jnxMacStatsEntry = _JnxMacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1)
)
jnxMacStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-MAC-MIB", "jnxVlanIndex"),
    (0, "JUNIPER-MAC-MIB", "jnxSourceMacAddress"),
)
if mibBuilder.loadTexts:
    jnxMacStatsEntry.setStatus("current")
_JnxVlanIndex_Type = JnxVlanIndex
_JnxVlanIndex_Object = MibTableColumn
jnxVlanIndex = _JnxVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 1),
    _JnxVlanIndex_Type()
)
jnxVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVlanIndex.setStatus("current")
_JnxSourceMacAddress_Type = MacAddress
_JnxSourceMacAddress_Object = MibTableColumn
jnxSourceMacAddress = _JnxSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 2),
    _JnxSourceMacAddress_Type()
)
jnxSourceMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSourceMacAddress.setStatus("current")
_JnxMacHCInOctets_Type = Counter64
_JnxMacHCInOctets_Object = MibTableColumn
jnxMacHCInOctets = _JnxMacHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 3),
    _JnxMacHCInOctets_Type()
)
jnxMacHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCInOctets.setStatus("current")
_JnxMacHCInFrames_Type = Counter64
_JnxMacHCInFrames_Object = MibTableColumn
jnxMacHCInFrames = _JnxMacHCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 4),
    _JnxMacHCInFrames_Type()
)
jnxMacHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCInFrames.setStatus("current")
_JnxMacHCOutOctets_Type = Counter64
_JnxMacHCOutOctets_Object = MibTableColumn
jnxMacHCOutOctets = _JnxMacHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 5),
    _JnxMacHCOutOctets_Type()
)
jnxMacHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCOutOctets.setStatus("current")
_JnxMacHCOutFrames_Type = Counter64
_JnxMacHCOutFrames_Object = MibTableColumn
jnxMacHCOutFrames = _JnxMacHCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 6),
    _JnxMacHCOutFrames_Type()
)
jnxMacHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCOutFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MAC-MIB",
    **{"JnxVlanIndex": JnxVlanIndex,
       "jnxMac": jnxMac,
       "jnxMacStats": jnxMacStats,
       "jnxMacStatsTable": jnxMacStatsTable,
       "jnxMacStatsEntry": jnxMacStatsEntry,
       "jnxVlanIndex": jnxVlanIndex,
       "jnxSourceMacAddress": jnxSourceMacAddress,
       "jnxMacHCInOctets": jnxMacHCInOctets,
       "jnxMacHCInFrames": jnxMacHCInFrames,
       "jnxMacHCOutOctets": jnxMacHCOutOctets,
       "jnxMacHCOutFrames": jnxMacHCOutFrames}
)
