# SNMP MIB module (ENTERASYS-LINK-FLAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-LINK-FLAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:04 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysLinkFlapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52)
)
etsysLinkFlapMIB.setRevisions(
        ("2009-10-16 12:53",
         "2004-08-20 14:47")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LinkFlapIntfAction(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysLinkFlapObjects_ObjectIdentity = ObjectIdentity
etsysLinkFlapObjects = _EtsysLinkFlapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1)
)
_EtsysLinkFlapNotificationBranch_ObjectIdentity = ObjectIdentity
etsysLinkFlapNotificationBranch = _EtsysLinkFlapNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 0)
)
_EtsysLinkFlapSystemBranch_ObjectIdentity = ObjectIdentity
etsysLinkFlapSystemBranch = _EtsysLinkFlapSystemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1)
)


class _EtsysLinkFlapSystemState_Type(EnabledStatus):
    """Custom type etsysLinkFlapSystemState based on EnabledStatus"""


_EtsysLinkFlapSystemState_Object = MibScalar
etsysLinkFlapSystemState = _EtsysLinkFlapSystemState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1, 1),
    _EtsysLinkFlapSystemState_Type()
)
etsysLinkFlapSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapSystemState.setStatus("current")


class _EtsysLinkFlapSystemSupportedActions_Type(LinkFlapIntfAction):
    """Custom type etsysLinkFlapSystemSupportedActions based on LinkFlapIntfAction"""
    defaultBinValue = "111"


_EtsysLinkFlapSystemSupportedActions_Object = MibScalar
etsysLinkFlapSystemSupportedActions = _EtsysLinkFlapSystemSupportedActions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1, 2),
    _EtsysLinkFlapSystemSupportedActions_Type()
)
etsysLinkFlapSystemSupportedActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLinkFlapSystemSupportedActions.setStatus("current")
_EtsysLinkFlapSystemLinkFlapMaximum_Type = Unsigned32
_EtsysLinkFlapSystemLinkFlapMaximum_Object = MibScalar
etsysLinkFlapSystemLinkFlapMaximum = _EtsysLinkFlapSystemLinkFlapMaximum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1, 3),
    _EtsysLinkFlapSystemLinkFlapMaximum_Type()
)
etsysLinkFlapSystemLinkFlapMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLinkFlapSystemLinkFlapMaximum.setStatus("current")
_EtsysLinkFlapInterfaceBranch_ObjectIdentity = ObjectIdentity
etsysLinkFlapInterfaceBranch = _EtsysLinkFlapInterfaceBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2)
)
_EtsysLinkFlapInterfaceTable_Object = MibTable
etsysLinkFlapInterfaceTable = _EtsysLinkFlapInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLinkFlapInterfaceTable.setStatus("current")
_EtsysLinkFlapInterfaceEntry_Object = MibTableRow
etsysLinkFlapInterfaceEntry = _EtsysLinkFlapInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1)
)
etsysLinkFlapInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysLinkFlapInterfaceEntry.setStatus("current")


class _EtsysLinkFlapIntfEnabledStatus_Type(Integer32):
    """Custom type etsysLinkFlapIntfEnabledStatus based on Integer32"""
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


_EtsysLinkFlapIntfEnabledStatus_Type.__name__ = "Integer32"
_EtsysLinkFlapIntfEnabledStatus_Object = MibTableColumn
etsysLinkFlapIntfEnabledStatus = _EtsysLinkFlapIntfEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 1),
    _EtsysLinkFlapIntfEnabledStatus_Type()
)
etsysLinkFlapIntfEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfEnabledStatus.setStatus("current")


class _EtsysLinkFlapIntfAction_Type(LinkFlapIntfAction):
    """Custom type etsysLinkFlapIntfAction based on LinkFlapIntfAction"""
    defaultBinValue = "011"


_EtsysLinkFlapIntfAction_Object = MibTableColumn
etsysLinkFlapIntfAction = _EtsysLinkFlapIntfAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 2),
    _EtsysLinkFlapIntfAction_Type()
)
etsysLinkFlapIntfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfAction.setStatus("current")


class _EtsysLinkFlapIntfOperStatus_Type(Integer32):
    """Custom type etsysLinkFlapIntfOperStatus based on Integer32"""
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
          ("operational", 1))
    )


_EtsysLinkFlapIntfOperStatus_Type.__name__ = "Integer32"
_EtsysLinkFlapIntfOperStatus_Object = MibTableColumn
etsysLinkFlapIntfOperStatus = _EtsysLinkFlapIntfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 3),
    _EtsysLinkFlapIntfOperStatus_Type()
)
etsysLinkFlapIntfOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfOperStatus.setStatus("current")


class _EtsysLinkFlapIntfClearStats_Type(TruthValue):
    """Custom type etsysLinkFlapIntfClearStats based on TruthValue"""


_EtsysLinkFlapIntfClearStats_Object = MibTableColumn
etsysLinkFlapIntfClearStats = _EtsysLinkFlapIntfClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 4),
    _EtsysLinkFlapIntfClearStats_Type()
)
etsysLinkFlapIntfClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfClearStats.setStatus("current")


class _EtsysLinkFlapIntfCountThreshold_Type(Unsigned32):
    """Custom type etsysLinkFlapIntfCountThreshold based on Unsigned32"""
    defaultValue = 5


_EtsysLinkFlapIntfCountThreshold_Object = MibTableColumn
etsysLinkFlapIntfCountThreshold = _EtsysLinkFlapIntfCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 5),
    _EtsysLinkFlapIntfCountThreshold_Type()
)
etsysLinkFlapIntfCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfCountThreshold.setUnits("link state transitions")


class _EtsysLinkFlapIntfTimeInterval_Type(Unsigned32):
    """Custom type etsysLinkFlapIntfTimeInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysLinkFlapIntfTimeInterval_Type.__name__ = "Unsigned32"
_EtsysLinkFlapIntfTimeInterval_Object = MibTableColumn
etsysLinkFlapIntfTimeInterval = _EtsysLinkFlapIntfTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 6),
    _EtsysLinkFlapIntfTimeInterval_Type()
)
etsysLinkFlapIntfTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfTimeInterval.setUnits("seconds")


class _EtsysLinkFlapIntfDownTime_Type(Unsigned32):
    """Custom type etsysLinkFlapIntfDownTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysLinkFlapIntfDownTime_Type.__name__ = "Unsigned32"
_EtsysLinkFlapIntfDownTime_Object = MibTableColumn
etsysLinkFlapIntfDownTime = _EtsysLinkFlapIntfDownTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 7),
    _EtsysLinkFlapIntfDownTime_Type()
)
etsysLinkFlapIntfDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfDownTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfDownTime.setUnits("seconds")
_EtsysLinkFlapIntfLinkdownCountCurrent_Type = Gauge32
_EtsysLinkFlapIntfLinkdownCountCurrent_Object = MibTableColumn
etsysLinkFlapIntfLinkdownCountCurrent = _EtsysLinkFlapIntfLinkdownCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 8),
    _EtsysLinkFlapIntfLinkdownCountCurrent_Type()
)
etsysLinkFlapIntfLinkdownCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfLinkdownCountCurrent.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfLinkdownCountCurrent.setUnits("link state transitions")
_EtsysLinkFlapIntfLinkdownCountTotal_Type = Gauge32
_EtsysLinkFlapIntfLinkdownCountTotal_Object = MibTableColumn
etsysLinkFlapIntfLinkdownCountTotal = _EtsysLinkFlapIntfLinkdownCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 9),
    _EtsysLinkFlapIntfLinkdownCountTotal_Type()
)
etsysLinkFlapIntfLinkdownCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfLinkdownCountTotal.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfLinkdownCountTotal.setUnits("link state transitions")
_EtsysLinkFlapIntfCurrentElapsed_Type = Unsigned32
_EtsysLinkFlapIntfCurrentElapsed_Object = MibTableColumn
etsysLinkFlapIntfCurrentElapsed = _EtsysLinkFlapIntfCurrentElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 10),
    _EtsysLinkFlapIntfCurrentElapsed_Type()
)
etsysLinkFlapIntfCurrentElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfCurrentElapsed.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfCurrentElapsed.setUnits("seconds")
_EtsysLinkFlapIntfLinkFlapViolations_Type = Gauge32
_EtsysLinkFlapIntfLinkFlapViolations_Object = MibTableColumn
etsysLinkFlapIntfLinkFlapViolations = _EtsysLinkFlapIntfLinkFlapViolations_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 11),
    _EtsysLinkFlapIntfLinkFlapViolations_Type()
)
etsysLinkFlapIntfLinkFlapViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfLinkFlapViolations.setStatus("current")
if mibBuilder.loadTexts:
    etsysLinkFlapIntfLinkFlapViolations.setUnits("violations")
_EtsysLinkFlapConformance_ObjectIdentity = ObjectIdentity
etsysLinkFlapConformance = _EtsysLinkFlapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2)
)
_EtsysLinkFlapGroups_ObjectIdentity = ObjectIdentity
etsysLinkFlapGroups = _EtsysLinkFlapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1)
)
_EtsysLinkFlapCompliances_ObjectIdentity = ObjectIdentity
etsysLinkFlapCompliances = _EtsysLinkFlapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 2)
)

# Managed Objects groups

etsysLinkFlapSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1, 1)
)
etsysLinkFlapSystemGroup.setObjects(
      *(("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemState"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemSupportedActions"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemLinkFlapMaximum"))
)
if mibBuilder.loadTexts:
    etsysLinkFlapSystemGroup.setStatus("current")

etsysLinkFlapInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1, 2)
)
etsysLinkFlapInterfaceGroup.setObjects(
      *(("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfEnabledStatus"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfAction"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfOperStatus"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfClearStats"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfCountThreshold"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfTimeInterval"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfDownTime"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfLinkdownCountCurrent"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfLinkdownCountTotal"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfCurrentElapsed"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfLinkFlapViolations"))
)
if mibBuilder.loadTexts:
    etsysLinkFlapInterfaceGroup.setStatus("current")


# Notification objects

etsysLinkFlapViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 0, 1)
)
etsysLinkFlapViolation.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfOperStatus"))
)
if mibBuilder.loadTexts:
    etsysLinkFlapViolation.setStatus(
        "current"
    )


# Notifications groups

etsysLinkFlapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1, 3)
)
etsysLinkFlapNotificationGroup.setObjects(
    ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapViolation")
)
if mibBuilder.loadTexts:
    etsysLinkFlapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysLinkFlapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLinkFlapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-LINK-FLAP-MIB",
    **{"LinkFlapIntfAction": LinkFlapIntfAction,
       "etsysLinkFlapMIB": etsysLinkFlapMIB,
       "etsysLinkFlapObjects": etsysLinkFlapObjects,
       "etsysLinkFlapNotificationBranch": etsysLinkFlapNotificationBranch,
       "etsysLinkFlapViolation": etsysLinkFlapViolation,
       "etsysLinkFlapSystemBranch": etsysLinkFlapSystemBranch,
       "etsysLinkFlapSystemState": etsysLinkFlapSystemState,
       "etsysLinkFlapSystemSupportedActions": etsysLinkFlapSystemSupportedActions,
       "etsysLinkFlapSystemLinkFlapMaximum": etsysLinkFlapSystemLinkFlapMaximum,
       "etsysLinkFlapInterfaceBranch": etsysLinkFlapInterfaceBranch,
       "etsysLinkFlapInterfaceTable": etsysLinkFlapInterfaceTable,
       "etsysLinkFlapInterfaceEntry": etsysLinkFlapInterfaceEntry,
       "etsysLinkFlapIntfEnabledStatus": etsysLinkFlapIntfEnabledStatus,
       "etsysLinkFlapIntfAction": etsysLinkFlapIntfAction,
       "etsysLinkFlapIntfOperStatus": etsysLinkFlapIntfOperStatus,
       "etsysLinkFlapIntfClearStats": etsysLinkFlapIntfClearStats,
       "etsysLinkFlapIntfCountThreshold": etsysLinkFlapIntfCountThreshold,
       "etsysLinkFlapIntfTimeInterval": etsysLinkFlapIntfTimeInterval,
       "etsysLinkFlapIntfDownTime": etsysLinkFlapIntfDownTime,
       "etsysLinkFlapIntfLinkdownCountCurrent": etsysLinkFlapIntfLinkdownCountCurrent,
       "etsysLinkFlapIntfLinkdownCountTotal": etsysLinkFlapIntfLinkdownCountTotal,
       "etsysLinkFlapIntfCurrentElapsed": etsysLinkFlapIntfCurrentElapsed,
       "etsysLinkFlapIntfLinkFlapViolations": etsysLinkFlapIntfLinkFlapViolations,
       "etsysLinkFlapConformance": etsysLinkFlapConformance,
       "etsysLinkFlapGroups": etsysLinkFlapGroups,
       "etsysLinkFlapSystemGroup": etsysLinkFlapSystemGroup,
       "etsysLinkFlapInterfaceGroup": etsysLinkFlapInterfaceGroup,
       "etsysLinkFlapNotificationGroup": etsysLinkFlapNotificationGroup,
       "etsysLinkFlapCompliances": etsysLinkFlapCompliances,
       "etsysLinkFlapCompliance": etsysLinkFlapCompliance}
)
