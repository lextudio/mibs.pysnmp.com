# SNMP MIB module (TIMETRA-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:51 2024
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxEnabledDisabled,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxEnabledDisabled")


# MODULE-IDENTITY

timetraAlarmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 77)
)
timetraAlarmMIBModule.setRevisions(
        ("2011-02-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxAlarmConformance_ObjectIdentity = ObjectIdentity
tmnxAlarmConformance = _TmnxAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77)
)
_TmnxAlarmCompliances_ObjectIdentity = ObjectIdentity
tmnxAlarmCompliances = _TmnxAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1)
)
_TmnxAlarmGroups_ObjectIdentity = ObjectIdentity
tmnxAlarmGroups = _TmnxAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2)
)
_TmnxAlarmV9v0Groups_ObjectIdentity = ObjectIdentity
tmnxAlarmV9v0Groups = _TmnxAlarmV9v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1)
)
_TmnxAlarmObjs_ObjectIdentity = ObjectIdentity
tmnxAlarmObjs = _TmnxAlarmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77)
)
_TmnxAlarmConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxAlarmConfigTimeStamps = _TmnxAlarmConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 1)
)
_TmnxAlarmConfigurations_ObjectIdentity = ObjectIdentity
tmnxAlarmConfigurations = _TmnxAlarmConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2)
)
_TmnxAlarmSystemConfig_ObjectIdentity = ObjectIdentity
tmnxAlarmSystemConfig = _TmnxAlarmSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2, 1)
)


class _TmnxAlarmAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxAlarmAdminState based on TmnxEnabledDisabled"""


_TmnxAlarmAdminState_Object = MibScalar
tmnxAlarmAdminState = _TmnxAlarmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2, 1, 1),
    _TmnxAlarmAdminState_Type()
)
tmnxAlarmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxAlarmAdminState.setStatus("current")
_TmnxAlarmNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxAlarmNotifyPrefix = _TmnxAlarmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 77)
)
_TmnxAlarmNotifications_ObjectIdentity = ObjectIdentity
tmnxAlarmNotifications = _TmnxAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 77, 0)
)

# Managed Objects groups

tmnxAlarmSystemConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1, 1)
)
tmnxAlarmSystemConfigGroup.setObjects(
    ("TIMETRA-ALARM-MIB", "tmnxAlarmAdminState")
)
if mibBuilder.loadTexts:
    tmnxAlarmSystemConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ALARM-MIB",
    **{"timetraAlarmMIBModule": timetraAlarmMIBModule,
       "tmnxAlarmConformance": tmnxAlarmConformance,
       "tmnxAlarmCompliances": tmnxAlarmCompliances,
       "tmnxAlarmCompliance": tmnxAlarmCompliance,
       "tmnxAlarmGroups": tmnxAlarmGroups,
       "tmnxAlarmV9v0Groups": tmnxAlarmV9v0Groups,
       "tmnxAlarmSystemConfigGroup": tmnxAlarmSystemConfigGroup,
       "tmnxAlarmObjs": tmnxAlarmObjs,
       "tmnxAlarmConfigTimeStamps": tmnxAlarmConfigTimeStamps,
       "tmnxAlarmConfigurations": tmnxAlarmConfigurations,
       "tmnxAlarmSystemConfig": tmnxAlarmSystemConfig,
       "tmnxAlarmAdminState": tmnxAlarmAdminState,
       "tmnxAlarmNotifyPrefix": tmnxAlarmNotifyPrefix,
       "tmnxAlarmNotifications": tmnxAlarmNotifications}
)
