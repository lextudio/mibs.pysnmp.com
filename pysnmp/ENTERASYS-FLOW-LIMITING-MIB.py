# SNMP MIB module (ENTERASYS-FLOW-LIMITING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-FLOW-LIMITING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:53 2024
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

etsysFlowLimitingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43)
)
etsysFlowLimitingMIB.setRevisions(
        ("2004-07-26 19:16",
         "2004-02-05 14:49",
         "2004-01-27 18:56",
         "2003-11-20 18:34")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FlowLmtIntfClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aggregatedUserPort", 3),
          ("interSwitchLink", 4),
          ("serverPort", 2),
          ("unspecified", 5),
          ("userPort", 1))
    )



class FlowLmtIntfAction(Bits, TextualConvention):
    status = "current"


class FlowLmtIntfLayer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l2", 2),
          ("l3", 3),
          ("l4", 4),
          ("none", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysFlowLimitingObjects_ObjectIdentity = ObjectIdentity
etsysFlowLimitingObjects = _EtsysFlowLimitingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1)
)
_EtsysFlowLimitingNotificationBranch_ObjectIdentity = ObjectIdentity
etsysFlowLimitingNotificationBranch = _EtsysFlowLimitingNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0)
)
_EtsysFlowLimitingSystemBranch_ObjectIdentity = ObjectIdentity
etsysFlowLimitingSystemBranch = _EtsysFlowLimitingSystemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1)
)


class _EtsysFlowLimitingSystemState_Type(EnabledStatus):
    """Custom type etsysFlowLimitingSystemState based on EnabledStatus"""


_EtsysFlowLimitingSystemState_Object = MibScalar
etsysFlowLimitingSystemState = _EtsysFlowLimitingSystemState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 1),
    _EtsysFlowLimitingSystemState_Type()
)
etsysFlowLimitingSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemState.setStatus("current")


class _EtsysFlowLimitingSystemSnmpNotifications_Type(EnabledStatus):
    """Custom type etsysFlowLimitingSystemSnmpNotifications based on EnabledStatus"""


_EtsysFlowLimitingSystemSnmpNotifications_Object = MibScalar
etsysFlowLimitingSystemSnmpNotifications = _EtsysFlowLimitingSystemSnmpNotifications_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 2),
    _EtsysFlowLimitingSystemSnmpNotifications_Type()
)
etsysFlowLimitingSystemSnmpNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemSnmpNotifications.setStatus("current")


class _EtsysFlowLimitingSystemInterfaceShutdown_Type(EnabledStatus):
    """Custom type etsysFlowLimitingSystemInterfaceShutdown based on EnabledStatus"""


_EtsysFlowLimitingSystemInterfaceShutdown_Object = MibScalar
etsysFlowLimitingSystemInterfaceShutdown = _EtsysFlowLimitingSystemInterfaceShutdown_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 3),
    _EtsysFlowLimitingSystemInterfaceShutdown_Type()
)
etsysFlowLimitingSystemInterfaceShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemInterfaceShutdown.setStatus("current")


class _EtsysFlowLimitingSystemNotificationInterval_Type(Unsigned32):
    """Custom type etsysFlowLimitingSystemNotificationInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingSystemNotificationInterval_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingSystemNotificationInterval_Object = MibScalar
etsysFlowLimitingSystemNotificationInterval = _EtsysFlowLimitingSystemNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 4),
    _EtsysFlowLimitingSystemNotificationInterval_Type()
)
etsysFlowLimitingSystemNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemNotificationInterval.setUnits("seconds")
_EtsysFlowLimitingSystemClearStats_Type = TruthValue
_EtsysFlowLimitingSystemClearStats_Object = MibScalar
etsysFlowLimitingSystemClearStats = _EtsysFlowLimitingSystemClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 5),
    _EtsysFlowLimitingSystemClearStats_Type()
)
etsysFlowLimitingSystemClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemClearStats.setStatus("current")


class _EtsysFlowLimitingSystemMaxSupportedFlowCount_Type(Unsigned32):
    """Custom type etsysFlowLimitingSystemMaxSupportedFlowCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingSystemMaxSupportedFlowCount_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingSystemMaxSupportedFlowCount_Object = MibScalar
etsysFlowLimitingSystemMaxSupportedFlowCount = _EtsysFlowLimitingSystemMaxSupportedFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 6),
    _EtsysFlowLimitingSystemMaxSupportedFlowCount_Type()
)
etsysFlowLimitingSystemMaxSupportedFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemMaxSupportedFlowCount.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemMaxSupportedFlowCount.setUnits("flows")


class _EtsysFlowLimitingSystemMaxSupportedSetupRate_Type(Unsigned32):
    """Custom type etsysFlowLimitingSystemMaxSupportedSetupRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingSystemMaxSupportedSetupRate_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingSystemMaxSupportedSetupRate_Object = MibScalar
etsysFlowLimitingSystemMaxSupportedSetupRate = _EtsysFlowLimitingSystemMaxSupportedSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 1, 7),
    _EtsysFlowLimitingSystemMaxSupportedSetupRate_Type()
)
etsysFlowLimitingSystemMaxSupportedSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemMaxSupportedSetupRate.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemMaxSupportedSetupRate.setUnits("flows/second")
_EtsysFlowLimitingClassBranch_ObjectIdentity = ObjectIdentity
etsysFlowLimitingClassBranch = _EtsysFlowLimitingClassBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2)
)
_EtsysFlowLimitingClassTable_Object = MibTable
etsysFlowLimitingClassTable = _EtsysFlowLimitingClassTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysFlowLimitingClassTable.setStatus("current")
_EtsysFlowLimitingClassEntry_Object = MibTableRow
etsysFlowLimitingClassEntry = _EtsysFlowLimitingClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1)
)
etsysFlowLimitingClassEntry.setIndexNames(
    (0, "ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassType"),
)
if mibBuilder.loadTexts:
    etsysFlowLimitingClassEntry.setStatus("current")
_EtsysFlowLimitingClassType_Type = FlowLmtIntfClass
_EtsysFlowLimitingClassType_Object = MibTableColumn
etsysFlowLimitingClassType = _EtsysFlowLimitingClassType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 1),
    _EtsysFlowLimitingClassType_Type()
)
etsysFlowLimitingClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassType.setStatus("current")


class _EtsysFlowLimitingClassFlowCountActionLimit1_Type(Unsigned32):
    """Custom type etsysFlowLimitingClassFlowCountActionLimit1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingClassFlowCountActionLimit1_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingClassFlowCountActionLimit1_Object = MibTableColumn
etsysFlowLimitingClassFlowCountActionLimit1 = _EtsysFlowLimitingClassFlowCountActionLimit1_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 2),
    _EtsysFlowLimitingClassFlowCountActionLimit1_Type()
)
etsysFlowLimitingClassFlowCountActionLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassFlowCountActionLimit1.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassFlowCountActionLimit1.setUnits("flows")
_EtsysFlowLimitingClassFlowCountActionTaken1_Type = FlowLmtIntfAction
_EtsysFlowLimitingClassFlowCountActionTaken1_Object = MibTableColumn
etsysFlowLimitingClassFlowCountActionTaken1 = _EtsysFlowLimitingClassFlowCountActionTaken1_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 3),
    _EtsysFlowLimitingClassFlowCountActionTaken1_Type()
)
etsysFlowLimitingClassFlowCountActionTaken1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassFlowCountActionTaken1.setStatus("current")


class _EtsysFlowLimitingClassFlowCountActionLimit2_Type(Unsigned32):
    """Custom type etsysFlowLimitingClassFlowCountActionLimit2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingClassFlowCountActionLimit2_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingClassFlowCountActionLimit2_Object = MibTableColumn
etsysFlowLimitingClassFlowCountActionLimit2 = _EtsysFlowLimitingClassFlowCountActionLimit2_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 4),
    _EtsysFlowLimitingClassFlowCountActionLimit2_Type()
)
etsysFlowLimitingClassFlowCountActionLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassFlowCountActionLimit2.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassFlowCountActionLimit2.setUnits("flows")
_EtsysFlowLimitingClassFlowCountActionTaken2_Type = FlowLmtIntfAction
_EtsysFlowLimitingClassFlowCountActionTaken2_Object = MibTableColumn
etsysFlowLimitingClassFlowCountActionTaken2 = _EtsysFlowLimitingClassFlowCountActionTaken2_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 5),
    _EtsysFlowLimitingClassFlowCountActionTaken2_Type()
)
etsysFlowLimitingClassFlowCountActionTaken2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassFlowCountActionTaken2.setStatus("current")


class _EtsysFlowLimitingClassSetupRateNotifyLimit_Type(Unsigned32):
    """Custom type etsysFlowLimitingClassSetupRateNotifyLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingClassSetupRateNotifyLimit_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingClassSetupRateNotifyLimit_Object = MibTableColumn
etsysFlowLimitingClassSetupRateNotifyLimit = _EtsysFlowLimitingClassSetupRateNotifyLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 6),
    _EtsysFlowLimitingClassSetupRateNotifyLimit_Type()
)
etsysFlowLimitingClassSetupRateNotifyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassSetupRateNotifyLimit.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassSetupRateNotifyLimit.setUnits("flows/second")


class _EtsysFlowLimitingClassSetupRateActionLimit_Type(Unsigned32):
    """Custom type etsysFlowLimitingClassSetupRateActionLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFlowLimitingClassSetupRateActionLimit_Type.__name__ = "Unsigned32"
_EtsysFlowLimitingClassSetupRateActionLimit_Object = MibTableColumn
etsysFlowLimitingClassSetupRateActionLimit = _EtsysFlowLimitingClassSetupRateActionLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 7),
    _EtsysFlowLimitingClassSetupRateActionLimit_Type()
)
etsysFlowLimitingClassSetupRateActionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassSetupRateActionLimit.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassSetupRateActionLimit.setUnits("flows/second")
_EtsysFlowLimitingClassSetupRateActionTaken_Type = FlowLmtIntfAction
_EtsysFlowLimitingClassSetupRateActionTaken_Object = MibTableColumn
etsysFlowLimitingClassSetupRateActionTaken = _EtsysFlowLimitingClassSetupRateActionTaken_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 2, 1, 1, 8),
    _EtsysFlowLimitingClassSetupRateActionTaken_Type()
)
etsysFlowLimitingClassSetupRateActionTaken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingClassSetupRateActionTaken.setStatus("current")
_EtsysFlowLimitingInterfaceBranch_ObjectIdentity = ObjectIdentity
etsysFlowLimitingInterfaceBranch = _EtsysFlowLimitingInterfaceBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3)
)
_EtsysFlowLimitingInterfaceTable_Object = MibTable
etsysFlowLimitingInterfaceTable = _EtsysFlowLimitingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysFlowLimitingInterfaceTable.setStatus("current")
_EtsysFlowLimitingInterfaceEntry_Object = MibTableRow
etsysFlowLimitingInterfaceEntry = _EtsysFlowLimitingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1)
)
etsysFlowLimitingInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysFlowLimitingInterfaceEntry.setStatus("current")


class _EtsysFlowLimitingIntfClassType_Type(FlowLmtIntfClass):
    """Custom type etsysFlowLimitingIntfClassType based on FlowLmtIntfClass"""


_EtsysFlowLimitingIntfClassType_Object = MibTableColumn
etsysFlowLimitingIntfClassType = _EtsysFlowLimitingIntfClassType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 1),
    _EtsysFlowLimitingIntfClassType_Type()
)
etsysFlowLimitingIntfClassType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfClassType.setStatus("current")


class _EtsysFlowLimitingIntfFlowLimitingState_Type(EnabledStatus):
    """Custom type etsysFlowLimitingIntfFlowLimitingState based on EnabledStatus"""


_EtsysFlowLimitingIntfFlowLimitingState_Object = MibTableColumn
etsysFlowLimitingIntfFlowLimitingState = _EtsysFlowLimitingIntfFlowLimitingState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 2),
    _EtsysFlowLimitingIntfFlowLimitingState_Type()
)
etsysFlowLimitingIntfFlowLimitingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowLimitingState.setStatus("current")


class _EtsysFlowLimitingIntfStatus_Type(Integer32):
    """Custom type etsysFlowLimitingIntfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("creatingDiscardFlows", 4),
          ("disabled", 2),
          ("droppingExcessFlows", 3),
          ("operational", 1))
    )


_EtsysFlowLimitingIntfStatus_Type.__name__ = "Integer32"
_EtsysFlowLimitingIntfStatus_Object = MibTableColumn
etsysFlowLimitingIntfStatus = _EtsysFlowLimitingIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 3),
    _EtsysFlowLimitingIntfStatus_Type()
)
etsysFlowLimitingIntfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfStatus.setStatus("current")


class _EtsysFlowLimitingIntfReason_Type(Integer32):
    """Custom type etsysFlowLimitingIntfReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flowCount", 2),
          ("noAction", 1),
          ("setupRate", 3))
    )


_EtsysFlowLimitingIntfReason_Type.__name__ = "Integer32"
_EtsysFlowLimitingIntfReason_Object = MibTableColumn
etsysFlowLimitingIntfReason = _EtsysFlowLimitingIntfReason_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 4),
    _EtsysFlowLimitingIntfReason_Type()
)
etsysFlowLimitingIntfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfReason.setStatus("current")
_EtsysFlowLimitingIntfClearStats_Type = TruthValue
_EtsysFlowLimitingIntfClearStats_Object = MibTableColumn
etsysFlowLimitingIntfClearStats = _EtsysFlowLimitingIntfClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 5),
    _EtsysFlowLimitingIntfClearStats_Type()
)
etsysFlowLimitingIntfClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfClearStats.setStatus("current")
_EtsysFlowLimitingIntfFlowCountCurrent_Type = Gauge32
_EtsysFlowLimitingIntfFlowCountCurrent_Object = MibTableColumn
etsysFlowLimitingIntfFlowCountCurrent = _EtsysFlowLimitingIntfFlowCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 6),
    _EtsysFlowLimitingIntfFlowCountCurrent_Type()
)
etsysFlowLimitingIntfFlowCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowCountCurrent.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowCountCurrent.setUnits("flows")
_EtsysFlowLimitingIntfFlowCountMax_Type = Gauge32
_EtsysFlowLimitingIntfFlowCountMax_Object = MibTableColumn
etsysFlowLimitingIntfFlowCountMax = _EtsysFlowLimitingIntfFlowCountMax_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 7),
    _EtsysFlowLimitingIntfFlowCountMax_Type()
)
etsysFlowLimitingIntfFlowCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowCountMax.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowCountMax.setUnits("flows")
_EtsysFlowLimitingIntfFlowCountMaxTime_Type = TimeTicks
_EtsysFlowLimitingIntfFlowCountMaxTime_Object = MibTableColumn
etsysFlowLimitingIntfFlowCountMaxTime = _EtsysFlowLimitingIntfFlowCountMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 8),
    _EtsysFlowLimitingIntfFlowCountMaxTime_Type()
)
etsysFlowLimitingIntfFlowCountMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowCountMaxTime.setStatus("current")
_EtsysFlowLimitingIntfFlowCountEvents_Type = Gauge32
_EtsysFlowLimitingIntfFlowCountEvents_Object = MibTableColumn
etsysFlowLimitingIntfFlowCountEvents = _EtsysFlowLimitingIntfFlowCountEvents_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 9),
    _EtsysFlowLimitingIntfFlowCountEvents_Type()
)
etsysFlowLimitingIntfFlowCountEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowCountEvents.setStatus("current")
_EtsysFlowLimitingIntfSetupRateCurrent_Type = Gauge32
_EtsysFlowLimitingIntfSetupRateCurrent_Object = MibTableColumn
etsysFlowLimitingIntfSetupRateCurrent = _EtsysFlowLimitingIntfSetupRateCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 10),
    _EtsysFlowLimitingIntfSetupRateCurrent_Type()
)
etsysFlowLimitingIntfSetupRateCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfSetupRateCurrent.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfSetupRateCurrent.setUnits("flows/second")
_EtsysFlowLimitingIntfSetupRateMax_Type = Gauge32
_EtsysFlowLimitingIntfSetupRateMax_Object = MibTableColumn
etsysFlowLimitingIntfSetupRateMax = _EtsysFlowLimitingIntfSetupRateMax_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 11),
    _EtsysFlowLimitingIntfSetupRateMax_Type()
)
etsysFlowLimitingIntfSetupRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfSetupRateMax.setStatus("current")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfSetupRateMax.setUnits("flows/second")
_EtsysFlowLimitingIntfSetupRateMaxTime_Type = TimeTicks
_EtsysFlowLimitingIntfSetupRateMaxTime_Object = MibTableColumn
etsysFlowLimitingIntfSetupRateMaxTime = _EtsysFlowLimitingIntfSetupRateMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 12),
    _EtsysFlowLimitingIntfSetupRateMaxTime_Type()
)
etsysFlowLimitingIntfSetupRateMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfSetupRateMaxTime.setStatus("current")
_EtsysFlowLimitingIntfSetupRateEvents_Type = Gauge32
_EtsysFlowLimitingIntfSetupRateEvents_Object = MibTableColumn
etsysFlowLimitingIntfSetupRateEvents = _EtsysFlowLimitingIntfSetupRateEvents_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 13),
    _EtsysFlowLimitingIntfSetupRateEvents_Type()
)
etsysFlowLimitingIntfSetupRateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfSetupRateEvents.setStatus("current")
_EtsysFlowLimitingIntfFlowProcessingLayer_Type = FlowLmtIntfLayer
_EtsysFlowLimitingIntfFlowProcessingLayer_Object = MibTableColumn
etsysFlowLimitingIntfFlowProcessingLayer = _EtsysFlowLimitingIntfFlowProcessingLayer_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 3, 1, 1, 14),
    _EtsysFlowLimitingIntfFlowProcessingLayer_Type()
)
etsysFlowLimitingIntfFlowProcessingLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFlowLimitingIntfFlowProcessingLayer.setStatus("current")
_EtsysFlowLimitingConformance_ObjectIdentity = ObjectIdentity
etsysFlowLimitingConformance = _EtsysFlowLimitingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2)
)
_EtsysFlowLimitingGroups_ObjectIdentity = ObjectIdentity
etsysFlowLimitingGroups = _EtsysFlowLimitingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1)
)
_EtsysFlowLimitingCompliances_ObjectIdentity = ObjectIdentity
etsysFlowLimitingCompliances = _EtsysFlowLimitingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 2)
)

# Managed Objects groups

etsysFlowLimitingSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 1)
)
etsysFlowLimitingSystemGroup.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemState"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemSnmpNotifications"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemInterfaceShutdown"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemNotificationInterval"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemClearStats"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemMaxSupportedFlowCount"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSystemMaxSupportedSetupRate"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSystemGroup.setStatus("current")

etsysFlowLimitingInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 2)
)
etsysFlowLimitingInterfaceGroup.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfClassType"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowLimitingState"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfReason"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfClearStats"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingInterfaceGroup.setStatus("deprecated")

etsysFlowLimitingFlowCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 3)
)
etsysFlowLimitingFlowCountGroup.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassFlowCountActionLimit1"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassFlowCountActionTaken1"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassFlowCountActionLimit2"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassFlowCountActionTaken2"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountMax"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountMaxTime"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountCurrent"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountEvents"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingFlowCountGroup.setStatus("current")

etsysFlowLimitingSetupRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 4)
)
etsysFlowLimitingSetupRateGroup.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassSetupRateNotifyLimit"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassSetupRateActionLimit"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingClassSetupRateActionTaken"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateMax"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateMaxTime"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateCurrent"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateEvents"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateGroup.setStatus("current")

etsysFlowLimitingInterfaceGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 7)
)
etsysFlowLimitingInterfaceGroupV2.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfClassType"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowLimitingState"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfReason"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfClearStats"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowProcessingLayer"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingInterfaceGroupV2.setStatus("current")


# Notification objects

etsysFlowlimitingFlowCountActionLimit1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 1)
)
etsysFlowlimitingFlowCountActionLimit1.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowlimitingFlowCountActionLimit1.setStatus(
        "deprecated"
    )

etsysFlowlimitingFlowCountActionLimit2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 2)
)
etsysFlowlimitingFlowCountActionLimit2.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowlimitingFlowCountActionLimit2.setStatus(
        "deprecated"
    )

etsysFlowLimitingSetupRateNotifyLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 3)
)
etsysFlowLimitingSetupRateNotifyLimit.setObjects(
    ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateCurrent")
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateNotifyLimit.setStatus(
        "deprecated"
    )

etsysFlowLimitingSetupRateActionLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 4)
)
etsysFlowLimitingSetupRateActionLimit.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateActionLimit.setStatus(
        "deprecated"
    )

etsysFlowlimitingFlowCountActionLimit1V2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 5)
)
etsysFlowlimitingFlowCountActionLimit1V2.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowlimitingFlowCountActionLimit1V2.setStatus(
        "current"
    )

etsysFlowlimitingFlowCountActionLimit2V2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 6)
)
etsysFlowlimitingFlowCountActionLimit2V2.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfFlowCountCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowlimitingFlowCountActionLimit2V2.setStatus(
        "current"
    )

etsysFlowLimitingSetupRateNotifyLimitV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 7)
)
etsysFlowLimitingSetupRateNotifyLimitV2.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateNotifyLimitV2.setStatus(
        "current"
    )

etsysFlowLimitingSetupRateActionLimitV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 1, 0, 8)
)
etsysFlowLimitingSetupRateActionLimitV2.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfStatus"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingIntfSetupRateCurrent"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateActionLimitV2.setStatus(
        "current"
    )


# Notifications groups

etsysFlowLimitingFlowCountNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 5)
)
etsysFlowLimitingFlowCountNotificationGroup.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowlimitingFlowCountActionLimit1"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowlimitingFlowCountActionLimit2"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingFlowCountNotificationGroup.setStatus(
        "deprecated"
    )

etsysFlowLimitingSetupRateNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 6)
)
etsysFlowLimitingSetupRateNotificationGroup.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSetupRateNotifyLimit"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSetupRateActionLimit"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateNotificationGroup.setStatus(
        "deprecated"
    )

etsysFlowLimitingFlowCountNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 8)
)
etsysFlowLimitingFlowCountNotificationGroupV2.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowlimitingFlowCountActionLimit1V2"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowlimitingFlowCountActionLimit2V2"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingFlowCountNotificationGroupV2.setStatus(
        "current"
    )

etsysFlowLimitingSetupRateNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 1, 9)
)
etsysFlowLimitingSetupRateNotificationGroupV2.setObjects(
      *(("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSetupRateNotifyLimitV2"),
        ("ENTERASYS-FLOW-LIMITING-MIB", "etsysFlowLimitingSetupRateActionLimitV2"))
)
if mibBuilder.loadTexts:
    etsysFlowLimitingSetupRateNotificationGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysFlowLimitingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysFlowLimitingCompliance.setStatus(
        "deprecated"
    )

etsysFlowLimitingComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysFlowLimitingComplianceV2.setStatus(
        "deprecated"
    )

etsysFlowLimitingComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 43, 2, 2, 3)
)
if mibBuilder.loadTexts:
    etsysFlowLimitingComplianceV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-FLOW-LIMITING-MIB",
    **{"FlowLmtIntfClass": FlowLmtIntfClass,
       "FlowLmtIntfAction": FlowLmtIntfAction,
       "FlowLmtIntfLayer": FlowLmtIntfLayer,
       "etsysFlowLimitingMIB": etsysFlowLimitingMIB,
       "etsysFlowLimitingObjects": etsysFlowLimitingObjects,
       "etsysFlowLimitingNotificationBranch": etsysFlowLimitingNotificationBranch,
       "etsysFlowlimitingFlowCountActionLimit1": etsysFlowlimitingFlowCountActionLimit1,
       "etsysFlowlimitingFlowCountActionLimit2": etsysFlowlimitingFlowCountActionLimit2,
       "etsysFlowLimitingSetupRateNotifyLimit": etsysFlowLimitingSetupRateNotifyLimit,
       "etsysFlowLimitingSetupRateActionLimit": etsysFlowLimitingSetupRateActionLimit,
       "etsysFlowlimitingFlowCountActionLimit1V2": etsysFlowlimitingFlowCountActionLimit1V2,
       "etsysFlowlimitingFlowCountActionLimit2V2": etsysFlowlimitingFlowCountActionLimit2V2,
       "etsysFlowLimitingSetupRateNotifyLimitV2": etsysFlowLimitingSetupRateNotifyLimitV2,
       "etsysFlowLimitingSetupRateActionLimitV2": etsysFlowLimitingSetupRateActionLimitV2,
       "etsysFlowLimitingSystemBranch": etsysFlowLimitingSystemBranch,
       "etsysFlowLimitingSystemState": etsysFlowLimitingSystemState,
       "etsysFlowLimitingSystemSnmpNotifications": etsysFlowLimitingSystemSnmpNotifications,
       "etsysFlowLimitingSystemInterfaceShutdown": etsysFlowLimitingSystemInterfaceShutdown,
       "etsysFlowLimitingSystemNotificationInterval": etsysFlowLimitingSystemNotificationInterval,
       "etsysFlowLimitingSystemClearStats": etsysFlowLimitingSystemClearStats,
       "etsysFlowLimitingSystemMaxSupportedFlowCount": etsysFlowLimitingSystemMaxSupportedFlowCount,
       "etsysFlowLimitingSystemMaxSupportedSetupRate": etsysFlowLimitingSystemMaxSupportedSetupRate,
       "etsysFlowLimitingClassBranch": etsysFlowLimitingClassBranch,
       "etsysFlowLimitingClassTable": etsysFlowLimitingClassTable,
       "etsysFlowLimitingClassEntry": etsysFlowLimitingClassEntry,
       "etsysFlowLimitingClassType": etsysFlowLimitingClassType,
       "etsysFlowLimitingClassFlowCountActionLimit1": etsysFlowLimitingClassFlowCountActionLimit1,
       "etsysFlowLimitingClassFlowCountActionTaken1": etsysFlowLimitingClassFlowCountActionTaken1,
       "etsysFlowLimitingClassFlowCountActionLimit2": etsysFlowLimitingClassFlowCountActionLimit2,
       "etsysFlowLimitingClassFlowCountActionTaken2": etsysFlowLimitingClassFlowCountActionTaken2,
       "etsysFlowLimitingClassSetupRateNotifyLimit": etsysFlowLimitingClassSetupRateNotifyLimit,
       "etsysFlowLimitingClassSetupRateActionLimit": etsysFlowLimitingClassSetupRateActionLimit,
       "etsysFlowLimitingClassSetupRateActionTaken": etsysFlowLimitingClassSetupRateActionTaken,
       "etsysFlowLimitingInterfaceBranch": etsysFlowLimitingInterfaceBranch,
       "etsysFlowLimitingInterfaceTable": etsysFlowLimitingInterfaceTable,
       "etsysFlowLimitingInterfaceEntry": etsysFlowLimitingInterfaceEntry,
       "etsysFlowLimitingIntfClassType": etsysFlowLimitingIntfClassType,
       "etsysFlowLimitingIntfFlowLimitingState": etsysFlowLimitingIntfFlowLimitingState,
       "etsysFlowLimitingIntfStatus": etsysFlowLimitingIntfStatus,
       "etsysFlowLimitingIntfReason": etsysFlowLimitingIntfReason,
       "etsysFlowLimitingIntfClearStats": etsysFlowLimitingIntfClearStats,
       "etsysFlowLimitingIntfFlowCountCurrent": etsysFlowLimitingIntfFlowCountCurrent,
       "etsysFlowLimitingIntfFlowCountMax": etsysFlowLimitingIntfFlowCountMax,
       "etsysFlowLimitingIntfFlowCountMaxTime": etsysFlowLimitingIntfFlowCountMaxTime,
       "etsysFlowLimitingIntfFlowCountEvents": etsysFlowLimitingIntfFlowCountEvents,
       "etsysFlowLimitingIntfSetupRateCurrent": etsysFlowLimitingIntfSetupRateCurrent,
       "etsysFlowLimitingIntfSetupRateMax": etsysFlowLimitingIntfSetupRateMax,
       "etsysFlowLimitingIntfSetupRateMaxTime": etsysFlowLimitingIntfSetupRateMaxTime,
       "etsysFlowLimitingIntfSetupRateEvents": etsysFlowLimitingIntfSetupRateEvents,
       "etsysFlowLimitingIntfFlowProcessingLayer": etsysFlowLimitingIntfFlowProcessingLayer,
       "etsysFlowLimitingConformance": etsysFlowLimitingConformance,
       "etsysFlowLimitingGroups": etsysFlowLimitingGroups,
       "etsysFlowLimitingSystemGroup": etsysFlowLimitingSystemGroup,
       "etsysFlowLimitingInterfaceGroup": etsysFlowLimitingInterfaceGroup,
       "etsysFlowLimitingFlowCountGroup": etsysFlowLimitingFlowCountGroup,
       "etsysFlowLimitingSetupRateGroup": etsysFlowLimitingSetupRateGroup,
       "etsysFlowLimitingFlowCountNotificationGroup": etsysFlowLimitingFlowCountNotificationGroup,
       "etsysFlowLimitingSetupRateNotificationGroup": etsysFlowLimitingSetupRateNotificationGroup,
       "etsysFlowLimitingInterfaceGroupV2": etsysFlowLimitingInterfaceGroupV2,
       "etsysFlowLimitingFlowCountNotificationGroupV2": etsysFlowLimitingFlowCountNotificationGroupV2,
       "etsysFlowLimitingSetupRateNotificationGroupV2": etsysFlowLimitingSetupRateNotificationGroupV2,
       "etsysFlowLimitingCompliances": etsysFlowLimitingCompliances,
       "etsysFlowLimitingCompliance": etsysFlowLimitingCompliance,
       "etsysFlowLimitingComplianceV2": etsysFlowLimitingComplianceV2,
       "etsysFlowLimitingComplianceV3": etsysFlowLimitingComplianceV3}
)
