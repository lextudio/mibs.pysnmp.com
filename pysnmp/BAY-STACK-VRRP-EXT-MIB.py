# SNMP MIB module (BAY-STACK-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-VRRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:24 2024
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

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")

(vrrpOperPrimaryIpAddr,
 vrrpOperVrId) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperPrimaryIpAddr",
    "vrrpOperVrId")


# MODULE-IDENTITY

bayStackVrrpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 11)
)
bayStackVrrpExtMib.setRevisions(
        ("2005-07-01 00:00",
         "2012-10-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsveNotifications_ObjectIdentity = ObjectIdentity
bsveNotifications = _BsveNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 0)
)
_BsveObjects_ObjectIdentity = ObjectIdentity
bsveObjects = _BsveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1)
)
_BsveScalars_ObjectIdentity = ObjectIdentity
bsveScalars = _BsveScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 1)
)
_BsveVrrpEnabled_Type = TruthValue
_BsveVrrpEnabled_Object = MibScalar
bsveVrrpEnabled = _BsveVrrpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 1, 1),
    _BsveVrrpEnabled_Type()
)
bsveVrrpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpEnabled.setStatus("current")


class _BsveVrrpPingVirtualAddrEnabled_Type(TruthValue):
    """Custom type bsveVrrpPingVirtualAddrEnabled based on TruthValue"""


_BsveVrrpPingVirtualAddrEnabled_Object = MibScalar
bsveVrrpPingVirtualAddrEnabled = _BsveVrrpPingVirtualAddrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 1, 2),
    _BsveVrrpPingVirtualAddrEnabled_Type()
)
bsveVrrpPingVirtualAddrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpPingVirtualAddrEnabled.setStatus("current")
_BsveVrrpOperExtTable_Object = MibTable
bsveVrrpOperExtTable = _BsveVrrpOperExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2)
)
if mibBuilder.loadTexts:
    bsveVrrpOperExtTable.setStatus("current")
_BsveVrrpOperExtEntry_Object = MibTableRow
bsveVrrpOperExtEntry = _BsveVrrpOperExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1)
)
bsveVrrpOperExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    bsveVrrpOperExtEntry.setStatus("current")
_BsveVrrpOperExtCriticalIpAddr_Type = IpAddress
_BsveVrrpOperExtCriticalIpAddr_Object = MibTableColumn
bsveVrrpOperExtCriticalIpAddr = _BsveVrrpOperExtCriticalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 1),
    _BsveVrrpOperExtCriticalIpAddr_Type()
)
bsveVrrpOperExtCriticalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtCriticalIpAddr.setStatus("current")


class _BsveVrrpOperExtCriticalIpAddrEnabled_Type(TruthValue):
    """Custom type bsveVrrpOperExtCriticalIpAddrEnabled based on TruthValue"""


_BsveVrrpOperExtCriticalIpAddrEnabled_Object = MibTableColumn
bsveVrrpOperExtCriticalIpAddrEnabled = _BsveVrrpOperExtCriticalIpAddrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 2),
    _BsveVrrpOperExtCriticalIpAddrEnabled_Type()
)
bsveVrrpOperExtCriticalIpAddrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtCriticalIpAddrEnabled.setStatus("current")


class _BsveVrrpOperExtHoldDownTimer_Type(Integer32):
    """Custom type bsveVrrpOperExtHoldDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21600),
    )


_BsveVrrpOperExtHoldDownTimer_Type.__name__ = "Integer32"
_BsveVrrpOperExtHoldDownTimer_Object = MibTableColumn
bsveVrrpOperExtHoldDownTimer = _BsveVrrpOperExtHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 3),
    _BsveVrrpOperExtHoldDownTimer_Type()
)
bsveVrrpOperExtHoldDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtHoldDownTimer.setStatus("current")


class _BsveVrrpOperExtHoldDownState_Type(Integer32):
    """Custom type bsveVrrpOperExtHoldDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("dormant", 1))
    )


_BsveVrrpOperExtHoldDownState_Type.__name__ = "Integer32"
_BsveVrrpOperExtHoldDownState_Object = MibTableColumn
bsveVrrpOperExtHoldDownState = _BsveVrrpOperExtHoldDownState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 4),
    _BsveVrrpOperExtHoldDownState_Type()
)
bsveVrrpOperExtHoldDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsveVrrpOperExtHoldDownState.setStatus("current")


class _BsveVrrpOperExtHoldDownTimeRemaining_Type(Integer32):
    """Custom type bsveVrrpOperExtHoldDownTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21600),
    )


_BsveVrrpOperExtHoldDownTimeRemaining_Type.__name__ = "Integer32"
_BsveVrrpOperExtHoldDownTimeRemaining_Object = MibTableColumn
bsveVrrpOperExtHoldDownTimeRemaining = _BsveVrrpOperExtHoldDownTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 5),
    _BsveVrrpOperExtHoldDownTimeRemaining_Type()
)
bsveVrrpOperExtHoldDownTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsveVrrpOperExtHoldDownTimeRemaining.setStatus("current")


class _BsveVrrpOperExtAction_Type(Integer32):
    """Custom type bsveVrrpOperExtAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("preemptHoldDownTimer", 2))
    )


_BsveVrrpOperExtAction_Type.__name__ = "Integer32"
_BsveVrrpOperExtAction_Object = MibTableColumn
bsveVrrpOperExtAction = _BsveVrrpOperExtAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 6),
    _BsveVrrpOperExtAction_Type()
)
bsveVrrpOperExtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtAction.setStatus("current")


class _BsveVrrpOperExtBackUpMasterEnabled_Type(TruthValue):
    """Custom type bsveVrrpOperExtBackUpMasterEnabled based on TruthValue"""


_BsveVrrpOperExtBackUpMasterEnabled_Object = MibTableColumn
bsveVrrpOperExtBackUpMasterEnabled = _BsveVrrpOperExtBackUpMasterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 7),
    _BsveVrrpOperExtBackUpMasterEnabled_Type()
)
bsveVrrpOperExtBackUpMasterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtBackUpMasterEnabled.setStatus("current")


class _BsveVrrpOperExtBackUpMasterState_Type(Integer32):
    """Custom type bsveVrrpOperExtBackUpMasterState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_BsveVrrpOperExtBackUpMasterState_Type.__name__ = "Integer32"
_BsveVrrpOperExtBackUpMasterState_Object = MibTableColumn
bsveVrrpOperExtBackUpMasterState = _BsveVrrpOperExtBackUpMasterState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 8),
    _BsveVrrpOperExtBackUpMasterState_Type()
)
bsveVrrpOperExtBackUpMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsveVrrpOperExtBackUpMasterState.setStatus("current")


class _BsveVrrpOperExtFasterAdvInterval_Type(Integer32):
    """Custom type bsveVrrpOperExtFasterAdvInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_BsveVrrpOperExtFasterAdvInterval_Type.__name__ = "Integer32"
_BsveVrrpOperExtFasterAdvInterval_Object = MibTableColumn
bsveVrrpOperExtFasterAdvInterval = _BsveVrrpOperExtFasterAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 9),
    _BsveVrrpOperExtFasterAdvInterval_Type()
)
bsveVrrpOperExtFasterAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtFasterAdvInterval.setStatus("current")


class _BsveVrrpOperExtFasterAdvIntervalEnabled_Type(TruthValue):
    """Custom type bsveVrrpOperExtFasterAdvIntervalEnabled based on TruthValue"""


_BsveVrrpOperExtFasterAdvIntervalEnabled_Object = MibTableColumn
bsveVrrpOperExtFasterAdvIntervalEnabled = _BsveVrrpOperExtFasterAdvIntervalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 10),
    _BsveVrrpOperExtFasterAdvIntervalEnabled_Type()
)
bsveVrrpOperExtFasterAdvIntervalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsveVrrpOperExtFasterAdvIntervalEnabled.setStatus("current")
_BsveNotificationObjects_ObjectIdentity = ObjectIdentity
bsveNotificationObjects = _BsveNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 4)
)


class _BsveVrrpTrapStateTransitionType_Type(Integer32):
    """Custom type bsveVrrpTrapStateTransitionType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("backUpMasterToBackup", 9),
          ("backupToBackUpMaster", 8),
          ("backupToInitialize", 7),
          ("backupToMaster", 3),
          ("initializeToBackup", 6),
          ("initializeToMaster", 4),
          ("masterToBackup", 2),
          ("masterToInitialize", 5),
          ("none", 1))
    )


_BsveVrrpTrapStateTransitionType_Type.__name__ = "Integer32"
_BsveVrrpTrapStateTransitionType_Object = MibScalar
bsveVrrpTrapStateTransitionType = _BsveVrrpTrapStateTransitionType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 4, 1),
    _BsveVrrpTrapStateTransitionType_Type()
)
bsveVrrpTrapStateTransitionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsveVrrpTrapStateTransitionType.setStatus("current")


class _BsveVrrpTrapStateTransitionCause_Type(Integer32):
    """Custom type bsveVrrpTrapStateTransitionCause based on Integer32"""
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("criticalIPFail", 7),
          ("higherPriorityAdvertizeReceived", 2),
          ("higherSrcIPEqualPrioAdvReceived", 12),
          ("iPInterfaceDown", 10),
          ("lowerPrioAdvReceived", 11),
          ("lowerSrcIPEqualPrioAdvReceived", 13),
          ("masterDownInterval", 5),
          ("none", 1),
          ("other", 15),
          ("preempted", 6),
          ("reboot", 16),
          ("shutdownReceived", 3),
          ("startVR", 14),
          ("syncFromPrimary", 9),
          ("usrConfig", 8),
          ("vrrpAddrAndPhysicalAddrMatch", 4))
    )


_BsveVrrpTrapStateTransitionCause_Type.__name__ = "Integer32"
_BsveVrrpTrapStateTransitionCause_Object = MibScalar
bsveVrrpTrapStateTransitionCause = _BsveVrrpTrapStateTransitionCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 4, 2),
    _BsveVrrpTrapStateTransitionCause_Type()
)
bsveVrrpTrapStateTransitionCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsveVrrpTrapStateTransitionCause.setStatus("current")

# Managed Objects groups


# Notification objects

bsveVrrpTrapStateTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 11, 0, 1)
)
bsveVrrpTrapStateTransition.setObjects(
      *(("BAY-STACK-VRRP-EXT-MIB", "bsveVrrpTrapStateTransitionType"),
        ("BAY-STACK-VRRP-EXT-MIB", "bsveVrrpTrapStateTransitionCause"),
        ("VRRP-MIB", "vrrpOperPrimaryIpAddr"),
        ("IP-MIB", "ipAdEntAddr"))
)
if mibBuilder.loadTexts:
    bsveVrrpTrapStateTransition.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-VRRP-EXT-MIB",
    **{"bayStackVrrpExtMib": bayStackVrrpExtMib,
       "bsveNotifications": bsveNotifications,
       "bsveVrrpTrapStateTransition": bsveVrrpTrapStateTransition,
       "bsveObjects": bsveObjects,
       "bsveScalars": bsveScalars,
       "bsveVrrpEnabled": bsveVrrpEnabled,
       "bsveVrrpPingVirtualAddrEnabled": bsveVrrpPingVirtualAddrEnabled,
       "bsveVrrpOperExtTable": bsveVrrpOperExtTable,
       "bsveVrrpOperExtEntry": bsveVrrpOperExtEntry,
       "bsveVrrpOperExtCriticalIpAddr": bsveVrrpOperExtCriticalIpAddr,
       "bsveVrrpOperExtCriticalIpAddrEnabled": bsveVrrpOperExtCriticalIpAddrEnabled,
       "bsveVrrpOperExtHoldDownTimer": bsveVrrpOperExtHoldDownTimer,
       "bsveVrrpOperExtHoldDownState": bsveVrrpOperExtHoldDownState,
       "bsveVrrpOperExtHoldDownTimeRemaining": bsveVrrpOperExtHoldDownTimeRemaining,
       "bsveVrrpOperExtAction": bsveVrrpOperExtAction,
       "bsveVrrpOperExtBackUpMasterEnabled": bsveVrrpOperExtBackUpMasterEnabled,
       "bsveVrrpOperExtBackUpMasterState": bsveVrrpOperExtBackUpMasterState,
       "bsveVrrpOperExtFasterAdvInterval": bsveVrrpOperExtFasterAdvInterval,
       "bsveVrrpOperExtFasterAdvIntervalEnabled": bsveVrrpOperExtFasterAdvIntervalEnabled,
       "bsveNotificationObjects": bsveNotificationObjects,
       "bsveVrrpTrapStateTransitionType": bsveVrrpTrapStateTransitionType,
       "bsveVrrpTrapStateTransitionCause": bsveVrrpTrapStateTransitionCause}
)
