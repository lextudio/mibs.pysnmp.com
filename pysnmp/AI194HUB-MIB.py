# SNMP MIB module (AI194HUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AI194HUB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:05 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiHub = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiProxy_ObjectIdentity = ObjectIdentity
aiProxy = _AiProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 1)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_AiHubTwistedPairPortNumber_Type = Integer32
_AiHubTwistedPairPortNumber_Object = MibScalar
aiHubTwistedPairPortNumber = _AiHubTwistedPairPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 1),
    _AiHubTwistedPairPortNumber_Type()
)
aiHubTwistedPairPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubTwistedPairPortNumber.setStatus("mandatory")
_AiHubNonTwistedPairPortNumber_Type = Integer32
_AiHubNonTwistedPairPortNumber_Object = MibScalar
aiHubNonTwistedPairPortNumber = _AiHubNonTwistedPairPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 2),
    _AiHubNonTwistedPairPortNumber_Type()
)
aiHubNonTwistedPairPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubNonTwistedPairPortNumber.setStatus("mandatory")
_AiHubPortTable_Object = MibTable
aiHubPortTable = _AiHubPortTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3)
)
if mibBuilder.loadTexts:
    aiHubPortTable.setStatus("mandatory")
_AiHubPortEntry_Object = MibTableRow
aiHubPortEntry = _AiHubPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1)
)
aiHubPortEntry.setIndexNames(
    (0, "AI194HUB-MIB", "aiHubPortIndex"),
)
if mibBuilder.loadTexts:
    aiHubPortEntry.setStatus("mandatory")
_AiHubPortIndex_Type = Integer32
_AiHubPortIndex_Object = MibTableColumn
aiHubPortIndex = _AiHubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 1),
    _AiHubPortIndex_Type()
)
aiHubPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortIndex.setStatus("mandatory")


class _AiHubPortName_Type(DisplayString):
    """Custom type aiHubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AiHubPortName_Type.__name__ = "DisplayString"
_AiHubPortName_Object = MibTableColumn
aiHubPortName = _AiHubPortName_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 2),
    _AiHubPortName_Type()
)
aiHubPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHubPortName.setStatus("mandatory")


class _AiHubPortAdminState_Type(Integer32):
    """Custom type aiHubPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_AiHubPortAdminState_Type.__name__ = "Integer32"
_AiHubPortAdminState_Object = MibTableColumn
aiHubPortAdminState = _AiHubPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 3),
    _AiHubPortAdminState_Type()
)
aiHubPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHubPortAdminState.setStatus("mandatory")


class _AiHubPortAutoPartitionState_Type(Integer32):
    """Custom type aiHubPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 3),
          ("notAutoPartitioned", 2),
          ("other", 1))
    )


_AiHubPortAutoPartitionState_Type.__name__ = "Integer32"
_AiHubPortAutoPartitionState_Object = MibTableColumn
aiHubPortAutoPartitionState = _AiHubPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 4),
    _AiHubPortAutoPartitionState_Type()
)
aiHubPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortAutoPartitionState.setStatus("mandatory")
_AiHubPortErrors_Type = Counter32
_AiHubPortErrors_Object = MibTableColumn
aiHubPortErrors = _AiHubPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 5),
    _AiHubPortErrors_Type()
)
aiHubPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortErrors.setStatus("mandatory")
_AiHubPortCollisions_Type = Counter32
_AiHubPortCollisions_Object = MibTableColumn
aiHubPortCollisions = _AiHubPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 6),
    _AiHubPortCollisions_Type()
)
aiHubPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortCollisions.setStatus("mandatory")


class _AiHubPortStatus_Type(Integer32):
    """Custom type aiHubPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_AiHubPortStatus_Type.__name__ = "Integer32"
_AiHubPortStatus_Object = MibTableColumn
aiHubPortStatus = _AiHubPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 7),
    _AiHubPortStatus_Type()
)
aiHubPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortStatus.setStatus("mandatory")
_AiHubPortLinkErrors_Type = Counter32
_AiHubPortLinkErrors_Object = MibTableColumn
aiHubPortLinkErrors = _AiHubPortLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 8),
    _AiHubPortLinkErrors_Type()
)
aiHubPortLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortLinkErrors.setStatus("mandatory")
_AiHubPortShortPackets_Type = Counter32
_AiHubPortShortPackets_Object = MibTableColumn
aiHubPortShortPackets = _AiHubPortShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 9),
    _AiHubPortShortPackets_Type()
)
aiHubPortShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortShortPackets.setStatus("mandatory")
_AiHubPortJabbers_Type = Counter32
_AiHubPortJabbers_Object = MibTableColumn
aiHubPortJabbers = _AiHubPortJabbers_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 10),
    _AiHubPortJabbers_Type()
)
aiHubPortJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortJabbers.setStatus("mandatory")
_AiHubPortPartition_Type = Counter32
_AiHubPortPartition_Object = MibTableColumn
aiHubPortPartition = _AiHubPortPartition_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 11),
    _AiHubPortPartition_Type()
)
aiHubPortPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortPartition.setStatus("mandatory")


class _AiHubPortZero_Type(Integer32):
    """Custom type aiHubPortZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_AiHubPortZero_Type.__name__ = "Integer32"
_AiHubPortZero_Object = MibTableColumn
aiHubPortZero = _AiHubPortZero_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 12),
    _AiHubPortZero_Type()
)
aiHubPortZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHubPortZero.setStatus("mandatory")
_AiHubPortZeroTime_Type = TimeTicks
_AiHubPortZeroTime_Object = MibTableColumn
aiHubPortZeroTime = _AiHubPortZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 3, 1, 13),
    _AiHubPortZeroTime_Type()
)
aiHubPortZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHubPortZeroTime.setStatus("mandatory")


class _AiHubLogMessage_Type(DisplayString):
    """Custom type aiHubLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AiHubLogMessage_Type.__name__ = "DisplayString"
_AiHubLogMessage_Object = MibScalar
aiHubLogMessage = _AiHubLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 4),
    _AiHubLogMessage_Type()
)
aiHubLogMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHubLogMessage.setStatus("mandatory")


class _AiHubPortAutoPartitionLimit_Type(Integer32):
    """Custom type aiHubPortAutoPartitionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coll31", 1),
          ("coll63", 2))
    )


_AiHubPortAutoPartitionLimit_Type.__name__ = "Integer32"
_AiHubPortAutoPartitionLimit_Object = MibScalar
aiHubPortAutoPartitionLimit = _AiHubPortAutoPartitionLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 3, 5),
    _AiHubPortAutoPartitionLimit_Type()
)
aiHubPortAutoPartitionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHubPortAutoPartitionLimit.setStatus("mandatory")
_AiGroup_ObjectIdentity = ObjectIdentity
aiGroup = _AiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4)
)
_AiGroup194_ObjectIdentity = ObjectIdentity
aiGroup194 = _AiGroup194_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194)
)
_AiGroup194Ver7_ObjectIdentity = ObjectIdentity
aiGroup194Ver7 = _AiGroup194Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7)
)
_AiGroup194Ver71_ObjectIdentity = ObjectIdentity
aiGroup194Ver71 = _AiGroup194Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 1)
)
_AiGroup194Ver72_ObjectIdentity = ObjectIdentity
aiGroup194Ver72 = _AiGroup194Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 2)
)
_AiGroup194Ver73_ObjectIdentity = ObjectIdentity
aiGroup194Ver73 = _AiGroup194Ver73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 3)
)
_AiGroup194Ver74_ObjectIdentity = ObjectIdentity
aiGroup194Ver74 = _AiGroup194Ver74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 4)
)
_AiISISGre_ObjectIdentity = ObjectIdentity
aiISISGre = _AiISISGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 5)
)
_AiManager_ObjectIdentity = ObjectIdentity
aiManager = _AiManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 6)
)
_AiSoftware_ObjectIdentity = ObjectIdentity
aiSoftware = _AiSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 7)
)
_AiSystem_ObjectIdentity = ObjectIdentity
aiSystem = _AiSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AI194HUB-MIB",
    **{"aii": aii,
       "aiProxy": aiProxy,
       "aiSystemOID": aiSystemOID,
       "aiHub": aiHub,
       "aiHubTwistedPairPortNumber": aiHubTwistedPairPortNumber,
       "aiHubNonTwistedPairPortNumber": aiHubNonTwistedPairPortNumber,
       "aiHubPortTable": aiHubPortTable,
       "aiHubPortEntry": aiHubPortEntry,
       "aiHubPortIndex": aiHubPortIndex,
       "aiHubPortName": aiHubPortName,
       "aiHubPortAdminState": aiHubPortAdminState,
       "aiHubPortAutoPartitionState": aiHubPortAutoPartitionState,
       "aiHubPortErrors": aiHubPortErrors,
       "aiHubPortCollisions": aiHubPortCollisions,
       "aiHubPortStatus": aiHubPortStatus,
       "aiHubPortLinkErrors": aiHubPortLinkErrors,
       "aiHubPortShortPackets": aiHubPortShortPackets,
       "aiHubPortJabbers": aiHubPortJabbers,
       "aiHubPortPartition": aiHubPortPartition,
       "aiHubPortZero": aiHubPortZero,
       "aiHubPortZeroTime": aiHubPortZeroTime,
       "aiHubLogMessage": aiHubLogMessage,
       "aiHubPortAutoPartitionLimit": aiHubPortAutoPartitionLimit,
       "aiGroup": aiGroup,
       "aiGroup194": aiGroup194,
       "aiGroup194Ver7": aiGroup194Ver7,
       "aiGroup194Ver71": aiGroup194Ver71,
       "aiGroup194Ver72": aiGroup194Ver72,
       "aiGroup194Ver73": aiGroup194Ver73,
       "aiGroup194Ver74": aiGroup194Ver74,
       "aiISISGre": aiISISGre,
       "aiManager": aiManager,
       "aiSoftware": aiSoftware,
       "aiSystem": aiSystem}
)
