# SNMP MIB module (AILUXCONNECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AILUXCONNECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:12 2024
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

(AIIConnType,) = mibBuilder.importSymbols(
    "AISYSTEM-MIB",
    "AIIConnType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiLuxConnect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 33)
)
aiLuxConnect.setRevisions(
        ("2001-04-30 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiLCTrapInfo_ObjectIdentity = ObjectIdentity
aiLCTrapInfo = _AiLCTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 33, 0)
)
_AiLCGtranActiveTable_Object = MibTable
aiLCGtranActiveTable = _AiLCGtranActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1)
)
if mibBuilder.loadTexts:
    aiLCGtranActiveTable.setStatus("current")
_AiLCGtranActiveEntry_Object = MibTableRow
aiLCGtranActiveEntry = _AiLCGtranActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1)
)
aiLCGtranActiveEntry.setIndexNames(
    (0, "AILUXCONNECT-MIB", "aiLCGtranActiveIndex"),
)
if mibBuilder.loadTexts:
    aiLCGtranActiveEntry.setStatus("current")
_AiLCGtranActiveIndex_Type = InterfaceIndex
_AiLCGtranActiveIndex_Object = MibTableColumn
aiLCGtranActiveIndex = _AiLCGtranActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 1),
    _AiLCGtranActiveIndex_Type()
)
aiLCGtranActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveIndex.setStatus("current")
_AiLCGtranActiveBackupIndex_Type = InterfaceIndex
_AiLCGtranActiveBackupIndex_Object = MibTableColumn
aiLCGtranActiveBackupIndex = _AiLCGtranActiveBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 2),
    _AiLCGtranActiveBackupIndex_Type()
)
aiLCGtranActiveBackupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveBackupIndex.setStatus("current")


class _AiLCGtranActiveSpan_Type(Integer32):
    """Custom type aiLCGtranActiveSpan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protect", 2),
          ("work", 1))
    )


_AiLCGtranActiveSpan_Type.__name__ = "Integer32"
_AiLCGtranActiveSpan_Object = MibTableColumn
aiLCGtranActiveSpan = _AiLCGtranActiveSpan_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 3),
    _AiLCGtranActiveSpan_Type()
)
aiLCGtranActiveSpan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLCGtranActiveSpan.setStatus("current")


class _AiLCGtranActiveRxUtilization_Type(Integer32):
    """Custom type aiLCGtranActiveRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AiLCGtranActiveRxUtilization_Type.__name__ = "Integer32"
_AiLCGtranActiveRxUtilization_Object = MibTableColumn
aiLCGtranActiveRxUtilization = _AiLCGtranActiveRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 4),
    _AiLCGtranActiveRxUtilization_Type()
)
aiLCGtranActiveRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveRxUtilization.setStatus("current")


class _AiLCGtranActiveTxUtilization_Type(Integer32):
    """Custom type aiLCGtranActiveTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AiLCGtranActiveTxUtilization_Type.__name__ = "Integer32"
_AiLCGtranActiveTxUtilization_Object = MibTableColumn
aiLCGtranActiveTxUtilization = _AiLCGtranActiveTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 5),
    _AiLCGtranActiveTxUtilization_Type()
)
aiLCGtranActiveTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveTxUtilization.setStatus("current")
_AiLCGtranActiveClockSlave_Type = TruthValue
_AiLCGtranActiveClockSlave_Object = MibTableColumn
aiLCGtranActiveClockSlave = _AiLCGtranActiveClockSlave_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 6),
    _AiLCGtranActiveClockSlave_Type()
)
aiLCGtranActiveClockSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLCGtranActiveClockSlave.setStatus("current")


class _AiLCGtranActiveCoolerStatus_Type(Integer32):
    """Custom type aiLCGtranActiveCoolerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AiLCGtranActiveCoolerStatus_Type.__name__ = "Integer32"
_AiLCGtranActiveCoolerStatus_Object = MibTableColumn
aiLCGtranActiveCoolerStatus = _AiLCGtranActiveCoolerStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 7),
    _AiLCGtranActiveCoolerStatus_Type()
)
aiLCGtranActiveCoolerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLCGtranActiveCoolerStatus.setStatus("current")


class _AiLCGtranActiveTemperature_Type(Integer32):
    """Custom type aiLCGtranActiveTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("trouble", 2))
    )


_AiLCGtranActiveTemperature_Type.__name__ = "Integer32"
_AiLCGtranActiveTemperature_Object = MibTableColumn
aiLCGtranActiveTemperature = _AiLCGtranActiveTemperature_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 8),
    _AiLCGtranActiveTemperature_Type()
)
aiLCGtranActiveTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveTemperature.setStatus("current")


class _AiLCGtranActiveRxPower_Type(Integer32):
    """Custom type aiLCGtranActiveRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("over", 3),
          ("under", 2))
    )


_AiLCGtranActiveRxPower_Type.__name__ = "Integer32"
_AiLCGtranActiveRxPower_Object = MibTableColumn
aiLCGtranActiveRxPower = _AiLCGtranActiveRxPower_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 9),
    _AiLCGtranActiveRxPower_Type()
)
aiLCGtranActiveRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveRxPower.setStatus("current")


class _AiLCGtranActiveTxPower_Type(Integer32):
    """Custom type aiLCGtranActiveTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("over", 3),
          ("under", 2))
    )


_AiLCGtranActiveTxPower_Type.__name__ = "Integer32"
_AiLCGtranActiveTxPower_Object = MibTableColumn
aiLCGtranActiveTxPower = _AiLCGtranActiveTxPower_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 10),
    _AiLCGtranActiveTxPower_Type()
)
aiLCGtranActiveTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranActiveTxPower.setStatus("current")
_AiLCGtranBackupTable_Object = MibTable
aiLCGtranBackupTable = _AiLCGtranBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 2)
)
if mibBuilder.loadTexts:
    aiLCGtranBackupTable.setStatus("current")
_AiLCGtranBackupEntry_Object = MibTableRow
aiLCGtranBackupEntry = _AiLCGtranBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 2, 1)
)
aiLCGtranBackupEntry.setIndexNames(
    (0, "AILUXCONNECT-MIB", "aiLCGtranBackupIndex"),
)
if mibBuilder.loadTexts:
    aiLCGtranBackupEntry.setStatus("current")
_AiLCGtranBackupIndex_Type = InterfaceIndex
_AiLCGtranBackupIndex_Object = MibTableColumn
aiLCGtranBackupIndex = _AiLCGtranBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 2, 1, 1),
    _AiLCGtranBackupIndex_Type()
)
aiLCGtranBackupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranBackupIndex.setStatus("current")
_AiLCGtranBackupActiveIndex_Type = InterfaceIndex
_AiLCGtranBackupActiveIndex_Object = MibTableColumn
aiLCGtranBackupActiveIndex = _AiLCGtranBackupActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 2, 1, 2),
    _AiLCGtranBackupActiveIndex_Type()
)
aiLCGtranBackupActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGtranBackupActiveIndex.setStatus("current")
_AiLcGbicTable_Object = MibTable
aiLcGbicTable = _AiLcGbicTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3)
)
if mibBuilder.loadTexts:
    aiLcGbicTable.setStatus("current")
_AiLCGbicEntry_Object = MibTableRow
aiLCGbicEntry = _AiLCGbicEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3, 1)
)
aiLCGbicEntry.setIndexNames(
    (0, "AILUXCONNECT-MIB", "aiLCGbicIndex"),
)
if mibBuilder.loadTexts:
    aiLCGbicEntry.setStatus("current")
_AiLCGbicIndex_Type = InterfaceIndex
_AiLCGbicIndex_Object = MibTableColumn
aiLCGbicIndex = _AiLCGbicIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 1),
    _AiLCGbicIndex_Type()
)
aiLCGbicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGbicIndex.setStatus("current")
_AiLCGbicConnectorType_Type = AIIConnType
_AiLCGbicConnectorType_Object = MibTableColumn
aiLCGbicConnectorType = _AiLCGbicConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 2),
    _AiLCGbicConnectorType_Type()
)
aiLCGbicConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGbicConnectorType.setStatus("current")


class _AiLCGbicTxMode_Type(Integer32):
    """Custom type aiLCGbicTxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("gtran", 3),
          ("up", 2))
    )


_AiLCGbicTxMode_Type.__name__ = "Integer32"
_AiLCGbicTxMode_Object = MibTableColumn
aiLCGbicTxMode = _AiLCGbicTxMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 3),
    _AiLCGbicTxMode_Type()
)
aiLCGbicTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLCGbicTxMode.setStatus("current")


class _AiLCGbicRxUtilization_Type(Integer32):
    """Custom type aiLCGbicRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AiLCGbicRxUtilization_Type.__name__ = "Integer32"
_AiLCGbicRxUtilization_Object = MibTableColumn
aiLCGbicRxUtilization = _AiLCGbicRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 4),
    _AiLCGbicRxUtilization_Type()
)
aiLCGbicRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGbicRxUtilization.setStatus("current")


class _AiLCGbicTxUtilization_Type(Integer32):
    """Custom type aiLCGbicTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AiLCGbicTxUtilization_Type.__name__ = "Integer32"
_AiLCGbicTxUtilization_Object = MibTableColumn
aiLCGbicTxUtilization = _AiLCGbicTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 5),
    _AiLCGbicTxUtilization_Type()
)
aiLCGbicTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLCGbicTxUtilization.setStatus("current")

# Managed Objects groups


# Notification objects

aiLCTrapGtranSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 33, 0, 1)
)
aiLCTrapGtranSwitch.setObjects(
      *(("AILUXCONNECT-MIB", "aiLCGtranActiveIndex"),
        ("AILUXCONNECT-MIB", "aiLCGtranActiveSpan"))
)
if mibBuilder.loadTexts:
    aiLCTrapGtranSwitch.setStatus(
        "current"
    )

aiLCTrapGbicInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 33, 0, 2)
)
aiLCTrapGbicInserted.setObjects(
      *(("AILUXCONNECT-MIB", "aiLCGbicIndex"),
        ("AILUXCONNECT-MIB", "aiLCGbicConnectorType"))
)
if mibBuilder.loadTexts:
    aiLCTrapGbicInserted.setStatus(
        "current"
    )

aiLCTrapGbicRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 33, 0, 3)
)
aiLCTrapGbicRemoved.setObjects(
      *(("AILUXCONNECT-MIB", "aiLCGbicIndex"),
        ("AILUXCONNECT-MIB", "aiLCGbicConnectorType"))
)
if mibBuilder.loadTexts:
    aiLCTrapGbicRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AILUXCONNECT-MIB",
    **{"aii": aii,
       "aiLuxConnect": aiLuxConnect,
       "aiLCTrapInfo": aiLCTrapInfo,
       "aiLCTrapGtranSwitch": aiLCTrapGtranSwitch,
       "aiLCTrapGbicInserted": aiLCTrapGbicInserted,
       "aiLCTrapGbicRemoved": aiLCTrapGbicRemoved,
       "aiLCGtranActiveTable": aiLCGtranActiveTable,
       "aiLCGtranActiveEntry": aiLCGtranActiveEntry,
       "aiLCGtranActiveIndex": aiLCGtranActiveIndex,
       "aiLCGtranActiveBackupIndex": aiLCGtranActiveBackupIndex,
       "aiLCGtranActiveSpan": aiLCGtranActiveSpan,
       "aiLCGtranActiveRxUtilization": aiLCGtranActiveRxUtilization,
       "aiLCGtranActiveTxUtilization": aiLCGtranActiveTxUtilization,
       "aiLCGtranActiveClockSlave": aiLCGtranActiveClockSlave,
       "aiLCGtranActiveCoolerStatus": aiLCGtranActiveCoolerStatus,
       "aiLCGtranActiveTemperature": aiLCGtranActiveTemperature,
       "aiLCGtranActiveRxPower": aiLCGtranActiveRxPower,
       "aiLCGtranActiveTxPower": aiLCGtranActiveTxPower,
       "aiLCGtranBackupTable": aiLCGtranBackupTable,
       "aiLCGtranBackupEntry": aiLCGtranBackupEntry,
       "aiLCGtranBackupIndex": aiLCGtranBackupIndex,
       "aiLCGtranBackupActiveIndex": aiLCGtranBackupActiveIndex,
       "aiLcGbicTable": aiLcGbicTable,
       "aiLCGbicEntry": aiLCGbicEntry,
       "aiLCGbicIndex": aiLCGbicIndex,
       "aiLCGbicConnectorType": aiLCGbicConnectorType,
       "aiLCGbicTxMode": aiLCGbicTxMode,
       "aiLCGbicRxUtilization": aiLCGbicRxUtilization,
       "aiLCGbicTxUtilization": aiLCGbicTxUtilization}
)
