# SNMP MIB module (CTSMTMIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTSMTMIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:57 2024
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

(ctsmtmib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctsmtmib")

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

_CtsmtmibRingTable_Object = MibTable
ctsmtmibRingTable = _CtsmtmibRingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctsmtmibRingTable.setStatus("mandatory")
_CtsmtmibRingEntry_Object = MibTableRow
ctsmtmibRingEntry = _CtsmtmibRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1)
)
ctsmtmibRingEntry.setIndexNames(
    (0, "CTSMTMIB-MIB", "ctsmtmibRingSmtIndex"),
    (0, "CTSMTMIB-MIB", "ctsmtmibRingMacIndex"),
    (0, "CTSMTMIB-MIB", "ctsmtmibRingNodeIndex"),
    (0, "CTSMTMIB-MIB", "ctsmtmibRingMacAddr"),
)
if mibBuilder.loadTexts:
    ctsmtmibRingEntry.setStatus("mandatory")
_CtsmtmibRingSmtIndex_Type = Integer32
_CtsmtmibRingSmtIndex_Object = MibTableColumn
ctsmtmibRingSmtIndex = _CtsmtmibRingSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 1),
    _CtsmtmibRingSmtIndex_Type()
)
ctsmtmibRingSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingSmtIndex.setStatus("mandatory")
_CtsmtmibRingMacIndex_Type = Integer32
_CtsmtmibRingMacIndex_Object = MibTableColumn
ctsmtmibRingMacIndex = _CtsmtmibRingMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 2),
    _CtsmtmibRingMacIndex_Type()
)
ctsmtmibRingMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingMacIndex.setStatus("mandatory")
_CtsmtmibRingNodeIndex_Type = Integer32
_CtsmtmibRingNodeIndex_Object = MibTableColumn
ctsmtmibRingNodeIndex = _CtsmtmibRingNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 3),
    _CtsmtmibRingNodeIndex_Type()
)
ctsmtmibRingNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingNodeIndex.setStatus("mandatory")
_CtsmtmibRingMacAddr_Type = OctetString
_CtsmtmibRingMacAddr_Object = MibTableColumn
ctsmtmibRingMacAddr = _CtsmtmibRingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 4),
    _CtsmtmibRingMacAddr_Type()
)
ctsmtmibRingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingMacAddr.setStatus("mandatory")


class _CtsmtmibRingUpStreamAddr_Type(OctetString):
    """Custom type ctsmtmibRingUpStreamAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CtsmtmibRingUpStreamAddr_Type.__name__ = "OctetString"
_CtsmtmibRingUpStreamAddr_Object = MibTableColumn
ctsmtmibRingUpStreamAddr = _CtsmtmibRingUpStreamAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 5),
    _CtsmtmibRingUpStreamAddr_Type()
)
ctsmtmibRingUpStreamAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingUpStreamAddr.setStatus("mandatory")


class _CtsmtmibRingNodeClass_Type(Integer32):
    """Custom type ctsmtmibRingNodeClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 2),
          ("station", 1))
    )


_CtsmtmibRingNodeClass_Type.__name__ = "Integer32"
_CtsmtmibRingNodeClass_Object = MibTableColumn
ctsmtmibRingNodeClass = _CtsmtmibRingNodeClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 6),
    _CtsmtmibRingNodeClass_Type()
)
ctsmtmibRingNodeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingNodeClass.setStatus("mandatory")
_CtsmtmibRingMacCount_Type = Integer32
_CtsmtmibRingMacCount_Object = MibTableColumn
ctsmtmibRingMacCount = _CtsmtmibRingMacCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 7),
    _CtsmtmibRingMacCount_Type()
)
ctsmtmibRingMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingMacCount.setStatus("mandatory")
_CtsmtmibRingNonMasterCount_Type = Integer32
_CtsmtmibRingNonMasterCount_Object = MibTableColumn
ctsmtmibRingNonMasterCount = _CtsmtmibRingNonMasterCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 8),
    _CtsmtmibRingNonMasterCount_Type()
)
ctsmtmibRingNonMasterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingNonMasterCount.setStatus("mandatory")


class _CtsmtmibRingMasterCount_Type(Integer32):
    """Custom type ctsmtmibRingMasterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtsmtmibRingMasterCount_Type.__name__ = "Integer32"
_CtsmtmibRingMasterCount_Object = MibTableColumn
ctsmtmibRingMasterCount = _CtsmtmibRingMasterCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 9),
    _CtsmtmibRingMasterCount_Type()
)
ctsmtmibRingMasterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingMasterCount.setStatus("mandatory")
_CtsmtmibRingTopology_Type = Integer32
_CtsmtmibRingTopology_Object = MibTableColumn
ctsmtmibRingTopology = _CtsmtmibRingTopology_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 10),
    _CtsmtmibRingTopology_Type()
)
ctsmtmibRingTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingTopology.setStatus("mandatory")


class _CtsmtmibRingDuplicate_Type(Integer32):
    """Custom type ctsmtmibRingDuplicate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CtsmtmibRingDuplicate_Type.__name__ = "Integer32"
_CtsmtmibRingDuplicate_Object = MibTableColumn
ctsmtmibRingDuplicate = _CtsmtmibRingDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 11),
    _CtsmtmibRingDuplicate_Type()
)
ctsmtmibRingDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibRingDuplicate.setStatus("mandatory")
_CtsmtmibMacTable_Object = MibTable
ctsmtmibMacTable = _CtsmtmibMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ctsmtmibMacTable.setStatus("mandatory")
_CtsmtmibMacEntry_Object = MibTableRow
ctsmtmibMacEntry = _CtsmtmibMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1)
)
ctsmtmibMacEntry.setIndexNames(
    (0, "CTSMTMIB-MIB", "ctsmtmibMacSmtIndex"),
    (0, "CTSMTMIB-MIB", "ctsmtmibMacIndex"),
)
if mibBuilder.loadTexts:
    ctsmtmibMacEntry.setStatus("mandatory")
_CtsmtmibMacSmtIndex_Type = Integer32
_CtsmtmibMacSmtIndex_Object = MibTableColumn
ctsmtmibMacSmtIndex = _CtsmtmibMacSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 1),
    _CtsmtmibMacSmtIndex_Type()
)
ctsmtmibMacSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacSmtIndex.setStatus("mandatory")
_CtsmtmibMacIndex_Type = Integer32
_CtsmtmibMacIndex_Object = MibTableColumn
ctsmtmibMacIndex = _CtsmtmibMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 2),
    _CtsmtmibMacIndex_Type()
)
ctsmtmibMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacIndex.setStatus("mandatory")
_CtsmtmibMacNifTxCts_Type = Counter32
_CtsmtmibMacNifTxCts_Object = MibTableColumn
ctsmtmibMacNifTxCts = _CtsmtmibMacNifTxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 3),
    _CtsmtmibMacNifTxCts_Type()
)
ctsmtmibMacNifTxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacNifTxCts.setStatus("mandatory")
_CtsmtmibMacNifRxCts_Type = Counter32
_CtsmtmibMacNifRxCts_Object = MibTableColumn
ctsmtmibMacNifRxCts = _CtsmtmibMacNifRxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 4),
    _CtsmtmibMacNifRxCts_Type()
)
ctsmtmibMacNifRxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacNifRxCts.setStatus("mandatory")
_CtsmtmibMacSifTxCts_Type = Counter32
_CtsmtmibMacSifTxCts_Object = MibTableColumn
ctsmtmibMacSifTxCts = _CtsmtmibMacSifTxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 5),
    _CtsmtmibMacSifTxCts_Type()
)
ctsmtmibMacSifTxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacSifTxCts.setStatus("mandatory")
_CtsmtmibMacSifRxCts_Type = Counter32
_CtsmtmibMacSifRxCts_Object = MibTableColumn
ctsmtmibMacSifRxCts = _CtsmtmibMacSifRxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 6),
    _CtsmtmibMacSifRxCts_Type()
)
ctsmtmibMacSifRxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacSifRxCts.setStatus("mandatory")
_CtsmtmibMacEcfTxCts_Type = Counter32
_CtsmtmibMacEcfTxCts_Object = MibTableColumn
ctsmtmibMacEcfTxCts = _CtsmtmibMacEcfTxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 7),
    _CtsmtmibMacEcfTxCts_Type()
)
ctsmtmibMacEcfTxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacEcfTxCts.setStatus("mandatory")
_CtsmtmibMacEcfRxCts_Type = Counter32
_CtsmtmibMacEcfRxCts_Object = MibTableColumn
ctsmtmibMacEcfRxCts = _CtsmtmibMacEcfRxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 8),
    _CtsmtmibMacEcfRxCts_Type()
)
ctsmtmibMacEcfRxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacEcfRxCts.setStatus("mandatory")
_CtsmtmibMacPmfTxCts_Type = Counter32
_CtsmtmibMacPmfTxCts_Object = MibTableColumn
ctsmtmibMacPmfTxCts = _CtsmtmibMacPmfTxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 9),
    _CtsmtmibMacPmfTxCts_Type()
)
ctsmtmibMacPmfTxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacPmfTxCts.setStatus("mandatory")
_CtsmtmibMacPmfRxCts_Type = Counter32
_CtsmtmibMacPmfRxCts_Object = MibTableColumn
ctsmtmibMacPmfRxCts = _CtsmtmibMacPmfRxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 10),
    _CtsmtmibMacPmfRxCts_Type()
)
ctsmtmibMacPmfRxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacPmfRxCts.setStatus("mandatory")
_CtsmtmibMacRdfTxCts_Type = Counter32
_CtsmtmibMacRdfTxCts_Object = MibTableColumn
ctsmtmibMacRdfTxCts = _CtsmtmibMacRdfTxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 11),
    _CtsmtmibMacRdfTxCts_Type()
)
ctsmtmibMacRdfTxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacRdfTxCts.setStatus("mandatory")
_CtsmtmibMacRdfRxCts_Type = Counter32
_CtsmtmibMacRdfRxCts_Object = MibTableColumn
ctsmtmibMacRdfRxCts = _CtsmtmibMacRdfRxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 12),
    _CtsmtmibMacRdfRxCts_Type()
)
ctsmtmibMacRdfRxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacRdfRxCts.setStatus("mandatory")
_CtsmtmibMacRingOpCts_Type = Counter32
_CtsmtmibMacRingOpCts_Object = MibTableColumn
ctsmtmibMacRingOpCts = _CtsmtmibMacRingOpCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 13),
    _CtsmtmibMacRingOpCts_Type()
)
ctsmtmibMacRingOpCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacRingOpCts.setStatus("mandatory")
_CtsmtmibMacTxCts_Type = Counter32
_CtsmtmibMacTxCts_Object = MibTableColumn
ctsmtmibMacTxCts = _CtsmtmibMacTxCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 14),
    _CtsmtmibMacTxCts_Type()
)
ctsmtmibMacTxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacTxCts.setStatus("mandatory")
_CtsmtmibMacRingMapUpdateCts_Type = Counter32
_CtsmtmibMacRingMapUpdateCts_Object = MibTableColumn
ctsmtmibMacRingMapUpdateCts = _CtsmtmibMacRingMapUpdateCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 15),
    _CtsmtmibMacRingMapUpdateCts_Type()
)
ctsmtmibMacRingMapUpdateCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibMacRingMapUpdateCts.setStatus("mandatory")


class _CtsmtmibMacAutoNegotiation_Type(Integer32):
    """Custom type ctsmtmibMacAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CtsmtmibMacAutoNegotiation_Type.__name__ = "Integer32"
_CtsmtmibMacAutoNegotiation_Object = MibTableColumn
ctsmtmibMacAutoNegotiation = _CtsmtmibMacAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 16),
    _CtsmtmibMacAutoNegotiation_Type()
)
ctsmtmibMacAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsmtmibMacAutoNegotiation.setStatus("mandatory")


class _CtsmtmibAttachmentNumber_Type(Integer32):
    """Custom type ctsmtmibAttachmentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtsmtmibAttachmentNumber_Type.__name__ = "Integer32"
_CtsmtmibAttachmentNumber_Object = MibScalar
ctsmtmibAttachmentNumber = _CtsmtmibAttachmentNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 3),
    _CtsmtmibAttachmentNumber_Type()
)
ctsmtmibAttachmentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentNumber.setStatus("mandatory")
_CtsmtmibAttachmentTable_Object = MibTable
ctsmtmibAttachmentTable = _CtsmtmibAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ctsmtmibAttachmentTable.setStatus("mandatory")
_CtsmtmibAttachmentEntry_Object = MibTableRow
ctsmtmibAttachmentEntry = _CtsmtmibAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1)
)
ctsmtmibAttachmentEntry.setIndexNames(
    (0, "CTSMTMIB-MIB", "ctsmtmibAttachmentSMTIndex"),
    (0, "CTSMTMIB-MIB", "ctsmtmibAttachmentIndex"),
)
if mibBuilder.loadTexts:
    ctsmtmibAttachmentEntry.setStatus("mandatory")


class _CtsmtmibAttachmentSMTIndex_Type(Integer32):
    """Custom type ctsmtmibAttachmentSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtsmtmibAttachmentSMTIndex_Type.__name__ = "Integer32"
_CtsmtmibAttachmentSMTIndex_Object = MibTableColumn
ctsmtmibAttachmentSMTIndex = _CtsmtmibAttachmentSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 1),
    _CtsmtmibAttachmentSMTIndex_Type()
)
ctsmtmibAttachmentSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentSMTIndex.setStatus("mandatory")


class _CtsmtmibAttachmentIndex_Type(Integer32):
    """Custom type ctsmtmibAttachmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtsmtmibAttachmentIndex_Type.__name__ = "Integer32"
_CtsmtmibAttachmentIndex_Object = MibTableColumn
ctsmtmibAttachmentIndex = _CtsmtmibAttachmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 2),
    _CtsmtmibAttachmentIndex_Type()
)
ctsmtmibAttachmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentIndex.setStatus("mandatory")


class _CtsmtmibAttachmentClass_Type(Integer32):
    """Custom type ctsmtmibAttachmentClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 3),
          ("dual-attachment", 2),
          ("single-attachment", 1))
    )


_CtsmtmibAttachmentClass_Type.__name__ = "Integer32"
_CtsmtmibAttachmentClass_Object = MibTableColumn
ctsmtmibAttachmentClass = _CtsmtmibAttachmentClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 3),
    _CtsmtmibAttachmentClass_Type()
)
ctsmtmibAttachmentClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentClass.setStatus("mandatory")


class _CtsmtmibAttachmentOpticalBypassPresent_Type(Integer32):
    """Custom type ctsmtmibAttachmentOpticalBypassPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CtsmtmibAttachmentOpticalBypassPresent_Type.__name__ = "Integer32"
_CtsmtmibAttachmentOpticalBypassPresent_Object = MibTableColumn
ctsmtmibAttachmentOpticalBypassPresent = _CtsmtmibAttachmentOpticalBypassPresent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 4),
    _CtsmtmibAttachmentOpticalBypassPresent_Type()
)
ctsmtmibAttachmentOpticalBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentOpticalBypassPresent.setStatus("mandatory")


class _CtsmtmibAttachmentIMaxExpiration_Type(Integer32):
    """Custom type ctsmtmibAttachmentIMaxExpiration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtsmtmibAttachmentIMaxExpiration_Type.__name__ = "Integer32"
_CtsmtmibAttachmentIMaxExpiration_Object = MibTableColumn
ctsmtmibAttachmentIMaxExpiration = _CtsmtmibAttachmentIMaxExpiration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 5),
    _CtsmtmibAttachmentIMaxExpiration_Type()
)
ctsmtmibAttachmentIMaxExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentIMaxExpiration.setStatus("mandatory")


class _CtsmtmibAttachmentInsertedStatus_Type(Integer32):
    """Custom type ctsmtmibAttachmentInsertedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unimplemented", 3))
    )


_CtsmtmibAttachmentInsertedStatus_Type.__name__ = "Integer32"
_CtsmtmibAttachmentInsertedStatus_Object = MibTableColumn
ctsmtmibAttachmentInsertedStatus = _CtsmtmibAttachmentInsertedStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 6),
    _CtsmtmibAttachmentInsertedStatus_Type()
)
ctsmtmibAttachmentInsertedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentInsertedStatus.setStatus("mandatory")


class _CtsmtmibAttachmentInsertPolicy_Type(Integer32):
    """Custom type ctsmtmibAttachmentInsertPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unimplemented", 3))
    )


_CtsmtmibAttachmentInsertPolicy_Type.__name__ = "Integer32"
_CtsmtmibAttachmentInsertPolicy_Object = MibTableColumn
ctsmtmibAttachmentInsertPolicy = _CtsmtmibAttachmentInsertPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 7),
    _CtsmtmibAttachmentInsertPolicy_Type()
)
ctsmtmibAttachmentInsertPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsmtmibAttachmentInsertPolicy.setStatus("mandatory")
_CtsmtmibSMTTable_Object = MibTable
ctsmtmibSMTTable = _CtsmtmibSMTTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ctsmtmibSMTTable.setStatus("mandatory")
_CtsmtmibSMTEntry_Object = MibTableRow
ctsmtmibSMTEntry = _CtsmtmibSMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1)
)
ctsmtmibSMTEntry.setIndexNames(
    (0, "CTSMTMIB-MIB", "ctsmtmibSmtIndex"),
)
if mibBuilder.loadTexts:
    ctsmtmibSMTEntry.setStatus("mandatory")


class _CtsmtmibSMTDualHomeStatus_Type(Integer32):
    """Custom type ctsmtmibSMTDualHomeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkAandB", 3),
          ("linkAorB", 2),
          ("notDualHomed", 1))
    )


_CtsmtmibSMTDualHomeStatus_Type.__name__ = "Integer32"
_CtsmtmibSMTDualHomeStatus_Object = MibTableColumn
ctsmtmibSMTDualHomeStatus = _CtsmtmibSMTDualHomeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 1),
    _CtsmtmibSMTDualHomeStatus_Type()
)
ctsmtmibSMTDualHomeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibSMTDualHomeStatus.setStatus("mandatory")


class _CtsmtmibSMTDualHomeWrpLEDStatus_Type(Integer32):
    """Custom type ctsmtmibSMTDualHomeWrpLEDStatus based on Integer32"""
    defaultValue = 1

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


_CtsmtmibSMTDualHomeWrpLEDStatus_Type.__name__ = "Integer32"
_CtsmtmibSMTDualHomeWrpLEDStatus_Object = MibTableColumn
ctsmtmibSMTDualHomeWrpLEDStatus = _CtsmtmibSMTDualHomeWrpLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 2),
    _CtsmtmibSMTDualHomeWrpLEDStatus_Type()
)
ctsmtmibSMTDualHomeWrpLEDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsmtmibSMTDualHomeWrpLEDStatus.setStatus("mandatory")
_CtsmtmibSmtIndex_Type = Integer32
_CtsmtmibSmtIndex_Object = MibTableColumn
ctsmtmibSmtIndex = _CtsmtmibSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 3),
    _CtsmtmibSmtIndex_Type()
)
ctsmtmibSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsmtmibSmtIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTSMTMIB-MIB",
    **{"ctsmtmibRingTable": ctsmtmibRingTable,
       "ctsmtmibRingEntry": ctsmtmibRingEntry,
       "ctsmtmibRingSmtIndex": ctsmtmibRingSmtIndex,
       "ctsmtmibRingMacIndex": ctsmtmibRingMacIndex,
       "ctsmtmibRingNodeIndex": ctsmtmibRingNodeIndex,
       "ctsmtmibRingMacAddr": ctsmtmibRingMacAddr,
       "ctsmtmibRingUpStreamAddr": ctsmtmibRingUpStreamAddr,
       "ctsmtmibRingNodeClass": ctsmtmibRingNodeClass,
       "ctsmtmibRingMacCount": ctsmtmibRingMacCount,
       "ctsmtmibRingNonMasterCount": ctsmtmibRingNonMasterCount,
       "ctsmtmibRingMasterCount": ctsmtmibRingMasterCount,
       "ctsmtmibRingTopology": ctsmtmibRingTopology,
       "ctsmtmibRingDuplicate": ctsmtmibRingDuplicate,
       "ctsmtmibMacTable": ctsmtmibMacTable,
       "ctsmtmibMacEntry": ctsmtmibMacEntry,
       "ctsmtmibMacSmtIndex": ctsmtmibMacSmtIndex,
       "ctsmtmibMacIndex": ctsmtmibMacIndex,
       "ctsmtmibMacNifTxCts": ctsmtmibMacNifTxCts,
       "ctsmtmibMacNifRxCts": ctsmtmibMacNifRxCts,
       "ctsmtmibMacSifTxCts": ctsmtmibMacSifTxCts,
       "ctsmtmibMacSifRxCts": ctsmtmibMacSifRxCts,
       "ctsmtmibMacEcfTxCts": ctsmtmibMacEcfTxCts,
       "ctsmtmibMacEcfRxCts": ctsmtmibMacEcfRxCts,
       "ctsmtmibMacPmfTxCts": ctsmtmibMacPmfTxCts,
       "ctsmtmibMacPmfRxCts": ctsmtmibMacPmfRxCts,
       "ctsmtmibMacRdfTxCts": ctsmtmibMacRdfTxCts,
       "ctsmtmibMacRdfRxCts": ctsmtmibMacRdfRxCts,
       "ctsmtmibMacRingOpCts": ctsmtmibMacRingOpCts,
       "ctsmtmibMacTxCts": ctsmtmibMacTxCts,
       "ctsmtmibMacRingMapUpdateCts": ctsmtmibMacRingMapUpdateCts,
       "ctsmtmibMacAutoNegotiation": ctsmtmibMacAutoNegotiation,
       "ctsmtmibAttachmentNumber": ctsmtmibAttachmentNumber,
       "ctsmtmibAttachmentTable": ctsmtmibAttachmentTable,
       "ctsmtmibAttachmentEntry": ctsmtmibAttachmentEntry,
       "ctsmtmibAttachmentSMTIndex": ctsmtmibAttachmentSMTIndex,
       "ctsmtmibAttachmentIndex": ctsmtmibAttachmentIndex,
       "ctsmtmibAttachmentClass": ctsmtmibAttachmentClass,
       "ctsmtmibAttachmentOpticalBypassPresent": ctsmtmibAttachmentOpticalBypassPresent,
       "ctsmtmibAttachmentIMaxExpiration": ctsmtmibAttachmentIMaxExpiration,
       "ctsmtmibAttachmentInsertedStatus": ctsmtmibAttachmentInsertedStatus,
       "ctsmtmibAttachmentInsertPolicy": ctsmtmibAttachmentInsertPolicy,
       "ctsmtmibSMTTable": ctsmtmibSMTTable,
       "ctsmtmibSMTEntry": ctsmtmibSMTEntry,
       "ctsmtmibSMTDualHomeStatus": ctsmtmibSMTDualHomeStatus,
       "ctsmtmibSMTDualHomeWrpLEDStatus": ctsmtmibSMTDualHomeWrpLEDStatus,
       "ctsmtmibSmtIndex": ctsmtmibSmtIndex}
)
