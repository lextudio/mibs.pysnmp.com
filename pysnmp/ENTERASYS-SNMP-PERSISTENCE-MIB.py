# SNMP MIB module (ENTERASYS-SNMP-PERSISTENCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-SNMP-PERSISTENCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:34 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysSnmpPersistenceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24)
)
etsysSnmpPersistenceMIB.setRevisions(
        ("2002-09-09 20:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysSnmpPersistenceObjects_ObjectIdentity = ObjectIdentity
etsysSnmpPersistenceObjects = _EtsysSnmpPersistenceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1)
)


class _EtsysSnmpPersistenceMode_Type(Integer32):
    """Custom type etsysSnmpPersistenceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pushButtonSave", 2),
          ("snmpNormalSave", 1),
          ("timeDelayedSave", 3))
    )


_EtsysSnmpPersistenceMode_Type.__name__ = "Integer32"
_EtsysSnmpPersistenceMode_Object = MibScalar
etsysSnmpPersistenceMode = _EtsysSnmpPersistenceMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 1),
    _EtsysSnmpPersistenceMode_Type()
)
etsysSnmpPersistenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSnmpPersistenceMode.setStatus("current")


class _EtsysSnmpPersistenceSave_Type(Integer32):
    """Custom type etsysSnmpPersistenceSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nop", 1),
          ("save", 2))
    )


_EtsysSnmpPersistenceSave_Type.__name__ = "Integer32"
_EtsysSnmpPersistenceSave_Object = MibScalar
etsysSnmpPersistenceSave = _EtsysSnmpPersistenceSave_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 2),
    _EtsysSnmpPersistenceSave_Type()
)
etsysSnmpPersistenceSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSnmpPersistenceSave.setStatus("current")


class _EtsysSnmpPersistenceStatus_Type(Integer32):
    """Custom type etsysSnmpPersistenceStatus based on Integer32"""
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
        *(("other", 1),
          ("saveFailed", 5),
          ("saveSucceeded", 4),
          ("savingChanges", 3),
          ("unsavedChanges", 2))
    )


_EtsysSnmpPersistenceStatus_Type.__name__ = "Integer32"
_EtsysSnmpPersistenceStatus_Object = MibScalar
etsysSnmpPersistenceStatus = _EtsysSnmpPersistenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 3),
    _EtsysSnmpPersistenceStatus_Type()
)
etsysSnmpPersistenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSnmpPersistenceStatus.setStatus("current")
_EtsysSnmpPersistenceStatusTime_Type = TimeTicks
_EtsysSnmpPersistenceStatusTime_Object = MibScalar
etsysSnmpPersistenceStatusTime = _EtsysSnmpPersistenceStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 4),
    _EtsysSnmpPersistenceStatusTime_Type()
)
etsysSnmpPersistenceStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSnmpPersistenceStatusTime.setStatus("current")
_EtsysSnmpPersistenceError_Type = SnmpAdminString
_EtsysSnmpPersistenceError_Object = MibScalar
etsysSnmpPersistenceError = _EtsysSnmpPersistenceError_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 5),
    _EtsysSnmpPersistenceError_Type()
)
etsysSnmpPersistenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSnmpPersistenceError.setStatus("current")
_EtsysSnmpPersistenceErrorTime_Type = DateAndTime
_EtsysSnmpPersistenceErrorTime_Object = MibScalar
etsysSnmpPersistenceErrorTime = _EtsysSnmpPersistenceErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 6),
    _EtsysSnmpPersistenceErrorTime_Type()
)
etsysSnmpPersistenceErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSnmpPersistenceErrorTime.setStatus("current")
_EtsysSnmpPersistenceConformance_ObjectIdentity = ObjectIdentity
etsysSnmpPersistenceConformance = _EtsysSnmpPersistenceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2)
)
_EtsysSnmpPersistenceGroups_ObjectIdentity = ObjectIdentity
etsysSnmpPersistenceGroups = _EtsysSnmpPersistenceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 1)
)
_EtsysSnmpPersistenceCompliances_ObjectIdentity = ObjectIdentity
etsysSnmpPersistenceCompliances = _EtsysSnmpPersistenceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 2)
)

# Managed Objects groups

etsysSnmpPersistenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 1, 1)
)
etsysSnmpPersistenceGroup.setObjects(
      *(("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceMode"),
        ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceSave"),
        ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceStatus"),
        ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceStatusTime"),
        ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceError"),
        ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceErrorTime"))
)
if mibBuilder.loadTexts:
    etsysSnmpPersistenceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysSnmpPersistenceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysSnmpPersistenceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SNMP-PERSISTENCE-MIB",
    **{"etsysSnmpPersistenceMIB": etsysSnmpPersistenceMIB,
       "etsysSnmpPersistenceObjects": etsysSnmpPersistenceObjects,
       "etsysSnmpPersistenceMode": etsysSnmpPersistenceMode,
       "etsysSnmpPersistenceSave": etsysSnmpPersistenceSave,
       "etsysSnmpPersistenceStatus": etsysSnmpPersistenceStatus,
       "etsysSnmpPersistenceStatusTime": etsysSnmpPersistenceStatusTime,
       "etsysSnmpPersistenceError": etsysSnmpPersistenceError,
       "etsysSnmpPersistenceErrorTime": etsysSnmpPersistenceErrorTime,
       "etsysSnmpPersistenceConformance": etsysSnmpPersistenceConformance,
       "etsysSnmpPersistenceGroups": etsysSnmpPersistenceGroups,
       "etsysSnmpPersistenceGroup": etsysSnmpPersistenceGroup,
       "etsysSnmpPersistenceCompliances": etsysSnmpPersistenceCompliances,
       "etsysSnmpPersistenceCompliance": etsysSnmpPersistenceCompliance}
)
