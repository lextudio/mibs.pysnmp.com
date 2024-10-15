# SNMP MIB module (CENTILLION-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-FDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:04 2024
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

(BitField,
 CardId,
 PortId,
 StatusIndicator,
 sysConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "BitField",
    "CardId",
    "PortId",
    "StatusIndicator",
    "sysConfig")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class FdbTypeId(Integer32):
    """Custom type FdbTypeId based on Integer32"""
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
        *(("ethernet", 3),
          ("route-descriptor", 4),
          ("token-ring", 2),
          ("unknown", 1))
    )





class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdbGroup_ObjectIdentity = ObjectIdentity
fdbGroup = _FdbGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22)
)


class _FdbRemoteAgingTimer_Type(Integer32):
    """Custom type fdbRemoteAgingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_FdbRemoteAgingTimer_Type.__name__ = "Integer32"
_FdbRemoteAgingTimer_Object = MibScalar
fdbRemoteAgingTimer = _FdbRemoteAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 1),
    _FdbRemoteAgingTimer_Type()
)
fdbRemoteAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbRemoteAgingTimer.setStatus("mandatory")


class _FdbTableFlush_Type(OctetString):
    """Custom type fdbTableFlush based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_FdbTableFlush_Type.__name__ = "OctetString"
_FdbTableFlush_Object = MibScalar
fdbTableFlush = _FdbTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 2),
    _FdbTableFlush_Type()
)
fdbTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbTableFlush.setStatus("mandatory")
_FdbTable_Object = MibTable
fdbTable = _FdbTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3)
)
if mibBuilder.loadTexts:
    fdbTable.setStatus("deprecated")
_FdbEntry_Object = MibTableRow
fdbEntry = _FdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1)
)
fdbEntry.setIndexNames(
    (0, "CENTILLION-FDB-MIB", "fdbType"),
    (0, "CENTILLION-FDB-MIB", "fdbAddress"),
    (0, "CENTILLION-FDB-MIB", "fdbCard"),
    (0, "CENTILLION-FDB-MIB", "fdbPort"),
)
if mibBuilder.loadTexts:
    fdbEntry.setStatus("deprecated")
_FdbType_Type = FdbTypeId
_FdbType_Object = MibTableColumn
fdbType = _FdbType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 1),
    _FdbType_Type()
)
fdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbType.setStatus("deprecated")
_FdbAddress_Type = PhysAddress
_FdbAddress_Object = MibTableColumn
fdbAddress = _FdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 2),
    _FdbAddress_Type()
)
fdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbAddress.setStatus("deprecated")
_FdbCard_Type = CardId
_FdbCard_Object = MibTableColumn
fdbCard = _FdbCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 3),
    _FdbCard_Type()
)
fdbCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbCard.setStatus("deprecated")
_FdbPort_Type = PortId
_FdbPort_Object = MibTableColumn
fdbPort = _FdbPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 4),
    _FdbPort_Type()
)
fdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbPort.setStatus("deprecated")
_FdbIfIndex_Type = Integer32
_FdbIfIndex_Object = MibTableColumn
fdbIfIndex = _FdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 5),
    _FdbIfIndex_Type()
)
fdbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbIfIndex.setStatus("deprecated")
_FdbStatus_Type = StatusIndicator
_FdbStatus_Object = MibTableColumn
fdbStatus = _FdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 6),
    _FdbStatus_Type()
)
fdbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbStatus.setStatus("deprecated")
_FdbLocal_Type = BitField
_FdbLocal_Object = MibTableColumn
fdbLocal = _FdbLocal_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 7),
    _FdbLocal_Type()
)
fdbLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbLocal.setStatus("deprecated")
_FdbStatic_Type = BitField
_FdbStatic_Object = MibTableColumn
fdbStatic = _FdbStatic_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 8),
    _FdbStatic_Type()
)
fdbStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatic.setStatus("deprecated")
_FdbDuplicate_Type = BitField
_FdbDuplicate_Object = MibTableColumn
fdbDuplicate = _FdbDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 9),
    _FdbDuplicate_Type()
)
fdbDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbDuplicate.setStatus("deprecated")


class _FdbRIFPath_Type(OctetString):
    """Custom type fdbRIFPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_FdbRIFPath_Type.__name__ = "OctetString"
_FdbRIFPath_Object = MibTableColumn
fdbRIFPath = _FdbRIFPath_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 10),
    _FdbRIFPath_Type()
)
fdbRIFPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbRIFPath.setStatus("deprecated")
_FdbSSTable_Object = MibTable
fdbSSTable = _FdbSSTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4)
)
if mibBuilder.loadTexts:
    fdbSSTable.setStatus("mandatory")
_FdbSSEntry_Object = MibTableRow
fdbSSEntry = _FdbSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1)
)
fdbSSEntry.setIndexNames(
    (0, "CENTILLION-FDB-MIB", "fdbSSIndex"),
)
if mibBuilder.loadTexts:
    fdbSSEntry.setStatus("mandatory")
_FdbSSIndex_Type = Integer32
_FdbSSIndex_Object = MibTableColumn
fdbSSIndex = _FdbSSIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 1),
    _FdbSSIndex_Type()
)
fdbSSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSSIndex.setStatus("mandatory")
_FdbSSType_Type = FdbTypeId
_FdbSSType_Object = MibTableColumn
fdbSSType = _FdbSSType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 2),
    _FdbSSType_Type()
)
fdbSSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSSType.setStatus("mandatory")
_FdbSSAddress_Type = PhysAddress
_FdbSSAddress_Object = MibTableColumn
fdbSSAddress = _FdbSSAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 3),
    _FdbSSAddress_Type()
)
fdbSSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSSAddress.setStatus("mandatory")
_FdbSSCard_Type = CardId
_FdbSSCard_Object = MibTableColumn
fdbSSCard = _FdbSSCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 4),
    _FdbSSCard_Type()
)
fdbSSCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSSCard.setStatus("mandatory")
_FdbSSPort_Type = PortId
_FdbSSPort_Object = MibTableColumn
fdbSSPort = _FdbSSPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 5),
    _FdbSSPort_Type()
)
fdbSSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSSPort.setStatus("mandatory")
_FdbSSVlanId_Type = VlanId
_FdbSSVlanId_Object = MibTableColumn
fdbSSVlanId = _FdbSSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 6),
    _FdbSSVlanId_Type()
)
fdbSSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSSVlanId.setStatus("mandatory")
_CnfdbTable_Object = MibTable
cnfdbTable = _CnfdbTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5)
)
if mibBuilder.loadTexts:
    cnfdbTable.setStatus("mandatory")
_CnfdbEntry_Object = MibTableRow
cnfdbEntry = _CnfdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1)
)
cnfdbEntry.setIndexNames(
    (0, "CENTILLION-FDB-MIB", "cnfdbType"),
    (0, "CENTILLION-FDB-MIB", "cnfdbAddress"),
    (0, "CENTILLION-FDB-MIB", "cnfdbCard"),
    (0, "CENTILLION-FDB-MIB", "cnfdbPort"),
    (0, "CENTILLION-FDB-MIB", "cnfdbVlanId"),
)
if mibBuilder.loadTexts:
    cnfdbEntry.setStatus("mandatory")
_CnfdbType_Type = FdbTypeId
_CnfdbType_Object = MibTableColumn
cnfdbType = _CnfdbType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 1),
    _CnfdbType_Type()
)
cnfdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbType.setStatus("mandatory")
_CnfdbAddress_Type = PhysAddress
_CnfdbAddress_Object = MibTableColumn
cnfdbAddress = _CnfdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 2),
    _CnfdbAddress_Type()
)
cnfdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbAddress.setStatus("mandatory")
_CnfdbCard_Type = CardId
_CnfdbCard_Object = MibTableColumn
cnfdbCard = _CnfdbCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 3),
    _CnfdbCard_Type()
)
cnfdbCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbCard.setStatus("mandatory")
_CnfdbPort_Type = PortId
_CnfdbPort_Object = MibTableColumn
cnfdbPort = _CnfdbPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 4),
    _CnfdbPort_Type()
)
cnfdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbPort.setStatus("mandatory")
_CnfdbVlanId_Type = VlanId
_CnfdbVlanId_Object = MibTableColumn
cnfdbVlanId = _CnfdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 5),
    _CnfdbVlanId_Type()
)
cnfdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbVlanId.setStatus("mandatory")
_CnfdbIfIndex_Type = Integer32
_CnfdbIfIndex_Object = MibTableColumn
cnfdbIfIndex = _CnfdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 6),
    _CnfdbIfIndex_Type()
)
cnfdbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbIfIndex.setStatus("mandatory")
_CnfdbStatus_Type = StatusIndicator
_CnfdbStatus_Object = MibTableColumn
cnfdbStatus = _CnfdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 7),
    _CnfdbStatus_Type()
)
cnfdbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfdbStatus.setStatus("mandatory")
_CnfdbLocal_Type = BitField
_CnfdbLocal_Object = MibTableColumn
cnfdbLocal = _CnfdbLocal_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 8),
    _CnfdbLocal_Type()
)
cnfdbLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfdbLocal.setStatus("mandatory")
_CnfdbStatic_Type = BitField
_CnfdbStatic_Object = MibTableColumn
cnfdbStatic = _CnfdbStatic_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 9),
    _CnfdbStatic_Type()
)
cnfdbStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbStatic.setStatus("mandatory")
_CnfdbDuplicate_Type = BitField
_CnfdbDuplicate_Object = MibTableColumn
cnfdbDuplicate = _CnfdbDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 10),
    _CnfdbDuplicate_Type()
)
cnfdbDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfdbDuplicate.setStatus("mandatory")


class _CnfdbRIFPath_Type(OctetString):
    """Custom type cnfdbRIFPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_CnfdbRIFPath_Type.__name__ = "OctetString"
_CnfdbRIFPath_Object = MibTableColumn
cnfdbRIFPath = _CnfdbRIFPath_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 11),
    _CnfdbRIFPath_Type()
)
cnfdbRIFPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfdbRIFPath.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-FDB-MIB",
    **{"FdbTypeId": FdbTypeId,
       "VlanId": VlanId,
       "fdbGroup": fdbGroup,
       "fdbRemoteAgingTimer": fdbRemoteAgingTimer,
       "fdbTableFlush": fdbTableFlush,
       "fdbTable": fdbTable,
       "fdbEntry": fdbEntry,
       "fdbType": fdbType,
       "fdbAddress": fdbAddress,
       "fdbCard": fdbCard,
       "fdbPort": fdbPort,
       "fdbIfIndex": fdbIfIndex,
       "fdbStatus": fdbStatus,
       "fdbLocal": fdbLocal,
       "fdbStatic": fdbStatic,
       "fdbDuplicate": fdbDuplicate,
       "fdbRIFPath": fdbRIFPath,
       "fdbSSTable": fdbSSTable,
       "fdbSSEntry": fdbSSEntry,
       "fdbSSIndex": fdbSSIndex,
       "fdbSSType": fdbSSType,
       "fdbSSAddress": fdbSSAddress,
       "fdbSSCard": fdbSSCard,
       "fdbSSPort": fdbSSPort,
       "fdbSSVlanId": fdbSSVlanId,
       "cnfdbTable": cnfdbTable,
       "cnfdbEntry": cnfdbEntry,
       "cnfdbType": cnfdbType,
       "cnfdbAddress": cnfdbAddress,
       "cnfdbCard": cnfdbCard,
       "cnfdbPort": cnfdbPort,
       "cnfdbVlanId": cnfdbVlanId,
       "cnfdbIfIndex": cnfdbIfIndex,
       "cnfdbStatus": cnfdbStatus,
       "cnfdbLocal": cnfdbLocal,
       "cnfdbStatic": cnfdbStatic,
       "cnfdbDuplicate": cnfdbDuplicate,
       "cnfdbRIFPath": cnfdbRIFPath}
)
