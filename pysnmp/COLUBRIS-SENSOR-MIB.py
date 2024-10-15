# SNMP MIB module (COLUBRIS-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-SENSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:24 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisSensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisSensorMIBObjects_ObjectIdentity = ObjectIdentity
colubrisSensorMIBObjects = _ColubrisSensorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 1)
)
_CoSensorStatusGroup_ObjectIdentity = ObjectIdentity
coSensorStatusGroup = _CoSensorStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1)
)


class _CoSensorOperState_Type(Integer32):
    """Custom type coSensorOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CoSensorOperState_Type.__name__ = "Integer32"
_CoSensorOperState_Object = MibScalar
coSensorOperState = _CoSensorOperState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 1),
    _CoSensorOperState_Type()
)
coSensorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coSensorOperState.setStatus("current")


class _CoSensorConfigMode_Type(Integer32):
    """Custom type coSensorConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("shared", 1))
    )


_CoSensorConfigMode_Type.__name__ = "Integer32"
_CoSensorConfigMode_Object = MibScalar
coSensorConfigMode = _CoSensorConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 2),
    _CoSensorConfigMode_Type()
)
coSensorConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coSensorConfigMode.setStatus("current")


class _CoSensorOperMode_Type(Integer32):
    """Custom type coSensorOperMode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("intrusionPreventionA", 8),
          ("intrusionPreventionABG", 10),
          ("intrusionPreventionATroubleshootingBG", 9),
          ("intrusionPreventionBG", 4),
          ("noEthernetLink", 12),
          ("noIpAddress", 13),
          ("noRfManagerServer", 14),
          ("notActiveOrStarting", 15),
          ("troubleshootingA", 5),
          ("troubleshootingABG", 6),
          ("troubleshootingAIntrusionPreventionBG", 7),
          ("troubleshootingBG", 3),
          ("unknown", 1),
          ("upgradingSoftware", 11),
          ("workingNormally", 2))
    )


_CoSensorOperMode_Type.__name__ = "Integer32"
_CoSensorOperMode_Object = MibScalar
coSensorOperMode = _CoSensorOperMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 3),
    _CoSensorOperMode_Type()
)
coSensorOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coSensorOperMode.setStatus("current")
_ColubrisSensorMIBConformance_ObjectIdentity = ObjectIdentity
colubrisSensorMIBConformance = _ColubrisSensorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 2)
)
_ColubrisSensorMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisSensorMIBCompliances = _ColubrisSensorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 1)
)
_ColubrisSensorMIBGroups_ObjectIdentity = ObjectIdentity
colubrisSensorMIBGroups = _ColubrisSensorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 2)
)

# Managed Objects groups

colubrisSensorStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 2, 1)
)
colubrisSensorStatusMIBGroup.setObjects(
      *(("COLUBRIS-SENSOR-MIB", "coSensorOperState"),
        ("COLUBRIS-SENSOR-MIB", "coSensorConfigMode"),
        ("COLUBRIS-SENSOR-MIB", "coSensorOperMode"))
)
if mibBuilder.loadTexts:
    colubrisSensorStatusMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisSensorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisSensorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-SENSOR-MIB",
    **{"colubrisSensorMIB": colubrisSensorMIB,
       "colubrisSensorMIBObjects": colubrisSensorMIBObjects,
       "coSensorStatusGroup": coSensorStatusGroup,
       "coSensorOperState": coSensorOperState,
       "coSensorConfigMode": coSensorConfigMode,
       "coSensorOperMode": coSensorOperMode,
       "colubrisSensorMIBConformance": colubrisSensorMIBConformance,
       "colubrisSensorMIBCompliances": colubrisSensorMIBCompliances,
       "colubrisSensorMIBCompliance": colubrisSensorMIBCompliance,
       "colubrisSensorMIBGroups": colubrisSensorMIBGroups,
       "colubrisSensorStatusMIBGroup": colubrisSensorStatusMIBGroup}
)
