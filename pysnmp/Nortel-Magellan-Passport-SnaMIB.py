# SNMP MIB module (Nortel-Magellan-Passport-SnaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-SnaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:22 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "DashedHexString",
    "HexString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vr,
 vrIndex,
 vrPp,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
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

_VrPpSnaPort_ObjectIdentity = ObjectIdentity
vrPpSnaPort = _VrPpSnaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15)
)
_VrPpSnaPortRowStatusTable_Object = MibTable
vrPpSnaPortRowStatusTable = _VrPpSnaPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 1)
)
if mibBuilder.loadTexts:
    vrPpSnaPortRowStatusTable.setStatus("mandatory")
_VrPpSnaPortRowStatusEntry_Object = MibTableRow
vrPpSnaPortRowStatusEntry = _VrPpSnaPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 1, 1)
)
vrPpSnaPortRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortRowStatusEntry.setStatus("mandatory")
_VrPpSnaPortRowStatus_Type = RowStatus
_VrPpSnaPortRowStatus_Object = MibTableColumn
vrPpSnaPortRowStatus = _VrPpSnaPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 1, 1, 1),
    _VrPpSnaPortRowStatus_Type()
)
vrPpSnaPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSnaPortRowStatus.setStatus("mandatory")
_VrPpSnaPortComponentName_Type = DisplayString
_VrPpSnaPortComponentName_Object = MibTableColumn
vrPpSnaPortComponentName = _VrPpSnaPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 1, 1, 2),
    _VrPpSnaPortComponentName_Type()
)
vrPpSnaPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortComponentName.setStatus("mandatory")
_VrPpSnaPortStorageType_Type = StorageType
_VrPpSnaPortStorageType_Object = MibTableColumn
vrPpSnaPortStorageType = _VrPpSnaPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 1, 1, 4),
    _VrPpSnaPortStorageType_Type()
)
vrPpSnaPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortStorageType.setStatus("mandatory")
_VrPpSnaPortIndex_Type = NonReplicated
_VrPpSnaPortIndex_Object = MibTableColumn
vrPpSnaPortIndex = _VrPpSnaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 1, 1, 10),
    _VrPpSnaPortIndex_Type()
)
vrPpSnaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSnaPortIndex.setStatus("mandatory")
_VrPpSnaPortCircuit_ObjectIdentity = ObjectIdentity
vrPpSnaPortCircuit = _VrPpSnaPortCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2)
)
_VrPpSnaPortCircuitRowStatusTable_Object = MibTable
vrPpSnaPortCircuitRowStatusTable = _VrPpSnaPortCircuitRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitRowStatusTable.setStatus("mandatory")
_VrPpSnaPortCircuitRowStatusEntry_Object = MibTableRow
vrPpSnaPortCircuitRowStatusEntry = _VrPpSnaPortCircuitRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1)
)
vrPpSnaPortCircuitRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS1MacIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS1SapIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS2MacIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS2SapIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitRowStatusEntry.setStatus("mandatory")
_VrPpSnaPortCircuitRowStatus_Type = RowStatus
_VrPpSnaPortCircuitRowStatus_Object = MibTableColumn
vrPpSnaPortCircuitRowStatus = _VrPpSnaPortCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 1),
    _VrPpSnaPortCircuitRowStatus_Type()
)
vrPpSnaPortCircuitRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitRowStatus.setStatus("mandatory")
_VrPpSnaPortCircuitComponentName_Type = DisplayString
_VrPpSnaPortCircuitComponentName_Object = MibTableColumn
vrPpSnaPortCircuitComponentName = _VrPpSnaPortCircuitComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 2),
    _VrPpSnaPortCircuitComponentName_Type()
)
vrPpSnaPortCircuitComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitComponentName.setStatus("mandatory")
_VrPpSnaPortCircuitStorageType_Type = StorageType
_VrPpSnaPortCircuitStorageType_Object = MibTableColumn
vrPpSnaPortCircuitStorageType = _VrPpSnaPortCircuitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 4),
    _VrPpSnaPortCircuitStorageType_Type()
)
vrPpSnaPortCircuitStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitStorageType.setStatus("mandatory")


class _VrPpSnaPortCircuitS1MacIndex_Type(DashedHexString):
    """Custom type vrPpSnaPortCircuitS1MacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrPpSnaPortCircuitS1MacIndex_Type.__name__ = "DashedHexString"
_VrPpSnaPortCircuitS1MacIndex_Object = MibTableColumn
vrPpSnaPortCircuitS1MacIndex = _VrPpSnaPortCircuitS1MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 10),
    _VrPpSnaPortCircuitS1MacIndex_Type()
)
vrPpSnaPortCircuitS1MacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS1MacIndex.setStatus("mandatory")


class _VrPpSnaPortCircuitS1SapIndex_Type(Integer32):
    """Custom type vrPpSnaPortCircuitS1SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_VrPpSnaPortCircuitS1SapIndex_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitS1SapIndex_Object = MibTableColumn
vrPpSnaPortCircuitS1SapIndex = _VrPpSnaPortCircuitS1SapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 11),
    _VrPpSnaPortCircuitS1SapIndex_Type()
)
vrPpSnaPortCircuitS1SapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS1SapIndex.setStatus("mandatory")


class _VrPpSnaPortCircuitS2MacIndex_Type(DashedHexString):
    """Custom type vrPpSnaPortCircuitS2MacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrPpSnaPortCircuitS2MacIndex_Type.__name__ = "DashedHexString"
_VrPpSnaPortCircuitS2MacIndex_Object = MibTableColumn
vrPpSnaPortCircuitS2MacIndex = _VrPpSnaPortCircuitS2MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 12),
    _VrPpSnaPortCircuitS2MacIndex_Type()
)
vrPpSnaPortCircuitS2MacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS2MacIndex.setStatus("mandatory")


class _VrPpSnaPortCircuitS2SapIndex_Type(Integer32):
    """Custom type vrPpSnaPortCircuitS2SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_VrPpSnaPortCircuitS2SapIndex_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitS2SapIndex_Object = MibTableColumn
vrPpSnaPortCircuitS2SapIndex = _VrPpSnaPortCircuitS2SapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 1, 1, 13),
    _VrPpSnaPortCircuitS2SapIndex_Type()
)
vrPpSnaPortCircuitS2SapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS2SapIndex.setStatus("mandatory")
_VrPpSnaPortCircuitOperTable_Object = MibTable
vrPpSnaPortCircuitOperTable = _VrPpSnaPortCircuitOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100)
)
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitOperTable.setStatus("mandatory")
_VrPpSnaPortCircuitOperEntry_Object = MibTableRow
vrPpSnaPortCircuitOperEntry = _VrPpSnaPortCircuitOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1)
)
vrPpSnaPortCircuitOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS1MacIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS1SapIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS2MacIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortCircuitS2SapIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitOperEntry.setStatus("mandatory")


class _VrPpSnaPortCircuitS1DlcType_Type(Integer32):
    """Custom type vrPpSnaPortCircuitS1DlcType based on Integer32"""
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


_VrPpSnaPortCircuitS1DlcType_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitS1DlcType_Object = MibTableColumn
vrPpSnaPortCircuitS1DlcType = _VrPpSnaPortCircuitS1DlcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 2),
    _VrPpSnaPortCircuitS1DlcType_Type()
)
vrPpSnaPortCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS1DlcType.setStatus("mandatory")


class _VrPpSnaPortCircuitS1RouteInfo_Type(HexString):
    """Custom type vrPpSnaPortCircuitS1RouteInfo based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VrPpSnaPortCircuitS1RouteInfo_Type.__name__ = "HexString"
_VrPpSnaPortCircuitS1RouteInfo_Object = MibTableColumn
vrPpSnaPortCircuitS1RouteInfo = _VrPpSnaPortCircuitS1RouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 3),
    _VrPpSnaPortCircuitS1RouteInfo_Type()
)
vrPpSnaPortCircuitS1RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS1RouteInfo.setStatus("mandatory")


class _VrPpSnaPortCircuitS2Location_Type(Integer32):
    """Custom type vrPpSnaPortCircuitS2Location based on Integer32"""
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


_VrPpSnaPortCircuitS2Location_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitS2Location_Object = MibTableColumn
vrPpSnaPortCircuitS2Location = _VrPpSnaPortCircuitS2Location_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 6),
    _VrPpSnaPortCircuitS2Location_Type()
)
vrPpSnaPortCircuitS2Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitS2Location.setStatus("mandatory")


class _VrPpSnaPortCircuitOrigin_Type(Integer32):
    """Custom type vrPpSnaPortCircuitOrigin based on Integer32"""
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


_VrPpSnaPortCircuitOrigin_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitOrigin_Object = MibTableColumn
vrPpSnaPortCircuitOrigin = _VrPpSnaPortCircuitOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 10),
    _VrPpSnaPortCircuitOrigin_Type()
)
vrPpSnaPortCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitOrigin.setStatus("mandatory")


class _VrPpSnaPortCircuitState_Type(Integer32):
    """Custom type vrPpSnaPortCircuitState based on Integer32"""
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


_VrPpSnaPortCircuitState_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitState_Object = MibTableColumn
vrPpSnaPortCircuitState = _VrPpSnaPortCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 13),
    _VrPpSnaPortCircuitState_Type()
)
vrPpSnaPortCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitState.setStatus("mandatory")


class _VrPpSnaPortCircuitPriority_Type(Integer32):
    """Custom type vrPpSnaPortCircuitPriority based on Integer32"""
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


_VrPpSnaPortCircuitPriority_Type.__name__ = "Integer32"
_VrPpSnaPortCircuitPriority_Object = MibTableColumn
vrPpSnaPortCircuitPriority = _VrPpSnaPortCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 14),
    _VrPpSnaPortCircuitPriority_Type()
)
vrPpSnaPortCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitPriority.setStatus("mandatory")
_VrPpSnaPortCircuitVcId_Type = RowPointer
_VrPpSnaPortCircuitVcId_Object = MibTableColumn
vrPpSnaPortCircuitVcId = _VrPpSnaPortCircuitVcId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 2, 100, 1, 26),
    _VrPpSnaPortCircuitVcId_Type()
)
vrPpSnaPortCircuitVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortCircuitVcId.setStatus("mandatory")
_VrPpSnaPortAdminControlTable_Object = MibTable
vrPpSnaPortAdminControlTable = _VrPpSnaPortAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 100)
)
if mibBuilder.loadTexts:
    vrPpSnaPortAdminControlTable.setStatus("mandatory")
_VrPpSnaPortAdminControlEntry_Object = MibTableRow
vrPpSnaPortAdminControlEntry = _VrPpSnaPortAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 100, 1)
)
vrPpSnaPortAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortAdminControlEntry.setStatus("mandatory")


class _VrPpSnaPortSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpSnaPortSnmpAdminStatus based on Integer32"""
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


_VrPpSnaPortSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpSnaPortSnmpAdminStatus_Object = MibTableColumn
vrPpSnaPortSnmpAdminStatus = _VrPpSnaPortSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 100, 1, 1),
    _VrPpSnaPortSnmpAdminStatus_Type()
)
vrPpSnaPortSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSnaPortSnmpAdminStatus.setStatus("mandatory")
_VrPpSnaPortProvTable_Object = MibTable
vrPpSnaPortProvTable = _VrPpSnaPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 101)
)
if mibBuilder.loadTexts:
    vrPpSnaPortProvTable.setStatus("mandatory")
_VrPpSnaPortProvEntry_Object = MibTableRow
vrPpSnaPortProvEntry = _VrPpSnaPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 101, 1)
)
vrPpSnaPortProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortProvEntry.setStatus("mandatory")


class _VrPpSnaPortVirtualSegmentLFSize_Type(Unsigned32):
    """Custom type vrPpSnaPortVirtualSegmentLFSize based on Unsigned32"""
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


_VrPpSnaPortVirtualSegmentLFSize_Type.__name__ = "Unsigned32"
_VrPpSnaPortVirtualSegmentLFSize_Object = MibTableColumn
vrPpSnaPortVirtualSegmentLFSize = _VrPpSnaPortVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 101, 1, 1),
    _VrPpSnaPortVirtualSegmentLFSize_Type()
)
vrPpSnaPortVirtualSegmentLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSnaPortVirtualSegmentLFSize.setStatus("mandatory")
_VrPpSnaPortStateTable_Object = MibTable
vrPpSnaPortStateTable = _VrPpSnaPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 103)
)
if mibBuilder.loadTexts:
    vrPpSnaPortStateTable.setStatus("mandatory")
_VrPpSnaPortStateEntry_Object = MibTableRow
vrPpSnaPortStateEntry = _VrPpSnaPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 103, 1)
)
vrPpSnaPortStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortStateEntry.setStatus("mandatory")


class _VrPpSnaPortAdminState_Type(Integer32):
    """Custom type vrPpSnaPortAdminState based on Integer32"""
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


_VrPpSnaPortAdminState_Type.__name__ = "Integer32"
_VrPpSnaPortAdminState_Object = MibTableColumn
vrPpSnaPortAdminState = _VrPpSnaPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 103, 1, 1),
    _VrPpSnaPortAdminState_Type()
)
vrPpSnaPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortAdminState.setStatus("mandatory")


class _VrPpSnaPortOperationalState_Type(Integer32):
    """Custom type vrPpSnaPortOperationalState based on Integer32"""
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


_VrPpSnaPortOperationalState_Type.__name__ = "Integer32"
_VrPpSnaPortOperationalState_Object = MibTableColumn
vrPpSnaPortOperationalState = _VrPpSnaPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 103, 1, 2),
    _VrPpSnaPortOperationalState_Type()
)
vrPpSnaPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortOperationalState.setStatus("mandatory")


class _VrPpSnaPortUsageState_Type(Integer32):
    """Custom type vrPpSnaPortUsageState based on Integer32"""
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


_VrPpSnaPortUsageState_Type.__name__ = "Integer32"
_VrPpSnaPortUsageState_Object = MibTableColumn
vrPpSnaPortUsageState = _VrPpSnaPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 103, 1, 3),
    _VrPpSnaPortUsageState_Type()
)
vrPpSnaPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortUsageState.setStatus("mandatory")
_VrPpSnaPortOperStatusTable_Object = MibTable
vrPpSnaPortOperStatusTable = _VrPpSnaPortOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 104)
)
if mibBuilder.loadTexts:
    vrPpSnaPortOperStatusTable.setStatus("mandatory")
_VrPpSnaPortOperStatusEntry_Object = MibTableRow
vrPpSnaPortOperStatusEntry = _VrPpSnaPortOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 104, 1)
)
vrPpSnaPortOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrPpSnaPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpSnaPortOperStatusEntry.setStatus("mandatory")


class _VrPpSnaPortSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSnaPortSnmpOperStatus based on Integer32"""
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


_VrPpSnaPortSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSnaPortSnmpOperStatus_Object = MibTableColumn
vrPpSnaPortSnmpOperStatus = _VrPpSnaPortSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 15, 104, 1, 1),
    _VrPpSnaPortSnmpOperStatus_Type()
)
vrPpSnaPortSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnaPortSnmpOperStatus.setStatus("mandatory")
_VrSna_ObjectIdentity = ObjectIdentity
vrSna = _VrSna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14)
)
_VrSnaRowStatusTable_Object = MibTable
vrSnaRowStatusTable = _VrSnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 1)
)
if mibBuilder.loadTexts:
    vrSnaRowStatusTable.setStatus("mandatory")
_VrSnaRowStatusEntry_Object = MibTableRow
vrSnaRowStatusEntry = _VrSnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 1, 1)
)
vrSnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaRowStatusEntry.setStatus("mandatory")
_VrSnaRowStatus_Type = RowStatus
_VrSnaRowStatus_Object = MibTableColumn
vrSnaRowStatus = _VrSnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 1, 1, 1),
    _VrSnaRowStatus_Type()
)
vrSnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnaRowStatus.setStatus("mandatory")
_VrSnaComponentName_Type = DisplayString
_VrSnaComponentName_Object = MibTableColumn
vrSnaComponentName = _VrSnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 1, 1, 2),
    _VrSnaComponentName_Type()
)
vrSnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaComponentName.setStatus("mandatory")
_VrSnaStorageType_Type = StorageType
_VrSnaStorageType_Object = MibTableColumn
vrSnaStorageType = _VrSnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 1, 1, 4),
    _VrSnaStorageType_Type()
)
vrSnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaStorageType.setStatus("mandatory")
_VrSnaIndex_Type = NonReplicated
_VrSnaIndex_Object = MibTableColumn
vrSnaIndex = _VrSnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 1, 1, 10),
    _VrSnaIndex_Type()
)
vrSnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnaIndex.setStatus("mandatory")
_VrSnaAdminControlTable_Object = MibTable
vrSnaAdminControlTable = _VrSnaAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 100)
)
if mibBuilder.loadTexts:
    vrSnaAdminControlTable.setStatus("mandatory")
_VrSnaAdminControlEntry_Object = MibTableRow
vrSnaAdminControlEntry = _VrSnaAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 100, 1)
)
vrSnaAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaAdminControlEntry.setStatus("mandatory")


class _VrSnaSnmpAdminStatus_Type(Integer32):
    """Custom type vrSnaSnmpAdminStatus based on Integer32"""
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


_VrSnaSnmpAdminStatus_Type.__name__ = "Integer32"
_VrSnaSnmpAdminStatus_Object = MibTableColumn
vrSnaSnmpAdminStatus = _VrSnaSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 100, 1, 1),
    _VrSnaSnmpAdminStatus_Type()
)
vrSnaSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnaSnmpAdminStatus.setStatus("mandatory")
_VrSnaStateTable_Object = MibTable
vrSnaStateTable = _VrSnaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 101)
)
if mibBuilder.loadTexts:
    vrSnaStateTable.setStatus("mandatory")
_VrSnaStateEntry_Object = MibTableRow
vrSnaStateEntry = _VrSnaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 101, 1)
)
vrSnaStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaStateEntry.setStatus("mandatory")


class _VrSnaAdminState_Type(Integer32):
    """Custom type vrSnaAdminState based on Integer32"""
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


_VrSnaAdminState_Type.__name__ = "Integer32"
_VrSnaAdminState_Object = MibTableColumn
vrSnaAdminState = _VrSnaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 101, 1, 1),
    _VrSnaAdminState_Type()
)
vrSnaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaAdminState.setStatus("mandatory")


class _VrSnaOperationalState_Type(Integer32):
    """Custom type vrSnaOperationalState based on Integer32"""
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


_VrSnaOperationalState_Type.__name__ = "Integer32"
_VrSnaOperationalState_Object = MibTableColumn
vrSnaOperationalState = _VrSnaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 101, 1, 2),
    _VrSnaOperationalState_Type()
)
vrSnaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaOperationalState.setStatus("mandatory")


class _VrSnaUsageState_Type(Integer32):
    """Custom type vrSnaUsageState based on Integer32"""
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


_VrSnaUsageState_Type.__name__ = "Integer32"
_VrSnaUsageState_Object = MibTableColumn
vrSnaUsageState = _VrSnaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 101, 1, 3),
    _VrSnaUsageState_Type()
)
vrSnaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaUsageState.setStatus("mandatory")
_VrSnaOperStatusTable_Object = MibTable
vrSnaOperStatusTable = _VrSnaOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 102)
)
if mibBuilder.loadTexts:
    vrSnaOperStatusTable.setStatus("mandatory")
_VrSnaOperStatusEntry_Object = MibTableRow
vrSnaOperStatusEntry = _VrSnaOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 102, 1)
)
vrSnaOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaOperStatusEntry.setStatus("mandatory")


class _VrSnaSnmpOperStatus_Type(Integer32):
    """Custom type vrSnaSnmpOperStatus based on Integer32"""
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


_VrSnaSnmpOperStatus_Type.__name__ = "Integer32"
_VrSnaSnmpOperStatus_Object = MibTableColumn
vrSnaSnmpOperStatus = _VrSnaSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 102, 1, 1),
    _VrSnaSnmpOperStatus_Type()
)
vrSnaSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaSnmpOperStatus.setStatus("mandatory")
_VrSnaOperTable_Object = MibTable
vrSnaOperTable = _VrSnaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 103)
)
if mibBuilder.loadTexts:
    vrSnaOperTable.setStatus("mandatory")
_VrSnaOperEntry_Object = MibTableRow
vrSnaOperEntry = _VrSnaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 103, 1)
)
vrSnaOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaOperEntry.setStatus("mandatory")


class _VrSnaVersion_Type(HexString):
    """Custom type vrSnaVersion based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VrSnaVersion_Type.__name__ = "HexString"
_VrSnaVersion_Object = MibTableColumn
vrSnaVersion = _VrSnaVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 103, 1, 2),
    _VrSnaVersion_Type()
)
vrSnaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaVersion.setStatus("mandatory")
_VrSnaCircStatsTable_Object = MibTable
vrSnaCircStatsTable = _VrSnaCircStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 104)
)
if mibBuilder.loadTexts:
    vrSnaCircStatsTable.setStatus("mandatory")
_VrSnaCircStatsEntry_Object = MibTableRow
vrSnaCircStatsEntry = _VrSnaCircStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 104, 1)
)
vrSnaCircStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaCircStatsEntry.setStatus("mandatory")


class _VrSnaActives_Type(Gauge32):
    """Custom type vrSnaActives based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_VrSnaActives_Type.__name__ = "Gauge32"
_VrSnaActives_Object = MibTableColumn
vrSnaActives = _VrSnaActives_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 104, 1, 1),
    _VrSnaActives_Type()
)
vrSnaActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaActives.setStatus("mandatory")
_VrSnaCreates_Type = Counter32
_VrSnaCreates_Object = MibTableColumn
vrSnaCreates = _VrSnaCreates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 104, 1, 2),
    _VrSnaCreates_Type()
)
vrSnaCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaCreates.setStatus("mandatory")
_VrSnaDirStatsTable_Object = MibTable
vrSnaDirStatsTable = _VrSnaDirStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 105)
)
if mibBuilder.loadTexts:
    vrSnaDirStatsTable.setStatus("mandatory")
_VrSnaDirStatsEntry_Object = MibTableRow
vrSnaDirStatsEntry = _VrSnaDirStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 105, 1)
)
vrSnaDirStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SnaMIB", "vrSnaIndex"),
)
if mibBuilder.loadTexts:
    vrSnaDirStatsEntry.setStatus("mandatory")


class _VrSnaMacEntries_Type(Gauge32):
    """Custom type vrSnaMacEntries based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VrSnaMacEntries_Type.__name__ = "Gauge32"
_VrSnaMacEntries_Object = MibTableColumn
vrSnaMacEntries = _VrSnaMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 105, 1, 1),
    _VrSnaMacEntries_Type()
)
vrSnaMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaMacEntries.setStatus("mandatory")
_VrSnaMacCacheHits_Type = Counter32
_VrSnaMacCacheHits_Object = MibTableColumn
vrSnaMacCacheHits = _VrSnaMacCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 105, 1, 2),
    _VrSnaMacCacheHits_Type()
)
vrSnaMacCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaMacCacheHits.setStatus("mandatory")
_VrSnaMacCacheMisses_Type = Counter32
_VrSnaMacCacheMisses_Object = MibTableColumn
vrSnaMacCacheMisses = _VrSnaMacCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 14, 105, 1, 3),
    _VrSnaMacCacheMisses_Type()
)
vrSnaMacCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnaMacCacheMisses.setStatus("mandatory")
_SnaMIB_ObjectIdentity = ObjectIdentity
snaMIB = _SnaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56)
)
_SnaGroup_ObjectIdentity = ObjectIdentity
snaGroup = _SnaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 1)
)
_SnaGroupBE_ObjectIdentity = ObjectIdentity
snaGroupBE = _SnaGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 1, 5)
)
_SnaGroupBE01_ObjectIdentity = ObjectIdentity
snaGroupBE01 = _SnaGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 1, 5, 2)
)
_SnaGroupBE01A_ObjectIdentity = ObjectIdentity
snaGroupBE01A = _SnaGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 1, 5, 2, 2)
)
_SnaCapabilities_ObjectIdentity = ObjectIdentity
snaCapabilities = _SnaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 3)
)
_SnaCapabilitiesBE_ObjectIdentity = ObjectIdentity
snaCapabilitiesBE = _SnaCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 3, 5)
)
_SnaCapabilitiesBE01_ObjectIdentity = ObjectIdentity
snaCapabilitiesBE01 = _SnaCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 3, 5, 2)
)
_SnaCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
snaCapabilitiesBE01A = _SnaCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 56, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-SnaMIB",
    **{"vrPpSnaPort": vrPpSnaPort,
       "vrPpSnaPortRowStatusTable": vrPpSnaPortRowStatusTable,
       "vrPpSnaPortRowStatusEntry": vrPpSnaPortRowStatusEntry,
       "vrPpSnaPortRowStatus": vrPpSnaPortRowStatus,
       "vrPpSnaPortComponentName": vrPpSnaPortComponentName,
       "vrPpSnaPortStorageType": vrPpSnaPortStorageType,
       "vrPpSnaPortIndex": vrPpSnaPortIndex,
       "vrPpSnaPortCircuit": vrPpSnaPortCircuit,
       "vrPpSnaPortCircuitRowStatusTable": vrPpSnaPortCircuitRowStatusTable,
       "vrPpSnaPortCircuitRowStatusEntry": vrPpSnaPortCircuitRowStatusEntry,
       "vrPpSnaPortCircuitRowStatus": vrPpSnaPortCircuitRowStatus,
       "vrPpSnaPortCircuitComponentName": vrPpSnaPortCircuitComponentName,
       "vrPpSnaPortCircuitStorageType": vrPpSnaPortCircuitStorageType,
       "vrPpSnaPortCircuitS1MacIndex": vrPpSnaPortCircuitS1MacIndex,
       "vrPpSnaPortCircuitS1SapIndex": vrPpSnaPortCircuitS1SapIndex,
       "vrPpSnaPortCircuitS2MacIndex": vrPpSnaPortCircuitS2MacIndex,
       "vrPpSnaPortCircuitS2SapIndex": vrPpSnaPortCircuitS2SapIndex,
       "vrPpSnaPortCircuitOperTable": vrPpSnaPortCircuitOperTable,
       "vrPpSnaPortCircuitOperEntry": vrPpSnaPortCircuitOperEntry,
       "vrPpSnaPortCircuitS1DlcType": vrPpSnaPortCircuitS1DlcType,
       "vrPpSnaPortCircuitS1RouteInfo": vrPpSnaPortCircuitS1RouteInfo,
       "vrPpSnaPortCircuitS2Location": vrPpSnaPortCircuitS2Location,
       "vrPpSnaPortCircuitOrigin": vrPpSnaPortCircuitOrigin,
       "vrPpSnaPortCircuitState": vrPpSnaPortCircuitState,
       "vrPpSnaPortCircuitPriority": vrPpSnaPortCircuitPriority,
       "vrPpSnaPortCircuitVcId": vrPpSnaPortCircuitVcId,
       "vrPpSnaPortAdminControlTable": vrPpSnaPortAdminControlTable,
       "vrPpSnaPortAdminControlEntry": vrPpSnaPortAdminControlEntry,
       "vrPpSnaPortSnmpAdminStatus": vrPpSnaPortSnmpAdminStatus,
       "vrPpSnaPortProvTable": vrPpSnaPortProvTable,
       "vrPpSnaPortProvEntry": vrPpSnaPortProvEntry,
       "vrPpSnaPortVirtualSegmentLFSize": vrPpSnaPortVirtualSegmentLFSize,
       "vrPpSnaPortStateTable": vrPpSnaPortStateTable,
       "vrPpSnaPortStateEntry": vrPpSnaPortStateEntry,
       "vrPpSnaPortAdminState": vrPpSnaPortAdminState,
       "vrPpSnaPortOperationalState": vrPpSnaPortOperationalState,
       "vrPpSnaPortUsageState": vrPpSnaPortUsageState,
       "vrPpSnaPortOperStatusTable": vrPpSnaPortOperStatusTable,
       "vrPpSnaPortOperStatusEntry": vrPpSnaPortOperStatusEntry,
       "vrPpSnaPortSnmpOperStatus": vrPpSnaPortSnmpOperStatus,
       "vrSna": vrSna,
       "vrSnaRowStatusTable": vrSnaRowStatusTable,
       "vrSnaRowStatusEntry": vrSnaRowStatusEntry,
       "vrSnaRowStatus": vrSnaRowStatus,
       "vrSnaComponentName": vrSnaComponentName,
       "vrSnaStorageType": vrSnaStorageType,
       "vrSnaIndex": vrSnaIndex,
       "vrSnaAdminControlTable": vrSnaAdminControlTable,
       "vrSnaAdminControlEntry": vrSnaAdminControlEntry,
       "vrSnaSnmpAdminStatus": vrSnaSnmpAdminStatus,
       "vrSnaStateTable": vrSnaStateTable,
       "vrSnaStateEntry": vrSnaStateEntry,
       "vrSnaAdminState": vrSnaAdminState,
       "vrSnaOperationalState": vrSnaOperationalState,
       "vrSnaUsageState": vrSnaUsageState,
       "vrSnaOperStatusTable": vrSnaOperStatusTable,
       "vrSnaOperStatusEntry": vrSnaOperStatusEntry,
       "vrSnaSnmpOperStatus": vrSnaSnmpOperStatus,
       "vrSnaOperTable": vrSnaOperTable,
       "vrSnaOperEntry": vrSnaOperEntry,
       "vrSnaVersion": vrSnaVersion,
       "vrSnaCircStatsTable": vrSnaCircStatsTable,
       "vrSnaCircStatsEntry": vrSnaCircStatsEntry,
       "vrSnaActives": vrSnaActives,
       "vrSnaCreates": vrSnaCreates,
       "vrSnaDirStatsTable": vrSnaDirStatsTable,
       "vrSnaDirStatsEntry": vrSnaDirStatsEntry,
       "vrSnaMacEntries": vrSnaMacEntries,
       "vrSnaMacCacheHits": vrSnaMacCacheHits,
       "vrSnaMacCacheMisses": vrSnaMacCacheMisses,
       "snaMIB": snaMIB,
       "snaGroup": snaGroup,
       "snaGroupBE": snaGroupBE,
       "snaGroupBE01": snaGroupBE01,
       "snaGroupBE01A": snaGroupBE01A,
       "snaCapabilities": snaCapabilities,
       "snaCapabilitiesBE": snaCapabilitiesBE,
       "snaCapabilitiesBE01": snaCapabilitiesBE01,
       "snaCapabilitiesBE01A": snaCapabilitiesBE01A}
)
