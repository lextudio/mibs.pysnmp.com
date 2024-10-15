# SNMP MIB module (F10-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:24 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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

f10IsisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18)
)
f10IsisMib.setRevisions(
        ("2011-07-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class F10IsisISLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("area", 1),
          ("domain", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F10IsisNotifications_ObjectIdentity = ObjectIdentity
f10IsisNotifications = _F10IsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 0)
)
_F10IsisObjects_ObjectIdentity = ObjectIdentity
f10IsisObjects = _F10IsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1)
)


class _F10IsisSysOloadSetOverload_Type(TruthValue):
    """Custom type f10IsisSysOloadSetOverload based on TruthValue"""


_F10IsisSysOloadSetOverload_Object = MibScalar
f10IsisSysOloadSetOverload = _F10IsisSysOloadSetOverload_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 1),
    _F10IsisSysOloadSetOverload_Type()
)
f10IsisSysOloadSetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10IsisSysOloadSetOverload.setStatus("current")


class _F10IsisSysOloadSetOloadOnStartupUntil_Type(Unsigned32):
    """Custom type f10IsisSysOloadSetOloadOnStartupUntil based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_F10IsisSysOloadSetOloadOnStartupUntil_Type.__name__ = "Unsigned32"
_F10IsisSysOloadSetOloadOnStartupUntil_Object = MibScalar
f10IsisSysOloadSetOloadOnStartupUntil = _F10IsisSysOloadSetOloadOnStartupUntil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 2),
    _F10IsisSysOloadSetOloadOnStartupUntil_Type()
)
f10IsisSysOloadSetOloadOnStartupUntil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10IsisSysOloadSetOloadOnStartupUntil.setStatus("current")
if mibBuilder.loadTexts:
    f10IsisSysOloadSetOloadOnStartupUntil.setUnits("Seconds")


class _F10IsisSysOloadWaitForBgp_Type(Unsigned32):
    """Custom type f10IsisSysOloadWaitForBgp based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_F10IsisSysOloadWaitForBgp_Type.__name__ = "Unsigned32"
_F10IsisSysOloadWaitForBgp_Object = MibScalar
f10IsisSysOloadWaitForBgp = _F10IsisSysOloadWaitForBgp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 3),
    _F10IsisSysOloadWaitForBgp_Type()
)
f10IsisSysOloadWaitForBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10IsisSysOloadWaitForBgp.setStatus("current")
if mibBuilder.loadTexts:
    f10IsisSysOloadWaitForBgp.setUnits("Seconds")


class _F10IsisSysOloadV6SetOverload_Type(TruthValue):
    """Custom type f10IsisSysOloadV6SetOverload based on TruthValue"""


_F10IsisSysOloadV6SetOverload_Object = MibScalar
f10IsisSysOloadV6SetOverload = _F10IsisSysOloadV6SetOverload_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 4),
    _F10IsisSysOloadV6SetOverload_Type()
)
f10IsisSysOloadV6SetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10IsisSysOloadV6SetOverload.setStatus("current")


class _F10IsisSysOloadV6SetOloadOnStartupUntil_Type(Unsigned32):
    """Custom type f10IsisSysOloadV6SetOloadOnStartupUntil based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_F10IsisSysOloadV6SetOloadOnStartupUntil_Type.__name__ = "Unsigned32"
_F10IsisSysOloadV6SetOloadOnStartupUntil_Object = MibScalar
f10IsisSysOloadV6SetOloadOnStartupUntil = _F10IsisSysOloadV6SetOloadOnStartupUntil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 5),
    _F10IsisSysOloadV6SetOloadOnStartupUntil_Type()
)
f10IsisSysOloadV6SetOloadOnStartupUntil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10IsisSysOloadV6SetOloadOnStartupUntil.setStatus("current")
if mibBuilder.loadTexts:
    f10IsisSysOloadV6SetOloadOnStartupUntil.setUnits("Seconds")


class _F10IsisSysOloadV6WaitForBgp_Type(Unsigned32):
    """Custom type f10IsisSysOloadV6WaitForBgp based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_F10IsisSysOloadV6WaitForBgp_Type.__name__ = "Unsigned32"
_F10IsisSysOloadV6WaitForBgp_Object = MibScalar
f10IsisSysOloadV6WaitForBgp = _F10IsisSysOloadV6WaitForBgp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 6),
    _F10IsisSysOloadV6WaitForBgp_Type()
)
f10IsisSysOloadV6WaitForBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10IsisSysOloadV6WaitForBgp.setStatus("current")
if mibBuilder.loadTexts:
    f10IsisSysOloadV6WaitForBgp.setUnits("Seconds")
_F10IsisSysLevelTable_Object = MibTable
f10IsisSysLevelTable = _F10IsisSysLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7)
)
if mibBuilder.loadTexts:
    f10IsisSysLevelTable.setStatus("current")
_F10IsisSysLevelEntry_Object = MibTableRow
f10IsisSysLevelEntry = _F10IsisSysLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1)
)
f10IsisSysLevelEntry.setIndexNames(
    (0, "F10-ISIS-MIB", "f10IsisSysLevelIndex"),
)
if mibBuilder.loadTexts:
    f10IsisSysLevelEntry.setStatus("current")
_F10IsisSysLevelIndex_Type = F10IsisISLevel
_F10IsisSysLevelIndex_Object = MibTableColumn
f10IsisSysLevelIndex = _F10IsisSysLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 1),
    _F10IsisSysLevelIndex_Type()
)
f10IsisSysLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10IsisSysLevelIndex.setStatus("current")
_F10IsisSysLevelOverloadState_Type = TruthValue
_F10IsisSysLevelOverloadState_Object = MibTableColumn
f10IsisSysLevelOverloadState = _F10IsisSysLevelOverloadState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 2),
    _F10IsisSysLevelOverloadState_Type()
)
f10IsisSysLevelOverloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IsisSysLevelOverloadState.setStatus("current")
_F10IsisSysLevelV6OverloadState_Type = TruthValue
_F10IsisSysLevelV6OverloadState_Object = MibTableColumn
f10IsisSysLevelV6OverloadState = _F10IsisSysLevelV6OverloadState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 3),
    _F10IsisSysLevelV6OverloadState_Type()
)
f10IsisSysLevelV6OverloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IsisSysLevelV6OverloadState.setStatus("current")
_F10IsisConformance_ObjectIdentity = ObjectIdentity
f10IsisConformance = _F10IsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2)
)
_F10IsisGroups_ObjectIdentity = ObjectIdentity
f10IsisGroups = _F10IsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1)
)
_F10IsisCompliances_ObjectIdentity = ObjectIdentity
f10IsisCompliances = _F10IsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2)
)

# Managed Objects groups

f10IsisSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 1)
)
f10IsisSystemGroup.setObjects(
      *(("F10-ISIS-MIB", "f10IsisSysOloadSetOverload"),
        ("F10-ISIS-MIB", "f10IsisSysOloadSetOloadOnStartupUntil"),
        ("F10-ISIS-MIB", "f10IsisSysOloadWaitForBgp"),
        ("F10-ISIS-MIB", "f10IsisSysOloadV6SetOverload"),
        ("F10-ISIS-MIB", "f10IsisSysOloadV6SetOloadOnStartupUntil"),
        ("F10-ISIS-MIB", "f10IsisSysLevelOverloadState"),
        ("F10-ISIS-MIB", "f10IsisSysLevelV6OverloadState"),
        ("F10-ISIS-MIB", "f10IsisSysOloadV6WaitForBgp"))
)
if mibBuilder.loadTexts:
    f10IsisSystemGroup.setStatus("current")


# Notification objects

f10IsisAdjChanges = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 0, 1)
)
if mibBuilder.loadTexts:
    f10IsisAdjChanges.setStatus(
        "current"
    )


# Notifications groups

f10IsisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 2)
)
f10IsisNotificationGroup.setObjects(
    ("F10-ISIS-MIB", "f10IsisAdjChanges")
)
if mibBuilder.loadTexts:
    f10IsisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10IsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    f10IsisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-ISIS-MIB",
    **{"F10IsisISLevel": F10IsisISLevel,
       "f10IsisMib": f10IsisMib,
       "f10IsisNotifications": f10IsisNotifications,
       "f10IsisAdjChanges": f10IsisAdjChanges,
       "f10IsisObjects": f10IsisObjects,
       "f10IsisSysOloadSetOverload": f10IsisSysOloadSetOverload,
       "f10IsisSysOloadSetOloadOnStartupUntil": f10IsisSysOloadSetOloadOnStartupUntil,
       "f10IsisSysOloadWaitForBgp": f10IsisSysOloadWaitForBgp,
       "f10IsisSysOloadV6SetOverload": f10IsisSysOloadV6SetOverload,
       "f10IsisSysOloadV6SetOloadOnStartupUntil": f10IsisSysOloadV6SetOloadOnStartupUntil,
       "f10IsisSysOloadV6WaitForBgp": f10IsisSysOloadV6WaitForBgp,
       "f10IsisSysLevelTable": f10IsisSysLevelTable,
       "f10IsisSysLevelEntry": f10IsisSysLevelEntry,
       "f10IsisSysLevelIndex": f10IsisSysLevelIndex,
       "f10IsisSysLevelOverloadState": f10IsisSysLevelOverloadState,
       "f10IsisSysLevelV6OverloadState": f10IsisSysLevelV6OverloadState,
       "f10IsisConformance": f10IsisConformance,
       "f10IsisGroups": f10IsisGroups,
       "f10IsisSystemGroup": f10IsisSystemGroup,
       "f10IsisNotificationGroup": f10IsisNotificationGroup,
       "f10IsisCompliances": f10IsisCompliances,
       "f10IsisCompliance": f10IsisCompliance}
)
