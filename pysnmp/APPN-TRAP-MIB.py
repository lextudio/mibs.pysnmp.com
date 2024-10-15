# SNMP MIB module (APPN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPN-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:55 2024
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

(dlurDlusSessnStatus,) = mibBuilder.importSymbols(
    "APPN-DLUR-MIB",
    "dlurDlusSessnStatus")

(appnCompliances,
 appnGroups,
 appnIsInP2SFmdBytes,
 appnIsInP2SFmdPius,
 appnIsInP2SNonFmdBytes,
 appnIsInP2SNonFmdPius,
 appnIsInS2PFmdBytes,
 appnIsInS2PFmdPius,
 appnIsInS2PNonFmdBytes,
 appnIsInS2PNonFmdPius,
 appnIsInSessUpTime,
 appnLocalTgCpCpSession,
 appnLocalTgOperational,
 appnLsOperState,
 appnMIB,
 appnObjects,
 appnPortOperState) = mibBuilder.importSymbols(
    "APPN-MIB",
    "appnCompliances",
    "appnGroups",
    "appnIsInP2SFmdBytes",
    "appnIsInP2SFmdPius",
    "appnIsInP2SNonFmdBytes",
    "appnIsInP2SNonFmdPius",
    "appnIsInS2PFmdBytes",
    "appnIsInS2PFmdPius",
    "appnIsInS2PNonFmdBytes",
    "appnIsInS2PNonFmdPius",
    "appnIsInSessUpTime",
    "appnLocalTgCpCpSession",
    "appnLocalTgOperational",
    "appnLsOperState",
    "appnMIB",
    "appnObjects",
    "appnPortOperState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

appnTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AppnTrapObjects_ObjectIdentity = ObjectIdentity
appnTrapObjects = _AppnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 7)
)


class _AppnTrapControl_Type(Bits):
    """Custom type appnTrapControl based on Bits"""
    namedValues = NamedValues(
        *(("appnLocalTgCpCpChangeTrap", 1),
          ("appnLocalTgOperStateChangeTrap", 0),
          ("appnLsOperStateChangeTrap", 3),
          ("appnPortOperStateChangeTrap", 2),
          ("dlurDlusStateChangeTrap", 4))
    )

_AppnTrapControl_Type.__name__ = "Bits"
_AppnTrapControl_Object = MibScalar
appnTrapControl = _AppnTrapControl_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1),
    _AppnTrapControl_Type()
)
appnTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnTrapControl.setStatus("current")
_AppnLocalTgTableChanges_Type = Counter32
_AppnLocalTgTableChanges_Object = MibScalar
appnLocalTgTableChanges = _AppnLocalTgTableChanges_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2),
    _AppnLocalTgTableChanges_Type()
)
appnLocalTgTableChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgTableChanges.setStatus("current")
_AppnPortTableChanges_Type = Counter32
_AppnPortTableChanges_Object = MibScalar
appnPortTableChanges = _AppnPortTableChanges_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3),
    _AppnPortTableChanges_Type()
)
appnPortTableChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortTableChanges.setStatus("current")
_AppnLsTableChanges_Type = Counter32
_AppnLsTableChanges_Object = MibScalar
appnLsTableChanges = _AppnLsTableChanges_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4),
    _AppnLsTableChanges_Type()
)
appnLsTableChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsTableChanges.setStatus("current")
_DlurDlusTableChanges_Type = Counter32
_DlurDlusTableChanges_Object = MibScalar
dlurDlusTableChanges = _DlurDlusTableChanges_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5),
    _DlurDlusTableChanges_Type()
)
dlurDlusTableChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurDlusTableChanges.setStatus("current")

# Managed Objects groups

appnTrapMibTopoConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)
)
appnTrapMibTopoConfGroup.setObjects(
      *(("APPN-TRAP-MIB", "appnTrapControl"),
        ("APPN-TRAP-MIB", "appnLocalTgTableChanges"),
        ("APPN-TRAP-MIB", "appnPortTableChanges"),
        ("APPN-TRAP-MIB", "appnLsTableChanges"))
)
if mibBuilder.loadTexts:
    appnTrapMibTopoConfGroup.setStatus("current")

appnTrapMibDlurConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)
)
appnTrapMibDlurConfGroup.setObjects(
      *(("APPN-TRAP-MIB", "appnTrapControl"),
        ("APPN-TRAP-MIB", "dlurDlusTableChanges"))
)
if mibBuilder.loadTexts:
    appnTrapMibDlurConfGroup.setStatus("current")


# Notification objects

appnIsrAccountingDataTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 0, 1)
)
appnIsrAccountingDataTrap.setObjects(
      *(("APPN-MIB", "appnIsInP2SFmdPius"),
        ("APPN-MIB", "appnIsInS2PFmdPius"),
        ("APPN-MIB", "appnIsInP2SNonFmdPius"),
        ("APPN-MIB", "appnIsInS2PNonFmdPius"),
        ("APPN-MIB", "appnIsInP2SFmdBytes"),
        ("APPN-MIB", "appnIsInS2PFmdBytes"),
        ("APPN-MIB", "appnIsInP2SNonFmdBytes"),
        ("APPN-MIB", "appnIsInS2PNonFmdBytes"),
        ("APPN-MIB", "appnIsInSessUpTime"))
)
if mibBuilder.loadTexts:
    appnIsrAccountingDataTrap.setStatus(
        "current"
    )

appnLocalTgOperStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 0, 2)
)
appnLocalTgOperStateChangeTrap.setObjects(
      *(("APPN-TRAP-MIB", "appnLocalTgTableChanges"),
        ("APPN-MIB", "appnLocalTgOperational"))
)
if mibBuilder.loadTexts:
    appnLocalTgOperStateChangeTrap.setStatus(
        "current"
    )

appnLocalTgCpCpChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 0, 3)
)
appnLocalTgCpCpChangeTrap.setObjects(
      *(("APPN-TRAP-MIB", "appnLocalTgTableChanges"),
        ("APPN-MIB", "appnLocalTgCpCpSession"))
)
if mibBuilder.loadTexts:
    appnLocalTgCpCpChangeTrap.setStatus(
        "current"
    )

appnPortOperStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 0, 4)
)
appnPortOperStateChangeTrap.setObjects(
      *(("APPN-TRAP-MIB", "appnPortTableChanges"),
        ("APPN-MIB", "appnPortOperState"))
)
if mibBuilder.loadTexts:
    appnPortOperStateChangeTrap.setStatus(
        "current"
    )

appnLsOperStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 0, 5)
)
appnLsOperStateChangeTrap.setObjects(
      *(("APPN-TRAP-MIB", "appnLsTableChanges"),
        ("APPN-MIB", "appnLsOperState"))
)
if mibBuilder.loadTexts:
    appnLsOperStateChangeTrap.setStatus(
        "current"
    )

dlurDlusStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 0, 6)
)
dlurDlusStateChangeTrap.setObjects(
      *(("APPN-TRAP-MIB", "dlurDlusTableChanges"),
        ("APPN-DLUR-MIB", "dlurDlusSessnStatus"))
)
if mibBuilder.loadTexts:
    dlurDlusStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups

appnTrapMibIsrNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)
)
appnTrapMibIsrNotifGroup.setObjects(
    ("APPN-TRAP-MIB", "appnIsrAccountingDataTrap")
)
if mibBuilder.loadTexts:
    appnTrapMibIsrNotifGroup.setStatus(
        "current"
    )

appnTrapMibTopoNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)
)
appnTrapMibTopoNotifGroup.setObjects(
      *(("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"),
        ("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"),
        ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"),
        ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"))
)
if mibBuilder.loadTexts:
    appnTrapMibTopoNotifGroup.setStatus(
        "current"
    )

appnTrapMibDlurNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)
)
appnTrapMibDlurNotifGroup.setObjects(
    ("APPN-TRAP-MIB", "dlurDlusStateChangeTrap")
)
if mibBuilder.loadTexts:
    appnTrapMibDlurNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

appnTrapMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    appnTrapMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPN-TRAP-MIB",
    **{"appnTrapMIB": appnTrapMIB,
       "appnIsrAccountingDataTrap": appnIsrAccountingDataTrap,
       "appnLocalTgOperStateChangeTrap": appnLocalTgOperStateChangeTrap,
       "appnLocalTgCpCpChangeTrap": appnLocalTgCpCpChangeTrap,
       "appnPortOperStateChangeTrap": appnPortOperStateChangeTrap,
       "appnLsOperStateChangeTrap": appnLsOperStateChangeTrap,
       "dlurDlusStateChangeTrap": dlurDlusStateChangeTrap,
       "appnTrapObjects": appnTrapObjects,
       "appnTrapControl": appnTrapControl,
       "appnLocalTgTableChanges": appnLocalTgTableChanges,
       "appnPortTableChanges": appnPortTableChanges,
       "appnLsTableChanges": appnLsTableChanges,
       "dlurDlusTableChanges": dlurDlusTableChanges,
       "appnTrapMibCompliance": appnTrapMibCompliance,
       "appnTrapMibIsrNotifGroup": appnTrapMibIsrNotifGroup,
       "appnTrapMibTopoConfGroup": appnTrapMibTopoConfGroup,
       "appnTrapMibTopoNotifGroup": appnTrapMibTopoNotifGroup,
       "appnTrapMibDlurConfGroup": appnTrapMibDlurConfGroup,
       "appnTrapMibDlurNotifGroup": appnTrapMibDlurNotifGroup}
)
