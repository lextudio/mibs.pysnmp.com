# SNMP MIB module (HH3C-DSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:00 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cDSP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89)
)
hh3cDSP.setRevisions(
        ("2008-01-16 13:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVPMStatusTable_Object = MibTable
hh3cVPMStatusTable = _Hh3cVPMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1)
)
if mibBuilder.loadTexts:
    hh3cVPMStatusTable.setStatus("current")
_Hh3cVPMStatusEntry_Object = MibTableRow
hh3cVPMStatusEntry = _Hh3cVPMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1)
)
hh3cVPMStatusEntry.setIndexNames(
    (0, "HH3C-DSP-MIB", "hh3cVPMIndex"),
)
if mibBuilder.loadTexts:
    hh3cVPMStatusEntry.setStatus("current")


class _Hh3cVPMIndex_Type(Integer32):
    """Custom type hh3cVPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cVPMIndex_Type.__name__ = "Integer32"
_Hh3cVPMIndex_Object = MibTableColumn
hh3cVPMIndex = _Hh3cVPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1, 1),
    _Hh3cVPMIndex_Type()
)
hh3cVPMIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVPMIndex.setStatus("current")
_Hh3cVPMEnPhysicalIndex_Type = PhysicalIndex
_Hh3cVPMEnPhysicalIndex_Object = MibTableColumn
hh3cVPMEnPhysicalIndex = _Hh3cVPMEnPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1, 2),
    _Hh3cVPMEnPhysicalIndex_Type()
)
hh3cVPMEnPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVPMEnPhysicalIndex.setStatus("current")


class _Hh3cVPMState_Type(Integer32):
    """Custom type hh3cVPMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fatal", 3),
          ("normal", 1),
          ("offLine", 4),
          ("warning", 2))
    )


_Hh3cVPMState_Type.__name__ = "Integer32"
_Hh3cVPMState_Object = MibTableColumn
hh3cVPMState = _Hh3cVPMState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1, 3),
    _Hh3cVPMState_Type()
)
hh3cVPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVPMState.setStatus("current")


class _Hh3cVPMResourceUtilization_Type(Integer32):
    """Custom type hh3cVPMResourceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVPMResourceUtilization_Type.__name__ = "Integer32"
_Hh3cVPMResourceUtilization_Object = MibTableColumn
hh3cVPMResourceUtilization = _Hh3cVPMResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1, 4),
    _Hh3cVPMResourceUtilization_Type()
)
hh3cVPMResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVPMResourceUtilization.setStatus("current")


class _Hh3cVPMHiWaterUtilization_Type(Integer32):
    """Custom type hh3cVPMHiWaterUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVPMHiWaterUtilization_Type.__name__ = "Integer32"
_Hh3cVPMHiWaterUtilization_Object = MibTableColumn
hh3cVPMHiWaterUtilization = _Hh3cVPMHiWaterUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1, 5),
    _Hh3cVPMHiWaterUtilization_Type()
)
hh3cVPMHiWaterUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVPMHiWaterUtilization.setStatus("current")
_Hh3cVPMMaxChannel_Type = Integer32
_Hh3cVPMMaxChannel_Object = MibTableColumn
hh3cVPMMaxChannel = _Hh3cVPMMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 1, 1, 6),
    _Hh3cVPMMaxChannel_Type()
)
hh3cVPMMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVPMMaxChannel.setStatus("current")
_Hh3cDSPStatusTable_Object = MibTable
hh3cDSPStatusTable = _Hh3cDSPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2)
)
if mibBuilder.loadTexts:
    hh3cDSPStatusTable.setStatus("current")
_Hh3cDSPStatusEntry_Object = MibTableRow
hh3cDSPStatusEntry = _Hh3cDSPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1)
)
hh3cDSPStatusEntry.setIndexNames(
    (0, "HH3C-DSP-MIB", "hh3cDSPIndex"),
)
if mibBuilder.loadTexts:
    hh3cDSPStatusEntry.setStatus("current")


class _Hh3cDSPIndex_Type(Integer32):
    """Custom type hh3cDSPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cDSPIndex_Type.__name__ = "Integer32"
_Hh3cDSPIndex_Object = MibTableColumn
hh3cDSPIndex = _Hh3cDSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 1),
    _Hh3cDSPIndex_Type()
)
hh3cDSPIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDSPIndex.setStatus("current")


class _Hh3cDSPVPMIndex_Type(Integer32):
    """Custom type hh3cDSPVPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cDSPVPMIndex_Type.__name__ = "Integer32"
_Hh3cDSPVPMIndex_Object = MibTableColumn
hh3cDSPVPMIndex = _Hh3cDSPVPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 2),
    _Hh3cDSPVPMIndex_Type()
)
hh3cDSPVPMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDSPVPMIndex.setStatus("current")
_Hh3cDSPEnPhysicalIndex_Type = PhysicalIndex
_Hh3cDSPEnPhysicalIndex_Object = MibTableColumn
hh3cDSPEnPhysicalIndex = _Hh3cDSPEnPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 3),
    _Hh3cDSPEnPhysicalIndex_Type()
)
hh3cDSPEnPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDSPEnPhysicalIndex.setStatus("current")
_Hh3cDSPResetTime_Type = TimeTicks
_Hh3cDSPResetTime_Object = MibTableColumn
hh3cDSPResetTime = _Hh3cDSPResetTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 4),
    _Hh3cDSPResetTime_Type()
)
hh3cDSPResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDSPResetTime.setStatus("current")
_Hh3cDSPMaxChannel_Type = Integer32
_Hh3cDSPMaxChannel_Object = MibTableColumn
hh3cDSPMaxChannel = _Hh3cDSPMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 5),
    _Hh3cDSPMaxChannel_Type()
)
hh3cDSPMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDSPMaxChannel.setStatus("current")


class _Hh3cDSPState_Type(Integer32):
    """Custom type hh3cDSPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fatal", 3),
          ("normal", 1),
          ("offLine", 4))
    )


_Hh3cDSPState_Type.__name__ = "Integer32"
_Hh3cDSPState_Object = MibTableColumn
hh3cDSPState = _Hh3cDSPState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 6),
    _Hh3cDSPState_Type()
)
hh3cDSPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDSPState.setStatus("current")
_Hh3cDSPInUseChannel_Type = Integer32
_Hh3cDSPInUseChannel_Object = MibTableColumn
hh3cDSPInUseChannel = _Hh3cDSPInUseChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 2, 1, 7),
    _Hh3cDSPInUseChannel_Type()
)
hh3cDSPInUseChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDSPInUseChannel.setStatus("current")
_Hh3cDSPTrap_ObjectIdentity = ObjectIdentity
hh3cDSPTrap = _Hh3cDSPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 3)
)
_Hh3cDSPTrapPrex_ObjectIdentity = ObjectIdentity
hh3cDSPTrapPrex = _Hh3cDSPTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cVPMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 3, 0, 1)
)
hh3cVPMStateChange.setObjects(
      *(("HH3C-DSP-MIB", "hh3cVPMIndex"),
        ("HH3C-DSP-MIB", "hh3cVPMEnPhysicalIndex"),
        ("HH3C-DSP-MIB", "hh3cVPMState"))
)
if mibBuilder.loadTexts:
    hh3cVPMStateChange.setStatus(
        "current"
    )

hh3cDSPStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89, 3, 0, 2)
)
hh3cDSPStateChange.setObjects(
      *(("HH3C-DSP-MIB", "hh3cDSPIndex"),
        ("HH3C-DSP-MIB", "hh3cDSPVPMIndex"),
        ("HH3C-DSP-MIB", "hh3cDSPEnPhysicalIndex"),
        ("HH3C-DSP-MIB", "hh3cDSPState"))
)
if mibBuilder.loadTexts:
    hh3cDSPStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DSP-MIB",
    **{"hh3cDSP": hh3cDSP,
       "hh3cVPMStatusTable": hh3cVPMStatusTable,
       "hh3cVPMStatusEntry": hh3cVPMStatusEntry,
       "hh3cVPMIndex": hh3cVPMIndex,
       "hh3cVPMEnPhysicalIndex": hh3cVPMEnPhysicalIndex,
       "hh3cVPMState": hh3cVPMState,
       "hh3cVPMResourceUtilization": hh3cVPMResourceUtilization,
       "hh3cVPMHiWaterUtilization": hh3cVPMHiWaterUtilization,
       "hh3cVPMMaxChannel": hh3cVPMMaxChannel,
       "hh3cDSPStatusTable": hh3cDSPStatusTable,
       "hh3cDSPStatusEntry": hh3cDSPStatusEntry,
       "hh3cDSPIndex": hh3cDSPIndex,
       "hh3cDSPVPMIndex": hh3cDSPVPMIndex,
       "hh3cDSPEnPhysicalIndex": hh3cDSPEnPhysicalIndex,
       "hh3cDSPResetTime": hh3cDSPResetTime,
       "hh3cDSPMaxChannel": hh3cDSPMaxChannel,
       "hh3cDSPState": hh3cDSPState,
       "hh3cDSPInUseChannel": hh3cDSPInUseChannel,
       "hh3cDSPTrap": hh3cDSPTrap,
       "hh3cDSPTrapPrex": hh3cDSPTrapPrex,
       "hh3cVPMStateChange": hh3cVPMStateChange,
       "hh3cDSPStateChange": hh3cDSPStateChange}
)
