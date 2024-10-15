# SNMP MIB module (ITOUCH-DECNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-DECNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:10 2024
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

(DateTime,
 iTouch) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "DateTime",
    "iTouch")

(PhivAddr,) = mibBuilder.importSymbols(
    "RFC1289-phivMIB",
    "PhivAddr")

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

_XDecnet_ObjectIdentity = ObjectIdentity
xDecnet = _XDecnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14)
)
_XRcp_ObjectIdentity = ObjectIdentity
xRcp = _XRcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 1)
)


class _RcpRemoteAddress_Type(OctetString):
    """Custom type rcpRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RcpRemoteAddress_Type.__name__ = "OctetString"
_RcpRemoteAddress_Object = MibScalar
rcpRemoteAddress = _RcpRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 1, 1),
    _RcpRemoteAddress_Type()
)
rcpRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpRemoteAddress.setStatus("mandatory")
_XPhiv_ObjectIdentity = ObjectIdentity
xPhiv = _XPhiv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2)
)
_XPhivRoute_ObjectIdentity = ObjectIdentity
xPhivRoute = _XPhivRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 1)
)


class _PhivPathSelection_Type(Integer32):
    """Custom type phivPathSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 1),
          ("samePath", 2))
    )


_PhivPathSelection_Type.__name__ = "Integer32"
_PhivPathSelection_Object = MibScalar
phivPathSelection = _PhivPathSelection_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 1, 1),
    _PhivPathSelection_Type()
)
phivPathSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivPathSelection.setStatus("mandatory")


class _PhivMaxPaths_Type(Integer32):
    """Custom type phivMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhivMaxPaths_Type.__name__ = "Integer32"
_PhivMaxPaths_Object = MibScalar
phivMaxPaths = _PhivMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 1, 2),
    _PhivMaxPaths_Type()
)
phivMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivMaxPaths.setStatus("mandatory")


class _PhivStatus_Type(Integer32):
    """Custom type phivStatus based on Integer32"""
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
        *(("active", 1),
          ("badCost", 5),
          ("disabled", 2),
          ("noAddressSpecified", 3),
          ("noInterfacesEnabled", 4))
    )


_PhivStatus_Type.__name__ = "Integer32"
_PhivStatus_Object = MibScalar
phivStatus = _PhivStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 1, 3),
    _PhivStatus_Type()
)
phivStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivStatus.setStatus("mandatory")
_XPhivCircuit_ObjectIdentity = ObjectIdentity
xPhivCircuit = _XPhivCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2)
)
_PhivCircuitTable_Object = MibTable
phivCircuitTable = _PhivCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    phivCircuitTable.setStatus("mandatory")
_PhivCircuitEntry_Object = MibTableRow
phivCircuitEntry = _PhivCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1)
)
phivCircuitEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "xPhivCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivCircuitEntry.setStatus("mandatory")
_XPhivCircuitIndex_Type = Integer32
_XPhivCircuitIndex_Object = MibTableColumn
xPhivCircuitIndex = _XPhivCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 1),
    _XPhivCircuitIndex_Type()
)
xPhivCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPhivCircuitIndex.setStatus("mandatory")


class _PhivCircuitRoutingTimer_Type(Integer32):
    """Custom type phivCircuitRoutingTimer based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivCircuitRoutingTimer_Type.__name__ = "Integer32"
_PhivCircuitRoutingTimer_Object = MibTableColumn
phivCircuitRoutingTimer = _PhivCircuitRoutingTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 2),
    _PhivCircuitRoutingTimer_Type()
)
phivCircuitRoutingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitRoutingTimer.setStatus("mandatory")
_PhivCircuitOperCost_Type = Integer32
_PhivCircuitOperCost_Object = MibTableColumn
phivCircuitOperCost = _PhivCircuitOperCost_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 3),
    _PhivCircuitOperCost_Type()
)
phivCircuitOperCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitOperCost.setStatus("mandatory")
_PhivCircuitErrors_Type = Counter32
_PhivCircuitErrors_Object = MibTableColumn
phivCircuitErrors = _PhivCircuitErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 4),
    _PhivCircuitErrors_Type()
)
phivCircuitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitErrors.setStatus("mandatory")


class _PhivCircuitLastError_Type(Integer32):
    """Custom type phivCircuitLastError based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("addressOutOfRange", 2),
          ("ageExceeded", 3),
          ("destinationUnreachable", 4),
          ("noError", 1),
          ("packetFormatError", 5),
          ("packetOversized", 6),
          ("partialRoutingUpdate", 7),
          ("verificationReject", 8))
    )


_PhivCircuitLastError_Type.__name__ = "Integer32"
_PhivCircuitLastError_Object = MibTableColumn
phivCircuitLastError = _PhivCircuitLastError_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 5),
    _PhivCircuitLastError_Type()
)
phivCircuitLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitLastError.setStatus("mandatory")
_PhivCircuitLastErrorTime_Type = DateTime
_PhivCircuitLastErrorTime_Object = MibTableColumn
phivCircuitLastErrorTime = _PhivCircuitLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 6),
    _PhivCircuitLastErrorTime_Type()
)
phivCircuitLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitLastErrorTime.setStatus("mandatory")


class _PhivCircuitLastErrorData_Type(OctetString):
    """Custom type phivCircuitLastErrorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_PhivCircuitLastErrorData_Type.__name__ = "OctetString"
_PhivCircuitLastErrorData_Object = MibTableColumn
phivCircuitLastErrorData = _PhivCircuitLastErrorData_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 7),
    _PhivCircuitLastErrorData_Type()
)
phivCircuitLastErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitLastErrorData.setStatus("mandatory")


class _PhivCircuitProtocolPriority_Type(Integer32):
    """Custom type phivCircuitProtocolPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_PhivCircuitProtocolPriority_Type.__name__ = "Integer32"
_PhivCircuitProtocolPriority_Object = MibTableColumn
phivCircuitProtocolPriority = _PhivCircuitProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 8),
    _PhivCircuitProtocolPriority_Type()
)
phivCircuitProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitProtocolPriority.setStatus("mandatory")


class _PhivCircuitRoutingPriority_Type(Integer32):
    """Custom type phivCircuitRoutingPriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivCircuitRoutingPriority_Type.__name__ = "Integer32"
_PhivCircuitRoutingPriority_Object = MibTableColumn
phivCircuitRoutingPriority = _PhivCircuitRoutingPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 2, 1, 1, 9),
    _PhivCircuitRoutingPriority_Type()
)
phivCircuitRoutingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitRoutingPriority.setStatus("mandatory")
_XPhivImport_ObjectIdentity = ObjectIdentity
xPhivImport = _XPhivImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3)
)
_PhivCircuitImportTable_Object = MibTable
phivCircuitImportTable = _PhivCircuitImportTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1)
)
if mibBuilder.loadTexts:
    phivCircuitImportTable.setStatus("mandatory")
_PhivCircuitImportEntry_Object = MibTableRow
phivCircuitImportEntry = _PhivCircuitImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1, 1)
)
phivCircuitImportEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "phivCircuitImportIf"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitImportAddr"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitImportMask"),
)
if mibBuilder.loadTexts:
    phivCircuitImportEntry.setStatus("mandatory")
_PhivCircuitImportIf_Type = Integer32
_PhivCircuitImportIf_Object = MibTableColumn
phivCircuitImportIf = _PhivCircuitImportIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1, 1, 1),
    _PhivCircuitImportIf_Type()
)
phivCircuitImportIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitImportIf.setStatus("mandatory")
_PhivCircuitImportAddr_Type = PhivAddr
_PhivCircuitImportAddr_Object = MibTableColumn
phivCircuitImportAddr = _PhivCircuitImportAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1, 1, 2),
    _PhivCircuitImportAddr_Type()
)
phivCircuitImportAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitImportAddr.setStatus("mandatory")
_PhivCircuitImportMask_Type = PhivAddr
_PhivCircuitImportMask_Object = MibTableColumn
phivCircuitImportMask = _PhivCircuitImportMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1, 1, 3),
    _PhivCircuitImportMask_Type()
)
phivCircuitImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitImportMask.setStatus("mandatory")


class _PhivCircuitImportAction_Type(Integer32):
    """Custom type phivCircuitImportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_PhivCircuitImportAction_Type.__name__ = "Integer32"
_PhivCircuitImportAction_Object = MibTableColumn
phivCircuitImportAction = _PhivCircuitImportAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1, 1, 4),
    _PhivCircuitImportAction_Type()
)
phivCircuitImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitImportAction.setStatus("mandatory")


class _PhivCircuitImportStatus_Type(Integer32):
    """Custom type phivCircuitImportStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PhivCircuitImportStatus_Type.__name__ = "Integer32"
_PhivCircuitImportStatus_Object = MibTableColumn
phivCircuitImportStatus = _PhivCircuitImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 3, 1, 1, 5),
    _PhivCircuitImportStatus_Type()
)
phivCircuitImportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitImportStatus.setStatus("mandatory")
_XPhivImportArea_ObjectIdentity = ObjectIdentity
xPhivImportArea = _XPhivImportArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4)
)
_PhivCircuitImportAreaTable_Object = MibTable
phivCircuitImportAreaTable = _PhivCircuitImportAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1)
)
if mibBuilder.loadTexts:
    phivCircuitImportAreaTable.setStatus("mandatory")
_PhivCircuitImportAreaEntry_Object = MibTableRow
phivCircuitImportAreaEntry = _PhivCircuitImportAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1, 1)
)
phivCircuitImportAreaEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "phivCircuitImportAreaIf"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitImportAreaAddr"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitImportAreaMask"),
)
if mibBuilder.loadTexts:
    phivCircuitImportAreaEntry.setStatus("mandatory")
_PhivCircuitImportAreaIf_Type = Integer32
_PhivCircuitImportAreaIf_Object = MibTableColumn
phivCircuitImportAreaIf = _PhivCircuitImportAreaIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1, 1, 1),
    _PhivCircuitImportAreaIf_Type()
)
phivCircuitImportAreaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitImportAreaIf.setStatus("mandatory")
_PhivCircuitImportAreaAddr_Type = PhivAddr
_PhivCircuitImportAreaAddr_Object = MibTableColumn
phivCircuitImportAreaAddr = _PhivCircuitImportAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1, 1, 2),
    _PhivCircuitImportAreaAddr_Type()
)
phivCircuitImportAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitImportAreaAddr.setStatus("mandatory")
_PhivCircuitImportAreaMask_Type = PhivAddr
_PhivCircuitImportAreaMask_Object = MibTableColumn
phivCircuitImportAreaMask = _PhivCircuitImportAreaMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1, 1, 3),
    _PhivCircuitImportAreaMask_Type()
)
phivCircuitImportAreaMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitImportAreaMask.setStatus("mandatory")


class _PhivCircuitImportAreaAction_Type(Integer32):
    """Custom type phivCircuitImportAreaAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_PhivCircuitImportAreaAction_Type.__name__ = "Integer32"
_PhivCircuitImportAreaAction_Object = MibTableColumn
phivCircuitImportAreaAction = _PhivCircuitImportAreaAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1, 1, 4),
    _PhivCircuitImportAreaAction_Type()
)
phivCircuitImportAreaAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitImportAreaAction.setStatus("mandatory")


class _PhivCircuitImportAreaStatus_Type(Integer32):
    """Custom type phivCircuitImportAreaStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PhivCircuitImportAreaStatus_Type.__name__ = "Integer32"
_PhivCircuitImportAreaStatus_Object = MibTableColumn
phivCircuitImportAreaStatus = _PhivCircuitImportAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 4, 1, 1, 5),
    _PhivCircuitImportAreaStatus_Type()
)
phivCircuitImportAreaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitImportAreaStatus.setStatus("mandatory")
_XPhivExport_ObjectIdentity = ObjectIdentity
xPhivExport = _XPhivExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5)
)
_PhivCircuitExportTable_Object = MibTable
phivCircuitExportTable = _PhivCircuitExportTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1)
)
if mibBuilder.loadTexts:
    phivCircuitExportTable.setStatus("mandatory")
_PhivCircuitExportEntry_Object = MibTableRow
phivCircuitExportEntry = _PhivCircuitExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1, 1)
)
phivCircuitExportEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "phivCircuitExportIf"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitExportAddr"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitExportMask"),
)
if mibBuilder.loadTexts:
    phivCircuitExportEntry.setStatus("mandatory")
_PhivCircuitExportIf_Type = Integer32
_PhivCircuitExportIf_Object = MibTableColumn
phivCircuitExportIf = _PhivCircuitExportIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1, 1, 1),
    _PhivCircuitExportIf_Type()
)
phivCircuitExportIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitExportIf.setStatus("mandatory")
_PhivCircuitExportAddr_Type = PhivAddr
_PhivCircuitExportAddr_Object = MibTableColumn
phivCircuitExportAddr = _PhivCircuitExportAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1, 1, 2),
    _PhivCircuitExportAddr_Type()
)
phivCircuitExportAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitExportAddr.setStatus("mandatory")
_PhivCircuitExportMask_Type = PhivAddr
_PhivCircuitExportMask_Object = MibTableColumn
phivCircuitExportMask = _PhivCircuitExportMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1, 1, 3),
    _PhivCircuitExportMask_Type()
)
phivCircuitExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitExportMask.setStatus("mandatory")


class _PhivCircuitExportAction_Type(Integer32):
    """Custom type phivCircuitExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_PhivCircuitExportAction_Type.__name__ = "Integer32"
_PhivCircuitExportAction_Object = MibTableColumn
phivCircuitExportAction = _PhivCircuitExportAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1, 1, 4),
    _PhivCircuitExportAction_Type()
)
phivCircuitExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExportAction.setStatus("mandatory")


class _PhivCircuitExportStatus_Type(Integer32):
    """Custom type phivCircuitExportStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PhivCircuitExportStatus_Type.__name__ = "Integer32"
_PhivCircuitExportStatus_Object = MibTableColumn
phivCircuitExportStatus = _PhivCircuitExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 5, 1, 1, 5),
    _PhivCircuitExportStatus_Type()
)
phivCircuitExportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExportStatus.setStatus("mandatory")
_XPhivExportArea_ObjectIdentity = ObjectIdentity
xPhivExportArea = _XPhivExportArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6)
)
_PhivCircuitExportAreaTable_Object = MibTable
phivCircuitExportAreaTable = _PhivCircuitExportAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1)
)
if mibBuilder.loadTexts:
    phivCircuitExportAreaTable.setStatus("mandatory")
_PhivCircuitExportAreaEntry_Object = MibTableRow
phivCircuitExportAreaEntry = _PhivCircuitExportAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1, 1)
)
phivCircuitExportAreaEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "phivCircuitExportAreaIf"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitExportAreaAddr"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitExportAreaMask"),
)
if mibBuilder.loadTexts:
    phivCircuitExportAreaEntry.setStatus("mandatory")
_PhivCircuitExportAreaIf_Type = Integer32
_PhivCircuitExportAreaIf_Object = MibTableColumn
phivCircuitExportAreaIf = _PhivCircuitExportAreaIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1, 1, 1),
    _PhivCircuitExportAreaIf_Type()
)
phivCircuitExportAreaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitExportAreaIf.setStatus("mandatory")
_PhivCircuitExportAreaAddr_Type = PhivAddr
_PhivCircuitExportAreaAddr_Object = MibTableColumn
phivCircuitExportAreaAddr = _PhivCircuitExportAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1, 1, 2),
    _PhivCircuitExportAreaAddr_Type()
)
phivCircuitExportAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitExportAreaAddr.setStatus("mandatory")
_PhivCircuitExportAreaMask_Type = PhivAddr
_PhivCircuitExportAreaMask_Object = MibTableColumn
phivCircuitExportAreaMask = _PhivCircuitExportAreaMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1, 1, 3),
    _PhivCircuitExportAreaMask_Type()
)
phivCircuitExportAreaMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitExportAreaMask.setStatus("mandatory")


class _PhivCircuitExportAreaAction_Type(Integer32):
    """Custom type phivCircuitExportAreaAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_PhivCircuitExportAreaAction_Type.__name__ = "Integer32"
_PhivCircuitExportAreaAction_Object = MibTableColumn
phivCircuitExportAreaAction = _PhivCircuitExportAreaAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1, 1, 4),
    _PhivCircuitExportAreaAction_Type()
)
phivCircuitExportAreaAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExportAreaAction.setStatus("mandatory")


class _PhivCircuitExportAreaStatus_Type(Integer32):
    """Custom type phivCircuitExportAreaStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PhivCircuitExportAreaStatus_Type.__name__ = "Integer32"
_PhivCircuitExportAreaStatus_Object = MibTableColumn
phivCircuitExportAreaStatus = _PhivCircuitExportAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 6, 1, 1, 5),
    _PhivCircuitExportAreaStatus_Type()
)
phivCircuitExportAreaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExportAreaStatus.setStatus("mandatory")
_XPhivFilter_ObjectIdentity = ObjectIdentity
xPhivFilter = _XPhivFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7)
)
_PhivCircuitFilterTable_Object = MibTable
phivCircuitFilterTable = _PhivCircuitFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1)
)
if mibBuilder.loadTexts:
    phivCircuitFilterTable.setStatus("mandatory")
_PhivCircuitFilterEntry_Object = MibTableRow
phivCircuitFilterEntry = _PhivCircuitFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1)
)
phivCircuitFilterEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "phivCircuitFilterIf"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitFilterDstAddr"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitFilterDstMask"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitFilterSrcAddr"),
    (0, "ITOUCH-DECNET-MIB", "phivCircuitFilterSrcMask"),
)
if mibBuilder.loadTexts:
    phivCircuitFilterEntry.setStatus("mandatory")
_PhivCircuitFilterIf_Type = Integer32
_PhivCircuitFilterIf_Object = MibTableColumn
phivCircuitFilterIf = _PhivCircuitFilterIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 1),
    _PhivCircuitFilterIf_Type()
)
phivCircuitFilterIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitFilterIf.setStatus("mandatory")
_PhivCircuitFilterDstAddr_Type = PhivAddr
_PhivCircuitFilterDstAddr_Object = MibTableColumn
phivCircuitFilterDstAddr = _PhivCircuitFilterDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 2),
    _PhivCircuitFilterDstAddr_Type()
)
phivCircuitFilterDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitFilterDstAddr.setStatus("mandatory")
_PhivCircuitFilterDstMask_Type = PhivAddr
_PhivCircuitFilterDstMask_Object = MibTableColumn
phivCircuitFilterDstMask = _PhivCircuitFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 3),
    _PhivCircuitFilterDstMask_Type()
)
phivCircuitFilterDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitFilterDstMask.setStatus("mandatory")
_PhivCircuitFilterSrcAddr_Type = PhivAddr
_PhivCircuitFilterSrcAddr_Object = MibTableColumn
phivCircuitFilterSrcAddr = _PhivCircuitFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 4),
    _PhivCircuitFilterSrcAddr_Type()
)
phivCircuitFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitFilterSrcAddr.setStatus("mandatory")
_PhivCircuitFilterSrcMask_Type = PhivAddr
_PhivCircuitFilterSrcMask_Object = MibTableColumn
phivCircuitFilterSrcMask = _PhivCircuitFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 5),
    _PhivCircuitFilterSrcMask_Type()
)
phivCircuitFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitFilterSrcMask.setStatus("mandatory")


class _PhivCircuitFilterAction_Type(Integer32):
    """Custom type phivCircuitFilterAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_PhivCircuitFilterAction_Type.__name__ = "Integer32"
_PhivCircuitFilterAction_Object = MibTableColumn
phivCircuitFilterAction = _PhivCircuitFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 6),
    _PhivCircuitFilterAction_Type()
)
phivCircuitFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitFilterAction.setStatus("mandatory")


class _PhivCircuitFilterStatus_Type(Integer32):
    """Custom type phivCircuitFilterStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PhivCircuitFilterStatus_Type.__name__ = "Integer32"
_PhivCircuitFilterStatus_Object = MibTableColumn
phivCircuitFilterStatus = _PhivCircuitFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 7, 1, 1, 7),
    _PhivCircuitFilterStatus_Type()
)
phivCircuitFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitFilterStatus.setStatus("mandatory")
_XPhivTraffic_ObjectIdentity = ObjectIdentity
xPhivTraffic = _XPhivTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8)
)


class _PhivTrafficSort_Type(Integer32):
    """Custom type phivTrafficSort based on Integer32"""
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


_PhivTrafficSort_Type.__name__ = "Integer32"
_PhivTrafficSort_Object = MibScalar
phivTrafficSort = _PhivTrafficSort_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 1),
    _PhivTrafficSort_Type()
)
phivTrafficSort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivTrafficSort.setStatus("mandatory")
_PhivTrafficTable_Object = MibTable
phivTrafficTable = _PhivTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2)
)
if mibBuilder.loadTexts:
    phivTrafficTable.setStatus("mandatory")
_PhivTrafficEntry_Object = MibTableRow
phivTrafficEntry = _PhivTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2, 1)
)
phivTrafficEntry.setIndexNames(
    (0, "ITOUCH-DECNET-MIB", "phivTrafficIndex"),
)
if mibBuilder.loadTexts:
    phivTrafficEntry.setStatus("mandatory")
_PhivTrafficIndex_Type = Integer32
_PhivTrafficIndex_Object = MibTableColumn
phivTrafficIndex = _PhivTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2, 1, 1),
    _PhivTrafficIndex_Type()
)
phivTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivTrafficIndex.setStatus("mandatory")


class _PhivTrafficPercent_Type(Integer32):
    """Custom type phivTrafficPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PhivTrafficPercent_Type.__name__ = "Integer32"
_PhivTrafficPercent_Object = MibTableColumn
phivTrafficPercent = _PhivTrafficPercent_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2, 1, 2),
    _PhivTrafficPercent_Type()
)
phivTrafficPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivTrafficPercent.setStatus("mandatory")
_PhivTrafficDst_Type = PhivAddr
_PhivTrafficDst_Object = MibTableColumn
phivTrafficDst = _PhivTrafficDst_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2, 1, 3),
    _PhivTrafficDst_Type()
)
phivTrafficDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivTrafficDst.setStatus("mandatory")
_PhivTrafficSrc_Type = PhivAddr
_PhivTrafficSrc_Object = MibTableColumn
phivTrafficSrc = _PhivTrafficSrc_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2, 1, 4),
    _PhivTrafficSrc_Type()
)
phivTrafficSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivTrafficSrc.setStatus("mandatory")
_PhivTrafficIf_Type = Integer32
_PhivTrafficIf_Object = MibTableColumn
phivTrafficIf = _PhivTrafficIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 2, 8, 2, 1, 5),
    _PhivTrafficIf_Type()
)
phivTrafficIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivTrafficIf.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-DECNET-MIB",
    **{"xDecnet": xDecnet,
       "xRcp": xRcp,
       "rcpRemoteAddress": rcpRemoteAddress,
       "xPhiv": xPhiv,
       "xPhivRoute": xPhivRoute,
       "phivPathSelection": phivPathSelection,
       "phivMaxPaths": phivMaxPaths,
       "phivStatus": phivStatus,
       "xPhivCircuit": xPhivCircuit,
       "phivCircuitTable": phivCircuitTable,
       "phivCircuitEntry": phivCircuitEntry,
       "xPhivCircuitIndex": xPhivCircuitIndex,
       "phivCircuitRoutingTimer": phivCircuitRoutingTimer,
       "phivCircuitOperCost": phivCircuitOperCost,
       "phivCircuitErrors": phivCircuitErrors,
       "phivCircuitLastError": phivCircuitLastError,
       "phivCircuitLastErrorTime": phivCircuitLastErrorTime,
       "phivCircuitLastErrorData": phivCircuitLastErrorData,
       "phivCircuitProtocolPriority": phivCircuitProtocolPriority,
       "phivCircuitRoutingPriority": phivCircuitRoutingPriority,
       "xPhivImport": xPhivImport,
       "phivCircuitImportTable": phivCircuitImportTable,
       "phivCircuitImportEntry": phivCircuitImportEntry,
       "phivCircuitImportIf": phivCircuitImportIf,
       "phivCircuitImportAddr": phivCircuitImportAddr,
       "phivCircuitImportMask": phivCircuitImportMask,
       "phivCircuitImportAction": phivCircuitImportAction,
       "phivCircuitImportStatus": phivCircuitImportStatus,
       "xPhivImportArea": xPhivImportArea,
       "phivCircuitImportAreaTable": phivCircuitImportAreaTable,
       "phivCircuitImportAreaEntry": phivCircuitImportAreaEntry,
       "phivCircuitImportAreaIf": phivCircuitImportAreaIf,
       "phivCircuitImportAreaAddr": phivCircuitImportAreaAddr,
       "phivCircuitImportAreaMask": phivCircuitImportAreaMask,
       "phivCircuitImportAreaAction": phivCircuitImportAreaAction,
       "phivCircuitImportAreaStatus": phivCircuitImportAreaStatus,
       "xPhivExport": xPhivExport,
       "phivCircuitExportTable": phivCircuitExportTable,
       "phivCircuitExportEntry": phivCircuitExportEntry,
       "phivCircuitExportIf": phivCircuitExportIf,
       "phivCircuitExportAddr": phivCircuitExportAddr,
       "phivCircuitExportMask": phivCircuitExportMask,
       "phivCircuitExportAction": phivCircuitExportAction,
       "phivCircuitExportStatus": phivCircuitExportStatus,
       "xPhivExportArea": xPhivExportArea,
       "phivCircuitExportAreaTable": phivCircuitExportAreaTable,
       "phivCircuitExportAreaEntry": phivCircuitExportAreaEntry,
       "phivCircuitExportAreaIf": phivCircuitExportAreaIf,
       "phivCircuitExportAreaAddr": phivCircuitExportAreaAddr,
       "phivCircuitExportAreaMask": phivCircuitExportAreaMask,
       "phivCircuitExportAreaAction": phivCircuitExportAreaAction,
       "phivCircuitExportAreaStatus": phivCircuitExportAreaStatus,
       "xPhivFilter": xPhivFilter,
       "phivCircuitFilterTable": phivCircuitFilterTable,
       "phivCircuitFilterEntry": phivCircuitFilterEntry,
       "phivCircuitFilterIf": phivCircuitFilterIf,
       "phivCircuitFilterDstAddr": phivCircuitFilterDstAddr,
       "phivCircuitFilterDstMask": phivCircuitFilterDstMask,
       "phivCircuitFilterSrcAddr": phivCircuitFilterSrcAddr,
       "phivCircuitFilterSrcMask": phivCircuitFilterSrcMask,
       "phivCircuitFilterAction": phivCircuitFilterAction,
       "phivCircuitFilterStatus": phivCircuitFilterStatus,
       "xPhivTraffic": xPhivTraffic,
       "phivTrafficSort": phivTrafficSort,
       "phivTrafficTable": phivTrafficTable,
       "phivTrafficEntry": phivTrafficEntry,
       "phivTrafficIndex": phivTrafficIndex,
       "phivTrafficPercent": phivTrafficPercent,
       "phivTrafficDst": phivTrafficDst,
       "phivTrafficSrc": phivTrafficSrc,
       "phivTrafficIf": phivTrafficIf}
)
