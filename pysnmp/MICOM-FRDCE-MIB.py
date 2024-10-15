# SNMP MIB module (MICOM-FRDCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-FRDCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:41 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,
 mcmSysIfExtModule,
 mcmSysIfExtPPA) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay",
    "mcmSysIfExtModule",
    "mcmSysIfExtPPA")

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
 NotificationType,
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
    "NotificationType",
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

_Micom_frdce_ObjectIdentity = ObjectIdentity
micom_frdce = _Micom_frdce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9)
)
_Frdce_configuration_ObjectIdentity = ObjectIdentity
frdce_configuration = _Frdce_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1)
)
_McmFrConnectTable_Object = MibTable
mcmFrConnectTable = _McmFrConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1)
)
if mibBuilder.loadTexts:
    mcmFrConnectTable.setStatus("mandatory")
_McmFrConnectEntry_Object = MibTableRow
mcmFrConnectEntry = _McmFrConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1)
)
mcmFrConnectEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "mcmFrConnectIfIndexLocal"),
    (0, "MICOM-FRDCE-MIB", "mcmFrConnectDLCILocal"),
)
if mibBuilder.loadTexts:
    mcmFrConnectEntry.setStatus("mandatory")


class _McmFrConnectIfIndexLocal_Type(Integer32):
    """Custom type mcmFrConnectIfIndexLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrConnectIfIndexLocal_Type.__name__ = "Integer32"
_McmFrConnectIfIndexLocal_Object = MibTableColumn
mcmFrConnectIfIndexLocal = _McmFrConnectIfIndexLocal_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 1),
    _McmFrConnectIfIndexLocal_Type()
)
mcmFrConnectIfIndexLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectIfIndexLocal.setStatus("mandatory")


class _McmFrConnectDLCILocal_Type(Integer32):
    """Custom type mcmFrConnectDLCILocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrConnectDLCILocal_Type.__name__ = "Integer32"
_McmFrConnectDLCILocal_Object = MibTableColumn
mcmFrConnectDLCILocal = _McmFrConnectDLCILocal_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 2),
    _McmFrConnectDLCILocal_Type()
)
mcmFrConnectDLCILocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectDLCILocal.setStatus("mandatory")


class _McmFrConnectConnectId_Type(Integer32):
    """Custom type mcmFrConnectConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmFrConnectConnectId_Type.__name__ = "Integer32"
_McmFrConnectConnectId_Object = MibTableColumn
mcmFrConnectConnectId = _McmFrConnectConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 3),
    _McmFrConnectConnectId_Type()
)
mcmFrConnectConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectConnectId.setStatus("mandatory")


class _McmFrConnectIfIndexRemote_Type(Integer32):
    """Custom type mcmFrConnectIfIndexRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrConnectIfIndexRemote_Type.__name__ = "Integer32"
_McmFrConnectIfIndexRemote_Object = MibTableColumn
mcmFrConnectIfIndexRemote = _McmFrConnectIfIndexRemote_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 4),
    _McmFrConnectIfIndexRemote_Type()
)
mcmFrConnectIfIndexRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectIfIndexRemote.setStatus("obsolete")


class _McmFrConnectDLCIRemote_Type(Integer32):
    """Custom type mcmFrConnectDLCIRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrConnectDLCIRemote_Type.__name__ = "Integer32"
_McmFrConnectDLCIRemote_Object = MibTableColumn
mcmFrConnectDLCIRemote = _McmFrConnectDLCIRemote_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 5),
    _McmFrConnectDLCIRemote_Type()
)
mcmFrConnectDLCIRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectDLCIRemote.setStatus("mandatory")


class _McmFrConnectIfIndexSVC_Type(Integer32):
    """Custom type mcmFrConnectIfIndexSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrConnectIfIndexSVC_Type.__name__ = "Integer32"
_McmFrConnectIfIndexSVC_Object = MibTableColumn
mcmFrConnectIfIndexSVC = _McmFrConnectIfIndexSVC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 6),
    _McmFrConnectIfIndexSVC_Type()
)
mcmFrConnectIfIndexSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectIfIndexSVC.setStatus("mandatory")


class _McmFrConnectDNARemote_Type(DisplayString):
    """Custom type mcmFrConnectDNARemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrConnectDNARemote_Type.__name__ = "DisplayString"
_McmFrConnectDNARemote_Object = MibTableColumn
mcmFrConnectDNARemote = _McmFrConnectDNARemote_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 7),
    _McmFrConnectDNARemote_Type()
)
mcmFrConnectDNARemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectDNARemote.setStatus("mandatory")


class _McmFrConnectSVCDLCI_Type(Integer32):
    """Custom type mcmFrConnectSVCDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrConnectSVCDLCI_Type.__name__ = "Integer32"
_McmFrConnectSVCDLCI_Object = MibTableColumn
mcmFrConnectSVCDLCI = _McmFrConnectSVCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 8),
    _McmFrConnectSVCDLCI_Type()
)
mcmFrConnectSVCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectSVCDLCI.setStatus("mandatory")


class _McmFrConnectDCEPVCLMIState_Type(Integer32):
    """Custom type mcmFrConnectDCEPVCLMIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_McmFrConnectDCEPVCLMIState_Type.__name__ = "Integer32"
_McmFrConnectDCEPVCLMIState_Object = MibTableColumn
mcmFrConnectDCEPVCLMIState = _McmFrConnectDCEPVCLMIState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 9),
    _McmFrConnectDCEPVCLMIState_Type()
)
mcmFrConnectDCEPVCLMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectDCEPVCLMIState.setStatus("mandatory")


class _McmFrConnectSVCState_Type(Integer32):
    """Custom type mcmFrConnectSVCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_McmFrConnectSVCState_Type.__name__ = "Integer32"
_McmFrConnectSVCState_Object = MibTableColumn
mcmFrConnectSVCState = _McmFrConnectSVCState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 10),
    _McmFrConnectSVCState_Type()
)
mcmFrConnectSVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectSVCState.setStatus("mandatory")


class _McmFrConnectConnType_Type(Integer32):
    """Custom type mcmFrConnectConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_McmFrConnectConnType_Type.__name__ = "Integer32"
_McmFrConnectConnType_Object = MibTableColumn
mcmFrConnectConnType = _McmFrConnectConnType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 11),
    _McmFrConnectConnType_Type()
)
mcmFrConnectConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectConnType.setStatus("mandatory")
_McmFrConnectLastChange_Type = TimeTicks
_McmFrConnectLastChange_Object = MibTableColumn
mcmFrConnectLastChange = _McmFrConnectLastChange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 12),
    _McmFrConnectLastChange_Type()
)
mcmFrConnectLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectLastChange.setStatus("mandatory")


class _McmFrConnectDisconnectReason_Type(Integer32):
    """Custom type mcmFrConnectDisconnectReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("local-FR-CORE-error", 9),
          ("local-PVC-LMI-is-down", 3),
          ("local-PVC-physical-link-is-down", 2),
          ("local-SVC-LMI-is-down", 7),
          ("local-SVC-is-down", 8),
          ("no-reason", 1),
          ("remote-PVC-LMI-is-down", 5),
          ("remote-PVC-physical-link-is-down", 4),
          ("remote-signaled", 6))
    )


_McmFrConnectDisconnectReason_Type.__name__ = "Integer32"
_McmFrConnectDisconnectReason_Object = MibTableColumn
mcmFrConnectDisconnectReason = _McmFrConnectDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 13),
    _McmFrConnectDisconnectReason_Type()
)
mcmFrConnectDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectDisconnectReason.setStatus("mandatory")


class _McmFrConnectSwitchType_Type(Integer32):
    """Custom type mcmFrConnectSwitchType based on Integer32"""
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
        *(("cbr", 3),
          ("frdce", 1),
          ("htds", 2),
          ("sna-sdlc", 5),
          ("x25", 4))
    )


_McmFrConnectSwitchType_Type.__name__ = "Integer32"
_McmFrConnectSwitchType_Object = MibTableColumn
mcmFrConnectSwitchType = _McmFrConnectSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 1, 1, 14),
    _McmFrConnectSwitchType_Type()
)
mcmFrConnectSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectSwitchType.setStatus("mandatory")
_McmFrConnSVCTable_Object = MibTable
mcmFrConnSVCTable = _McmFrConnSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2)
)
if mibBuilder.loadTexts:
    mcmFrConnSVCTable.setStatus("obsolete")
_McmFrConnSVCEntry_Object = MibTableRow
mcmFrConnSVCEntry = _McmFrConnSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1)
)
mcmFrConnSVCEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "mcmFrConnSVCIfIndex"),
    (0, "MICOM-FRDCE-MIB", "mcmFrConnSVCConnectId"),
)
if mibBuilder.loadTexts:
    mcmFrConnSVCEntry.setStatus("obsolete")


class _McmFrConnSVCIfIndex_Type(Integer32):
    """Custom type mcmFrConnSVCIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrConnSVCIfIndex_Type.__name__ = "Integer32"
_McmFrConnSVCIfIndex_Object = MibTableColumn
mcmFrConnSVCIfIndex = _McmFrConnSVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 1),
    _McmFrConnSVCIfIndex_Type()
)
mcmFrConnSVCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCIfIndex.setStatus("obsolete")


class _McmFrConnSVCConnectId_Type(Integer32):
    """Custom type mcmFrConnSVCConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmFrConnSVCConnectId_Type.__name__ = "Integer32"
_McmFrConnSVCConnectId_Object = MibTableColumn
mcmFrConnSVCConnectId = _McmFrConnSVCConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 2),
    _McmFrConnSVCConnectId_Type()
)
mcmFrConnSVCConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCConnectId.setStatus("obsolete")


class _McmFrConnSVCDNA_Type(DisplayString):
    """Custom type mcmFrConnSVCDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 30),
    )


_McmFrConnSVCDNA_Type.__name__ = "DisplayString"
_McmFrConnSVCDNA_Object = MibTableColumn
mcmFrConnSVCDNA = _McmFrConnSVCDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 3),
    _McmFrConnSVCDNA_Type()
)
mcmFrConnSVCDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCDNA.setStatus("obsolete")


class _McmFrConnSVCDLCI_Type(Integer32):
    """Custom type mcmFrConnSVCDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrConnSVCDLCI_Type.__name__ = "Integer32"
_McmFrConnSVCDLCI_Object = MibTableColumn
mcmFrConnSVCDLCI = _McmFrConnSVCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 4),
    _McmFrConnSVCDLCI_Type()
)
mcmFrConnSVCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCDLCI.setStatus("obsolete")


class _McmFrConnSVCMaxTxSize_Type(Integer32):
    """Custom type mcmFrConnSVCMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrConnSVCMaxTxSize_Type.__name__ = "Integer32"
_McmFrConnSVCMaxTxSize_Object = MibTableColumn
mcmFrConnSVCMaxTxSize = _McmFrConnSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 5),
    _McmFrConnSVCMaxTxSize_Type()
)
mcmFrConnSVCMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMaxTxSize.setStatus("obsolete")


class _McmFrConnSVCMaxRxSize_Type(Integer32):
    """Custom type mcmFrConnSVCMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrConnSVCMaxRxSize_Type.__name__ = "Integer32"
_McmFrConnSVCMaxRxSize_Object = MibTableColumn
mcmFrConnSVCMaxRxSize = _McmFrConnSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 6),
    _McmFrConnSVCMaxRxSize_Type()
)
mcmFrConnSVCMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMaxRxSize.setStatus("obsolete")


class _McmFrConnSVCMinTxThroughput_Type(Integer32):
    """Custom type mcmFrConnSVCMinTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCMinTxThroughput_Type.__name__ = "Integer32"
_McmFrConnSVCMinTxThroughput_Object = MibTableColumn
mcmFrConnSVCMinTxThroughput = _McmFrConnSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 7),
    _McmFrConnSVCMinTxThroughput_Type()
)
mcmFrConnSVCMinTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMinTxThroughput.setStatus("obsolete")


class _McmFrConnSVCMinRxThroughput_Type(Integer32):
    """Custom type mcmFrConnSVCMinRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCMinRxThroughput_Type.__name__ = "Integer32"
_McmFrConnSVCMinRxThroughput_Object = MibTableColumn
mcmFrConnSVCMinRxThroughput = _McmFrConnSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 8),
    _McmFrConnSVCMinRxThroughput_Type()
)
mcmFrConnSVCMinRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMinRxThroughput.setStatus("obsolete")


class _McmFrConnSVCMaxTxThroughput_Type(Integer32):
    """Custom type mcmFrConnSVCMaxTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCMaxTxThroughput_Type.__name__ = "Integer32"
_McmFrConnSVCMaxTxThroughput_Object = MibTableColumn
mcmFrConnSVCMaxTxThroughput = _McmFrConnSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 9),
    _McmFrConnSVCMaxTxThroughput_Type()
)
mcmFrConnSVCMaxTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMaxTxThroughput.setStatus("obsolete")


class _McmFrConnSVCMaxRxThroughput_Type(Integer32):
    """Custom type mcmFrConnSVCMaxRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCMaxRxThroughput_Type.__name__ = "Integer32"
_McmFrConnSVCMaxRxThroughput_Object = MibTableColumn
mcmFrConnSVCMaxRxThroughput = _McmFrConnSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 10),
    _McmFrConnSVCMaxRxThroughput_Type()
)
mcmFrConnSVCMaxRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMaxRxThroughput.setStatus("obsolete")


class _McmFrConnSVCMaxTxBurstSize_Type(Integer32):
    """Custom type mcmFrConnSVCMaxTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCMaxTxBurstSize_Type.__name__ = "Integer32"
_McmFrConnSVCMaxTxBurstSize_Object = MibTableColumn
mcmFrConnSVCMaxTxBurstSize = _McmFrConnSVCMaxTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 11),
    _McmFrConnSVCMaxTxBurstSize_Type()
)
mcmFrConnSVCMaxTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMaxTxBurstSize.setStatus("obsolete")


class _McmFrConnSVCMaxRxBurstSize_Type(Integer32):
    """Custom type mcmFrConnSVCMaxRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCMaxRxBurstSize_Type.__name__ = "Integer32"
_McmFrConnSVCMaxRxBurstSize_Object = MibTableColumn
mcmFrConnSVCMaxRxBurstSize = _McmFrConnSVCMaxRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 12),
    _McmFrConnSVCMaxRxBurstSize_Type()
)
mcmFrConnSVCMaxRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCMaxRxBurstSize.setStatus("obsolete")


class _McmFrConnSVCExcessTxBurstSize_Type(Integer32):
    """Custom type mcmFrConnSVCExcessTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_McmFrConnSVCExcessTxBurstSize_Object = MibTableColumn
mcmFrConnSVCExcessTxBurstSize = _McmFrConnSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 13),
    _McmFrConnSVCExcessTxBurstSize_Type()
)
mcmFrConnSVCExcessTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCExcessTxBurstSize.setStatus("obsolete")


class _McmFrConnSVCExcessRxBurstSize_Type(Integer32):
    """Custom type mcmFrConnSVCExcessRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrConnSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_McmFrConnSVCExcessRxBurstSize_Object = MibTableColumn
mcmFrConnSVCExcessRxBurstSize = _McmFrConnSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 14),
    _McmFrConnSVCExcessRxBurstSize_Type()
)
mcmFrConnSVCExcessRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCExcessRxBurstSize.setStatus("obsolete")


class _McmFrConnSVCTransferPriority_Type(Integer32):
    """Custom type mcmFrConnSVCTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmFrConnSVCTransferPriority_Type.__name__ = "Integer32"
_McmFrConnSVCTransferPriority_Object = MibTableColumn
mcmFrConnSVCTransferPriority = _McmFrConnSVCTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 15),
    _McmFrConnSVCTransferPriority_Type()
)
mcmFrConnSVCTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCTransferPriority.setStatus("obsolete")


class _McmFrConnSVCReasonForDisconnect_Type(Integer32):
    """Custom type mcmFrConnSVCReasonForDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              18,
              21,
              30,
              34,
              44,
              47,
              81,
              96,
              97,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("invalid-call-reference", 81),
          ("invalid-element", 100),
          ("invalid-message-for-state", 101),
          ("message-type-unknown", 97),
          ("missing-element", 96),
          ("no-DLCI-available", 34),
          ("no-user-present-in-call", 18),
          ("remote-PVC-already-connected-ie-busy", 17),
          ("remote-PVC-down-ie-unavailable", 21),
          ("resource-unavailable", 47),
          ("response-to-status-inquiry", 30),
          ("specified-DLCI-unavailable", 44),
          ("the-PVC-does-not-exist-ie-unassigned", 1),
          ("timer-recovery", 102))
    )


_McmFrConnSVCReasonForDisconnect_Type.__name__ = "Integer32"
_McmFrConnSVCReasonForDisconnect_Object = MibTableColumn
mcmFrConnSVCReasonForDisconnect = _McmFrConnSVCReasonForDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 2, 1, 16),
    _McmFrConnSVCReasonForDisconnect_Type()
)
mcmFrConnSVCReasonForDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnSVCReasonForDisconnect.setStatus("obsolete")
_McmFrServiceParamTable_Object = MibTable
mcmFrServiceParamTable = _McmFrServiceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3)
)
if mibBuilder.loadTexts:
    mcmFrServiceParamTable.setStatus("mandatory")
_McmFrServiceParamEntry_Object = MibTableRow
mcmFrServiceParamEntry = _McmFrServiceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1)
)
mcmFrServiceParamEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "mcmFrServiceParamIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrServiceParamEntry.setStatus("mandatory")


class _McmFrServiceParamIfIndex_Type(Integer32):
    """Custom type mcmFrServiceParamIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrServiceParamIfIndex_Type.__name__ = "Integer32"
_McmFrServiceParamIfIndex_Object = MibTableColumn
mcmFrServiceParamIfIndex = _McmFrServiceParamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 1),
    _McmFrServiceParamIfIndex_Type()
)
mcmFrServiceParamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamIfIndex.setStatus("mandatory")


class _McmFrServiceParamFlowControl_Type(Integer32):
    """Custom type mcmFrServiceParamFlowControl based on Integer32"""
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


_McmFrServiceParamFlowControl_Type.__name__ = "Integer32"
_McmFrServiceParamFlowControl_Object = MibTableColumn
mcmFrServiceParamFlowControl = _McmFrServiceParamFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 2),
    _McmFrServiceParamFlowControl_Type()
)
mcmFrServiceParamFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamFlowControl.setStatus("mandatory")
_McmFrServiceParamDelta_Type = Integer32
_McmFrServiceParamDelta_Object = MibTableColumn
mcmFrServiceParamDelta = _McmFrServiceParamDelta_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 3),
    _McmFrServiceParamDelta_Type()
)
mcmFrServiceParamDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamDelta.setStatus("mandatory")
_McmFrServiceParamConsecutiveFrames_Type = Integer32
_McmFrServiceParamConsecutiveFrames_Object = MibTableColumn
mcmFrServiceParamConsecutiveFrames = _McmFrServiceParamConsecutiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 4),
    _McmFrServiceParamConsecutiveFrames_Type()
)
mcmFrServiceParamConsecutiveFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamConsecutiveFrames.setStatus("mandatory")


class _McmFrServiceParamRateEnf_Type(Integer32):
    """Custom type mcmFrServiceParamRateEnf based on Integer32"""
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


_McmFrServiceParamRateEnf_Type.__name__ = "Integer32"
_McmFrServiceParamRateEnf_Object = MibTableColumn
mcmFrServiceParamRateEnf = _McmFrServiceParamRateEnf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 5),
    _McmFrServiceParamRateEnf_Type()
)
mcmFrServiceParamRateEnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamRateEnf.setStatus("mandatory")


class _McmFrServiceParamTxMTU_Type(Integer32):
    """Custom type mcmFrServiceParamTxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_McmFrServiceParamTxMTU_Type.__name__ = "Integer32"
_McmFrServiceParamTxMTU_Object = MibTableColumn
mcmFrServiceParamTxMTU = _McmFrServiceParamTxMTU_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 6),
    _McmFrServiceParamTxMTU_Type()
)
mcmFrServiceParamTxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamTxMTU.setStatus("mandatory")


class _McmFrServiceParamRxMTU_Type(Integer32):
    """Custom type mcmFrServiceParamRxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_McmFrServiceParamRxMTU_Type.__name__ = "Integer32"
_McmFrServiceParamRxMTU_Object = MibTableColumn
mcmFrServiceParamRxMTU = _McmFrServiceParamRxMTU_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 7),
    _McmFrServiceParamRxMTU_Type()
)
mcmFrServiceParamRxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamRxMTU.setStatus("mandatory")


class _McmFrServiceParamTxBc_Type(Integer32):
    """Custom type mcmFrServiceParamTxBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrServiceParamTxBc_Type.__name__ = "Integer32"
_McmFrServiceParamTxBc_Object = MibTableColumn
mcmFrServiceParamTxBc = _McmFrServiceParamTxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 8),
    _McmFrServiceParamTxBc_Type()
)
mcmFrServiceParamTxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamTxBc.setStatus("mandatory")


class _McmFrServiceParamRxBc_Type(Integer32):
    """Custom type mcmFrServiceParamRxBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrServiceParamRxBc_Type.__name__ = "Integer32"
_McmFrServiceParamRxBc_Object = MibTableColumn
mcmFrServiceParamRxBc = _McmFrServiceParamRxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 9),
    _McmFrServiceParamRxBc_Type()
)
mcmFrServiceParamRxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamRxBc.setStatus("mandatory")


class _McmFrServiceParamTxBe_Type(Integer32):
    """Custom type mcmFrServiceParamTxBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrServiceParamTxBe_Type.__name__ = "Integer32"
_McmFrServiceParamTxBe_Object = MibTableColumn
mcmFrServiceParamTxBe = _McmFrServiceParamTxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 10),
    _McmFrServiceParamTxBe_Type()
)
mcmFrServiceParamTxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamTxBe.setStatus("mandatory")


class _McmFrServiceParamRxBe_Type(Integer32):
    """Custom type mcmFrServiceParamRxBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrServiceParamRxBe_Type.__name__ = "Integer32"
_McmFrServiceParamRxBe_Object = MibTableColumn
mcmFrServiceParamRxBe = _McmFrServiceParamRxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 11),
    _McmFrServiceParamRxBe_Type()
)
mcmFrServiceParamRxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamRxBe.setStatus("mandatory")


class _McmFrServiceParamTxThroughput_Type(Integer32):
    """Custom type mcmFrServiceParamTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrServiceParamTxThroughput_Type.__name__ = "Integer32"
_McmFrServiceParamTxThroughput_Object = MibTableColumn
mcmFrServiceParamTxThroughput = _McmFrServiceParamTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 12),
    _McmFrServiceParamTxThroughput_Type()
)
mcmFrServiceParamTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamTxThroughput.setStatus("mandatory")


class _McmFrServiceParamRxThroughput_Type(Integer32):
    """Custom type mcmFrServiceParamRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrServiceParamRxThroughput_Type.__name__ = "Integer32"
_McmFrServiceParamRxThroughput_Object = MibTableColumn
mcmFrServiceParamRxThroughput = _McmFrServiceParamRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 13),
    _McmFrServiceParamRxThroughput_Type()
)
mcmFrServiceParamRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamRxThroughput.setStatus("mandatory")


class _McmFrServiceParamPVCLMIStatus_Type(Integer32):
    """Custom type mcmFrServiceParamPVCLMIStatus based on Integer32"""
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


_McmFrServiceParamPVCLMIStatus_Type.__name__ = "Integer32"
_McmFrServiceParamPVCLMIStatus_Object = MibTableColumn
mcmFrServiceParamPVCLMIStatus = _McmFrServiceParamPVCLMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 14),
    _McmFrServiceParamPVCLMIStatus_Type()
)
mcmFrServiceParamPVCLMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamPVCLMIStatus.setStatus("mandatory")


class _McmFrServiceParamSVCLMIStatus_Type(Integer32):
    """Custom type mcmFrServiceParamSVCLMIStatus based on Integer32"""
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


_McmFrServiceParamSVCLMIStatus_Type.__name__ = "Integer32"
_McmFrServiceParamSVCLMIStatus_Object = MibTableColumn
mcmFrServiceParamSVCLMIStatus = _McmFrServiceParamSVCLMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 3, 1, 15),
    _McmFrServiceParamSVCLMIStatus_Type()
)
mcmFrServiceParamSVCLMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrServiceParamSVCLMIStatus.setStatus("mandatory")
_NvmFrConnectTable_Object = MibTable
nvmFrConnectTable = _NvmFrConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4)
)
if mibBuilder.loadTexts:
    nvmFrConnectTable.setStatus("mandatory")
_NvmFrConnectEntry_Object = MibTableRow
nvmFrConnectEntry = _NvmFrConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1)
)
nvmFrConnectEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "nvmFrConnectIfIndexLocal"),
    (0, "MICOM-FRDCE-MIB", "nvmFrConnectDLCILocal"),
)
if mibBuilder.loadTexts:
    nvmFrConnectEntry.setStatus("mandatory")


class _NvmFrConnectIfIndexLocal_Type(Integer32):
    """Custom type nvmFrConnectIfIndexLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrConnectIfIndexLocal_Type.__name__ = "Integer32"
_NvmFrConnectIfIndexLocal_Object = MibTableColumn
nvmFrConnectIfIndexLocal = _NvmFrConnectIfIndexLocal_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 1),
    _NvmFrConnectIfIndexLocal_Type()
)
nvmFrConnectIfIndexLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnectIfIndexLocal.setStatus("mandatory")


class _NvmFrConnectDLCILocal_Type(Integer32):
    """Custom type nvmFrConnectDLCILocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NvmFrConnectDLCILocal_Type.__name__ = "Integer32"
_NvmFrConnectDLCILocal_Object = MibTableColumn
nvmFrConnectDLCILocal = _NvmFrConnectDLCILocal_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 2),
    _NvmFrConnectDLCILocal_Type()
)
nvmFrConnectDLCILocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnectDLCILocal.setStatus("mandatory")


class _NvmFrConnectConnectId_Type(Integer32):
    """Custom type nvmFrConnectConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmFrConnectConnectId_Type.__name__ = "Integer32"
_NvmFrConnectConnectId_Object = MibTableColumn
nvmFrConnectConnectId = _NvmFrConnectConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 3),
    _NvmFrConnectConnectId_Type()
)
nvmFrConnectConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnectConnectId.setStatus("mandatory")


class _NvmFrConnectIfIndexRemote_Type(Integer32):
    """Custom type nvmFrConnectIfIndexRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrConnectIfIndexRemote_Type.__name__ = "Integer32"
_NvmFrConnectIfIndexRemote_Object = MibTableColumn
nvmFrConnectIfIndexRemote = _NvmFrConnectIfIndexRemote_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 4),
    _NvmFrConnectIfIndexRemote_Type()
)
nvmFrConnectIfIndexRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectIfIndexRemote.setStatus("obsolete")


class _NvmFrConnectDLCIRemote_Type(Integer32):
    """Custom type nvmFrConnectDLCIRemote based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NvmFrConnectDLCIRemote_Type.__name__ = "Integer32"
_NvmFrConnectDLCIRemote_Object = MibTableColumn
nvmFrConnectDLCIRemote = _NvmFrConnectDLCIRemote_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 5),
    _NvmFrConnectDLCIRemote_Type()
)
nvmFrConnectDLCIRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectDLCIRemote.setStatus("mandatory")


class _NvmFrConnectIfIndexSVC_Type(Integer32):
    """Custom type nvmFrConnectIfIndexSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrConnectIfIndexSVC_Type.__name__ = "Integer32"
_NvmFrConnectIfIndexSVC_Object = MibTableColumn
nvmFrConnectIfIndexSVC = _NvmFrConnectIfIndexSVC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 6),
    _NvmFrConnectIfIndexSVC_Type()
)
nvmFrConnectIfIndexSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectIfIndexSVC.setStatus("obsolete")


class _NvmFrConnectDNARemote_Type(DisplayString):
    """Custom type nvmFrConnectDNARemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmFrConnectDNARemote_Type.__name__ = "DisplayString"
_NvmFrConnectDNARemote_Object = MibTableColumn
nvmFrConnectDNARemote = _NvmFrConnectDNARemote_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 7),
    _NvmFrConnectDNARemote_Type()
)
nvmFrConnectDNARemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectDNARemote.setStatus("mandatory")


class _NvmFrConnectConnType_Type(Integer32):
    """Custom type nvmFrConnectConnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_NvmFrConnectConnType_Type.__name__ = "Integer32"
_NvmFrConnectConnType_Object = MibTableColumn
nvmFrConnectConnType = _NvmFrConnectConnType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 8),
    _NvmFrConnectConnType_Type()
)
nvmFrConnectConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectConnType.setStatus("mandatory")


class _NvmFrConnectRowStatus_Type(Integer32):
    """Custom type nvmFrConnectRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_NvmFrConnectRowStatus_Type.__name__ = "Integer32"
_NvmFrConnectRowStatus_Object = MibTableColumn
nvmFrConnectRowStatus = _NvmFrConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 9),
    _NvmFrConnectRowStatus_Type()
)
nvmFrConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectRowStatus.setStatus("mandatory")


class _NvmFrConnectSwitchType_Type(Integer32):
    """Custom type nvmFrConnectSwitchType based on Integer32"""
    defaultValue = 1

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
        *(("cbr", 3),
          ("frdce", 1),
          ("htds", 2),
          ("sna-sdlc", 5),
          ("x25", 4))
    )


_NvmFrConnectSwitchType_Type.__name__ = "Integer32"
_NvmFrConnectSwitchType_Object = MibTableColumn
nvmFrConnectSwitchType = _NvmFrConnectSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 4, 1, 10),
    _NvmFrConnectSwitchType_Type()
)
nvmFrConnectSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnectSwitchType.setStatus("mandatory")
_NvmFrConnSVCTable_Object = MibTable
nvmFrConnSVCTable = _NvmFrConnSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5)
)
if mibBuilder.loadTexts:
    nvmFrConnSVCTable.setStatus("obsolete")
_NvmFrConnSVCEntry_Object = MibTableRow
nvmFrConnSVCEntry = _NvmFrConnSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1)
)
nvmFrConnSVCEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "nvmFrConnSVCIfIndex"),
    (0, "MICOM-FRDCE-MIB", "nvmFrConnSVCConnectId"),
)
if mibBuilder.loadTexts:
    nvmFrConnSVCEntry.setStatus("obsolete")


class _NvmFrConnSVCIfIndex_Type(Integer32):
    """Custom type nvmFrConnSVCIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrConnSVCIfIndex_Type.__name__ = "Integer32"
_NvmFrConnSVCIfIndex_Object = MibTableColumn
nvmFrConnSVCIfIndex = _NvmFrConnSVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 1),
    _NvmFrConnSVCIfIndex_Type()
)
nvmFrConnSVCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnSVCIfIndex.setStatus("obsolete")


class _NvmFrConnSVCConnectId_Type(Integer32):
    """Custom type nvmFrConnSVCConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmFrConnSVCConnectId_Type.__name__ = "Integer32"
_NvmFrConnSVCConnectId_Object = MibTableColumn
nvmFrConnSVCConnectId = _NvmFrConnSVCConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 2),
    _NvmFrConnSVCConnectId_Type()
)
nvmFrConnSVCConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnSVCConnectId.setStatus("obsolete")


class _NvmFrConnSVCDNA_Type(DisplayString):
    """Custom type nvmFrConnSVCDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 30),
    )


_NvmFrConnSVCDNA_Type.__name__ = "DisplayString"
_NvmFrConnSVCDNA_Object = MibTableColumn
nvmFrConnSVCDNA = _NvmFrConnSVCDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 3),
    _NvmFrConnSVCDNA_Type()
)
nvmFrConnSVCDNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCDNA.setStatus("obsolete")


class _NvmFrConnSVCMaxTxSize_Type(Integer32):
    """Custom type nvmFrConnSVCMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrConnSVCMaxTxSize_Type.__name__ = "Integer32"
_NvmFrConnSVCMaxTxSize_Object = MibTableColumn
nvmFrConnSVCMaxTxSize = _NvmFrConnSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 4),
    _NvmFrConnSVCMaxTxSize_Type()
)
nvmFrConnSVCMaxTxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCMaxTxSize.setStatus("obsolete")


class _NvmFrConnSVCMaxRxSize_Type(Integer32):
    """Custom type nvmFrConnSVCMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrConnSVCMaxRxSize_Type.__name__ = "Integer32"
_NvmFrConnSVCMaxRxSize_Object = MibTableColumn
nvmFrConnSVCMaxRxSize = _NvmFrConnSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 5),
    _NvmFrConnSVCMaxRxSize_Type()
)
nvmFrConnSVCMaxRxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCMaxRxSize.setStatus("obsolete")


class _NvmFrConnSVCMinTxThroughput_Type(Integer32):
    """Custom type nvmFrConnSVCMinTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCMinTxThroughput_Type.__name__ = "Integer32"
_NvmFrConnSVCMinTxThroughput_Object = MibTableColumn
nvmFrConnSVCMinTxThroughput = _NvmFrConnSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 6),
    _NvmFrConnSVCMinTxThroughput_Type()
)
nvmFrConnSVCMinTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCMinTxThroughput.setStatus("obsolete")


class _NvmFrConnSVCMinRxThroughput_Type(Integer32):
    """Custom type nvmFrConnSVCMinRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCMinRxThroughput_Type.__name__ = "Integer32"
_NvmFrConnSVCMinRxThroughput_Object = MibTableColumn
nvmFrConnSVCMinRxThroughput = _NvmFrConnSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 7),
    _NvmFrConnSVCMinRxThroughput_Type()
)
nvmFrConnSVCMinRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCMinRxThroughput.setStatus("obsolete")


class _NvmFrConnSVCMaxTxThroughput_Type(Integer32):
    """Custom type nvmFrConnSVCMaxTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCMaxTxThroughput_Type.__name__ = "Integer32"
_NvmFrConnSVCMaxTxThroughput_Object = MibTableColumn
nvmFrConnSVCMaxTxThroughput = _NvmFrConnSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 8),
    _NvmFrConnSVCMaxTxThroughput_Type()
)
nvmFrConnSVCMaxTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnSVCMaxTxThroughput.setStatus("obsolete")


class _NvmFrConnSVCMaxRxThroughput_Type(Integer32):
    """Custom type nvmFrConnSVCMaxRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCMaxRxThroughput_Type.__name__ = "Integer32"
_NvmFrConnSVCMaxRxThroughput_Object = MibTableColumn
nvmFrConnSVCMaxRxThroughput = _NvmFrConnSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 9),
    _NvmFrConnSVCMaxRxThroughput_Type()
)
nvmFrConnSVCMaxRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnSVCMaxRxThroughput.setStatus("obsolete")


class _NvmFrConnSVCMaxTxBurstSize_Type(Integer32):
    """Custom type nvmFrConnSVCMaxTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCMaxTxBurstSize_Type.__name__ = "Integer32"
_NvmFrConnSVCMaxTxBurstSize_Object = MibTableColumn
nvmFrConnSVCMaxTxBurstSize = _NvmFrConnSVCMaxTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 10),
    _NvmFrConnSVCMaxTxBurstSize_Type()
)
nvmFrConnSVCMaxTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnSVCMaxTxBurstSize.setStatus("obsolete")


class _NvmFrConnSVCMaxRxBurstSize_Type(Integer32):
    """Custom type nvmFrConnSVCMaxRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCMaxRxBurstSize_Type.__name__ = "Integer32"
_NvmFrConnSVCMaxRxBurstSize_Object = MibTableColumn
nvmFrConnSVCMaxRxBurstSize = _NvmFrConnSVCMaxRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 11),
    _NvmFrConnSVCMaxRxBurstSize_Type()
)
nvmFrConnSVCMaxRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrConnSVCMaxRxBurstSize.setStatus("obsolete")


class _NvmFrConnSVCExcessTxBurstSize_Type(Integer32):
    """Custom type nvmFrConnSVCExcessTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_NvmFrConnSVCExcessTxBurstSize_Object = MibTableColumn
nvmFrConnSVCExcessTxBurstSize = _NvmFrConnSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 12),
    _NvmFrConnSVCExcessTxBurstSize_Type()
)
nvmFrConnSVCExcessTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCExcessTxBurstSize.setStatus("obsolete")


class _NvmFrConnSVCExcessRxBurstSize_Type(Integer32):
    """Custom type nvmFrConnSVCExcessRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrConnSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_NvmFrConnSVCExcessRxBurstSize_Object = MibTableColumn
nvmFrConnSVCExcessRxBurstSize = _NvmFrConnSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 13),
    _NvmFrConnSVCExcessRxBurstSize_Type()
)
nvmFrConnSVCExcessRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCExcessRxBurstSize.setStatus("obsolete")


class _NvmFrConnSVCTransferPriority_Type(Integer32):
    """Custom type nvmFrConnSVCTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_NvmFrConnSVCTransferPriority_Type.__name__ = "Integer32"
_NvmFrConnSVCTransferPriority_Object = MibTableColumn
nvmFrConnSVCTransferPriority = _NvmFrConnSVCTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 5, 1, 14),
    _NvmFrConnSVCTransferPriority_Type()
)
nvmFrConnSVCTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrConnSVCTransferPriority.setStatus("obsolete")
_NvmFrServiceParamTable_Object = MibTable
nvmFrServiceParamTable = _NvmFrServiceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6)
)
if mibBuilder.loadTexts:
    nvmFrServiceParamTable.setStatus("mandatory")
_NvmFrServiceParamEntry_Object = MibTableRow
nvmFrServiceParamEntry = _NvmFrServiceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1)
)
nvmFrServiceParamEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "nvmFrServiceParamIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrServiceParamEntry.setStatus("mandatory")


class _NvmFrServiceParamIfIndex_Type(Integer32):
    """Custom type nvmFrServiceParamIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrServiceParamIfIndex_Type.__name__ = "Integer32"
_NvmFrServiceParamIfIndex_Object = MibTableColumn
nvmFrServiceParamIfIndex = _NvmFrServiceParamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 1),
    _NvmFrServiceParamIfIndex_Type()
)
nvmFrServiceParamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrServiceParamIfIndex.setStatus("mandatory")


class _NvmFrServiceParamFlowControl_Type(Integer32):
    """Custom type nvmFrServiceParamFlowControl based on Integer32"""
    defaultValue = 2

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


_NvmFrServiceParamFlowControl_Type.__name__ = "Integer32"
_NvmFrServiceParamFlowControl_Object = MibTableColumn
nvmFrServiceParamFlowControl = _NvmFrServiceParamFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 2),
    _NvmFrServiceParamFlowControl_Type()
)
nvmFrServiceParamFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamFlowControl.setStatus("mandatory")


class _NvmFrServiceParamDelta_Type(Integer32):
    """Custom type nvmFrServiceParamDelta based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrServiceParamDelta_Type.__name__ = "Integer32"
_NvmFrServiceParamDelta_Object = MibTableColumn
nvmFrServiceParamDelta = _NvmFrServiceParamDelta_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 3),
    _NvmFrServiceParamDelta_Type()
)
nvmFrServiceParamDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamDelta.setStatus("mandatory")


class _NvmFrServiceParamConsecutiveFrames_Type(Integer32):
    """Custom type nvmFrServiceParamConsecutiveFrames based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NvmFrServiceParamConsecutiveFrames_Type.__name__ = "Integer32"
_NvmFrServiceParamConsecutiveFrames_Object = MibTableColumn
nvmFrServiceParamConsecutiveFrames = _NvmFrServiceParamConsecutiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 4),
    _NvmFrServiceParamConsecutiveFrames_Type()
)
nvmFrServiceParamConsecutiveFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamConsecutiveFrames.setStatus("mandatory")


class _NvmFrServiceParamRateEnf_Type(Integer32):
    """Custom type nvmFrServiceParamRateEnf based on Integer32"""
    defaultValue = 2

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


_NvmFrServiceParamRateEnf_Type.__name__ = "Integer32"
_NvmFrServiceParamRateEnf_Object = MibTableColumn
nvmFrServiceParamRateEnf = _NvmFrServiceParamRateEnf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 5),
    _NvmFrServiceParamRateEnf_Type()
)
nvmFrServiceParamRateEnf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamRateEnf.setStatus("mandatory")


class _NvmFrServiceParamTxMTU_Type(Integer32):
    """Custom type nvmFrServiceParamTxMTU based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NvmFrServiceParamTxMTU_Type.__name__ = "Integer32"
_NvmFrServiceParamTxMTU_Object = MibTableColumn
nvmFrServiceParamTxMTU = _NvmFrServiceParamTxMTU_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 6),
    _NvmFrServiceParamTxMTU_Type()
)
nvmFrServiceParamTxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamTxMTU.setStatus("mandatory")


class _NvmFrServiceParamRxMTU_Type(Integer32):
    """Custom type nvmFrServiceParamRxMTU based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NvmFrServiceParamRxMTU_Type.__name__ = "Integer32"
_NvmFrServiceParamRxMTU_Object = MibTableColumn
nvmFrServiceParamRxMTU = _NvmFrServiceParamRxMTU_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 7),
    _NvmFrServiceParamRxMTU_Type()
)
nvmFrServiceParamRxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamRxMTU.setStatus("mandatory")


class _NvmFrServiceParamTxBc_Type(Integer32):
    """Custom type nvmFrServiceParamTxBc based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrServiceParamTxBc_Type.__name__ = "Integer32"
_NvmFrServiceParamTxBc_Object = MibTableColumn
nvmFrServiceParamTxBc = _NvmFrServiceParamTxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 8),
    _NvmFrServiceParamTxBc_Type()
)
nvmFrServiceParamTxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrServiceParamTxBc.setStatus("mandatory")


class _NvmFrServiceParamRxBc_Type(Integer32):
    """Custom type nvmFrServiceParamRxBc based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrServiceParamRxBc_Type.__name__ = "Integer32"
_NvmFrServiceParamRxBc_Object = MibTableColumn
nvmFrServiceParamRxBc = _NvmFrServiceParamRxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 9),
    _NvmFrServiceParamRxBc_Type()
)
nvmFrServiceParamRxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrServiceParamRxBc.setStatus("mandatory")


class _NvmFrServiceParamTxBe_Type(Integer32):
    """Custom type nvmFrServiceParamTxBe based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrServiceParamTxBe_Type.__name__ = "Integer32"
_NvmFrServiceParamTxBe_Object = MibTableColumn
nvmFrServiceParamTxBe = _NvmFrServiceParamTxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 10),
    _NvmFrServiceParamTxBe_Type()
)
nvmFrServiceParamTxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamTxBe.setStatus("mandatory")


class _NvmFrServiceParamRxBe_Type(Integer32):
    """Custom type nvmFrServiceParamRxBe based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrServiceParamRxBe_Type.__name__ = "Integer32"
_NvmFrServiceParamRxBe_Object = MibTableColumn
nvmFrServiceParamRxBe = _NvmFrServiceParamRxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 11),
    _NvmFrServiceParamRxBe_Type()
)
nvmFrServiceParamRxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamRxBe.setStatus("mandatory")


class _NvmFrServiceParamTxThroughput_Type(Integer32):
    """Custom type nvmFrServiceParamTxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrServiceParamTxThroughput_Type.__name__ = "Integer32"
_NvmFrServiceParamTxThroughput_Object = MibTableColumn
nvmFrServiceParamTxThroughput = _NvmFrServiceParamTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 12),
    _NvmFrServiceParamTxThroughput_Type()
)
nvmFrServiceParamTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamTxThroughput.setStatus("mandatory")


class _NvmFrServiceParamRxThroughput_Type(Integer32):
    """Custom type nvmFrServiceParamRxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrServiceParamRxThroughput_Type.__name__ = "Integer32"
_NvmFrServiceParamRxThroughput_Object = MibTableColumn
nvmFrServiceParamRxThroughput = _NvmFrServiceParamRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 6, 1, 13),
    _NvmFrServiceParamRxThroughput_Type()
)
nvmFrServiceParamRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrServiceParamRxThroughput.setStatus("mandatory")
_McmMPANLConnSVCTable_Object = MibTable
mcmMPANLConnSVCTable = _McmMPANLConnSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7)
)
if mibBuilder.loadTexts:
    mcmMPANLConnSVCTable.setStatus("mandatory")
_McmMPANLConnSVCEntry_Object = MibTableRow
mcmMPANLConnSVCEntry = _McmMPANLConnSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1)
)
mcmMPANLConnSVCEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "mcmMPANLConnSVCConnectId"),
)
if mibBuilder.loadTexts:
    mcmMPANLConnSVCEntry.setStatus("mandatory")


class _McmMPANLConnSVCConnectId_Type(Integer32):
    """Custom type mcmMPANLConnSVCConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmMPANLConnSVCConnectId_Type.__name__ = "Integer32"
_McmMPANLConnSVCConnectId_Object = MibTableColumn
mcmMPANLConnSVCConnectId = _McmMPANLConnSVCConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 1),
    _McmMPANLConnSVCConnectId_Type()
)
mcmMPANLConnSVCConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCConnectId.setStatus("mandatory")


class _McmMPANLConnSVCDNA_Type(DisplayString):
    """Custom type mcmMPANLConnSVCDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmMPANLConnSVCDNA_Type.__name__ = "DisplayString"
_McmMPANLConnSVCDNA_Object = MibTableColumn
mcmMPANLConnSVCDNA = _McmMPANLConnSVCDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 2),
    _McmMPANLConnSVCDNA_Type()
)
mcmMPANLConnSVCDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCDNA.setStatus("mandatory")


class _McmMPANLConnSVCDLCI_Type(Integer32):
    """Custom type mcmMPANLConnSVCDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmMPANLConnSVCDLCI_Type.__name__ = "Integer32"
_McmMPANLConnSVCDLCI_Object = MibTableColumn
mcmMPANLConnSVCDLCI = _McmMPANLConnSVCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 3),
    _McmMPANLConnSVCDLCI_Type()
)
mcmMPANLConnSVCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCDLCI.setStatus("mandatory")


class _McmMPANLConnSVCMaxTxSize_Type(Integer32):
    """Custom type mcmMPANLConnSVCMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmMPANLConnSVCMaxTxSize_Type.__name__ = "Integer32"
_McmMPANLConnSVCMaxTxSize_Object = MibTableColumn
mcmMPANLConnSVCMaxTxSize = _McmMPANLConnSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 4),
    _McmMPANLConnSVCMaxTxSize_Type()
)
mcmMPANLConnSVCMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMaxTxSize.setStatus("mandatory")


class _McmMPANLConnSVCMaxRxSize_Type(Integer32):
    """Custom type mcmMPANLConnSVCMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmMPANLConnSVCMaxRxSize_Type.__name__ = "Integer32"
_McmMPANLConnSVCMaxRxSize_Object = MibTableColumn
mcmMPANLConnSVCMaxRxSize = _McmMPANLConnSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 5),
    _McmMPANLConnSVCMaxRxSize_Type()
)
mcmMPANLConnSVCMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMaxRxSize.setStatus("mandatory")


class _McmMPANLConnSVCMinTxThroughput_Type(Integer32):
    """Custom type mcmMPANLConnSVCMinTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCMinTxThroughput_Type.__name__ = "Integer32"
_McmMPANLConnSVCMinTxThroughput_Object = MibTableColumn
mcmMPANLConnSVCMinTxThroughput = _McmMPANLConnSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 6),
    _McmMPANLConnSVCMinTxThroughput_Type()
)
mcmMPANLConnSVCMinTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMinTxThroughput.setStatus("mandatory")


class _McmMPANLConnSVCMinRxThroughput_Type(Integer32):
    """Custom type mcmMPANLConnSVCMinRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCMinRxThroughput_Type.__name__ = "Integer32"
_McmMPANLConnSVCMinRxThroughput_Object = MibTableColumn
mcmMPANLConnSVCMinRxThroughput = _McmMPANLConnSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 7),
    _McmMPANLConnSVCMinRxThroughput_Type()
)
mcmMPANLConnSVCMinRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMinRxThroughput.setStatus("mandatory")


class _McmMPANLConnSVCMaxTxThroughput_Type(Integer32):
    """Custom type mcmMPANLConnSVCMaxTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCMaxTxThroughput_Type.__name__ = "Integer32"
_McmMPANLConnSVCMaxTxThroughput_Object = MibTableColumn
mcmMPANLConnSVCMaxTxThroughput = _McmMPANLConnSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 8),
    _McmMPANLConnSVCMaxTxThroughput_Type()
)
mcmMPANLConnSVCMaxTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMaxTxThroughput.setStatus("mandatory")


class _McmMPANLConnSVCMaxRxThroughput_Type(Integer32):
    """Custom type mcmMPANLConnSVCMaxRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCMaxRxThroughput_Type.__name__ = "Integer32"
_McmMPANLConnSVCMaxRxThroughput_Object = MibTableColumn
mcmMPANLConnSVCMaxRxThroughput = _McmMPANLConnSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 9),
    _McmMPANLConnSVCMaxRxThroughput_Type()
)
mcmMPANLConnSVCMaxRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMaxRxThroughput.setStatus("mandatory")


class _McmMPANLConnSVCMaxTxBurstSize_Type(Integer32):
    """Custom type mcmMPANLConnSVCMaxTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCMaxTxBurstSize_Type.__name__ = "Integer32"
_McmMPANLConnSVCMaxTxBurstSize_Object = MibTableColumn
mcmMPANLConnSVCMaxTxBurstSize = _McmMPANLConnSVCMaxTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 10),
    _McmMPANLConnSVCMaxTxBurstSize_Type()
)
mcmMPANLConnSVCMaxTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMaxTxBurstSize.setStatus("mandatory")


class _McmMPANLConnSVCMaxRxBurstSize_Type(Integer32):
    """Custom type mcmMPANLConnSVCMaxRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCMaxRxBurstSize_Type.__name__ = "Integer32"
_McmMPANLConnSVCMaxRxBurstSize_Object = MibTableColumn
mcmMPANLConnSVCMaxRxBurstSize = _McmMPANLConnSVCMaxRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 11),
    _McmMPANLConnSVCMaxRxBurstSize_Type()
)
mcmMPANLConnSVCMaxRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCMaxRxBurstSize.setStatus("mandatory")


class _McmMPANLConnSVCExcessTxBurstSize_Type(Integer32):
    """Custom type mcmMPANLConnSVCExcessTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_McmMPANLConnSVCExcessTxBurstSize_Object = MibTableColumn
mcmMPANLConnSVCExcessTxBurstSize = _McmMPANLConnSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 12),
    _McmMPANLConnSVCExcessTxBurstSize_Type()
)
mcmMPANLConnSVCExcessTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCExcessTxBurstSize.setStatus("mandatory")


class _McmMPANLConnSVCExcessRxBurstSize_Type(Integer32):
    """Custom type mcmMPANLConnSVCExcessRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMPANLConnSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_McmMPANLConnSVCExcessRxBurstSize_Object = MibTableColumn
mcmMPANLConnSVCExcessRxBurstSize = _McmMPANLConnSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 13),
    _McmMPANLConnSVCExcessRxBurstSize_Type()
)
mcmMPANLConnSVCExcessRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCExcessRxBurstSize.setStatus("mandatory")


class _McmMPANLConnSVCTransferPriority_Type(Integer32):
    """Custom type mcmMPANLConnSVCTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmMPANLConnSVCTransferPriority_Type.__name__ = "Integer32"
_McmMPANLConnSVCTransferPriority_Object = MibTableColumn
mcmMPANLConnSVCTransferPriority = _McmMPANLConnSVCTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 14),
    _McmMPANLConnSVCTransferPriority_Type()
)
mcmMPANLConnSVCTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCTransferPriority.setStatus("mandatory")


class _McmMPANLConnSVCReasonForDisconnect_Type(Integer32):
    """Custom type mcmMPANLConnSVCReasonForDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              21,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              47,
              49,
              50,
              57,
              58,
              63,
              65,
              66,
              70,
              79,
              81,
              82,
              87,
              88,
              90,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              111,
              127,
              128)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-implemented", 65),
          ("bearer-capability-not-presently-available", 58),
          ("call-awarded-and-being-delivered-in-an-est-channel", 7),
          ("channel-type-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("destination-out-of-order", 27),
          ("element-non-existent-or-not-implemented", 99),
          ("facility-rejected", 29),
          ("identified-channel-does-not-exist", 82),
          ("incompatible-destination", 88),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-element", 100),
          ("invalid-message-for-state", 101),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network-selection", 91),
          ("message-not-compatible", 98),
          ("message-type-unknown", 97),
          ("missing-element", 96),
          ("network-out-of-order", 38),
          ("no-DLCI-available", 34),
          ("no-route-to-destination", 3),
          ("no-route-to-specified-transit-network", 2),
          ("no-user-present-in-call", 18),
          ("non-existent-CUG", 90),
          ("normal-call-clearing", 16),
          ("normal-condition", 128),
          ("normal-unspecified", 31),
          ("only-restricted-digital-capability-is-available", 70),
          ("permanent-frame-mode-connection-operational", 40),
          ("permanent-frame-mode-connection-out-of-service", 39),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-not-available", 49),
          ("remote-PVC-already-connected-ie-busy", 17),
          ("remote-PVC-down-ie-unavailable", 21),
          ("requested-facility-not-subscribed", 50),
          ("resource-unavailable", 47),
          ("response-to-status-inquiry", 30),
          ("service-or-option-not-available-unspecified", 63),
          ("service-or-option-not-implemented-unspecified", 79),
          ("specified-DLCI-unavailable", 44),
          ("switching-equipment-congestion", 42),
          ("temporary-failure", 41),
          ("the-PVC-does-not-exist-ie-unassigned", 1),
          ("timer-recovery", 102),
          ("user-not-member-of-CUG", 87))
    )


_McmMPANLConnSVCReasonForDisconnect_Type.__name__ = "Integer32"
_McmMPANLConnSVCReasonForDisconnect_Object = MibTableColumn
mcmMPANLConnSVCReasonForDisconnect = _McmMPANLConnSVCReasonForDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 15),
    _McmMPANLConnSVCReasonForDisconnect_Type()
)
mcmMPANLConnSVCReasonForDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCReasonForDisconnect.setStatus("mandatory")


class _McmMPANLConnSVCDiscardPriority_Type(Integer32):
    """Custom type mcmMPANLConnSVCDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_McmMPANLConnSVCDiscardPriority_Type.__name__ = "Integer32"
_McmMPANLConnSVCDiscardPriority_Object = MibTableColumn
mcmMPANLConnSVCDiscardPriority = _McmMPANLConnSVCDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 16),
    _McmMPANLConnSVCDiscardPriority_Type()
)
mcmMPANLConnSVCDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCDiscardPriority.setStatus("mandatory")


class _McmMPANLConnSVCIfindex_Type(Integer32):
    """Custom type mcmMPANLConnSVCIfindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMPANLConnSVCIfindex_Type.__name__ = "Integer32"
_McmMPANLConnSVCIfindex_Object = MibTableColumn
mcmMPANLConnSVCIfindex = _McmMPANLConnSVCIfindex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 17),
    _McmMPANLConnSVCIfindex_Type()
)
mcmMPANLConnSVCIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCIfindex.setStatus("mandatory")


class _McmMPANLConnSVCSetupPriority_Type(Integer32):
    """Custom type mcmMPANLConnSVCSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmMPANLConnSVCSetupPriority_Type.__name__ = "Integer32"
_McmMPANLConnSVCSetupPriority_Object = MibTableColumn
mcmMPANLConnSVCSetupPriority = _McmMPANLConnSVCSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 18),
    _McmMPANLConnSVCSetupPriority_Type()
)
mcmMPANLConnSVCSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCSetupPriority.setStatus("mandatory")


class _McmMPANLConnSVCHoldingPriority_Type(Integer32):
    """Custom type mcmMPANLConnSVCHoldingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmMPANLConnSVCHoldingPriority_Type.__name__ = "Integer32"
_McmMPANLConnSVCHoldingPriority_Object = MibTableColumn
mcmMPANLConnSVCHoldingPriority = _McmMPANLConnSVCHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 7, 1, 19),
    _McmMPANLConnSVCHoldingPriority_Type()
)
mcmMPANLConnSVCHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMPANLConnSVCHoldingPriority.setStatus("mandatory")
_NvmMPANLConnSVCTable_Object = MibTable
nvmMPANLConnSVCTable = _NvmMPANLConnSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8)
)
if mibBuilder.loadTexts:
    nvmMPANLConnSVCTable.setStatus("mandatory")
_NvmMPANLConnSVCEntry_Object = MibTableRow
nvmMPANLConnSVCEntry = _NvmMPANLConnSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1)
)
nvmMPANLConnSVCEntry.setIndexNames(
    (0, "MICOM-FRDCE-MIB", "nvmMPANLConnSVCConnectId"),
)
if mibBuilder.loadTexts:
    nvmMPANLConnSVCEntry.setStatus("mandatory")


class _NvmMPANLConnSVCConnectId_Type(Integer32):
    """Custom type nvmMPANLConnSVCConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmMPANLConnSVCConnectId_Type.__name__ = "Integer32"
_NvmMPANLConnSVCConnectId_Object = MibTableColumn
nvmMPANLConnSVCConnectId = _NvmMPANLConnSVCConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 1),
    _NvmMPANLConnSVCConnectId_Type()
)
nvmMPANLConnSVCConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCConnectId.setStatus("mandatory")


class _NvmMPANLConnSVCDNA_Type(DisplayString):
    """Custom type nvmMPANLConnSVCDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmMPANLConnSVCDNA_Type.__name__ = "DisplayString"
_NvmMPANLConnSVCDNA_Object = MibTableColumn
nvmMPANLConnSVCDNA = _NvmMPANLConnSVCDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 2),
    _NvmMPANLConnSVCDNA_Type()
)
nvmMPANLConnSVCDNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCDNA.setStatus("mandatory")


class _NvmMPANLConnSVCMaxTxSize_Type(Integer32):
    """Custom type nvmMPANLConnSVCMaxTxSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmMPANLConnSVCMaxTxSize_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMaxTxSize_Object = MibTableColumn
nvmMPANLConnSVCMaxTxSize = _NvmMPANLConnSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 3),
    _NvmMPANLConnSVCMaxTxSize_Type()
)
nvmMPANLConnSVCMaxTxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMaxTxSize.setStatus("mandatory")


class _NvmMPANLConnSVCMaxRxSize_Type(Integer32):
    """Custom type nvmMPANLConnSVCMaxRxSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmMPANLConnSVCMaxRxSize_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMaxRxSize_Object = MibTableColumn
nvmMPANLConnSVCMaxRxSize = _NvmMPANLConnSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 4),
    _NvmMPANLConnSVCMaxRxSize_Type()
)
nvmMPANLConnSVCMaxRxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMaxRxSize.setStatus("mandatory")


class _NvmMPANLConnSVCMinTxThroughput_Type(Integer32):
    """Custom type nvmMPANLConnSVCMinTxThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCMinTxThroughput_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMinTxThroughput_Object = MibTableColumn
nvmMPANLConnSVCMinTxThroughput = _NvmMPANLConnSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 5),
    _NvmMPANLConnSVCMinTxThroughput_Type()
)
nvmMPANLConnSVCMinTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMinTxThroughput.setStatus("mandatory")


class _NvmMPANLConnSVCMinRxThroughput_Type(Integer32):
    """Custom type nvmMPANLConnSVCMinRxThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCMinRxThroughput_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMinRxThroughput_Object = MibTableColumn
nvmMPANLConnSVCMinRxThroughput = _NvmMPANLConnSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 6),
    _NvmMPANLConnSVCMinRxThroughput_Type()
)
nvmMPANLConnSVCMinRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMinRxThroughput.setStatus("mandatory")


class _NvmMPANLConnSVCMaxTxThroughput_Type(Integer32):
    """Custom type nvmMPANLConnSVCMaxTxThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCMaxTxThroughput_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMaxTxThroughput_Object = MibTableColumn
nvmMPANLConnSVCMaxTxThroughput = _NvmMPANLConnSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 7),
    _NvmMPANLConnSVCMaxTxThroughput_Type()
)
nvmMPANLConnSVCMaxTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMaxTxThroughput.setStatus("mandatory")


class _NvmMPANLConnSVCMaxRxThroughput_Type(Integer32):
    """Custom type nvmMPANLConnSVCMaxRxThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCMaxRxThroughput_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMaxRxThroughput_Object = MibTableColumn
nvmMPANLConnSVCMaxRxThroughput = _NvmMPANLConnSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 8),
    _NvmMPANLConnSVCMaxRxThroughput_Type()
)
nvmMPANLConnSVCMaxRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMaxRxThroughput.setStatus("mandatory")


class _NvmMPANLConnSVCMaxTxBurstSize_Type(Integer32):
    """Custom type nvmMPANLConnSVCMaxTxBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCMaxTxBurstSize_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMaxTxBurstSize_Object = MibTableColumn
nvmMPANLConnSVCMaxTxBurstSize = _NvmMPANLConnSVCMaxTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 9),
    _NvmMPANLConnSVCMaxTxBurstSize_Type()
)
nvmMPANLConnSVCMaxTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMaxTxBurstSize.setStatus("mandatory")


class _NvmMPANLConnSVCMaxRxBurstSize_Type(Integer32):
    """Custom type nvmMPANLConnSVCMaxRxBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCMaxRxBurstSize_Type.__name__ = "Integer32"
_NvmMPANLConnSVCMaxRxBurstSize_Object = MibTableColumn
nvmMPANLConnSVCMaxRxBurstSize = _NvmMPANLConnSVCMaxRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 10),
    _NvmMPANLConnSVCMaxRxBurstSize_Type()
)
nvmMPANLConnSVCMaxRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCMaxRxBurstSize.setStatus("mandatory")


class _NvmMPANLConnSVCExcessTxBurstSize_Type(Integer32):
    """Custom type nvmMPANLConnSVCExcessTxBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_NvmMPANLConnSVCExcessTxBurstSize_Object = MibTableColumn
nvmMPANLConnSVCExcessTxBurstSize = _NvmMPANLConnSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 11),
    _NvmMPANLConnSVCExcessTxBurstSize_Type()
)
nvmMPANLConnSVCExcessTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCExcessTxBurstSize.setStatus("mandatory")


class _NvmMPANLConnSVCExcessRxBurstSize_Type(Integer32):
    """Custom type nvmMPANLConnSVCExcessRxBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmMPANLConnSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_NvmMPANLConnSVCExcessRxBurstSize_Object = MibTableColumn
nvmMPANLConnSVCExcessRxBurstSize = _NvmMPANLConnSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 12),
    _NvmMPANLConnSVCExcessRxBurstSize_Type()
)
nvmMPANLConnSVCExcessRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCExcessRxBurstSize.setStatus("mandatory")


class _NvmMPANLConnSVCTransferPriority_Type(Integer32):
    """Custom type nvmMPANLConnSVCTransferPriority based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NvmMPANLConnSVCTransferPriority_Type.__name__ = "Integer32"
_NvmMPANLConnSVCTransferPriority_Object = MibTableColumn
nvmMPANLConnSVCTransferPriority = _NvmMPANLConnSVCTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 13),
    _NvmMPANLConnSVCTransferPriority_Type()
)
nvmMPANLConnSVCTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCTransferPriority.setStatus("mandatory")


class _NvmMPANLConnSVCDiscardPriority_Type(Integer32):
    """Custom type nvmMPANLConnSVCDiscardPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_NvmMPANLConnSVCDiscardPriority_Type.__name__ = "Integer32"
_NvmMPANLConnSVCDiscardPriority_Object = MibTableColumn
nvmMPANLConnSVCDiscardPriority = _NvmMPANLConnSVCDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 14),
    _NvmMPANLConnSVCDiscardPriority_Type()
)
nvmMPANLConnSVCDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCDiscardPriority.setStatus("mandatory")


class _NvmMPANLConnSVCSetupPriority_Type(Integer32):
    """Custom type nvmMPANLConnSVCSetupPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmMPANLConnSVCSetupPriority_Type.__name__ = "Integer32"
_NvmMPANLConnSVCSetupPriority_Object = MibTableColumn
nvmMPANLConnSVCSetupPriority = _NvmMPANLConnSVCSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 15),
    _NvmMPANLConnSVCSetupPriority_Type()
)
nvmMPANLConnSVCSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCSetupPriority.setStatus("mandatory")


class _NvmMPANLConnSVCHoldingPriority_Type(Integer32):
    """Custom type nvmMPANLConnSVCHoldingPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmMPANLConnSVCHoldingPriority_Type.__name__ = "Integer32"
_NvmMPANLConnSVCHoldingPriority_Object = MibTableColumn
nvmMPANLConnSVCHoldingPriority = _NvmMPANLConnSVCHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 1, 8, 1, 16),
    _NvmMPANLConnSVCHoldingPriority_Type()
)
nvmMPANLConnSVCHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMPANLConnSVCHoldingPriority.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmFrPvcLmiLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 0, 1)
)
mcmFrPvcLmiLinkUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-SYS-MIB", "mcmSysIfExtModule"),
        ("MICOM-SYS-MIB", "mcmSysIfExtPPA"))
)
if mibBuilder.loadTexts:
    mcmFrPvcLmiLinkUp.setStatus(
        ""
    )

mcmFrPvcLmiLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 9, 0, 2)
)
mcmFrPvcLmiLinkDown.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-SYS-MIB", "mcmSysIfExtModule"),
        ("MICOM-SYS-MIB", "mcmSysIfExtPPA"))
)
if mibBuilder.loadTexts:
    mcmFrPvcLmiLinkDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-FRDCE-MIB",
    **{"micom-frdce": micom_frdce,
       "mcmFrPvcLmiLinkUp": mcmFrPvcLmiLinkUp,
       "mcmFrPvcLmiLinkDown": mcmFrPvcLmiLinkDown,
       "frdce-configuration": frdce_configuration,
       "mcmFrConnectTable": mcmFrConnectTable,
       "mcmFrConnectEntry": mcmFrConnectEntry,
       "mcmFrConnectIfIndexLocal": mcmFrConnectIfIndexLocal,
       "mcmFrConnectDLCILocal": mcmFrConnectDLCILocal,
       "mcmFrConnectConnectId": mcmFrConnectConnectId,
       "mcmFrConnectIfIndexRemote": mcmFrConnectIfIndexRemote,
       "mcmFrConnectDLCIRemote": mcmFrConnectDLCIRemote,
       "mcmFrConnectIfIndexSVC": mcmFrConnectIfIndexSVC,
       "mcmFrConnectDNARemote": mcmFrConnectDNARemote,
       "mcmFrConnectSVCDLCI": mcmFrConnectSVCDLCI,
       "mcmFrConnectDCEPVCLMIState": mcmFrConnectDCEPVCLMIState,
       "mcmFrConnectSVCState": mcmFrConnectSVCState,
       "mcmFrConnectConnType": mcmFrConnectConnType,
       "mcmFrConnectLastChange": mcmFrConnectLastChange,
       "mcmFrConnectDisconnectReason": mcmFrConnectDisconnectReason,
       "mcmFrConnectSwitchType": mcmFrConnectSwitchType,
       "mcmFrConnSVCTable": mcmFrConnSVCTable,
       "mcmFrConnSVCEntry": mcmFrConnSVCEntry,
       "mcmFrConnSVCIfIndex": mcmFrConnSVCIfIndex,
       "mcmFrConnSVCConnectId": mcmFrConnSVCConnectId,
       "mcmFrConnSVCDNA": mcmFrConnSVCDNA,
       "mcmFrConnSVCDLCI": mcmFrConnSVCDLCI,
       "mcmFrConnSVCMaxTxSize": mcmFrConnSVCMaxTxSize,
       "mcmFrConnSVCMaxRxSize": mcmFrConnSVCMaxRxSize,
       "mcmFrConnSVCMinTxThroughput": mcmFrConnSVCMinTxThroughput,
       "mcmFrConnSVCMinRxThroughput": mcmFrConnSVCMinRxThroughput,
       "mcmFrConnSVCMaxTxThroughput": mcmFrConnSVCMaxTxThroughput,
       "mcmFrConnSVCMaxRxThroughput": mcmFrConnSVCMaxRxThroughput,
       "mcmFrConnSVCMaxTxBurstSize": mcmFrConnSVCMaxTxBurstSize,
       "mcmFrConnSVCMaxRxBurstSize": mcmFrConnSVCMaxRxBurstSize,
       "mcmFrConnSVCExcessTxBurstSize": mcmFrConnSVCExcessTxBurstSize,
       "mcmFrConnSVCExcessRxBurstSize": mcmFrConnSVCExcessRxBurstSize,
       "mcmFrConnSVCTransferPriority": mcmFrConnSVCTransferPriority,
       "mcmFrConnSVCReasonForDisconnect": mcmFrConnSVCReasonForDisconnect,
       "mcmFrServiceParamTable": mcmFrServiceParamTable,
       "mcmFrServiceParamEntry": mcmFrServiceParamEntry,
       "mcmFrServiceParamIfIndex": mcmFrServiceParamIfIndex,
       "mcmFrServiceParamFlowControl": mcmFrServiceParamFlowControl,
       "mcmFrServiceParamDelta": mcmFrServiceParamDelta,
       "mcmFrServiceParamConsecutiveFrames": mcmFrServiceParamConsecutiveFrames,
       "mcmFrServiceParamRateEnf": mcmFrServiceParamRateEnf,
       "mcmFrServiceParamTxMTU": mcmFrServiceParamTxMTU,
       "mcmFrServiceParamRxMTU": mcmFrServiceParamRxMTU,
       "mcmFrServiceParamTxBc": mcmFrServiceParamTxBc,
       "mcmFrServiceParamRxBc": mcmFrServiceParamRxBc,
       "mcmFrServiceParamTxBe": mcmFrServiceParamTxBe,
       "mcmFrServiceParamRxBe": mcmFrServiceParamRxBe,
       "mcmFrServiceParamTxThroughput": mcmFrServiceParamTxThroughput,
       "mcmFrServiceParamRxThroughput": mcmFrServiceParamRxThroughput,
       "mcmFrServiceParamPVCLMIStatus": mcmFrServiceParamPVCLMIStatus,
       "mcmFrServiceParamSVCLMIStatus": mcmFrServiceParamSVCLMIStatus,
       "nvmFrConnectTable": nvmFrConnectTable,
       "nvmFrConnectEntry": nvmFrConnectEntry,
       "nvmFrConnectIfIndexLocal": nvmFrConnectIfIndexLocal,
       "nvmFrConnectDLCILocal": nvmFrConnectDLCILocal,
       "nvmFrConnectConnectId": nvmFrConnectConnectId,
       "nvmFrConnectIfIndexRemote": nvmFrConnectIfIndexRemote,
       "nvmFrConnectDLCIRemote": nvmFrConnectDLCIRemote,
       "nvmFrConnectIfIndexSVC": nvmFrConnectIfIndexSVC,
       "nvmFrConnectDNARemote": nvmFrConnectDNARemote,
       "nvmFrConnectConnType": nvmFrConnectConnType,
       "nvmFrConnectRowStatus": nvmFrConnectRowStatus,
       "nvmFrConnectSwitchType": nvmFrConnectSwitchType,
       "nvmFrConnSVCTable": nvmFrConnSVCTable,
       "nvmFrConnSVCEntry": nvmFrConnSVCEntry,
       "nvmFrConnSVCIfIndex": nvmFrConnSVCIfIndex,
       "nvmFrConnSVCConnectId": nvmFrConnSVCConnectId,
       "nvmFrConnSVCDNA": nvmFrConnSVCDNA,
       "nvmFrConnSVCMaxTxSize": nvmFrConnSVCMaxTxSize,
       "nvmFrConnSVCMaxRxSize": nvmFrConnSVCMaxRxSize,
       "nvmFrConnSVCMinTxThroughput": nvmFrConnSVCMinTxThroughput,
       "nvmFrConnSVCMinRxThroughput": nvmFrConnSVCMinRxThroughput,
       "nvmFrConnSVCMaxTxThroughput": nvmFrConnSVCMaxTxThroughput,
       "nvmFrConnSVCMaxRxThroughput": nvmFrConnSVCMaxRxThroughput,
       "nvmFrConnSVCMaxTxBurstSize": nvmFrConnSVCMaxTxBurstSize,
       "nvmFrConnSVCMaxRxBurstSize": nvmFrConnSVCMaxRxBurstSize,
       "nvmFrConnSVCExcessTxBurstSize": nvmFrConnSVCExcessTxBurstSize,
       "nvmFrConnSVCExcessRxBurstSize": nvmFrConnSVCExcessRxBurstSize,
       "nvmFrConnSVCTransferPriority": nvmFrConnSVCTransferPriority,
       "nvmFrServiceParamTable": nvmFrServiceParamTable,
       "nvmFrServiceParamEntry": nvmFrServiceParamEntry,
       "nvmFrServiceParamIfIndex": nvmFrServiceParamIfIndex,
       "nvmFrServiceParamFlowControl": nvmFrServiceParamFlowControl,
       "nvmFrServiceParamDelta": nvmFrServiceParamDelta,
       "nvmFrServiceParamConsecutiveFrames": nvmFrServiceParamConsecutiveFrames,
       "nvmFrServiceParamRateEnf": nvmFrServiceParamRateEnf,
       "nvmFrServiceParamTxMTU": nvmFrServiceParamTxMTU,
       "nvmFrServiceParamRxMTU": nvmFrServiceParamRxMTU,
       "nvmFrServiceParamTxBc": nvmFrServiceParamTxBc,
       "nvmFrServiceParamRxBc": nvmFrServiceParamRxBc,
       "nvmFrServiceParamTxBe": nvmFrServiceParamTxBe,
       "nvmFrServiceParamRxBe": nvmFrServiceParamRxBe,
       "nvmFrServiceParamTxThroughput": nvmFrServiceParamTxThroughput,
       "nvmFrServiceParamRxThroughput": nvmFrServiceParamRxThroughput,
       "mcmMPANLConnSVCTable": mcmMPANLConnSVCTable,
       "mcmMPANLConnSVCEntry": mcmMPANLConnSVCEntry,
       "mcmMPANLConnSVCConnectId": mcmMPANLConnSVCConnectId,
       "mcmMPANLConnSVCDNA": mcmMPANLConnSVCDNA,
       "mcmMPANLConnSVCDLCI": mcmMPANLConnSVCDLCI,
       "mcmMPANLConnSVCMaxTxSize": mcmMPANLConnSVCMaxTxSize,
       "mcmMPANLConnSVCMaxRxSize": mcmMPANLConnSVCMaxRxSize,
       "mcmMPANLConnSVCMinTxThroughput": mcmMPANLConnSVCMinTxThroughput,
       "mcmMPANLConnSVCMinRxThroughput": mcmMPANLConnSVCMinRxThroughput,
       "mcmMPANLConnSVCMaxTxThroughput": mcmMPANLConnSVCMaxTxThroughput,
       "mcmMPANLConnSVCMaxRxThroughput": mcmMPANLConnSVCMaxRxThroughput,
       "mcmMPANLConnSVCMaxTxBurstSize": mcmMPANLConnSVCMaxTxBurstSize,
       "mcmMPANLConnSVCMaxRxBurstSize": mcmMPANLConnSVCMaxRxBurstSize,
       "mcmMPANLConnSVCExcessTxBurstSize": mcmMPANLConnSVCExcessTxBurstSize,
       "mcmMPANLConnSVCExcessRxBurstSize": mcmMPANLConnSVCExcessRxBurstSize,
       "mcmMPANLConnSVCTransferPriority": mcmMPANLConnSVCTransferPriority,
       "mcmMPANLConnSVCReasonForDisconnect": mcmMPANLConnSVCReasonForDisconnect,
       "mcmMPANLConnSVCDiscardPriority": mcmMPANLConnSVCDiscardPriority,
       "mcmMPANLConnSVCIfindex": mcmMPANLConnSVCIfindex,
       "mcmMPANLConnSVCSetupPriority": mcmMPANLConnSVCSetupPriority,
       "mcmMPANLConnSVCHoldingPriority": mcmMPANLConnSVCHoldingPriority,
       "nvmMPANLConnSVCTable": nvmMPANLConnSVCTable,
       "nvmMPANLConnSVCEntry": nvmMPANLConnSVCEntry,
       "nvmMPANLConnSVCConnectId": nvmMPANLConnSVCConnectId,
       "nvmMPANLConnSVCDNA": nvmMPANLConnSVCDNA,
       "nvmMPANLConnSVCMaxTxSize": nvmMPANLConnSVCMaxTxSize,
       "nvmMPANLConnSVCMaxRxSize": nvmMPANLConnSVCMaxRxSize,
       "nvmMPANLConnSVCMinTxThroughput": nvmMPANLConnSVCMinTxThroughput,
       "nvmMPANLConnSVCMinRxThroughput": nvmMPANLConnSVCMinRxThroughput,
       "nvmMPANLConnSVCMaxTxThroughput": nvmMPANLConnSVCMaxTxThroughput,
       "nvmMPANLConnSVCMaxRxThroughput": nvmMPANLConnSVCMaxRxThroughput,
       "nvmMPANLConnSVCMaxTxBurstSize": nvmMPANLConnSVCMaxTxBurstSize,
       "nvmMPANLConnSVCMaxRxBurstSize": nvmMPANLConnSVCMaxRxBurstSize,
       "nvmMPANLConnSVCExcessTxBurstSize": nvmMPANLConnSVCExcessTxBurstSize,
       "nvmMPANLConnSVCExcessRxBurstSize": nvmMPANLConnSVCExcessRxBurstSize,
       "nvmMPANLConnSVCTransferPriority": nvmMPANLConnSVCTransferPriority,
       "nvmMPANLConnSVCDiscardPriority": nvmMPANLConnSVCDiscardPriority,
       "nvmMPANLConnSVCSetupPriority": nvmMPANLConnSVCSetupPriority,
       "nvmMPANLConnSVCHoldingPriority": nvmMPANLConnSVCHoldingPriority}
)
