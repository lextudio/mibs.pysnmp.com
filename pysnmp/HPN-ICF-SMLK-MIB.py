# SNMP MIB module (HPN-ICF-SMLK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SMLK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:49 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfSmlk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147)
)
hpnicfSmlk.setRevisions(
        ("2014-07-23 15:03",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSmlkObject_ObjectIdentity = ObjectIdentity
hpnicfSmlkObject = _HpnicfSmlkObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1)
)
_HpnicfSmlkGroupTable_Object = MibTable
hpnicfSmlkGroupTable = _HpnicfSmlkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfSmlkGroupTable.setStatus("current")
_HpnicfSmlkGroupEntry_Object = MibTableRow
hpnicfSmlkGroupEntry = _HpnicfSmlkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1)
)
hpnicfSmlkGroupEntry.setIndexNames(
    (0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfSmlkGroupEntry.setStatus("current")


class _HpnicfSmlkGroupID_Type(Integer32):
    """Custom type hpnicfSmlkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpnicfSmlkGroupID_Type.__name__ = "Integer32"
_HpnicfSmlkGroupID_Object = MibTableColumn
hpnicfSmlkGroupID = _HpnicfSmlkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 1),
    _HpnicfSmlkGroupID_Type()
)
hpnicfSmlkGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSmlkGroupID.setStatus("current")
_HpnicfSmlkDeviceID_Type = MacAddress
_HpnicfSmlkDeviceID_Object = MibTableColumn
hpnicfSmlkDeviceID = _HpnicfSmlkDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 2),
    _HpnicfSmlkDeviceID_Type()
)
hpnicfSmlkDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSmlkDeviceID.setStatus("current")


class _HpnicfSmlkPreemptionMode_Type(Integer32):
    """Custom type hpnicfSmlkPreemptionMode based on Integer32"""
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


_HpnicfSmlkPreemptionMode_Type.__name__ = "Integer32"
_HpnicfSmlkPreemptionMode_Object = MibTableColumn
hpnicfSmlkPreemptionMode = _HpnicfSmlkPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 3),
    _HpnicfSmlkPreemptionMode_Type()
)
hpnicfSmlkPreemptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkPreemptionMode.setStatus("current")


class _HpnicfSmlkSpeedThreshold_Type(Integer32):
    """Custom type hpnicfSmlkSpeedThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HpnicfSmlkSpeedThreshold_Type.__name__ = "Integer32"
_HpnicfSmlkSpeedThreshold_Object = MibTableColumn
hpnicfSmlkSpeedThreshold = _HpnicfSmlkSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 4),
    _HpnicfSmlkSpeedThreshold_Type()
)
hpnicfSmlkSpeedThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkSpeedThreshold.setStatus("current")


class _HpnicfSmlkPreemptionDelay_Type(Integer32):
    """Custom type hpnicfSmlkPreemptionDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HpnicfSmlkPreemptionDelay_Type.__name__ = "Integer32"
_HpnicfSmlkPreemptionDelay_Object = MibTableColumn
hpnicfSmlkPreemptionDelay = _HpnicfSmlkPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 5),
    _HpnicfSmlkPreemptionDelay_Type()
)
hpnicfSmlkPreemptionDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkPreemptionDelay.setStatus("current")


class _HpnicfSmlkControlVlanID_Type(Integer32):
    """Custom type hpnicfSmlkControlVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfSmlkControlVlanID_Type.__name__ = "Integer32"
_HpnicfSmlkControlVlanID_Object = MibTableColumn
hpnicfSmlkControlVlanID = _HpnicfSmlkControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 6),
    _HpnicfSmlkControlVlanID_Type()
)
hpnicfSmlkControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkControlVlanID.setStatus("current")


class _HpnicfSmlkInstanceListLow_Type(OctetString):
    """Custom type hpnicfSmlkInstanceListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfSmlkInstanceListLow_Type.__name__ = "OctetString"
_HpnicfSmlkInstanceListLow_Object = MibTableColumn
hpnicfSmlkInstanceListLow = _HpnicfSmlkInstanceListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 7),
    _HpnicfSmlkInstanceListLow_Type()
)
hpnicfSmlkInstanceListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkInstanceListLow.setStatus("current")


class _HpnicfSmlkInstanceListHigh_Type(OctetString):
    """Custom type hpnicfSmlkInstanceListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfSmlkInstanceListHigh_Type.__name__ = "OctetString"
_HpnicfSmlkInstanceListHigh_Object = MibTableColumn
hpnicfSmlkInstanceListHigh = _HpnicfSmlkInstanceListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 8),
    _HpnicfSmlkInstanceListHigh_Type()
)
hpnicfSmlkInstanceListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkInstanceListHigh.setStatus("current")
_HpnicfSmlkGroupRowStatus_Type = RowStatus
_HpnicfSmlkGroupRowStatus_Object = MibTableColumn
hpnicfSmlkGroupRowStatus = _HpnicfSmlkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 9),
    _HpnicfSmlkGroupRowStatus_Type()
)
hpnicfSmlkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkGroupRowStatus.setStatus("current")
_HpnicfSmlkPortTable_Object = MibTable
hpnicfSmlkPortTable = _HpnicfSmlkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfSmlkPortTable.setStatus("current")
_HpnicfSmlkPortEntry_Object = MibTableRow
hpnicfSmlkPortEntry = _HpnicfSmlkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1)
)
hpnicfSmlkPortEntry.setIndexNames(
    (0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkGroupID"),
    (0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkPortIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSmlkPortEntry.setStatus("current")
_HpnicfSmlkPortIfIndex_Type = InterfaceIndex
_HpnicfSmlkPortIfIndex_Object = MibTableColumn
hpnicfSmlkPortIfIndex = _HpnicfSmlkPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 1),
    _HpnicfSmlkPortIfIndex_Type()
)
hpnicfSmlkPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSmlkPortIfIndex.setStatus("current")


class _HpnicfSmlkPortRole_Type(Integer32):
    """Custom type hpnicfSmlkPortRole based on Integer32"""
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


_HpnicfSmlkPortRole_Type.__name__ = "Integer32"
_HpnicfSmlkPortRole_Object = MibTableColumn
hpnicfSmlkPortRole = _HpnicfSmlkPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 2),
    _HpnicfSmlkPortRole_Type()
)
hpnicfSmlkPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkPortRole.setStatus("current")


class _HpnicfSmlkPortStatus_Type(Integer32):
    """Custom type hpnicfSmlkPortStatus based on Integer32"""
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


_HpnicfSmlkPortStatus_Type.__name__ = "Integer32"
_HpnicfSmlkPortStatus_Object = MibTableColumn
hpnicfSmlkPortStatus = _HpnicfSmlkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 3),
    _HpnicfSmlkPortStatus_Type()
)
hpnicfSmlkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSmlkPortStatus.setStatus("current")
_HpnicfSmlkFlushCount_Type = Counter64
_HpnicfSmlkFlushCount_Object = MibTableColumn
hpnicfSmlkFlushCount = _HpnicfSmlkFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 4),
    _HpnicfSmlkFlushCount_Type()
)
hpnicfSmlkFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSmlkFlushCount.setStatus("current")
_HpnicfSmlkLastFlushTime_Type = DateAndTime
_HpnicfSmlkLastFlushTime_Object = MibTableColumn
hpnicfSmlkLastFlushTime = _HpnicfSmlkLastFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 5),
    _HpnicfSmlkLastFlushTime_Type()
)
hpnicfSmlkLastFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSmlkLastFlushTime.setStatus("current")
_HpnicfSmlkPortRowStatus_Type = RowStatus
_HpnicfSmlkPortRowStatus_Object = MibTableColumn
hpnicfSmlkPortRowStatus = _HpnicfSmlkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 6),
    _HpnicfSmlkPortRowStatus_Type()
)
hpnicfSmlkPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSmlkPortRowStatus.setStatus("current")
_HpnicfSmlkFlushEnableTable_Object = MibTable
hpnicfSmlkFlushEnableTable = _HpnicfSmlkFlushEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfSmlkFlushEnableTable.setStatus("current")
_HpnicfSmlkFlushEnableEntry_Object = MibTableRow
hpnicfSmlkFlushEnableEntry = _HpnicfSmlkFlushEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1)
)
hpnicfSmlkFlushEnableEntry.setIndexNames(
    (0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSmlkFlushEnableEntry.setStatus("current")
_HpnicfSmlkIfIndex_Type = InterfaceIndex
_HpnicfSmlkIfIndex_Object = MibTableColumn
hpnicfSmlkIfIndex = _HpnicfSmlkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1, 1),
    _HpnicfSmlkIfIndex_Type()
)
hpnicfSmlkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSmlkIfIndex.setStatus("current")


class _HpnicfSmlkControlVlanListLow_Type(OctetString):
    """Custom type hpnicfSmlkControlVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfSmlkControlVlanListLow_Type.__name__ = "OctetString"
_HpnicfSmlkControlVlanListLow_Object = MibTableColumn
hpnicfSmlkControlVlanListLow = _HpnicfSmlkControlVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1, 2),
    _HpnicfSmlkControlVlanListLow_Type()
)
hpnicfSmlkControlVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmlkControlVlanListLow.setStatus("current")


class _HpnicfSmlkControlVlanListHigh_Type(OctetString):
    """Custom type hpnicfSmlkControlVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfSmlkControlVlanListHigh_Type.__name__ = "OctetString"
_HpnicfSmlkControlVlanListHigh_Object = MibTableColumn
hpnicfSmlkControlVlanListHigh = _HpnicfSmlkControlVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1, 3),
    _HpnicfSmlkControlVlanListHigh_Type()
)
hpnicfSmlkControlVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmlkControlVlanListHigh.setStatus("current")
_HpnicfSmlkTrap_ObjectIdentity = ObjectIdentity
hpnicfSmlkTrap = _HpnicfSmlkTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 2)
)
_HpnicfSmlkTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfSmlkTrapPrefix = _HpnicfSmlkTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfSmlkGroupLinkActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 2, 0, 1)
)
hpnicfSmlkGroupLinkActive.setObjects(
      *(("HPN-ICF-SMLK-MIB", "hpnicfSmlkGroupID"),
        ("HPN-ICF-SMLK-MIB", "hpnicfSmlkPortIfIndex"))
)
if mibBuilder.loadTexts:
    hpnicfSmlkGroupLinkActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SMLK-MIB",
    **{"hpnicfSmlk": hpnicfSmlk,
       "hpnicfSmlkObject": hpnicfSmlkObject,
       "hpnicfSmlkGroupTable": hpnicfSmlkGroupTable,
       "hpnicfSmlkGroupEntry": hpnicfSmlkGroupEntry,
       "hpnicfSmlkGroupID": hpnicfSmlkGroupID,
       "hpnicfSmlkDeviceID": hpnicfSmlkDeviceID,
       "hpnicfSmlkPreemptionMode": hpnicfSmlkPreemptionMode,
       "hpnicfSmlkSpeedThreshold": hpnicfSmlkSpeedThreshold,
       "hpnicfSmlkPreemptionDelay": hpnicfSmlkPreemptionDelay,
       "hpnicfSmlkControlVlanID": hpnicfSmlkControlVlanID,
       "hpnicfSmlkInstanceListLow": hpnicfSmlkInstanceListLow,
       "hpnicfSmlkInstanceListHigh": hpnicfSmlkInstanceListHigh,
       "hpnicfSmlkGroupRowStatus": hpnicfSmlkGroupRowStatus,
       "hpnicfSmlkPortTable": hpnicfSmlkPortTable,
       "hpnicfSmlkPortEntry": hpnicfSmlkPortEntry,
       "hpnicfSmlkPortIfIndex": hpnicfSmlkPortIfIndex,
       "hpnicfSmlkPortRole": hpnicfSmlkPortRole,
       "hpnicfSmlkPortStatus": hpnicfSmlkPortStatus,
       "hpnicfSmlkFlushCount": hpnicfSmlkFlushCount,
       "hpnicfSmlkLastFlushTime": hpnicfSmlkLastFlushTime,
       "hpnicfSmlkPortRowStatus": hpnicfSmlkPortRowStatus,
       "hpnicfSmlkFlushEnableTable": hpnicfSmlkFlushEnableTable,
       "hpnicfSmlkFlushEnableEntry": hpnicfSmlkFlushEnableEntry,
       "hpnicfSmlkIfIndex": hpnicfSmlkIfIndex,
       "hpnicfSmlkControlVlanListLow": hpnicfSmlkControlVlanListLow,
       "hpnicfSmlkControlVlanListHigh": hpnicfSmlkControlVlanListHigh,
       "hpnicfSmlkTrap": hpnicfSmlkTrap,
       "hpnicfSmlkTrapPrefix": hpnicfSmlkTrapPrefix,
       "hpnicfSmlkGroupLinkActive": hpnicfSmlkGroupLinkActive}
)
