# SNMP MIB module (ALTIGA-IP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-IP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:14 2024
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

(alIpMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alIpMibModule")

(alIpGroup,
 alStatsIp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alIpGroup",
    "alStatsIp")

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

altigaIpStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2)
)
altigaIpStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaIpStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaIpStatsMibConformance = _AltigaIpStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1)
)
_AltigaIpStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaIpStatsMibCompliances = _AltigaIpStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1)
)
_AlStatsIpGlobal_ObjectIdentity = ObjectIdentity
alStatsIpGlobal = _AlStatsIpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1)
)
_AlIpInterfaceStatsTable_Object = MibTable
alIpInterfaceStatsTable = _AlIpInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    alIpInterfaceStatsTable.setStatus("current")
_AlIpInterfaceStatsEntry_Object = MibTableRow
alIpInterfaceStatsEntry = _AlIpInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1)
)
alIpInterfaceStatsEntry.setIndexNames(
    (0, "ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    alIpInterfaceStatsEntry.setStatus("current")


class _AlIpInterfaceStatsIndex_Type(Integer32):
    """Custom type alIpInterfaceStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlIpInterfaceStatsIndex_Type.__name__ = "Integer32"
_AlIpInterfaceStatsIndex_Object = MibTableColumn
alIpInterfaceStatsIndex = _AlIpInterfaceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 1),
    _AlIpInterfaceStatsIndex_Type()
)
alIpInterfaceStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIpInterfaceStatsIndex.setStatus("current")


class _AlIpInterfaceStatsCurrentDuplex_Type(Integer32):
    """Custom type alIpInterfaceStatsCurrentDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 3))
    )


_AlIpInterfaceStatsCurrentDuplex_Type.__name__ = "Integer32"
_AlIpInterfaceStatsCurrentDuplex_Object = MibTableColumn
alIpInterfaceStatsCurrentDuplex = _AlIpInterfaceStatsCurrentDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 2),
    _AlIpInterfaceStatsCurrentDuplex_Type()
)
alIpInterfaceStatsCurrentDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIpInterfaceStatsCurrentDuplex.setStatus("current")

# Managed Objects groups

altigaIpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 8, 2)
)
altigaIpStatsGroup.setObjects(
      *(("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"),
        ("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsCurrentDuplex"))
)
if mibBuilder.loadTexts:
    altigaIpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaIpStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaIpStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-IP-STATS-MIB",
    **{"altigaIpStatsMibModule": altigaIpStatsMibModule,
       "altigaIpStatsMibConformance": altigaIpStatsMibConformance,
       "altigaIpStatsMibCompliances": altigaIpStatsMibCompliances,
       "altigaIpStatsMibCompliance": altigaIpStatsMibCompliance,
       "altigaIpStatsGroup": altigaIpStatsGroup,
       "alStatsIpGlobal": alStatsIpGlobal,
       "alIpInterfaceStatsTable": alIpInterfaceStatsTable,
       "alIpInterfaceStatsEntry": alIpInterfaceStatsEntry,
       "alIpInterfaceStatsIndex": alIpInterfaceStatsIndex,
       "alIpInterfaceStatsCurrentDuplex": alIpInterfaceStatsCurrentDuplex}
)
