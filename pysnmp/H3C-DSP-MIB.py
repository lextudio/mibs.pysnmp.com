# SNMP MIB module (H3C-DSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:20 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cDSP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89)
)
h3cDSP.setRevisions(
        ("2008-01-16 13:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVPMStatusTable_Object = MibTable
h3cVPMStatusTable = _H3cVPMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1)
)
if mibBuilder.loadTexts:
    h3cVPMStatusTable.setStatus("current")
_H3cVPMStatusEntry_Object = MibTableRow
h3cVPMStatusEntry = _H3cVPMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1)
)
h3cVPMStatusEntry.setIndexNames(
    (0, "H3C-DSP-MIB", "h3cVPMIndex"),
)
if mibBuilder.loadTexts:
    h3cVPMStatusEntry.setStatus("current")


class _H3cVPMIndex_Type(Integer32):
    """Custom type h3cVPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cVPMIndex_Type.__name__ = "Integer32"
_H3cVPMIndex_Object = MibTableColumn
h3cVPMIndex = _H3cVPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 1),
    _H3cVPMIndex_Type()
)
h3cVPMIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVPMIndex.setStatus("current")
_H3cVPMEnPhysicalIndex_Type = PhysicalIndex
_H3cVPMEnPhysicalIndex_Object = MibTableColumn
h3cVPMEnPhysicalIndex = _H3cVPMEnPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 2),
    _H3cVPMEnPhysicalIndex_Type()
)
h3cVPMEnPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVPMEnPhysicalIndex.setStatus("current")


class _H3cVPMState_Type(Integer32):
    """Custom type h3cVPMState based on Integer32"""
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


_H3cVPMState_Type.__name__ = "Integer32"
_H3cVPMState_Object = MibTableColumn
h3cVPMState = _H3cVPMState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 3),
    _H3cVPMState_Type()
)
h3cVPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVPMState.setStatus("current")


class _H3cVPMResourceUtilization_Type(Integer32):
    """Custom type h3cVPMResourceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVPMResourceUtilization_Type.__name__ = "Integer32"
_H3cVPMResourceUtilization_Object = MibTableColumn
h3cVPMResourceUtilization = _H3cVPMResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 4),
    _H3cVPMResourceUtilization_Type()
)
h3cVPMResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVPMResourceUtilization.setStatus("current")


class _H3cVPMHiWaterUtilization_Type(Integer32):
    """Custom type h3cVPMHiWaterUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVPMHiWaterUtilization_Type.__name__ = "Integer32"
_H3cVPMHiWaterUtilization_Object = MibTableColumn
h3cVPMHiWaterUtilization = _H3cVPMHiWaterUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 5),
    _H3cVPMHiWaterUtilization_Type()
)
h3cVPMHiWaterUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVPMHiWaterUtilization.setStatus("current")
_H3cVPMMaxChannel_Type = Integer32
_H3cVPMMaxChannel_Object = MibTableColumn
h3cVPMMaxChannel = _H3cVPMMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 1, 1, 6),
    _H3cVPMMaxChannel_Type()
)
h3cVPMMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVPMMaxChannel.setStatus("current")
_H3cDSPStatusTable_Object = MibTable
h3cDSPStatusTable = _H3cDSPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2)
)
if mibBuilder.loadTexts:
    h3cDSPStatusTable.setStatus("current")
_H3cDSPStatusEntry_Object = MibTableRow
h3cDSPStatusEntry = _H3cDSPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1)
)
h3cDSPStatusEntry.setIndexNames(
    (0, "H3C-DSP-MIB", "h3cDSPIndex"),
)
if mibBuilder.loadTexts:
    h3cDSPStatusEntry.setStatus("current")


class _H3cDSPIndex_Type(Integer32):
    """Custom type h3cDSPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_H3cDSPIndex_Type.__name__ = "Integer32"
_H3cDSPIndex_Object = MibTableColumn
h3cDSPIndex = _H3cDSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 1),
    _H3cDSPIndex_Type()
)
h3cDSPIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDSPIndex.setStatus("current")


class _H3cDSPVPMIndex_Type(Integer32):
    """Custom type h3cDSPVPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_H3cDSPVPMIndex_Type.__name__ = "Integer32"
_H3cDSPVPMIndex_Object = MibTableColumn
h3cDSPVPMIndex = _H3cDSPVPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 2),
    _H3cDSPVPMIndex_Type()
)
h3cDSPVPMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDSPVPMIndex.setStatus("current")
_H3cDSPEnPhysicalIndex_Type = PhysicalIndex
_H3cDSPEnPhysicalIndex_Object = MibTableColumn
h3cDSPEnPhysicalIndex = _H3cDSPEnPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 3),
    _H3cDSPEnPhysicalIndex_Type()
)
h3cDSPEnPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDSPEnPhysicalIndex.setStatus("current")
_H3cDSPResetTime_Type = TimeTicks
_H3cDSPResetTime_Object = MibTableColumn
h3cDSPResetTime = _H3cDSPResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 4),
    _H3cDSPResetTime_Type()
)
h3cDSPResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDSPResetTime.setStatus("current")
_H3cDSPMaxChannel_Type = Integer32
_H3cDSPMaxChannel_Object = MibTableColumn
h3cDSPMaxChannel = _H3cDSPMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 5),
    _H3cDSPMaxChannel_Type()
)
h3cDSPMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDSPMaxChannel.setStatus("current")


class _H3cDSPState_Type(Integer32):
    """Custom type h3cDSPState based on Integer32"""
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


_H3cDSPState_Type.__name__ = "Integer32"
_H3cDSPState_Object = MibTableColumn
h3cDSPState = _H3cDSPState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 6),
    _H3cDSPState_Type()
)
h3cDSPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDSPState.setStatus("current")
_H3cDSPInUseChannel_Type = Integer32
_H3cDSPInUseChannel_Object = MibTableColumn
h3cDSPInUseChannel = _H3cDSPInUseChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 2, 1, 7),
    _H3cDSPInUseChannel_Type()
)
h3cDSPInUseChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDSPInUseChannel.setStatus("current")
_H3cDSPTrap_ObjectIdentity = ObjectIdentity
h3cDSPTrap = _H3cDSPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3)
)
_H3cDSPTrapPrex_ObjectIdentity = ObjectIdentity
h3cDSPTrapPrex = _H3cDSPTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cVPMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3, 0, 1)
)
h3cVPMStateChange.setObjects(
      *(("H3C-DSP-MIB", "h3cVPMIndex"),
        ("H3C-DSP-MIB", "h3cVPMEnPhysicalIndex"),
        ("H3C-DSP-MIB", "h3cVPMState"))
)
if mibBuilder.loadTexts:
    h3cVPMStateChange.setStatus(
        "current"
    )

h3cDSPStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 89, 3, 0, 2)
)
h3cDSPStateChange.setObjects(
      *(("H3C-DSP-MIB", "h3cDSPIndex"),
        ("H3C-DSP-MIB", "h3cDSPVPMIndex"),
        ("H3C-DSP-MIB", "h3cDSPEnPhysicalIndex"),
        ("H3C-DSP-MIB", "h3cDSPState"))
)
if mibBuilder.loadTexts:
    h3cDSPStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DSP-MIB",
    **{"h3cDSP": h3cDSP,
       "h3cVPMStatusTable": h3cVPMStatusTable,
       "h3cVPMStatusEntry": h3cVPMStatusEntry,
       "h3cVPMIndex": h3cVPMIndex,
       "h3cVPMEnPhysicalIndex": h3cVPMEnPhysicalIndex,
       "h3cVPMState": h3cVPMState,
       "h3cVPMResourceUtilization": h3cVPMResourceUtilization,
       "h3cVPMHiWaterUtilization": h3cVPMHiWaterUtilization,
       "h3cVPMMaxChannel": h3cVPMMaxChannel,
       "h3cDSPStatusTable": h3cDSPStatusTable,
       "h3cDSPStatusEntry": h3cDSPStatusEntry,
       "h3cDSPIndex": h3cDSPIndex,
       "h3cDSPVPMIndex": h3cDSPVPMIndex,
       "h3cDSPEnPhysicalIndex": h3cDSPEnPhysicalIndex,
       "h3cDSPResetTime": h3cDSPResetTime,
       "h3cDSPMaxChannel": h3cDSPMaxChannel,
       "h3cDSPState": h3cDSPState,
       "h3cDSPInUseChannel": h3cDSPInUseChannel,
       "h3cDSPTrap": h3cDSPTrap,
       "h3cDSPTrapPrex": h3cDSPTrapPrex,
       "h3cVPMStateChange": h3cVPMStateChange,
       "h3cDSPStateChange": h3cDSPStateChange}
)
