# SNMP MIB module (REDSTONE-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:36 2024
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

rsDs3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4)
)
rsDs3MIB.setRevisions(
        ("1999-07-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsDs3Objects_ObjectIdentity = ObjectIdentity
rsDs3Objects = _RsDs3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 1)
)
_RsDsx3ConfigTable_Object = MibTable
rsDsx3ConfigTable = _RsDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsDsx3ConfigTable.setStatus("current")
_RsDsx3ConfigEntry_Object = MibTableRow
rsDsx3ConfigEntry = _RsDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1)
)
rsDsx3ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsDsx3ConfigEntry.setStatus("current")


class _RsDsx3LineLength_Type(Integer32):
    """Custom type rsDsx3LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_RsDsx3LineLength_Type.__name__ = "Integer32"
_RsDsx3LineLength_Object = MibTableColumn
rsDsx3LineLength = _RsDsx3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 1),
    _RsDsx3LineLength_Type()
)
rsDsx3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx3LineLength.setStatus("current")
if mibBuilder.loadTexts:
    rsDsx3LineLength.setUnits("meters")


class _RsDsx3LineType_Type(Integer32):
    """Custom type rsDsx3LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              18,
              20)
        )
    )
    namedValues = NamedValues(
        *(("rsDsx3CbitParity", 4),
          ("rsDsx3CbitParityPlcp", 20),
          ("rsDsx3ClearChannel", 5),
          ("rsDsx3M23", 2),
          ("rsDsx3M23Plcp", 18),
          ("rsDsx3SYNTRAN", 3),
          ("rsDsx3other", 1),
          ("rsE3Framed", 7),
          ("rsE3G832", 6),
          ("rsE3Plcp", 8))
    )


_RsDsx3LineType_Type.__name__ = "Integer32"
_RsDsx3LineType_Object = MibTableColumn
rsDsx3LineType = _RsDsx3LineType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 2),
    _RsDsx3LineType_Type()
)
rsDsx3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx3LineType.setStatus("current")


class _RsDsx3CellScramblerConfig_Type(Integer32):
    """Custom type rsDsx3CellScramblerConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("scramblerOff", 2),
          ("scramblerOn", 1))
    )


_RsDsx3CellScramblerConfig_Type.__name__ = "Integer32"
_RsDsx3CellScramblerConfig_Object = MibTableColumn
rsDsx3CellScramblerConfig = _RsDsx3CellScramblerConfig_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 1, 1, 1, 3),
    _RsDsx3CellScramblerConfig_Type()
)
rsDsx3CellScramblerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx3CellScramblerConfig.setStatus("current")
_RsDs3Conformance_ObjectIdentity = ObjectIdentity
rsDs3Conformance = _RsDs3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 4)
)
_RsDs3Compliances_ObjectIdentity = ObjectIdentity
rsDs3Compliances = _RsDs3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 1)
)
_RsDs3Groups_ObjectIdentity = ObjectIdentity
rsDs3Groups = _RsDs3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 2)
)

# Managed Objects groups

rsDs3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 2, 1)
)
rsDs3Group.setObjects(
      *(("REDSTONE-DS3-MIB", "rsDsx3LineLength"),
        ("REDSTONE-DS3-MIB", "rsDsx3LineType"),
        ("REDSTONE-DS3-MIB", "rsDsx3CellScramblerConfig"))
)
if mibBuilder.loadTexts:
    rsDs3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsDs3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsDs3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-DS3-MIB",
    **{"rsDs3MIB": rsDs3MIB,
       "rsDs3Objects": rsDs3Objects,
       "rsDsx3ConfigTable": rsDsx3ConfigTable,
       "rsDsx3ConfigEntry": rsDsx3ConfigEntry,
       "rsDsx3LineLength": rsDsx3LineLength,
       "rsDsx3LineType": rsDsx3LineType,
       "rsDsx3CellScramblerConfig": rsDsx3CellScramblerConfig,
       "rsDs3Conformance": rsDs3Conformance,
       "rsDs3Compliances": rsDs3Compliances,
       "rsDs3Compliance": rsDs3Compliance,
       "rsDs3Groups": rsDs3Groups,
       "rsDs3Group": rsDs3Group}
)
