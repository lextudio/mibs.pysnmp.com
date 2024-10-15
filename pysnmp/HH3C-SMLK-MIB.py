# SNMP MIB module (HH3C-SMLK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SMLK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:52 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSmlk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147)
)
hh3cSmlk.setRevisions(
        ("2014-07-23 15:03",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSmlkObject_ObjectIdentity = ObjectIdentity
hh3cSmlkObject = _Hh3cSmlkObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1)
)
_Hh3cSmlkGroupTable_Object = MibTable
hh3cSmlkGroupTable = _Hh3cSmlkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSmlkGroupTable.setStatus("current")
_Hh3cSmlkGroupEntry_Object = MibTableRow
hh3cSmlkGroupEntry = _Hh3cSmlkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1)
)
hh3cSmlkGroupEntry.setIndexNames(
    (0, "HH3C-SMLK-MIB", "hh3cSmlkGroupID"),
)
if mibBuilder.loadTexts:
    hh3cSmlkGroupEntry.setStatus("current")


class _Hh3cSmlkGroupID_Type(Integer32):
    """Custom type hh3cSmlkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cSmlkGroupID_Type.__name__ = "Integer32"
_Hh3cSmlkGroupID_Object = MibTableColumn
hh3cSmlkGroupID = _Hh3cSmlkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 1),
    _Hh3cSmlkGroupID_Type()
)
hh3cSmlkGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSmlkGroupID.setStatus("current")
_Hh3cSmlkDeviceID_Type = MacAddress
_Hh3cSmlkDeviceID_Object = MibTableColumn
hh3cSmlkDeviceID = _Hh3cSmlkDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 2),
    _Hh3cSmlkDeviceID_Type()
)
hh3cSmlkDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSmlkDeviceID.setStatus("current")


class _Hh3cSmlkPreemptionMode_Type(Integer32):
    """Custom type hh3cSmlkPreemptionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("role", 2),
          ("speed", 3))
    )


_Hh3cSmlkPreemptionMode_Type.__name__ = "Integer32"
_Hh3cSmlkPreemptionMode_Object = MibTableColumn
hh3cSmlkPreemptionMode = _Hh3cSmlkPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 3),
    _Hh3cSmlkPreemptionMode_Type()
)
hh3cSmlkPreemptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkPreemptionMode.setStatus("current")


class _Hh3cSmlkSpeedThreshold_Type(Integer32):
    """Custom type hh3cSmlkSpeedThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hh3cSmlkSpeedThreshold_Type.__name__ = "Integer32"
_Hh3cSmlkSpeedThreshold_Object = MibTableColumn
hh3cSmlkSpeedThreshold = _Hh3cSmlkSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 4),
    _Hh3cSmlkSpeedThreshold_Type()
)
hh3cSmlkSpeedThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkSpeedThreshold.setStatus("current")


class _Hh3cSmlkPreemptionDelay_Type(Integer32):
    """Custom type hh3cSmlkPreemptionDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Hh3cSmlkPreemptionDelay_Type.__name__ = "Integer32"
_Hh3cSmlkPreemptionDelay_Object = MibTableColumn
hh3cSmlkPreemptionDelay = _Hh3cSmlkPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 5),
    _Hh3cSmlkPreemptionDelay_Type()
)
hh3cSmlkPreemptionDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkPreemptionDelay.setStatus("current")


class _Hh3cSmlkControlVlanID_Type(Integer32):
    """Custom type hh3cSmlkControlVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cSmlkControlVlanID_Type.__name__ = "Integer32"
_Hh3cSmlkControlVlanID_Object = MibTableColumn
hh3cSmlkControlVlanID = _Hh3cSmlkControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 6),
    _Hh3cSmlkControlVlanID_Type()
)
hh3cSmlkControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkControlVlanID.setStatus("current")


class _Hh3cSmlkInstanceListLow_Type(OctetString):
    """Custom type hh3cSmlkInstanceListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cSmlkInstanceListLow_Type.__name__ = "OctetString"
_Hh3cSmlkInstanceListLow_Object = MibTableColumn
hh3cSmlkInstanceListLow = _Hh3cSmlkInstanceListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 7),
    _Hh3cSmlkInstanceListLow_Type()
)
hh3cSmlkInstanceListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkInstanceListLow.setStatus("current")


class _Hh3cSmlkInstanceListHigh_Type(OctetString):
    """Custom type hh3cSmlkInstanceListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cSmlkInstanceListHigh_Type.__name__ = "OctetString"
_Hh3cSmlkInstanceListHigh_Object = MibTableColumn
hh3cSmlkInstanceListHigh = _Hh3cSmlkInstanceListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 8),
    _Hh3cSmlkInstanceListHigh_Type()
)
hh3cSmlkInstanceListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkInstanceListHigh.setStatus("current")
_Hh3cSmlkGroupRowStatus_Type = RowStatus
_Hh3cSmlkGroupRowStatus_Object = MibTableColumn
hh3cSmlkGroupRowStatus = _Hh3cSmlkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 1, 1, 9),
    _Hh3cSmlkGroupRowStatus_Type()
)
hh3cSmlkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkGroupRowStatus.setStatus("current")
_Hh3cSmlkPortTable_Object = MibTable
hh3cSmlkPortTable = _Hh3cSmlkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSmlkPortTable.setStatus("current")
_Hh3cSmlkPortEntry_Object = MibTableRow
hh3cSmlkPortEntry = _Hh3cSmlkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1)
)
hh3cSmlkPortEntry.setIndexNames(
    (0, "HH3C-SMLK-MIB", "hh3cSmlkGroupID"),
    (0, "HH3C-SMLK-MIB", "hh3cSmlkPortIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cSmlkPortEntry.setStatus("current")
_Hh3cSmlkPortIfIndex_Type = InterfaceIndex
_Hh3cSmlkPortIfIndex_Object = MibTableColumn
hh3cSmlkPortIfIndex = _Hh3cSmlkPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1, 1),
    _Hh3cSmlkPortIfIndex_Type()
)
hh3cSmlkPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSmlkPortIfIndex.setStatus("current")


class _Hh3cSmlkPortRole_Type(Integer32):
    """Custom type hh3cSmlkPortRole based on Integer32"""
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


_Hh3cSmlkPortRole_Type.__name__ = "Integer32"
_Hh3cSmlkPortRole_Object = MibTableColumn
hh3cSmlkPortRole = _Hh3cSmlkPortRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1, 2),
    _Hh3cSmlkPortRole_Type()
)
hh3cSmlkPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkPortRole.setStatus("current")


class _Hh3cSmlkPortStatus_Type(Integer32):
    """Custom type hh3cSmlkPortStatus based on Integer32"""
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
          ("down", 1),
          ("standby", 3))
    )


_Hh3cSmlkPortStatus_Type.__name__ = "Integer32"
_Hh3cSmlkPortStatus_Object = MibTableColumn
hh3cSmlkPortStatus = _Hh3cSmlkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1, 3),
    _Hh3cSmlkPortStatus_Type()
)
hh3cSmlkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSmlkPortStatus.setStatus("current")
_Hh3cSmlkFlushCount_Type = Counter64
_Hh3cSmlkFlushCount_Object = MibTableColumn
hh3cSmlkFlushCount = _Hh3cSmlkFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1, 4),
    _Hh3cSmlkFlushCount_Type()
)
hh3cSmlkFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSmlkFlushCount.setStatus("current")
_Hh3cSmlkLastFlushTime_Type = DateAndTime
_Hh3cSmlkLastFlushTime_Object = MibTableColumn
hh3cSmlkLastFlushTime = _Hh3cSmlkLastFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1, 5),
    _Hh3cSmlkLastFlushTime_Type()
)
hh3cSmlkLastFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSmlkLastFlushTime.setStatus("current")
_Hh3cSmlkPortRowStatus_Type = RowStatus
_Hh3cSmlkPortRowStatus_Object = MibTableColumn
hh3cSmlkPortRowStatus = _Hh3cSmlkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 2, 1, 6),
    _Hh3cSmlkPortRowStatus_Type()
)
hh3cSmlkPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSmlkPortRowStatus.setStatus("current")
_Hh3cSmlkFlushEnableTable_Object = MibTable
hh3cSmlkFlushEnableTable = _Hh3cSmlkFlushEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cSmlkFlushEnableTable.setStatus("current")
_Hh3cSmlkFlushEnableEntry_Object = MibTableRow
hh3cSmlkFlushEnableEntry = _Hh3cSmlkFlushEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 3, 1)
)
hh3cSmlkFlushEnableEntry.setIndexNames(
    (0, "HH3C-SMLK-MIB", "hh3cSmlkIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cSmlkFlushEnableEntry.setStatus("current")
_Hh3cSmlkIfIndex_Type = InterfaceIndex
_Hh3cSmlkIfIndex_Object = MibTableColumn
hh3cSmlkIfIndex = _Hh3cSmlkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 3, 1, 1),
    _Hh3cSmlkIfIndex_Type()
)
hh3cSmlkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSmlkIfIndex.setStatus("current")


class _Hh3cSmlkControlVlanListLow_Type(OctetString):
    """Custom type hh3cSmlkControlVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cSmlkControlVlanListLow_Type.__name__ = "OctetString"
_Hh3cSmlkControlVlanListLow_Object = MibTableColumn
hh3cSmlkControlVlanListLow = _Hh3cSmlkControlVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 3, 1, 2),
    _Hh3cSmlkControlVlanListLow_Type()
)
hh3cSmlkControlVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmlkControlVlanListLow.setStatus("current")


class _Hh3cSmlkControlVlanListHigh_Type(OctetString):
    """Custom type hh3cSmlkControlVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cSmlkControlVlanListHigh_Type.__name__ = "OctetString"
_Hh3cSmlkControlVlanListHigh_Object = MibTableColumn
hh3cSmlkControlVlanListHigh = _Hh3cSmlkControlVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 1, 3, 1, 3),
    _Hh3cSmlkControlVlanListHigh_Type()
)
hh3cSmlkControlVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmlkControlVlanListHigh.setStatus("current")
_Hh3cSmlkTrap_ObjectIdentity = ObjectIdentity
hh3cSmlkTrap = _Hh3cSmlkTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 2)
)
_Hh3cSmlkTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cSmlkTrapPrefix = _Hh3cSmlkTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cSmlkGroupLinkActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147, 2, 0, 1)
)
hh3cSmlkGroupLinkActive.setObjects(
      *(("HH3C-SMLK-MIB", "hh3cSmlkGroupID"),
        ("HH3C-SMLK-MIB", "hh3cSmlkPortIfIndex"))
)
if mibBuilder.loadTexts:
    hh3cSmlkGroupLinkActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SMLK-MIB",
    **{"hh3cSmlk": hh3cSmlk,
       "hh3cSmlkObject": hh3cSmlkObject,
       "hh3cSmlkGroupTable": hh3cSmlkGroupTable,
       "hh3cSmlkGroupEntry": hh3cSmlkGroupEntry,
       "hh3cSmlkGroupID": hh3cSmlkGroupID,
       "hh3cSmlkDeviceID": hh3cSmlkDeviceID,
       "hh3cSmlkPreemptionMode": hh3cSmlkPreemptionMode,
       "hh3cSmlkSpeedThreshold": hh3cSmlkSpeedThreshold,
       "hh3cSmlkPreemptionDelay": hh3cSmlkPreemptionDelay,
       "hh3cSmlkControlVlanID": hh3cSmlkControlVlanID,
       "hh3cSmlkInstanceListLow": hh3cSmlkInstanceListLow,
       "hh3cSmlkInstanceListHigh": hh3cSmlkInstanceListHigh,
       "hh3cSmlkGroupRowStatus": hh3cSmlkGroupRowStatus,
       "hh3cSmlkPortTable": hh3cSmlkPortTable,
       "hh3cSmlkPortEntry": hh3cSmlkPortEntry,
       "hh3cSmlkPortIfIndex": hh3cSmlkPortIfIndex,
       "hh3cSmlkPortRole": hh3cSmlkPortRole,
       "hh3cSmlkPortStatus": hh3cSmlkPortStatus,
       "hh3cSmlkFlushCount": hh3cSmlkFlushCount,
       "hh3cSmlkLastFlushTime": hh3cSmlkLastFlushTime,
       "hh3cSmlkPortRowStatus": hh3cSmlkPortRowStatus,
       "hh3cSmlkFlushEnableTable": hh3cSmlkFlushEnableTable,
       "hh3cSmlkFlushEnableEntry": hh3cSmlkFlushEnableEntry,
       "hh3cSmlkIfIndex": hh3cSmlkIfIndex,
       "hh3cSmlkControlVlanListLow": hh3cSmlkControlVlanListLow,
       "hh3cSmlkControlVlanListHigh": hh3cSmlkControlVlanListHigh,
       "hh3cSmlkTrap": hh3cSmlkTrap,
       "hh3cSmlkTrapPrefix": hh3cSmlkTrapPrefix,
       "hh3cSmlkGroupLinkActive": hh3cSmlkGroupLinkActive}
)
