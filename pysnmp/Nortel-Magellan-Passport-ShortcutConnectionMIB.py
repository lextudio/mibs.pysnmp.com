# SNMP MIB module (Nortel-Magellan-Passport-ShortcutConnectionMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ShortcutConnectionMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:21 2024
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

(Counter32,
 DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "HexString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vrIndex,
 vrPp,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vrIndex",
    "vrPp",
    "vrPpIndex")

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

_VrPpSc_ObjectIdentity = ObjectIdentity
vrPpSc = _VrPpSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16)
)
_VrPpScRowStatusTable_Object = MibTable
vrPpScRowStatusTable = _VrPpScRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 1)
)
if mibBuilder.loadTexts:
    vrPpScRowStatusTable.setStatus("mandatory")
_VrPpScRowStatusEntry_Object = MibTableRow
vrPpScRowStatusEntry = _VrPpScRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 1, 1)
)
vrPpScRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScIndex"),
)
if mibBuilder.loadTexts:
    vrPpScRowStatusEntry.setStatus("mandatory")
_VrPpScRowStatus_Type = RowStatus
_VrPpScRowStatus_Object = MibTableColumn
vrPpScRowStatus = _VrPpScRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 1, 1, 1),
    _VrPpScRowStatus_Type()
)
vrPpScRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScRowStatus.setStatus("mandatory")
_VrPpScComponentName_Type = DisplayString
_VrPpScComponentName_Object = MibTableColumn
vrPpScComponentName = _VrPpScComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 1, 1, 2),
    _VrPpScComponentName_Type()
)
vrPpScComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScComponentName.setStatus("mandatory")
_VrPpScStorageType_Type = StorageType
_VrPpScStorageType_Object = MibTableColumn
vrPpScStorageType = _VrPpScStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 1, 1, 4),
    _VrPpScStorageType_Type()
)
vrPpScStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScStorageType.setStatus("mandatory")


class _VrPpScIndex_Type(Integer32):
    """Custom type vrPpScIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_VrPpScIndex_Type.__name__ = "Integer32"
_VrPpScIndex_Object = MibTableColumn
vrPpScIndex = _VrPpScIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 1, 1, 10),
    _VrPpScIndex_Type()
)
vrPpScIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpScIndex.setStatus("mandatory")
_VrPpScAtmCon_ObjectIdentity = ObjectIdentity
vrPpScAtmCon = _VrPpScAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4)
)
_VrPpScAtmConRowStatusTable_Object = MibTable
vrPpScAtmConRowStatusTable = _VrPpScAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 1)
)
if mibBuilder.loadTexts:
    vrPpScAtmConRowStatusTable.setStatus("mandatory")
_VrPpScAtmConRowStatusEntry_Object = MibTableRow
vrPpScAtmConRowStatusEntry = _VrPpScAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 1, 1)
)
vrPpScAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScAtmConIndex"),
)
if mibBuilder.loadTexts:
    vrPpScAtmConRowStatusEntry.setStatus("mandatory")
_VrPpScAtmConRowStatus_Type = RowStatus
_VrPpScAtmConRowStatus_Object = MibTableColumn
vrPpScAtmConRowStatus = _VrPpScAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 1, 1, 1),
    _VrPpScAtmConRowStatus_Type()
)
vrPpScAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScAtmConRowStatus.setStatus("mandatory")
_VrPpScAtmConComponentName_Type = DisplayString
_VrPpScAtmConComponentName_Object = MibTableColumn
vrPpScAtmConComponentName = _VrPpScAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 1, 1, 2),
    _VrPpScAtmConComponentName_Type()
)
vrPpScAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScAtmConComponentName.setStatus("mandatory")
_VrPpScAtmConStorageType_Type = StorageType
_VrPpScAtmConStorageType_Object = MibTableColumn
vrPpScAtmConStorageType = _VrPpScAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 1, 1, 4),
    _VrPpScAtmConStorageType_Type()
)
vrPpScAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScAtmConStorageType.setStatus("mandatory")
_VrPpScAtmConIndex_Type = NonReplicated
_VrPpScAtmConIndex_Object = MibTableColumn
vrPpScAtmConIndex = _VrPpScAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 1, 1, 10),
    _VrPpScAtmConIndex_Type()
)
vrPpScAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpScAtmConIndex.setStatus("mandatory")
_VrPpScAtmConOperTable_Object = MibTable
vrPpScAtmConOperTable = _VrPpScAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 10)
)
if mibBuilder.loadTexts:
    vrPpScAtmConOperTable.setStatus("mandatory")
_VrPpScAtmConOperEntry_Object = MibTableRow
vrPpScAtmConOperEntry = _VrPpScAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 10, 1)
)
vrPpScAtmConOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScAtmConIndex"),
)
if mibBuilder.loadTexts:
    vrPpScAtmConOperEntry.setStatus("mandatory")
_VrPpScAtmConNextHop_Type = RowPointer
_VrPpScAtmConNextHop_Object = MibTableColumn
vrPpScAtmConNextHop = _VrPpScAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 4, 10, 1, 1),
    _VrPpScAtmConNextHop_Type()
)
vrPpScAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScAtmConNextHop.setStatus("mandatory")
_VrPpScOperTable_Object = MibTable
vrPpScOperTable = _VrPpScOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10)
)
if mibBuilder.loadTexts:
    vrPpScOperTable.setStatus("mandatory")
_VrPpScOperEntry_Object = MibTableRow
vrPpScOperEntry = _VrPpScOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10, 1)
)
vrPpScOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScIndex"),
)
if mibBuilder.loadTexts:
    vrPpScOperEntry.setStatus("mandatory")


class _VrPpScRemoteNbmaAddress_Type(HexString):
    """Custom type vrPpScRemoteNbmaAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VrPpScRemoteNbmaAddress_Type.__name__ = "HexString"
_VrPpScRemoteNbmaAddress_Object = MibTableColumn
vrPpScRemoteNbmaAddress = _VrPpScRemoteNbmaAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10, 1, 1),
    _VrPpScRemoteNbmaAddress_Type()
)
vrPpScRemoteNbmaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScRemoteNbmaAddress.setStatus("mandatory")


class _VrPpScAge_Type(Unsigned32):
    """Custom type vrPpScAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_VrPpScAge_Type.__name__ = "Unsigned32"
_VrPpScAge_Object = MibTableColumn
vrPpScAge = _VrPpScAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10, 1, 2),
    _VrPpScAge_Type()
)
vrPpScAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScAge.setStatus("mandatory")


class _VrPpScMtu_Type(Unsigned32):
    """Custom type vrPpScMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrPpScMtu_Type.__name__ = "Unsigned32"
_VrPpScMtu_Object = MibTableColumn
vrPpScMtu = _VrPpScMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10, 1, 3),
    _VrPpScMtu_Type()
)
vrPpScMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScMtu.setStatus("mandatory")


class _VrPpScConnSource_Type(Integer32):
    """Custom type vrPpScConnSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_VrPpScConnSource_Type.__name__ = "Integer32"
_VrPpScConnSource_Object = MibTableColumn
vrPpScConnSource = _VrPpScConnSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10, 1, 4),
    _VrPpScConnSource_Type()
)
vrPpScConnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScConnSource.setStatus("mandatory")


class _VrPpScType_Type(Integer32):
    """Custom type vrPpScType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_VrPpScType_Type.__name__ = "Integer32"
_VrPpScType_Object = MibTableColumn
vrPpScType = _VrPpScType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 10, 1, 5),
    _VrPpScType_Type()
)
vrPpScType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScType.setStatus("mandatory")
_VrPpScStatsTable_Object = MibTable
vrPpScStatsTable = _VrPpScStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 11)
)
if mibBuilder.loadTexts:
    vrPpScStatsTable.setStatus("mandatory")
_VrPpScStatsEntry_Object = MibTableRow
vrPpScStatsEntry = _VrPpScStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 11, 1)
)
vrPpScStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-ShortcutConnectionMIB", "vrPpScIndex"),
)
if mibBuilder.loadTexts:
    vrPpScStatsEntry.setStatus("mandatory")
_VrPpScTxFrames_Type = Counter32
_VrPpScTxFrames_Object = MibTableColumn
vrPpScTxFrames = _VrPpScTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 11, 1, 1),
    _VrPpScTxFrames_Type()
)
vrPpScTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScTxFrames.setStatus("mandatory")
_VrPpScRxFrames_Type = Counter32
_VrPpScRxFrames_Object = MibTableColumn
vrPpScRxFrames = _VrPpScRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 16, 11, 1, 2),
    _VrPpScRxFrames_Type()
)
vrPpScRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpScRxFrames.setStatus("mandatory")
_ShortcutConnectionMIB_ObjectIdentity = ObjectIdentity
shortcutConnectionMIB = _ShortcutConnectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78)
)
_ShortcutConnectionGroup_ObjectIdentity = ObjectIdentity
shortcutConnectionGroup = _ShortcutConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 1)
)
_ShortcutConnectionGroupBE_ObjectIdentity = ObjectIdentity
shortcutConnectionGroupBE = _ShortcutConnectionGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 1, 5)
)
_ShortcutConnectionGroupBE01_ObjectIdentity = ObjectIdentity
shortcutConnectionGroupBE01 = _ShortcutConnectionGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 1, 5, 2)
)
_ShortcutConnectionGroupBE01A_ObjectIdentity = ObjectIdentity
shortcutConnectionGroupBE01A = _ShortcutConnectionGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 1, 5, 2, 2)
)
_ShortcutConnectionCapabilities_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilities = _ShortcutConnectionCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 3)
)
_ShortcutConnectionCapabilitiesBE_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilitiesBE = _ShortcutConnectionCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 3, 5)
)
_ShortcutConnectionCapabilitiesBE01_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilitiesBE01 = _ShortcutConnectionCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 3, 5, 2)
)
_ShortcutConnectionCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilitiesBE01A = _ShortcutConnectionCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 78, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ShortcutConnectionMIB",
    **{"vrPpSc": vrPpSc,
       "vrPpScRowStatusTable": vrPpScRowStatusTable,
       "vrPpScRowStatusEntry": vrPpScRowStatusEntry,
       "vrPpScRowStatus": vrPpScRowStatus,
       "vrPpScComponentName": vrPpScComponentName,
       "vrPpScStorageType": vrPpScStorageType,
       "vrPpScIndex": vrPpScIndex,
       "vrPpScAtmCon": vrPpScAtmCon,
       "vrPpScAtmConRowStatusTable": vrPpScAtmConRowStatusTable,
       "vrPpScAtmConRowStatusEntry": vrPpScAtmConRowStatusEntry,
       "vrPpScAtmConRowStatus": vrPpScAtmConRowStatus,
       "vrPpScAtmConComponentName": vrPpScAtmConComponentName,
       "vrPpScAtmConStorageType": vrPpScAtmConStorageType,
       "vrPpScAtmConIndex": vrPpScAtmConIndex,
       "vrPpScAtmConOperTable": vrPpScAtmConOperTable,
       "vrPpScAtmConOperEntry": vrPpScAtmConOperEntry,
       "vrPpScAtmConNextHop": vrPpScAtmConNextHop,
       "vrPpScOperTable": vrPpScOperTable,
       "vrPpScOperEntry": vrPpScOperEntry,
       "vrPpScRemoteNbmaAddress": vrPpScRemoteNbmaAddress,
       "vrPpScAge": vrPpScAge,
       "vrPpScMtu": vrPpScMtu,
       "vrPpScConnSource": vrPpScConnSource,
       "vrPpScType": vrPpScType,
       "vrPpScStatsTable": vrPpScStatsTable,
       "vrPpScStatsEntry": vrPpScStatsEntry,
       "vrPpScTxFrames": vrPpScTxFrames,
       "vrPpScRxFrames": vrPpScRxFrames,
       "shortcutConnectionMIB": shortcutConnectionMIB,
       "shortcutConnectionGroup": shortcutConnectionGroup,
       "shortcutConnectionGroupBE": shortcutConnectionGroupBE,
       "shortcutConnectionGroupBE01": shortcutConnectionGroupBE01,
       "shortcutConnectionGroupBE01A": shortcutConnectionGroupBE01A,
       "shortcutConnectionCapabilities": shortcutConnectionCapabilities,
       "shortcutConnectionCapabilitiesBE": shortcutConnectionCapabilitiesBE,
       "shortcutConnectionCapabilitiesBE01": shortcutConnectionCapabilitiesBE01,
       "shortcutConnectionCapabilitiesBE01A": shortcutConnectionCapabilitiesBE01A}
)
