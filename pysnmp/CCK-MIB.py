# SNMP MIB module (CCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:52 2024
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rsCCK,) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rsCCK")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
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





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsCCKElementTable_Object = MibTable
rsCCKElementTable = _RsCCKElementTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1)
)
if mibBuilder.loadTexts:
    rsCCKElementTable.setStatus("mandatory")
_RsCCKElementEntry_Object = MibTableRow
rsCCKElementEntry = _RsCCKElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1)
)
rsCCKElementEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKElementId"),
)
if mibBuilder.loadTexts:
    rsCCKElementEntry.setStatus("mandatory")
_RsCCKElementId_Type = Integer32
_RsCCKElementId_Object = MibTableColumn
rsCCKElementId = _RsCCKElementId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 1),
    _RsCCKElementId_Type()
)
rsCCKElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementId.setStatus("mandatory")


class _RsCCKElementDescription_Type(DisplayString):
    """Custom type rsCCKElementDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKElementDescription_Type.__name__ = "DisplayString"
_RsCCKElementDescription_Object = MibTableColumn
rsCCKElementDescription = _RsCCKElementDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 2),
    _RsCCKElementDescription_Type()
)
rsCCKElementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementDescription.setStatus("mandatory")


class _RsCCKElementGroup_Type(DisplayString):
    """Custom type rsCCKElementGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKElementGroup_Type.__name__ = "DisplayString"
_RsCCKElementGroup_Object = MibTableColumn
rsCCKElementGroup = _RsCCKElementGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 3),
    _RsCCKElementGroup_Type()
)
rsCCKElementGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementGroup.setStatus("mandatory")


class _RsCCKElementIsActive_Type(Integer32):
    """Custom type rsCCKElementIsActive based on Integer32"""
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


_RsCCKElementIsActive_Type.__name__ = "Integer32"
_RsCCKElementIsActive_Object = MibTableColumn
rsCCKElementIsActive = _RsCCKElementIsActive_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 4),
    _RsCCKElementIsActive_Type()
)
rsCCKElementIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementIsActive.setStatus("mandatory")


class _RsCCKElementIsAvailable_Type(Integer32):
    """Custom type rsCCKElementIsAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_RsCCKElementIsAvailable_Type.__name__ = "Integer32"
_RsCCKElementIsAvailable_Object = MibTableColumn
rsCCKElementIsAvailable = _RsCCKElementIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 5),
    _RsCCKElementIsAvailable_Type()
)
rsCCKElementIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementIsAvailable.setStatus("mandatory")
_RsCCKElementDftAddr_Type = IpAddress
_RsCCKElementDftAddr_Object = MibTableColumn
rsCCKElementDftAddr = _RsCCKElementDftAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 6),
    _RsCCKElementDftAddr_Type()
)
rsCCKElementDftAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementDftAddr.setStatus("mandatory")
_RsCCKElementRowStatus_Type = RowStatus
_RsCCKElementRowStatus_Object = MibTableColumn
rsCCKElementRowStatus = _RsCCKElementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 1, 1, 7),
    _RsCCKElementRowStatus_Type()
)
rsCCKElementRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKElementRowStatus.setStatus("mandatory")
_RsCCKHealthChkTable_Object = MibTable
rsCCKHealthChkTable = _RsCCKHealthChkTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2)
)
if mibBuilder.loadTexts:
    rsCCKHealthChkTable.setStatus("mandatory")
_RsCCKHealthChkEntry_Object = MibTableRow
rsCCKHealthChkEntry = _RsCCKHealthChkEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1)
)
rsCCKHealthChkEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKHealthChkName"),
)
if mibBuilder.loadTexts:
    rsCCKHealthChkEntry.setStatus("mandatory")


class _RsCCKHealthChkName_Type(DisplayString):
    """Custom type rsCCKHealthChkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKHealthChkName_Type.__name__ = "DisplayString"
_RsCCKHealthChkName_Object = MibTableColumn
rsCCKHealthChkName = _RsCCKHealthChkName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 1),
    _RsCCKHealthChkName_Type()
)
rsCCKHealthChkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkName.setStatus("mandatory")
_RsCCKHealthChkId_Type = Integer32
_RsCCKHealthChkId_Object = MibTableColumn
rsCCKHealthChkId = _RsCCKHealthChkId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 2),
    _RsCCKHealthChkId_Type()
)
rsCCKHealthChkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkId.setStatus("mandatory")
_RsCCKHealthChkMethod_Type = Integer32
_RsCCKHealthChkMethod_Object = MibTableColumn
rsCCKHealthChkMethod = _RsCCKHealthChkMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 3),
    _RsCCKHealthChkMethod_Type()
)
rsCCKHealthChkMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkMethod.setStatus("mandatory")


class _RsCCKHealthChkStatus_Type(Integer32):
    """Custom type rsCCKHealthChkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("passed", 3),
          ("unknown", 1))
    )


_RsCCKHealthChkStatus_Type.__name__ = "Integer32"
_RsCCKHealthChkStatus_Object = MibTableColumn
rsCCKHealthChkStatus = _RsCCKHealthChkStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 4),
    _RsCCKHealthChkStatus_Type()
)
rsCCKHealthChkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKHealthChkStatus.setStatus("mandatory")
_RsCCKHealthChkDstAddr_Type = IpAddress
_RsCCKHealthChkDstAddr_Object = MibTableColumn
rsCCKHealthChkDstAddr = _RsCCKHealthChkDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 5),
    _RsCCKHealthChkDstAddr_Type()
)
rsCCKHealthChkDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkDstAddr.setStatus("mandatory")
_RsCCKHealthChkNextHop_Type = IpAddress
_RsCCKHealthChkNextHop_Object = MibTableColumn
rsCCKHealthChkNextHop = _RsCCKHealthChkNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 6),
    _RsCCKHealthChkNextHop_Type()
)
rsCCKHealthChkNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkNextHop.setStatus("mandatory")
_RsCCKHealthChkDstPort_Type = Integer32
_RsCCKHealthChkDstPort_Object = MibTableColumn
rsCCKHealthChkDstPort = _RsCCKHealthChkDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 7),
    _RsCCKHealthChkDstPort_Type()
)
rsCCKHealthChkDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkDstPort.setStatus("mandatory")


class _RsCCKHealthChkArguments_Type(DisplayString):
    """Custom type rsCCKHealthChkArguments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKHealthChkArguments_Type.__name__ = "DisplayString"
_RsCCKHealthChkArguments_Object = MibTableColumn
rsCCKHealthChkArguments = _RsCCKHealthChkArguments_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 8),
    _RsCCKHealthChkArguments_Type()
)
rsCCKHealthChkArguments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkArguments.setStatus("mandatory")
_RsCCKHealthChkInterval_Type = Integer32
_RsCCKHealthChkInterval_Object = MibTableColumn
rsCCKHealthChkInterval = _RsCCKHealthChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 9),
    _RsCCKHealthChkInterval_Type()
)
rsCCKHealthChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkInterval.setStatus("mandatory")
_RsCCKHealthChkRetries_Type = Integer32
_RsCCKHealthChkRetries_Object = MibTableColumn
rsCCKHealthChkRetries = _RsCCKHealthChkRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 10),
    _RsCCKHealthChkRetries_Type()
)
rsCCKHealthChkRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkRetries.setStatus("mandatory")
_RsCCKHealthChkTimeout_Type = Integer32
_RsCCKHealthChkTimeout_Object = MibTableColumn
rsCCKHealthChkTimeout = _RsCCKHealthChkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 11),
    _RsCCKHealthChkTimeout_Type()
)
rsCCKHealthChkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkTimeout.setStatus("mandatory")
_RsCCKHealthChkRowStatus_Type = RowStatus
_RsCCKHealthChkRowStatus_Object = MibTableColumn
rsCCKHealthChkRowStatus = _RsCCKHealthChkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 2, 1, 12),
    _RsCCKHealthChkRowStatus_Type()
)
rsCCKHealthChkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKHealthChkRowStatus.setStatus("mandatory")
_RsCCKChkBindingTable_Object = MibTable
rsCCKChkBindingTable = _RsCCKChkBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3)
)
if mibBuilder.loadTexts:
    rsCCKChkBindingTable.setStatus("mandatory")
_RsCCKChkBindingEntry_Object = MibTableRow
rsCCKChkBindingEntry = _RsCCKChkBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1)
)
rsCCKChkBindingEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKChkBindingHealthChk"),
    (0, "CCK-MIB", "rsCCKChkBindingElement"),
)
if mibBuilder.loadTexts:
    rsCCKChkBindingEntry.setStatus("mandatory")
_RsCCKChkBindingHealthChk_Type = Integer32
_RsCCKChkBindingHealthChk_Object = MibTableColumn
rsCCKChkBindingHealthChk = _RsCCKChkBindingHealthChk_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 1),
    _RsCCKChkBindingHealthChk_Type()
)
rsCCKChkBindingHealthChk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkBindingHealthChk.setStatus("mandatory")
_RsCCKChkBindingElement_Type = Integer32
_RsCCKChkBindingElement_Object = MibTableColumn
rsCCKChkBindingElement = _RsCCKChkBindingElement_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 2),
    _RsCCKChkBindingElement_Type()
)
rsCCKChkBindingElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkBindingElement.setStatus("mandatory")
_RsCCKChkBindingGroup_Type = Integer32
_RsCCKChkBindingGroup_Object = MibTableColumn
rsCCKChkBindingGroup = _RsCCKChkBindingGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 3),
    _RsCCKChkBindingGroup_Type()
)
rsCCKChkBindingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKChkBindingGroup.setStatus("mandatory")


class _RsCCKChkBindingMandatory_Type(Integer32):
    """Custom type rsCCKChkBindingMandatory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ismandatory", 1),
          ("isnon-mandatory", 2))
    )


_RsCCKChkBindingMandatory_Type.__name__ = "Integer32"
_RsCCKChkBindingMandatory_Object = MibTableColumn
rsCCKChkBindingMandatory = _RsCCKChkBindingMandatory_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 4),
    _RsCCKChkBindingMandatory_Type()
)
rsCCKChkBindingMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKChkBindingMandatory.setStatus("mandatory")
_RsCCKChkBindingRowStatus_Type = RowStatus
_RsCCKChkBindingRowStatus_Object = MibTableColumn
rsCCKChkBindingRowStatus = _RsCCKChkBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 3, 1, 5),
    _RsCCKChkBindingRowStatus_Type()
)
rsCCKChkBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKChkBindingRowStatus.setStatus("mandatory")
_RsCCKChkMethodTable_Object = MibTable
rsCCKChkMethodTable = _RsCCKChkMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4)
)
if mibBuilder.loadTexts:
    rsCCKChkMethodTable.setStatus("mandatory")
_RsCCKChkMethodEntry_Object = MibTableRow
rsCCKChkMethodEntry = _RsCCKChkMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1)
)
rsCCKChkMethodEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKChkMethodId"),
)
if mibBuilder.loadTexts:
    rsCCKChkMethodEntry.setStatus("mandatory")
_RsCCKChkMethodId_Type = Integer32
_RsCCKChkMethodId_Object = MibTableColumn
rsCCKChkMethodId = _RsCCKChkMethodId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1, 1),
    _RsCCKChkMethodId_Type()
)
rsCCKChkMethodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkMethodId.setStatus("mandatory")


class _RsCCKChkMethodDescription_Type(DisplayString):
    """Custom type rsCCKChkMethodDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKChkMethodDescription_Type.__name__ = "DisplayString"
_RsCCKChkMethodDescription_Object = MibTableColumn
rsCCKChkMethodDescription = _RsCCKChkMethodDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1, 2),
    _RsCCKChkMethodDescription_Type()
)
rsCCKChkMethodDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkMethodDescription.setStatus("mandatory")
_RsCCKChkMethodRowStatus_Type = RowStatus
_RsCCKChkMethodRowStatus_Object = MibTableColumn
rsCCKChkMethodRowStatus = _RsCCKChkMethodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 4, 1, 3),
    _RsCCKChkMethodRowStatus_Type()
)
rsCCKChkMethodRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCCKChkMethodRowStatus.setStatus("mandatory")
_RsCCKPktSequenceTable_Object = MibTable
rsCCKPktSequenceTable = _RsCCKPktSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5)
)
if mibBuilder.loadTexts:
    rsCCKPktSequenceTable.setStatus("mandatory")
_RsCCKPktSequenceEntry_Object = MibTableRow
rsCCKPktSequenceEntry = _RsCCKPktSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1)
)
rsCCKPktSequenceEntry.setIndexNames(
    (0, "CCK-MIB", "rsCCKPktSequenceSeqId"),
    (0, "CCK-MIB", "rsCCKPktSequencePktId"),
)
if mibBuilder.loadTexts:
    rsCCKPktSequenceEntry.setStatus("mandatory")
_RsCCKPktSequenceSeqId_Type = Integer32
_RsCCKPktSequenceSeqId_Object = MibTableColumn
rsCCKPktSequenceSeqId = _RsCCKPktSequenceSeqId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 1),
    _RsCCKPktSequenceSeqId_Type()
)
rsCCKPktSequenceSeqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceSeqId.setStatus("mandatory")
_RsCCKPktSequencePktId_Type = Integer32
_RsCCKPktSequencePktId_Object = MibTableColumn
rsCCKPktSequencePktId = _RsCCKPktSequencePktId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 2),
    _RsCCKPktSequencePktId_Type()
)
rsCCKPktSequencePktId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequencePktId.setStatus("mandatory")


class _RsCCKPktSequenceType_Type(Integer32):
    """Custom type rsCCKPktSequenceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("send", 1))
    )


_RsCCKPktSequenceType_Type.__name__ = "Integer32"
_RsCCKPktSequenceType_Object = MibTableColumn
rsCCKPktSequenceType = _RsCCKPktSequenceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 3),
    _RsCCKPktSequenceType_Type()
)
rsCCKPktSequenceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceType.setStatus("mandatory")


class _RsCCKPktSequenceString_Type(DisplayString):
    """Custom type rsCCKPktSequenceString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKPktSequenceString_Type.__name__ = "DisplayString"
_RsCCKPktSequenceString_Object = MibTableColumn
rsCCKPktSequenceString = _RsCCKPktSequenceString_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 4),
    _RsCCKPktSequenceString_Type()
)
rsCCKPktSequenceString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceString.setStatus("mandatory")


class _RsCCKPktSequenceDescription_Type(DisplayString):
    """Custom type rsCCKPktSequenceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsCCKPktSequenceDescription_Type.__name__ = "DisplayString"
_RsCCKPktSequenceDescription_Object = MibTableColumn
rsCCKPktSequenceDescription = _RsCCKPktSequenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 5),
    _RsCCKPktSequenceDescription_Type()
)
rsCCKPktSequenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceDescription.setStatus("mandatory")
_RsCCKPktSequenceRowStatus_Type = RowStatus
_RsCCKPktSequenceRowStatus_Object = MibTableColumn
rsCCKPktSequenceRowStatus = _RsCCKPktSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 5, 1, 6),
    _RsCCKPktSequenceRowStatus_Type()
)
rsCCKPktSequenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKPktSequenceRowStatus.setStatus("mandatory")


class _RsCCKArgDelimiter_Type(DisplayString):
    """Custom type rsCCKArgDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_RsCCKArgDelimiter_Type.__name__ = "DisplayString"
_RsCCKArgDelimiter_Object = MibScalar
rsCCKArgDelimiter = _RsCCKArgDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 6),
    _RsCCKArgDelimiter_Type()
)
rsCCKArgDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKArgDelimiter.setStatus("mandatory")
_RsCCKNextElementId_Type = Integer32
_RsCCKNextElementId_Object = MibScalar
rsCCKNextElementId = _RsCCKNextElementId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 7),
    _RsCCKNextElementId_Type()
)
rsCCKNextElementId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKNextElementId.setStatus("mandatory")
_RsCCKNextCheckId_Type = Integer32
_RsCCKNextCheckId_Object = MibScalar
rsCCKNextCheckId = _RsCCKNextCheckId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 8),
    _RsCCKNextCheckId_Type()
)
rsCCKNextCheckId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKNextCheckId.setStatus("mandatory")


class _RsCCKStatus_Type(Integer32):
    """Custom type rsCCKStatus based on Integer32"""
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


_RsCCKStatus_Type.__name__ = "Integer32"
_RsCCKStatus_Object = MibScalar
rsCCKStatus = _RsCCKStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79, 9),
    _RsCCKStatus_Type()
)
rsCCKStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCCKStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CCK-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "rsCCKElementTable": rsCCKElementTable,
       "rsCCKElementEntry": rsCCKElementEntry,
       "rsCCKElementId": rsCCKElementId,
       "rsCCKElementDescription": rsCCKElementDescription,
       "rsCCKElementGroup": rsCCKElementGroup,
       "rsCCKElementIsActive": rsCCKElementIsActive,
       "rsCCKElementIsAvailable": rsCCKElementIsAvailable,
       "rsCCKElementDftAddr": rsCCKElementDftAddr,
       "rsCCKElementRowStatus": rsCCKElementRowStatus,
       "rsCCKHealthChkTable": rsCCKHealthChkTable,
       "rsCCKHealthChkEntry": rsCCKHealthChkEntry,
       "rsCCKHealthChkName": rsCCKHealthChkName,
       "rsCCKHealthChkId": rsCCKHealthChkId,
       "rsCCKHealthChkMethod": rsCCKHealthChkMethod,
       "rsCCKHealthChkStatus": rsCCKHealthChkStatus,
       "rsCCKHealthChkDstAddr": rsCCKHealthChkDstAddr,
       "rsCCKHealthChkNextHop": rsCCKHealthChkNextHop,
       "rsCCKHealthChkDstPort": rsCCKHealthChkDstPort,
       "rsCCKHealthChkArguments": rsCCKHealthChkArguments,
       "rsCCKHealthChkInterval": rsCCKHealthChkInterval,
       "rsCCKHealthChkRetries": rsCCKHealthChkRetries,
       "rsCCKHealthChkTimeout": rsCCKHealthChkTimeout,
       "rsCCKHealthChkRowStatus": rsCCKHealthChkRowStatus,
       "rsCCKChkBindingTable": rsCCKChkBindingTable,
       "rsCCKChkBindingEntry": rsCCKChkBindingEntry,
       "rsCCKChkBindingHealthChk": rsCCKChkBindingHealthChk,
       "rsCCKChkBindingElement": rsCCKChkBindingElement,
       "rsCCKChkBindingGroup": rsCCKChkBindingGroup,
       "rsCCKChkBindingMandatory": rsCCKChkBindingMandatory,
       "rsCCKChkBindingRowStatus": rsCCKChkBindingRowStatus,
       "rsCCKChkMethodTable": rsCCKChkMethodTable,
       "rsCCKChkMethodEntry": rsCCKChkMethodEntry,
       "rsCCKChkMethodId": rsCCKChkMethodId,
       "rsCCKChkMethodDescription": rsCCKChkMethodDescription,
       "rsCCKChkMethodRowStatus": rsCCKChkMethodRowStatus,
       "rsCCKPktSequenceTable": rsCCKPktSequenceTable,
       "rsCCKPktSequenceEntry": rsCCKPktSequenceEntry,
       "rsCCKPktSequenceSeqId": rsCCKPktSequenceSeqId,
       "rsCCKPktSequencePktId": rsCCKPktSequencePktId,
       "rsCCKPktSequenceType": rsCCKPktSequenceType,
       "rsCCKPktSequenceString": rsCCKPktSequenceString,
       "rsCCKPktSequenceDescription": rsCCKPktSequenceDescription,
       "rsCCKPktSequenceRowStatus": rsCCKPktSequenceRowStatus,
       "rsCCKArgDelimiter": rsCCKArgDelimiter,
       "rsCCKNextElementId": rsCCKNextElementId,
       "rsCCKNextCheckId": rsCCKNextCheckId,
       "rsCCKStatus": rsCCKStatus}
)
