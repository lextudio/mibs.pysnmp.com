# SNMP MIB module (NLS-BBNSTATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NLS-BBNSTATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:33 2024
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

(bbnState,) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "bbnState")

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



class _UnitAdministrativeState_Type(Integer32):
    """Custom type unitAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )


_UnitAdministrativeState_Type.__name__ = "Integer32"
_UnitAdministrativeState_Object = MibScalar
unitAdministrativeState = _UnitAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 1),
    _UnitAdministrativeState_Type()
)
unitAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitAdministrativeState.setStatus("mandatory")


class _UnitOperationalState_Type(Integer32):
    """Custom type unitOperationalState based on Integer32"""
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


_UnitOperationalState_Type.__name__ = "Integer32"
_UnitOperationalState_Object = MibScalar
unitOperationalState = _UnitOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 2),
    _UnitOperationalState_Type()
)
unitOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOperationalState.setStatus("mandatory")


class _UnitUsageState_Type(Integer32):
    """Custom type unitUsageState based on Integer32"""
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
          ("busy", 3),
          ("idle", 1))
    )


_UnitUsageState_Type.__name__ = "Integer32"
_UnitUsageState_Object = MibScalar
unitUsageState = _UnitUsageState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 3),
    _UnitUsageState_Type()
)
unitUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitUsageState.setStatus("mandatory")


class _UnitProceduralStatus_Type(Integer32):
    """Custom type unitProceduralStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("initializationRequired", 1),
          ("initializing", 3),
          ("notInitialized", 2),
          ("ready", 6),
          ("reporting", 4),
          ("terminating", 5))
    )


_UnitProceduralStatus_Type.__name__ = "Integer32"
_UnitProceduralStatus_Object = MibScalar
unitProceduralStatus = _UnitProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 4),
    _UnitProceduralStatus_Type()
)
unitProceduralStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitProceduralStatus.setStatus("mandatory")


class _UnitAlarmStatus_Type(Integer32):
    """Custom type unitAlarmStatus based on Integer32"""
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
        *(("alarmOutstanding", 8),
          ("critical", 6),
          ("idle", 9),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("underRepair", 7),
          ("undetermined", 2),
          ("warning", 3))
    )


_UnitAlarmStatus_Type.__name__ = "Integer32"
_UnitAlarmStatus_Object = MibScalar
unitAlarmStatus = _UnitAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 5),
    _UnitAlarmStatus_Type()
)
unitAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitAlarmStatus.setStatus("mandatory")


class _UnitAvailabilityStatus_Type(Integer32):
    """Custom type unitAvailabilityStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("available", 10),
          ("degraded", 7),
          ("dependency", 6),
          ("failed", 2),
          ("inTest", 1),
          ("logFull", 9),
          ("notInstalled", 8),
          ("offDuty", 5),
          ("offLine", 4),
          ("powerOff", 3))
    )


_UnitAvailabilityStatus_Type.__name__ = "Integer32"
_UnitAvailabilityStatus_Object = MibScalar
unitAvailabilityStatus = _UnitAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 6),
    _UnitAvailabilityStatus_Type()
)
unitAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAvailabilityStatus.setStatus("mandatory")


class _UnitControlStatus_Type(Integer32):
    """Custom type unitControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("free", 4),
          ("partLocked", 1),
          ("reservedToTest", 2),
          ("subjectToTest", 32767),
          ("suspended", 3))
    )


_UnitControlStatus_Type.__name__ = "Integer32"
_UnitControlStatus_Object = MibScalar
unitControlStatus = _UnitControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 7),
    _UnitControlStatus_Type()
)
unitControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitControlStatus.setStatus("mandatory")


class _UnitStandbyStatus_Type(Integer32):
    """Custom type unitStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 2),
          ("hotStandby", 1),
          ("providingService", 3))
    )


_UnitStandbyStatus_Type.__name__ = "Integer32"
_UnitStandbyStatus_Object = MibScalar
unitStandbyStatus = _UnitStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 8),
    _UnitStandbyStatus_Type()
)
unitStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitStandbyStatus.setStatus("mandatory")


class _UnitUnknownStatus_Type(Integer32):
    """Custom type unitUnknownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_UnitUnknownStatus_Type.__name__ = "Integer32"
_UnitUnknownStatus_Object = MibScalar
unitUnknownStatus = _UnitUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2, 9),
    _UnitUnknownStatus_Type()
)
unitUnknownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitUnknownStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NLS-BBNSTATE-MIB",
    **{"unitAdministrativeState": unitAdministrativeState,
       "unitOperationalState": unitOperationalState,
       "unitUsageState": unitUsageState,
       "unitProceduralStatus": unitProceduralStatus,
       "unitAlarmStatus": unitAlarmStatus,
       "unitAvailabilityStatus": unitAvailabilityStatus,
       "unitControlStatus": unitControlStatus,
       "unitStandbyStatus": unitStandbyStatus,
       "unitUnknownStatus": unitUnknownStatus}
)
