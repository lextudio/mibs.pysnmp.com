# SNMP MIB module (NBFLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBFLT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:44 2024
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

(ngen,) = mibBuilder.importSymbols(
    "NT-Reference-MIB",
    "ngen")

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
 NotificationType,
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
    "NotificationType",
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

_NGenBase_ObjectIdentity = ObjectIdentity
nGenBase = _NGenBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1)
)
_NbFltMngmt_ObjectIdentity = ObjectIdentity
nbFltMngmt = _NbFltMngmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5)
)
_NbFltSNMPAgent_ObjectIdentity = ObjectIdentity
nbFltSNMPAgent = _NbFltSNMPAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1)
)
_NbFltSNMPAgentStatus_ObjectIdentity = ObjectIdentity
nbFltSNMPAgentStatus = _NbFltSNMPAgentStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 1)
)


class _NbFltTrapOnAlarm_Type(Integer32):
    """Custom type nbFltTrapOnAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NbFltTrapOnAlarm_Type.__name__ = "Integer32"
_NbFltTrapOnAlarm_Object = MibScalar
nbFltTrapOnAlarm = _NbFltTrapOnAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 1, 1),
    _NbFltTrapOnAlarm_Type()
)
nbFltTrapOnAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFltTrapOnAlarm.setStatus("mandatory")


class _NbFltAgentRunningState_Type(Integer32):
    """Custom type nbFltAgentRunningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_NbFltAgentRunningState_Type.__name__ = "Integer32"
_NbFltAgentRunningState_Object = MibScalar
nbFltAgentRunningState = _NbFltAgentRunningState_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 1, 2),
    _NbFltAgentRunningState_Type()
)
nbFltAgentRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbFltAgentRunningState.setStatus("mandatory")
_NbFltAlarmTrapFormat_ObjectIdentity = ObjectIdentity
nbFltAlarmTrapFormat = _NbFltAlarmTrapFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 2)
)


class _NbFltAlarmSymposiumTrapFormat_Type(Integer32):
    """Custom type nbFltAlarmSymposiumTrapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NbFltAlarmSymposiumTrapFormat_Type.__name__ = "Integer32"
_NbFltAlarmSymposiumTrapFormat_Object = MibScalar
nbFltAlarmSymposiumTrapFormat = _NbFltAlarmSymposiumTrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 2, 1),
    _NbFltAlarmSymposiumTrapFormat_Type()
)
nbFltAlarmSymposiumTrapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFltAlarmSymposiumTrapFormat.setStatus("mandatory")


class _NbFltAlarmCybeleTrapFormat_Type(Integer32):
    """Custom type nbFltAlarmCybeleTrapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NbFltAlarmCybeleTrapFormat_Type.__name__ = "Integer32"
_NbFltAlarmCybeleTrapFormat_Object = MibScalar
nbFltAlarmCybeleTrapFormat = _NbFltAlarmCybeleTrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 2, 2),
    _NbFltAlarmCybeleTrapFormat_Type()
)
nbFltAlarmCybeleTrapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFltAlarmCybeleTrapFormat.setStatus("mandatory")
_NbFltTrapObjects_ObjectIdentity = ObjectIdentity
nbFltTrapObjects = _NbFltTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2)
)
_NbFltAlarmTrapObjects_ObjectIdentity = ObjectIdentity
nbFltAlarmTrapObjects = _NbFltAlarmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1)
)
_NbFltAlarmSequence_Type = Counter32
_NbFltAlarmSequence_Object = MibScalar
nbFltAlarmSequence = _NbFltAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 1),
    _NbFltAlarmSequence_Type()
)
nbFltAlarmSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmSequence.setStatus("mandatory")


class _NbFltAlarmTimeStamp_Type(DisplayString):
    """Custom type nbFltAlarmTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbFltAlarmTimeStamp_Type.__name__ = "DisplayString"
_NbFltAlarmTimeStamp_Object = MibScalar
nbFltAlarmTimeStamp = _NbFltAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 2),
    _NbFltAlarmTimeStamp_Type()
)
nbFltAlarmTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmTimeStamp.setStatus("mandatory")
_NbFltAlarmEventCode_Type = Integer32
_NbFltAlarmEventCode_Object = MibScalar
nbFltAlarmEventCode = _NbFltAlarmEventCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 3),
    _NbFltAlarmEventCode_Type()
)
nbFltAlarmEventCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmEventCode.setStatus("mandatory")


class _NbFltAlarmEventType_Type(Integer32):
    """Custom type nbFltAlarmEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("message", 4),
          ("set", 1),
          ("unknown", 0))
    )


_NbFltAlarmEventType_Type.__name__ = "Integer32"
_NbFltAlarmEventType_Object = MibScalar
nbFltAlarmEventType = _NbFltAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 4),
    _NbFltAlarmEventType_Type()
)
nbFltAlarmEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmEventType.setStatus("mandatory")


class _NbFltAlarmEventSeverity_Type(Integer32):
    """Custom type nbFltAlarmEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3))
    )


_NbFltAlarmEventSeverity_Type.__name__ = "Integer32"
_NbFltAlarmEventSeverity_Object = MibScalar
nbFltAlarmEventSeverity = _NbFltAlarmEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 5),
    _NbFltAlarmEventSeverity_Type()
)
nbFltAlarmEventSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmEventSeverity.setStatus("mandatory")
_NbFltAlarmTenantID_Type = Integer32
_NbFltAlarmTenantID_Object = MibScalar
nbFltAlarmTenantID = _NbFltAlarmTenantID_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 6),
    _NbFltAlarmTenantID_Type()
)
nbFltAlarmTenantID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmTenantID.setStatus("mandatory")
_NbFltAlarmCustomerID_Type = Integer32
_NbFltAlarmCustomerID_Object = MibScalar
nbFltAlarmCustomerID = _NbFltAlarmCustomerID_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 7),
    _NbFltAlarmCustomerID_Type()
)
nbFltAlarmCustomerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmCustomerID.setStatus("mandatory")


class _NbFltAlarmOriginator_Type(DisplayString):
    """Custom type nbFltAlarmOriginator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbFltAlarmOriginator_Type.__name__ = "DisplayString"
_NbFltAlarmOriginator_Object = MibScalar
nbFltAlarmOriginator = _NbFltAlarmOriginator_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 8),
    _NbFltAlarmOriginator_Type()
)
nbFltAlarmOriginator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmOriginator.setStatus("mandatory")


class _NbFltAlarmDescription_Type(DisplayString):
    """Custom type nbFltAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NbFltAlarmDescription_Type.__name__ = "DisplayString"
_NbFltAlarmDescription_Object = MibScalar
nbFltAlarmDescription = _NbFltAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 9),
    _NbFltAlarmDescription_Type()
)
nbFltAlarmDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbFltAlarmDescription.setStatus("mandatory")
_NbFltTraps_ObjectIdentity = ObjectIdentity
nbFltTraps = _NbFltTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 3)
)

# Managed Objects groups


# Notification objects

nbSymposiumAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 3, 0, 1)
)
nbSymposiumAlarmTrap.setObjects(
      *(("NBFLT-MIB", "nbFltAlarmSequence"),
        ("NBFLT-MIB", "nbFltAlarmTimeStamp"),
        ("NBFLT-MIB", "nbFltAlarmEventCode"),
        ("NBFLT-MIB", "nbFltAlarmEventType"),
        ("NBFLT-MIB", "nbFltAlarmEventSeverity"),
        ("NBFLT-MIB", "nbFltAlarmTenantID"),
        ("NBFLT-MIB", "nbFltAlarmCustomerID"),
        ("NBFLT-MIB", "nbFltAlarmOriginator"),
        ("NBFLT-MIB", "nbFltAlarmDescription"))
)
if mibBuilder.loadTexts:
    nbSymposiumAlarmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBFLT-MIB",
    **{"nGenBase": nGenBase,
       "nbFltMngmt": nbFltMngmt,
       "nbFltSNMPAgent": nbFltSNMPAgent,
       "nbFltSNMPAgentStatus": nbFltSNMPAgentStatus,
       "nbFltTrapOnAlarm": nbFltTrapOnAlarm,
       "nbFltAgentRunningState": nbFltAgentRunningState,
       "nbFltAlarmTrapFormat": nbFltAlarmTrapFormat,
       "nbFltAlarmSymposiumTrapFormat": nbFltAlarmSymposiumTrapFormat,
       "nbFltAlarmCybeleTrapFormat": nbFltAlarmCybeleTrapFormat,
       "nbFltTrapObjects": nbFltTrapObjects,
       "nbFltAlarmTrapObjects": nbFltAlarmTrapObjects,
       "nbFltAlarmSequence": nbFltAlarmSequence,
       "nbFltAlarmTimeStamp": nbFltAlarmTimeStamp,
       "nbFltAlarmEventCode": nbFltAlarmEventCode,
       "nbFltAlarmEventType": nbFltAlarmEventType,
       "nbFltAlarmEventSeverity": nbFltAlarmEventSeverity,
       "nbFltAlarmTenantID": nbFltAlarmTenantID,
       "nbFltAlarmCustomerID": nbFltAlarmCustomerID,
       "nbFltAlarmOriginator": nbFltAlarmOriginator,
       "nbFltAlarmDescription": nbFltAlarmDescription,
       "nbFltTraps": nbFltTraps,
       "nbSymposiumAlarmTrap": nbSymposiumAlarmTrap}
)
