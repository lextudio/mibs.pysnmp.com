# SNMP MIB module (Wellfleet-MPLS-MLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MPLS-MLM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:42 2024
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

(wfMplsAtmGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfMplsAtmGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfMplsAtm_ObjectIdentity = ObjectIdentity
wfMplsAtm = _WfMplsAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1)
)
_WfMplsAtmIfConfTable_Object = MibTable
wfMplsAtmIfConfTable = _WfMplsAtmIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 1)
)
if mibBuilder.loadTexts:
    wfMplsAtmIfConfTable.setStatus("mandatory")
_WfMplsAtmIfConfEntry_Object = MibTableRow
wfMplsAtmIfConfEntry = _WfMplsAtmIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 1, 1)
)
wfMplsAtmIfConfEntry.setIndexNames(
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmIfConfLineNumber"),
)
if mibBuilder.loadTexts:
    wfMplsAtmIfConfEntry.setStatus("mandatory")


class _WfMplsAtmIfCreate_Type(Integer32):
    """Custom type wfMplsAtmIfCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfMplsAtmIfCreate_Type.__name__ = "Integer32"
_WfMplsAtmIfCreate_Object = MibTableColumn
wfMplsAtmIfCreate = _WfMplsAtmIfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 1, 1, 1),
    _WfMplsAtmIfCreate_Type()
)
wfMplsAtmIfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmIfCreate.setStatus("mandatory")


class _WfMplsAtmIfAdminStatus_Type(Integer32):
    """Custom type wfMplsAtmIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfMplsAtmIfAdminStatus_Type.__name__ = "Integer32"
_WfMplsAtmIfAdminStatus_Object = MibTableColumn
wfMplsAtmIfAdminStatus = _WfMplsAtmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 1, 1, 2),
    _WfMplsAtmIfAdminStatus_Type()
)
wfMplsAtmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmIfAdminStatus.setStatus("mandatory")
_WfMplsAtmIfConfLineNumber_Type = Integer32
_WfMplsAtmIfConfLineNumber_Object = MibTableColumn
wfMplsAtmIfConfLineNumber = _WfMplsAtmIfConfLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 1, 1, 3),
    _WfMplsAtmIfConfLineNumber_Type()
)
wfMplsAtmIfConfLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfConfLineNumber.setStatus("mandatory")


class _WfMplsAtmIfDebugLogMask_Type(Integer32):
    """Custom type wfMplsAtmIfDebugLogMask based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              128,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 255),
          ("fsm", 16),
          ("none", 1),
          ("other", 128))
    )


_WfMplsAtmIfDebugLogMask_Type.__name__ = "Integer32"
_WfMplsAtmIfDebugLogMask_Object = MibTableColumn
wfMplsAtmIfDebugLogMask = _WfMplsAtmIfDebugLogMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 1, 1, 4),
    _WfMplsAtmIfDebugLogMask_Type()
)
wfMplsAtmIfDebugLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmIfDebugLogMask.setStatus("mandatory")
_WfMplsAtmIfStatusTable_Object = MibTable
wfMplsAtmIfStatusTable = _WfMplsAtmIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2)
)
if mibBuilder.loadTexts:
    wfMplsAtmIfStatusTable.setStatus("mandatory")
_WfMplsAtmIfStatusEntry_Object = MibTableRow
wfMplsAtmIfStatusEntry = _WfMplsAtmIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1)
)
wfMplsAtmIfStatusEntry.setIndexNames(
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmIfStatusLineNumber"),
)
if mibBuilder.loadTexts:
    wfMplsAtmIfStatusEntry.setStatus("mandatory")


class _WfMplsAtmIfOperStatus_Type(Integer32):
    """Custom type wfMplsAtmIfOperStatus based on Integer32"""
    defaultValue = 5

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
        *(("cleanup", 4),
          ("down", 1),
          ("init", 2),
          ("notpresent", 5),
          ("up", 3))
    )


_WfMplsAtmIfOperStatus_Type.__name__ = "Integer32"
_WfMplsAtmIfOperStatus_Object = MibTableColumn
wfMplsAtmIfOperStatus = _WfMplsAtmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1, 1),
    _WfMplsAtmIfOperStatus_Type()
)
wfMplsAtmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfOperStatus.setStatus("mandatory")
_WfMplsAtmIfStatusLineNumber_Type = Integer32
_WfMplsAtmIfStatusLineNumber_Object = MibTableColumn
wfMplsAtmIfStatusLineNumber = _WfMplsAtmIfStatusLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1, 2),
    _WfMplsAtmIfStatusLineNumber_Type()
)
wfMplsAtmIfStatusLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfStatusLineNumber.setStatus("mandatory")


class _WfMplsAtmIfCircuit_Type(Integer32):
    """Custom type wfMplsAtmIfCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsAtmIfCircuit_Type.__name__ = "Integer32"
_WfMplsAtmIfCircuit_Object = MibTableColumn
wfMplsAtmIfCircuit = _WfMplsAtmIfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1, 3),
    _WfMplsAtmIfCircuit_Type()
)
wfMplsAtmIfCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfCircuit.setStatus("mandatory")
_WfMplsAtmIfTotalSess_Type = Counter32
_WfMplsAtmIfTotalSess_Object = MibTableColumn
wfMplsAtmIfTotalSess = _WfMplsAtmIfTotalSess_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1, 4),
    _WfMplsAtmIfTotalSess_Type()
)
wfMplsAtmIfTotalSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfTotalSess.setStatus("mandatory")
_WfMplsAtmIfTotalVcs_Type = Counter32
_WfMplsAtmIfTotalVcs_Object = MibTableColumn
wfMplsAtmIfTotalVcs = _WfMplsAtmIfTotalVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1, 5),
    _WfMplsAtmIfTotalVcs_Type()
)
wfMplsAtmIfTotalVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfTotalVcs.setStatus("mandatory")
_WfMplsAtmIfAllocVcs_Type = Counter32
_WfMplsAtmIfAllocVcs_Object = MibTableColumn
wfMplsAtmIfAllocVcs = _WfMplsAtmIfAllocVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 2, 1, 6),
    _WfMplsAtmIfAllocVcs_Type()
)
wfMplsAtmIfAllocVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmIfAllocVcs.setStatus("mandatory")
_WfMplsAtmSessConfTable_Object = MibTable
wfMplsAtmSessConfTable = _WfMplsAtmSessConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3)
)
if mibBuilder.loadTexts:
    wfMplsAtmSessConfTable.setStatus("mandatory")
_WfMplsAtmSessConfEntry_Object = MibTableRow
wfMplsAtmSessConfEntry = _WfMplsAtmSessConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1)
)
wfMplsAtmSessConfEntry.setIndexNames(
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmSessConfLineNumber"),
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmSessConfIndex"),
)
if mibBuilder.loadTexts:
    wfMplsAtmSessConfEntry.setStatus("mandatory")


class _WfMplsAtmSessDelete_Type(Integer32):
    """Custom type wfMplsAtmSessDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfMplsAtmSessDelete_Type.__name__ = "Integer32"
_WfMplsAtmSessDelete_Object = MibTableColumn
wfMplsAtmSessDelete = _WfMplsAtmSessDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 1),
    _WfMplsAtmSessDelete_Type()
)
wfMplsAtmSessDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDelete.setStatus("mandatory")


class _WfMplsAtmSessAdminStatus_Type(Integer32):
    """Custom type wfMplsAtmSessAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfMplsAtmSessAdminStatus_Type.__name__ = "Integer32"
_WfMplsAtmSessAdminStatus_Object = MibTableColumn
wfMplsAtmSessAdminStatus = _WfMplsAtmSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 2),
    _WfMplsAtmSessAdminStatus_Type()
)
wfMplsAtmSessAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessAdminStatus.setStatus("mandatory")
_WfMplsAtmSessConfLineNumber_Type = Integer32
_WfMplsAtmSessConfLineNumber_Object = MibTableColumn
wfMplsAtmSessConfLineNumber = _WfMplsAtmSessConfLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 3),
    _WfMplsAtmSessConfLineNumber_Type()
)
wfMplsAtmSessConfLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfLineNumber.setStatus("mandatory")


class _WfMplsAtmSessConfIndex_Type(Integer32):
    """Custom type wfMplsAtmSessConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsAtmSessConfIndex_Type.__name__ = "Integer32"
_WfMplsAtmSessConfIndex_Object = MibTableColumn
wfMplsAtmSessConfIndex = _WfMplsAtmSessConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 4),
    _WfMplsAtmSessConfIndex_Type()
)
wfMplsAtmSessConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfIndex.setStatus("mandatory")


class _WfMplsAtmSessConfDefVclVpi_Type(Integer32):
    """Custom type wfMplsAtmSessConfDefVclVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfMplsAtmSessConfDefVclVpi_Type.__name__ = "Integer32"
_WfMplsAtmSessConfDefVclVpi_Object = MibTableColumn
wfMplsAtmSessConfDefVclVpi = _WfMplsAtmSessConfDefVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 5),
    _WfMplsAtmSessConfDefVclVpi_Type()
)
wfMplsAtmSessConfDefVclVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfDefVclVpi.setStatus("mandatory")


class _WfMplsAtmSessConfDefVclVci_Type(Integer32):
    """Custom type wfMplsAtmSessConfDefVclVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessConfDefVclVci_Type.__name__ = "Integer32"
_WfMplsAtmSessConfDefVclVci_Object = MibTableColumn
wfMplsAtmSessConfDefVclVci = _WfMplsAtmSessConfDefVclVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 6),
    _WfMplsAtmSessConfDefVclVci_Type()
)
wfMplsAtmSessConfDefVclVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfDefVclVci.setStatus("mandatory")


class _WfMplsAtmSessConfVcRangeVpi_Type(Integer32):
    """Custom type wfMplsAtmSessConfVcRangeVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfMplsAtmSessConfVcRangeVpi_Type.__name__ = "Integer32"
_WfMplsAtmSessConfVcRangeVpi_Object = MibTableColumn
wfMplsAtmSessConfVcRangeVpi = _WfMplsAtmSessConfVcRangeVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 7),
    _WfMplsAtmSessConfVcRangeVpi_Type()
)
wfMplsAtmSessConfVcRangeVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfVcRangeVpi.setStatus("mandatory")


class _WfMplsAtmSessConfVcRangeMinVci_Type(Integer32):
    """Custom type wfMplsAtmSessConfVcRangeMinVci based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessConfVcRangeMinVci_Type.__name__ = "Integer32"
_WfMplsAtmSessConfVcRangeMinVci_Object = MibTableColumn
wfMplsAtmSessConfVcRangeMinVci = _WfMplsAtmSessConfVcRangeMinVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 8),
    _WfMplsAtmSessConfVcRangeMinVci_Type()
)
wfMplsAtmSessConfVcRangeMinVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfVcRangeMinVci.setStatus("mandatory")


class _WfMplsAtmSessConfVcRangeMaxVci_Type(Integer32):
    """Custom type wfMplsAtmSessConfVcRangeMaxVci based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessConfVcRangeMaxVci_Type.__name__ = "Integer32"
_WfMplsAtmSessConfVcRangeMaxVci_Object = MibTableColumn
wfMplsAtmSessConfVcRangeMaxVci = _WfMplsAtmSessConfVcRangeMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 9),
    _WfMplsAtmSessConfVcRangeMaxVci_Type()
)
wfMplsAtmSessConfVcRangeMaxVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessConfVcRangeMaxVci.setStatus("mandatory")


class _WfMplsAtmSessDefVclXmtPeakCellRate_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclXmtPeakCellRate based on Integer32"""
    defaultValue = 0


_WfMplsAtmSessDefVclXmtPeakCellRate_Object = MibTableColumn
wfMplsAtmSessDefVclXmtPeakCellRate = _WfMplsAtmSessDefVclXmtPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 10),
    _WfMplsAtmSessDefVclXmtPeakCellRate_Type()
)
wfMplsAtmSessDefVclXmtPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclXmtPeakCellRate.setStatus("mandatory")


class _WfMplsAtmSessDefVclXmtSustainableCellRate_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclXmtSustainableCellRate based on Integer32"""
    defaultValue = 0


_WfMplsAtmSessDefVclXmtSustainableCellRate_Object = MibTableColumn
wfMplsAtmSessDefVclXmtSustainableCellRate = _WfMplsAtmSessDefVclXmtSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 11),
    _WfMplsAtmSessDefVclXmtSustainableCellRate_Type()
)
wfMplsAtmSessDefVclXmtSustainableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclXmtSustainableCellRate.setStatus("mandatory")


class _WfMplsAtmSessDefVclXmtBurstSize_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclXmtBurstSize based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("default", 40)
    )


_WfMplsAtmSessDefVclXmtBurstSize_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclXmtBurstSize_Object = MibTableColumn
wfMplsAtmSessDefVclXmtBurstSize = _WfMplsAtmSessDefVclXmtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 12),
    _WfMplsAtmSessDefVclXmtBurstSize_Type()
)
wfMplsAtmSessDefVclXmtBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclXmtBurstSize.setStatus("mandatory")


class _WfMplsAtmSessDefVclXmtQosClass_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclXmtQosClass based on Integer32"""
    defaultValue = 4

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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_WfMplsAtmSessDefVclXmtQosClass_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclXmtQosClass_Object = MibTableColumn
wfMplsAtmSessDefVclXmtQosClass = _WfMplsAtmSessDefVclXmtQosClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 13),
    _WfMplsAtmSessDefVclXmtQosClass_Type()
)
wfMplsAtmSessDefVclXmtQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclXmtQosClass.setStatus("mandatory")


class _WfMplsAtmSessDefVclRcvPeakCellRate_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclRcvPeakCellRate based on Integer32"""
    defaultValue = 0


_WfMplsAtmSessDefVclRcvPeakCellRate_Object = MibTableColumn
wfMplsAtmSessDefVclRcvPeakCellRate = _WfMplsAtmSessDefVclRcvPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 14),
    _WfMplsAtmSessDefVclRcvPeakCellRate_Type()
)
wfMplsAtmSessDefVclRcvPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclRcvPeakCellRate.setStatus("mandatory")


class _WfMplsAtmSessDefVclRcvSustainableCellRate_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclRcvSustainableCellRate based on Integer32"""
    defaultValue = 0


_WfMplsAtmSessDefVclRcvSustainableCellRate_Object = MibTableColumn
wfMplsAtmSessDefVclRcvSustainableCellRate = _WfMplsAtmSessDefVclRcvSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 15),
    _WfMplsAtmSessDefVclRcvSustainableCellRate_Type()
)
wfMplsAtmSessDefVclRcvSustainableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclRcvSustainableCellRate.setStatus("mandatory")


class _WfMplsAtmSessDefVclRcvBurstSize_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclRcvBurstSize based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("default", 40)
    )


_WfMplsAtmSessDefVclRcvBurstSize_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclRcvBurstSize_Object = MibTableColumn
wfMplsAtmSessDefVclRcvBurstSize = _WfMplsAtmSessDefVclRcvBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 16),
    _WfMplsAtmSessDefVclRcvBurstSize_Type()
)
wfMplsAtmSessDefVclRcvBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclRcvBurstSize.setStatus("mandatory")


class _WfMplsAtmSessDefVclRcvQosClass_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclRcvQosClass based on Integer32"""
    defaultValue = 4

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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_WfMplsAtmSessDefVclRcvQosClass_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclRcvQosClass_Object = MibTableColumn
wfMplsAtmSessDefVclRcvQosClass = _WfMplsAtmSessDefVclRcvQosClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 17),
    _WfMplsAtmSessDefVclRcvQosClass_Type()
)
wfMplsAtmSessDefVclRcvQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclRcvQosClass.setStatus("mandatory")


class _WfMplsAtmSessDefVclAalType_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclAalType based on Integer32"""
    defaultValue = 3

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
        *(("other", 4),
          ("type1", 1),
          ("type34", 2),
          ("type5", 3),
          ("unknown", 5))
    )


_WfMplsAtmSessDefVclAalType_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclAalType_Object = MibTableColumn
wfMplsAtmSessDefVclAalType = _WfMplsAtmSessDefVclAalType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 18),
    _WfMplsAtmSessDefVclAalType_Type()
)
wfMplsAtmSessDefVclAalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclAalType.setStatus("mandatory")


class _WfMplsAtmSessDefVclAalCpcsTransmitSduSize_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclAalCpcsTransmitSduSize based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsAtmSessDefVclAalCpcsTransmitSduSize_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclAalCpcsTransmitSduSize_Object = MibTableColumn
wfMplsAtmSessDefVclAalCpcsTransmitSduSize = _WfMplsAtmSessDefVclAalCpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 19),
    _WfMplsAtmSessDefVclAalCpcsTransmitSduSize_Type()
)
wfMplsAtmSessDefVclAalCpcsTransmitSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclAalCpcsTransmitSduSize.setStatus("mandatory")


class _WfMplsAtmSessDefVclAalCpcsReceiveSduSize_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclAalCpcsReceiveSduSize based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsAtmSessDefVclAalCpcsReceiveSduSize_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclAalCpcsReceiveSduSize_Object = MibTableColumn
wfMplsAtmSessDefVclAalCpcsReceiveSduSize = _WfMplsAtmSessDefVclAalCpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 20),
    _WfMplsAtmSessDefVclAalCpcsReceiveSduSize_Type()
)
wfMplsAtmSessDefVclAalCpcsReceiveSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclAalCpcsReceiveSduSize.setStatus("mandatory")


class _WfMplsAtmSessDefVclAalEncapsType_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclAalEncapsType based on Integer32"""
    defaultValue = 2

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
        *(("llcencaps", 2),
          ("null", 3),
          ("other", 4),
          ("unknown", 1))
    )


_WfMplsAtmSessDefVclAalEncapsType_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclAalEncapsType_Object = MibTableColumn
wfMplsAtmSessDefVclAalEncapsType = _WfMplsAtmSessDefVclAalEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 21),
    _WfMplsAtmSessDefVclAalEncapsType_Type()
)
wfMplsAtmSessDefVclAalEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclAalEncapsType.setStatus("mandatory")


class _WfMplsAtmSessDefVclCongestionIndication_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclCongestionIndication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WfMplsAtmSessDefVclCongestionIndication_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclCongestionIndication_Object = MibTableColumn
wfMplsAtmSessDefVclCongestionIndication = _WfMplsAtmSessDefVclCongestionIndication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 22),
    _WfMplsAtmSessDefVclCongestionIndication_Type()
)
wfMplsAtmSessDefVclCongestionIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclCongestionIndication.setStatus("mandatory")


class _WfMplsAtmSessDefVclCellLossPriority_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclCellLossPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WfMplsAtmSessDefVclCellLossPriority_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclCellLossPriority_Object = MibTableColumn
wfMplsAtmSessDefVclCellLossPriority = _WfMplsAtmSessDefVclCellLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 23),
    _WfMplsAtmSessDefVclCellLossPriority_Type()
)
wfMplsAtmSessDefVclCellLossPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclCellLossPriority.setStatus("mandatory")


class _WfMplsAtmSessDefVclXmtTagging_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclXmtTagging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfMplsAtmSessDefVclXmtTagging_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclXmtTagging_Object = MibTableColumn
wfMplsAtmSessDefVclXmtTagging = _WfMplsAtmSessDefVclXmtTagging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 24),
    _WfMplsAtmSessDefVclXmtTagging_Type()
)
wfMplsAtmSessDefVclXmtTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclXmtTagging.setStatus("mandatory")


class _WfMplsAtmSessDefVclRcvTagging_Type(Integer32):
    """Custom type wfMplsAtmSessDefVclRcvTagging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfMplsAtmSessDefVclRcvTagging_Type.__name__ = "Integer32"
_WfMplsAtmSessDefVclRcvTagging_Object = MibTableColumn
wfMplsAtmSessDefVclRcvTagging = _WfMplsAtmSessDefVclRcvTagging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 3, 1, 25),
    _WfMplsAtmSessDefVclRcvTagging_Type()
)
wfMplsAtmSessDefVclRcvTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsAtmSessDefVclRcvTagging.setStatus("mandatory")
_WfMplsAtmSessStatusTable_Object = MibTable
wfMplsAtmSessStatusTable = _WfMplsAtmSessStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4)
)
if mibBuilder.loadTexts:
    wfMplsAtmSessStatusTable.setStatus("mandatory")
_WfMplsAtmSessStatusEntry_Object = MibTableRow
wfMplsAtmSessStatusEntry = _WfMplsAtmSessStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1)
)
wfMplsAtmSessStatusEntry.setIndexNames(
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmSessStatusLineNumber"),
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmSessStatusIndex"),
)
if mibBuilder.loadTexts:
    wfMplsAtmSessStatusEntry.setStatus("mandatory")


class _WfMplsAtmSessOperStatus_Type(Integer32):
    """Custom type wfMplsAtmSessOperStatus based on Integer32"""
    defaultValue = 5

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
        *(("cleanup", 4),
          ("down", 1),
          ("init", 2),
          ("notpresent", 5),
          ("up", 3))
    )


_WfMplsAtmSessOperStatus_Type.__name__ = "Integer32"
_WfMplsAtmSessOperStatus_Object = MibTableColumn
wfMplsAtmSessOperStatus = _WfMplsAtmSessOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 1),
    _WfMplsAtmSessOperStatus_Type()
)
wfMplsAtmSessOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessOperStatus.setStatus("mandatory")
_WfMplsAtmSessStatusLineNumber_Type = Integer32
_WfMplsAtmSessStatusLineNumber_Object = MibTableColumn
wfMplsAtmSessStatusLineNumber = _WfMplsAtmSessStatusLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 2),
    _WfMplsAtmSessStatusLineNumber_Type()
)
wfMplsAtmSessStatusLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessStatusLineNumber.setStatus("mandatory")


class _WfMplsAtmSessStatusIndex_Type(Integer32):
    """Custom type wfMplsAtmSessStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsAtmSessStatusIndex_Type.__name__ = "Integer32"
_WfMplsAtmSessStatusIndex_Object = MibTableColumn
wfMplsAtmSessStatusIndex = _WfMplsAtmSessStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 3),
    _WfMplsAtmSessStatusIndex_Type()
)
wfMplsAtmSessStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessStatusIndex.setStatus("mandatory")


class _WfMplsAtmSessActualVcRangeVpi_Type(Integer32):
    """Custom type wfMplsAtmSessActualVcRangeVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfMplsAtmSessActualVcRangeVpi_Type.__name__ = "Integer32"
_WfMplsAtmSessActualVcRangeVpi_Object = MibTableColumn
wfMplsAtmSessActualVcRangeVpi = _WfMplsAtmSessActualVcRangeVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 4),
    _WfMplsAtmSessActualVcRangeVpi_Type()
)
wfMplsAtmSessActualVcRangeVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessActualVcRangeVpi.setStatus("mandatory")


class _WfMplsAtmSessActualVcRangeMinVci_Type(Integer32):
    """Custom type wfMplsAtmSessActualVcRangeMinVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessActualVcRangeMinVci_Type.__name__ = "Integer32"
_WfMplsAtmSessActualVcRangeMinVci_Object = MibTableColumn
wfMplsAtmSessActualVcRangeMinVci = _WfMplsAtmSessActualVcRangeMinVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 5),
    _WfMplsAtmSessActualVcRangeMinVci_Type()
)
wfMplsAtmSessActualVcRangeMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessActualVcRangeMinVci.setStatus("mandatory")


class _WfMplsAtmSessActualVcRangeMaxVci_Type(Integer32):
    """Custom type wfMplsAtmSessActualVcRangeMaxVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessActualVcRangeMaxVci_Type.__name__ = "Integer32"
_WfMplsAtmSessActualVcRangeMaxVci_Object = MibTableColumn
wfMplsAtmSessActualVcRangeMaxVci = _WfMplsAtmSessActualVcRangeMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 6),
    _WfMplsAtmSessActualVcRangeMaxVci_Type()
)
wfMplsAtmSessActualVcRangeMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessActualVcRangeMaxVci.setStatus("mandatory")


class _WfMplsAtmSessNegotiatedVcRangeVpi_Type(Integer32):
    """Custom type wfMplsAtmSessNegotiatedVcRangeVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_WfMplsAtmSessNegotiatedVcRangeVpi_Type.__name__ = "Integer32"
_WfMplsAtmSessNegotiatedVcRangeVpi_Object = MibTableColumn
wfMplsAtmSessNegotiatedVcRangeVpi = _WfMplsAtmSessNegotiatedVcRangeVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 7),
    _WfMplsAtmSessNegotiatedVcRangeVpi_Type()
)
wfMplsAtmSessNegotiatedVcRangeVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessNegotiatedVcRangeVpi.setStatus("mandatory")


class _WfMplsAtmSessNegotiatedVcRangeMinVci_Type(Integer32):
    """Custom type wfMplsAtmSessNegotiatedVcRangeMinVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessNegotiatedVcRangeMinVci_Type.__name__ = "Integer32"
_WfMplsAtmSessNegotiatedVcRangeMinVci_Object = MibTableColumn
wfMplsAtmSessNegotiatedVcRangeMinVci = _WfMplsAtmSessNegotiatedVcRangeMinVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 8),
    _WfMplsAtmSessNegotiatedVcRangeMinVci_Type()
)
wfMplsAtmSessNegotiatedVcRangeMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessNegotiatedVcRangeMinVci.setStatus("mandatory")


class _WfMplsAtmSessNegotiatedVcRangeMaxVci_Type(Integer32):
    """Custom type wfMplsAtmSessNegotiatedVcRangeMaxVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfMplsAtmSessNegotiatedVcRangeMaxVci_Type.__name__ = "Integer32"
_WfMplsAtmSessNegotiatedVcRangeMaxVci_Object = MibTableColumn
wfMplsAtmSessNegotiatedVcRangeMaxVci = _WfMplsAtmSessNegotiatedVcRangeMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 9),
    _WfMplsAtmSessNegotiatedVcRangeMaxVci_Type()
)
wfMplsAtmSessNegotiatedVcRangeMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessNegotiatedVcRangeMaxVci.setStatus("mandatory")
_WfMplsAtmSessInboundInuseVcs_Type = Counter32
_WfMplsAtmSessInboundInuseVcs_Object = MibTableColumn
wfMplsAtmSessInboundInuseVcs = _WfMplsAtmSessInboundInuseVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 10),
    _WfMplsAtmSessInboundInuseVcs_Type()
)
wfMplsAtmSessInboundInuseVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessInboundInuseVcs.setStatus("mandatory")
_WfMplsAtmSessOutboundInuseVcs_Type = Counter32
_WfMplsAtmSessOutboundInuseVcs_Object = MibTableColumn
wfMplsAtmSessOutboundInuseVcs = _WfMplsAtmSessOutboundInuseVcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 4, 1, 11),
    _WfMplsAtmSessOutboundInuseVcs_Type()
)
wfMplsAtmSessOutboundInuseVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmSessOutboundInuseVcs.setStatus("mandatory")
_WfMplsAtmVclTable_Object = MibTable
wfMplsAtmVclTable = _WfMplsAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5)
)
if mibBuilder.loadTexts:
    wfMplsAtmVclTable.setStatus("mandatory")
_WfMplsAtmVclEntry_Object = MibTableRow
wfMplsAtmVclEntry = _WfMplsAtmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1)
)
wfMplsAtmVclEntry.setIndexNames(
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmVclLineNumber"),
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmVclVpi"),
    (0, "Wellfleet-MPLS-MLM-MIB", "wfMplsAtmVclVci"),
)
if mibBuilder.loadTexts:
    wfMplsAtmVclEntry.setStatus("mandatory")
_WfMplsAtmVclLineNumber_Type = Integer32
_WfMplsAtmVclLineNumber_Object = MibTableColumn
wfMplsAtmVclLineNumber = _WfMplsAtmVclLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 1),
    _WfMplsAtmVclLineNumber_Type()
)
wfMplsAtmVclLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclLineNumber.setStatus("mandatory")
_WfMplsAtmVclVpi_Type = Integer32
_WfMplsAtmVclVpi_Object = MibTableColumn
wfMplsAtmVclVpi = _WfMplsAtmVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 2),
    _WfMplsAtmVclVpi_Type()
)
wfMplsAtmVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclVpi.setStatus("mandatory")
_WfMplsAtmVclVci_Type = Integer32
_WfMplsAtmVclVci_Object = MibTableColumn
wfMplsAtmVclVci = _WfMplsAtmVclVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 3),
    _WfMplsAtmVclVci_Type()
)
wfMplsAtmVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclVci.setStatus("mandatory")
_WfMplsAtmVclLdpIndex_Type = Integer32
_WfMplsAtmVclLdpIndex_Object = MibTableColumn
wfMplsAtmVclLdpIndex = _WfMplsAtmVclLdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 4),
    _WfMplsAtmVclLdpIndex_Type()
)
wfMplsAtmVclLdpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclLdpIndex.setStatus("mandatory")


class _WfMplsAtmVclDirection_Type(Integer32):
    """Custom type wfMplsAtmVclDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_WfMplsAtmVclDirection_Type.__name__ = "Integer32"
_WfMplsAtmVclDirection_Object = MibTableColumn
wfMplsAtmVclDirection = _WfMplsAtmVclDirection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 5),
    _WfMplsAtmVclDirection_Type()
)
wfMplsAtmVclDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclDirection.setStatus("mandatory")


class _WfMplsAtmVclState_Type(Integer32):
    """Custom type wfMplsAtmVclState based on Integer32"""
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
        *(("cleanup", 4),
          ("down", 1),
          ("init", 2),
          ("notpresent", 5),
          ("up", 3))
    )


_WfMplsAtmVclState_Type.__name__ = "Integer32"
_WfMplsAtmVclState_Object = MibTableColumn
wfMplsAtmVclState = _WfMplsAtmVclState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 6),
    _WfMplsAtmVclState_Type()
)
wfMplsAtmVclState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclState.setStatus("mandatory")


class _WfMplsAtmVclType_Type(Integer32):
    """Custom type wfMplsAtmVclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("lsp", 2),
          ("unknown", 3))
    )


_WfMplsAtmVclType_Type.__name__ = "Integer32"
_WfMplsAtmVclType_Object = MibTableColumn
wfMplsAtmVclType = _WfMplsAtmVclType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 7),
    _WfMplsAtmVclType_Type()
)
wfMplsAtmVclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclType.setStatus("mandatory")
_WfMplsAtmVclLastChange_Type = TimeTicks
_WfMplsAtmVclLastChange_Object = MibTableColumn
wfMplsAtmVclLastChange = _WfMplsAtmVclLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 8),
    _WfMplsAtmVclLastChange_Type()
)
wfMplsAtmVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclLastChange.setStatus("mandatory")


class _WfMplsAtmVclXmtPeakCellRate_Type(Integer32):
    """Custom type wfMplsAtmVclXmtPeakCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4716
        )
    )
    namedValues = NamedValues(
        ("default", 4716)
    )


_WfMplsAtmVclXmtPeakCellRate_Type.__name__ = "Integer32"
_WfMplsAtmVclXmtPeakCellRate_Object = MibTableColumn
wfMplsAtmVclXmtPeakCellRate = _WfMplsAtmVclXmtPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 9),
    _WfMplsAtmVclXmtPeakCellRate_Type()
)
wfMplsAtmVclXmtPeakCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclXmtPeakCellRate.setStatus("mandatory")


class _WfMplsAtmVclXmtSustainableCellRate_Type(Integer32):
    """Custom type wfMplsAtmVclXmtSustainableCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4716
        )
    )
    namedValues = NamedValues(
        ("default", 4716)
    )


_WfMplsAtmVclXmtSustainableCellRate_Type.__name__ = "Integer32"
_WfMplsAtmVclXmtSustainableCellRate_Object = MibTableColumn
wfMplsAtmVclXmtSustainableCellRate = _WfMplsAtmVclXmtSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 10),
    _WfMplsAtmVclXmtSustainableCellRate_Type()
)
wfMplsAtmVclXmtSustainableCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclXmtSustainableCellRate.setStatus("mandatory")


class _WfMplsAtmVclXmtBurstSize_Type(Integer32):
    """Custom type wfMplsAtmVclXmtBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("default", 40)
    )


_WfMplsAtmVclXmtBurstSize_Type.__name__ = "Integer32"
_WfMplsAtmVclXmtBurstSize_Object = MibTableColumn
wfMplsAtmVclXmtBurstSize = _WfMplsAtmVclXmtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 11),
    _WfMplsAtmVclXmtBurstSize_Type()
)
wfMplsAtmVclXmtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclXmtBurstSize.setStatus("mandatory")


class _WfMplsAtmVclXmtQosClass_Type(Integer32):
    """Custom type wfMplsAtmVclXmtQosClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_WfMplsAtmVclXmtQosClass_Type.__name__ = "Integer32"
_WfMplsAtmVclXmtQosClass_Object = MibTableColumn
wfMplsAtmVclXmtQosClass = _WfMplsAtmVclXmtQosClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 12),
    _WfMplsAtmVclXmtQosClass_Type()
)
wfMplsAtmVclXmtQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclXmtQosClass.setStatus("mandatory")


class _WfMplsAtmVclRcvPeakCellRate_Type(Integer32):
    """Custom type wfMplsAtmVclRcvPeakCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4716
        )
    )
    namedValues = NamedValues(
        ("default", 4716)
    )


_WfMplsAtmVclRcvPeakCellRate_Type.__name__ = "Integer32"
_WfMplsAtmVclRcvPeakCellRate_Object = MibTableColumn
wfMplsAtmVclRcvPeakCellRate = _WfMplsAtmVclRcvPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 13),
    _WfMplsAtmVclRcvPeakCellRate_Type()
)
wfMplsAtmVclRcvPeakCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclRcvPeakCellRate.setStatus("mandatory")


class _WfMplsAtmVclRcvSustainableCellRate_Type(Integer32):
    """Custom type wfMplsAtmVclRcvSustainableCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4716
        )
    )
    namedValues = NamedValues(
        ("default", 4716)
    )


_WfMplsAtmVclRcvSustainableCellRate_Type.__name__ = "Integer32"
_WfMplsAtmVclRcvSustainableCellRate_Object = MibTableColumn
wfMplsAtmVclRcvSustainableCellRate = _WfMplsAtmVclRcvSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 14),
    _WfMplsAtmVclRcvSustainableCellRate_Type()
)
wfMplsAtmVclRcvSustainableCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclRcvSustainableCellRate.setStatus("mandatory")


class _WfMplsAtmVclRcvBurstSize_Type(Integer32):
    """Custom type wfMplsAtmVclRcvBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("default", 40)
    )


_WfMplsAtmVclRcvBurstSize_Type.__name__ = "Integer32"
_WfMplsAtmVclRcvBurstSize_Object = MibTableColumn
wfMplsAtmVclRcvBurstSize = _WfMplsAtmVclRcvBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 15),
    _WfMplsAtmVclRcvBurstSize_Type()
)
wfMplsAtmVclRcvBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclRcvBurstSize.setStatus("mandatory")


class _WfMplsAtmVclRcvQosClass_Type(Integer32):
    """Custom type wfMplsAtmVclRcvQosClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_WfMplsAtmVclRcvQosClass_Type.__name__ = "Integer32"
_WfMplsAtmVclRcvQosClass_Object = MibTableColumn
wfMplsAtmVclRcvQosClass = _WfMplsAtmVclRcvQosClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 16),
    _WfMplsAtmVclRcvQosClass_Type()
)
wfMplsAtmVclRcvQosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclRcvQosClass.setStatus("mandatory")


class _WfMplsAtmVclAalType_Type(Integer32):
    """Custom type wfMplsAtmVclAalType based on Integer32"""
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
        *(("other", 4),
          ("type1", 1),
          ("type34", 2),
          ("type5", 3),
          ("unknown", 5))
    )


_WfMplsAtmVclAalType_Type.__name__ = "Integer32"
_WfMplsAtmVclAalType_Object = MibTableColumn
wfMplsAtmVclAalType = _WfMplsAtmVclAalType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 17),
    _WfMplsAtmVclAalType_Type()
)
wfMplsAtmVclAalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclAalType.setStatus("mandatory")


class _WfMplsAtmVclAalCpcsTransmitSduSize_Type(Integer32):
    """Custom type wfMplsAtmVclAalCpcsTransmitSduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsAtmVclAalCpcsTransmitSduSize_Type.__name__ = "Integer32"
_WfMplsAtmVclAalCpcsTransmitSduSize_Object = MibTableColumn
wfMplsAtmVclAalCpcsTransmitSduSize = _WfMplsAtmVclAalCpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 18),
    _WfMplsAtmVclAalCpcsTransmitSduSize_Type()
)
wfMplsAtmVclAalCpcsTransmitSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclAalCpcsTransmitSduSize.setStatus("mandatory")


class _WfMplsAtmVclAalCpcsReceiveSduSize_Type(Integer32):
    """Custom type wfMplsAtmVclAalCpcsReceiveSduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsAtmVclAalCpcsReceiveSduSize_Type.__name__ = "Integer32"
_WfMplsAtmVclAalCpcsReceiveSduSize_Object = MibTableColumn
wfMplsAtmVclAalCpcsReceiveSduSize = _WfMplsAtmVclAalCpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 19),
    _WfMplsAtmVclAalCpcsReceiveSduSize_Type()
)
wfMplsAtmVclAalCpcsReceiveSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclAalCpcsReceiveSduSize.setStatus("mandatory")


class _WfMplsAtmVclAalEncapsType_Type(Integer32):
    """Custom type wfMplsAtmVclAalEncapsType based on Integer32"""
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
        *(("llcencaps", 2),
          ("null", 3),
          ("other", 4),
          ("unknown", 1))
    )


_WfMplsAtmVclAalEncapsType_Type.__name__ = "Integer32"
_WfMplsAtmVclAalEncapsType_Object = MibTableColumn
wfMplsAtmVclAalEncapsType = _WfMplsAtmVclAalEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 20),
    _WfMplsAtmVclAalEncapsType_Type()
)
wfMplsAtmVclAalEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclAalEncapsType.setStatus("mandatory")


class _WfMplsAtmVclCongestionIndication_Type(Integer32):
    """Custom type wfMplsAtmVclCongestionIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WfMplsAtmVclCongestionIndication_Type.__name__ = "Integer32"
_WfMplsAtmVclCongestionIndication_Object = MibTableColumn
wfMplsAtmVclCongestionIndication = _WfMplsAtmVclCongestionIndication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 21),
    _WfMplsAtmVclCongestionIndication_Type()
)
wfMplsAtmVclCongestionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclCongestionIndication.setStatus("mandatory")


class _WfMplsAtmVclCellLossPriority_Type(Integer32):
    """Custom type wfMplsAtmVclCellLossPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WfMplsAtmVclCellLossPriority_Type.__name__ = "Integer32"
_WfMplsAtmVclCellLossPriority_Object = MibTableColumn
wfMplsAtmVclCellLossPriority = _WfMplsAtmVclCellLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 22),
    _WfMplsAtmVclCellLossPriority_Type()
)
wfMplsAtmVclCellLossPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclCellLossPriority.setStatus("mandatory")


class _WfMplsAtmVclXmtTagging_Type(Integer32):
    """Custom type wfMplsAtmVclXmtTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfMplsAtmVclXmtTagging_Type.__name__ = "Integer32"
_WfMplsAtmVclXmtTagging_Object = MibTableColumn
wfMplsAtmVclXmtTagging = _WfMplsAtmVclXmtTagging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 23),
    _WfMplsAtmVclXmtTagging_Type()
)
wfMplsAtmVclXmtTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclXmtTagging.setStatus("mandatory")


class _WfMplsAtmVclRcvTagging_Type(Integer32):
    """Custom type wfMplsAtmVclRcvTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfMplsAtmVclRcvTagging_Type.__name__ = "Integer32"
_WfMplsAtmVclRcvTagging_Object = MibTableColumn
wfMplsAtmVclRcvTagging = _WfMplsAtmVclRcvTagging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16, 1, 5, 1, 24),
    _WfMplsAtmVclRcvTagging_Type()
)
wfMplsAtmVclRcvTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsAtmVclRcvTagging.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MPLS-MLM-MIB",
    **{"wfMplsAtm": wfMplsAtm,
       "wfMplsAtmIfConfTable": wfMplsAtmIfConfTable,
       "wfMplsAtmIfConfEntry": wfMplsAtmIfConfEntry,
       "wfMplsAtmIfCreate": wfMplsAtmIfCreate,
       "wfMplsAtmIfAdminStatus": wfMplsAtmIfAdminStatus,
       "wfMplsAtmIfConfLineNumber": wfMplsAtmIfConfLineNumber,
       "wfMplsAtmIfDebugLogMask": wfMplsAtmIfDebugLogMask,
       "wfMplsAtmIfStatusTable": wfMplsAtmIfStatusTable,
       "wfMplsAtmIfStatusEntry": wfMplsAtmIfStatusEntry,
       "wfMplsAtmIfOperStatus": wfMplsAtmIfOperStatus,
       "wfMplsAtmIfStatusLineNumber": wfMplsAtmIfStatusLineNumber,
       "wfMplsAtmIfCircuit": wfMplsAtmIfCircuit,
       "wfMplsAtmIfTotalSess": wfMplsAtmIfTotalSess,
       "wfMplsAtmIfTotalVcs": wfMplsAtmIfTotalVcs,
       "wfMplsAtmIfAllocVcs": wfMplsAtmIfAllocVcs,
       "wfMplsAtmSessConfTable": wfMplsAtmSessConfTable,
       "wfMplsAtmSessConfEntry": wfMplsAtmSessConfEntry,
       "wfMplsAtmSessDelete": wfMplsAtmSessDelete,
       "wfMplsAtmSessAdminStatus": wfMplsAtmSessAdminStatus,
       "wfMplsAtmSessConfLineNumber": wfMplsAtmSessConfLineNumber,
       "wfMplsAtmSessConfIndex": wfMplsAtmSessConfIndex,
       "wfMplsAtmSessConfDefVclVpi": wfMplsAtmSessConfDefVclVpi,
       "wfMplsAtmSessConfDefVclVci": wfMplsAtmSessConfDefVclVci,
       "wfMplsAtmSessConfVcRangeVpi": wfMplsAtmSessConfVcRangeVpi,
       "wfMplsAtmSessConfVcRangeMinVci": wfMplsAtmSessConfVcRangeMinVci,
       "wfMplsAtmSessConfVcRangeMaxVci": wfMplsAtmSessConfVcRangeMaxVci,
       "wfMplsAtmSessDefVclXmtPeakCellRate": wfMplsAtmSessDefVclXmtPeakCellRate,
       "wfMplsAtmSessDefVclXmtSustainableCellRate": wfMplsAtmSessDefVclXmtSustainableCellRate,
       "wfMplsAtmSessDefVclXmtBurstSize": wfMplsAtmSessDefVclXmtBurstSize,
       "wfMplsAtmSessDefVclXmtQosClass": wfMplsAtmSessDefVclXmtQosClass,
       "wfMplsAtmSessDefVclRcvPeakCellRate": wfMplsAtmSessDefVclRcvPeakCellRate,
       "wfMplsAtmSessDefVclRcvSustainableCellRate": wfMplsAtmSessDefVclRcvSustainableCellRate,
       "wfMplsAtmSessDefVclRcvBurstSize": wfMplsAtmSessDefVclRcvBurstSize,
       "wfMplsAtmSessDefVclRcvQosClass": wfMplsAtmSessDefVclRcvQosClass,
       "wfMplsAtmSessDefVclAalType": wfMplsAtmSessDefVclAalType,
       "wfMplsAtmSessDefVclAalCpcsTransmitSduSize": wfMplsAtmSessDefVclAalCpcsTransmitSduSize,
       "wfMplsAtmSessDefVclAalCpcsReceiveSduSize": wfMplsAtmSessDefVclAalCpcsReceiveSduSize,
       "wfMplsAtmSessDefVclAalEncapsType": wfMplsAtmSessDefVclAalEncapsType,
       "wfMplsAtmSessDefVclCongestionIndication": wfMplsAtmSessDefVclCongestionIndication,
       "wfMplsAtmSessDefVclCellLossPriority": wfMplsAtmSessDefVclCellLossPriority,
       "wfMplsAtmSessDefVclXmtTagging": wfMplsAtmSessDefVclXmtTagging,
       "wfMplsAtmSessDefVclRcvTagging": wfMplsAtmSessDefVclRcvTagging,
       "wfMplsAtmSessStatusTable": wfMplsAtmSessStatusTable,
       "wfMplsAtmSessStatusEntry": wfMplsAtmSessStatusEntry,
       "wfMplsAtmSessOperStatus": wfMplsAtmSessOperStatus,
       "wfMplsAtmSessStatusLineNumber": wfMplsAtmSessStatusLineNumber,
       "wfMplsAtmSessStatusIndex": wfMplsAtmSessStatusIndex,
       "wfMplsAtmSessActualVcRangeVpi": wfMplsAtmSessActualVcRangeVpi,
       "wfMplsAtmSessActualVcRangeMinVci": wfMplsAtmSessActualVcRangeMinVci,
       "wfMplsAtmSessActualVcRangeMaxVci": wfMplsAtmSessActualVcRangeMaxVci,
       "wfMplsAtmSessNegotiatedVcRangeVpi": wfMplsAtmSessNegotiatedVcRangeVpi,
       "wfMplsAtmSessNegotiatedVcRangeMinVci": wfMplsAtmSessNegotiatedVcRangeMinVci,
       "wfMplsAtmSessNegotiatedVcRangeMaxVci": wfMplsAtmSessNegotiatedVcRangeMaxVci,
       "wfMplsAtmSessInboundInuseVcs": wfMplsAtmSessInboundInuseVcs,
       "wfMplsAtmSessOutboundInuseVcs": wfMplsAtmSessOutboundInuseVcs,
       "wfMplsAtmVclTable": wfMplsAtmVclTable,
       "wfMplsAtmVclEntry": wfMplsAtmVclEntry,
       "wfMplsAtmVclLineNumber": wfMplsAtmVclLineNumber,
       "wfMplsAtmVclVpi": wfMplsAtmVclVpi,
       "wfMplsAtmVclVci": wfMplsAtmVclVci,
       "wfMplsAtmVclLdpIndex": wfMplsAtmVclLdpIndex,
       "wfMplsAtmVclDirection": wfMplsAtmVclDirection,
       "wfMplsAtmVclState": wfMplsAtmVclState,
       "wfMplsAtmVclType": wfMplsAtmVclType,
       "wfMplsAtmVclLastChange": wfMplsAtmVclLastChange,
       "wfMplsAtmVclXmtPeakCellRate": wfMplsAtmVclXmtPeakCellRate,
       "wfMplsAtmVclXmtSustainableCellRate": wfMplsAtmVclXmtSustainableCellRate,
       "wfMplsAtmVclXmtBurstSize": wfMplsAtmVclXmtBurstSize,
       "wfMplsAtmVclXmtQosClass": wfMplsAtmVclXmtQosClass,
       "wfMplsAtmVclRcvPeakCellRate": wfMplsAtmVclRcvPeakCellRate,
       "wfMplsAtmVclRcvSustainableCellRate": wfMplsAtmVclRcvSustainableCellRate,
       "wfMplsAtmVclRcvBurstSize": wfMplsAtmVclRcvBurstSize,
       "wfMplsAtmVclRcvQosClass": wfMplsAtmVclRcvQosClass,
       "wfMplsAtmVclAalType": wfMplsAtmVclAalType,
       "wfMplsAtmVclAalCpcsTransmitSduSize": wfMplsAtmVclAalCpcsTransmitSduSize,
       "wfMplsAtmVclAalCpcsReceiveSduSize": wfMplsAtmVclAalCpcsReceiveSduSize,
       "wfMplsAtmVclAalEncapsType": wfMplsAtmVclAalEncapsType,
       "wfMplsAtmVclCongestionIndication": wfMplsAtmVclCongestionIndication,
       "wfMplsAtmVclCellLossPriority": wfMplsAtmVclCellLossPriority,
       "wfMplsAtmVclXmtTagging": wfMplsAtmVclXmtTagging,
       "wfMplsAtmVclRcvTagging": wfMplsAtmVclRcvTagging}
)
