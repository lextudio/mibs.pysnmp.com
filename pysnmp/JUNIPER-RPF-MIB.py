# SNMP MIB module (JUNIPER-RPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-RPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:06 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

jnxRpf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17)
)
jnxRpf.setRevisions(
        ("2002-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxRpfStats_ObjectIdentity = ObjectIdentity
jnxRpfStats = _JnxRpfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1)
)
_JnxRpfStatsTable_Object = MibTable
jnxRpfStatsTable = _JnxRpfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    jnxRpfStatsTable.setStatus("current")
_JnxRpfStatsEntry_Object = MibTableRow
jnxRpfStatsEntry = _JnxRpfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1)
)
jnxRpfStatsEntry.setIndexNames(
    (0, "JUNIPER-RPF-MIB", "jnxRpfStatsIfIndex"),
    (0, "JUNIPER-RPF-MIB", "jnxRpfStatsAddrFamily"),
)
if mibBuilder.loadTexts:
    jnxRpfStatsEntry.setStatus("current")
_JnxRpfStatsIfIndex_Type = InterfaceIndex
_JnxRpfStatsIfIndex_Object = MibTableColumn
jnxRpfStatsIfIndex = _JnxRpfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 1),
    _JnxRpfStatsIfIndex_Type()
)
jnxRpfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpfStatsIfIndex.setStatus("current")


class _JnxRpfStatsAddrFamily_Type(Integer32):
    """Custom type jnxRpfStatsAddrFamily based on Integer32"""
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


_JnxRpfStatsAddrFamily_Type.__name__ = "Integer32"
_JnxRpfStatsAddrFamily_Object = MibTableColumn
jnxRpfStatsAddrFamily = _JnxRpfStatsAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 2),
    _JnxRpfStatsAddrFamily_Type()
)
jnxRpfStatsAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpfStatsAddrFamily.setStatus("current")
_JnxRpfStatsPackets_Type = Counter64
_JnxRpfStatsPackets_Object = MibTableColumn
jnxRpfStatsPackets = _JnxRpfStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 3),
    _JnxRpfStatsPackets_Type()
)
jnxRpfStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpfStatsPackets.setStatus("current")
_JnxRpfStatsBytes_Type = Counter64
_JnxRpfStatsBytes_Object = MibTableColumn
jnxRpfStatsBytes = _JnxRpfStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 4),
    _JnxRpfStatsBytes_Type()
)
jnxRpfStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpfStatsBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RPF-MIB",
    **{"jnxRpf": jnxRpf,
       "jnxRpfStats": jnxRpfStats,
       "jnxRpfStatsTable": jnxRpfStatsTable,
       "jnxRpfStatsEntry": jnxRpfStatsEntry,
       "jnxRpfStatsIfIndex": jnxRpfStatsIfIndex,
       "jnxRpfStatsAddrFamily": jnxRpfStatsAddrFamily,
       "jnxRpfStatsPackets": jnxRpfStatsPackets,
       "jnxRpfStatsBytes": jnxRpfStatsBytes}
)
