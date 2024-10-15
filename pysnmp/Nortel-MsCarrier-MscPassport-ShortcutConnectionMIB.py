# SNMP MIB module (Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:00 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVrIndex,
 mscVrPp,
 mscVrPpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVrIndex",
    "mscVrPp",
    "mscVrPpIndex")

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

_MscVrPpSc_ObjectIdentity = ObjectIdentity
mscVrPpSc = _MscVrPpSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16)
)
_MscVrPpScRowStatusTable_Object = MibTable
mscVrPpScRowStatusTable = _MscVrPpScRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1)
)
if mibBuilder.loadTexts:
    mscVrPpScRowStatusTable.setStatus("mandatory")
_MscVrPpScRowStatusEntry_Object = MibTableRow
mscVrPpScRowStatusEntry = _MscVrPpScRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1)
)
mscVrPpScRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpScRowStatusEntry.setStatus("mandatory")
_MscVrPpScRowStatus_Type = RowStatus
_MscVrPpScRowStatus_Object = MibTableColumn
mscVrPpScRowStatus = _MscVrPpScRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 1),
    _MscVrPpScRowStatus_Type()
)
mscVrPpScRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScRowStatus.setStatus("mandatory")
_MscVrPpScComponentName_Type = DisplayString
_MscVrPpScComponentName_Object = MibTableColumn
mscVrPpScComponentName = _MscVrPpScComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 2),
    _MscVrPpScComponentName_Type()
)
mscVrPpScComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScComponentName.setStatus("mandatory")
_MscVrPpScStorageType_Type = StorageType
_MscVrPpScStorageType_Object = MibTableColumn
mscVrPpScStorageType = _MscVrPpScStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 4),
    _MscVrPpScStorageType_Type()
)
mscVrPpScStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScStorageType.setStatus("mandatory")


class _MscVrPpScIndex_Type(Integer32):
    """Custom type mscVrPpScIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscVrPpScIndex_Type.__name__ = "Integer32"
_MscVrPpScIndex_Object = MibTableColumn
mscVrPpScIndex = _MscVrPpScIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 1, 1, 10),
    _MscVrPpScIndex_Type()
)
mscVrPpScIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpScIndex.setStatus("mandatory")
_MscVrPpScAtmCon_ObjectIdentity = ObjectIdentity
mscVrPpScAtmCon = _MscVrPpScAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4)
)
_MscVrPpScAtmConRowStatusTable_Object = MibTable
mscVrPpScAtmConRowStatusTable = _MscVrPpScAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrPpScAtmConRowStatusTable.setStatus("mandatory")
_MscVrPpScAtmConRowStatusEntry_Object = MibTableRow
mscVrPpScAtmConRowStatusEntry = _MscVrPpScAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1)
)
mscVrPpScAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpScAtmConRowStatusEntry.setStatus("mandatory")
_MscVrPpScAtmConRowStatus_Type = RowStatus
_MscVrPpScAtmConRowStatus_Object = MibTableColumn
mscVrPpScAtmConRowStatus = _MscVrPpScAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 1),
    _MscVrPpScAtmConRowStatus_Type()
)
mscVrPpScAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScAtmConRowStatus.setStatus("mandatory")
_MscVrPpScAtmConComponentName_Type = DisplayString
_MscVrPpScAtmConComponentName_Object = MibTableColumn
mscVrPpScAtmConComponentName = _MscVrPpScAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 2),
    _MscVrPpScAtmConComponentName_Type()
)
mscVrPpScAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScAtmConComponentName.setStatus("mandatory")
_MscVrPpScAtmConStorageType_Type = StorageType
_MscVrPpScAtmConStorageType_Object = MibTableColumn
mscVrPpScAtmConStorageType = _MscVrPpScAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 4),
    _MscVrPpScAtmConStorageType_Type()
)
mscVrPpScAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScAtmConStorageType.setStatus("mandatory")
_MscVrPpScAtmConIndex_Type = NonReplicated
_MscVrPpScAtmConIndex_Object = MibTableColumn
mscVrPpScAtmConIndex = _MscVrPpScAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 1, 1, 10),
    _MscVrPpScAtmConIndex_Type()
)
mscVrPpScAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpScAtmConIndex.setStatus("mandatory")
_MscVrPpScAtmConOperTable_Object = MibTable
mscVrPpScAtmConOperTable = _MscVrPpScAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrPpScAtmConOperTable.setStatus("mandatory")
_MscVrPpScAtmConOperEntry_Object = MibTableRow
mscVrPpScAtmConOperEntry = _MscVrPpScAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 10, 1)
)
mscVrPpScAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpScAtmConOperEntry.setStatus("mandatory")
_MscVrPpScAtmConNextHop_Type = RowPointer
_MscVrPpScAtmConNextHop_Object = MibTableColumn
mscVrPpScAtmConNextHop = _MscVrPpScAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 4, 10, 1, 1),
    _MscVrPpScAtmConNextHop_Type()
)
mscVrPpScAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScAtmConNextHop.setStatus("mandatory")
_MscVrPpScOperTable_Object = MibTable
mscVrPpScOperTable = _MscVrPpScOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10)
)
if mibBuilder.loadTexts:
    mscVrPpScOperTable.setStatus("mandatory")
_MscVrPpScOperEntry_Object = MibTableRow
mscVrPpScOperEntry = _MscVrPpScOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1)
)
mscVrPpScOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpScOperEntry.setStatus("mandatory")


class _MscVrPpScRemoteNbmaAddress_Type(HexString):
    """Custom type mscVrPpScRemoteNbmaAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscVrPpScRemoteNbmaAddress_Type.__name__ = "HexString"
_MscVrPpScRemoteNbmaAddress_Object = MibTableColumn
mscVrPpScRemoteNbmaAddress = _MscVrPpScRemoteNbmaAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 1),
    _MscVrPpScRemoteNbmaAddress_Type()
)
mscVrPpScRemoteNbmaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScRemoteNbmaAddress.setStatus("mandatory")


class _MscVrPpScAge_Type(Unsigned32):
    """Custom type mscVrPpScAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscVrPpScAge_Type.__name__ = "Unsigned32"
_MscVrPpScAge_Object = MibTableColumn
mscVrPpScAge = _MscVrPpScAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 2),
    _MscVrPpScAge_Type()
)
mscVrPpScAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScAge.setStatus("mandatory")


class _MscVrPpScMtu_Type(Unsigned32):
    """Custom type mscVrPpScMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrPpScMtu_Type.__name__ = "Unsigned32"
_MscVrPpScMtu_Object = MibTableColumn
mscVrPpScMtu = _MscVrPpScMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 3),
    _MscVrPpScMtu_Type()
)
mscVrPpScMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScMtu.setStatus("mandatory")


class _MscVrPpScConnSource_Type(Integer32):
    """Custom type mscVrPpScConnSource based on Integer32"""
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


_MscVrPpScConnSource_Type.__name__ = "Integer32"
_MscVrPpScConnSource_Object = MibTableColumn
mscVrPpScConnSource = _MscVrPpScConnSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 4),
    _MscVrPpScConnSource_Type()
)
mscVrPpScConnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScConnSource.setStatus("mandatory")


class _MscVrPpScType_Type(Integer32):
    """Custom type mscVrPpScType based on Integer32"""
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


_MscVrPpScType_Type.__name__ = "Integer32"
_MscVrPpScType_Object = MibTableColumn
mscVrPpScType = _MscVrPpScType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 10, 1, 5),
    _MscVrPpScType_Type()
)
mscVrPpScType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScType.setStatus("mandatory")
_MscVrPpScStatsTable_Object = MibTable
mscVrPpScStatsTable = _MscVrPpScStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11)
)
if mibBuilder.loadTexts:
    mscVrPpScStatsTable.setStatus("mandatory")
_MscVrPpScStatsEntry_Object = MibTableRow
mscVrPpScStatsEntry = _MscVrPpScStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11, 1)
)
mscVrPpScStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB", "mscVrPpScIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpScStatsEntry.setStatus("mandatory")
_MscVrPpScTxFrames_Type = Counter32
_MscVrPpScTxFrames_Object = MibTableColumn
mscVrPpScTxFrames = _MscVrPpScTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11, 1, 1),
    _MscVrPpScTxFrames_Type()
)
mscVrPpScTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScTxFrames.setStatus("mandatory")
_MscVrPpScRxFrames_Type = Counter32
_MscVrPpScRxFrames_Object = MibTableColumn
mscVrPpScRxFrames = _MscVrPpScRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 16, 11, 1, 2),
    _MscVrPpScRxFrames_Type()
)
mscVrPpScRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpScRxFrames.setStatus("mandatory")
_ShortcutConnectionMIB_ObjectIdentity = ObjectIdentity
shortcutConnectionMIB = _ShortcutConnectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78)
)
_ShortcutConnectionGroup_ObjectIdentity = ObjectIdentity
shortcutConnectionGroup = _ShortcutConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1)
)
_ShortcutConnectionGroupCA_ObjectIdentity = ObjectIdentity
shortcutConnectionGroupCA = _ShortcutConnectionGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1, 1)
)
_ShortcutConnectionGroupCA02_ObjectIdentity = ObjectIdentity
shortcutConnectionGroupCA02 = _ShortcutConnectionGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1, 1, 3)
)
_ShortcutConnectionGroupCA02A_ObjectIdentity = ObjectIdentity
shortcutConnectionGroupCA02A = _ShortcutConnectionGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 1, 1, 3, 2)
)
_ShortcutConnectionCapabilities_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilities = _ShortcutConnectionCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3)
)
_ShortcutConnectionCapabilitiesCA_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilitiesCA = _ShortcutConnectionCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3, 1)
)
_ShortcutConnectionCapabilitiesCA02_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilitiesCA02 = _ShortcutConnectionCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3, 1, 3)
)
_ShortcutConnectionCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
shortcutConnectionCapabilitiesCA02A = _ShortcutConnectionCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 78, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ShortcutConnectionMIB",
    **{"mscVrPpSc": mscVrPpSc,
       "mscVrPpScRowStatusTable": mscVrPpScRowStatusTable,
       "mscVrPpScRowStatusEntry": mscVrPpScRowStatusEntry,
       "mscVrPpScRowStatus": mscVrPpScRowStatus,
       "mscVrPpScComponentName": mscVrPpScComponentName,
       "mscVrPpScStorageType": mscVrPpScStorageType,
       "mscVrPpScIndex": mscVrPpScIndex,
       "mscVrPpScAtmCon": mscVrPpScAtmCon,
       "mscVrPpScAtmConRowStatusTable": mscVrPpScAtmConRowStatusTable,
       "mscVrPpScAtmConRowStatusEntry": mscVrPpScAtmConRowStatusEntry,
       "mscVrPpScAtmConRowStatus": mscVrPpScAtmConRowStatus,
       "mscVrPpScAtmConComponentName": mscVrPpScAtmConComponentName,
       "mscVrPpScAtmConStorageType": mscVrPpScAtmConStorageType,
       "mscVrPpScAtmConIndex": mscVrPpScAtmConIndex,
       "mscVrPpScAtmConOperTable": mscVrPpScAtmConOperTable,
       "mscVrPpScAtmConOperEntry": mscVrPpScAtmConOperEntry,
       "mscVrPpScAtmConNextHop": mscVrPpScAtmConNextHop,
       "mscVrPpScOperTable": mscVrPpScOperTable,
       "mscVrPpScOperEntry": mscVrPpScOperEntry,
       "mscVrPpScRemoteNbmaAddress": mscVrPpScRemoteNbmaAddress,
       "mscVrPpScAge": mscVrPpScAge,
       "mscVrPpScMtu": mscVrPpScMtu,
       "mscVrPpScConnSource": mscVrPpScConnSource,
       "mscVrPpScType": mscVrPpScType,
       "mscVrPpScStatsTable": mscVrPpScStatsTable,
       "mscVrPpScStatsEntry": mscVrPpScStatsEntry,
       "mscVrPpScTxFrames": mscVrPpScTxFrames,
       "mscVrPpScRxFrames": mscVrPpScRxFrames,
       "shortcutConnectionMIB": shortcutConnectionMIB,
       "shortcutConnectionGroup": shortcutConnectionGroup,
       "shortcutConnectionGroupCA": shortcutConnectionGroupCA,
       "shortcutConnectionGroupCA02": shortcutConnectionGroupCA02,
       "shortcutConnectionGroupCA02A": shortcutConnectionGroupCA02A,
       "shortcutConnectionCapabilities": shortcutConnectionCapabilities,
       "shortcutConnectionCapabilitiesCA": shortcutConnectionCapabilitiesCA,
       "shortcutConnectionCapabilitiesCA02": shortcutConnectionCapabilitiesCA02,
       "shortcutConnectionCapabilitiesCA02A": shortcutConnectionCapabilitiesCA02A}
)
