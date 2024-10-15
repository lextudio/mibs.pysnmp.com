# SNMP MIB module (AT-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:00 2024
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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

chassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23)
)
chassis.setRevisions(
        ("2012-05-15 00:00",
         "2011-09-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisNotifications_ObjectIdentity = ObjectIdentity
chassisNotifications = _ChassisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0)
)


class _SlotNumber_Type(Unsigned32):
    """Custom type slotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SlotNumber_Type.__name__ = "Unsigned32"
_SlotNumber_Object = MibScalar
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 4),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotNumber.setStatus("current")


class _ChassisRole_Type(Integer32):
    """Custom type chassisRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("activeMaster", 7),
          ("disabledMaster", 6),
          ("discovering", 2),
          ("leaving", 1),
          ("pendingMaster", 5),
          ("standbyMember", 4),
          ("synchronizing", 3))
    )


_ChassisRole_Type.__name__ = "Integer32"
_ChassisRole_Object = MibScalar
chassisRole = _ChassisRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 5),
    _ChassisRole_Type()
)
chassisRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chassisRole.setStatus("current")
_ChassisCardTable_Object = MibTable
chassisCardTable = _ChassisCardTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1)
)
if mibBuilder.loadTexts:
    chassisCardTable.setStatus("current")
_ChassisCardEntry_Object = MibTableRow
chassisCardEntry = _ChassisCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1)
)
chassisCardEntry.setIndexNames(
    (0, "AT-CHASSIS-MIB", "chassisCardSlot"),
)
if mibBuilder.loadTexts:
    chassisCardEntry.setStatus("current")


class _ChassisCardSlot_Type(Integer32):
    """Custom type chassisCardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ChassisCardSlot_Type.__name__ = "Integer32"
_ChassisCardSlot_Object = MibTableColumn
chassisCardSlot = _ChassisCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 1),
    _ChassisCardSlot_Type()
)
chassisCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCardSlot.setStatus("current")
_ChassisCardBoardOID_Type = ObjectIdentifier
_ChassisCardBoardOID_Object = MibTableColumn
chassisCardBoardOID = _ChassisCardBoardOID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 2),
    _ChassisCardBoardOID_Type()
)
chassisCardBoardOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCardBoardOID.setStatus("current")
_ChassisCardName_Type = DisplayString
_ChassisCardName_Object = MibTableColumn
chassisCardName = _ChassisCardName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 3),
    _ChassisCardName_Type()
)
chassisCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCardName.setStatus("current")


class _ChassisCardState_Type(Integer32):
    """Custom type chassisCardState based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("booting", 10),
          ("configuring", 2),
          ("disabled", 8),
          ("incompatibleSW", 7),
          ("initializing", 9),
          ("joining", 6),
          ("online", 4),
          ("provisioned", 12),
          ("syncing", 3),
          ("syncingFirmware", 5),
          ("unknown", 1),
          ("unsupportedHW", 11))
    )


_ChassisCardState_Type.__name__ = "Integer32"
_ChassisCardState_Object = MibTableColumn
chassisCardState = _ChassisCardState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 4),
    _ChassisCardState_Type()
)
chassisCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCardState.setStatus("current")


class _ChassisCardControllerState_Type(Integer32):
    """Custom type chassisCardControllerState based on Integer32"""
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
          ("standby", 3),
          ("unknown", 1))
    )


_ChassisCardControllerState_Type.__name__ = "Integer32"
_ChassisCardControllerState_Object = MibTableColumn
chassisCardControllerState = _ChassisCardControllerState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 5),
    _ChassisCardControllerState_Type()
)
chassisCardControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCardControllerState.setStatus("current")

# Managed Objects groups


# Notification objects

chassisCardRoleChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 1)
)
chassisCardRoleChangeNotify.setObjects(
      *(("AT-CHASSIS-MIB", "slotNumber"),
        ("AT-CHASSIS-MIB", "chassisRole"))
)
if mibBuilder.loadTexts:
    chassisCardRoleChangeNotify.setStatus(
        "current"
    )

chassisCardJoinNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 2)
)
chassisCardJoinNotify.setObjects(
    ("AT-CHASSIS-MIB", "slotNumber")
)
if mibBuilder.loadTexts:
    chassisCardJoinNotify.setStatus(
        "current"
    )

chassisCardLeaveNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 3)
)
chassisCardLeaveNotify.setObjects(
    ("AT-CHASSIS-MIB", "slotNumber")
)
if mibBuilder.loadTexts:
    chassisCardLeaveNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-CHASSIS-MIB",
    **{"chassis": chassis,
       "chassisNotifications": chassisNotifications,
       "chassisCardRoleChangeNotify": chassisCardRoleChangeNotify,
       "chassisCardJoinNotify": chassisCardJoinNotify,
       "chassisCardLeaveNotify": chassisCardLeaveNotify,
       "slotNumber": slotNumber,
       "chassisRole": chassisRole,
       "chassisCardTable": chassisCardTable,
       "chassisCardEntry": chassisCardEntry,
       "chassisCardSlot": chassisCardSlot,
       "chassisCardBoardOID": chassisCardBoardOID,
       "chassisCardName": chassisCardName,
       "chassisCardState": chassisCardState,
       "chassisCardControllerState": chassisCardControllerState}
)
