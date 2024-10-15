# SNMP MIB module (CISCO-DOT11-ANTENNA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-ANTENNA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:44 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11AntennaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 384)
)
ciscoDot11AntennaMIB.setRevisions(
        ("2016-02-15 00:00",
         "2003-12-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CDot11AntennaMIBObjects_ObjectIdentity = ObjectIdentity
cDot11AntennaMIBObjects = _CDot11AntennaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 1)
)
_CDot11AntennaGlobal_ObjectIdentity = ObjectIdentity
cDot11AntennaGlobal = _CDot11AntennaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1)
)
_CDot11AntennaTable_Object = MibTable
cDot11AntennaTable = _CDot11AntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cDot11AntennaTable.setStatus("current")
_CDot11AntennaEntry_Object = MibTableRow
cDot11AntennaEntry = _CDot11AntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1)
)
cDot11AntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cDot11AntennaEntry.setStatus("current")
_CDot11AntennaIsGainConfigured_Type = TruthValue
_CDot11AntennaIsGainConfigured_Object = MibTableColumn
cDot11AntennaIsGainConfigured = _CDot11AntennaIsGainConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 1),
    _CDot11AntennaIsGainConfigured_Type()
)
cDot11AntennaIsGainConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AntennaIsGainConfigured.setStatus("current")


class _CDot11AntennaResultantGain_Type(Integer32):
    """Custom type cDot11AntennaResultantGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_CDot11AntennaResultantGain_Type.__name__ = "Integer32"
_CDot11AntennaResultantGain_Object = MibTableColumn
cDot11AntennaResultantGain = _CDot11AntennaResultantGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 2),
    _CDot11AntennaResultantGain_Type()
)
cDot11AntennaResultantGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AntennaResultantGain.setStatus("current")
_CDot11AntennaMIBConform_ObjectIdentity = ObjectIdentity
cDot11AntennaMIBConform = _CDot11AntennaMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 2)
)
_CDot11AntennaMIBCompliances_ObjectIdentity = ObjectIdentity
cDot11AntennaMIBCompliances = _CDot11AntennaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1)
)
_CDot11AntennaMIBGroups_ObjectIdentity = ObjectIdentity
cDot11AntennaMIBGroups = _CDot11AntennaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2)
)

# Managed Objects groups

cDot11AntennaGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2, 1)
)
cDot11AntennaGlobalGroup.setObjects(
      *(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaIsGainConfigured"),
        ("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaResultantGain"))
)
if mibBuilder.loadTexts:
    cDot11AntennaGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cDot11AntennaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cDot11AntennaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-ANTENNA-MIB",
    **{"ciscoDot11AntennaMIB": ciscoDot11AntennaMIB,
       "cDot11AntennaMIBObjects": cDot11AntennaMIBObjects,
       "cDot11AntennaGlobal": cDot11AntennaGlobal,
       "cDot11AntennaTable": cDot11AntennaTable,
       "cDot11AntennaEntry": cDot11AntennaEntry,
       "cDot11AntennaIsGainConfigured": cDot11AntennaIsGainConfigured,
       "cDot11AntennaResultantGain": cDot11AntennaResultantGain,
       "cDot11AntennaMIBConform": cDot11AntennaMIBConform,
       "cDot11AntennaMIBCompliances": cDot11AntennaMIBCompliances,
       "cDot11AntennaMIBCompliance": cDot11AntennaMIBCompliance,
       "cDot11AntennaMIBGroups": cDot11AntennaMIBGroups,
       "cDot11AntennaGlobalGroup": cDot11AntennaGlobalGroup}
)
