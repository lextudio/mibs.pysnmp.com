# SNMP MIB module (APPIAN-TRUNK-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-TRUNK-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:48 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 acTrunks) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "acTrunks")

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

acTrunksPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4)
)
acTrunksPrivate.setRevisions(
        ("1900-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcTrunkPrivateTraps_ObjectIdentity = ObjectIdentity
acTrunkPrivateTraps = _AcTrunkPrivateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 0)
)
_AcTrunkPrivateTable_Object = MibTable
acTrunkPrivateTable = _AcTrunkPrivateTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    acTrunkPrivateTable.setStatus("current")
_AcTrunkPrivateEntry_Object = MibTableRow
acTrunkPrivateEntry = _AcTrunkPrivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1)
)
acTrunkPrivateEntry.setIndexNames(
    (0, "APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateNodeId"),
    (0, "APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateIndex"),
)
if mibBuilder.loadTexts:
    acTrunkPrivateEntry.setStatus("current")
_AcTrunkPrivateNodeId_Type = AcNodeId
_AcTrunkPrivateNodeId_Object = MibTableColumn
acTrunkPrivateNodeId = _AcTrunkPrivateNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 1),
    _AcTrunkPrivateNodeId_Type()
)
acTrunkPrivateNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrunkPrivateNodeId.setStatus("current")
_AcTrunkPrivateIndex_Type = Integer32
_AcTrunkPrivateIndex_Object = MibTableColumn
acTrunkPrivateIndex = _AcTrunkPrivateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 2),
    _AcTrunkPrivateIndex_Type()
)
acTrunkPrivateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrunkPrivateIndex.setStatus("current")


class _AcTrunkPrivateAdminStatus_Type(AcAdminStatus):
    """Custom type acTrunkPrivateAdminStatus based on AcAdminStatus"""


_AcTrunkPrivateAdminStatus_Object = MibTableColumn
acTrunkPrivateAdminStatus = _AcTrunkPrivateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 3),
    _AcTrunkPrivateAdminStatus_Type()
)
acTrunkPrivateAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrunkPrivateAdminStatus.setStatus("current")
_AcTrunkPrivateOpStatus_Type = AcOpStatus
_AcTrunkPrivateOpStatus_Object = MibTableColumn
acTrunkPrivateOpStatus = _AcTrunkPrivateOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 4),
    _AcTrunkPrivateOpStatus_Type()
)
acTrunkPrivateOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkPrivateOpStatus.setStatus("current")


class _AcTrunkPrivateDetailStatus_Type(DisplayString):
    """Custom type acTrunkPrivateDetailStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcTrunkPrivateDetailStatus_Type.__name__ = "DisplayString"
_AcTrunkPrivateDetailStatus_Object = MibTableColumn
acTrunkPrivateDetailStatus = _AcTrunkPrivateDetailStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 5),
    _AcTrunkPrivateDetailStatus_Type()
)
acTrunkPrivateDetailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkPrivateDetailStatus.setStatus("current")

# Managed Objects groups


# Notification objects

acTrunkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 0, 1)
)
acTrunkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateNodeId"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateIndex"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateOpStatus"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateDetailStatus"))
)
if mibBuilder.loadTexts:
    acTrunkUpTrap.setStatus(
        "current"
    )

acTrunkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 0, 2)
)
acTrunkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateNodeId"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateIndex"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateOpStatus"),
        ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateDetailStatus"))
)
if mibBuilder.loadTexts:
    acTrunkDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-TRUNK-PRIVATE-MIB",
    **{"acTrunksPrivate": acTrunksPrivate,
       "acTrunkPrivateTraps": acTrunkPrivateTraps,
       "acTrunkUpTrap": acTrunkUpTrap,
       "acTrunkDownTrap": acTrunkDownTrap,
       "acTrunkPrivateTable": acTrunkPrivateTable,
       "acTrunkPrivateEntry": acTrunkPrivateEntry,
       "acTrunkPrivateNodeId": acTrunkPrivateNodeId,
       "acTrunkPrivateIndex": acTrunkPrivateIndex,
       "acTrunkPrivateAdminStatus": acTrunkPrivateAdminStatus,
       "acTrunkPrivateOpStatus": acTrunkPrivateOpStatus,
       "acTrunkPrivateDetailStatus": acTrunkPrivateDetailStatus}
)
