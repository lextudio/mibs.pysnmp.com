# SNMP MIB module (DELL-NETWORKING-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:55 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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

dellNetIsisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18)
)
dellNetIsisMib.setRevisions(
        ("2011-07-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DellNetIsisISLevel(Integer32, TextualConvention):
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

_DellNetIsisNotifications_ObjectIdentity = ObjectIdentity
dellNetIsisNotifications = _DellNetIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 0)
)
_DellNetIsisObjects_ObjectIdentity = ObjectIdentity
dellNetIsisObjects = _DellNetIsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1)
)


class _DellNetIsisSysOloadSetOverload_Type(TruthValue):
    """Custom type dellNetIsisSysOloadSetOverload based on TruthValue"""


_DellNetIsisSysOloadSetOverload_Object = MibScalar
dellNetIsisSysOloadSetOverload = _DellNetIsisSysOloadSetOverload_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 1),
    _DellNetIsisSysOloadSetOverload_Type()
)
dellNetIsisSysOloadSetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadSetOverload.setStatus("current")


class _DellNetIsisSysOloadSetOloadOnStartupUntil_Type(Unsigned32):
    """Custom type dellNetIsisSysOloadSetOloadOnStartupUntil based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DellNetIsisSysOloadSetOloadOnStartupUntil_Type.__name__ = "Unsigned32"
_DellNetIsisSysOloadSetOloadOnStartupUntil_Object = MibScalar
dellNetIsisSysOloadSetOloadOnStartupUntil = _DellNetIsisSysOloadSetOloadOnStartupUntil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 2),
    _DellNetIsisSysOloadSetOloadOnStartupUntil_Type()
)
dellNetIsisSysOloadSetOloadOnStartupUntil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadSetOloadOnStartupUntil.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadSetOloadOnStartupUntil.setUnits("Seconds")


class _DellNetIsisSysOloadWaitForBgp_Type(Unsigned32):
    """Custom type dellNetIsisSysOloadWaitForBgp based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DellNetIsisSysOloadWaitForBgp_Type.__name__ = "Unsigned32"
_DellNetIsisSysOloadWaitForBgp_Object = MibScalar
dellNetIsisSysOloadWaitForBgp = _DellNetIsisSysOloadWaitForBgp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 3),
    _DellNetIsisSysOloadWaitForBgp_Type()
)
dellNetIsisSysOloadWaitForBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadWaitForBgp.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadWaitForBgp.setUnits("Seconds")


class _DellNetIsisSysOloadV6SetOverload_Type(TruthValue):
    """Custom type dellNetIsisSysOloadV6SetOverload based on TruthValue"""


_DellNetIsisSysOloadV6SetOverload_Object = MibScalar
dellNetIsisSysOloadV6SetOverload = _DellNetIsisSysOloadV6SetOverload_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 4),
    _DellNetIsisSysOloadV6SetOverload_Type()
)
dellNetIsisSysOloadV6SetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadV6SetOverload.setStatus("current")


class _DellNetIsisSysOloadV6SetOloadOnStartupUntil_Type(Unsigned32):
    """Custom type dellNetIsisSysOloadV6SetOloadOnStartupUntil based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DellNetIsisSysOloadV6SetOloadOnStartupUntil_Type.__name__ = "Unsigned32"
_DellNetIsisSysOloadV6SetOloadOnStartupUntil_Object = MibScalar
dellNetIsisSysOloadV6SetOloadOnStartupUntil = _DellNetIsisSysOloadV6SetOloadOnStartupUntil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 5),
    _DellNetIsisSysOloadV6SetOloadOnStartupUntil_Type()
)
dellNetIsisSysOloadV6SetOloadOnStartupUntil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadV6SetOloadOnStartupUntil.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadV6SetOloadOnStartupUntil.setUnits("Seconds")


class _DellNetIsisSysOloadV6WaitForBgp_Type(Unsigned32):
    """Custom type dellNetIsisSysOloadV6WaitForBgp based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DellNetIsisSysOloadV6WaitForBgp_Type.__name__ = "Unsigned32"
_DellNetIsisSysOloadV6WaitForBgp_Object = MibScalar
dellNetIsisSysOloadV6WaitForBgp = _DellNetIsisSysOloadV6WaitForBgp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 6),
    _DellNetIsisSysOloadV6WaitForBgp_Type()
)
dellNetIsisSysOloadV6WaitForBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadV6WaitForBgp.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIsisSysOloadV6WaitForBgp.setUnits("Seconds")
_DellNetIsisSysLevelTable_Object = MibTable
dellNetIsisSysLevelTable = _DellNetIsisSysLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7)
)
if mibBuilder.loadTexts:
    dellNetIsisSysLevelTable.setStatus("current")
_DellNetIsisSysLevelEntry_Object = MibTableRow
dellNetIsisSysLevelEntry = _DellNetIsisSysLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1)
)
dellNetIsisSysLevelEntry.setIndexNames(
    (0, "DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysLevelIndex"),
)
if mibBuilder.loadTexts:
    dellNetIsisSysLevelEntry.setStatus("current")
_DellNetIsisSysLevelIndex_Type = DellNetIsisISLevel
_DellNetIsisSysLevelIndex_Object = MibTableColumn
dellNetIsisSysLevelIndex = _DellNetIsisSysLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 1),
    _DellNetIsisSysLevelIndex_Type()
)
dellNetIsisSysLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetIsisSysLevelIndex.setStatus("current")
_DellNetIsisSysLevelOverloadState_Type = TruthValue
_DellNetIsisSysLevelOverloadState_Object = MibTableColumn
dellNetIsisSysLevelOverloadState = _DellNetIsisSysLevelOverloadState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 2),
    _DellNetIsisSysLevelOverloadState_Type()
)
dellNetIsisSysLevelOverloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIsisSysLevelOverloadState.setStatus("current")
_DellNetIsisSysLevelV6OverloadState_Type = TruthValue
_DellNetIsisSysLevelV6OverloadState_Object = MibTableColumn
dellNetIsisSysLevelV6OverloadState = _DellNetIsisSysLevelV6OverloadState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 3),
    _DellNetIsisSysLevelV6OverloadState_Type()
)
dellNetIsisSysLevelV6OverloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIsisSysLevelV6OverloadState.setStatus("current")
_DellNetIsisConformance_ObjectIdentity = ObjectIdentity
dellNetIsisConformance = _DellNetIsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2)
)
_DellNetIsisGroups_ObjectIdentity = ObjectIdentity
dellNetIsisGroups = _DellNetIsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1)
)
_DellNetIsisCompliances_ObjectIdentity = ObjectIdentity
dellNetIsisCompliances = _DellNetIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2)
)

# Managed Objects groups

dellNetIsisSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 1)
)
dellNetIsisSystemGroup.setObjects(
      *(("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadSetOverload"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadSetOloadOnStartupUntil"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadWaitForBgp"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadV6SetOverload"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadV6SetOloadOnStartupUntil"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysLevelOverloadState"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysLevelV6OverloadState"),
        ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisSysOloadV6WaitForBgp"))
)
if mibBuilder.loadTexts:
    dellNetIsisSystemGroup.setStatus("current")


# Notification objects

dellNetIsisAdjChanges = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 0, 1)
)
if mibBuilder.loadTexts:
    dellNetIsisAdjChanges.setStatus(
        "current"
    )


# Notifications groups

dellNetIsisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 2)
)
dellNetIsisNotificationGroup.setObjects(
    ("DELL-NETWORKING-ISIS-MIB", "dellNetIsisAdjChanges")
)
if mibBuilder.loadTexts:
    dellNetIsisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetIsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetIsisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-ISIS-MIB",
    **{"DellNetIsisISLevel": DellNetIsisISLevel,
       "dellNetIsisMib": dellNetIsisMib,
       "dellNetIsisNotifications": dellNetIsisNotifications,
       "dellNetIsisAdjChanges": dellNetIsisAdjChanges,
       "dellNetIsisObjects": dellNetIsisObjects,
       "dellNetIsisSysOloadSetOverload": dellNetIsisSysOloadSetOverload,
       "dellNetIsisSysOloadSetOloadOnStartupUntil": dellNetIsisSysOloadSetOloadOnStartupUntil,
       "dellNetIsisSysOloadWaitForBgp": dellNetIsisSysOloadWaitForBgp,
       "dellNetIsisSysOloadV6SetOverload": dellNetIsisSysOloadV6SetOverload,
       "dellNetIsisSysOloadV6SetOloadOnStartupUntil": dellNetIsisSysOloadV6SetOloadOnStartupUntil,
       "dellNetIsisSysOloadV6WaitForBgp": dellNetIsisSysOloadV6WaitForBgp,
       "dellNetIsisSysLevelTable": dellNetIsisSysLevelTable,
       "dellNetIsisSysLevelEntry": dellNetIsisSysLevelEntry,
       "dellNetIsisSysLevelIndex": dellNetIsisSysLevelIndex,
       "dellNetIsisSysLevelOverloadState": dellNetIsisSysLevelOverloadState,
       "dellNetIsisSysLevelV6OverloadState": dellNetIsisSysLevelV6OverloadState,
       "dellNetIsisConformance": dellNetIsisConformance,
       "dellNetIsisGroups": dellNetIsisGroups,
       "dellNetIsisSystemGroup": dellNetIsisSystemGroup,
       "dellNetIsisNotificationGroup": dellNetIsisNotificationGroup,
       "dellNetIsisCompliances": dellNetIsisCompliances,
       "dellNetIsisCompliance": dellNetIsisCompliance}
)
