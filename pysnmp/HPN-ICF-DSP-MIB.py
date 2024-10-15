# SNMP MIB module (HPN-ICF-DSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:59 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDSP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89)
)
hpnicfDSP.setRevisions(
        ("2008-01-16 13:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVPMStatusTable_Object = MibTable
hpnicfVPMStatusTable = _HpnicfVPMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1)
)
if mibBuilder.loadTexts:
    hpnicfVPMStatusTable.setStatus("current")
_HpnicfVPMStatusEntry_Object = MibTableRow
hpnicfVPMStatusEntry = _HpnicfVPMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1)
)
hpnicfVPMStatusEntry.setIndexNames(
    (0, "HPN-ICF-DSP-MIB", "hpnicfVPMIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVPMStatusEntry.setStatus("current")


class _HpnicfVPMIndex_Type(Integer32):
    """Custom type hpnicfVPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfVPMIndex_Type.__name__ = "Integer32"
_HpnicfVPMIndex_Object = MibTableColumn
hpnicfVPMIndex = _HpnicfVPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 1),
    _HpnicfVPMIndex_Type()
)
hpnicfVPMIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfVPMIndex.setStatus("current")
_HpnicfVPMEnPhysicalIndex_Type = PhysicalIndex
_HpnicfVPMEnPhysicalIndex_Object = MibTableColumn
hpnicfVPMEnPhysicalIndex = _HpnicfVPMEnPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 2),
    _HpnicfVPMEnPhysicalIndex_Type()
)
hpnicfVPMEnPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVPMEnPhysicalIndex.setStatus("current")


class _HpnicfVPMState_Type(Integer32):
    """Custom type hpnicfVPMState based on Integer32"""
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


_HpnicfVPMState_Type.__name__ = "Integer32"
_HpnicfVPMState_Object = MibTableColumn
hpnicfVPMState = _HpnicfVPMState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 3),
    _HpnicfVPMState_Type()
)
hpnicfVPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVPMState.setStatus("current")


class _HpnicfVPMResourceUtilization_Type(Integer32):
    """Custom type hpnicfVPMResourceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfVPMResourceUtilization_Type.__name__ = "Integer32"
_HpnicfVPMResourceUtilization_Object = MibTableColumn
hpnicfVPMResourceUtilization = _HpnicfVPMResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 4),
    _HpnicfVPMResourceUtilization_Type()
)
hpnicfVPMResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVPMResourceUtilization.setStatus("current")


class _HpnicfVPMHiWaterUtilization_Type(Integer32):
    """Custom type hpnicfVPMHiWaterUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfVPMHiWaterUtilization_Type.__name__ = "Integer32"
_HpnicfVPMHiWaterUtilization_Object = MibTableColumn
hpnicfVPMHiWaterUtilization = _HpnicfVPMHiWaterUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 5),
    _HpnicfVPMHiWaterUtilization_Type()
)
hpnicfVPMHiWaterUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVPMHiWaterUtilization.setStatus("current")
_HpnicfVPMMaxChannel_Type = Integer32
_HpnicfVPMMaxChannel_Object = MibTableColumn
hpnicfVPMMaxChannel = _HpnicfVPMMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 6),
    _HpnicfVPMMaxChannel_Type()
)
hpnicfVPMMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVPMMaxChannel.setStatus("current")
_HpnicfDSPStatusTable_Object = MibTable
hpnicfDSPStatusTable = _HpnicfDSPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2)
)
if mibBuilder.loadTexts:
    hpnicfDSPStatusTable.setStatus("current")
_HpnicfDSPStatusEntry_Object = MibTableRow
hpnicfDSPStatusEntry = _HpnicfDSPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1)
)
hpnicfDSPStatusEntry.setIndexNames(
    (0, "HPN-ICF-DSP-MIB", "hpnicfDSPIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDSPStatusEntry.setStatus("current")


class _HpnicfDSPIndex_Type(Integer32):
    """Custom type hpnicfDSPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpnicfDSPIndex_Type.__name__ = "Integer32"
_HpnicfDSPIndex_Object = MibTableColumn
hpnicfDSPIndex = _HpnicfDSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 1),
    _HpnicfDSPIndex_Type()
)
hpnicfDSPIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDSPIndex.setStatus("current")


class _HpnicfDSPVPMIndex_Type(Integer32):
    """Custom type hpnicfDSPVPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HpnicfDSPVPMIndex_Type.__name__ = "Integer32"
_HpnicfDSPVPMIndex_Object = MibTableColumn
hpnicfDSPVPMIndex = _HpnicfDSPVPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 2),
    _HpnicfDSPVPMIndex_Type()
)
hpnicfDSPVPMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDSPVPMIndex.setStatus("current")
_HpnicfDSPEnPhysicalIndex_Type = PhysicalIndex
_HpnicfDSPEnPhysicalIndex_Object = MibTableColumn
hpnicfDSPEnPhysicalIndex = _HpnicfDSPEnPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 3),
    _HpnicfDSPEnPhysicalIndex_Type()
)
hpnicfDSPEnPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDSPEnPhysicalIndex.setStatus("current")
_HpnicfDSPResetTime_Type = TimeTicks
_HpnicfDSPResetTime_Object = MibTableColumn
hpnicfDSPResetTime = _HpnicfDSPResetTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 4),
    _HpnicfDSPResetTime_Type()
)
hpnicfDSPResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDSPResetTime.setStatus("current")
_HpnicfDSPMaxChannel_Type = Integer32
_HpnicfDSPMaxChannel_Object = MibTableColumn
hpnicfDSPMaxChannel = _HpnicfDSPMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 5),
    _HpnicfDSPMaxChannel_Type()
)
hpnicfDSPMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDSPMaxChannel.setStatus("current")


class _HpnicfDSPState_Type(Integer32):
    """Custom type hpnicfDSPState based on Integer32"""
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


_HpnicfDSPState_Type.__name__ = "Integer32"
_HpnicfDSPState_Object = MibTableColumn
hpnicfDSPState = _HpnicfDSPState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 6),
    _HpnicfDSPState_Type()
)
hpnicfDSPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDSPState.setStatus("current")
_HpnicfDSPInUseChannel_Type = Integer32
_HpnicfDSPInUseChannel_Object = MibTableColumn
hpnicfDSPInUseChannel = _HpnicfDSPInUseChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 7),
    _HpnicfDSPInUseChannel_Type()
)
hpnicfDSPInUseChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDSPInUseChannel.setStatus("current")
_HpnicfDSPTrap_ObjectIdentity = ObjectIdentity
hpnicfDSPTrap = _HpnicfDSPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3)
)
_HpnicfDSPTrapPrex_ObjectIdentity = ObjectIdentity
hpnicfDSPTrapPrex = _HpnicfDSPTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfVPMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3, 0, 1)
)
hpnicfVPMStateChange.setObjects(
      *(("HPN-ICF-DSP-MIB", "hpnicfVPMIndex"),
        ("HPN-ICF-DSP-MIB", "hpnicfVPMEnPhysicalIndex"),
        ("HPN-ICF-DSP-MIB", "hpnicfVPMState"))
)
if mibBuilder.loadTexts:
    hpnicfVPMStateChange.setStatus(
        "current"
    )

hpnicfDSPStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3, 0, 2)
)
hpnicfDSPStateChange.setObjects(
      *(("HPN-ICF-DSP-MIB", "hpnicfDSPIndex"),
        ("HPN-ICF-DSP-MIB", "hpnicfDSPVPMIndex"),
        ("HPN-ICF-DSP-MIB", "hpnicfDSPEnPhysicalIndex"),
        ("HPN-ICF-DSP-MIB", "hpnicfDSPState"))
)
if mibBuilder.loadTexts:
    hpnicfDSPStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DSP-MIB",
    **{"hpnicfDSP": hpnicfDSP,
       "hpnicfVPMStatusTable": hpnicfVPMStatusTable,
       "hpnicfVPMStatusEntry": hpnicfVPMStatusEntry,
       "hpnicfVPMIndex": hpnicfVPMIndex,
       "hpnicfVPMEnPhysicalIndex": hpnicfVPMEnPhysicalIndex,
       "hpnicfVPMState": hpnicfVPMState,
       "hpnicfVPMResourceUtilization": hpnicfVPMResourceUtilization,
       "hpnicfVPMHiWaterUtilization": hpnicfVPMHiWaterUtilization,
       "hpnicfVPMMaxChannel": hpnicfVPMMaxChannel,
       "hpnicfDSPStatusTable": hpnicfDSPStatusTable,
       "hpnicfDSPStatusEntry": hpnicfDSPStatusEntry,
       "hpnicfDSPIndex": hpnicfDSPIndex,
       "hpnicfDSPVPMIndex": hpnicfDSPVPMIndex,
       "hpnicfDSPEnPhysicalIndex": hpnicfDSPEnPhysicalIndex,
       "hpnicfDSPResetTime": hpnicfDSPResetTime,
       "hpnicfDSPMaxChannel": hpnicfDSPMaxChannel,
       "hpnicfDSPState": hpnicfDSPState,
       "hpnicfDSPInUseChannel": hpnicfDSPInUseChannel,
       "hpnicfDSPTrap": hpnicfDSPTrap,
       "hpnicfDSPTrapPrex": hpnicfDSPTrapPrex,
       "hpnicfVPMStateChange": hpnicfVPMStateChange,
       "hpnicfDSPStateChange": hpnicfDSPStateChange}
)
