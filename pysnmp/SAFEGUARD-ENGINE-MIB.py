# SNMP MIB module (SAFEGUARD-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:20 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swSafeGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSafeGuardGblMgmt_ObjectIdentity = ObjectIdentity
swSafeGuardGblMgmt = _SwSafeGuardGblMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 1)
)


class _SwSafeGuardAdminState_Type(Integer32):
    """Custom type swSafeGuardAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSafeGuardAdminState_Type.__name__ = "Integer32"
_SwSafeGuardAdminState_Object = MibScalar
swSafeGuardAdminState = _SwSafeGuardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 1, 1),
    _SwSafeGuardAdminState_Type()
)
swSafeGuardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardAdminState.setStatus("current")
_SwSafeGuardctrl_ObjectIdentity = ObjectIdentity
swSafeGuardctrl = _SwSafeGuardctrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2)
)


class _SwSafeGuardRisingThreshold_Type(Integer32):
    """Custom type swSafeGuardRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SwSafeGuardRisingThreshold_Type.__name__ = "Integer32"
_SwSafeGuardRisingThreshold_Object = MibScalar
swSafeGuardRisingThreshold = _SwSafeGuardRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 1),
    _SwSafeGuardRisingThreshold_Type()
)
swSafeGuardRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardRisingThreshold.setStatus("current")


class _SwSafeGuardFallingThreshold_Type(Integer32):
    """Custom type swSafeGuardFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SwSafeGuardFallingThreshold_Type.__name__ = "Integer32"
_SwSafeGuardFallingThreshold_Object = MibScalar
swSafeGuardFallingThreshold = _SwSafeGuardFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 2),
    _SwSafeGuardFallingThreshold_Type()
)
swSafeGuardFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardFallingThreshold.setStatus("current")


class _SwSafeGuardAlarmAdminState_Type(Integer32):
    """Custom type swSafeGuardAlarmAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSafeGuardAlarmAdminState_Type.__name__ = "Integer32"
_SwSafeGuardAlarmAdminState_Object = MibScalar
swSafeGuardAlarmAdminState = _SwSafeGuardAlarmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 4),
    _SwSafeGuardAlarmAdminState_Type()
)
swSafeGuardAlarmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardAlarmAdminState.setStatus("current")


class _SwSafeGuardCurrentStatus_Type(Integer32):
    """Custom type swSafeGuardCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exhausted", 2),
          ("normal", 1))
    )


_SwSafeGuardCurrentStatus_Type.__name__ = "Integer32"
_SwSafeGuardCurrentStatus_Object = MibScalar
swSafeGuardCurrentStatus = _SwSafeGuardCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 5),
    _SwSafeGuardCurrentStatus_Type()
)
swSafeGuardCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSafeGuardCurrentStatus.setStatus("current")


class _SwSafeGuardInterval_Type(Integer32):
    """Custom type swSafeGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwSafeGuardInterval_Type.__name__ = "Integer32"
_SwSafeGuardInterval_Object = MibScalar
swSafeGuardInterval = _SwSafeGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 6),
    _SwSafeGuardInterval_Type()
)
swSafeGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSafeGuardInterval.setStatus("current")
_SwSafeGuardNotify_ObjectIdentity = ObjectIdentity
swSafeGuardNotify = _SwSafeGuardNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4)
)
_SwSafeGuardNotification_ObjectIdentity = ObjectIdentity
swSafeGuardNotification = _SwSafeGuardNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1)
)
_SwSafeGuardNotifyPrefix_ObjectIdentity = ObjectIdentity
swSafeGuardNotifyPrefix = _SwSafeGuardNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0)
)

# Managed Objects groups


# Notification objects

swSafeGuardChgToExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0, 1)
)
swSafeGuardChgToExhausted.setObjects(
    ("SAFEGUARD-ENGINE-MIB", "swSafeGuardCurrentStatus")
)
if mibBuilder.loadTexts:
    swSafeGuardChgToExhausted.setStatus(
        "current"
    )

swSafeGuardChgToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0, 2)
)
swSafeGuardChgToNormal.setObjects(
    ("SAFEGUARD-ENGINE-MIB", "swSafeGuardCurrentStatus")
)
if mibBuilder.loadTexts:
    swSafeGuardChgToNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAFEGUARD-ENGINE-MIB",
    **{"swSafeGuardMIB": swSafeGuardMIB,
       "swSafeGuardGblMgmt": swSafeGuardGblMgmt,
       "swSafeGuardAdminState": swSafeGuardAdminState,
       "swSafeGuardctrl": swSafeGuardctrl,
       "swSafeGuardRisingThreshold": swSafeGuardRisingThreshold,
       "swSafeGuardFallingThreshold": swSafeGuardFallingThreshold,
       "swSafeGuardAlarmAdminState": swSafeGuardAlarmAdminState,
       "swSafeGuardCurrentStatus": swSafeGuardCurrentStatus,
       "swSafeGuardInterval": swSafeGuardInterval,
       "swSafeGuardNotify": swSafeGuardNotify,
       "swSafeGuardNotification": swSafeGuardNotification,
       "swSafeGuardNotifyPrefix": swSafeGuardNotifyPrefix,
       "swSafeGuardChgToExhausted": swSafeGuardChgToExhausted,
       "swSafeGuardChgToNormal": swSafeGuardChgToNormal}
)
