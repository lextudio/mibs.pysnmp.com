# SNMP MIB module (NMS-EAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:39 2024
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

_NmsEAPS_ObjectIdentity = ObjectIdentity
nmsEAPS = _NmsEAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230)
)
_NmsEAPSRings_Type = Integer32
_NmsEAPSRings_Object = MibScalar
nmsEAPSRings = _NmsEAPSRings_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 1),
    _NmsEAPSRings_Type()
)
nmsEAPSRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRings.setStatus("mandatory")
_NmsEAPSPduRx_Type = Integer32
_NmsEAPSPduRx_Object = MibScalar
nmsEAPSPduRx = _NmsEAPSPduRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 2),
    _NmsEAPSPduRx_Type()
)
nmsEAPSPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSPduRx.setStatus("mandatory")
_NmsEAPSPduTx_Type = Integer32
_NmsEAPSPduTx_Object = MibScalar
nmsEAPSPduTx = _NmsEAPSPduTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 3),
    _NmsEAPSPduTx_Type()
)
nmsEAPSPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSPduTx.setStatus("mandatory")
_NmsEAPSRingTable_Object = MibTable
nmsEAPSRingTable = _NmsEAPSRingTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4)
)
if mibBuilder.loadTexts:
    nmsEAPSRingTable.setStatus("mandatory")
_NmsEAPSRingTableEntry_Object = MibTableRow
nmsEAPSRingTableEntry = _NmsEAPSRingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1)
)
nmsEAPSRingTableEntry.setIndexNames(
    (0, "NMS-EAPS-MIB", "nmsEAPSRingID"),
)
if mibBuilder.loadTexts:
    nmsEAPSRingTableEntry.setStatus("mandatory")
_NmsEAPSRingID_Type = Integer32
_NmsEAPSRingID_Object = MibTableColumn
nmsEAPSRingID = _NmsEAPSRingID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 1),
    _NmsEAPSRingID_Type()
)
nmsEAPSRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingID.setStatus("mandatory")


class _NmsEAPSRingNodeType_Type(Integer32):
    """Custom type nmsEAPSRingNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterNode", 1),
          ("transitNode", 2),
          ("unknown", 0))
    )


_NmsEAPSRingNodeType_Type.__name__ = "Integer32"
_NmsEAPSRingNodeType_Object = MibTableColumn
nmsEAPSRingNodeType = _NmsEAPSRingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 2),
    _NmsEAPSRingNodeType_Type()
)
nmsEAPSRingNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingNodeType.setStatus("mandatory")
_NmsEAPSRingControlVlan_Type = Integer32
_NmsEAPSRingControlVlan_Object = MibTableColumn
nmsEAPSRingControlVlan = _NmsEAPSRingControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 3),
    _NmsEAPSRingControlVlan_Type()
)
nmsEAPSRingControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingControlVlan.setStatus("mandatory")
_NmsEAPSRingPorts_Type = Integer32
_NmsEAPSRingPorts_Object = MibTableColumn
nmsEAPSRingPorts = _NmsEAPSRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 4),
    _NmsEAPSRingPorts_Type()
)
nmsEAPSRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPorts.setStatus("mandatory")


class _NmsEAPSRingState_Type(Integer32):
    """Custom type nmsEAPSRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("ringFault", 2),
          ("unknown", 0))
    )


_NmsEAPSRingState_Type.__name__ = "Integer32"
_NmsEAPSRingState_Object = MibTableColumn
nmsEAPSRingState = _NmsEAPSRingState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 5),
    _NmsEAPSRingState_Type()
)
nmsEAPSRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingState.setStatus("mandatory")


class _NmsEAPSRingHealthCheck_Type(Integer32):
    """Custom type nmsEAPSRingHealthCheck based on Integer32"""
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


_NmsEAPSRingHealthCheck_Type.__name__ = "Integer32"
_NmsEAPSRingHealthCheck_Object = MibTableColumn
nmsEAPSRingHealthCheck = _NmsEAPSRingHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 6),
    _NmsEAPSRingHealthCheck_Type()
)
nmsEAPSRingHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingHealthCheck.setStatus("mandatory")
_NmsEAPSRingHelloTime_Type = Integer32
_NmsEAPSRingHelloTime_Object = MibTableColumn
nmsEAPSRingHelloTime = _NmsEAPSRingHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 7),
    _NmsEAPSRingHelloTime_Type()
)
nmsEAPSRingHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingHelloTime.setStatus("mandatory")
_NmsEAPSRingFailTime_Type = Integer32
_NmsEAPSRingFailTime_Object = MibTableColumn
nmsEAPSRingFailTime = _NmsEAPSRingFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 8),
    _NmsEAPSRingFailTime_Type()
)
nmsEAPSRingFailTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingFailTime.setStatus("mandatory")
_NmsEAPSRingPreforwardTime_Type = Integer32
_NmsEAPSRingPreforwardTime_Object = MibTableColumn
nmsEAPSRingPreforwardTime = _NmsEAPSRingPreforwardTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 9),
    _NmsEAPSRingPreforwardTime_Type()
)
nmsEAPSRingPreforwardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingPreforwardTime.setStatus("mandatory")


class _NmsEAPSRingAdminStatus_Type(Integer32):
    """Custom type nmsEAPSRingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("running", 2))
    )


_NmsEAPSRingAdminStatus_Type.__name__ = "Integer32"
_NmsEAPSRingAdminStatus_Object = MibTableColumn
nmsEAPSRingAdminStatus = _NmsEAPSRingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 10),
    _NmsEAPSRingAdminStatus_Type()
)
nmsEAPSRingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsEAPSRingAdminStatus.setStatus("mandatory")
_NmsEAPSRingPrimaryPort_Type = Integer32
_NmsEAPSRingPrimaryPort_Object = MibTableColumn
nmsEAPSRingPrimaryPort = _NmsEAPSRingPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 11),
    _NmsEAPSRingPrimaryPort_Type()
)
nmsEAPSRingPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingPrimaryPort.setStatus("mandatory")


class _NmsEAPSRingPrimaryPortState_Type(Integer32):
    """Custom type nmsEAPSRingPrimaryPortState based on Integer32"""
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
        *(("blocking", 3),
          ("forwarding", 1),
          ("preforwarding", 2),
          ("unknown", 0))
    )


_NmsEAPSRingPrimaryPortState_Type.__name__ = "Integer32"
_NmsEAPSRingPrimaryPortState_Object = MibTableColumn
nmsEAPSRingPrimaryPortState = _NmsEAPSRingPrimaryPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 12),
    _NmsEAPSRingPrimaryPortState_Type()
)
nmsEAPSRingPrimaryPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPrimaryPortState.setStatus("mandatory")


class _NmsEAPSRingPrimaryPortStatus_Type(Integer32):
    """Custom type nmsEAPSRingPrimaryPortStatus based on Integer32"""
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


_NmsEAPSRingPrimaryPortStatus_Type.__name__ = "Integer32"
_NmsEAPSRingPrimaryPortStatus_Object = MibTableColumn
nmsEAPSRingPrimaryPortStatus = _NmsEAPSRingPrimaryPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 13),
    _NmsEAPSRingPrimaryPortStatus_Type()
)
nmsEAPSRingPrimaryPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPrimaryPortStatus.setStatus("mandatory")
_NmsEAPSRingSecondaryPort_Type = Integer32
_NmsEAPSRingSecondaryPort_Object = MibTableColumn
nmsEAPSRingSecondaryPort = _NmsEAPSRingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 14),
    _NmsEAPSRingSecondaryPort_Type()
)
nmsEAPSRingSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEAPSRingSecondaryPort.setStatus("mandatory")


class _NmsEAPSRingSecondaryPortState_Type(Integer32):
    """Custom type nmsEAPSRingSecondaryPortState based on Integer32"""
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
        *(("blocking", 3),
          ("forwarding", 1),
          ("preforwarding", 2),
          ("unknown", 0))
    )


_NmsEAPSRingSecondaryPortState_Type.__name__ = "Integer32"
_NmsEAPSRingSecondaryPortState_Object = MibTableColumn
nmsEAPSRingSecondaryPortState = _NmsEAPSRingSecondaryPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 15),
    _NmsEAPSRingSecondaryPortState_Type()
)
nmsEAPSRingSecondaryPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingSecondaryPortState.setStatus("mandatory")


class _NmsEAPSRingSecondaryPortStatus_Type(Integer32):
    """Custom type nmsEAPSRingSecondaryPortStatus based on Integer32"""
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


_NmsEAPSRingSecondaryPortStatus_Type.__name__ = "Integer32"
_NmsEAPSRingSecondaryPortStatus_Object = MibTableColumn
nmsEAPSRingSecondaryPortStatus = _NmsEAPSRingSecondaryPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 16),
    _NmsEAPSRingSecondaryPortStatus_Type()
)
nmsEAPSRingSecondaryPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingSecondaryPortStatus.setStatus("mandatory")
_NmsEAPSRingPortTable_Object = MibTable
nmsEAPSRingPortTable = _NmsEAPSRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5)
)
if mibBuilder.loadTexts:
    nmsEAPSRingPortTable.setStatus("mandatory")
_NmsEAPSRingPortTableEntry_Object = MibTableRow
nmsEAPSRingPortTableEntry = _NmsEAPSRingPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1)
)
nmsEAPSRingPortTableEntry.setIndexNames(
    (0, "NMS-EAPS-MIB", "nmsEAPSRingPortRingID"),
    (0, "NMS-EAPS-MIB", "nmsEAPSRingPort"),
)
if mibBuilder.loadTexts:
    nmsEAPSRingPortTableEntry.setStatus("mandatory")
_NmsEAPSRingPortRingID_Type = Integer32
_NmsEAPSRingPortRingID_Object = MibTableColumn
nmsEAPSRingPortRingID = _NmsEAPSRingPortRingID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 1),
    _NmsEAPSRingPortRingID_Type()
)
nmsEAPSRingPortRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortRingID.setStatus("mandatory")
_NmsEAPSRingPort_Type = Integer32
_NmsEAPSRingPort_Object = MibTableColumn
nmsEAPSRingPort = _NmsEAPSRingPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 2),
    _NmsEAPSRingPort_Type()
)
nmsEAPSRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPort.setStatus("mandatory")


class _NmsEAPSRingPortType_Type(Integer32):
    """Custom type nmsEAPSRingPortType based on Integer32"""
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
        *(("primaryPort", 1),
          ("secondaryPort", 2),
          ("transitPort", 3),
          ("unknown", 0))
    )


_NmsEAPSRingPortType_Type.__name__ = "Integer32"
_NmsEAPSRingPortType_Object = MibTableColumn
nmsEAPSRingPortType = _NmsEAPSRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 3),
    _NmsEAPSRingPortType_Type()
)
nmsEAPSRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortType.setStatus("mandatory")


class _NmsEAPSRingPortState_Type(Integer32):
    """Custom type nmsEAPSRingPortState based on Integer32"""
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
        *(("blocking", 3),
          ("forwarding", 1),
          ("preforwarding", 2),
          ("unknown", 0))
    )


_NmsEAPSRingPortState_Type.__name__ = "Integer32"
_NmsEAPSRingPortState_Object = MibTableColumn
nmsEAPSRingPortState = _NmsEAPSRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 4),
    _NmsEAPSRingPortState_Type()
)
nmsEAPSRingPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortState.setStatus("mandatory")
_NmsEAPSRingPortForwards_Type = Integer32
_NmsEAPSRingPortForwards_Object = MibTableColumn
nmsEAPSRingPortForwards = _NmsEAPSRingPortForwards_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 5),
    _NmsEAPSRingPortForwards_Type()
)
nmsEAPSRingPortForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortForwards.setStatus("mandatory")
_NmsEAPSRingPortRx_Type = Integer32
_NmsEAPSRingPortRx_Object = MibTableColumn
nmsEAPSRingPortRx = _NmsEAPSRingPortRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 6),
    _NmsEAPSRingPortRx_Type()
)
nmsEAPSRingPortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortRx.setStatus("mandatory")
_NmsEAPSRingPortTx_Type = Integer32
_NmsEAPSRingPortTx_Object = MibTableColumn
nmsEAPSRingPortTx = _NmsEAPSRingPortTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 7),
    _NmsEAPSRingPortTx_Type()
)
nmsEAPSRingPortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortTx.setStatus("mandatory")


class _NmsEAPSRingPortStatus_Type(Integer32):
    """Custom type nmsEAPSRingPortStatus based on Integer32"""
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


_NmsEAPSRingPortStatus_Type.__name__ = "Integer32"
_NmsEAPSRingPortStatus_Object = MibTableColumn
nmsEAPSRingPortStatus = _NmsEAPSRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 8),
    _NmsEAPSRingPortStatus_Type()
)
nmsEAPSRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsEAPSRingPortStatus.setStatus("mandatory")
_NmsEAPSRingNotifications_ObjectIdentity = ObjectIdentity
nmsEAPSRingNotifications = _NmsEAPSRingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 6)
)

# Managed Objects groups


# Notification objects

nmsEAPSRingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 6, 1)
)
nmsEAPSRingNotification.setObjects(
      *(("NMS-EAPS-MIB", "nmsEAPSRingID"),
        ("NMS-EAPS-MIB", "nmsEAPSRingNodeType"),
        ("NMS-EAPS-MIB", "nmsEAPSRingState"))
)
if mibBuilder.loadTexts:
    nmsEAPSRingNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EAPS-MIB",
    **{"nmsEAPS": nmsEAPS,
       "nmsEAPSRings": nmsEAPSRings,
       "nmsEAPSPduRx": nmsEAPSPduRx,
       "nmsEAPSPduTx": nmsEAPSPduTx,
       "nmsEAPSRingTable": nmsEAPSRingTable,
       "nmsEAPSRingTableEntry": nmsEAPSRingTableEntry,
       "nmsEAPSRingID": nmsEAPSRingID,
       "nmsEAPSRingNodeType": nmsEAPSRingNodeType,
       "nmsEAPSRingControlVlan": nmsEAPSRingControlVlan,
       "nmsEAPSRingPorts": nmsEAPSRingPorts,
       "nmsEAPSRingState": nmsEAPSRingState,
       "nmsEAPSRingHealthCheck": nmsEAPSRingHealthCheck,
       "nmsEAPSRingHelloTime": nmsEAPSRingHelloTime,
       "nmsEAPSRingFailTime": nmsEAPSRingFailTime,
       "nmsEAPSRingPreforwardTime": nmsEAPSRingPreforwardTime,
       "nmsEAPSRingAdminStatus": nmsEAPSRingAdminStatus,
       "nmsEAPSRingPrimaryPort": nmsEAPSRingPrimaryPort,
       "nmsEAPSRingPrimaryPortState": nmsEAPSRingPrimaryPortState,
       "nmsEAPSRingPrimaryPortStatus": nmsEAPSRingPrimaryPortStatus,
       "nmsEAPSRingSecondaryPort": nmsEAPSRingSecondaryPort,
       "nmsEAPSRingSecondaryPortState": nmsEAPSRingSecondaryPortState,
       "nmsEAPSRingSecondaryPortStatus": nmsEAPSRingSecondaryPortStatus,
       "nmsEAPSRingPortTable": nmsEAPSRingPortTable,
       "nmsEAPSRingPortTableEntry": nmsEAPSRingPortTableEntry,
       "nmsEAPSRingPortRingID": nmsEAPSRingPortRingID,
       "nmsEAPSRingPort": nmsEAPSRingPort,
       "nmsEAPSRingPortType": nmsEAPSRingPortType,
       "nmsEAPSRingPortState": nmsEAPSRingPortState,
       "nmsEAPSRingPortForwards": nmsEAPSRingPortForwards,
       "nmsEAPSRingPortRx": nmsEAPSRingPortRx,
       "nmsEAPSRingPortTx": nmsEAPSRingPortTx,
       "nmsEAPSRingPortStatus": nmsEAPSRingPortStatus,
       "nmsEAPSRingNotifications": nmsEAPSRingNotifications,
       "nmsEAPSRingNotification": nmsEAPSRingNotification}
)
