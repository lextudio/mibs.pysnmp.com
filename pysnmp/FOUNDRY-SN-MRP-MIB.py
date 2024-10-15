# SNMP MIB module (FOUNDRY-SN-MRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-MRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:59 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

snMetroRing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29)
)
snMetroRing.setRevisions(
        ("2010-06-02 00:00",
         "2007-05-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnMetroRingGlobalObjects_ObjectIdentity = ObjectIdentity
snMetroRingGlobalObjects = _SnMetroRingGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 1)
)
_SnMetroRingTableObjects_ObjectIdentity = ObjectIdentity
snMetroRingTableObjects = _SnMetroRingTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2)
)
_SnMetroRingTable_Object = MibTable
snMetroRingTable = _SnMetroRingTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1)
)
if mibBuilder.loadTexts:
    snMetroRingTable.setStatus("current")
_SnMetroRingEntry_Object = MibTableRow
snMetroRingEntry = _SnMetroRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1)
)
snMetroRingEntry.setIndexNames(
    (0, "FOUNDRY-SN-MRP-MIB", "snMetroRingVLanId"),
    (0, "FOUNDRY-SN-MRP-MIB", "snMetroRingId"),
)
if mibBuilder.loadTexts:
    snMetroRingEntry.setStatus("current")
_SnMetroRingVLanId_Type = Integer32
_SnMetroRingVLanId_Object = MibTableColumn
snMetroRingVLanId = _SnMetroRingVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 1),
    _SnMetroRingVLanId_Type()
)
snMetroRingVLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMetroRingVLanId.setStatus("current")
_SnMetroRingId_Type = Integer32
_SnMetroRingId_Object = MibTableColumn
snMetroRingId = _SnMetroRingId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 2),
    _SnMetroRingId_Type()
)
snMetroRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMetroRingId.setStatus("current")


class _SnMetroRingConfigState_Type(Integer32):
    """Custom type snMetroRingConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SnMetroRingConfigState_Type.__name__ = "Integer32"
_SnMetroRingConfigState_Object = MibTableColumn
snMetroRingConfigState = _SnMetroRingConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 3),
    _SnMetroRingConfigState_Type()
)
snMetroRingConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingConfigState.setStatus("current")


class _SnMetroRingRole_Type(Integer32):
    """Custom type snMetroRingRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("member", 3),
          ("other", 1))
    )


_SnMetroRingRole_Type.__name__ = "Integer32"
_SnMetroRingRole_Object = MibTableColumn
snMetroRingRole = _SnMetroRingRole_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 4),
    _SnMetroRingRole_Type()
)
snMetroRingRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingRole.setStatus("current")
_SnMetroRingHelloTime_Type = Integer32
_SnMetroRingHelloTime_Object = MibTableColumn
snMetroRingHelloTime = _SnMetroRingHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 5),
    _SnMetroRingHelloTime_Type()
)
snMetroRingHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingHelloTime.setStatus("current")
_SnMetroRingPreforwardingTime_Type = Integer32
_SnMetroRingPreforwardingTime_Object = MibTableColumn
snMetroRingPreforwardingTime = _SnMetroRingPreforwardingTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 6),
    _SnMetroRingPreforwardingTime_Type()
)
snMetroRingPreforwardingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingPreforwardingTime.setStatus("current")
_SnMetroRingPort1_Type = InterfaceIndex
_SnMetroRingPort1_Object = MibTableColumn
snMetroRingPort1 = _SnMetroRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 7),
    _SnMetroRingPort1_Type()
)
snMetroRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingPort1.setStatus("current")
_SnMetroRingPort2_Type = InterfaceIndex
_SnMetroRingPort2_Object = MibTableColumn
snMetroRingPort2 = _SnMetroRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 8),
    _SnMetroRingPort2_Type()
)
snMetroRingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingPort2.setStatus("current")
_SnMetroRingName_Type = DisplayString
_SnMetroRingName_Object = MibTableColumn
snMetroRingName = _SnMetroRingName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 9),
    _SnMetroRingName_Type()
)
snMetroRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingName.setStatus("current")


class _SnMetroRingRowStatus_Type(Integer32):
    """Custom type snMetroRingRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnMetroRingRowStatus_Type.__name__ = "Integer32"
_SnMetroRingRowStatus_Object = MibTableColumn
snMetroRingRowStatus = _SnMetroRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 10),
    _SnMetroRingRowStatus_Type()
)
snMetroRingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMetroRingRowStatus.setStatus("current")


class _SnMetroRingOperState_Type(Integer32):
    """Custom type snMetroRingOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SnMetroRingOperState_Type.__name__ = "Integer32"
_SnMetroRingOperState_Object = MibTableColumn
snMetroRingOperState = _SnMetroRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 11),
    _SnMetroRingOperState_Type()
)
snMetroRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingOperState.setStatus("current")
_SnMetroRingTopoGroupId_Type = Integer32
_SnMetroRingTopoGroupId_Object = MibTableColumn
snMetroRingTopoGroupId = _SnMetroRingTopoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 12),
    _SnMetroRingTopoGroupId_Type()
)
snMetroRingTopoGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingTopoGroupId.setStatus("current")
_SnMetroRingRHPTransmitted_Type = Counter32
_SnMetroRingRHPTransmitted_Object = MibTableColumn
snMetroRingRHPTransmitted = _SnMetroRingRHPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 13),
    _SnMetroRingRHPTransmitted_Type()
)
snMetroRingRHPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingRHPTransmitted.setStatus("current")
_SnMetroRingRHPReceived_Type = Counter32
_SnMetroRingRHPReceived_Object = MibTableColumn
snMetroRingRHPReceived = _SnMetroRingRHPReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 14),
    _SnMetroRingRHPReceived_Type()
)
snMetroRingRHPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingRHPReceived.setStatus("current")
_SnMetroRingStateChanged_Type = Counter32
_SnMetroRingStateChanged_Object = MibTableColumn
snMetroRingStateChanged = _SnMetroRingStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 15),
    _SnMetroRingStateChanged_Type()
)
snMetroRingStateChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingStateChanged.setStatus("current")
_SnMetroRingTCRBPDUReceived_Type = Counter32
_SnMetroRingTCRBPDUReceived_Object = MibTableColumn
snMetroRingTCRBPDUReceived = _SnMetroRingTCRBPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 16),
    _SnMetroRingTCRBPDUReceived_Type()
)
snMetroRingTCRBPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingTCRBPDUReceived.setStatus("current")
_SnMetroRingPriPort_Type = InterfaceIndex
_SnMetroRingPriPort_Object = MibTableColumn
snMetroRingPriPort = _SnMetroRingPriPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 17),
    _SnMetroRingPriPort_Type()
)
snMetroRingPriPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingPriPort.setStatus("current")
_SnMetroRingSecPort_Type = InterfaceIndex
_SnMetroRingSecPort_Object = MibTableColumn
snMetroRingSecPort = _SnMetroRingSecPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 18),
    _SnMetroRingSecPort_Type()
)
snMetroRingSecPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingSecPort.setStatus("current")


class _SnMetroRingPriPortState_Type(Integer32):
    """Custom type snMetroRingPriPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 4),
          ("disabled", 5),
          ("forwarding", 3),
          ("other", 1),
          ("preforwarding", 2))
    )


_SnMetroRingPriPortState_Type.__name__ = "Integer32"
_SnMetroRingPriPortState_Object = MibTableColumn
snMetroRingPriPortState = _SnMetroRingPriPortState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 19),
    _SnMetroRingPriPortState_Type()
)
snMetroRingPriPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingPriPortState.setStatus("current")


class _SnMetroRingSecPortState_Type(Integer32):
    """Custom type snMetroRingSecPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 4),
          ("disabled", 5),
          ("forwarding", 3),
          ("other", 1),
          ("preforwarding", 2))
    )


_SnMetroRingSecPortState_Type.__name__ = "Integer32"
_SnMetroRingSecPortState_Object = MibTableColumn
snMetroRingSecPortState = _SnMetroRingSecPortState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 20),
    _SnMetroRingSecPortState_Type()
)
snMetroRingSecPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingSecPortState.setStatus("current")


class _SnMetroRingPriPortType_Type(Integer32):
    """Custom type snMetroRingPriPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("regular", 2),
          ("tunnel", 3))
    )


_SnMetroRingPriPortType_Type.__name__ = "Integer32"
_SnMetroRingPriPortType_Object = MibTableColumn
snMetroRingPriPortType = _SnMetroRingPriPortType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 21),
    _SnMetroRingPriPortType_Type()
)
snMetroRingPriPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingPriPortType.setStatus("current")


class _SnMetroRingSecPortType_Type(Integer32):
    """Custom type snMetroRingSecPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("regular", 2),
          ("tunnel", 3))
    )


_SnMetroRingSecPortType_Type.__name__ = "Integer32"
_SnMetroRingSecPortType_Object = MibTableColumn
snMetroRingSecPortType = _SnMetroRingSecPortType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 22),
    _SnMetroRingSecPortType_Type()
)
snMetroRingSecPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingSecPortType.setStatus("current")
_SnMetroRingPriPortActivePort_Type = InterfaceIndex
_SnMetroRingPriPortActivePort_Object = MibTableColumn
snMetroRingPriPortActivePort = _SnMetroRingPriPortActivePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 23),
    _SnMetroRingPriPortActivePort_Type()
)
snMetroRingPriPortActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingPriPortActivePort.setStatus("current")
_SnMetroRingSecPortActivePort_Type = InterfaceIndex
_SnMetroRingSecPortActivePort_Object = MibTableColumn
snMetroRingSecPortActivePort = _SnMetroRingSecPortActivePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 24),
    _SnMetroRingSecPortActivePort_Type()
)
snMetroRingSecPortActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMetroRingSecPortActivePort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-MRP-MIB",
    **{"snMetroRing": snMetroRing,
       "snMetroRingGlobalObjects": snMetroRingGlobalObjects,
       "snMetroRingTableObjects": snMetroRingTableObjects,
       "snMetroRingTable": snMetroRingTable,
       "snMetroRingEntry": snMetroRingEntry,
       "snMetroRingVLanId": snMetroRingVLanId,
       "snMetroRingId": snMetroRingId,
       "snMetroRingConfigState": snMetroRingConfigState,
       "snMetroRingRole": snMetroRingRole,
       "snMetroRingHelloTime": snMetroRingHelloTime,
       "snMetroRingPreforwardingTime": snMetroRingPreforwardingTime,
       "snMetroRingPort1": snMetroRingPort1,
       "snMetroRingPort2": snMetroRingPort2,
       "snMetroRingName": snMetroRingName,
       "snMetroRingRowStatus": snMetroRingRowStatus,
       "snMetroRingOperState": snMetroRingOperState,
       "snMetroRingTopoGroupId": snMetroRingTopoGroupId,
       "snMetroRingRHPTransmitted": snMetroRingRHPTransmitted,
       "snMetroRingRHPReceived": snMetroRingRHPReceived,
       "snMetroRingStateChanged": snMetroRingStateChanged,
       "snMetroRingTCRBPDUReceived": snMetroRingTCRBPDUReceived,
       "snMetroRingPriPort": snMetroRingPriPort,
       "snMetroRingSecPort": snMetroRingSecPort,
       "snMetroRingPriPortState": snMetroRingPriPortState,
       "snMetroRingSecPortState": snMetroRingSecPortState,
       "snMetroRingPriPortType": snMetroRingPriPortType,
       "snMetroRingSecPortType": snMetroRingSecPortType,
       "snMetroRingPriPortActivePort": snMetroRingPriPortActivePort,
       "snMetroRingSecPortActivePort": snMetroRingSecPortActivePort}
)
