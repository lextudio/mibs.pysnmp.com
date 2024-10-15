# SNMP MIB module (CTRMONXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRMONXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:28 2024
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

(ctronRmon,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctronRmon")

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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

_CtDiscovery_ObjectIdentity = ObjectIdentity
ctDiscovery = _CtDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20)
)
_CtDiscoveryProtocol_ObjectIdentity = ObjectIdentity
ctDiscoveryProtocol = _CtDiscoveryProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1)
)
_CtProtIP_ObjectIdentity = ObjectIdentity
ctProtIP = _CtProtIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 1)
)
_CtProtNetware_ObjectIdentity = ObjectIdentity
ctProtNetware = _CtProtNetware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 2)
)
_CtProtDecNet_ObjectIdentity = ObjectIdentity
ctProtDecNet = _CtProtDecNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 1, 3)
)
_CtDiscoveryControlTable_Object = MibTable
ctDiscoveryControlTable = _CtDiscoveryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2)
)
if mibBuilder.loadTexts:
    ctDiscoveryControlTable.setStatus("mandatory")
_CtDiscoveryControlEntry_Object = MibTableRow
ctDiscoveryControlEntry = _CtDiscoveryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1)
)
ctDiscoveryControlEntry.setIndexNames(
    (0, "CTRMONXT-MIB", "ctDiscoveryControlIndex"),
)
if mibBuilder.loadTexts:
    ctDiscoveryControlEntry.setStatus("mandatory")


class _CtDiscoveryControlIndex_Type(Integer32):
    """Custom type ctDiscoveryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtDiscoveryControlIndex_Type.__name__ = "Integer32"
_CtDiscoveryControlIndex_Object = MibTableColumn
ctDiscoveryControlIndex = _CtDiscoveryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 1),
    _CtDiscoveryControlIndex_Type()
)
ctDiscoveryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryControlIndex.setStatus("mandatory")
_CtDiscoveryControlDataSource_Type = ObjectIdentifier
_CtDiscoveryControlDataSource_Object = MibTableColumn
ctDiscoveryControlDataSource = _CtDiscoveryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 2),
    _CtDiscoveryControlDataSource_Type()
)
ctDiscoveryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDiscoveryControlDataSource.setStatus("mandatory")
_CtDiscoveryControlProtocol_Type = ObjectIdentifier
_CtDiscoveryControlProtocol_Object = MibTableColumn
ctDiscoveryControlProtocol = _CtDiscoveryControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 3),
    _CtDiscoveryControlProtocol_Type()
)
ctDiscoveryControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDiscoveryControlProtocol.setStatus("mandatory")
_CtDiscoveryControlTableSize_Type = Integer32
_CtDiscoveryControlTableSize_Object = MibTableColumn
ctDiscoveryControlTableSize = _CtDiscoveryControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 4),
    _CtDiscoveryControlTableSize_Type()
)
ctDiscoveryControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryControlTableSize.setStatus("mandatory")
_CtDiscoveryControlLastDeleteTime_Type = TimeTicks
_CtDiscoveryControlLastDeleteTime_Object = MibTableColumn
ctDiscoveryControlLastDeleteTime = _CtDiscoveryControlLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 5),
    _CtDiscoveryControlLastDeleteTime_Type()
)
ctDiscoveryControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryControlLastDeleteTime.setStatus("mandatory")
_CtDiscoveryControlAgeInterval_Type = Integer32
_CtDiscoveryControlAgeInterval_Object = MibTableColumn
ctDiscoveryControlAgeInterval = _CtDiscoveryControlAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 6),
    _CtDiscoveryControlAgeInterval_Type()
)
ctDiscoveryControlAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDiscoveryControlAgeInterval.setStatus("mandatory")
_CtDiscoveryControlOwner_Type = OwnerString
_CtDiscoveryControlOwner_Object = MibTableColumn
ctDiscoveryControlOwner = _CtDiscoveryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 7),
    _CtDiscoveryControlOwner_Type()
)
ctDiscoveryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDiscoveryControlOwner.setStatus("mandatory")
_CtDiscoveryControlStatus_Type = EntryStatus
_CtDiscoveryControlStatus_Object = MibTableColumn
ctDiscoveryControlStatus = _CtDiscoveryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 2, 1, 8),
    _CtDiscoveryControlStatus_Type()
)
ctDiscoveryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDiscoveryControlStatus.setStatus("mandatory")
_CtDiscoveryMNTable_Object = MibTable
ctDiscoveryMNTable = _CtDiscoveryMNTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3)
)
if mibBuilder.loadTexts:
    ctDiscoveryMNTable.setStatus("mandatory")
_CtDiscoveryMNEntry_Object = MibTableRow
ctDiscoveryMNEntry = _CtDiscoveryMNEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1)
)
ctDiscoveryMNEntry.setIndexNames(
    (0, "CTRMONXT-MIB", "ctDiscoveryMNIndex"),
    (0, "CTRMONXT-MIB", "ctDiscoveryMNMACAddress"),
    (0, "CTRMONXT-MIB", "ctDiscoveryMNNetworkAddress"),
)
if mibBuilder.loadTexts:
    ctDiscoveryMNEntry.setStatus("mandatory")
_CtDiscoveryMNMACAddress_Type = OctetString
_CtDiscoveryMNMACAddress_Object = MibTableColumn
ctDiscoveryMNMACAddress = _CtDiscoveryMNMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 1),
    _CtDiscoveryMNMACAddress_Type()
)
ctDiscoveryMNMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNMACAddress.setStatus("mandatory")
_CtDiscoveryMNNetworkAddress_Type = OctetString
_CtDiscoveryMNNetworkAddress_Object = MibTableColumn
ctDiscoveryMNNetworkAddress = _CtDiscoveryMNNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 2),
    _CtDiscoveryMNNetworkAddress_Type()
)
ctDiscoveryMNNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNNetworkAddress.setStatus("mandatory")


class _CtDiscoveryMNIndex_Type(Integer32):
    """Custom type ctDiscoveryMNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtDiscoveryMNIndex_Type.__name__ = "Integer32"
_CtDiscoveryMNIndex_Object = MibTableColumn
ctDiscoveryMNIndex = _CtDiscoveryMNIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 3),
    _CtDiscoveryMNIndex_Type()
)
ctDiscoveryMNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNIndex.setStatus("mandatory")
_CtDiscoveryMNCreationTime_Type = TimeTicks
_CtDiscoveryMNCreationTime_Object = MibTableColumn
ctDiscoveryMNCreationTime = _CtDiscoveryMNCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 4),
    _CtDiscoveryMNCreationTime_Type()
)
ctDiscoveryMNCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNCreationTime.setStatus("mandatory")
_CtDiscoveryMNLastTransmitTime_Type = TimeTicks
_CtDiscoveryMNLastTransmitTime_Object = MibTableColumn
ctDiscoveryMNLastTransmitTime = _CtDiscoveryMNLastTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 5),
    _CtDiscoveryMNLastTransmitTime_Type()
)
ctDiscoveryMNLastTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNLastTransmitTime.setStatus("mandatory")
_CtDiscoveryMNBoard_Type = Integer32
_CtDiscoveryMNBoard_Object = MibTableColumn
ctDiscoveryMNBoard = _CtDiscoveryMNBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 6),
    _CtDiscoveryMNBoard_Type()
)
ctDiscoveryMNBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNBoard.setStatus("mandatory")
_CtDiscoveryMNPort_Type = Integer32
_CtDiscoveryMNPort_Object = MibTableColumn
ctDiscoveryMNPort = _CtDiscoveryMNPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 3, 1, 7),
    _CtDiscoveryMNPort_Type()
)
ctDiscoveryMNPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryMNPort.setStatus("mandatory")
_CtDiscoveryNMTable_Object = MibTable
ctDiscoveryNMTable = _CtDiscoveryNMTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4)
)
if mibBuilder.loadTexts:
    ctDiscoveryNMTable.setStatus("mandatory")
_CtDiscoveryNMEntry_Object = MibTableRow
ctDiscoveryNMEntry = _CtDiscoveryNMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1)
)
ctDiscoveryNMEntry.setIndexNames(
    (0, "CTRMONXT-MIB", "ctDiscoveryNMIndex"),
    (0, "CTRMONXT-MIB", "ctDiscoveryNMNetworkAddress"),
    (0, "CTRMONXT-MIB", "ctDiscoveryNMMACAddress"),
)
if mibBuilder.loadTexts:
    ctDiscoveryNMEntry.setStatus("mandatory")
_CtDiscoveryNMNetworkAddress_Type = OctetString
_CtDiscoveryNMNetworkAddress_Object = MibTableColumn
ctDiscoveryNMNetworkAddress = _CtDiscoveryNMNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 1),
    _CtDiscoveryNMNetworkAddress_Type()
)
ctDiscoveryNMNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMNetworkAddress.setStatus("mandatory")
_CtDiscoveryNMMACAddress_Type = OctetString
_CtDiscoveryNMMACAddress_Object = MibTableColumn
ctDiscoveryNMMACAddress = _CtDiscoveryNMMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 2),
    _CtDiscoveryNMMACAddress_Type()
)
ctDiscoveryNMMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMMACAddress.setStatus("mandatory")


class _CtDiscoveryNMIndex_Type(Integer32):
    """Custom type ctDiscoveryNMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtDiscoveryNMIndex_Type.__name__ = "Integer32"
_CtDiscoveryNMIndex_Object = MibTableColumn
ctDiscoveryNMIndex = _CtDiscoveryNMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 3),
    _CtDiscoveryNMIndex_Type()
)
ctDiscoveryNMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMIndex.setStatus("mandatory")
_CtDiscoveryNMCreationTime_Type = TimeTicks
_CtDiscoveryNMCreationTime_Object = MibTableColumn
ctDiscoveryNMCreationTime = _CtDiscoveryNMCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 4),
    _CtDiscoveryNMCreationTime_Type()
)
ctDiscoveryNMCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMCreationTime.setStatus("mandatory")
_CtDiscoveryNMLastTransmitTime_Type = TimeTicks
_CtDiscoveryNMLastTransmitTime_Object = MibTableColumn
ctDiscoveryNMLastTransmitTime = _CtDiscoveryNMLastTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 5),
    _CtDiscoveryNMLastTransmitTime_Type()
)
ctDiscoveryNMLastTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMLastTransmitTime.setStatus("mandatory")
_CtDiscoveryNMBoard_Type = Integer32
_CtDiscoveryNMBoard_Object = MibTableColumn
ctDiscoveryNMBoard = _CtDiscoveryNMBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 6),
    _CtDiscoveryNMBoard_Type()
)
ctDiscoveryNMBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMBoard.setStatus("mandatory")
_CtDiscoveryNMPort_Type = Integer32
_CtDiscoveryNMPort_Object = MibTableColumn
ctDiscoveryNMPort = _CtDiscoveryNMPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2, 20, 4, 1, 7),
    _CtDiscoveryNMPort_Type()
)
ctDiscoveryNMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDiscoveryNMPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRMONXT-MIB",
    **{"ctDiscovery": ctDiscovery,
       "ctDiscoveryProtocol": ctDiscoveryProtocol,
       "ctProtIP": ctProtIP,
       "ctProtNetware": ctProtNetware,
       "ctProtDecNet": ctProtDecNet,
       "ctDiscoveryControlTable": ctDiscoveryControlTable,
       "ctDiscoveryControlEntry": ctDiscoveryControlEntry,
       "ctDiscoveryControlIndex": ctDiscoveryControlIndex,
       "ctDiscoveryControlDataSource": ctDiscoveryControlDataSource,
       "ctDiscoveryControlProtocol": ctDiscoveryControlProtocol,
       "ctDiscoveryControlTableSize": ctDiscoveryControlTableSize,
       "ctDiscoveryControlLastDeleteTime": ctDiscoveryControlLastDeleteTime,
       "ctDiscoveryControlAgeInterval": ctDiscoveryControlAgeInterval,
       "ctDiscoveryControlOwner": ctDiscoveryControlOwner,
       "ctDiscoveryControlStatus": ctDiscoveryControlStatus,
       "ctDiscoveryMNTable": ctDiscoveryMNTable,
       "ctDiscoveryMNEntry": ctDiscoveryMNEntry,
       "ctDiscoveryMNMACAddress": ctDiscoveryMNMACAddress,
       "ctDiscoveryMNNetworkAddress": ctDiscoveryMNNetworkAddress,
       "ctDiscoveryMNIndex": ctDiscoveryMNIndex,
       "ctDiscoveryMNCreationTime": ctDiscoveryMNCreationTime,
       "ctDiscoveryMNLastTransmitTime": ctDiscoveryMNLastTransmitTime,
       "ctDiscoveryMNBoard": ctDiscoveryMNBoard,
       "ctDiscoveryMNPort": ctDiscoveryMNPort,
       "ctDiscoveryNMTable": ctDiscoveryNMTable,
       "ctDiscoveryNMEntry": ctDiscoveryNMEntry,
       "ctDiscoveryNMNetworkAddress": ctDiscoveryNMNetworkAddress,
       "ctDiscoveryNMMACAddress": ctDiscoveryNMMACAddress,
       "ctDiscoveryNMIndex": ctDiscoveryNMIndex,
       "ctDiscoveryNMCreationTime": ctDiscoveryNMCreationTime,
       "ctDiscoveryNMLastTransmitTime": ctDiscoveryNMLastTransmitTime,
       "ctDiscoveryNMBoard": ctDiscoveryNMBoard,
       "ctDiscoveryNMPort": ctDiscoveryNMPort}
)
