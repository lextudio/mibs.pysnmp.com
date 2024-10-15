# SNMP MIB module (Wellfleet-RFWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RFWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:00 2024
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

(wfFwallGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFwallGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRFwallGroup_ObjectIdentity = ObjectIdentity
wfRFwallGroup = _WfRFwallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2)
)


class _WfRFwallDelete_Type(Integer32):
    """Custom type wfRFwallDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRFwallDelete_Type.__name__ = "Integer32"
_WfRFwallDelete_Object = MibScalar
wfRFwallDelete = _WfRFwallDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 1),
    _WfRFwallDelete_Type()
)
wfRFwallDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallDelete.setStatus("mandatory")


class _WfRFwallDisable_Type(Integer32):
    """Custom type wfRFwallDisable based on Integer32"""
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


_WfRFwallDisable_Type.__name__ = "Integer32"
_WfRFwallDisable_Object = MibScalar
wfRFwallDisable = _WfRFwallDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 2),
    _WfRFwallDisable_Type()
)
wfRFwallDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallDisable.setStatus("mandatory")


class _WfRFwallState_Type(Integer32):
    """Custom type wfRFwallState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfRFwallState_Type.__name__ = "Integer32"
_WfRFwallState_Object = MibScalar
wfRFwallState = _WfRFwallState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 3),
    _WfRFwallState_Type()
)
wfRFwallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRFwallState.setStatus("mandatory")
_WfRFwallLogHostIp_Type = IpAddress
_WfRFwallLogHostIp_Object = MibScalar
wfRFwallLogHostIp = _WfRFwallLogHostIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 4),
    _WfRFwallLogHostIp_Type()
)
wfRFwallLogHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogHostIp.setStatus("mandatory")
_WfRFwallLogHostIpInt_Type = Integer32
_WfRFwallLogHostIpInt_Object = MibScalar
wfRFwallLogHostIpInt = _WfRFwallLogHostIpInt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 5),
    _WfRFwallLogHostIpInt_Type()
)
wfRFwallLogHostIpInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogHostIpInt.setStatus("obsolete")
_WfRFwallLocalHostIp_Type = IpAddress
_WfRFwallLocalHostIp_Object = MibScalar
wfRFwallLocalHostIp = _WfRFwallLocalHostIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 6),
    _WfRFwallLocalHostIp_Type()
)
wfRFwallLocalHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLocalHostIp.setStatus("mandatory")
_WfRFwallLocalHostIpInt_Type = Integer32
_WfRFwallLocalHostIpInt_Object = MibScalar
wfRFwallLocalHostIpInt = _WfRFwallLocalHostIpInt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 7),
    _WfRFwallLocalHostIpInt_Type()
)
wfRFwallLocalHostIpInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLocalHostIpInt.setStatus("obsolete")


class _WfRFwallVersion_Type(Integer32):
    """Custom type wfRFwallVersion based on Integer32"""
    defaultValue = 1


_WfRFwallVersion_Object = MibScalar
wfRFwallVersion = _WfRFwallVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 8),
    _WfRFwallVersion_Type()
)
wfRFwallVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallVersion.setStatus("mandatory")


class _WfRFwallHmemMin_Type(Integer32):
    """Custom type wfRFwallHmemMin based on Integer32"""
    defaultValue = 50000


_WfRFwallHmemMin_Object = MibScalar
wfRFwallHmemMin = _WfRFwallHmemMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 9),
    _WfRFwallHmemMin_Type()
)
wfRFwallHmemMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallHmemMin.setStatus("mandatory")


class _WfRFwallHmemMax_Type(Integer32):
    """Custom type wfRFwallHmemMax based on Integer32"""
    defaultValue = 100000


_WfRFwallHmemMax_Object = MibScalar
wfRFwallHmemMax = _WfRFwallHmemMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 10),
    _WfRFwallHmemMax_Type()
)
wfRFwallHmemMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallHmemMax.setStatus("mandatory")
_WfRFwallLogHostIpBkp1_Type = IpAddress
_WfRFwallLogHostIpBkp1_Object = MibScalar
wfRFwallLogHostIpBkp1 = _WfRFwallLogHostIpBkp1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 11),
    _WfRFwallLogHostIpBkp1_Type()
)
wfRFwallLogHostIpBkp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogHostIpBkp1.setStatus("mandatory")
_WfRFwallLogHostIpIntBkp1_Type = Integer32
_WfRFwallLogHostIpIntBkp1_Object = MibScalar
wfRFwallLogHostIpIntBkp1 = _WfRFwallLogHostIpIntBkp1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 12),
    _WfRFwallLogHostIpIntBkp1_Type()
)
wfRFwallLogHostIpIntBkp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogHostIpIntBkp1.setStatus("obsolete")
_WfRFwallLogHostIpBkp2_Type = IpAddress
_WfRFwallLogHostIpBkp2_Object = MibScalar
wfRFwallLogHostIpBkp2 = _WfRFwallLogHostIpBkp2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 13),
    _WfRFwallLogHostIpBkp2_Type()
)
wfRFwallLogHostIpBkp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogHostIpBkp2.setStatus("mandatory")
_WfRFwallLogHostIpIntBkp2_Type = Integer32
_WfRFwallLogHostIpIntBkp2_Object = MibScalar
wfRFwallLogHostIpIntBkp2 = _WfRFwallLogHostIpIntBkp2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 14),
    _WfRFwallLogHostIpIntBkp2_Type()
)
wfRFwallLogHostIpIntBkp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogHostIpIntBkp2.setStatus("obsolete")


class _WfRFwallFastPathDisable_Type(Integer32):
    """Custom type wfRFwallFastPathDisable based on Integer32"""
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


_WfRFwallFastPathDisable_Type.__name__ = "Integer32"
_WfRFwallFastPathDisable_Object = MibScalar
wfRFwallFastPathDisable = _WfRFwallFastPathDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 15),
    _WfRFwallFastPathDisable_Type()
)
wfRFwallFastPathDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallFastPathDisable.setStatus("mandatory")


class _WfRFwallFilterTimer_Type(Integer32):
    """Custom type wfRFwallFilterTimer based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 180),
    )


_WfRFwallFilterTimer_Type.__name__ = "Integer32"
_WfRFwallFilterTimer_Object = MibScalar
wfRFwallFilterTimer = _WfRFwallFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 16),
    _WfRFwallFilterTimer_Type()
)
wfRFwallFilterTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallFilterTimer.setStatus("mandatory")


class _WfRFwallLogTimer_Type(Integer32):
    """Custom type wfRFwallLogTimer based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 180),
    )


_WfRFwallLogTimer_Type.__name__ = "Integer32"
_WfRFwallLogTimer_Object = MibScalar
wfRFwallLogTimer = _WfRFwallLogTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 17),
    _WfRFwallLogTimer_Type()
)
wfRFwallLogTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallLogTimer.setStatus("mandatory")


class _WfRFwallKeepaliveTimerIdle_Type(Integer32):
    """Custom type wfRFwallKeepaliveTimerIdle based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WfRFwallKeepaliveTimerIdle_Type.__name__ = "Integer32"
_WfRFwallKeepaliveTimerIdle_Object = MibScalar
wfRFwallKeepaliveTimerIdle = _WfRFwallKeepaliveTimerIdle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 18),
    _WfRFwallKeepaliveTimerIdle_Type()
)
wfRFwallKeepaliveTimerIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallKeepaliveTimerIdle.setStatus("mandatory")


class _WfRFwallKeepaliveTimerRetryTmo_Type(Integer32):
    """Custom type wfRFwallKeepaliveTimerRetryTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WfRFwallKeepaliveTimerRetryTmo_Type.__name__ = "Integer32"
_WfRFwallKeepaliveTimerRetryTmo_Object = MibScalar
wfRFwallKeepaliveTimerRetryTmo = _WfRFwallKeepaliveTimerRetryTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 19),
    _WfRFwallKeepaliveTimerRetryTmo_Type()
)
wfRFwallKeepaliveTimerRetryTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallKeepaliveTimerRetryTmo.setStatus("mandatory")


class _WfRFwallKeepaliveTimerRetries_Type(Integer32):
    """Custom type wfRFwallKeepaliveTimerRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfRFwallKeepaliveTimerRetries_Type.__name__ = "Integer32"
_WfRFwallKeepaliveTimerRetries_Object = MibScalar
wfRFwallKeepaliveTimerRetries = _WfRFwallKeepaliveTimerRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 2, 20),
    _WfRFwallKeepaliveTimerRetries_Type()
)
wfRFwallKeepaliveTimerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRFwallKeepaliveTimerRetries.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RFWALL-MIB",
    **{"wfRFwallGroup": wfRFwallGroup,
       "wfRFwallDelete": wfRFwallDelete,
       "wfRFwallDisable": wfRFwallDisable,
       "wfRFwallState": wfRFwallState,
       "wfRFwallLogHostIp": wfRFwallLogHostIp,
       "wfRFwallLogHostIpInt": wfRFwallLogHostIpInt,
       "wfRFwallLocalHostIp": wfRFwallLocalHostIp,
       "wfRFwallLocalHostIpInt": wfRFwallLocalHostIpInt,
       "wfRFwallVersion": wfRFwallVersion,
       "wfRFwallHmemMin": wfRFwallHmemMin,
       "wfRFwallHmemMax": wfRFwallHmemMax,
       "wfRFwallLogHostIpBkp1": wfRFwallLogHostIpBkp1,
       "wfRFwallLogHostIpIntBkp1": wfRFwallLogHostIpIntBkp1,
       "wfRFwallLogHostIpBkp2": wfRFwallLogHostIpBkp2,
       "wfRFwallLogHostIpIntBkp2": wfRFwallLogHostIpIntBkp2,
       "wfRFwallFastPathDisable": wfRFwallFastPathDisable,
       "wfRFwallFilterTimer": wfRFwallFilterTimer,
       "wfRFwallLogTimer": wfRFwallLogTimer,
       "wfRFwallKeepaliveTimerIdle": wfRFwallKeepaliveTimerIdle,
       "wfRFwallKeepaliveTimerRetryTmo": wfRFwallKeepaliveTimerRetryTmo,
       "wfRFwallKeepaliveTimerRetries": wfRFwallKeepaliveTimerRetries}
)
