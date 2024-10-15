# SNMP MIB module (ELTEX-ULD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-ULD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:20 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

eltexULDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexULDNotifications_ObjectIdentity = ObjectIdentity
eltexULDNotifications = _EltexULDNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 34, 0)
)
_EltexULDMgmt_ObjectIdentity = ObjectIdentity
eltexULDMgmt = _EltexULDMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1)
)
_EltexULDTable_Object = MibTable
eltexULDTable = _EltexULDTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1)
)
if mibBuilder.loadTexts:
    eltexULDTable.setStatus("current")
_EltexULDEntry_Object = MibTableRow
eltexULDEntry = _EltexULDEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1)
)
eltexULDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltexULDEntry.setStatus("current")


class _EltexULDAdminState_Type(Integer32):
    """Custom type eltexULDAdminState based on Integer32"""
    defaultValue = 2

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


_EltexULDAdminState_Type.__name__ = "Integer32"
_EltexULDAdminState_Object = MibTableColumn
eltexULDAdminState = _EltexULDAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 1),
    _EltexULDAdminState_Type()
)
eltexULDAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDAdminState.setStatus("current")


class _EltexULDOperStatus_Type(Integer32):
    """Custom type eltexULDOperStatus based on Integer32"""
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


_EltexULDOperStatus_Type.__name__ = "Integer32"
_EltexULDOperStatus_Object = MibTableColumn
eltexULDOperStatus = _EltexULDOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 2),
    _EltexULDOperStatus_Type()
)
eltexULDOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexULDOperStatus.setStatus("current")


class _EltexULDMode_Type(Integer32):
    """Custom type eltexULDMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("err-disable", 2),
          ("log", 1))
    )


_EltexULDMode_Type.__name__ = "Integer32"
_EltexULDMode_Object = MibTableColumn
eltexULDMode = _EltexULDMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 3),
    _EltexULDMode_Type()
)
eltexULDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDMode.setStatus("current")


class _EltexULDDiscoveryTime_Type(Integer32):
    """Custom type eltexULDDiscoveryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_EltexULDDiscoveryTime_Type.__name__ = "Integer32"
_EltexULDDiscoveryTime_Object = MibTableColumn
eltexULDDiscoveryTime = _EltexULDDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 4),
    _EltexULDDiscoveryTime_Type()
)
eltexULDDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDDiscoveryTime.setStatus("current")


class _EltexULDIsAggressive_Type(TruthValue):
    """Custom type eltexULDIsAggressive based on TruthValue"""


_EltexULDIsAggressive_Object = MibTableColumn
eltexULDIsAggressive = _EltexULDIsAggressive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 5),
    _EltexULDIsAggressive_Type()
)
eltexULDIsAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexULDIsAggressive.setStatus("current")


class _EltexULDLinkStatus_Type(Integer32):
    """Custom type eltexULDLinkStatus based on Integer32"""
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
        *(("bidirectional", 3),
          ("neighbor-mismatch", 5),
          ("tx-rx-loop", 4),
          ("unidirectional", 2),
          ("unknown", 1))
    )


_EltexULDLinkStatus_Type.__name__ = "Integer32"
_EltexULDLinkStatus_Object = MibTableColumn
eltexULDLinkStatus = _EltexULDLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 6),
    _EltexULDLinkStatus_Type()
)
eltexULDLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexULDLinkStatus.setStatus("current")

# Managed Objects groups


# Notification objects

eltexULDLinkStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 34, 0, 1)
)
eltexULDLinkStatusChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ELTEX-ULD-MIB", "eltexULDLinkStatus"))
)
if mibBuilder.loadTexts:
    eltexULDLinkStatusChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-ULD-MIB",
    **{"eltexULDMIB": eltexULDMIB,
       "eltexULDNotifications": eltexULDNotifications,
       "eltexULDLinkStatusChanged": eltexULDLinkStatusChanged,
       "eltexULDMgmt": eltexULDMgmt,
       "eltexULDTable": eltexULDTable,
       "eltexULDEntry": eltexULDEntry,
       "eltexULDAdminState": eltexULDAdminState,
       "eltexULDOperStatus": eltexULDOperStatus,
       "eltexULDMode": eltexULDMode,
       "eltexULDDiscoveryTime": eltexULDDiscoveryTime,
       "eltexULDIsAggressive": eltexULDIsAggressive,
       "eltexULDLinkStatus": eltexULDLinkStatus}
)
