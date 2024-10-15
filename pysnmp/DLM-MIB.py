# SNMP MIB module (DLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:37 2024
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

(ctronDLM,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctronDLM")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpPollTable_Object = MibTable
snmpPollTable = _SnmpPollTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    snmpPollTable.setStatus("mandatory")
_SnmpPollEntry_Object = MibTableRow
snmpPollEntry = _SnmpPollEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1)
)
snmpPollEntry.setIndexNames(
    (0, "DLM-MIB", "snmpPollDestination"),
    (0, "DLM-MIB", "snmpPollOwner"),
)
if mibBuilder.loadTexts:
    snmpPollEntry.setStatus("mandatory")
_SnmpPollDestination_Type = IpAddress
_SnmpPollDestination_Object = MibTableColumn
snmpPollDestination = _SnmpPollDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 1),
    _SnmpPollDestination_Type()
)
snmpPollDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPollDestination.setStatus("mandatory")
_SnmpPollOwner_Type = IpAddress
_SnmpPollOwner_Object = MibTableColumn
snmpPollOwner = _SnmpPollOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 2),
    _SnmpPollOwner_Type()
)
snmpPollOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPollOwner.setStatus("mandatory")


class _SnmpPollCommunity_Type(OctetString):
    """Custom type snmpPollCommunity based on OctetString"""
    defaultValue = OctetString("public")


_SnmpPollCommunity_Object = MibTableColumn
snmpPollCommunity = _SnmpPollCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 3),
    _SnmpPollCommunity_Type()
)
snmpPollCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollCommunity.setStatus("mandatory")


class _SnmpPollInterval_Type(Integer32):
    """Custom type snmpPollInterval based on Integer32"""
    defaultValue = 60


_SnmpPollInterval_Object = MibTableColumn
snmpPollInterval = _SnmpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 4),
    _SnmpPollInterval_Type()
)
snmpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollInterval.setStatus("mandatory")


class _SnmpPollRetry_Type(Integer32):
    """Custom type snmpPollRetry based on Integer32"""
    defaultValue = 3


_SnmpPollRetry_Object = MibTableColumn
snmpPollRetry = _SnmpPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 5),
    _SnmpPollRetry_Type()
)
snmpPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollRetry.setStatus("mandatory")


class _SnmpPollAction_Type(Integer32):
    """Custom type snmpPollAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("send-trap", 2))
    )


_SnmpPollAction_Type.__name__ = "Integer32"
_SnmpPollAction_Object = MibTableColumn
snmpPollAction = _SnmpPollAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 6),
    _SnmpPollAction_Type()
)
snmpPollAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollAction.setStatus("mandatory")
_SnmpPollTrapAddress_Type = IpAddress
_SnmpPollTrapAddress_Object = MibTableColumn
snmpPollTrapAddress = _SnmpPollTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 7),
    _SnmpPollTrapAddress_Type()
)
snmpPollTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollTrapAddress.setStatus("mandatory")


class _SnmpPollType_Type(Integer32):
    """Custom type snmpPollType based on Integer32"""
    defaultValue = 3

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
        *(("activate", 3),
          ("invalid", 2),
          ("other", 1),
          ("suspend", 4))
    )


_SnmpPollType_Type.__name__ = "Integer32"
_SnmpPollType_Object = MibTableColumn
snmpPollType = _SnmpPollType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 8),
    _SnmpPollType_Type()
)
snmpPollType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollType.setStatus("mandatory")


class _SnmpPollStatus_Type(Integer32):
    """Custom type snmpPollStatus based on Integer32"""
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
        *(("active", 2),
          ("alarm-condition", 4),
          ("general-failure", 5),
          ("inactive", 1),
          ("lost-contact", 3))
    )


_SnmpPollStatus_Type.__name__ = "Integer32"
_SnmpPollStatus_Object = MibTableColumn
snmpPollStatus = _SnmpPollStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 9),
    _SnmpPollStatus_Type()
)
snmpPollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPollStatus.setStatus("mandatory")
_SnmpPollRequests_Type = Counter32
_SnmpPollRequests_Object = MibTableColumn
snmpPollRequests = _SnmpPollRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 10),
    _SnmpPollRequests_Type()
)
snmpPollRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPollRequests.setStatus("mandatory")
_SnmpPollLastContact_Type = TimeTicks
_SnmpPollLastContact_Object = MibTableColumn
snmpPollLastContact = _SnmpPollLastContact_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 11),
    _SnmpPollLastContact_Type()
)
snmpPollLastContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPollLastContact.setStatus("mandatory")
_SnmpPollLastAlarm_Type = TimeTicks
_SnmpPollLastAlarm_Object = MibTableColumn
snmpPollLastAlarm = _SnmpPollLastAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 12),
    _SnmpPollLastAlarm_Type()
)
snmpPollLastAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPollLastAlarm.setStatus("mandatory")


class _SnmpPollAlarmWait_Type(Integer32):
    """Custom type snmpPollAlarmWait based on Integer32"""
    defaultValue = 60


_SnmpPollAlarmWait_Object = MibTableColumn
snmpPollAlarmWait = _SnmpPollAlarmWait_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 13),
    _SnmpPollAlarmWait_Type()
)
snmpPollAlarmWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollAlarmWait.setStatus("mandatory")


class _SnmpPollTrapCommunity_Type(OctetString):
    """Custom type snmpPollTrapCommunity based on OctetString"""
    defaultValue = OctetString("public")


_SnmpPollTrapCommunity_Object = MibTableColumn
snmpPollTrapCommunity = _SnmpPollTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 14),
    _SnmpPollTrapCommunity_Type()
)
snmpPollTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollTrapCommunity.setStatus("mandatory")


class _SnmpPollProtocol_Type(Integer32):
    """Custom type snmpPollProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internet-ping", 1),
          ("snmp", 2))
    )


_SnmpPollProtocol_Type.__name__ = "Integer32"
_SnmpPollProtocol_Object = MibTableColumn
snmpPollProtocol = _SnmpPollProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 1, 1, 15),
    _SnmpPollProtocol_Type()
)
snmpPollProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPollProtocol.setStatus("mandatory")
_SnmpOIDTable_Object = MibTable
snmpOIDTable = _SnmpOIDTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    snmpOIDTable.setStatus("mandatory")
_SnmpOIDEntry_Object = MibTableRow
snmpOIDEntry = _SnmpOIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1)
)
snmpOIDEntry.setIndexNames(
    (0, "DLM-MIB", "snmpOIDDestination"),
    (0, "DLM-MIB", "snmpOIDOwner"),
    (0, "DLM-MIB", "snmpOIDSequence"),
)
if mibBuilder.loadTexts:
    snmpOIDEntry.setStatus("mandatory")
_SnmpOIDDestination_Type = IpAddress
_SnmpOIDDestination_Object = MibTableColumn
snmpOIDDestination = _SnmpOIDDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 1),
    _SnmpOIDDestination_Type()
)
snmpOIDDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDDestination.setStatus("mandatory")
_SnmpOIDOwner_Type = IpAddress
_SnmpOIDOwner_Object = MibTableColumn
snmpOIDOwner = _SnmpOIDOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 2),
    _SnmpOIDOwner_Type()
)
snmpOIDOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDOwner.setStatus("mandatory")
_SnmpOIDSequence_Type = Integer32
_SnmpOIDSequence_Object = MibTableColumn
snmpOIDSequence = _SnmpOIDSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 3),
    _SnmpOIDSequence_Type()
)
snmpOIDSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDSequence.setStatus("mandatory")
_SnmpOIDObject_Type = ObjectIdentifier
_SnmpOIDObject_Object = MibTableColumn
snmpOIDObject = _SnmpOIDObject_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 4),
    _SnmpOIDObject_Type()
)
snmpOIDObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDObject.setStatus("mandatory")


class _SnmpOIDComparator_Type(Integer32):
    """Custom type snmpOIDComparator based on Integer32"""
    defaultValue = 7

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dont-compare", 7),
          ("equal", 1),
          ("greater", 2),
          ("greater-or-equal", 4),
          ("less", 3),
          ("less-or-equal", 5),
          ("not-equal", 8),
          ("trap-always", 6))
    )


_SnmpOIDComparator_Type.__name__ = "Integer32"
_SnmpOIDComparator_Object = MibTableColumn
snmpOIDComparator = _SnmpOIDComparator_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 5),
    _SnmpOIDComparator_Type()
)
snmpOIDComparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDComparator.setStatus("mandatory")


class _SnmpOIDEnumType_Type(Integer32):
    """Custom type snmpOIDEnumType based on Integer32"""
    defaultValue = 4

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
        *(("counter", 2),
          ("gauge", 3),
          ("integer", 1),
          ("ticks", 4))
    )


_SnmpOIDEnumType_Type.__name__ = "Integer32"
_SnmpOIDEnumType_Object = MibTableColumn
snmpOIDEnumType = _SnmpOIDEnumType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 6),
    _SnmpOIDEnumType_Type()
)
snmpOIDEnumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDEnumType.setStatus("mandatory")


class _SnmpOIDThresholdInteger_Type(Integer32):
    """Custom type snmpOIDThresholdInteger based on Integer32"""
    defaultValue = 0


_SnmpOIDThresholdInteger_Object = MibTableColumn
snmpOIDThresholdInteger = _SnmpOIDThresholdInteger_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 7),
    _SnmpOIDThresholdInteger_Type()
)
snmpOIDThresholdInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDThresholdInteger.setStatus("mandatory")
_SnmpOIDThresholdCounter_Type = Counter32
_SnmpOIDThresholdCounter_Object = MibTableColumn
snmpOIDThresholdCounter = _SnmpOIDThresholdCounter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 8),
    _SnmpOIDThresholdCounter_Type()
)
snmpOIDThresholdCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDThresholdCounter.setStatus("mandatory")
_SnmpOIDThresholdGauge_Type = Gauge32
_SnmpOIDThresholdGauge_Object = MibTableColumn
snmpOIDThresholdGauge = _SnmpOIDThresholdGauge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 9),
    _SnmpOIDThresholdGauge_Type()
)
snmpOIDThresholdGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDThresholdGauge.setStatus("mandatory")


class _SnmpOIDThresholdTicks_Type(TimeTicks):
    """Custom type snmpOIDThresholdTicks based on TimeTicks"""
    defaultValue = 0


_SnmpOIDThresholdTicks_Object = MibTableColumn
snmpOIDThresholdTicks = _SnmpOIDThresholdTicks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 10),
    _SnmpOIDThresholdTicks_Type()
)
snmpOIDThresholdTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDThresholdTicks.setStatus("mandatory")


class _SnmpOIDType_Type(Integer32):
    """Custom type snmpOIDType based on Integer32"""
    defaultValue = 3

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
        *(("activate", 3),
          ("inactive", 2),
          ("other", 1),
          ("suspend", 4))
    )


_SnmpOIDType_Type.__name__ = "Integer32"
_SnmpOIDType_Object = MibTableColumn
snmpOIDType = _SnmpOIDType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 11),
    _SnmpOIDType_Type()
)
snmpOIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpOIDType.setStatus("mandatory")


class _SnmpOIDStatus_Type(Integer32):
    """Custom type snmpOIDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("alarm-condition", 3),
          ("inactive", 1))
    )


_SnmpOIDStatus_Type.__name__ = "Integer32"
_SnmpOIDStatus_Object = MibTableColumn
snmpOIDStatus = _SnmpOIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 12),
    _SnmpOIDStatus_Type()
)
snmpOIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOIDStatus.setStatus("mandatory")
_SnmpOIDLastValue_Type = Integer32
_SnmpOIDLastValue_Object = MibTableColumn
snmpOIDLastValue = _SnmpOIDLastValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1, 2, 1, 13),
    _SnmpOIDLastValue_Type()
)
snmpOIDLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOIDLastValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLM-MIB",
    **{"snmpPollTable": snmpPollTable,
       "snmpPollEntry": snmpPollEntry,
       "snmpPollDestination": snmpPollDestination,
       "snmpPollOwner": snmpPollOwner,
       "snmpPollCommunity": snmpPollCommunity,
       "snmpPollInterval": snmpPollInterval,
       "snmpPollRetry": snmpPollRetry,
       "snmpPollAction": snmpPollAction,
       "snmpPollTrapAddress": snmpPollTrapAddress,
       "snmpPollType": snmpPollType,
       "snmpPollStatus": snmpPollStatus,
       "snmpPollRequests": snmpPollRequests,
       "snmpPollLastContact": snmpPollLastContact,
       "snmpPollLastAlarm": snmpPollLastAlarm,
       "snmpPollAlarmWait": snmpPollAlarmWait,
       "snmpPollTrapCommunity": snmpPollTrapCommunity,
       "snmpPollProtocol": snmpPollProtocol,
       "snmpOIDTable": snmpOIDTable,
       "snmpOIDEntry": snmpOIDEntry,
       "snmpOIDDestination": snmpOIDDestination,
       "snmpOIDOwner": snmpOIDOwner,
       "snmpOIDSequence": snmpOIDSequence,
       "snmpOIDObject": snmpOIDObject,
       "snmpOIDComparator": snmpOIDComparator,
       "snmpOIDEnumType": snmpOIDEnumType,
       "snmpOIDThresholdInteger": snmpOIDThresholdInteger,
       "snmpOIDThresholdCounter": snmpOIDThresholdCounter,
       "snmpOIDThresholdGauge": snmpOIDThresholdGauge,
       "snmpOIDThresholdTicks": snmpOIDThresholdTicks,
       "snmpOIDType": snmpOIDType,
       "snmpOIDStatus": snmpOIDStatus,
       "snmpOIDLastValue": snmpOIDLastValue}
)
