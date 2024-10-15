# SNMP MIB module (CISCO-FIPS-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FIPS-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:33 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoFipsStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999)
)
ciscoFipsStatsMIB.setRevisions(
        ("2003-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFipsStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFipsStatsMIBNotifs = _CiscoFipsStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 0)
)
_CiscoFipsStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFipsStatsMIBObjects = _CiscoFipsStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1)
)
_CfipsStats_ObjectIdentity = ObjectIdentity
cfipsStats = _CfipsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1)
)
_CfipsStatsGlobal_ObjectIdentity = ObjectIdentity
cfipsStatsGlobal = _CfipsStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1)
)


class _CfipsPostStatus_Type(Integer32):
    """Custom type cfipsPostStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("notAvailable", 4),
          ("passed", 2),
          ("running", 1))
    )


_CfipsPostStatus_Type.__name__ = "Integer32"
_CfipsPostStatus_Object = MibScalar
cfipsPostStatus = _CfipsPostStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 1),
    _CfipsPostStatus_Type()
)
cfipsPostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfipsPostStatus.setStatus("current")
_CiscoFipsStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoFipsStatsMIBConform = _CiscoFipsStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2)
)
_CiscoFipsStatsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFipsStatsMIBCompliances = _CiscoFipsStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1)
)
_CiscoFipsStatsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFipsStatsMIBGroups = _CiscoFipsStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2)
)

# Managed Objects groups

ciscoFipsStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 1)
)
ciscoFipsStatsMIBGroup.setObjects(
    ("CISCO-FIPS-STATS-MIB", "cfipsPostStatus")
)
if mibBuilder.loadTexts:
    ciscoFipsStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFipsStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFipsStatsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIPS-STATS-MIB",
    **{"ciscoFipsStatsMIB": ciscoFipsStatsMIB,
       "ciscoFipsStatsMIBNotifs": ciscoFipsStatsMIBNotifs,
       "ciscoFipsStatsMIBObjects": ciscoFipsStatsMIBObjects,
       "cfipsStats": cfipsStats,
       "cfipsStatsGlobal": cfipsStatsGlobal,
       "cfipsPostStatus": cfipsPostStatus,
       "ciscoFipsStatsMIBConform": ciscoFipsStatsMIBConform,
       "ciscoFipsStatsMIBCompliances": ciscoFipsStatsMIBCompliances,
       "ciscoFipsStatsMIBCompliance": ciscoFipsStatsMIBCompliance,
       "ciscoFipsStatsMIBGroups": ciscoFipsStatsMIBGroups,
       "ciscoFipsStatsMIBGroup": ciscoFipsStatsMIBGroup}
)
