# SNMP MIB module (REDSTONE-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:48 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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

rsSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7)
)
rsSonetMIB.setRevisions(
        ("1998-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSonetObjects_ObjectIdentity = ObjectIdentity
rsSonetObjects = _RsSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1)
)
_RsSonetMediumTable_Object = MibTable
rsSonetMediumTable = _RsSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rsSonetMediumTable.setStatus("current")
_RsSonetMediumEntry_Object = MibTableRow
rsSonetMediumEntry = _RsSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1)
)
rsSonetMediumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsSonetMediumEntry.setStatus("current")


class _RsSonetMediumType_Type(Integer32):
    """Custom type rsSonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_RsSonetMediumType_Type.__name__ = "Integer32"
_RsSonetMediumType_Object = MibTableColumn
rsSonetMediumType = _RsSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 1),
    _RsSonetMediumType_Type()
)
rsSonetMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSonetMediumType.setStatus("current")


class _RsSonetMediumLoopbackConfig_Type(Integer32):
    """Custom type rsSonetMediumLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonetFacilityLoop", 1),
          ("sonetNoLoop", 0),
          ("sonetOtherLoop", 3),
          ("sonetTerminalLoop", 2))
    )


_RsSonetMediumLoopbackConfig_Type.__name__ = "Integer32"
_RsSonetMediumLoopbackConfig_Object = MibTableColumn
rsSonetMediumLoopbackConfig = _RsSonetMediumLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 2),
    _RsSonetMediumLoopbackConfig_Type()
)
rsSonetMediumLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSonetMediumLoopbackConfig.setStatus("current")


class _RsSonetMediumTimingSource_Type(Integer32):
    """Custom type rsSonetMediumTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("loop", 0))
    )


_RsSonetMediumTimingSource_Type.__name__ = "Integer32"
_RsSonetMediumTimingSource_Object = MibTableColumn
rsSonetMediumTimingSource = _RsSonetMediumTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 3),
    _RsSonetMediumTimingSource_Type()
)
rsSonetMediumTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSonetMediumTimingSource.setStatus("current")


class _RsSonetMediumCircuitIdentifier_Type(DisplayString):
    """Custom type rsSonetMediumCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsSonetMediumCircuitIdentifier_Type.__name__ = "DisplayString"
_RsSonetMediumCircuitIdentifier_Object = MibTableColumn
rsSonetMediumCircuitIdentifier = _RsSonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 1, 1, 1, 4),
    _RsSonetMediumCircuitIdentifier_Type()
)
rsSonetMediumCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSonetMediumCircuitIdentifier.setStatus("current")
_RsSonetConformance_ObjectIdentity = ObjectIdentity
rsSonetConformance = _RsSonetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 4)
)
_RsSonetCompliances_ObjectIdentity = ObjectIdentity
rsSonetCompliances = _RsSonetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 1)
)
_RsSonetGroups_ObjectIdentity = ObjectIdentity
rsSonetGroups = _RsSonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 2)
)

# Managed Objects groups

rsSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 2, 1)
)
rsSonetGroup.setObjects(
      *(("REDSTONE-SONET-MIB", "rsSonetMediumType"),
        ("REDSTONE-SONET-MIB", "rsSonetMediumLoopbackConfig"),
        ("REDSTONE-SONET-MIB", "rsSonetMediumTimingSource"),
        ("REDSTONE-SONET-MIB", "rsSonetMediumCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    rsSonetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsSonetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsSonetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-SONET-MIB",
    **{"rsSonetMIB": rsSonetMIB,
       "rsSonetObjects": rsSonetObjects,
       "rsSonetMediumTable": rsSonetMediumTable,
       "rsSonetMediumEntry": rsSonetMediumEntry,
       "rsSonetMediumType": rsSonetMediumType,
       "rsSonetMediumLoopbackConfig": rsSonetMediumLoopbackConfig,
       "rsSonetMediumTimingSource": rsSonetMediumTimingSource,
       "rsSonetMediumCircuitIdentifier": rsSonetMediumCircuitIdentifier,
       "rsSonetConformance": rsSonetConformance,
       "rsSonetCompliances": rsSonetCompliances,
       "rsSonetCompliance": rsSonetCompliance,
       "rsSonetGroups": rsSonetGroups,
       "rsSonetGroup": rsSonetGroup}
)
