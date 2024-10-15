# SNMP MIB module (DLINK-3100-SAFE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-SAFE-GUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:17 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSafeGuard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131)
)
rlSafeGuard.setRevisions(
        ("2007-11-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlSafeGuardEnabled_Type(TruthValue):
    """Custom type rlSafeGuardEnabled based on TruthValue"""


_RlSafeGuardEnabled_Object = MibScalar
rlSafeGuardEnabled = _RlSafeGuardEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 1),
    _RlSafeGuardEnabled_Type()
)
rlSafeGuardEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSafeGuardEnabled.setStatus("current")


class _RlSafeGuardStatus_Type(Integer32):
    """Custom type rlSafeGuardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("attack", 1),
          ("idle", 0))
    )


_RlSafeGuardStatus_Type.__name__ = "Integer32"
_RlSafeGuardStatus_Object = MibScalar
rlSafeGuardStatus = _RlSafeGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 2),
    _RlSafeGuardStatus_Type()
)
rlSafeGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSafeGuardStatus.setStatus("current")


class _RlSafeGuardCpuUtilizationUpper_Type(Integer32):
    """Custom type rlSafeGuardCpuUtilizationUpper based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RlSafeGuardCpuUtilizationUpper_Type.__name__ = "Integer32"
_RlSafeGuardCpuUtilizationUpper_Object = MibScalar
rlSafeGuardCpuUtilizationUpper = _RlSafeGuardCpuUtilizationUpper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 3),
    _RlSafeGuardCpuUtilizationUpper_Type()
)
rlSafeGuardCpuUtilizationUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSafeGuardCpuUtilizationUpper.setStatus("current")


class _RlSafeGuardCpuUtilizationLower_Type(Integer32):
    """Custom type rlSafeGuardCpuUtilizationLower based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RlSafeGuardCpuUtilizationLower_Type.__name__ = "Integer32"
_RlSafeGuardCpuUtilizationLower_Object = MibScalar
rlSafeGuardCpuUtilizationLower = _RlSafeGuardCpuUtilizationLower_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 4),
    _RlSafeGuardCpuUtilizationLower_Type()
)
rlSafeGuardCpuUtilizationLower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSafeGuardCpuUtilizationLower.setStatus("current")


class _RlSafeGuardBroadcastRateUpper_Type(Integer32):
    """Custom type rlSafeGuardBroadcastRateUpper based on Integer32"""
    defaultValue = 350

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 1000),
    )


_RlSafeGuardBroadcastRateUpper_Type.__name__ = "Integer32"
_RlSafeGuardBroadcastRateUpper_Object = MibScalar
rlSafeGuardBroadcastRateUpper = _RlSafeGuardBroadcastRateUpper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 5),
    _RlSafeGuardBroadcastRateUpper_Type()
)
rlSafeGuardBroadcastRateUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSafeGuardBroadcastRateUpper.setStatus("current")


class _RlSafeGuardBroadcastRateLower_Type(Integer32):
    """Custom type rlSafeGuardBroadcastRateLower based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 1000),
    )


_RlSafeGuardBroadcastRateLower_Type.__name__ = "Integer32"
_RlSafeGuardBroadcastRateLower_Object = MibScalar
rlSafeGuardBroadcastRateLower = _RlSafeGuardBroadcastRateLower_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 6),
    _RlSafeGuardBroadcastRateLower_Type()
)
rlSafeGuardBroadcastRateLower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSafeGuardBroadcastRateLower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-SAFE-GUARD-MIB",
    **{"rlSafeGuard": rlSafeGuard,
       "rlSafeGuardEnabled": rlSafeGuardEnabled,
       "rlSafeGuardStatus": rlSafeGuardStatus,
       "rlSafeGuardCpuUtilizationUpper": rlSafeGuardCpuUtilizationUpper,
       "rlSafeGuardCpuUtilizationLower": rlSafeGuardCpuUtilizationLower,
       "rlSafeGuardBroadcastRateUpper": rlSafeGuardBroadcastRateUpper,
       "rlSafeGuardBroadcastRateLower": rlSafeGuardBroadcastRateLower}
)
