# SNMP MIB module (MPLS-LSR-EXT-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:19 2024
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

(mplsInSegmentGroup,
 mplsInterfaceGroup,
 mplsLsrNotificationGroup,
 mplsOutSegmentGroup,
 mplsXCGroup,
 mplsXCInSegmentIndex,
 mplsXCIndex,
 mplsXCOutSegmentIndex) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsInSegmentGroup",
    "mplsInterfaceGroup",
    "mplsLsrNotificationGroup",
    "mplsOutSegmentGroup",
    "mplsXCGroup",
    "mplsXCInSegmentIndex",
    "mplsXCIndex",
    "mplsXCOutSegmentIndex")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

mplsLsrExtStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 19)
)
mplsLsrExtStdMIB.setRevisions(
        ("2015-02-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLsrExtNotifications_ObjectIdentity = ObjectIdentity
mplsLsrExtNotifications = _MplsLsrExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 0)
)
_MplsLsrExtObjects_ObjectIdentity = ObjectIdentity
mplsLsrExtObjects = _MplsLsrExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 1)
)
_MplsXCExtTable_Object = MibTable
mplsXCExtTable = _MplsXCExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1)
)
if mibBuilder.loadTexts:
    mplsXCExtTable.setStatus("current")
_MplsXCExtEntry_Object = MibTableRow
mplsXCExtEntry = _MplsXCExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1)
)
mplsXCExtEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsXCIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsXCExtEntry.setStatus("current")
_MplsXCExtTunnelPointer_Type = RowPointer
_MplsXCExtTunnelPointer_Object = MibTableColumn
mplsXCExtTunnelPointer = _MplsXCExtTunnelPointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 1),
    _MplsXCExtTunnelPointer_Type()
)
mplsXCExtTunnelPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCExtTunnelPointer.setStatus("current")
_MplsXCExtOppositeDirXCPtr_Type = RowPointer
_MplsXCExtOppositeDirXCPtr_Object = MibTableColumn
mplsXCExtOppositeDirXCPtr = _MplsXCExtOppositeDirXCPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 2),
    _MplsXCExtOppositeDirXCPtr_Type()
)
mplsXCExtOppositeDirXCPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCExtOppositeDirXCPtr.setStatus("current")
_MplsLsrExtConformance_ObjectIdentity = ObjectIdentity
mplsLsrExtConformance = _MplsLsrExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2)
)
_MplsLsrExtCompliances_ObjectIdentity = ObjectIdentity
mplsLsrExtCompliances = _MplsLsrExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1)
)
_MplsLsrExtGroups_ObjectIdentity = ObjectIdentity
mplsLsrExtGroups = _MplsLsrExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2)
)

# Managed Objects groups

mplsXCExtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 1)
)
mplsXCExtGroup.setObjects(
      *(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"),
        ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
)
if mibBuilder.loadTexts:
    mplsXCExtGroup.setStatus("current")

mplsXCExtReadOnlyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 2)
)
mplsXCExtReadOnlyObjectsGroup.setObjects(
      *(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"),
        ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
)
if mibBuilder.loadTexts:
    mplsXCExtReadOnlyObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLsrExtModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLsrExtModuleFullCompliance.setStatus(
        "current"
    )

mplsLsrExtModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLsrExtModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LSR-EXT-STD-MIB",
    **{"mplsLsrExtStdMIB": mplsLsrExtStdMIB,
       "mplsLsrExtNotifications": mplsLsrExtNotifications,
       "mplsLsrExtObjects": mplsLsrExtObjects,
       "mplsXCExtTable": mplsXCExtTable,
       "mplsXCExtEntry": mplsXCExtEntry,
       "mplsXCExtTunnelPointer": mplsXCExtTunnelPointer,
       "mplsXCExtOppositeDirXCPtr": mplsXCExtOppositeDirXCPtr,
       "mplsLsrExtConformance": mplsLsrExtConformance,
       "mplsLsrExtCompliances": mplsLsrExtCompliances,
       "mplsLsrExtModuleFullCompliance": mplsLsrExtModuleFullCompliance,
       "mplsLsrExtModuleReadOnlyCompliance": mplsLsrExtModuleReadOnlyCompliance,
       "mplsLsrExtGroups": mplsLsrExtGroups,
       "mplsXCExtGroup": mplsXCExtGroup,
       "mplsXCExtReadOnlyObjectsGroup": mplsXCExtReadOnlyObjectsGroup}
)
