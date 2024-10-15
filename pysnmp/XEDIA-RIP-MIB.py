# SNMP MIB module (XEDIA-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-RIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:04 2024
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

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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

xediaRipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XripObjects_ObjectIdentity = ObjectIdentity
xripObjects = _XripObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1)
)


class _XripAdminStat_Type(Integer32):
    """Custom type xripAdminStat based on Integer32"""
    defaultValue = 1

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


_XripAdminStat_Type.__name__ = "Integer32"
_XripAdminStat_Object = MibScalar
xripAdminStat = _XripAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 1),
    _XripAdminStat_Type()
)
xripAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xripAdminStat.setStatus("current")


class _XripImportAdmin_Type(Integer32):
    """Custom type xripImportAdmin based on Integer32"""
    defaultValue = 1

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


_XripImportAdmin_Type.__name__ = "Integer32"
_XripImportAdmin_Object = MibScalar
xripImportAdmin = _XripImportAdmin_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 2),
    _XripImportAdmin_Type()
)
xripImportAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xripImportAdmin.setStatus("current")


class _XripImportMetric_Type(Integer32):
    """Custom type xripImportMetric based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_XripImportMetric_Type.__name__ = "Integer32"
_XripImportMetric_Object = MibScalar
xripImportMetric = _XripImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 3),
    _XripImportMetric_Type()
)
xripImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xripImportMetric.setStatus("current")


class _XripUpdateTimer_Type(Integer32):
    """Custom type xripUpdateTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 360),
    )


_XripUpdateTimer_Type.__name__ = "Integer32"
_XripUpdateTimer_Object = MibScalar
xripUpdateTimer = _XripUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 4),
    _XripUpdateTimer_Type()
)
xripUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xripUpdateTimer.setStatus("current")
_XRip2XIfConfTable_Object = MibTable
xRip2XIfConfTable = _XRip2XIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 10)
)
if mibBuilder.loadTexts:
    xRip2XIfConfTable.setStatus("current")
_XRip2XIfConfEntry_Object = MibTableRow
xRip2XIfConfEntry = _XRip2XIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 10, 1)
)
if mibBuilder.loadTexts:
    xRip2XIfConfEntry.setStatus("current")


class _Xrip2IfConfSlowConvergenceTechnique_Type(Integer32):
    """Custom type xrip2IfConfSlowConvergenceTechnique based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("poisonReverse", 3),
          ("splitHorizon", 2))
    )


_Xrip2IfConfSlowConvergenceTechnique_Type.__name__ = "Integer32"
_Xrip2IfConfSlowConvergenceTechnique_Object = MibTableColumn
xrip2IfConfSlowConvergenceTechnique = _Xrip2IfConfSlowConvergenceTechnique_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 10, 1, 1),
    _Xrip2IfConfSlowConvergenceTechnique_Type()
)
xrip2IfConfSlowConvergenceTechnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xrip2IfConfSlowConvergenceTechnique.setStatus("current")


class _Xrip2IfConfTriggerEvents_Type(Integer32):
    """Custom type xrip2IfConfTriggerEvents based on Integer32"""
    defaultValue = 1

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


_Xrip2IfConfTriggerEvents_Type.__name__ = "Integer32"
_Xrip2IfConfTriggerEvents_Object = MibTableColumn
xrip2IfConfTriggerEvents = _Xrip2IfConfTriggerEvents_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 1, 10, 1, 2),
    _Xrip2IfConfTriggerEvents_Type()
)
xrip2IfConfTriggerEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xrip2IfConfTriggerEvents.setStatus("current")
_XripConformance_ObjectIdentity = ObjectIdentity
xripConformance = _XripConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 2)
)
_XripCompliances_ObjectIdentity = ObjectIdentity
xripCompliances = _XripCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 2, 1)
)
_XripGroups_ObjectIdentity = ObjectIdentity
xripGroups = _XripGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 2, 2)
)
rip2IfConfEntry.registerAugmentions(
    ("XEDIA-RIP-MIB",
     "xRip2XIfConfEntry")
)
xRip2XIfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())

# Managed Objects groups

xripAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 2, 2, 1)
)
xripAllGroup.setObjects(
      *(("XEDIA-RIP-MIB", "xripAdminStat"),
        ("XEDIA-RIP-MIB", "xripImportAdmin"),
        ("XEDIA-RIP-MIB", "xripImportMetric"),
        ("XEDIA-RIP-MIB", "xrip2IfConfSlowConvergenceTechnique"),
        ("XEDIA-RIP-MIB", "xrip2IfConfTriggerEvents"))
)
if mibBuilder.loadTexts:
    xripAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xripCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xripCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-RIP-MIB",
    **{"xediaRipMIB": xediaRipMIB,
       "xripObjects": xripObjects,
       "xripAdminStat": xripAdminStat,
       "xripImportAdmin": xripImportAdmin,
       "xripImportMetric": xripImportMetric,
       "xripUpdateTimer": xripUpdateTimer,
       "xRip2XIfConfTable": xRip2XIfConfTable,
       "xRip2XIfConfEntry": xRip2XIfConfEntry,
       "xrip2IfConfSlowConvergenceTechnique": xrip2IfConfSlowConvergenceTechnique,
       "xrip2IfConfTriggerEvents": xrip2IfConfTriggerEvents,
       "xripConformance": xripConformance,
       "xripCompliances": xripCompliances,
       "xripCompliance": xripCompliance,
       "xripGroups": xripGroups,
       "xripAllGroup": xripAllGroup}
)
