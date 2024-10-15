# SNMP MIB module (XEDIA-POS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-POS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:02 2024
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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaPosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XPosTables_ObjectIdentity = ObjectIdentity
xPosTables = _XPosTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 1)
)
_XPosInterfaceConfTable_Object = MibTable
xPosInterfaceConfTable = _XPosInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1)
)
if mibBuilder.loadTexts:
    xPosInterfaceConfTable.setStatus("current")
_XPosInterfaceConfEntry_Object = MibTableRow
xPosInterfaceConfEntry = _XPosInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1, 1)
)
xPosInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPosInterfaceConfEntry.setStatus("current")


class _XPosConfigCrcMode_Type(Integer32):
    """Custom type xPosConfigCrcMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_XPosConfigCrcMode_Type.__name__ = "Integer32"
_XPosConfigCrcMode_Object = MibTableColumn
xPosConfigCrcMode = _XPosConfigCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1, 1, 1),
    _XPosConfigCrcMode_Type()
)
xPosConfigCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPosConfigCrcMode.setStatus("current")
_XPosConformance_ObjectIdentity = ObjectIdentity
xPosConformance = _XPosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 2)
)
_XPosCompliances_ObjectIdentity = ObjectIdentity
xPosCompliances = _XPosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 1)
)
_XPosGroups_ObjectIdentity = ObjectIdentity
xPosGroups = _XPosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 2)
)

# Managed Objects groups

xPosAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 2, 1)
)
xPosAllGroup.setObjects(
    ("XEDIA-POS-MIB", "xPosConfigCrcMode")
)
if mibBuilder.loadTexts:
    xPosAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xPosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xPosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-POS-MIB",
    **{"xediaPosMIB": xediaPosMIB,
       "xPosTables": xPosTables,
       "xPosInterfaceConfTable": xPosInterfaceConfTable,
       "xPosInterfaceConfEntry": xPosInterfaceConfEntry,
       "xPosConfigCrcMode": xPosConfigCrcMode,
       "xPosConformance": xPosConformance,
       "xPosCompliances": xPosCompliances,
       "xPosCompliance": xPosCompliance,
       "xPosGroups": xPosGroups,
       "xPosAllGroup": xPosAllGroup}
)
