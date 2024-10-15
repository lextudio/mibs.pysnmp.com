# SNMP MIB module (ELTEX-MES-ULD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-ULD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:05 2024
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

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

eltMesULDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87)
)
eltMesULDMIB.setRevisions(
        ("2015-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesULDNotifications_ObjectIdentity = ObjectIdentity
eltMesULDNotifications = _EltMesULDNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 0)
)
_EltMesULDMgmt_ObjectIdentity = ObjectIdentity
eltMesULDMgmt = _EltMesULDMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1)
)
_EltULDTable_Object = MibTable
eltULDTable = _EltULDTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1)
)
if mibBuilder.loadTexts:
    eltULDTable.setStatus("deprecated")
_EltULDEntry_Object = MibTableRow
eltULDEntry = _EltULDEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1)
)
eltULDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltULDEntry.setStatus("deprecated")


class _EltULDAdminState_Type(Integer32):
    """Custom type eltULDAdminState based on Integer32"""
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


_EltULDAdminState_Type.__name__ = "Integer32"
_EltULDAdminState_Object = MibTableColumn
eltULDAdminState = _EltULDAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1, 1),
    _EltULDAdminState_Type()
)
eltULDAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltULDAdminState.setStatus("deprecated")


class _EltULDOperStatus_Type(Integer32):
    """Custom type eltULDOperStatus based on Integer32"""
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


_EltULDOperStatus_Type.__name__ = "Integer32"
_EltULDOperStatus_Object = MibTableColumn
eltULDOperStatus = _EltULDOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1, 2),
    _EltULDOperStatus_Type()
)
eltULDOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltULDOperStatus.setStatus("deprecated")


class _EltULDMode_Type(Integer32):
    """Custom type eltULDMode based on Integer32"""
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


_EltULDMode_Type.__name__ = "Integer32"
_EltULDMode_Object = MibTableColumn
eltULDMode = _EltULDMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1, 3),
    _EltULDMode_Type()
)
eltULDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltULDMode.setStatus("deprecated")


class _EltULDDiscoveryTime_Type(Integer32):
    """Custom type eltULDDiscoveryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_EltULDDiscoveryTime_Type.__name__ = "Integer32"
_EltULDDiscoveryTime_Object = MibTableColumn
eltULDDiscoveryTime = _EltULDDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1, 4),
    _EltULDDiscoveryTime_Type()
)
eltULDDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltULDDiscoveryTime.setStatus("deprecated")


class _EltULDIsAggressive_Type(TruthValue):
    """Custom type eltULDIsAggressive based on TruthValue"""


_EltULDIsAggressive_Object = MibTableColumn
eltULDIsAggressive = _EltULDIsAggressive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1, 5),
    _EltULDIsAggressive_Type()
)
eltULDIsAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltULDIsAggressive.setStatus("deprecated")


class _EltULDLinkStatus_Type(Integer32):
    """Custom type eltULDLinkStatus based on Integer32"""
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


_EltULDLinkStatus_Type.__name__ = "Integer32"
_EltULDLinkStatus_Object = MibTableColumn
eltULDLinkStatus = _EltULDLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 1, 1, 1, 6),
    _EltULDLinkStatus_Type()
)
eltULDLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltULDLinkStatus.setStatus("deprecated")

# Managed Objects groups


# Notification objects

eltULDLinkStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 87, 0, 1)
)
eltULDLinkStatusChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ELTEX-MES-ULD-MIB", "eltULDLinkStatus"))
)
if mibBuilder.loadTexts:
    eltULDLinkStatusChanged.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ULD-MIB",
    **{"eltMesULDMIB": eltMesULDMIB,
       "eltMesULDNotifications": eltMesULDNotifications,
       "eltULDLinkStatusChanged": eltULDLinkStatusChanged,
       "eltMesULDMgmt": eltMesULDMgmt,
       "eltULDTable": eltULDTable,
       "eltULDEntry": eltULDEntry,
       "eltULDAdminState": eltULDAdminState,
       "eltULDOperStatus": eltULDOperStatus,
       "eltULDMode": eltULDMode,
       "eltULDDiscoveryTime": eltULDDiscoveryTime,
       "eltULDIsAggressive": eltULDIsAggressive,
       "eltULDLinkStatus": eltULDLinkStatus}
)
