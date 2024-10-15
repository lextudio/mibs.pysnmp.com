# SNMP MIB module (EXTREME-STACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(extremeCurrentTemperature,) = mibBuilder.importSymbols(
    "EXTREME-SYSTEM-MIB",
    "extremeCurrentTemperature")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeStackable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeStackDetection_Type = TruthValue
_ExtremeStackDetection_Object = MibScalar
extremeStackDetection = _ExtremeStackDetection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 1),
    _ExtremeStackDetection_Type()
)
extremeStackDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeStackDetection.setStatus("current")
_ExtremeStackMemberTable_Object = MibTable
extremeStackMemberTable = _ExtremeStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2)
)
if mibBuilder.loadTexts:
    extremeStackMemberTable.setStatus("current")
_ExtremeStackMemberEntry_Object = MibTableRow
extremeStackMemberEntry = _ExtremeStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1)
)
extremeStackMemberEntry.setIndexNames(
    (0, "EXTREME-STACKING-MIB", "extremeStackMemberSlotId"),
)
if mibBuilder.loadTexts:
    extremeStackMemberEntry.setStatus("current")


class _ExtremeStackMemberSlotId_Type(Integer32):
    """Custom type extremeStackMemberSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremeStackMemberSlotId_Type.__name__ = "Integer32"
_ExtremeStackMemberSlotId_Object = MibTableColumn
extremeStackMemberSlotId = _ExtremeStackMemberSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 1),
    _ExtremeStackMemberSlotId_Type()
)
extremeStackMemberSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberSlotId.setStatus("current")
_ExtremeStackMemberType_Type = ObjectIdentifier
_ExtremeStackMemberType_Object = MibTableColumn
extremeStackMemberType = _ExtremeStackMemberType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 2),
    _ExtremeStackMemberType_Type()
)
extremeStackMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberType.setStatus("current")


class _ExtremeStackMemberOperStatus_Type(Integer32):
    """Custom type extremeStackMemberOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("mismatch", 3),
          ("up", 1))
    )


_ExtremeStackMemberOperStatus_Type.__name__ = "Integer32"
_ExtremeStackMemberOperStatus_Object = MibTableColumn
extremeStackMemberOperStatus = _ExtremeStackMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 3),
    _ExtremeStackMemberOperStatus_Type()
)
extremeStackMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberOperStatus.setStatus("current")


class _ExtremeStackMemberRole_Type(Integer32):
    """Custom type extremeStackMemberRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ExtremeStackMemberRole_Type.__name__ = "Integer32"
_ExtremeStackMemberRole_Object = MibTableColumn
extremeStackMemberRole = _ExtremeStackMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 4),
    _ExtremeStackMemberRole_Type()
)
extremeStackMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberRole.setStatus("current")
_ExtremeStackMemberEntPhysicalIndex_Type = Integer32
_ExtremeStackMemberEntPhysicalIndex_Object = MibTableColumn
extremeStackMemberEntPhysicalIndex = _ExtremeStackMemberEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 5),
    _ExtremeStackMemberEntPhysicalIndex_Type()
)
extremeStackMemberEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberEntPhysicalIndex.setStatus("current")
_ExtremeStackMemberMACAddress_Type = MacAddress
_ExtremeStackMemberMACAddress_Object = MibTableColumn
extremeStackMemberMACAddress = _ExtremeStackMemberMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 6),
    _ExtremeStackMemberMACAddress_Type()
)
extremeStackMemberMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberMACAddress.setStatus("current")


class _ExtremeStackMemberCurImageVersion_Type(DisplayString):
    """Custom type extremeStackMemberCurImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeStackMemberCurImageVersion_Type.__name__ = "DisplayString"
_ExtremeStackMemberCurImageVersion_Object = MibTableColumn
extremeStackMemberCurImageVersion = _ExtremeStackMemberCurImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 7),
    _ExtremeStackMemberCurImageVersion_Type()
)
extremeStackMemberCurImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberCurImageVersion.setStatus("current")


class _ExtremeStackMemberPriImageVersion_Type(DisplayString):
    """Custom type extremeStackMemberPriImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeStackMemberPriImageVersion_Type.__name__ = "DisplayString"
_ExtremeStackMemberPriImageVersion_Object = MibTableColumn
extremeStackMemberPriImageVersion = _ExtremeStackMemberPriImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 8),
    _ExtremeStackMemberPriImageVersion_Type()
)
extremeStackMemberPriImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberPriImageVersion.setStatus("current")


class _ExtremeStackMemberSecImageVersion_Type(DisplayString):
    """Custom type extremeStackMemberSecImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeStackMemberSecImageVersion_Type.__name__ = "DisplayString"
_ExtremeStackMemberSecImageVersion_Object = MibTableColumn
extremeStackMemberSecImageVersion = _ExtremeStackMemberSecImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 9),
    _ExtremeStackMemberSecImageVersion_Type()
)
extremeStackMemberSecImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberSecImageVersion.setStatus("current")


class _ExtremeStackMemberBootRomVersion_Type(DisplayString):
    """Custom type extremeStackMemberBootRomVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeStackMemberBootRomVersion_Type.__name__ = "DisplayString"
_ExtremeStackMemberBootRomVersion_Object = MibTableColumn
extremeStackMemberBootRomVersion = _ExtremeStackMemberBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 10),
    _ExtremeStackMemberBootRomVersion_Type()
)
extremeStackMemberBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberBootRomVersion.setStatus("current")


class _ExtremeStackMemberCurConfig_Type(DisplayString):
    """Custom type extremeStackMemberCurConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeStackMemberCurConfig_Type.__name__ = "DisplayString"
_ExtremeStackMemberCurConfig_Object = MibTableColumn
extremeStackMemberCurConfig = _ExtremeStackMemberCurConfig_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 11),
    _ExtremeStackMemberCurConfig_Type()
)
extremeStackMemberCurConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberCurConfig.setStatus("current")


class _ExtremeStackMemberConfigSelected_Type(Integer32):
    """Custom type extremeStackMemberConfigSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeStackMemberConfigSelected_Type.__name__ = "Integer32"
_ExtremeStackMemberConfigSelected_Object = MibTableColumn
extremeStackMemberConfigSelected = _ExtremeStackMemberConfigSelected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 12),
    _ExtremeStackMemberConfigSelected_Type()
)
extremeStackMemberConfigSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberConfigSelected.setStatus("current")


class _ExtremeStackMemberImageSelected_Type(Integer32):
    """Custom type extremeStackMemberImageSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeStackMemberImageSelected_Type.__name__ = "Integer32"
_ExtremeStackMemberImageSelected_Object = MibTableColumn
extremeStackMemberImageSelected = _ExtremeStackMemberImageSelected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 13),
    _ExtremeStackMemberImageSelected_Type()
)
extremeStackMemberImageSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberImageSelected.setStatus("current")
_ExtremeStackMemberStackPriority_Type = Integer32
_ExtremeStackMemberStackPriority_Object = MibTableColumn
extremeStackMemberStackPriority = _ExtremeStackMemberStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 14),
    _ExtremeStackMemberStackPriority_Type()
)
extremeStackMemberStackPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberStackPriority.setStatus("current")
_ExtremeStackMemberMgmtIpAddress_Type = IpAddress
_ExtremeStackMemberMgmtIpAddress_Object = MibTableColumn
extremeStackMemberMgmtIpAddress = _ExtremeStackMemberMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 15),
    _ExtremeStackMemberMgmtIpAddress_Type()
)
extremeStackMemberMgmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberMgmtIpAddress.setStatus("current")


class _ExtremeStackMemberSysLocation_Type(DisplayString):
    """Custom type extremeStackMemberSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtremeStackMemberSysLocation_Type.__name__ = "DisplayString"
_ExtremeStackMemberSysLocation_Object = MibTableColumn
extremeStackMemberSysLocation = _ExtremeStackMemberSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 16),
    _ExtremeStackMemberSysLocation_Type()
)
extremeStackMemberSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeStackMemberSysLocation.setStatus("current")
_ExtremeStackMemberAutoConfig_Type = TruthValue
_ExtremeStackMemberAutoConfig_Object = MibTableColumn
extremeStackMemberAutoConfig = _ExtremeStackMemberAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 17),
    _ExtremeStackMemberAutoConfig_Type()
)
extremeStackMemberAutoConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackMemberAutoConfig.setStatus("current")


class _ExtremeStackMemberStackStatus_Type(Integer32):
    """Custom type extremeStackMemberStackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ExtremeStackMemberStackStatus_Type.__name__ = "Integer32"
_ExtremeStackMemberStackStatus_Object = MibTableColumn
extremeStackMemberStackStatus = _ExtremeStackMemberStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 2, 1, 18),
    _ExtremeStackMemberStackStatus_Type()
)
extremeStackMemberStackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeStackMemberStackStatus.setStatus("current")
_ExtremeStackingPortTable_Object = MibTable
extremeStackingPortTable = _ExtremeStackingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 3)
)
if mibBuilder.loadTexts:
    extremeStackingPortTable.setStatus("current")
_ExtremeStackingPortEntry_Object = MibTableRow
extremeStackingPortEntry = _ExtremeStackingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 3, 1)
)
extremeStackingPortEntry.setIndexNames(
    (0, "EXTREME-STACKING-MIB", "extremeStackingPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeStackingPortEntry.setStatus("current")


class _ExtremeStackingPortIfIndex_Type(Integer32):
    """Custom type extremeStackingPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeStackingPortIfIndex_Type.__name__ = "Integer32"
_ExtremeStackingPortIfIndex_Object = MibTableColumn
extremeStackingPortIfIndex = _ExtremeStackingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 3, 1, 1),
    _ExtremeStackingPortIfIndex_Type()
)
extremeStackingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackingPortIfIndex.setStatus("current")
_ExtremeStackingPortRemoteMac_Type = MacAddress
_ExtremeStackingPortRemoteMac_Object = MibTableColumn
extremeStackingPortRemoteMac = _ExtremeStackingPortRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 3, 1, 2),
    _ExtremeStackingPortRemoteMac_Type()
)
extremeStackingPortRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackingPortRemoteMac.setStatus("current")
_ExtremeStackingPortLinkSpeed_Type = Unsigned32
_ExtremeStackingPortLinkSpeed_Object = MibTableColumn
extremeStackingPortLinkSpeed = _ExtremeStackingPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 3, 1, 3),
    _ExtremeStackingPortLinkSpeed_Type()
)
extremeStackingPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackingPortLinkSpeed.setStatus("current")


class _ExtremeStackingPortLinkStatus_Type(Integer32):
    """Custom type extremeStackingPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ExtremeStackingPortLinkStatus_Type.__name__ = "Integer32"
_ExtremeStackingPortLinkStatus_Object = MibTableColumn
extremeStackingPortLinkStatus = _ExtremeStackingPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 3, 1, 4),
    _ExtremeStackingPortLinkStatus_Type()
)
extremeStackingPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStackingPortLinkStatus.setStatus("current")
_ExtremeStackableTraps_ObjectIdentity = ObjectIdentity
extremeStackableTraps = _ExtremeStackableTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 4)
)
_ExtremeStackTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeStackTrapsPrefix = _ExtremeStackTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 4, 0)
)

# Managed Objects groups


# Notification objects

extremeStackMemberOverheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 4, 0, 1)
)
extremeStackMemberOverheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeCurrentTemperature"),
        ("EXTREME-STACKING-MIB", "extremeStackMemberSlotId"))
)
if mibBuilder.loadTexts:
    extremeStackMemberOverheat.setStatus(
        "current"
    )

extremeStackMemberStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 4, 0, 2)
)
extremeStackMemberStatusChanged.setObjects(
      *(("EXTREME-STACKING-MIB", "extremeStackMemberSlotId"),
        ("EXTREME-STACKING-MIB", "extremeStackMemberOperStatus"))
)
if mibBuilder.loadTexts:
    extremeStackMemberStatusChanged.setStatus(
        "current"
    )

extremeStackingPortStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33, 4, 0, 3)
)
extremeStackingPortStatusChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-STACKING-MIB", "extremeStackingPortRemoteMac"),
        ("EXTREME-STACKING-MIB", "extremeStackingPortLinkSpeed"),
        ("EXTREME-STACKING-MIB", "extremeStackingPortLinkStatus"))
)
if mibBuilder.loadTexts:
    extremeStackingPortStatusChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-STACKING-MIB",
    **{"extremeStackable": extremeStackable,
       "extremeStackDetection": extremeStackDetection,
       "extremeStackMemberTable": extremeStackMemberTable,
       "extremeStackMemberEntry": extremeStackMemberEntry,
       "extremeStackMemberSlotId": extremeStackMemberSlotId,
       "extremeStackMemberType": extremeStackMemberType,
       "extremeStackMemberOperStatus": extremeStackMemberOperStatus,
       "extremeStackMemberRole": extremeStackMemberRole,
       "extremeStackMemberEntPhysicalIndex": extremeStackMemberEntPhysicalIndex,
       "extremeStackMemberMACAddress": extremeStackMemberMACAddress,
       "extremeStackMemberCurImageVersion": extremeStackMemberCurImageVersion,
       "extremeStackMemberPriImageVersion": extremeStackMemberPriImageVersion,
       "extremeStackMemberSecImageVersion": extremeStackMemberSecImageVersion,
       "extremeStackMemberBootRomVersion": extremeStackMemberBootRomVersion,
       "extremeStackMemberCurConfig": extremeStackMemberCurConfig,
       "extremeStackMemberConfigSelected": extremeStackMemberConfigSelected,
       "extremeStackMemberImageSelected": extremeStackMemberImageSelected,
       "extremeStackMemberStackPriority": extremeStackMemberStackPriority,
       "extremeStackMemberMgmtIpAddress": extremeStackMemberMgmtIpAddress,
       "extremeStackMemberSysLocation": extremeStackMemberSysLocation,
       "extremeStackMemberAutoConfig": extremeStackMemberAutoConfig,
       "extremeStackMemberStackStatus": extremeStackMemberStackStatus,
       "extremeStackingPortTable": extremeStackingPortTable,
       "extremeStackingPortEntry": extremeStackingPortEntry,
       "extremeStackingPortIfIndex": extremeStackingPortIfIndex,
       "extremeStackingPortRemoteMac": extremeStackingPortRemoteMac,
       "extremeStackingPortLinkSpeed": extremeStackingPortLinkSpeed,
       "extremeStackingPortLinkStatus": extremeStackingPortLinkStatus,
       "extremeStackableTraps": extremeStackableTraps,
       "extremeStackTrapsPrefix": extremeStackTrapsPrefix,
       "extremeStackMemberOverheat": extremeStackMemberOverheat,
       "extremeStackMemberStatusChanged": extremeStackMemberStatusChanged,
       "extremeStackingPortStatusChanged": extremeStackingPortStatusChanged}
)
