# SNMP MIB module (TIMETRA-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:52 2024
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

(apsChanConfigEntry,
 apsCommandEntry,
 apsCommandSwitch,
 apsConfigEntry,
 apsStatusCurrent,
 apsStatusK1K2Rcv,
 apsStatusK1K2Trans,
 apsStatusSwitchedChannel) = mibBuilder.importSymbols(
    "APS-MIB",
    "apsChanConfigEntry",
    "apsCommandEntry",
    "apsCommandSwitch",
    "apsConfigEntry",
    "apsStatusCurrent",
    "apsStatusK1K2Rcv",
    "apsStatusK1K2Trans",
    "apsStatusSwitchedChannel")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

timetraAPSMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 29)
)
timetraAPSMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1906-03-23 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-10-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TApsMIBConformance_ObjectIdentity = ObjectIdentity
tApsMIBConformance = _TApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29)
)
_TmnxApsMIBCompliances_ObjectIdentity = ObjectIdentity
tmnxApsMIBCompliances = _TmnxApsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1)
)
_TmnxApsMIBGroups_ObjectIdentity = ObjectIdentity
tmnxApsMIBGroups = _TmnxApsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2)
)
_TApsMIBObjs_ObjectIdentity = ObjectIdentity
tApsMIBObjs = _TApsMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29)
)
_TApsCommandTable_Object = MibTable
tApsCommandTable = _TApsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 1)
)
if mibBuilder.loadTexts:
    tApsCommandTable.setStatus("current")
_TApsCommandEntry_Object = MibTableRow
tApsCommandEntry = _TApsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 1, 1)
)
if mibBuilder.loadTexts:
    tApsCommandEntry.setStatus("current")


class _TApsExerciseCommandResult_Type(Integer32):
    """Custom type tApsExerciseCommandResult based on Integer32"""
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
        *(("failed", 2),
          ("passed", 1),
          ("preempted", 3),
          ("unknown", 4))
    )


_TApsExerciseCommandResult_Type.__name__ = "Integer32"
_TApsExerciseCommandResult_Object = MibTableColumn
tApsExerciseCommandResult = _TApsExerciseCommandResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 1, 1, 1),
    _TApsExerciseCommandResult_Type()
)
tApsExerciseCommandResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tApsExerciseCommandResult.setStatus("current")
_TApsChanStatusTable_Object = MibTable
tApsChanStatusTable = _TApsChanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 2)
)
if mibBuilder.loadTexts:
    tApsChanStatusTable.setStatus("current")
_TApsChanStatusEntry_Object = MibTableRow
tApsChanStatusEntry = _TApsChanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 2, 1)
)
if mibBuilder.loadTexts:
    tApsChanStatusEntry.setStatus("current")


class _TApsChanTxLaisState_Type(Integer32):
    """Custom type tApsChanTxLaisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("momentary", 1),
          ("persistent", 2))
    )


_TApsChanTxLaisState_Type.__name__ = "Integer32"
_TApsChanTxLaisState_Object = MibTableColumn
tApsChanTxLaisState = _TApsChanTxLaisState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 2, 1, 1),
    _TApsChanTxLaisState_Type()
)
tApsChanTxLaisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tApsChanTxLaisState.setStatus("current")
_TApsMcConfigTable_Object = MibTable
tApsMcConfigTable = _TApsMcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3)
)
if mibBuilder.loadTexts:
    tApsMcConfigTable.setStatus("current")
_TApsMcConfigEntry_Object = MibTableRow
tApsMcConfigEntry = _TApsMcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1)
)
if mibBuilder.loadTexts:
    tApsMcConfigEntry.setStatus("current")
_TApsMcNeighborAddrType_Type = InetAddressType
_TApsMcNeighborAddrType_Object = MibTableColumn
tApsMcNeighborAddrType = _TApsMcNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 1),
    _TApsMcNeighborAddrType_Type()
)
tApsMcNeighborAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsMcNeighborAddrType.setStatus("current")


class _TApsMcNeighborAddr_Type(InetAddress):
    """Custom type tApsMcNeighborAddr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_TApsMcNeighborAddr_Type.__name__ = "InetAddress"
_TApsMcNeighborAddr_Object = MibTableColumn
tApsMcNeighborAddr = _TApsMcNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 2),
    _TApsMcNeighborAddr_Type()
)
tApsMcNeighborAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsMcNeighborAddr.setStatus("current")


class _TApsMcAdvertiseInterval_Type(Unsigned32):
    """Custom type tApsMcAdvertiseInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 650),
    )


_TApsMcAdvertiseInterval_Type.__name__ = "Unsigned32"
_TApsMcAdvertiseInterval_Object = MibTableColumn
tApsMcAdvertiseInterval = _TApsMcAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 3),
    _TApsMcAdvertiseInterval_Type()
)
tApsMcAdvertiseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsMcAdvertiseInterval.setStatus("current")
if mibBuilder.loadTexts:
    tApsMcAdvertiseInterval.setUnits("100s of milliseconds")


class _TApsMcHoldTime_Type(Unsigned32):
    """Custom type tApsMcHoldTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 650),
    )


_TApsMcHoldTime_Type.__name__ = "Unsigned32"
_TApsMcHoldTime_Object = MibTableColumn
tApsMcHoldTime = _TApsMcHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 4),
    _TApsMcHoldTime_Type()
)
tApsMcHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsMcHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tApsMcHoldTime.setUnits("100s of milliseconds")
_TApsMcStatusTable_Object = MibTable
tApsMcStatusTable = _TApsMcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 4)
)
if mibBuilder.loadTexts:
    tApsMcStatusTable.setStatus("current")
_TApsMcStatusEntry_Object = MibTableRow
tApsMcStatusEntry = _TApsMcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 4, 1)
)
if mibBuilder.loadTexts:
    tApsMcStatusEntry.setStatus("current")


class _TApsMcApsCtlLinkState_Type(Integer32):
    """Custom type tApsMcApsCtlLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnIncompatibleNbr", 2),
          ("dnSignalingFailure", 1),
          ("up", 0))
    )


_TApsMcApsCtlLinkState_Type.__name__ = "Integer32"
_TApsMcApsCtlLinkState_Object = MibTableColumn
tApsMcApsCtlLinkState = _TApsMcApsCtlLinkState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 4, 1, 1),
    _TApsMcApsCtlLinkState_Type()
)
tApsMcApsCtlLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tApsMcApsCtlLinkState.setStatus("current")
_TApsConfigTable_Object = MibTable
tApsConfigTable = _TApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5)
)
if mibBuilder.loadTexts:
    tApsConfigTable.setStatus("current")
_TApsConfigEntry_Object = MibTableRow
tApsConfigEntry = _TApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1)
)
if mibBuilder.loadTexts:
    tApsConfigEntry.setStatus("current")


class _TApsProtectionType_Type(Integer32):
    """Custom type tApsProtectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 2),
          ("onePlusOneSignalling", 1))
    )


_TApsProtectionType_Type.__name__ = "Integer32"
_TApsProtectionType_Object = MibTableColumn
tApsProtectionType = _TApsProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 1),
    _TApsProtectionType_Type()
)
tApsProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsProtectionType.setStatus("current")


class _TApsLineSFHoldTime_Type(Unsigned32):
    """Custom type tApsLineSFHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TApsLineSFHoldTime_Type.__name__ = "Unsigned32"
_TApsLineSFHoldTime_Object = MibTableColumn
tApsLineSFHoldTime = _TApsLineSFHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 2),
    _TApsLineSFHoldTime_Type()
)
tApsLineSFHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsLineSFHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tApsLineSFHoldTime.setUnits("100s of milliseconds")


class _TApsLineSDHoldTime_Type(Unsigned32):
    """Custom type tApsLineSDHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TApsLineSDHoldTime_Type.__name__ = "Unsigned32"
_TApsLineSDHoldTime_Object = MibTableColumn
tApsLineSDHoldTime = _TApsLineSDHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 3),
    _TApsLineSDHoldTime_Type()
)
tApsLineSDHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsLineSDHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tApsLineSDHoldTime.setUnits("100s of milliseconds")


class _TApsRdiAlarmGeneration_Type(Integer32):
    """Custom type tApsRdiAlarmGeneration based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("suppress", 0))
    )


_TApsRdiAlarmGeneration_Type.__name__ = "Integer32"
_TApsRdiAlarmGeneration_Object = MibTableColumn
tApsRdiAlarmGeneration = _TApsRdiAlarmGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 4),
    _TApsRdiAlarmGeneration_Type()
)
tApsRdiAlarmGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsRdiAlarmGeneration.setStatus("current")
_TApsGroupCommandTable_Object = MibTable
tApsGroupCommandTable = _TApsGroupCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 6)
)
if mibBuilder.loadTexts:
    tApsGroupCommandTable.setStatus("current")
_TApsGroupCommandEntry_Object = MibTableRow
tApsGroupCommandEntry = _TApsGroupCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 6, 1)
)
if mibBuilder.loadTexts:
    tApsGroupCommandEntry.setStatus("current")


class _TApsAnnexBCommandSwitch_Type(Integer32):
    """Custom type tApsAnnexBCommandSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearLockout", 3),
          ("lockout", 2),
          ("noCmd", 1))
    )


_TApsAnnexBCommandSwitch_Type.__name__ = "Integer32"
_TApsAnnexBCommandSwitch_Object = MibTableColumn
tApsAnnexBCommandSwitch = _TApsAnnexBCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 6, 1, 1),
    _TApsAnnexBCommandSwitch_Type()
)
tApsAnnexBCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tApsAnnexBCommandSwitch.setStatus("current")
_TApsNotificationsPrefix_ObjectIdentity = ObjectIdentity
tApsNotificationsPrefix = _TApsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29)
)
_TApsNotifications_ObjectIdentity = ObjectIdentity
tApsNotifications = _TApsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0)
)
apsCommandEntry.registerAugmentions(
    ("TIMETRA-APS-MIB",
     "tApsCommandEntry")
)
tApsCommandEntry.setIndexNames(*apsCommandEntry.getIndexNames())
apsChanConfigEntry.registerAugmentions(
    ("TIMETRA-APS-MIB",
     "tApsChanStatusEntry")
)
tApsChanStatusEntry.setIndexNames(*apsChanConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions(
    ("TIMETRA-APS-MIB",
     "tApsMcConfigEntry")
)
tApsMcConfigEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions(
    ("TIMETRA-APS-MIB",
     "tApsMcStatusEntry")
)
tApsMcStatusEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions(
    ("TIMETRA-APS-MIB",
     "tApsConfigEntry")
)
tApsConfigEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions(
    ("TIMETRA-APS-MIB",
     "tApsGroupCommandEntry")
)
tApsGroupCommandEntry.setIndexNames(*apsConfigEntry.getIndexNames())

# Managed Objects groups

tmnxApsSwitchCommand = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 1)
)
tmnxApsSwitchCommand.setObjects(
    ("TIMETRA-APS-MIB", "tApsExerciseCommandResult")
)
if mibBuilder.loadTexts:
    tmnxApsSwitchCommand.setStatus("current")

tmnxApsChanStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 2)
)
tmnxApsChanStatus.setObjects(
    ("TIMETRA-APS-MIB", "tApsChanTxLaisState")
)
if mibBuilder.loadTexts:
    tmnxApsChanStatus.setStatus("current")

tmnxApsMcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 5)
)
tmnxApsMcGroup.setObjects(
      *(("TIMETRA-APS-MIB", "tApsMcNeighborAddrType"),
        ("TIMETRA-APS-MIB", "tApsMcNeighborAddr"),
        ("TIMETRA-APS-MIB", "tApsMcAdvertiseInterval"),
        ("TIMETRA-APS-MIB", "tApsMcHoldTime"),
        ("TIMETRA-APS-MIB", "tApsMcApsCtlLinkState"))
)
if mibBuilder.loadTexts:
    tmnxApsMcGroup.setStatus("current")

tmnxApsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 6)
)
tmnxApsConfigGroup.setObjects(
      *(("TIMETRA-APS-MIB", "tApsProtectionType"),
        ("TIMETRA-APS-MIB", "tApsLineSFHoldTime"),
        ("TIMETRA-APS-MIB", "tApsLineSDHoldTime"))
)
if mibBuilder.loadTexts:
    tmnxApsConfigGroup.setStatus("current")

tmnxApsConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 7)
)
tmnxApsConfigV8v0Group.setObjects(
    ("TIMETRA-APS-MIB", "tApsRdiAlarmGeneration")
)
if mibBuilder.loadTexts:
    tmnxApsConfigV8v0Group.setStatus("current")

tmnxApsGroupCommandV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 8)
)
tmnxApsGroupCommandV9v0Group.setObjects(
    ("TIMETRA-APS-MIB", "tApsAnnexBCommandSwitch")
)
if mibBuilder.loadTexts:
    tmnxApsGroupCommandV9v0Group.setStatus("current")


# Notification objects

tApsModeMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 1)
)
tApsModeMismatchClear.setObjects(
    ("APS-MIB", "apsStatusCurrent")
)
if mibBuilder.loadTexts:
    tApsModeMismatchClear.setStatus(
        "current"
    )

tApsChannelMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 2)
)
tApsChannelMismatchClear.setObjects(
    ("APS-MIB", "apsStatusCurrent")
)
if mibBuilder.loadTexts:
    tApsChannelMismatchClear.setStatus(
        "current"
    )

tApsPSBFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 3)
)
tApsPSBFClear.setObjects(
    ("APS-MIB", "apsStatusCurrent")
)
if mibBuilder.loadTexts:
    tApsPSBFClear.setStatus(
        "current"
    )

tApsFEPLFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 4)
)
tApsFEPLFClear.setObjects(
    ("APS-MIB", "apsStatusCurrent")
)
if mibBuilder.loadTexts:
    tApsFEPLFClear.setStatus(
        "current"
    )

tApsLocalSwitchCommandSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 5)
)
tApsLocalSwitchCommandSet.setObjects(
    ("APS-MIB", "apsCommandSwitch")
)
if mibBuilder.loadTexts:
    tApsLocalSwitchCommandSet.setStatus(
        "current"
    )

tApsLocalSwitchCommandClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 6)
)
tApsLocalSwitchCommandClear.setObjects(
    ("APS-MIB", "apsCommandSwitch")
)
if mibBuilder.loadTexts:
    tApsLocalSwitchCommandClear.setStatus(
        "current"
    )

tApsRemoteSwitchCommandSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 7)
)
tApsRemoteSwitchCommandSet.setObjects(
    ("APS-MIB", "apsCommandSwitch")
)
if mibBuilder.loadTexts:
    tApsRemoteSwitchCommandSet.setStatus(
        "current"
    )

tApsRemoteSwitchCommandClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 8)
)
tApsRemoteSwitchCommandClear.setObjects(
    ("APS-MIB", "apsCommandSwitch")
)
if mibBuilder.loadTexts:
    tApsRemoteSwitchCommandClear.setStatus(
        "current"
    )

tApsMcApsCtlLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 9)
)
tApsMcApsCtlLinkStateChange.setObjects(
    ("TIMETRA-APS-MIB", "tApsMcApsCtlLinkState")
)
if mibBuilder.loadTexts:
    tApsMcApsCtlLinkStateChange.setStatus(
        "current"
    )

tApsChanTxLaisStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 10)
)
tApsChanTxLaisStateChange.setObjects(
    ("TIMETRA-APS-MIB", "tApsChanTxLaisState")
)
if mibBuilder.loadTexts:
    tApsChanTxLaisStateChange.setStatus(
        "current"
    )

tApsPrimaryChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 11)
)
tApsPrimaryChannelChange.setObjects(
      *(("APS-MIB", "apsStatusSwitchedChannel"),
        ("APS-MIB", "apsStatusK1K2Trans"),
        ("APS-MIB", "apsStatusK1K2Rcv"))
)
if mibBuilder.loadTexts:
    tApsPrimaryChannelChange.setStatus(
        "current"
    )


# Notifications groups

tmnxApsNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 3)
)
tmnxApsNotifications.setObjects(
      *(("TIMETRA-APS-MIB", "tApsModeMismatchClear"),
        ("TIMETRA-APS-MIB", "tApsChannelMismatchClear"),
        ("TIMETRA-APS-MIB", "tApsPSBFClear"),
        ("TIMETRA-APS-MIB", "tApsFEPLFClear"),
        ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandSet"),
        ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandClear"),
        ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandSet"),
        ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandClear"))
)
if mibBuilder.loadTexts:
    tmnxApsNotifications.setStatus(
        "obsolete"
    )

tmnxApsNotificationsV4v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 4)
)
tmnxApsNotificationsV4v0.setObjects(
      *(("TIMETRA-APS-MIB", "tApsModeMismatchClear"),
        ("TIMETRA-APS-MIB", "tApsChannelMismatchClear"),
        ("TIMETRA-APS-MIB", "tApsPSBFClear"),
        ("TIMETRA-APS-MIB", "tApsFEPLFClear"),
        ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandSet"),
        ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandClear"),
        ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandSet"),
        ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandClear"),
        ("TIMETRA-APS-MIB", "tApsMcApsCtlLinkStateChange"),
        ("TIMETRA-APS-MIB", "tApsChanTxLaisStateChange"))
)
if mibBuilder.loadTexts:
    tmnxApsNotificationsV4v0.setStatus(
        "current"
    )

tmnxApsNotificationsV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 9)
)
tmnxApsNotificationsV9v0Group.setObjects(
    ("TIMETRA-APS-MIB", "tApsPrimaryChannelChange")
)
if mibBuilder.loadTexts:
    tmnxApsNotificationsV9v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tApsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 1)
)
if mibBuilder.loadTexts:
    tApsMIBCompliance.setStatus(
        "obsolete"
    )

tApsMIBComplianceV4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 2)
)
if mibBuilder.loadTexts:
    tApsMIBComplianceV4v0.setStatus(
        "obsolete"
    )

tApsMIBComplianceV7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 3)
)
if mibBuilder.loadTexts:
    tApsMIBComplianceV7v0.setStatus(
        "obsolete"
    )

tApsMIBComplianceV8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 4)
)
if mibBuilder.loadTexts:
    tApsMIBComplianceV8v0.setStatus(
        "obsolete"
    )

tApsMIBComplianceV9v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 5)
)
if mibBuilder.loadTexts:
    tApsMIBComplianceV9v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-APS-MIB",
    **{"timetraAPSMIBModule": timetraAPSMIBModule,
       "tApsMIBConformance": tApsMIBConformance,
       "tmnxApsMIBCompliances": tmnxApsMIBCompliances,
       "tApsMIBCompliance": tApsMIBCompliance,
       "tApsMIBComplianceV4v0": tApsMIBComplianceV4v0,
       "tApsMIBComplianceV7v0": tApsMIBComplianceV7v0,
       "tApsMIBComplianceV8v0": tApsMIBComplianceV8v0,
       "tApsMIBComplianceV9v0": tApsMIBComplianceV9v0,
       "tmnxApsMIBGroups": tmnxApsMIBGroups,
       "tmnxApsSwitchCommand": tmnxApsSwitchCommand,
       "tmnxApsChanStatus": tmnxApsChanStatus,
       "tmnxApsNotifications": tmnxApsNotifications,
       "tmnxApsNotificationsV4v0": tmnxApsNotificationsV4v0,
       "tmnxApsMcGroup": tmnxApsMcGroup,
       "tmnxApsConfigGroup": tmnxApsConfigGroup,
       "tmnxApsConfigV8v0Group": tmnxApsConfigV8v0Group,
       "tmnxApsGroupCommandV9v0Group": tmnxApsGroupCommandV9v0Group,
       "tmnxApsNotificationsV9v0Group": tmnxApsNotificationsV9v0Group,
       "tApsMIBObjs": tApsMIBObjs,
       "tApsCommandTable": tApsCommandTable,
       "tApsCommandEntry": tApsCommandEntry,
       "tApsExerciseCommandResult": tApsExerciseCommandResult,
       "tApsChanStatusTable": tApsChanStatusTable,
       "tApsChanStatusEntry": tApsChanStatusEntry,
       "tApsChanTxLaisState": tApsChanTxLaisState,
       "tApsMcConfigTable": tApsMcConfigTable,
       "tApsMcConfigEntry": tApsMcConfigEntry,
       "tApsMcNeighborAddrType": tApsMcNeighborAddrType,
       "tApsMcNeighborAddr": tApsMcNeighborAddr,
       "tApsMcAdvertiseInterval": tApsMcAdvertiseInterval,
       "tApsMcHoldTime": tApsMcHoldTime,
       "tApsMcStatusTable": tApsMcStatusTable,
       "tApsMcStatusEntry": tApsMcStatusEntry,
       "tApsMcApsCtlLinkState": tApsMcApsCtlLinkState,
       "tApsConfigTable": tApsConfigTable,
       "tApsConfigEntry": tApsConfigEntry,
       "tApsProtectionType": tApsProtectionType,
       "tApsLineSFHoldTime": tApsLineSFHoldTime,
       "tApsLineSDHoldTime": tApsLineSDHoldTime,
       "tApsRdiAlarmGeneration": tApsRdiAlarmGeneration,
       "tApsGroupCommandTable": tApsGroupCommandTable,
       "tApsGroupCommandEntry": tApsGroupCommandEntry,
       "tApsAnnexBCommandSwitch": tApsAnnexBCommandSwitch,
       "tApsNotificationsPrefix": tApsNotificationsPrefix,
       "tApsNotifications": tApsNotifications,
       "tApsModeMismatchClear": tApsModeMismatchClear,
       "tApsChannelMismatchClear": tApsChannelMismatchClear,
       "tApsPSBFClear": tApsPSBFClear,
       "tApsFEPLFClear": tApsFEPLFClear,
       "tApsLocalSwitchCommandSet": tApsLocalSwitchCommandSet,
       "tApsLocalSwitchCommandClear": tApsLocalSwitchCommandClear,
       "tApsRemoteSwitchCommandSet": tApsRemoteSwitchCommandSet,
       "tApsRemoteSwitchCommandClear": tApsRemoteSwitchCommandClear,
       "tApsMcApsCtlLinkStateChange": tApsMcApsCtlLinkStateChange,
       "tApsChanTxLaisStateChange": tApsChanTxLaisStateChange,
       "tApsPrimaryChannelChange": tApsPrimaryChannelChange}
)
