# SNMP MIB module (CISCO-BITS-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BITS-CLOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:19 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoBitsClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 459)
)
ciscoBitsClockMIB.setRevisions(
        ("2005-01-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBitsClockMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoBitsClockMIBNotifs = _CiscoBitsClockMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 0)
)
_CiscoBitsClockMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBitsClockMIBObjects = _CiscoBitsClockMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1)
)
_CBitsClkSourceTable_Object = MibTable
cBitsClkSourceTable = _CBitsClkSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1)
)
if mibBuilder.loadTexts:
    cBitsClkSourceTable.setStatus("current")
_CBitsClkSourceEntry_Object = MibTableRow
cBitsClkSourceEntry = _CBitsClkSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1)
)
cBitsClkSourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cBitsClkSourceEntry.setStatus("current")


class _CBitsClkSourceRoleAdmin_Type(Integer32):
    """Custom type cBitsClkSourceRoleAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_CBitsClkSourceRoleAdmin_Type.__name__ = "Integer32"
_CBitsClkSourceRoleAdmin_Object = MibTableColumn
cBitsClkSourceRoleAdmin = _CBitsClkSourceRoleAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1, 1),
    _CBitsClkSourceRoleAdmin_Type()
)
cBitsClkSourceRoleAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBitsClkSourceRoleAdmin.setStatus("current")


class _CBitsClkSourceRoleCurrent_Type(Integer32):
    """Custom type cBitsClkSourceRoleCurrent based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3),
          ("unavailable", 0))
    )


_CBitsClkSourceRoleCurrent_Type.__name__ = "Integer32"
_CBitsClkSourceRoleCurrent_Object = MibTableColumn
cBitsClkSourceRoleCurrent = _CBitsClkSourceRoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1, 2),
    _CBitsClkSourceRoleCurrent_Type()
)
cBitsClkSourceRoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBitsClkSourceRoleCurrent.setStatus("current")
_CBitsClkSourceTimestamp_Type = TimeStamp
_CBitsClkSourceTimestamp_Object = MibTableColumn
cBitsClkSourceTimestamp = _CBitsClkSourceTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1, 3),
    _CBitsClkSourceTimestamp_Type()
)
cBitsClkSourceTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBitsClkSourceTimestamp.setStatus("current")
_CBitsClkSourceActiveSeconds_Type = Counter32
_CBitsClkSourceActiveSeconds_Object = MibTableColumn
cBitsClkSourceActiveSeconds = _CBitsClkSourceActiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1, 4),
    _CBitsClkSourceActiveSeconds_Type()
)
cBitsClkSourceActiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBitsClkSourceActiveSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cBitsClkSourceActiveSeconds.setUnits("seconds")
_CBitsClkSourceInactiveSeconds_Type = Counter32
_CBitsClkSourceInactiveSeconds_Object = MibTableColumn
cBitsClkSourceInactiveSeconds = _CBitsClkSourceInactiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1, 5),
    _CBitsClkSourceInactiveSeconds_Type()
)
cBitsClkSourceInactiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBitsClkSourceInactiveSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cBitsClkSourceInactiveSeconds.setUnits("seconds")
_CBitsClkSourceDescription_Type = SnmpAdminString
_CBitsClkSourceDescription_Object = MibTableColumn
cBitsClkSourceDescription = _CBitsClkSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 1, 1, 6),
    _CBitsClkSourceDescription_Type()
)
cBitsClkSourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBitsClkSourceDescription.setStatus("current")


class _CBitsClkNotifEnabled_Type(TruthValue):
    """Custom type cBitsClkNotifEnabled based on TruthValue"""


_CBitsClkNotifEnabled_Object = MibScalar
cBitsClkNotifEnabled = _CBitsClkNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 1, 2),
    _CBitsClkNotifEnabled_Type()
)
cBitsClkNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cBitsClkNotifEnabled.setStatus("current")
_CiscoBitsClockMIBConform_ObjectIdentity = ObjectIdentity
ciscoBitsClockMIBConform = _CiscoBitsClockMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 2)
)
_CiscoBitsClockMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBitsClockMIBCompliances = _CiscoBitsClockMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 2, 1)
)
_CiscoBitsClockMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBitsClockMIBGroups = _CiscoBitsClockMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 2, 2)
)

# Managed Objects groups

ciscoBitsClockSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 2, 2, 1)
)
ciscoBitsClockSourceGroup.setObjects(
      *(("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceRoleAdmin"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceRoleCurrent"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceTimestamp"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceActiveSeconds"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceInactiveSeconds"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceDescription"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoBitsClockSourceGroup.setStatus("current")


# Notification objects

ciscoBitsClockSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 0, 1)
)
ciscoBitsClockSource.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceDescription"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceRoleAdmin"),
        ("CISCO-BITS-CLOCK-MIB", "cBitsClkSourceRoleCurrent"))
)
if mibBuilder.loadTexts:
    ciscoBitsClockSource.setStatus(
        "current"
    )

ciscoBitsClockFreerun = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 0, 2)
)
ciscoBitsClockFreerun.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    ciscoBitsClockFreerun.setStatus(
        "current"
    )

ciscoBitsClockHoldover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 0, 3)
)
ciscoBitsClockHoldover.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    ciscoBitsClockHoldover.setStatus(
        "current"
    )


# Notifications groups

ciscoBitsClockNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 2, 2, 2)
)
ciscoBitsClockNotifGroup.setObjects(
      *(("CISCO-BITS-CLOCK-MIB", "ciscoBitsClockSource"),
        ("CISCO-BITS-CLOCK-MIB", "ciscoBitsClockFreerun"),
        ("CISCO-BITS-CLOCK-MIB", "ciscoBitsClockHoldover"))
)
if mibBuilder.loadTexts:
    ciscoBitsClockNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBitsClockMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 459, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBitsClockMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BITS-CLOCK-MIB",
    **{"ciscoBitsClockMIB": ciscoBitsClockMIB,
       "ciscoBitsClockMIBNotifs": ciscoBitsClockMIBNotifs,
       "ciscoBitsClockSource": ciscoBitsClockSource,
       "ciscoBitsClockFreerun": ciscoBitsClockFreerun,
       "ciscoBitsClockHoldover": ciscoBitsClockHoldover,
       "ciscoBitsClockMIBObjects": ciscoBitsClockMIBObjects,
       "cBitsClkSourceTable": cBitsClkSourceTable,
       "cBitsClkSourceEntry": cBitsClkSourceEntry,
       "cBitsClkSourceRoleAdmin": cBitsClkSourceRoleAdmin,
       "cBitsClkSourceRoleCurrent": cBitsClkSourceRoleCurrent,
       "cBitsClkSourceTimestamp": cBitsClkSourceTimestamp,
       "cBitsClkSourceActiveSeconds": cBitsClkSourceActiveSeconds,
       "cBitsClkSourceInactiveSeconds": cBitsClkSourceInactiveSeconds,
       "cBitsClkSourceDescription": cBitsClkSourceDescription,
       "cBitsClkNotifEnabled": cBitsClkNotifEnabled,
       "ciscoBitsClockMIBConform": ciscoBitsClockMIBConform,
       "ciscoBitsClockMIBCompliances": ciscoBitsClockMIBCompliances,
       "ciscoBitsClockMIBCompliance": ciscoBitsClockMIBCompliance,
       "ciscoBitsClockMIBGroups": ciscoBitsClockMIBGroups,
       "ciscoBitsClockSourceGroup": ciscoBitsClockSourceGroup,
       "ciscoBitsClockNotifGroup": ciscoBitsClockNotifGroup}
)
