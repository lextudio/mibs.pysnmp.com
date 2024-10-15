# SNMP MIB module (Nortel-MsCarrier-MscPassport-SnaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-SnaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:01 2024
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
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DashedHexString,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "DashedHexString",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex,
 mscVrPp,
 mscVrPpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
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

_MscVrPpSnaPort_ObjectIdentity = ObjectIdentity
mscVrPpSnaPort = _MscVrPpSnaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15)
)
_MscVrPpSnaPortRowStatusTable_Object = MibTable
mscVrPpSnaPortRowStatusTable = _MscVrPpSnaPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortRowStatusTable.setStatus("mandatory")
_MscVrPpSnaPortRowStatusEntry_Object = MibTableRow
mscVrPpSnaPortRowStatusEntry = _MscVrPpSnaPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 1, 1)
)
mscVrPpSnaPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortRowStatusEntry.setStatus("mandatory")
_MscVrPpSnaPortRowStatus_Type = RowStatus
_MscVrPpSnaPortRowStatus_Object = MibTableColumn
mscVrPpSnaPortRowStatus = _MscVrPpSnaPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 1, 1, 1),
    _MscVrPpSnaPortRowStatus_Type()
)
mscVrPpSnaPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSnaPortRowStatus.setStatus("mandatory")
_MscVrPpSnaPortComponentName_Type = DisplayString
_MscVrPpSnaPortComponentName_Object = MibTableColumn
mscVrPpSnaPortComponentName = _MscVrPpSnaPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 1, 1, 2),
    _MscVrPpSnaPortComponentName_Type()
)
mscVrPpSnaPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortComponentName.setStatus("mandatory")
_MscVrPpSnaPortStorageType_Type = StorageType
_MscVrPpSnaPortStorageType_Object = MibTableColumn
mscVrPpSnaPortStorageType = _MscVrPpSnaPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 1, 1, 4),
    _MscVrPpSnaPortStorageType_Type()
)
mscVrPpSnaPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortStorageType.setStatus("mandatory")
_MscVrPpSnaPortIndex_Type = NonReplicated
_MscVrPpSnaPortIndex_Object = MibTableColumn
mscVrPpSnaPortIndex = _MscVrPpSnaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 1, 1, 10),
    _MscVrPpSnaPortIndex_Type()
)
mscVrPpSnaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSnaPortIndex.setStatus("mandatory")
_MscVrPpSnaPortCircuit_ObjectIdentity = ObjectIdentity
mscVrPpSnaPortCircuit = _MscVrPpSnaPortCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2)
)
_MscVrPpSnaPortCircuitRowStatusTable_Object = MibTable
mscVrPpSnaPortCircuitRowStatusTable = _MscVrPpSnaPortCircuitRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitRowStatusTable.setStatus("mandatory")
_MscVrPpSnaPortCircuitRowStatusEntry_Object = MibTableRow
mscVrPpSnaPortCircuitRowStatusEntry = _MscVrPpSnaPortCircuitRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1)
)
mscVrPpSnaPortCircuitRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS1MacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS1SapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS2MacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS2SapIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitRowStatusEntry.setStatus("mandatory")
_MscVrPpSnaPortCircuitRowStatus_Type = RowStatus
_MscVrPpSnaPortCircuitRowStatus_Object = MibTableColumn
mscVrPpSnaPortCircuitRowStatus = _MscVrPpSnaPortCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 1),
    _MscVrPpSnaPortCircuitRowStatus_Type()
)
mscVrPpSnaPortCircuitRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitRowStatus.setStatus("mandatory")
_MscVrPpSnaPortCircuitComponentName_Type = DisplayString
_MscVrPpSnaPortCircuitComponentName_Object = MibTableColumn
mscVrPpSnaPortCircuitComponentName = _MscVrPpSnaPortCircuitComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 2),
    _MscVrPpSnaPortCircuitComponentName_Type()
)
mscVrPpSnaPortCircuitComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitComponentName.setStatus("mandatory")
_MscVrPpSnaPortCircuitStorageType_Type = StorageType
_MscVrPpSnaPortCircuitStorageType_Object = MibTableColumn
mscVrPpSnaPortCircuitStorageType = _MscVrPpSnaPortCircuitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 4),
    _MscVrPpSnaPortCircuitStorageType_Type()
)
mscVrPpSnaPortCircuitStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitStorageType.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS1MacIndex_Type(DashedHexString):
    """Custom type mscVrPpSnaPortCircuitS1MacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrPpSnaPortCircuitS1MacIndex_Type.__name__ = "DashedHexString"
_MscVrPpSnaPortCircuitS1MacIndex_Object = MibTableColumn
mscVrPpSnaPortCircuitS1MacIndex = _MscVrPpSnaPortCircuitS1MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 10),
    _MscVrPpSnaPortCircuitS1MacIndex_Type()
)
mscVrPpSnaPortCircuitS1MacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS1MacIndex.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS1SapIndex_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitS1SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_MscVrPpSnaPortCircuitS1SapIndex_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitS1SapIndex_Object = MibTableColumn
mscVrPpSnaPortCircuitS1SapIndex = _MscVrPpSnaPortCircuitS1SapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 11),
    _MscVrPpSnaPortCircuitS1SapIndex_Type()
)
mscVrPpSnaPortCircuitS1SapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS1SapIndex.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS2MacIndex_Type(DashedHexString):
    """Custom type mscVrPpSnaPortCircuitS2MacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrPpSnaPortCircuitS2MacIndex_Type.__name__ = "DashedHexString"
_MscVrPpSnaPortCircuitS2MacIndex_Object = MibTableColumn
mscVrPpSnaPortCircuitS2MacIndex = _MscVrPpSnaPortCircuitS2MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 12),
    _MscVrPpSnaPortCircuitS2MacIndex_Type()
)
mscVrPpSnaPortCircuitS2MacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS2MacIndex.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS2SapIndex_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitS2SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_MscVrPpSnaPortCircuitS2SapIndex_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitS2SapIndex_Object = MibTableColumn
mscVrPpSnaPortCircuitS2SapIndex = _MscVrPpSnaPortCircuitS2SapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 1, 1, 13),
    _MscVrPpSnaPortCircuitS2SapIndex_Type()
)
mscVrPpSnaPortCircuitS2SapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS2SapIndex.setStatus("mandatory")
_MscVrPpSnaPortCircuitOperTable_Object = MibTable
mscVrPpSnaPortCircuitOperTable = _MscVrPpSnaPortCircuitOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitOperTable.setStatus("mandatory")
_MscVrPpSnaPortCircuitOperEntry_Object = MibTableRow
mscVrPpSnaPortCircuitOperEntry = _MscVrPpSnaPortCircuitOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1)
)
mscVrPpSnaPortCircuitOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS1MacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS1SapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS2MacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortCircuitS2SapIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitOperEntry.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS1DlcType_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitS1DlcType based on Integer32"""
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
        *(("llc", 3),
          ("na", 2),
          ("other", 1),
          ("qllc", 5),
          ("sdlc", 4))
    )


_MscVrPpSnaPortCircuitS1DlcType_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitS1DlcType_Object = MibTableColumn
mscVrPpSnaPortCircuitS1DlcType = _MscVrPpSnaPortCircuitS1DlcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 2),
    _MscVrPpSnaPortCircuitS1DlcType_Type()
)
mscVrPpSnaPortCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS1DlcType.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS1RouteInfo_Type(HexString):
    """Custom type mscVrPpSnaPortCircuitS1RouteInfo based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MscVrPpSnaPortCircuitS1RouteInfo_Type.__name__ = "HexString"
_MscVrPpSnaPortCircuitS1RouteInfo_Object = MibTableColumn
mscVrPpSnaPortCircuitS1RouteInfo = _MscVrPpSnaPortCircuitS1RouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 3),
    _MscVrPpSnaPortCircuitS1RouteInfo_Type()
)
mscVrPpSnaPortCircuitS1RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS1RouteInfo.setStatus("mandatory")


class _MscVrPpSnaPortCircuitS2Location_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitS2Location based on Integer32"""
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
        *(("internal", 2),
          ("local", 4),
          ("other", 1),
          ("remote", 3))
    )


_MscVrPpSnaPortCircuitS2Location_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitS2Location_Object = MibTableColumn
mscVrPpSnaPortCircuitS2Location = _MscVrPpSnaPortCircuitS2Location_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 6),
    _MscVrPpSnaPortCircuitS2Location_Type()
)
mscVrPpSnaPortCircuitS2Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitS2Location.setStatus("mandatory")


class _MscVrPpSnaPortCircuitOrigin_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 0))
    )


_MscVrPpSnaPortCircuitOrigin_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitOrigin_Object = MibTableColumn
mscVrPpSnaPortCircuitOrigin = _MscVrPpSnaPortCircuitOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 10),
    _MscVrPpSnaPortCircuitOrigin_Type()
)
mscVrPpSnaPortCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitOrigin.setStatus("mandatory")


class _MscVrPpSnaPortCircuitState_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("circuitEstablished", 5),
          ("circuitPending", 4),
          ("circuitRestart", 12),
          ("circuitStart", 2),
          ("connectPending", 6),
          ("connected", 8),
          ("contactPending", 7),
          ("disconnectPending", 9),
          ("disconnected", 1),
          ("haltPending", 10),
          ("haltPendingNoack", 11),
          ("resolvePending", 3),
          ("restartPending", 13))
    )


_MscVrPpSnaPortCircuitState_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitState_Object = MibTableColumn
mscVrPpSnaPortCircuitState = _MscVrPpSnaPortCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 13),
    _MscVrPpSnaPortCircuitState_Type()
)
mscVrPpSnaPortCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitState.setStatus("mandatory")


class _MscVrPpSnaPortCircuitPriority_Type(Integer32):
    """Custom type mscVrPpSnaPortCircuitPriority based on Integer32"""
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
        *(("high", 4),
          ("highest", 5),
          ("low", 2),
          ("medium", 3),
          ("unsupported", 1))
    )


_MscVrPpSnaPortCircuitPriority_Type.__name__ = "Integer32"
_MscVrPpSnaPortCircuitPriority_Object = MibTableColumn
mscVrPpSnaPortCircuitPriority = _MscVrPpSnaPortCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 14),
    _MscVrPpSnaPortCircuitPriority_Type()
)
mscVrPpSnaPortCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitPriority.setStatus("mandatory")
_MscVrPpSnaPortCircuitVcId_Type = RowPointer
_MscVrPpSnaPortCircuitVcId_Object = MibTableColumn
mscVrPpSnaPortCircuitVcId = _MscVrPpSnaPortCircuitVcId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 2, 100, 1, 26),
    _MscVrPpSnaPortCircuitVcId_Type()
)
mscVrPpSnaPortCircuitVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortCircuitVcId.setStatus("mandatory")
_MscVrPpSnaPortAdminControlTable_Object = MibTable
mscVrPpSnaPortAdminControlTable = _MscVrPpSnaPortAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 100)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortAdminControlTable.setStatus("mandatory")
_MscVrPpSnaPortAdminControlEntry_Object = MibTableRow
mscVrPpSnaPortAdminControlEntry = _MscVrPpSnaPortAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 100, 1)
)
mscVrPpSnaPortAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortAdminControlEntry.setStatus("mandatory")


class _MscVrPpSnaPortSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpSnaPortSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpSnaPortSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSnaPortSnmpAdminStatus_Object = MibTableColumn
mscVrPpSnaPortSnmpAdminStatus = _MscVrPpSnaPortSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 100, 1, 1),
    _MscVrPpSnaPortSnmpAdminStatus_Type()
)
mscVrPpSnaPortSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSnaPortSnmpAdminStatus.setStatus("mandatory")
_MscVrPpSnaPortProvTable_Object = MibTable
mscVrPpSnaPortProvTable = _MscVrPpSnaPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 101)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortProvTable.setStatus("mandatory")
_MscVrPpSnaPortProvEntry_Object = MibTableRow
mscVrPpSnaPortProvEntry = _MscVrPpSnaPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 101, 1)
)
mscVrPpSnaPortProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortProvEntry.setStatus("mandatory")


class _MscVrPpSnaPortVirtualSegmentLFSize_Type(Unsigned32):
    """Custom type mscVrPpSnaPortVirtualSegmentLFSize based on Unsigned32"""
    defaultValue = 2345

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 516),
        ValueRangeConstraint(635, 635),
        ValueRangeConstraint(754, 754),
        ValueRangeConstraint(873, 873),
        ValueRangeConstraint(993, 993),
        ValueRangeConstraint(1112, 1112),
        ValueRangeConstraint(1231, 1231),
        ValueRangeConstraint(1350, 1350),
        ValueRangeConstraint(1470, 1470),
        ValueRangeConstraint(1542, 1542),
        ValueRangeConstraint(1615, 1615),
        ValueRangeConstraint(1688, 1688),
        ValueRangeConstraint(1761, 1761),
        ValueRangeConstraint(1833, 1833),
        ValueRangeConstraint(1906, 1906),
        ValueRangeConstraint(1979, 1979),
        ValueRangeConstraint(2052, 2052),
        ValueRangeConstraint(2345, 2345),
        ValueRangeConstraint(5331, 5331),
        ValueRangeConstraint(5798, 5798),
        ValueRangeConstraint(6264, 6264),
        ValueRangeConstraint(6730, 6730),
        ValueRangeConstraint(7197, 7197),
        ValueRangeConstraint(7663, 7663),
        ValueRangeConstraint(8130, 8130),
        ValueRangeConstraint(8539, 8539),
        ValueRangeConstraint(8949, 8949),
        ValueRangeConstraint(9358, 9358),
        ValueRangeConstraint(9768, 9768),
        ValueRangeConstraint(10178, 10178),
        ValueRangeConstraint(10587, 10587),
        ValueRangeConstraint(10997, 10997),
        ValueRangeConstraint(11407, 11407),
        ValueRangeConstraint(12199, 12199),
        ValueRangeConstraint(12992, 12992),
        ValueRangeConstraint(13785, 13785),
        ValueRangeConstraint(14578, 14578),
        ValueRangeConstraint(15370, 15370),
        ValueRangeConstraint(16163, 16163),
        ValueRangeConstraint(16956, 16956),
        ValueRangeConstraint(17749, 17749),
        ValueRangeConstraint(20730, 20730),
        ValueRangeConstraint(23711, 23711),
        ValueRangeConstraint(26693, 26693),
        ValueRangeConstraint(29674, 29674),
        ValueRangeConstraint(32655, 32655),
        ValueRangeConstraint(35637, 35637),
        ValueRangeConstraint(38618, 38618),
        ValueRangeConstraint(41600, 41600),
        ValueRangeConstraint(44591, 44591),
        ValueRangeConstraint(47583, 47583),
        ValueRangeConstraint(50575, 50575),
        ValueRangeConstraint(53567, 53567),
        ValueRangeConstraint(56559, 56559),
        ValueRangeConstraint(59551, 59551),
        ValueRangeConstraint(65535, 65535),
    )


_MscVrPpSnaPortVirtualSegmentLFSize_Type.__name__ = "Unsigned32"
_MscVrPpSnaPortVirtualSegmentLFSize_Object = MibTableColumn
mscVrPpSnaPortVirtualSegmentLFSize = _MscVrPpSnaPortVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 101, 1, 1),
    _MscVrPpSnaPortVirtualSegmentLFSize_Type()
)
mscVrPpSnaPortVirtualSegmentLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSnaPortVirtualSegmentLFSize.setStatus("mandatory")
_MscVrPpSnaPortStateTable_Object = MibTable
mscVrPpSnaPortStateTable = _MscVrPpSnaPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 103)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortStateTable.setStatus("mandatory")
_MscVrPpSnaPortStateEntry_Object = MibTableRow
mscVrPpSnaPortStateEntry = _MscVrPpSnaPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 103, 1)
)
mscVrPpSnaPortStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortStateEntry.setStatus("mandatory")


class _MscVrPpSnaPortAdminState_Type(Integer32):
    """Custom type mscVrPpSnaPortAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrPpSnaPortAdminState_Type.__name__ = "Integer32"
_MscVrPpSnaPortAdminState_Object = MibTableColumn
mscVrPpSnaPortAdminState = _MscVrPpSnaPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 103, 1, 1),
    _MscVrPpSnaPortAdminState_Type()
)
mscVrPpSnaPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortAdminState.setStatus("mandatory")


class _MscVrPpSnaPortOperationalState_Type(Integer32):
    """Custom type mscVrPpSnaPortOperationalState based on Integer32"""
    defaultValue = 0

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


_MscVrPpSnaPortOperationalState_Type.__name__ = "Integer32"
_MscVrPpSnaPortOperationalState_Object = MibTableColumn
mscVrPpSnaPortOperationalState = _MscVrPpSnaPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 103, 1, 2),
    _MscVrPpSnaPortOperationalState_Type()
)
mscVrPpSnaPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortOperationalState.setStatus("mandatory")


class _MscVrPpSnaPortUsageState_Type(Integer32):
    """Custom type mscVrPpSnaPortUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrPpSnaPortUsageState_Type.__name__ = "Integer32"
_MscVrPpSnaPortUsageState_Object = MibTableColumn
mscVrPpSnaPortUsageState = _MscVrPpSnaPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 103, 1, 3),
    _MscVrPpSnaPortUsageState_Type()
)
mscVrPpSnaPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortUsageState.setStatus("mandatory")
_MscVrPpSnaPortOperStatusTable_Object = MibTable
mscVrPpSnaPortOperStatusTable = _MscVrPpSnaPortOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 104)
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortOperStatusTable.setStatus("mandatory")
_MscVrPpSnaPortOperStatusEntry_Object = MibTableRow
mscVrPpSnaPortOperStatusEntry = _MscVrPpSnaPortOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 104, 1)
)
mscVrPpSnaPortOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpSnaPortOperStatusEntry.setStatus("mandatory")


class _MscVrPpSnaPortSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSnaPortSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpSnaPortSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSnaPortSnmpOperStatus_Object = MibTableColumn
mscVrPpSnaPortSnmpOperStatus = _MscVrPpSnaPortSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 15, 104, 1, 1),
    _MscVrPpSnaPortSnmpOperStatus_Type()
)
mscVrPpSnaPortSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnaPortSnmpOperStatus.setStatus("mandatory")
_MscVrSna_ObjectIdentity = ObjectIdentity
mscVrSna = _MscVrSna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14)
)
_MscVrSnaRowStatusTable_Object = MibTable
mscVrSnaRowStatusTable = _MscVrSnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 1)
)
if mibBuilder.loadTexts:
    mscVrSnaRowStatusTable.setStatus("mandatory")
_MscVrSnaRowStatusEntry_Object = MibTableRow
mscVrSnaRowStatusEntry = _MscVrSnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 1, 1)
)
mscVrSnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaRowStatusEntry.setStatus("mandatory")
_MscVrSnaRowStatus_Type = RowStatus
_MscVrSnaRowStatus_Object = MibTableColumn
mscVrSnaRowStatus = _MscVrSnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 1, 1, 1),
    _MscVrSnaRowStatus_Type()
)
mscVrSnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnaRowStatus.setStatus("mandatory")
_MscVrSnaComponentName_Type = DisplayString
_MscVrSnaComponentName_Object = MibTableColumn
mscVrSnaComponentName = _MscVrSnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 1, 1, 2),
    _MscVrSnaComponentName_Type()
)
mscVrSnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaComponentName.setStatus("mandatory")
_MscVrSnaStorageType_Type = StorageType
_MscVrSnaStorageType_Object = MibTableColumn
mscVrSnaStorageType = _MscVrSnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 1, 1, 4),
    _MscVrSnaStorageType_Type()
)
mscVrSnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaStorageType.setStatus("mandatory")
_MscVrSnaIndex_Type = NonReplicated
_MscVrSnaIndex_Object = MibTableColumn
mscVrSnaIndex = _MscVrSnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 1, 1, 10),
    _MscVrSnaIndex_Type()
)
mscVrSnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnaIndex.setStatus("mandatory")
_MscVrSnaAdminControlTable_Object = MibTable
mscVrSnaAdminControlTable = _MscVrSnaAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 100)
)
if mibBuilder.loadTexts:
    mscVrSnaAdminControlTable.setStatus("mandatory")
_MscVrSnaAdminControlEntry_Object = MibTableRow
mscVrSnaAdminControlEntry = _MscVrSnaAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 100, 1)
)
mscVrSnaAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaAdminControlEntry.setStatus("mandatory")


class _MscVrSnaSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrSnaSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrSnaSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrSnaSnmpAdminStatus_Object = MibTableColumn
mscVrSnaSnmpAdminStatus = _MscVrSnaSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 100, 1, 1),
    _MscVrSnaSnmpAdminStatus_Type()
)
mscVrSnaSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnaSnmpAdminStatus.setStatus("mandatory")
_MscVrSnaStateTable_Object = MibTable
mscVrSnaStateTable = _MscVrSnaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 101)
)
if mibBuilder.loadTexts:
    mscVrSnaStateTable.setStatus("mandatory")
_MscVrSnaStateEntry_Object = MibTableRow
mscVrSnaStateEntry = _MscVrSnaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 101, 1)
)
mscVrSnaStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaStateEntry.setStatus("mandatory")


class _MscVrSnaAdminState_Type(Integer32):
    """Custom type mscVrSnaAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrSnaAdminState_Type.__name__ = "Integer32"
_MscVrSnaAdminState_Object = MibTableColumn
mscVrSnaAdminState = _MscVrSnaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 101, 1, 1),
    _MscVrSnaAdminState_Type()
)
mscVrSnaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaAdminState.setStatus("mandatory")


class _MscVrSnaOperationalState_Type(Integer32):
    """Custom type mscVrSnaOperationalState based on Integer32"""
    defaultValue = 0

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


_MscVrSnaOperationalState_Type.__name__ = "Integer32"
_MscVrSnaOperationalState_Object = MibTableColumn
mscVrSnaOperationalState = _MscVrSnaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 101, 1, 2),
    _MscVrSnaOperationalState_Type()
)
mscVrSnaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaOperationalState.setStatus("mandatory")


class _MscVrSnaUsageState_Type(Integer32):
    """Custom type mscVrSnaUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrSnaUsageState_Type.__name__ = "Integer32"
_MscVrSnaUsageState_Object = MibTableColumn
mscVrSnaUsageState = _MscVrSnaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 101, 1, 3),
    _MscVrSnaUsageState_Type()
)
mscVrSnaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaUsageState.setStatus("mandatory")
_MscVrSnaOperStatusTable_Object = MibTable
mscVrSnaOperStatusTable = _MscVrSnaOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 102)
)
if mibBuilder.loadTexts:
    mscVrSnaOperStatusTable.setStatus("mandatory")
_MscVrSnaOperStatusEntry_Object = MibTableRow
mscVrSnaOperStatusEntry = _MscVrSnaOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 102, 1)
)
mscVrSnaOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaOperStatusEntry.setStatus("mandatory")


class _MscVrSnaSnmpOperStatus_Type(Integer32):
    """Custom type mscVrSnaSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrSnaSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrSnaSnmpOperStatus_Object = MibTableColumn
mscVrSnaSnmpOperStatus = _MscVrSnaSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 102, 1, 1),
    _MscVrSnaSnmpOperStatus_Type()
)
mscVrSnaSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaSnmpOperStatus.setStatus("mandatory")
_MscVrSnaOperTable_Object = MibTable
mscVrSnaOperTable = _MscVrSnaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 103)
)
if mibBuilder.loadTexts:
    mscVrSnaOperTable.setStatus("mandatory")
_MscVrSnaOperEntry_Object = MibTableRow
mscVrSnaOperEntry = _MscVrSnaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 103, 1)
)
mscVrSnaOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaOperEntry.setStatus("mandatory")


class _MscVrSnaVersion_Type(HexString):
    """Custom type mscVrSnaVersion based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVrSnaVersion_Type.__name__ = "HexString"
_MscVrSnaVersion_Object = MibTableColumn
mscVrSnaVersion = _MscVrSnaVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 103, 1, 2),
    _MscVrSnaVersion_Type()
)
mscVrSnaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaVersion.setStatus("mandatory")
_MscVrSnaCircStatsTable_Object = MibTable
mscVrSnaCircStatsTable = _MscVrSnaCircStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 104)
)
if mibBuilder.loadTexts:
    mscVrSnaCircStatsTable.setStatus("mandatory")
_MscVrSnaCircStatsEntry_Object = MibTableRow
mscVrSnaCircStatsEntry = _MscVrSnaCircStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 104, 1)
)
mscVrSnaCircStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaCircStatsEntry.setStatus("mandatory")


class _MscVrSnaActives_Type(Gauge32):
    """Custom type mscVrSnaActives based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscVrSnaActives_Type.__name__ = "Gauge32"
_MscVrSnaActives_Object = MibTableColumn
mscVrSnaActives = _MscVrSnaActives_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 104, 1, 1),
    _MscVrSnaActives_Type()
)
mscVrSnaActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaActives.setStatus("mandatory")
_MscVrSnaCreates_Type = Counter32
_MscVrSnaCreates_Object = MibTableColumn
mscVrSnaCreates = _MscVrSnaCreates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 104, 1, 2),
    _MscVrSnaCreates_Type()
)
mscVrSnaCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaCreates.setStatus("mandatory")
_MscVrSnaDirStatsTable_Object = MibTable
mscVrSnaDirStatsTable = _MscVrSnaDirStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 105)
)
if mibBuilder.loadTexts:
    mscVrSnaDirStatsTable.setStatus("mandatory")
_MscVrSnaDirStatsEntry_Object = MibTableRow
mscVrSnaDirStatsEntry = _MscVrSnaDirStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 105, 1)
)
mscVrSnaDirStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SnaMIB", "mscVrSnaIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnaDirStatsEntry.setStatus("mandatory")


class _MscVrSnaMacEntries_Type(Gauge32):
    """Custom type mscVrSnaMacEntries based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscVrSnaMacEntries_Type.__name__ = "Gauge32"
_MscVrSnaMacEntries_Object = MibTableColumn
mscVrSnaMacEntries = _MscVrSnaMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 105, 1, 1),
    _MscVrSnaMacEntries_Type()
)
mscVrSnaMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaMacEntries.setStatus("mandatory")
_MscVrSnaMacCacheHits_Type = Counter32
_MscVrSnaMacCacheHits_Object = MibTableColumn
mscVrSnaMacCacheHits = _MscVrSnaMacCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 105, 1, 2),
    _MscVrSnaMacCacheHits_Type()
)
mscVrSnaMacCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaMacCacheHits.setStatus("mandatory")
_MscVrSnaMacCacheMisses_Type = Counter32
_MscVrSnaMacCacheMisses_Object = MibTableColumn
mscVrSnaMacCacheMisses = _MscVrSnaMacCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 14, 105, 1, 3),
    _MscVrSnaMacCacheMisses_Type()
)
mscVrSnaMacCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnaMacCacheMisses.setStatus("mandatory")
_SnaMIB_ObjectIdentity = ObjectIdentity
snaMIB = _SnaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56)
)
_SnaGroup_ObjectIdentity = ObjectIdentity
snaGroup = _SnaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 1)
)
_SnaGroupCA_ObjectIdentity = ObjectIdentity
snaGroupCA = _SnaGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 1, 1)
)
_SnaGroupCA02_ObjectIdentity = ObjectIdentity
snaGroupCA02 = _SnaGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 1, 1, 3)
)
_SnaGroupCA02DevelopmentLoad_ObjectIdentity = ObjectIdentity
snaGroupCA02DevelopmentLoad = _SnaGroupCA02DevelopmentLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 1, 1, 3, 1)
)
_SnaGroupCA0214_ObjectIdentity = ObjectIdentity
snaGroupCA0214 = _SnaGroupCA0214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 1, 1, 3, 1, 14)
)
_SnaGroupCA0214A_ObjectIdentity = ObjectIdentity
snaGroupCA0214A = _SnaGroupCA0214A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 1, 1, 3, 1, 14, 1)
)
_SnaCapabilities_ObjectIdentity = ObjectIdentity
snaCapabilities = _SnaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 3)
)
_SnaCapabilitiesCA_ObjectIdentity = ObjectIdentity
snaCapabilitiesCA = _SnaCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 3, 1)
)
_SnaCapabilitiesCA02_ObjectIdentity = ObjectIdentity
snaCapabilitiesCA02 = _SnaCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 3, 1, 3)
)
_SnaCapabilitiesCA02DevelopmentLoad_ObjectIdentity = ObjectIdentity
snaCapabilitiesCA02DevelopmentLoad = _SnaCapabilitiesCA02DevelopmentLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 3, 1, 3, 1)
)
_SnaCapabilitiesCA0214_ObjectIdentity = ObjectIdentity
snaCapabilitiesCA0214 = _SnaCapabilitiesCA0214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 3, 1, 3, 1, 14)
)
_SnaCapabilitiesCA0214A_ObjectIdentity = ObjectIdentity
snaCapabilitiesCA0214A = _SnaCapabilitiesCA0214A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 56, 3, 1, 3, 1, 14, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-SnaMIB",
    **{"mscVrPpSnaPort": mscVrPpSnaPort,
       "mscVrPpSnaPortRowStatusTable": mscVrPpSnaPortRowStatusTable,
       "mscVrPpSnaPortRowStatusEntry": mscVrPpSnaPortRowStatusEntry,
       "mscVrPpSnaPortRowStatus": mscVrPpSnaPortRowStatus,
       "mscVrPpSnaPortComponentName": mscVrPpSnaPortComponentName,
       "mscVrPpSnaPortStorageType": mscVrPpSnaPortStorageType,
       "mscVrPpSnaPortIndex": mscVrPpSnaPortIndex,
       "mscVrPpSnaPortCircuit": mscVrPpSnaPortCircuit,
       "mscVrPpSnaPortCircuitRowStatusTable": mscVrPpSnaPortCircuitRowStatusTable,
       "mscVrPpSnaPortCircuitRowStatusEntry": mscVrPpSnaPortCircuitRowStatusEntry,
       "mscVrPpSnaPortCircuitRowStatus": mscVrPpSnaPortCircuitRowStatus,
       "mscVrPpSnaPortCircuitComponentName": mscVrPpSnaPortCircuitComponentName,
       "mscVrPpSnaPortCircuitStorageType": mscVrPpSnaPortCircuitStorageType,
       "mscVrPpSnaPortCircuitS1MacIndex": mscVrPpSnaPortCircuitS1MacIndex,
       "mscVrPpSnaPortCircuitS1SapIndex": mscVrPpSnaPortCircuitS1SapIndex,
       "mscVrPpSnaPortCircuitS2MacIndex": mscVrPpSnaPortCircuitS2MacIndex,
       "mscVrPpSnaPortCircuitS2SapIndex": mscVrPpSnaPortCircuitS2SapIndex,
       "mscVrPpSnaPortCircuitOperTable": mscVrPpSnaPortCircuitOperTable,
       "mscVrPpSnaPortCircuitOperEntry": mscVrPpSnaPortCircuitOperEntry,
       "mscVrPpSnaPortCircuitS1DlcType": mscVrPpSnaPortCircuitS1DlcType,
       "mscVrPpSnaPortCircuitS1RouteInfo": mscVrPpSnaPortCircuitS1RouteInfo,
       "mscVrPpSnaPortCircuitS2Location": mscVrPpSnaPortCircuitS2Location,
       "mscVrPpSnaPortCircuitOrigin": mscVrPpSnaPortCircuitOrigin,
       "mscVrPpSnaPortCircuitState": mscVrPpSnaPortCircuitState,
       "mscVrPpSnaPortCircuitPriority": mscVrPpSnaPortCircuitPriority,
       "mscVrPpSnaPortCircuitVcId": mscVrPpSnaPortCircuitVcId,
       "mscVrPpSnaPortAdminControlTable": mscVrPpSnaPortAdminControlTable,
       "mscVrPpSnaPortAdminControlEntry": mscVrPpSnaPortAdminControlEntry,
       "mscVrPpSnaPortSnmpAdminStatus": mscVrPpSnaPortSnmpAdminStatus,
       "mscVrPpSnaPortProvTable": mscVrPpSnaPortProvTable,
       "mscVrPpSnaPortProvEntry": mscVrPpSnaPortProvEntry,
       "mscVrPpSnaPortVirtualSegmentLFSize": mscVrPpSnaPortVirtualSegmentLFSize,
       "mscVrPpSnaPortStateTable": mscVrPpSnaPortStateTable,
       "mscVrPpSnaPortStateEntry": mscVrPpSnaPortStateEntry,
       "mscVrPpSnaPortAdminState": mscVrPpSnaPortAdminState,
       "mscVrPpSnaPortOperationalState": mscVrPpSnaPortOperationalState,
       "mscVrPpSnaPortUsageState": mscVrPpSnaPortUsageState,
       "mscVrPpSnaPortOperStatusTable": mscVrPpSnaPortOperStatusTable,
       "mscVrPpSnaPortOperStatusEntry": mscVrPpSnaPortOperStatusEntry,
       "mscVrPpSnaPortSnmpOperStatus": mscVrPpSnaPortSnmpOperStatus,
       "mscVrSna": mscVrSna,
       "mscVrSnaRowStatusTable": mscVrSnaRowStatusTable,
       "mscVrSnaRowStatusEntry": mscVrSnaRowStatusEntry,
       "mscVrSnaRowStatus": mscVrSnaRowStatus,
       "mscVrSnaComponentName": mscVrSnaComponentName,
       "mscVrSnaStorageType": mscVrSnaStorageType,
       "mscVrSnaIndex": mscVrSnaIndex,
       "mscVrSnaAdminControlTable": mscVrSnaAdminControlTable,
       "mscVrSnaAdminControlEntry": mscVrSnaAdminControlEntry,
       "mscVrSnaSnmpAdminStatus": mscVrSnaSnmpAdminStatus,
       "mscVrSnaStateTable": mscVrSnaStateTable,
       "mscVrSnaStateEntry": mscVrSnaStateEntry,
       "mscVrSnaAdminState": mscVrSnaAdminState,
       "mscVrSnaOperationalState": mscVrSnaOperationalState,
       "mscVrSnaUsageState": mscVrSnaUsageState,
       "mscVrSnaOperStatusTable": mscVrSnaOperStatusTable,
       "mscVrSnaOperStatusEntry": mscVrSnaOperStatusEntry,
       "mscVrSnaSnmpOperStatus": mscVrSnaSnmpOperStatus,
       "mscVrSnaOperTable": mscVrSnaOperTable,
       "mscVrSnaOperEntry": mscVrSnaOperEntry,
       "mscVrSnaVersion": mscVrSnaVersion,
       "mscVrSnaCircStatsTable": mscVrSnaCircStatsTable,
       "mscVrSnaCircStatsEntry": mscVrSnaCircStatsEntry,
       "mscVrSnaActives": mscVrSnaActives,
       "mscVrSnaCreates": mscVrSnaCreates,
       "mscVrSnaDirStatsTable": mscVrSnaDirStatsTable,
       "mscVrSnaDirStatsEntry": mscVrSnaDirStatsEntry,
       "mscVrSnaMacEntries": mscVrSnaMacEntries,
       "mscVrSnaMacCacheHits": mscVrSnaMacCacheHits,
       "mscVrSnaMacCacheMisses": mscVrSnaMacCacheMisses,
       "snaMIB": snaMIB,
       "snaGroup": snaGroup,
       "snaGroupCA": snaGroupCA,
       "snaGroupCA02": snaGroupCA02,
       "snaGroupCA02DevelopmentLoad": snaGroupCA02DevelopmentLoad,
       "snaGroupCA0214": snaGroupCA0214,
       "snaGroupCA0214A": snaGroupCA0214A,
       "snaCapabilities": snaCapabilities,
       "snaCapabilitiesCA": snaCapabilitiesCA,
       "snaCapabilitiesCA02": snaCapabilitiesCA02,
       "snaCapabilitiesCA02DevelopmentLoad": snaCapabilitiesCA02DevelopmentLoad,
       "snaCapabilitiesCA0214": snaCapabilitiesCA0214,
       "snaCapabilitiesCA0214A": snaCapabilitiesCA0214A}
)
