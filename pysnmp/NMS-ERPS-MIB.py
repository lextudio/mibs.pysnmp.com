# SNMP MIB module (NMS-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-ERPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:53 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsERPS_ObjectIdentity = ObjectIdentity
nmsERPS = _NmsERPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231)
)
_NmsERPSRings_Type = Integer32
_NmsERPSRings_Object = MibScalar
nmsERPSRings = _NmsERPSRings_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 1),
    _NmsERPSRings_Type()
)
nmsERPSRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRings.setStatus("mandatory")


class _NmsERPSInconsistenceCheck_Type(Integer32):
    """Custom type nmsERPSInconsistenceCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NmsERPSInconsistenceCheck_Type.__name__ = "Integer32"
_NmsERPSInconsistenceCheck_Object = MibScalar
nmsERPSInconsistenceCheck = _NmsERPSInconsistenceCheck_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 2),
    _NmsERPSInconsistenceCheck_Type()
)
nmsERPSInconsistenceCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSInconsistenceCheck.setStatus("mandatory")
_NmsERPSPduRx_Type = Integer32
_NmsERPSPduRx_Object = MibScalar
nmsERPSPduRx = _NmsERPSPduRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 3),
    _NmsERPSPduRx_Type()
)
nmsERPSPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSPduRx.setStatus("mandatory")
_NmsERPSPduRxDropped_Type = Integer32
_NmsERPSPduRxDropped_Object = MibScalar
nmsERPSPduRxDropped = _NmsERPSPduRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 4),
    _NmsERPSPduRxDropped_Type()
)
nmsERPSPduRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSPduRxDropped.setStatus("mandatory")
_NmsERPSPduTx_Type = Integer32
_NmsERPSPduTx_Object = MibScalar
nmsERPSPduTx = _NmsERPSPduTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 5),
    _NmsERPSPduTx_Type()
)
nmsERPSPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSPduTx.setStatus("mandatory")
_NmsERPSRingTable_Object = MibTable
nmsERPSRingTable = _NmsERPSRingTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6)
)
if mibBuilder.loadTexts:
    nmsERPSRingTable.setStatus("mandatory")
_NmsERPSRingTableEntry_Object = MibTableRow
nmsERPSRingTableEntry = _NmsERPSRingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1)
)
nmsERPSRingTableEntry.setIndexNames(
    (0, "NMS-ERPS-MIB", "nmsERPSRingID"),
)
if mibBuilder.loadTexts:
    nmsERPSRingTableEntry.setStatus("mandatory")
_NmsERPSRingID_Type = Integer32
_NmsERPSRingID_Object = MibTableColumn
nmsERPSRingID = _NmsERPSRingID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 1),
    _NmsERPSRingID_Type()
)
nmsERPSRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingID.setStatus("mandatory")


class _NmsERPSRingNodeID_Type(DisplayString):
    """Custom type nmsERPSRingNodeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsERPSRingNodeID_Type.__name__ = "DisplayString"
_NmsERPSRingNodeID_Object = MibTableColumn
nmsERPSRingNodeID = _NmsERPSRingNodeID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 2),
    _NmsERPSRingNodeID_Type()
)
nmsERPSRingNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingNodeID.setStatus("mandatory")
_NmsERPSRingPorts_Type = Integer32
_NmsERPSRingPorts_Object = MibTableColumn
nmsERPSRingPorts = _NmsERPSRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 3),
    _NmsERPSRingPorts_Type()
)
nmsERPSRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPorts.setStatus("mandatory")


class _NmsERPSRingRole_Type(Integer32):
    """Custom type nmsERPSRingRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRplOwner", 0),
          ("rplOwner", 1))
    )


_NmsERPSRingRole_Type.__name__ = "Integer32"
_NmsERPSRingRole_Object = MibTableColumn
nmsERPSRingRole = _NmsERPSRingRole_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 4),
    _NmsERPSRingRole_Type()
)
nmsERPSRingRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingRole.setStatus("mandatory")


class _NmsERPSRingState_Type(Integer32):
    """Custom type nmsERPSRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("protection", 1))
    )


_NmsERPSRingState_Type.__name__ = "Integer32"
_NmsERPSRingState_Object = MibTableColumn
nmsERPSRingState = _NmsERPSRingState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 5),
    _NmsERPSRingState_Type()
)
nmsERPSRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingState.setStatus("mandatory")


class _NmsERPSRingWTR_Type(Integer32):
    """Custom type nmsERPSRingWTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notWaitToRestore", 0),
          ("waitToRestore", 1))
    )


_NmsERPSRingWTR_Type.__name__ = "Integer32"
_NmsERPSRingWTR_Object = MibTableColumn
nmsERPSRingWTR = _NmsERPSRingWTR_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 6),
    _NmsERPSRingWTR_Type()
)
nmsERPSRingWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingWTR.setStatus("mandatory")
_NmsERPSRingWtrWhile_Type = Integer32
_NmsERPSRingWtrWhile_Object = MibTableColumn
nmsERPSRingWtrWhile = _NmsERPSRingWtrWhile_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 7),
    _NmsERPSRingWtrWhile_Type()
)
nmsERPSRingWtrWhile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingWtrWhile.setStatus("mandatory")


class _NmsERPSRingSignalFail_Type(Integer32):
    """Custom type nmsERPSRingSignalFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noSignalFail", 0),
          ("signalFail", 1))
    )


_NmsERPSRingSignalFail_Type.__name__ = "Integer32"
_NmsERPSRingSignalFail_Object = MibTableColumn
nmsERPSRingSignalFail = _NmsERPSRingSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 8),
    _NmsERPSRingSignalFail_Type()
)
nmsERPSRingSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingSignalFail.setStatus("mandatory")


class _NmsERPSRingSending_Type(DisplayString):
    """Custom type nmsERPSRingSending based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsERPSRingSending_Type.__name__ = "DisplayString"
_NmsERPSRingSending_Object = MibTableColumn
nmsERPSRingSending = _NmsERPSRingSending_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 9),
    _NmsERPSRingSending_Type()
)
nmsERPSRingSending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingSending.setStatus("mandatory")


class _NmsERPSRingRplOwnerID_Type(DisplayString):
    """Custom type nmsERPSRingRplOwnerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsERPSRingRplOwnerID_Type.__name__ = "DisplayString"
_NmsERPSRingRplOwnerID_Object = MibTableColumn
nmsERPSRingRplOwnerID = _NmsERPSRingRplOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 10),
    _NmsERPSRingRplOwnerID_Type()
)
nmsERPSRingRplOwnerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingRplOwnerID.setStatus("mandatory")


class _NmsERPSRingRplOwnerMAC_Type(DisplayString):
    """Custom type nmsERPSRingRplOwnerMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsERPSRingRplOwnerMAC_Type.__name__ = "DisplayString"
_NmsERPSRingRplOwnerMAC_Object = MibTableColumn
nmsERPSRingRplOwnerMAC = _NmsERPSRingRplOwnerMAC_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 11),
    _NmsERPSRingRplOwnerMAC_Type()
)
nmsERPSRingRplOwnerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingRplOwnerMAC.setStatus("mandatory")


class _NmsERPSRingDiscovering_Type(Integer32):
    """Custom type nmsERPSRingDiscovering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("discovering", 1),
          ("enabled", 3),
          ("notDiscovering", 0))
    )


_NmsERPSRingDiscovering_Type.__name__ = "Integer32"
_NmsERPSRingDiscovering_Object = MibTableColumn
nmsERPSRingDiscovering = _NmsERPSRingDiscovering_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 12),
    _NmsERPSRingDiscovering_Type()
)
nmsERPSRingDiscovering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingDiscovering.setStatus("mandatory")
_NmsERPSRingDiscoverWhile_Type = Integer32
_NmsERPSRingDiscoverWhile_Object = MibTableColumn
nmsERPSRingDiscoverWhile = _NmsERPSRingDiscoverWhile_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 13),
    _NmsERPSRingDiscoverWhile_Type()
)
nmsERPSRingDiscoverWhile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingDiscoverWhile.setStatus("mandatory")
_NmsERPSRingPriorityValue_Type = Integer32
_NmsERPSRingPriorityValue_Object = MibTableColumn
nmsERPSRingPriorityValue = _NmsERPSRingPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 14),
    _NmsERPSRingPriorityValue_Type()
)
nmsERPSRingPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingPriorityValue.setStatus("mandatory")
_NmsERPSRingWtrTime_Type = Integer32
_NmsERPSRingWtrTime_Object = MibTableColumn
nmsERPSRingWtrTime = _NmsERPSRingWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 15),
    _NmsERPSRingWtrTime_Type()
)
nmsERPSRingWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingWtrTime.setStatus("mandatory")
_NmsERPSRingGuardTime_Type = Integer32
_NmsERPSRingGuardTime_Object = MibTableColumn
nmsERPSRingGuardTime = _NmsERPSRingGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 16),
    _NmsERPSRingGuardTime_Type()
)
nmsERPSRingGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingGuardTime.setStatus("mandatory")
_NmsERPSRingSendTime_Type = Integer32
_NmsERPSRingSendTime_Object = MibTableColumn
nmsERPSRingSendTime = _NmsERPSRingSendTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 17),
    _NmsERPSRingSendTime_Type()
)
nmsERPSRingSendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingSendTime.setStatus("mandatory")
_NmsERPSRingDiscoveryTime_Type = Integer32
_NmsERPSRingDiscoveryTime_Object = MibTableColumn
nmsERPSRingDiscoveryTime = _NmsERPSRingDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 18),
    _NmsERPSRingDiscoveryTime_Type()
)
nmsERPSRingDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingDiscoveryTime.setStatus("mandatory")
_NmsERPSRingDpduInterval_Type = Integer32
_NmsERPSRingDpduInterval_Object = MibTableColumn
nmsERPSRingDpduInterval = _NmsERPSRingDpduInterval_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 19),
    _NmsERPSRingDpduInterval_Type()
)
nmsERPSRingDpduInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingDpduInterval.setStatus("mandatory")
_NmsERPSRingDiscoveryCount_Type = Integer32
_NmsERPSRingDiscoveryCount_Object = MibTableColumn
nmsERPSRingDiscoveryCount = _NmsERPSRingDiscoveryCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 20),
    _NmsERPSRingDiscoveryCount_Type()
)
nmsERPSRingDiscoveryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingDiscoveryCount.setStatus("mandatory")
_NmsERPSRingDiscoveryLastDuration_Type = Integer32
_NmsERPSRingDiscoveryLastDuration_Object = MibTableColumn
nmsERPSRingDiscoveryLastDuration = _NmsERPSRingDiscoveryLastDuration_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 21),
    _NmsERPSRingDiscoveryLastDuration_Type()
)
nmsERPSRingDiscoveryLastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingDiscoveryLastDuration.setStatus("mandatory")
_NmsERPSRingDiscoveryLastElapsed_Type = Integer32
_NmsERPSRingDiscoveryLastElapsed_Object = MibTableColumn
nmsERPSRingDiscoveryLastElapsed = _NmsERPSRingDiscoveryLastElapsed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 22),
    _NmsERPSRingDiscoveryLastElapsed_Type()
)
nmsERPSRingDiscoveryLastElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingDiscoveryLastElapsed.setStatus("mandatory")


class _NmsERPSRingAdminStatus_Type(Integer32):
    """Custom type nmsERPSRingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NmsERPSRingAdminStatus_Type.__name__ = "Integer32"
_NmsERPSRingAdminStatus_Object = MibTableColumn
nmsERPSRingAdminStatus = _NmsERPSRingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 23),
    _NmsERPSRingAdminStatus_Type()
)
nmsERPSRingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsERPSRingAdminStatus.setStatus("mandatory")
_NmsERPSRingPort1_Type = Integer32
_NmsERPSRingPort1_Object = MibTableColumn
nmsERPSRingPort1 = _NmsERPSRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 24),
    _NmsERPSRingPort1_Type()
)
nmsERPSRingPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsERPSRingPort1.setStatus("mandatory")


class _NmsERPSRingPort1AdminType_Type(Integer32):
    """Custom type nmsERPSRingPort1AdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring-port", 0),
          ("rpl", 1))
    )


_NmsERPSRingPort1AdminType_Type.__name__ = "Integer32"
_NmsERPSRingPort1AdminType_Object = MibTableColumn
nmsERPSRingPort1AdminType = _NmsERPSRingPort1AdminType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 25),
    _NmsERPSRingPort1AdminType_Type()
)
nmsERPSRingPort1AdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingPort1AdminType.setStatus("mandatory")


class _NmsERPSRingPort1OperType_Type(Integer32):
    """Custom type nmsERPSRingPort1OperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring-port", 0),
          ("rpl", 1))
    )


_NmsERPSRingPort1OperType_Type.__name__ = "Integer32"
_NmsERPSRingPort1OperType_Object = MibTableColumn
nmsERPSRingPort1OperType = _NmsERPSRingPort1OperType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 26),
    _NmsERPSRingPort1OperType_Type()
)
nmsERPSRingPort1OperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort1OperType.setStatus("mandatory")


class _NmsERPSRingPort1State_Type(Integer32):
    """Custom type nmsERPSRingPort1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 0),
          ("forwarding", 1))
    )


_NmsERPSRingPort1State_Type.__name__ = "Integer32"
_NmsERPSRingPort1State_Object = MibTableColumn
nmsERPSRingPort1State = _NmsERPSRingPort1State_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 27),
    _NmsERPSRingPort1State_Type()
)
nmsERPSRingPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort1State.setStatus("mandatory")


class _NmsERPSRingPort1Status_Type(Integer32):
    """Custom type nmsERPSRingPort1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_NmsERPSRingPort1Status_Type.__name__ = "Integer32"
_NmsERPSRingPort1Status_Object = MibTableColumn
nmsERPSRingPort1Status = _NmsERPSRingPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 28),
    _NmsERPSRingPort1Status_Type()
)
nmsERPSRingPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort1Status.setStatus("mandatory")
_NmsERPSRingPort2_Type = Integer32
_NmsERPSRingPort2_Object = MibTableColumn
nmsERPSRingPort2 = _NmsERPSRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 29),
    _NmsERPSRingPort2_Type()
)
nmsERPSRingPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsERPSRingPort2.setStatus("mandatory")


class _NmsERPSRingPort2AdminType_Type(Integer32):
    """Custom type nmsERPSRingPort2AdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring-port", 0),
          ("rpl", 1))
    )


_NmsERPSRingPort2AdminType_Type.__name__ = "Integer32"
_NmsERPSRingPort2AdminType_Object = MibTableColumn
nmsERPSRingPort2AdminType = _NmsERPSRingPort2AdminType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 30),
    _NmsERPSRingPort2AdminType_Type()
)
nmsERPSRingPort2AdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsERPSRingPort2AdminType.setStatus("mandatory")


class _NmsERPSRingPort2OperType_Type(Integer32):
    """Custom type nmsERPSRingPort2OperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring-port", 0),
          ("rpl", 1))
    )


_NmsERPSRingPort2OperType_Type.__name__ = "Integer32"
_NmsERPSRingPort2OperType_Object = MibTableColumn
nmsERPSRingPort2OperType = _NmsERPSRingPort2OperType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 31),
    _NmsERPSRingPort2OperType_Type()
)
nmsERPSRingPort2OperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort2OperType.setStatus("mandatory")


class _NmsERPSRingPort2State_Type(Integer32):
    """Custom type nmsERPSRingPort2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 0),
          ("forwarding", 1))
    )


_NmsERPSRingPort2State_Type.__name__ = "Integer32"
_NmsERPSRingPort2State_Object = MibTableColumn
nmsERPSRingPort2State = _NmsERPSRingPort2State_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 32),
    _NmsERPSRingPort2State_Type()
)
nmsERPSRingPort2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort2State.setStatus("mandatory")


class _NmsERPSRingPort2Status_Type(Integer32):
    """Custom type nmsERPSRingPort2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_NmsERPSRingPort2Status_Type.__name__ = "Integer32"
_NmsERPSRingPort2Status_Object = MibTableColumn
nmsERPSRingPort2Status = _NmsERPSRingPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 6, 1, 33),
    _NmsERPSRingPort2Status_Type()
)
nmsERPSRingPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort2Status.setStatus("mandatory")
_NmsERPSRingPortTable_Object = MibTable
nmsERPSRingPortTable = _NmsERPSRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7)
)
if mibBuilder.loadTexts:
    nmsERPSRingPortTable.setStatus("mandatory")
_NmsERPSRingPortTableEntry_Object = MibTableRow
nmsERPSRingPortTableEntry = _NmsERPSRingPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1)
)
nmsERPSRingPortTableEntry.setIndexNames(
    (0, "NMS-ERPS-MIB", "nmsERPSRingPortRingID"),
    (0, "NMS-ERPS-MIB", "nmsERPSRingPort"),
)
if mibBuilder.loadTexts:
    nmsERPSRingPortTableEntry.setStatus("mandatory")
_NmsERPSRingPortRingID_Type = Integer32
_NmsERPSRingPortRingID_Object = MibTableColumn
nmsERPSRingPortRingID = _NmsERPSRingPortRingID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 1),
    _NmsERPSRingPortRingID_Type()
)
nmsERPSRingPortRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortRingID.setStatus("mandatory")
_NmsERPSRingPort_Type = Integer32
_NmsERPSRingPort_Object = MibTableColumn
nmsERPSRingPort = _NmsERPSRingPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 2),
    _NmsERPSRingPort_Type()
)
nmsERPSRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPort.setStatus("mandatory")


class _NmsERPSRingPortAdminType_Type(Integer32):
    """Custom type nmsERPSRingPortAdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring-port", 0),
          ("rpl", 1))
    )


_NmsERPSRingPortAdminType_Type.__name__ = "Integer32"
_NmsERPSRingPortAdminType_Object = MibTableColumn
nmsERPSRingPortAdminType = _NmsERPSRingPortAdminType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 3),
    _NmsERPSRingPortAdminType_Type()
)
nmsERPSRingPortAdminType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortAdminType.setStatus("mandatory")


class _NmsERPSRingPortOperType_Type(Integer32):
    """Custom type nmsERPSRingPortOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring-port", 0),
          ("rpl", 1))
    )


_NmsERPSRingPortOperType_Type.__name__ = "Integer32"
_NmsERPSRingPortOperType_Object = MibTableColumn
nmsERPSRingPortOperType = _NmsERPSRingPortOperType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 4),
    _NmsERPSRingPortOperType_Type()
)
nmsERPSRingPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortOperType.setStatus("mandatory")


class _NmsERPSRingPortState_Type(Integer32):
    """Custom type nmsERPSRingPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 0),
          ("forwarding", 1))
    )


_NmsERPSRingPortState_Type.__name__ = "Integer32"
_NmsERPSRingPortState_Object = MibTableColumn
nmsERPSRingPortState = _NmsERPSRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 5),
    _NmsERPSRingPortState_Type()
)
nmsERPSRingPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortState.setStatus("mandatory")


class _NmsERPSRingPortStatus_Type(Integer32):
    """Custom type nmsERPSRingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_NmsERPSRingPortStatus_Type.__name__ = "Integer32"
_NmsERPSRingPortStatus_Object = MibTableColumn
nmsERPSRingPortStatus = _NmsERPSRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 6),
    _NmsERPSRingPortStatus_Type()
)
nmsERPSRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortStatus.setStatus("mandatory")
_NmsERPSRingPortForwards_Type = Integer32
_NmsERPSRingPortForwards_Object = MibTableColumn
nmsERPSRingPortForwards = _NmsERPSRingPortForwards_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 7),
    _NmsERPSRingPortForwards_Type()
)
nmsERPSRingPortForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortForwards.setStatus("mandatory")
_NmsERPSRingPortForwardLastElapsed_Type = Integer32
_NmsERPSRingPortForwardLastElapsed_Object = MibTableColumn
nmsERPSRingPortForwardLastElapsed = _NmsERPSRingPortForwardLastElapsed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 8),
    _NmsERPSRingPortForwardLastElapsed_Type()
)
nmsERPSRingPortForwardLastElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortForwardLastElapsed.setStatus("mandatory")
_NmsERPSRingPortRx_Type = Integer32
_NmsERPSRingPortRx_Object = MibTableColumn
nmsERPSRingPortRx = _NmsERPSRingPortRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 9),
    _NmsERPSRingPortRx_Type()
)
nmsERPSRingPortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortRx.setStatus("mandatory")
_NmsERPSRingPortTx_Type = Integer32
_NmsERPSRingPortTx_Object = MibTableColumn
nmsERPSRingPortTx = _NmsERPSRingPortTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 7, 1, 10),
    _NmsERPSRingPortTx_Type()
)
nmsERPSRingPortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsERPSRingPortTx.setStatus("mandatory")
_NmsERPSRingNotifications_ObjectIdentity = ObjectIdentity
nmsERPSRingNotifications = _NmsERPSRingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 8)
)

# Managed Objects groups


# Notification objects

nmsERPSRingRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 8, 1)
)
nmsERPSRingRoleChange.setObjects(
      *(("NMS-ERPS-MIB", "nmsERPSRingID"),
        ("NMS-ERPS-MIB", "nmsERPSRingNodeID"),
        ("NMS-ERPS-MIB", "nmsERPSRingRole"))
)
if mibBuilder.loadTexts:
    nmsERPSRingRoleChange.setStatus(
        "current"
    )

nmsERPSRingStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 231, 8, 2)
)
nmsERPSRingStateChange.setObjects(
      *(("NMS-ERPS-MIB", "nmsERPSRingID"),
        ("NMS-ERPS-MIB", "nmsERPSRingNodeID"),
        ("NMS-ERPS-MIB", "nmsERPSRingRole"),
        ("NMS-ERPS-MIB", "nmsERPSRingState"))
)
if mibBuilder.loadTexts:
    nmsERPSRingStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-ERPS-MIB",
    **{"nmsERPS": nmsERPS,
       "nmsERPSRings": nmsERPSRings,
       "nmsERPSInconsistenceCheck": nmsERPSInconsistenceCheck,
       "nmsERPSPduRx": nmsERPSPduRx,
       "nmsERPSPduRxDropped": nmsERPSPduRxDropped,
       "nmsERPSPduTx": nmsERPSPduTx,
       "nmsERPSRingTable": nmsERPSRingTable,
       "nmsERPSRingTableEntry": nmsERPSRingTableEntry,
       "nmsERPSRingID": nmsERPSRingID,
       "nmsERPSRingNodeID": nmsERPSRingNodeID,
       "nmsERPSRingPorts": nmsERPSRingPorts,
       "nmsERPSRingRole": nmsERPSRingRole,
       "nmsERPSRingState": nmsERPSRingState,
       "nmsERPSRingWTR": nmsERPSRingWTR,
       "nmsERPSRingWtrWhile": nmsERPSRingWtrWhile,
       "nmsERPSRingSignalFail": nmsERPSRingSignalFail,
       "nmsERPSRingSending": nmsERPSRingSending,
       "nmsERPSRingRplOwnerID": nmsERPSRingRplOwnerID,
       "nmsERPSRingRplOwnerMAC": nmsERPSRingRplOwnerMAC,
       "nmsERPSRingDiscovering": nmsERPSRingDiscovering,
       "nmsERPSRingDiscoverWhile": nmsERPSRingDiscoverWhile,
       "nmsERPSRingPriorityValue": nmsERPSRingPriorityValue,
       "nmsERPSRingWtrTime": nmsERPSRingWtrTime,
       "nmsERPSRingGuardTime": nmsERPSRingGuardTime,
       "nmsERPSRingSendTime": nmsERPSRingSendTime,
       "nmsERPSRingDiscoveryTime": nmsERPSRingDiscoveryTime,
       "nmsERPSRingDpduInterval": nmsERPSRingDpduInterval,
       "nmsERPSRingDiscoveryCount": nmsERPSRingDiscoveryCount,
       "nmsERPSRingDiscoveryLastDuration": nmsERPSRingDiscoveryLastDuration,
       "nmsERPSRingDiscoveryLastElapsed": nmsERPSRingDiscoveryLastElapsed,
       "nmsERPSRingAdminStatus": nmsERPSRingAdminStatus,
       "nmsERPSRingPort1": nmsERPSRingPort1,
       "nmsERPSRingPort1AdminType": nmsERPSRingPort1AdminType,
       "nmsERPSRingPort1OperType": nmsERPSRingPort1OperType,
       "nmsERPSRingPort1State": nmsERPSRingPort1State,
       "nmsERPSRingPort1Status": nmsERPSRingPort1Status,
       "nmsERPSRingPort2": nmsERPSRingPort2,
       "nmsERPSRingPort2AdminType": nmsERPSRingPort2AdminType,
       "nmsERPSRingPort2OperType": nmsERPSRingPort2OperType,
       "nmsERPSRingPort2State": nmsERPSRingPort2State,
       "nmsERPSRingPort2Status": nmsERPSRingPort2Status,
       "nmsERPSRingPortTable": nmsERPSRingPortTable,
       "nmsERPSRingPortTableEntry": nmsERPSRingPortTableEntry,
       "nmsERPSRingPortRingID": nmsERPSRingPortRingID,
       "nmsERPSRingPort": nmsERPSRingPort,
       "nmsERPSRingPortAdminType": nmsERPSRingPortAdminType,
       "nmsERPSRingPortOperType": nmsERPSRingPortOperType,
       "nmsERPSRingPortState": nmsERPSRingPortState,
       "nmsERPSRingPortStatus": nmsERPSRingPortStatus,
       "nmsERPSRingPortForwards": nmsERPSRingPortForwards,
       "nmsERPSRingPortForwardLastElapsed": nmsERPSRingPortForwardLastElapsed,
       "nmsERPSRingPortRx": nmsERPSRingPortRx,
       "nmsERPSRingPortTx": nmsERPSRingPortTx,
       "nmsERPSRingNotifications": nmsERPSRingNotifications,
       "nmsERPSRingRoleChange": nmsERPSRingRoleChange,
       "nmsERPSRingStateChange": nmsERPSRingStateChange}
)
