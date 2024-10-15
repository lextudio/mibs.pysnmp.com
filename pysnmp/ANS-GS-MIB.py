# SNMP MIB module (ANS-GS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-GS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:58 2024
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

(DateAndTime,
 RowPointer,
 RowStatus,
 mlpmpR115) = mibBuilder.importSymbols(
    "ANS-COMMON-MIB",
    "DateAndTime",
    "RowPointer",
    "RowStatus",
    "mlpmpR115")

(ansBoardPosition,
 ansBoardSubrackIndex,
 ansBoardSystemNodeIndex) = mibBuilder.importSymbols(
    "ANS-EQUIPMENT-MIB",
    "ansBoardPosition",
    "ansBoardSubrackIndex",
    "ansBoardSystemNodeIndex")

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



class AnsPortType(Integer32):
    """Custom type AnsPortType based on Integer32"""
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
        *(("atm", 1),
          ("ds1", 5),
          ("e1", 4),
          ("ethernet", 2),
          ("other", 3))
    )





class AnsCCType(Integer32):
    """Custom type AnsCCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )





class AnsCCServiceClass(Integer32):
    """Custom type AnsCCServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr1", 1),
          ("cbr2", 2),
          ("ubr", 3))
    )





class AnsCCSourceType(Integer32):
    """Custom type AnsCCSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("epd", 2),
          ("normal", 1))
    )





class AnsCCMulti(Integer32):
    """Custom type AnsCCMulti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptmp", 2),
          ("ptp", 1))
    )





class AnsCCAdminStatus(Integer32):
    """Custom type AnsCCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )





class AnsAal1ParsType(Integer32):
    """Custom type AnsAal1ParsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("structured-contiguous", 2),
          ("structured-free", 3),
          ("unstructured", 1))
    )





class AnsAal1ParsTcMode(Integer32):
    """Custom type AnsAal1ParsTcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleyed", 2),
          ("immediate", 1),
          ("undefined", -1))
    )





class AnsAal1ParsTcType(Integer32):
    """Custom type AnsAal1ParsTcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0ais", 2),
          ("service-specific", 1),
          ("undefined", -1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Connections_ObjectIdentity = ObjectIdentity
connections = _Connections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4)
)
_AccessUserPort_ObjectIdentity = ObjectIdentity
accessUserPort = _AccessUserPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1)
)
_AnsAccessUserPortTable_Object = MibTable
ansAccessUserPortTable = _AnsAccessUserPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ansAccessUserPortTable.setStatus("mandatory")
_AnsAccessUserPortEntry_Object = MibTableRow
ansAccessUserPortEntry = _AnsAccessUserPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1)
)
ansAccessUserPortEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAccessUserPortSystemNode"),
    (0, "ANS-GS-MIB", "ansAccessUserPortSubrack"),
    (0, "ANS-GS-MIB", "ansAccessUserPortPosition"),
    (0, "ANS-GS-MIB", "ansAccessUserPortIndex"),
)
if mibBuilder.loadTexts:
    ansAccessUserPortEntry.setStatus("mandatory")
_AnsAccessUserPortSystemNode_Type = Integer32
_AnsAccessUserPortSystemNode_Object = MibTableColumn
ansAccessUserPortSystemNode = _AnsAccessUserPortSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 1),
    _AnsAccessUserPortSystemNode_Type()
)
ansAccessUserPortSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortSystemNode.setStatus("mandatory")
_AnsAccessUserPortSubrack_Type = Integer32
_AnsAccessUserPortSubrack_Object = MibTableColumn
ansAccessUserPortSubrack = _AnsAccessUserPortSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 2),
    _AnsAccessUserPortSubrack_Type()
)
ansAccessUserPortSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortSubrack.setStatus("mandatory")
_AnsAccessUserPortPosition_Type = Integer32
_AnsAccessUserPortPosition_Object = MibTableColumn
ansAccessUserPortPosition = _AnsAccessUserPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 3),
    _AnsAccessUserPortPosition_Type()
)
ansAccessUserPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortPosition.setStatus("mandatory")
_AnsAccessUserPortIndex_Type = Integer32
_AnsAccessUserPortIndex_Object = MibTableColumn
ansAccessUserPortIndex = _AnsAccessUserPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 4),
    _AnsAccessUserPortIndex_Type()
)
ansAccessUserPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortIndex.setStatus("mandatory")
_AnsAccessUserPortType_Type = AnsPortType
_AnsAccessUserPortType_Object = MibTableColumn
ansAccessUserPortType = _AnsAccessUserPortType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 5),
    _AnsAccessUserPortType_Type()
)
ansAccessUserPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortType.setStatus("mandatory")
_AnsAccessUserPortMaxBwDs_Type = Integer32
_AnsAccessUserPortMaxBwDs_Object = MibTableColumn
ansAccessUserPortMaxBwDs = _AnsAccessUserPortMaxBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 6),
    _AnsAccessUserPortMaxBwDs_Type()
)
ansAccessUserPortMaxBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortMaxBwDs.setStatus("mandatory")
_AnsAccessUserPortMaxBwUs_Type = Integer32
_AnsAccessUserPortMaxBwUs_Object = MibTableColumn
ansAccessUserPortMaxBwUs = _AnsAccessUserPortMaxBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 7),
    _AnsAccessUserPortMaxBwUs_Type()
)
ansAccessUserPortMaxBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortMaxBwUs.setStatus("mandatory")
_AnsAccessUserPortAvailBwDs_Type = Integer32
_AnsAccessUserPortAvailBwDs_Object = MibTableColumn
ansAccessUserPortAvailBwDs = _AnsAccessUserPortAvailBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 8),
    _AnsAccessUserPortAvailBwDs_Type()
)
ansAccessUserPortAvailBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortAvailBwDs.setStatus("mandatory")
_AnsAccessUserPortAvailBwUs_Type = Integer32
_AnsAccessUserPortAvailBwUs_Object = MibTableColumn
ansAccessUserPortAvailBwUs = _AnsAccessUserPortAvailBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 9),
    _AnsAccessUserPortAvailBwUs_Type()
)
ansAccessUserPortAvailBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortAvailBwUs.setStatus("mandatory")
_AnsAccessUserPortMinVpi_Type = Integer32
_AnsAccessUserPortMinVpi_Object = MibTableColumn
ansAccessUserPortMinVpi = _AnsAccessUserPortMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 10),
    _AnsAccessUserPortMinVpi_Type()
)
ansAccessUserPortMinVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortMinVpi.setStatus("mandatory")
_AnsAccessUserPortMaxVpi_Type = Integer32
_AnsAccessUserPortMaxVpi_Object = MibTableColumn
ansAccessUserPortMaxVpi = _AnsAccessUserPortMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 11),
    _AnsAccessUserPortMaxVpi_Type()
)
ansAccessUserPortMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortMaxVpi.setStatus("mandatory")
_AnsAccessUserPortMinVci_Type = Integer32
_AnsAccessUserPortMinVci_Object = MibTableColumn
ansAccessUserPortMinVci = _AnsAccessUserPortMinVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 12),
    _AnsAccessUserPortMinVci_Type()
)
ansAccessUserPortMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortMinVci.setStatus("mandatory")
_AnsAccessUserPortMaxVci_Type = Integer32
_AnsAccessUserPortMaxVci_Object = MibTableColumn
ansAccessUserPortMaxVci = _AnsAccessUserPortMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 13),
    _AnsAccessUserPortMaxVci_Type()
)
ansAccessUserPortMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortMaxVci.setStatus("mandatory")
_AnsAccessUserPortLabel_Type = DisplayString
_AnsAccessUserPortLabel_Object = MibTableColumn
ansAccessUserPortLabel = _AnsAccessUserPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 14),
    _AnsAccessUserPortLabel_Type()
)
ansAccessUserPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessUserPortLabel.setStatus("mandatory")


class _AnsAccessUserPortOperStatus_Type(Integer32):
    """Custom type ansAccessUserPortOperStatus based on Integer32"""
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


_AnsAccessUserPortOperStatus_Type.__name__ = "Integer32"
_AnsAccessUserPortOperStatus_Object = MibTableColumn
ansAccessUserPortOperStatus = _AnsAccessUserPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 15),
    _AnsAccessUserPortOperStatus_Type()
)
ansAccessUserPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortOperStatus.setStatus("mandatory")


class _AnsAccessUserPortAdminStatus_Type(Integer32):
    """Custom type ansAccessUserPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_AnsAccessUserPortAdminStatus_Type.__name__ = "Integer32"
_AnsAccessUserPortAdminStatus_Object = MibTableColumn
ansAccessUserPortAdminStatus = _AnsAccessUserPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 16),
    _AnsAccessUserPortAdminStatus_Type()
)
ansAccessUserPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessUserPortAdminStatus.setStatus("mandatory")


class _AnsAccessUserPortUsageState_Type(Integer32):
    """Custom type ansAccessUserPortUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_AnsAccessUserPortUsageState_Type.__name__ = "Integer32"
_AnsAccessUserPortUsageState_Object = MibTableColumn
ansAccessUserPortUsageState = _AnsAccessUserPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 17),
    _AnsAccessUserPortUsageState_Type()
)
ansAccessUserPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessUserPortUsageState.setStatus("mandatory")


class _AnsAccessUserPortAtmFormat_Type(Integer32):
    """Custom type ansAccessUserPortAtmFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_AnsAccessUserPortAtmFormat_Type.__name__ = "Integer32"
_AnsAccessUserPortAtmFormat_Object = MibTableColumn
ansAccessUserPortAtmFormat = _AnsAccessUserPortAtmFormat_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 1, 1, 1, 18),
    _AnsAccessUserPortAtmFormat_Type()
)
ansAccessUserPortAtmFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessUserPortAtmFormat.setStatus("mandatory")
_AccessServicePort_ObjectIdentity = ObjectIdentity
accessServicePort = _AccessServicePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2)
)
_AnsAccessServicePortTable_Object = MibTable
ansAccessServicePortTable = _AnsAccessServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ansAccessServicePortTable.setStatus("mandatory")
_AnsAccessServicePortEntry_Object = MibTableRow
ansAccessServicePortEntry = _AnsAccessServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1)
)
ansAccessServicePortEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAccessServicePortSystemNode"),
    (0, "ANS-GS-MIB", "ansAccessServicePortSubrack"),
    (0, "ANS-GS-MIB", "ansAccessServicePortPosition"),
    (0, "ANS-GS-MIB", "ansAccessServicePortIndex"),
)
if mibBuilder.loadTexts:
    ansAccessServicePortEntry.setStatus("mandatory")
_AnsAccessServicePortSystemNode_Type = Integer32
_AnsAccessServicePortSystemNode_Object = MibTableColumn
ansAccessServicePortSystemNode = _AnsAccessServicePortSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 1),
    _AnsAccessServicePortSystemNode_Type()
)
ansAccessServicePortSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortSystemNode.setStatus("mandatory")
_AnsAccessServicePortSubrack_Type = Integer32
_AnsAccessServicePortSubrack_Object = MibTableColumn
ansAccessServicePortSubrack = _AnsAccessServicePortSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 2),
    _AnsAccessServicePortSubrack_Type()
)
ansAccessServicePortSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortSubrack.setStatus("mandatory")
_AnsAccessServicePortPosition_Type = Integer32
_AnsAccessServicePortPosition_Object = MibTableColumn
ansAccessServicePortPosition = _AnsAccessServicePortPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 3),
    _AnsAccessServicePortPosition_Type()
)
ansAccessServicePortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortPosition.setStatus("mandatory")
_AnsAccessServicePortIndex_Type = Integer32
_AnsAccessServicePortIndex_Object = MibTableColumn
ansAccessServicePortIndex = _AnsAccessServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 4),
    _AnsAccessServicePortIndex_Type()
)
ansAccessServicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortIndex.setStatus("mandatory")
_AnsAccessServicePortLabel_Type = DisplayString
_AnsAccessServicePortLabel_Object = MibTableColumn
ansAccessServicePortLabel = _AnsAccessServicePortLabel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 5),
    _AnsAccessServicePortLabel_Type()
)
ansAccessServicePortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessServicePortLabel.setStatus("mandatory")
_AnsAccessServicePortMaxBwDs_Type = Integer32
_AnsAccessServicePortMaxBwDs_Object = MibTableColumn
ansAccessServicePortMaxBwDs = _AnsAccessServicePortMaxBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 6),
    _AnsAccessServicePortMaxBwDs_Type()
)
ansAccessServicePortMaxBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortMaxBwDs.setStatus("mandatory")
_AnsAccessServicePortMaxBwUs_Type = Integer32
_AnsAccessServicePortMaxBwUs_Object = MibTableColumn
ansAccessServicePortMaxBwUs = _AnsAccessServicePortMaxBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 7),
    _AnsAccessServicePortMaxBwUs_Type()
)
ansAccessServicePortMaxBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortMaxBwUs.setStatus("mandatory")
_AnsAccessServicePortAvailBwDs_Type = Integer32
_AnsAccessServicePortAvailBwDs_Object = MibTableColumn
ansAccessServicePortAvailBwDs = _AnsAccessServicePortAvailBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 8),
    _AnsAccessServicePortAvailBwDs_Type()
)
ansAccessServicePortAvailBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortAvailBwDs.setStatus("mandatory")
_AnsAccessServicePortAvailBwUs_Type = Integer32
_AnsAccessServicePortAvailBwUs_Object = MibTableColumn
ansAccessServicePortAvailBwUs = _AnsAccessServicePortAvailBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 9),
    _AnsAccessServicePortAvailBwUs_Type()
)
ansAccessServicePortAvailBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortAvailBwUs.setStatus("mandatory")
_AnsAccessServicePortMinVpi_Type = Integer32
_AnsAccessServicePortMinVpi_Object = MibTableColumn
ansAccessServicePortMinVpi = _AnsAccessServicePortMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 10),
    _AnsAccessServicePortMinVpi_Type()
)
ansAccessServicePortMinVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortMinVpi.setStatus("mandatory")
_AnsAccessServicePortMaxVpi_Type = Integer32
_AnsAccessServicePortMaxVpi_Object = MibTableColumn
ansAccessServicePortMaxVpi = _AnsAccessServicePortMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 11),
    _AnsAccessServicePortMaxVpi_Type()
)
ansAccessServicePortMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortMaxVpi.setStatus("mandatory")
_AnsAccessServicePortMinVci_Type = Integer32
_AnsAccessServicePortMinVci_Object = MibTableColumn
ansAccessServicePortMinVci = _AnsAccessServicePortMinVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 12),
    _AnsAccessServicePortMinVci_Type()
)
ansAccessServicePortMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortMinVci.setStatus("mandatory")
_AnsAccessServicePortMaxVci_Type = Integer32
_AnsAccessServicePortMaxVci_Object = MibTableColumn
ansAccessServicePortMaxVci = _AnsAccessServicePortMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 13),
    _AnsAccessServicePortMaxVci_Type()
)
ansAccessServicePortMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortMaxVci.setStatus("mandatory")


class _AnsAccessServicePortOperStatus_Type(Integer32):
    """Custom type ansAccessServicePortOperStatus based on Integer32"""
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


_AnsAccessServicePortOperStatus_Type.__name__ = "Integer32"
_AnsAccessServicePortOperStatus_Object = MibTableColumn
ansAccessServicePortOperStatus = _AnsAccessServicePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 14),
    _AnsAccessServicePortOperStatus_Type()
)
ansAccessServicePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortOperStatus.setStatus("mandatory")


class _AnsAccessServicePortAdminStatus_Type(Integer32):
    """Custom type ansAccessServicePortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_AnsAccessServicePortAdminStatus_Type.__name__ = "Integer32"
_AnsAccessServicePortAdminStatus_Object = MibTableColumn
ansAccessServicePortAdminStatus = _AnsAccessServicePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 15),
    _AnsAccessServicePortAdminStatus_Type()
)
ansAccessServicePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessServicePortAdminStatus.setStatus("mandatory")


class _AnsAccessServicePortUsageState_Type(Integer32):
    """Custom type ansAccessServicePortUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_AnsAccessServicePortUsageState_Type.__name__ = "Integer32"
_AnsAccessServicePortUsageState_Object = MibTableColumn
ansAccessServicePortUsageState = _AnsAccessServicePortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 16),
    _AnsAccessServicePortUsageState_Type()
)
ansAccessServicePortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortUsageState.setStatus("mandatory")


class _AnsAccessServicePortAtmFormat_Type(Integer32):
    """Custom type ansAccessServicePortAtmFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_AnsAccessServicePortAtmFormat_Type.__name__ = "Integer32"
_AnsAccessServicePortAtmFormat_Object = MibTableColumn
ansAccessServicePortAtmFormat = _AnsAccessServicePortAtmFormat_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 17),
    _AnsAccessServicePortAtmFormat_Type()
)
ansAccessServicePortAtmFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessServicePortAtmFormat.setStatus("mandatory")
_AnsAccessServicePortType_Type = AnsPortType
_AnsAccessServicePortType_Object = MibTableColumn
ansAccessServicePortType = _AnsAccessServicePortType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 2, 1, 1, 18),
    _AnsAccessServicePortType_Type()
)
ansAccessServicePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServicePortType.setStatus("mandatory")
_AccessServiceUserPort_ObjectIdentity = ObjectIdentity
accessServiceUserPort = _AccessServiceUserPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3)
)
_AnsAccessServiceUserPortTable_Object = MibTable
ansAccessServiceUserPortTable = _AnsAccessServiceUserPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ansAccessServiceUserPortTable.setStatus("mandatory")
_AnsAccessServiceUserPortEntry_Object = MibTableRow
ansAccessServiceUserPortEntry = _AnsAccessServiceUserPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1)
)
ansAccessServiceUserPortEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAccessServiceUserPortSystemNode"),
    (0, "ANS-GS-MIB", "ansAccessServiceUserPortSubrack"),
    (0, "ANS-GS-MIB", "ansAccessServiceUserPortPosition"),
    (0, "ANS-GS-MIB", "ansAccessServiceUserPortIndex"),
)
if mibBuilder.loadTexts:
    ansAccessServiceUserPortEntry.setStatus("mandatory")
_AnsAccessServiceUserPortSystemNode_Type = Integer32
_AnsAccessServiceUserPortSystemNode_Object = MibTableColumn
ansAccessServiceUserPortSystemNode = _AnsAccessServiceUserPortSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 1),
    _AnsAccessServiceUserPortSystemNode_Type()
)
ansAccessServiceUserPortSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortSystemNode.setStatus("mandatory")
_AnsAccessServiceUserPortSubrack_Type = Integer32
_AnsAccessServiceUserPortSubrack_Object = MibTableColumn
ansAccessServiceUserPortSubrack = _AnsAccessServiceUserPortSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 2),
    _AnsAccessServiceUserPortSubrack_Type()
)
ansAccessServiceUserPortSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortSubrack.setStatus("mandatory")
_AnsAccessServiceUserPortPosition_Type = Integer32
_AnsAccessServiceUserPortPosition_Object = MibTableColumn
ansAccessServiceUserPortPosition = _AnsAccessServiceUserPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 3),
    _AnsAccessServiceUserPortPosition_Type()
)
ansAccessServiceUserPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortPosition.setStatus("mandatory")
_AnsAccessServiceUserPortIndex_Type = Integer32
_AnsAccessServiceUserPortIndex_Object = MibTableColumn
ansAccessServiceUserPortIndex = _AnsAccessServiceUserPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 4),
    _AnsAccessServiceUserPortIndex_Type()
)
ansAccessServiceUserPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortIndex.setStatus("mandatory")
_AnsAccessServiceUserPortLabel_Type = DisplayString
_AnsAccessServiceUserPortLabel_Object = MibTableColumn
ansAccessServiceUserPortLabel = _AnsAccessServiceUserPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 5),
    _AnsAccessServiceUserPortLabel_Type()
)
ansAccessServiceUserPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortLabel.setStatus("mandatory")
_AnsAccessServiceUserPortMaxBwDs_Type = Integer32
_AnsAccessServiceUserPortMaxBwDs_Object = MibTableColumn
ansAccessServiceUserPortMaxBwDs = _AnsAccessServiceUserPortMaxBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 6),
    _AnsAccessServiceUserPortMaxBwDs_Type()
)
ansAccessServiceUserPortMaxBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortMaxBwDs.setStatus("mandatory")
_AnsAccessServiceUserPortMaxBwUs_Type = Integer32
_AnsAccessServiceUserPortMaxBwUs_Object = MibTableColumn
ansAccessServiceUserPortMaxBwUs = _AnsAccessServiceUserPortMaxBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 7),
    _AnsAccessServiceUserPortMaxBwUs_Type()
)
ansAccessServiceUserPortMaxBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortMaxBwUs.setStatus("mandatory")
_AnsAccessServiceUserPortAvailBwDs_Type = Integer32
_AnsAccessServiceUserPortAvailBwDs_Object = MibTableColumn
ansAccessServiceUserPortAvailBwDs = _AnsAccessServiceUserPortAvailBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 8),
    _AnsAccessServiceUserPortAvailBwDs_Type()
)
ansAccessServiceUserPortAvailBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortAvailBwDs.setStatus("mandatory")
_AnsAccessServiceUserPortAvailBwUs_Type = Integer32
_AnsAccessServiceUserPortAvailBwUs_Object = MibTableColumn
ansAccessServiceUserPortAvailBwUs = _AnsAccessServiceUserPortAvailBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 9),
    _AnsAccessServiceUserPortAvailBwUs_Type()
)
ansAccessServiceUserPortAvailBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortAvailBwUs.setStatus("mandatory")
_AnsAccessServiceUserPortMinVpi_Type = Integer32
_AnsAccessServiceUserPortMinVpi_Object = MibTableColumn
ansAccessServiceUserPortMinVpi = _AnsAccessServiceUserPortMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 10),
    _AnsAccessServiceUserPortMinVpi_Type()
)
ansAccessServiceUserPortMinVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortMinVpi.setStatus("mandatory")
_AnsAccessServiceUserPortMaxVpi_Type = Integer32
_AnsAccessServiceUserPortMaxVpi_Object = MibTableColumn
ansAccessServiceUserPortMaxVpi = _AnsAccessServiceUserPortMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 11),
    _AnsAccessServiceUserPortMaxVpi_Type()
)
ansAccessServiceUserPortMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortMaxVpi.setStatus("mandatory")
_AnsAccessServiceUserPortMinVci_Type = Integer32
_AnsAccessServiceUserPortMinVci_Object = MibTableColumn
ansAccessServiceUserPortMinVci = _AnsAccessServiceUserPortMinVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 12),
    _AnsAccessServiceUserPortMinVci_Type()
)
ansAccessServiceUserPortMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortMinVci.setStatus("mandatory")
_AnsAccessServiceUserPortMaxVci_Type = Integer32
_AnsAccessServiceUserPortMaxVci_Object = MibTableColumn
ansAccessServiceUserPortMaxVci = _AnsAccessServiceUserPortMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 13),
    _AnsAccessServiceUserPortMaxVci_Type()
)
ansAccessServiceUserPortMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortMaxVci.setStatus("mandatory")


class _AnsAccessServiceUserPortOperStatus_Type(Integer32):
    """Custom type ansAccessServiceUserPortOperStatus based on Integer32"""
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


_AnsAccessServiceUserPortOperStatus_Type.__name__ = "Integer32"
_AnsAccessServiceUserPortOperStatus_Object = MibTableColumn
ansAccessServiceUserPortOperStatus = _AnsAccessServiceUserPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 14),
    _AnsAccessServiceUserPortOperStatus_Type()
)
ansAccessServiceUserPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortOperStatus.setStatus("mandatory")


class _AnsAccessServiceUserPortAdminStatus_Type(Integer32):
    """Custom type ansAccessServiceUserPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_AnsAccessServiceUserPortAdminStatus_Type.__name__ = "Integer32"
_AnsAccessServiceUserPortAdminStatus_Object = MibTableColumn
ansAccessServiceUserPortAdminStatus = _AnsAccessServiceUserPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 15),
    _AnsAccessServiceUserPortAdminStatus_Type()
)
ansAccessServiceUserPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortAdminStatus.setStatus("mandatory")


class _AnsAccessServiceUserPortUsageState_Type(Integer32):
    """Custom type ansAccessServiceUserPortUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_AnsAccessServiceUserPortUsageState_Type.__name__ = "Integer32"
_AnsAccessServiceUserPortUsageState_Object = MibTableColumn
ansAccessServiceUserPortUsageState = _AnsAccessServiceUserPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 16),
    _AnsAccessServiceUserPortUsageState_Type()
)
ansAccessServiceUserPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortUsageState.setStatus("mandatory")


class _AnsAccessServiceUserPortAtmFormat_Type(Integer32):
    """Custom type ansAccessServiceUserPortAtmFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_AnsAccessServiceUserPortAtmFormat_Type.__name__ = "Integer32"
_AnsAccessServiceUserPortAtmFormat_Object = MibTableColumn
ansAccessServiceUserPortAtmFormat = _AnsAccessServiceUserPortAtmFormat_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 17),
    _AnsAccessServiceUserPortAtmFormat_Type()
)
ansAccessServiceUserPortAtmFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortAtmFormat.setStatus("mandatory")
_AnsAccessServiceUserPortType_Type = AnsPortType
_AnsAccessServiceUserPortType_Object = MibTableColumn
ansAccessServiceUserPortType = _AnsAccessServiceUserPortType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 3, 1, 1, 18),
    _AnsAccessServiceUserPortType_Type()
)
ansAccessServiceUserPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessServiceUserPortType.setStatus("mandatory")
_AccessInternalPort_ObjectIdentity = ObjectIdentity
accessInternalPort = _AccessInternalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4)
)
_AnsAccessInternalPortTable_Object = MibTable
ansAccessInternalPortTable = _AnsAccessInternalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ansAccessInternalPortTable.setStatus("mandatory")
_AnsAccessInternalPortEntry_Object = MibTableRow
ansAccessInternalPortEntry = _AnsAccessInternalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1)
)
ansAccessInternalPortEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAccessInternalPortSystemNode"),
    (0, "ANS-GS-MIB", "ansAccessInternalPortSubrack"),
    (0, "ANS-GS-MIB", "ansAccessInternalPortPosition"),
    (0, "ANS-GS-MIB", "ansAccessInternalPortIndex"),
)
if mibBuilder.loadTexts:
    ansAccessInternalPortEntry.setStatus("mandatory")
_AnsAccessInternalPortSystemNode_Type = Integer32
_AnsAccessInternalPortSystemNode_Object = MibTableColumn
ansAccessInternalPortSystemNode = _AnsAccessInternalPortSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 1),
    _AnsAccessInternalPortSystemNode_Type()
)
ansAccessInternalPortSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortSystemNode.setStatus("mandatory")
_AnsAccessInternalPortSubrack_Type = Integer32
_AnsAccessInternalPortSubrack_Object = MibTableColumn
ansAccessInternalPortSubrack = _AnsAccessInternalPortSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 2),
    _AnsAccessInternalPortSubrack_Type()
)
ansAccessInternalPortSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortSubrack.setStatus("mandatory")
_AnsAccessInternalPortPosition_Type = Integer32
_AnsAccessInternalPortPosition_Object = MibTableColumn
ansAccessInternalPortPosition = _AnsAccessInternalPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 3),
    _AnsAccessInternalPortPosition_Type()
)
ansAccessInternalPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortPosition.setStatus("mandatory")
_AnsAccessInternalPortIndex_Type = Integer32
_AnsAccessInternalPortIndex_Object = MibTableColumn
ansAccessInternalPortIndex = _AnsAccessInternalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 4),
    _AnsAccessInternalPortIndex_Type()
)
ansAccessInternalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortIndex.setStatus("mandatory")
_AnsAccessInternalPortLabel_Type = DisplayString
_AnsAccessInternalPortLabel_Object = MibTableColumn
ansAccessInternalPortLabel = _AnsAccessInternalPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 5),
    _AnsAccessInternalPortLabel_Type()
)
ansAccessInternalPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessInternalPortLabel.setStatus("mandatory")
_AnsAccessInternalPortMaxBwDs_Type = Integer32
_AnsAccessInternalPortMaxBwDs_Object = MibTableColumn
ansAccessInternalPortMaxBwDs = _AnsAccessInternalPortMaxBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 6),
    _AnsAccessInternalPortMaxBwDs_Type()
)
ansAccessInternalPortMaxBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortMaxBwDs.setStatus("mandatory")
_AnsAccessInternalPortMaxBwUs_Type = Integer32
_AnsAccessInternalPortMaxBwUs_Object = MibTableColumn
ansAccessInternalPortMaxBwUs = _AnsAccessInternalPortMaxBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 7),
    _AnsAccessInternalPortMaxBwUs_Type()
)
ansAccessInternalPortMaxBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortMaxBwUs.setStatus("mandatory")
_AnsAccessInternalPortAvailBwDs_Type = Integer32
_AnsAccessInternalPortAvailBwDs_Object = MibTableColumn
ansAccessInternalPortAvailBwDs = _AnsAccessInternalPortAvailBwDs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 8),
    _AnsAccessInternalPortAvailBwDs_Type()
)
ansAccessInternalPortAvailBwDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortAvailBwDs.setStatus("mandatory")
_AnsAccessInternalPortAvailBwUs_Type = Integer32
_AnsAccessInternalPortAvailBwUs_Object = MibTableColumn
ansAccessInternalPortAvailBwUs = _AnsAccessInternalPortAvailBwUs_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 9),
    _AnsAccessInternalPortAvailBwUs_Type()
)
ansAccessInternalPortAvailBwUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortAvailBwUs.setStatus("mandatory")
_AnsAccessInternalPortMinVpi_Type = Integer32
_AnsAccessInternalPortMinVpi_Object = MibTableColumn
ansAccessInternalPortMinVpi = _AnsAccessInternalPortMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 10),
    _AnsAccessInternalPortMinVpi_Type()
)
ansAccessInternalPortMinVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortMinVpi.setStatus("mandatory")
_AnsAccessInternalPortMaxVpi_Type = Integer32
_AnsAccessInternalPortMaxVpi_Object = MibTableColumn
ansAccessInternalPortMaxVpi = _AnsAccessInternalPortMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 11),
    _AnsAccessInternalPortMaxVpi_Type()
)
ansAccessInternalPortMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortMaxVpi.setStatus("mandatory")
_AnsAccessInternalPortMinVci_Type = Integer32
_AnsAccessInternalPortMinVci_Object = MibTableColumn
ansAccessInternalPortMinVci = _AnsAccessInternalPortMinVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 12),
    _AnsAccessInternalPortMinVci_Type()
)
ansAccessInternalPortMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortMinVci.setStatus("mandatory")
_AnsAccessInternalPortMaxVci_Type = Integer32
_AnsAccessInternalPortMaxVci_Object = MibTableColumn
ansAccessInternalPortMaxVci = _AnsAccessInternalPortMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 13),
    _AnsAccessInternalPortMaxVci_Type()
)
ansAccessInternalPortMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortMaxVci.setStatus("mandatory")


class _AnsAccessInternalPortOperStatus_Type(Integer32):
    """Custom type ansAccessInternalPortOperStatus based on Integer32"""
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


_AnsAccessInternalPortOperStatus_Type.__name__ = "Integer32"
_AnsAccessInternalPortOperStatus_Object = MibTableColumn
ansAccessInternalPortOperStatus = _AnsAccessInternalPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 14),
    _AnsAccessInternalPortOperStatus_Type()
)
ansAccessInternalPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortOperStatus.setStatus("mandatory")


class _AnsAccessInternalPortAdminStatus_Type(Integer32):
    """Custom type ansAccessInternalPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_AnsAccessInternalPortAdminStatus_Type.__name__ = "Integer32"
_AnsAccessInternalPortAdminStatus_Object = MibTableColumn
ansAccessInternalPortAdminStatus = _AnsAccessInternalPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 15),
    _AnsAccessInternalPortAdminStatus_Type()
)
ansAccessInternalPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessInternalPortAdminStatus.setStatus("mandatory")


class _AnsAccessInternalPortUsageState_Type(Integer32):
    """Custom type ansAccessInternalPortUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_AnsAccessInternalPortUsageState_Type.__name__ = "Integer32"
_AnsAccessInternalPortUsageState_Object = MibTableColumn
ansAccessInternalPortUsageState = _AnsAccessInternalPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 16),
    _AnsAccessInternalPortUsageState_Type()
)
ansAccessInternalPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortUsageState.setStatus("mandatory")


class _AnsAccessInternalPortAtmFormat_Type(Integer32):
    """Custom type ansAccessInternalPortAtmFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_AnsAccessInternalPortAtmFormat_Type.__name__ = "Integer32"
_AnsAccessInternalPortAtmFormat_Object = MibTableColumn
ansAccessInternalPortAtmFormat = _AnsAccessInternalPortAtmFormat_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 17),
    _AnsAccessInternalPortAtmFormat_Type()
)
ansAccessInternalPortAtmFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAccessInternalPortAtmFormat.setStatus("mandatory")
_AnsAccessInternalPortType_Type = AnsPortType
_AnsAccessInternalPortType_Object = MibTableColumn
ansAccessInternalPortType = _AnsAccessInternalPortType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 4, 1, 1, 18),
    _AnsAccessInternalPortType_Type()
)
ansAccessInternalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAccessInternalPortType.setStatus("mandatory")
_AnsAtmCreateCC_ObjectIdentity = ObjectIdentity
ansAtmCreateCC = _AnsAtmCreateCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5)
)
_AnsAtmCreateCCTable_Object = MibTable
ansAtmCreateCCTable = _AnsAtmCreateCCTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ansAtmCreateCCTable.setStatus("mandatory")
_AnsAtmCreateCCEntry_Object = MibTableRow
ansAtmCreateCCEntry = _AnsAtmCreateCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1)
)
ansAtmCreateCCEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAtmCCAUPSystemNode"),
    (0, "ANS-GS-MIB", "ansAtmCCAUPSubrack"),
    (0, "ANS-GS-MIB", "ansAtmCCAUPPosition"),
    (0, "ANS-GS-MIB", "ansAtmCCAUPIndex"),
    (0, "ANS-GS-MIB", "ansAtmCCAUPVPI"),
    (0, "ANS-GS-MIB", "ansAtmCCAUPVCI"),
)
if mibBuilder.loadTexts:
    ansAtmCreateCCEntry.setStatus("mandatory")
_AnsAtmCCAUPSystemNode_Type = Integer32
_AnsAtmCCAUPSystemNode_Object = MibTableColumn
ansAtmCCAUPSystemNode = _AnsAtmCCAUPSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 1),
    _AnsAtmCCAUPSystemNode_Type()
)
ansAtmCCAUPSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAtmCCAUPSystemNode.setStatus("mandatory")
_AnsAtmCCAUPSubrack_Type = Integer32
_AnsAtmCCAUPSubrack_Object = MibTableColumn
ansAtmCCAUPSubrack = _AnsAtmCCAUPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 2),
    _AnsAtmCCAUPSubrack_Type()
)
ansAtmCCAUPSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAtmCCAUPSubrack.setStatus("mandatory")
_AnsAtmCCAUPPosition_Type = Integer32
_AnsAtmCCAUPPosition_Object = MibTableColumn
ansAtmCCAUPPosition = _AnsAtmCCAUPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 3),
    _AnsAtmCCAUPPosition_Type()
)
ansAtmCCAUPPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAtmCCAUPPosition.setStatus("mandatory")
_AnsAtmCCAUPIndex_Type = Integer32
_AnsAtmCCAUPIndex_Object = MibTableColumn
ansAtmCCAUPIndex = _AnsAtmCCAUPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 4),
    _AnsAtmCCAUPIndex_Type()
)
ansAtmCCAUPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAtmCCAUPIndex.setStatus("mandatory")
_AnsAtmCCAUPVPI_Type = Integer32
_AnsAtmCCAUPVPI_Object = MibTableColumn
ansAtmCCAUPVPI = _AnsAtmCCAUPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 5),
    _AnsAtmCCAUPVPI_Type()
)
ansAtmCCAUPVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAtmCCAUPVPI.setStatus("mandatory")
_AnsAtmCCAUPVCI_Type = Integer32
_AnsAtmCCAUPVCI_Object = MibTableColumn
ansAtmCCAUPVCI = _AnsAtmCCAUPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 6),
    _AnsAtmCCAUPVCI_Type()
)
ansAtmCCAUPVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAtmCCAUPVCI.setStatus("mandatory")
_AnsAtmCCASPSubrack_Type = Integer32
_AnsAtmCCASPSubrack_Object = MibTableColumn
ansAtmCCASPSubrack = _AnsAtmCCASPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 7),
    _AnsAtmCCASPSubrack_Type()
)
ansAtmCCASPSubrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCASPSubrack.setStatus("mandatory")
_AnsAtmCCASPPosition_Type = Integer32
_AnsAtmCCASPPosition_Object = MibTableColumn
ansAtmCCASPPosition = _AnsAtmCCASPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 8),
    _AnsAtmCCASPPosition_Type()
)
ansAtmCCASPPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCASPPosition.setStatus("mandatory")
_AnsAtmCCASPIndex_Type = Integer32
_AnsAtmCCASPIndex_Object = MibTableColumn
ansAtmCCASPIndex = _AnsAtmCCASPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 9),
    _AnsAtmCCASPIndex_Type()
)
ansAtmCCASPIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCASPIndex.setStatus("mandatory")
_AnsAtmCCASPVPI_Type = Integer32
_AnsAtmCCASPVPI_Object = MibTableColumn
ansAtmCCASPVPI = _AnsAtmCCASPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 10),
    _AnsAtmCCASPVPI_Type()
)
ansAtmCCASPVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCASPVPI.setStatus("mandatory")
_AnsAtmCCASPVCI_Type = Integer32
_AnsAtmCCASPVCI_Object = MibTableColumn
ansAtmCCASPVCI = _AnsAtmCCASPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 11),
    _AnsAtmCCASPVCI_Type()
)
ansAtmCCASPVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCASPVCI.setStatus("mandatory")
_AnsAtmCCType_Type = AnsCCType
_AnsAtmCCType_Object = MibTableColumn
ansAtmCCType = _AnsAtmCCType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 12),
    _AnsAtmCCType_Type()
)
ansAtmCCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCType.setStatus("mandatory")
_AnsAtmCCServiceClass_Type = AnsCCServiceClass
_AnsAtmCCServiceClass_Object = MibTableColumn
ansAtmCCServiceClass = _AnsAtmCCServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 13),
    _AnsAtmCCServiceClass_Type()
)
ansAtmCCServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCServiceClass.setStatus("mandatory")
_AnsAtmCCSourceType_Type = AnsCCSourceType
_AnsAtmCCSourceType_Object = MibTableColumn
ansAtmCCSourceType = _AnsAtmCCSourceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 14),
    _AnsAtmCCSourceType_Type()
)
ansAtmCCSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCSourceType.setStatus("mandatory")


class _AnsAtmCCServiceType_Type(Integer32):
    """Custom type ansAtmCCServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("ethernet", 3))
    )


_AnsAtmCCServiceType_Type.__name__ = "Integer32"
_AnsAtmCCServiceType_Object = MibTableColumn
ansAtmCCServiceType = _AnsAtmCCServiceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 15),
    _AnsAtmCCServiceType_Type()
)
ansAtmCCServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCServiceType.setStatus("mandatory")
_AnsAtmCCPcrAtoB_Type = Integer32
_AnsAtmCCPcrAtoB_Object = MibTableColumn
ansAtmCCPcrAtoB = _AnsAtmCCPcrAtoB_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 16),
    _AnsAtmCCPcrAtoB_Type()
)
ansAtmCCPcrAtoB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCPcrAtoB.setStatus("mandatory")
_AnsAtmCCPcrBtoA_Type = Integer32
_AnsAtmCCPcrBtoA_Object = MibTableColumn
ansAtmCCPcrBtoA = _AnsAtmCCPcrBtoA_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 17),
    _AnsAtmCCPcrBtoA_Type()
)
ansAtmCCPcrBtoA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCPcrBtoA.setStatus("mandatory")
_AnsAtmCCMulti_Type = AnsCCMulti
_AnsAtmCCMulti_Object = MibTableColumn
ansAtmCCMulti = _AnsAtmCCMulti_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 18),
    _AnsAtmCCMulti_Type()
)
ansAtmCCMulti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCMulti.setStatus("mandatory")
_AnsAtmCCAdminStatus_Type = AnsCCAdminStatus
_AnsAtmCCAdminStatus_Object = MibTableColumn
ansAtmCCAdminStatus = _AnsAtmCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 19),
    _AnsAtmCCAdminStatus_Type()
)
ansAtmCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCAdminStatus.setStatus("mandatory")
_AnsAtmCCRowStatus_Type = RowStatus
_AnsAtmCCRowStatus_Object = MibTableColumn
ansAtmCCRowStatus = _AnsAtmCCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 5, 1, 1, 20),
    _AnsAtmCCRowStatus_Type()
)
ansAtmCCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAtmCCRowStatus.setStatus("mandatory")
_AnsCeAtmCreateCC_ObjectIdentity = ObjectIdentity
ansCeAtmCreateCC = _AnsCeAtmCreateCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6)
)
_AnsCeAtmCreateCCTable_Object = MibTable
ansCeAtmCreateCCTable = _AnsCeAtmCreateCCTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ansCeAtmCreateCCTable.setStatus("mandatory")
_AnsCeAtmCreateCCEntry_Object = MibTableRow
ansCeAtmCreateCCEntry = _AnsCeAtmCreateCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1)
)
ansCeAtmCreateCCEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansCeAtmCCAUPSystemNode"),
    (0, "ANS-GS-MIB", "ansCeAtmCCAUPSubrack"),
    (0, "ANS-GS-MIB", "ansCeAtmCCAUPPosition"),
    (0, "ANS-GS-MIB", "ansCeAtmCCAUPIndex"),
    (0, "ANS-GS-MIB", "ansCeAtmCCAUPVPI"),
    (0, "ANS-GS-MIB", "ansCeAtmCCAUPVCI"),
)
if mibBuilder.loadTexts:
    ansCeAtmCreateCCEntry.setStatus("mandatory")
_AnsCeAtmCCAUPSystemNode_Type = Integer32
_AnsCeAtmCCAUPSystemNode_Object = MibTableColumn
ansCeAtmCCAUPSystemNode = _AnsCeAtmCCAUPSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 1),
    _AnsCeAtmCCAUPSystemNode_Type()
)
ansCeAtmCCAUPSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeAtmCCAUPSystemNode.setStatus("mandatory")
_AnsCeAtmCCAUPSubrack_Type = Integer32
_AnsCeAtmCCAUPSubrack_Object = MibTableColumn
ansCeAtmCCAUPSubrack = _AnsCeAtmCCAUPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 2),
    _AnsCeAtmCCAUPSubrack_Type()
)
ansCeAtmCCAUPSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeAtmCCAUPSubrack.setStatus("mandatory")
_AnsCeAtmCCAUPPosition_Type = Integer32
_AnsCeAtmCCAUPPosition_Object = MibTableColumn
ansCeAtmCCAUPPosition = _AnsCeAtmCCAUPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 3),
    _AnsCeAtmCCAUPPosition_Type()
)
ansCeAtmCCAUPPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeAtmCCAUPPosition.setStatus("mandatory")
_AnsCeAtmCCAUPIndex_Type = Integer32
_AnsCeAtmCCAUPIndex_Object = MibTableColumn
ansCeAtmCCAUPIndex = _AnsCeAtmCCAUPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 4),
    _AnsCeAtmCCAUPIndex_Type()
)
ansCeAtmCCAUPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeAtmCCAUPIndex.setStatus("mandatory")
_AnsCeAtmCCAUPVPI_Type = Integer32
_AnsCeAtmCCAUPVPI_Object = MibTableColumn
ansCeAtmCCAUPVPI = _AnsCeAtmCCAUPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 5),
    _AnsCeAtmCCAUPVPI_Type()
)
ansCeAtmCCAUPVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeAtmCCAUPVPI.setStatus("mandatory")
_AnsCeAtmCCAUPVCI_Type = Integer32
_AnsCeAtmCCAUPVCI_Object = MibTableColumn
ansCeAtmCCAUPVCI = _AnsCeAtmCCAUPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 6),
    _AnsCeAtmCCAUPVCI_Type()
)
ansCeAtmCCAUPVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeAtmCCAUPVCI.setStatus("mandatory")
_AnsCeAtmCCASPSubrack_Type = Integer32
_AnsCeAtmCCASPSubrack_Object = MibTableColumn
ansCeAtmCCASPSubrack = _AnsCeAtmCCASPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 7),
    _AnsCeAtmCCASPSubrack_Type()
)
ansCeAtmCCASPSubrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCASPSubrack.setStatus("mandatory")
_AnsCeAtmCCASPPosition_Type = Integer32
_AnsCeAtmCCASPPosition_Object = MibTableColumn
ansCeAtmCCASPPosition = _AnsCeAtmCCASPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 8),
    _AnsCeAtmCCASPPosition_Type()
)
ansCeAtmCCASPPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCASPPosition.setStatus("mandatory")
_AnsCeAtmCCASPIndex_Type = Integer32
_AnsCeAtmCCASPIndex_Object = MibTableColumn
ansCeAtmCCASPIndex = _AnsCeAtmCCASPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 9),
    _AnsCeAtmCCASPIndex_Type()
)
ansCeAtmCCASPIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCASPIndex.setStatus("mandatory")
_AnsCeAtmCCASPVPI_Type = Integer32
_AnsCeAtmCCASPVPI_Object = MibTableColumn
ansCeAtmCCASPVPI = _AnsCeAtmCCASPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 10),
    _AnsCeAtmCCASPVPI_Type()
)
ansCeAtmCCASPVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCASPVPI.setStatus("mandatory")
_AnsCeAtmCCASPVCI_Type = Integer32
_AnsCeAtmCCASPVCI_Object = MibTableColumn
ansCeAtmCCASPVCI = _AnsCeAtmCCASPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 11),
    _AnsCeAtmCCASPVCI_Type()
)
ansCeAtmCCASPVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCASPVCI.setStatus("mandatory")
_AnsCeAtmCCType_Type = AnsCCType
_AnsCeAtmCCType_Object = MibTableColumn
ansCeAtmCCType = _AnsCeAtmCCType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 12),
    _AnsCeAtmCCType_Type()
)
ansCeAtmCCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCType.setStatus("mandatory")
_AnsCeAtmCCServiceClass_Type = AnsCCServiceClass
_AnsCeAtmCCServiceClass_Object = MibTableColumn
ansCeAtmCCServiceClass = _AnsCeAtmCCServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 13),
    _AnsCeAtmCCServiceClass_Type()
)
ansCeAtmCCServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCServiceClass.setStatus("mandatory")
_AnsCeAtmCCSourceType_Type = AnsCCSourceType
_AnsCeAtmCCSourceType_Object = MibTableColumn
ansCeAtmCCSourceType = _AnsCeAtmCCSourceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 14),
    _AnsCeAtmCCSourceType_Type()
)
ansCeAtmCCSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCSourceType.setStatus("mandatory")
_AnsCeAtmCCPcrAtoB_Type = Integer32
_AnsCeAtmCCPcrAtoB_Object = MibTableColumn
ansCeAtmCCPcrAtoB = _AnsCeAtmCCPcrAtoB_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 15),
    _AnsCeAtmCCPcrAtoB_Type()
)
ansCeAtmCCPcrAtoB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCPcrAtoB.setStatus("mandatory")
_AnsCeAtmCCPcrBtoA_Type = Integer32
_AnsCeAtmCCPcrBtoA_Object = MibTableColumn
ansCeAtmCCPcrBtoA = _AnsCeAtmCCPcrBtoA_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 16),
    _AnsCeAtmCCPcrBtoA_Type()
)
ansCeAtmCCPcrBtoA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCPcrBtoA.setStatus("mandatory")
_AnsCeAtmCCMulti_Type = AnsCCMulti
_AnsCeAtmCCMulti_Object = MibTableColumn
ansCeAtmCCMulti = _AnsCeAtmCCMulti_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 17),
    _AnsCeAtmCCMulti_Type()
)
ansCeAtmCCMulti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCMulti.setStatus("mandatory")
_AnsCeAtmCCAdminStatus_Type = AnsCCAdminStatus
_AnsCeAtmCCAdminStatus_Object = MibTableColumn
ansCeAtmCCAdminStatus = _AnsCeAtmCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 18),
    _AnsCeAtmCCAdminStatus_Type()
)
ansCeAtmCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCAdminStatus.setStatus("mandatory")
_AnsCeAtmCCTimeSlotPa_Type = DisplayString
_AnsCeAtmCCTimeSlotPa_Object = MibTableColumn
ansCeAtmCCTimeSlotPa = _AnsCeAtmCCTimeSlotPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 19),
    _AnsCeAtmCCTimeSlotPa_Type()
)
ansCeAtmCCTimeSlotPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCTimeSlotPa.setStatus("mandatory")
_AnsCeAtmCCTypePa_Type = AnsAal1ParsType
_AnsCeAtmCCTypePa_Object = MibTableColumn
ansCeAtmCCTypePa = _AnsCeAtmCCTypePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 20),
    _AnsCeAtmCCTypePa_Type()
)
ansCeAtmCCTypePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCTypePa.setStatus("mandatory")
_AnsCeAtmCCFillLevelPa_Type = Integer32
_AnsCeAtmCCFillLevelPa_Object = MibTableColumn
ansCeAtmCCFillLevelPa = _AnsCeAtmCCFillLevelPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 21),
    _AnsCeAtmCCFillLevelPa_Type()
)
ansCeAtmCCFillLevelPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCFillLevelPa.setStatus("mandatory")
_AnsCeAtmCCCdvtPa_Type = Integer32
_AnsCeAtmCCCdvtPa_Object = MibTableColumn
ansCeAtmCCCdvtPa = _AnsCeAtmCCCdvtPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 22),
    _AnsCeAtmCCCdvtPa_Type()
)
ansCeAtmCCCdvtPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCCdvtPa.setStatus("mandatory")
_AnsCeAtmCCMaxBuffSizePa_Type = Integer32
_AnsCeAtmCCMaxBuffSizePa_Object = MibTableColumn
ansCeAtmCCMaxBuffSizePa = _AnsCeAtmCCMaxBuffSizePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 23),
    _AnsCeAtmCCMaxBuffSizePa_Type()
)
ansCeAtmCCMaxBuffSizePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCMaxBuffSizePa.setStatus("mandatory")
_AnsCeAtmCCTcModePa_Type = AnsAal1ParsTcMode
_AnsCeAtmCCTcModePa_Object = MibTableColumn
ansCeAtmCCTcModePa = _AnsCeAtmCCTcModePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 24),
    _AnsCeAtmCCTcModePa_Type()
)
ansCeAtmCCTcModePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCTcModePa.setStatus("mandatory")
_AnsCeAtmCCTcTypePa_Type = AnsAal1ParsTcType
_AnsCeAtmCCTcTypePa_Object = MibTableColumn
ansCeAtmCCTcTypePa = _AnsCeAtmCCTcTypePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 25),
    _AnsCeAtmCCTcTypePa_Type()
)
ansCeAtmCCTcTypePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCTcTypePa.setStatus("mandatory")
_AnsCeAtmCCTcBtoAPa_Type = Integer32
_AnsCeAtmCCTcBtoAPa_Object = MibTableColumn
ansCeAtmCCTcBtoAPa = _AnsCeAtmCCTcBtoAPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 26),
    _AnsCeAtmCCTcBtoAPa_Type()
)
ansCeAtmCCTcBtoAPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCTcBtoAPa.setStatus("mandatory")
_AnsCeAtmCCTcAtoBPa_Type = Integer32
_AnsCeAtmCCTcAtoBPa_Object = MibTableColumn
ansCeAtmCCTcAtoBPa = _AnsCeAtmCCTcAtoBPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 27),
    _AnsCeAtmCCTcAtoBPa_Type()
)
ansCeAtmCCTcAtoBPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCTcAtoBPa.setStatus("mandatory")
_AnsCeAtmCCRowStatus_Type = RowStatus
_AnsCeAtmCCRowStatus_Object = MibTableColumn
ansCeAtmCCRowStatus = _AnsCeAtmCCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 6, 1, 1, 28),
    _AnsCeAtmCCRowStatus_Type()
)
ansCeAtmCCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeAtmCCRowStatus.setStatus("mandatory")
_AnsCeCeCreateCC_ObjectIdentity = ObjectIdentity
ansCeCeCreateCC = _AnsCeCeCreateCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7)
)
_AnsCeCeCreateCCTable_Object = MibTable
ansCeCeCreateCCTable = _AnsCeCeCreateCCTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ansCeCeCreateCCTable.setStatus("mandatory")
_AnsCeCeCreateCCEntry_Object = MibTableRow
ansCeCeCreateCCEntry = _AnsCeCeCreateCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1)
)
ansCeCeCreateCCEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansCeCeCCAUPSystemNode"),
    (0, "ANS-GS-MIB", "ansCeCeCCAUPSubrack"),
    (0, "ANS-GS-MIB", "ansCeCeCCAUPPosition"),
    (0, "ANS-GS-MIB", "ansCeCeCCAUPIndex"),
    (0, "ANS-GS-MIB", "ansCeCeCCAUPVPI"),
    (0, "ANS-GS-MIB", "ansCeCeCCAUPVCI"),
)
if mibBuilder.loadTexts:
    ansCeCeCreateCCEntry.setStatus("mandatory")
_AnsCeCeCCAUPSystemNode_Type = Integer32
_AnsCeCeCCAUPSystemNode_Object = MibTableColumn
ansCeCeCCAUPSystemNode = _AnsCeCeCCAUPSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 1),
    _AnsCeCeCCAUPSystemNode_Type()
)
ansCeCeCCAUPSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeCeCCAUPSystemNode.setStatus("mandatory")
_AnsCeCeCCAUPSubrack_Type = Integer32
_AnsCeCeCCAUPSubrack_Object = MibTableColumn
ansCeCeCCAUPSubrack = _AnsCeCeCCAUPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 2),
    _AnsCeCeCCAUPSubrack_Type()
)
ansCeCeCCAUPSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeCeCCAUPSubrack.setStatus("mandatory")
_AnsCeCeCCAUPPosition_Type = Integer32
_AnsCeCeCCAUPPosition_Object = MibTableColumn
ansCeCeCCAUPPosition = _AnsCeCeCCAUPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 3),
    _AnsCeCeCCAUPPosition_Type()
)
ansCeCeCCAUPPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeCeCCAUPPosition.setStatus("mandatory")
_AnsCeCeCCAUPIndex_Type = Integer32
_AnsCeCeCCAUPIndex_Object = MibTableColumn
ansCeCeCCAUPIndex = _AnsCeCeCCAUPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 4),
    _AnsCeCeCCAUPIndex_Type()
)
ansCeCeCCAUPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeCeCCAUPIndex.setStatus("mandatory")
_AnsCeCeCCAUPVPI_Type = Integer32
_AnsCeCeCCAUPVPI_Object = MibTableColumn
ansCeCeCCAUPVPI = _AnsCeCeCCAUPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 5),
    _AnsCeCeCCAUPVPI_Type()
)
ansCeCeCCAUPVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeCeCCAUPVPI.setStatus("mandatory")
_AnsCeCeCCAUPVCI_Type = Integer32
_AnsCeCeCCAUPVCI_Object = MibTableColumn
ansCeCeCCAUPVCI = _AnsCeCeCCAUPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 6),
    _AnsCeCeCCAUPVCI_Type()
)
ansCeCeCCAUPVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCeCeCCAUPVCI.setStatus("mandatory")
_AnsCeCeCCASPSubrack_Type = Integer32
_AnsCeCeCCASPSubrack_Object = MibTableColumn
ansCeCeCCASPSubrack = _AnsCeCeCCASPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 7),
    _AnsCeCeCCASPSubrack_Type()
)
ansCeCeCCASPSubrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCASPSubrack.setStatus("mandatory")
_AnsCeCeCCASPPosition_Type = Integer32
_AnsCeCeCCASPPosition_Object = MibTableColumn
ansCeCeCCASPPosition = _AnsCeCeCCASPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 8),
    _AnsCeCeCCASPPosition_Type()
)
ansCeCeCCASPPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCASPPosition.setStatus("mandatory")
_AnsCeCeCCASPIndex_Type = Integer32
_AnsCeCeCCASPIndex_Object = MibTableColumn
ansCeCeCCASPIndex = _AnsCeCeCCASPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 9),
    _AnsCeCeCCASPIndex_Type()
)
ansCeCeCCASPIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCASPIndex.setStatus("mandatory")
_AnsCeCeCCASPVPI_Type = Integer32
_AnsCeCeCCASPVPI_Object = MibTableColumn
ansCeCeCCASPVPI = _AnsCeCeCCASPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 10),
    _AnsCeCeCCASPVPI_Type()
)
ansCeCeCCASPVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCASPVPI.setStatus("mandatory")
_AnsCeCeCCASPVCI_Type = Integer32
_AnsCeCeCCASPVCI_Object = MibTableColumn
ansCeCeCCASPVCI = _AnsCeCeCCASPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 11),
    _AnsCeCeCCASPVCI_Type()
)
ansCeCeCCASPVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCASPVCI.setStatus("mandatory")
_AnsCeCeCCType_Type = AnsCCType
_AnsCeCeCCType_Object = MibTableColumn
ansCeCeCCType = _AnsCeCeCCType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 12),
    _AnsCeCeCCType_Type()
)
ansCeCeCCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCType.setStatus("mandatory")
_AnsCeCeCCServiceClass_Type = AnsCCServiceClass
_AnsCeCeCCServiceClass_Object = MibTableColumn
ansCeCeCCServiceClass = _AnsCeCeCCServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 13),
    _AnsCeCeCCServiceClass_Type()
)
ansCeCeCCServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCServiceClass.setStatus("mandatory")
_AnsCeCeCCSourceType_Type = AnsCCSourceType
_AnsCeCeCCSourceType_Object = MibTableColumn
ansCeCeCCSourceType = _AnsCeCeCCSourceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 14),
    _AnsCeCeCCSourceType_Type()
)
ansCeCeCCSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCSourceType.setStatus("mandatory")
_AnsCeCeCCPcrAtoB_Type = Integer32
_AnsCeCeCCPcrAtoB_Object = MibTableColumn
ansCeCeCCPcrAtoB = _AnsCeCeCCPcrAtoB_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 15),
    _AnsCeCeCCPcrAtoB_Type()
)
ansCeCeCCPcrAtoB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCPcrAtoB.setStatus("mandatory")
_AnsCeCeCCPcrBtoA_Type = Integer32
_AnsCeCeCCPcrBtoA_Object = MibTableColumn
ansCeCeCCPcrBtoA = _AnsCeCeCCPcrBtoA_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 16),
    _AnsCeCeCCPcrBtoA_Type()
)
ansCeCeCCPcrBtoA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCPcrBtoA.setStatus("mandatory")
_AnsCeCeCCMulti_Type = AnsCCMulti
_AnsCeCeCCMulti_Object = MibTableColumn
ansCeCeCCMulti = _AnsCeCeCCMulti_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 17),
    _AnsCeCeCCMulti_Type()
)
ansCeCeCCMulti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCMulti.setStatus("mandatory")
_AnsCeCeCCAdminStatus_Type = AnsCCAdminStatus
_AnsCeCeCCAdminStatus_Object = MibTableColumn
ansCeCeCCAdminStatus = _AnsCeCeCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 18),
    _AnsCeCeCCAdminStatus_Type()
)
ansCeCeCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCAdminStatus.setStatus("mandatory")
_AnsCeCeCCTimeSlotPa_Type = DisplayString
_AnsCeCeCCTimeSlotPa_Object = MibTableColumn
ansCeCeCCTimeSlotPa = _AnsCeCeCCTimeSlotPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 19),
    _AnsCeCeCCTimeSlotPa_Type()
)
ansCeCeCCTimeSlotPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTimeSlotPa.setStatus("mandatory")
_AnsCeCeCCTypePa_Type = AnsAal1ParsType
_AnsCeCeCCTypePa_Object = MibTableColumn
ansCeCeCCTypePa = _AnsCeCeCCTypePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 20),
    _AnsCeCeCCTypePa_Type()
)
ansCeCeCCTypePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTypePa.setStatus("mandatory")
_AnsCeCeCCFillLevelPa_Type = Integer32
_AnsCeCeCCFillLevelPa_Object = MibTableColumn
ansCeCeCCFillLevelPa = _AnsCeCeCCFillLevelPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 21),
    _AnsCeCeCCFillLevelPa_Type()
)
ansCeCeCCFillLevelPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCFillLevelPa.setStatus("mandatory")
_AnsCeCeCCCdvtPa_Type = Integer32
_AnsCeCeCCCdvtPa_Object = MibTableColumn
ansCeCeCCCdvtPa = _AnsCeCeCCCdvtPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 22),
    _AnsCeCeCCCdvtPa_Type()
)
ansCeCeCCCdvtPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCCdvtPa.setStatus("mandatory")
_AnsCeCeCCMaxBuffSizePa_Type = Integer32
_AnsCeCeCCMaxBuffSizePa_Object = MibTableColumn
ansCeCeCCMaxBuffSizePa = _AnsCeCeCCMaxBuffSizePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 23),
    _AnsCeCeCCMaxBuffSizePa_Type()
)
ansCeCeCCMaxBuffSizePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCMaxBuffSizePa.setStatus("mandatory")
_AnsCeCeCCTcModePa_Type = AnsAal1ParsTcMode
_AnsCeCeCCTcModePa_Object = MibTableColumn
ansCeCeCCTcModePa = _AnsCeCeCCTcModePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 24),
    _AnsCeCeCCTcModePa_Type()
)
ansCeCeCCTcModePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcModePa.setStatus("mandatory")
_AnsCeCeCCTcTypePa_Type = AnsAal1ParsTcType
_AnsCeCeCCTcTypePa_Object = MibTableColumn
ansCeCeCCTcTypePa = _AnsCeCeCCTcTypePa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 25),
    _AnsCeCeCCTcTypePa_Type()
)
ansCeCeCCTcTypePa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcTypePa.setStatus("mandatory")
_AnsCeCeCCTcBtoAPa_Type = Integer32
_AnsCeCeCCTcBtoAPa_Object = MibTableColumn
ansCeCeCCTcBtoAPa = _AnsCeCeCCTcBtoAPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 26),
    _AnsCeCeCCTcBtoAPa_Type()
)
ansCeCeCCTcBtoAPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcBtoAPa.setStatus("mandatory")
_AnsCeCeCCTcAtoBPa_Type = Integer32
_AnsCeCeCCTcAtoBPa_Object = MibTableColumn
ansCeCeCCTcAtoBPa = _AnsCeCeCCTcAtoBPa_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 27),
    _AnsCeCeCCTcAtoBPa_Type()
)
ansCeCeCCTcAtoBPa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcAtoBPa.setStatus("mandatory")
_AnsCeCeCCTimeSlotPb_Type = DisplayString
_AnsCeCeCCTimeSlotPb_Object = MibTableColumn
ansCeCeCCTimeSlotPb = _AnsCeCeCCTimeSlotPb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 28),
    _AnsCeCeCCTimeSlotPb_Type()
)
ansCeCeCCTimeSlotPb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTimeSlotPb.setStatus("mandatory")
_AnsCeCeCCTypePb_Type = AnsAal1ParsType
_AnsCeCeCCTypePb_Object = MibTableColumn
ansCeCeCCTypePb = _AnsCeCeCCTypePb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 29),
    _AnsCeCeCCTypePb_Type()
)
ansCeCeCCTypePb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTypePb.setStatus("mandatory")
_AnsCeCeCCFillLevelPb_Type = Integer32
_AnsCeCeCCFillLevelPb_Object = MibTableColumn
ansCeCeCCFillLevelPb = _AnsCeCeCCFillLevelPb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 30),
    _AnsCeCeCCFillLevelPb_Type()
)
ansCeCeCCFillLevelPb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCFillLevelPb.setStatus("mandatory")
_AnsCeCeCCCdvtPb_Type = Integer32
_AnsCeCeCCCdvtPb_Object = MibTableColumn
ansCeCeCCCdvtPb = _AnsCeCeCCCdvtPb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 31),
    _AnsCeCeCCCdvtPb_Type()
)
ansCeCeCCCdvtPb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCCdvtPb.setStatus("mandatory")
_AnsCeCeCCMaxBuffSizePb_Type = Integer32
_AnsCeCeCCMaxBuffSizePb_Object = MibTableColumn
ansCeCeCCMaxBuffSizePb = _AnsCeCeCCMaxBuffSizePb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 32),
    _AnsCeCeCCMaxBuffSizePb_Type()
)
ansCeCeCCMaxBuffSizePb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCMaxBuffSizePb.setStatus("mandatory")
_AnsCeCeCCTcModePb_Type = AnsAal1ParsTcMode
_AnsCeCeCCTcModePb_Object = MibTableColumn
ansCeCeCCTcModePb = _AnsCeCeCCTcModePb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 33),
    _AnsCeCeCCTcModePb_Type()
)
ansCeCeCCTcModePb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcModePb.setStatus("mandatory")
_AnsCeCeCCTcTypePb_Type = AnsAal1ParsTcType
_AnsCeCeCCTcTypePb_Object = MibTableColumn
ansCeCeCCTcTypePb = _AnsCeCeCCTcTypePb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 34),
    _AnsCeCeCCTcTypePb_Type()
)
ansCeCeCCTcTypePb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcTypePb.setStatus("mandatory")
_AnsCeCeCCTcBtoAPb_Type = Integer32
_AnsCeCeCCTcBtoAPb_Object = MibTableColumn
ansCeCeCCTcBtoAPb = _AnsCeCeCCTcBtoAPb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 35),
    _AnsCeCeCCTcBtoAPb_Type()
)
ansCeCeCCTcBtoAPb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcBtoAPb.setStatus("mandatory")
_AnsCeCeCCTcAtoBPb_Type = Integer32
_AnsCeCeCCTcAtoBPb_Object = MibTableColumn
ansCeCeCCTcAtoBPb = _AnsCeCeCCTcAtoBPb_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 36),
    _AnsCeCeCCTcAtoBPb_Type()
)
ansCeCeCCTcAtoBPb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCTcAtoBPb.setStatus("mandatory")
_AnsCeCeCCRowStatus_Type = RowStatus
_AnsCeCeCCRowStatus_Object = MibTableColumn
ansCeCeCCRowStatus = _AnsCeCeCCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 7, 1, 1, 37),
    _AnsCeCeCCRowStatus_Type()
)
ansCeCeCCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCeCeCCRowStatus.setStatus("mandatory")
_AnsCrossConnect_ObjectIdentity = ObjectIdentity
ansCrossConnect = _AnsCrossConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8)
)
_AnsCrossConnectTable_Object = MibTable
ansCrossConnectTable = _AnsCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1)
)
if mibBuilder.loadTexts:
    ansCrossConnectTable.setStatus("mandatory")
_AnsCrossConnectEntry_Object = MibTableRow
ansCrossConnectEntry = _AnsCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1)
)
ansCrossConnectEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansCCAUPSystemNode"),
    (0, "ANS-GS-MIB", "ansCCAUPSubrack"),
    (0, "ANS-GS-MIB", "ansCCAUPPosition"),
    (0, "ANS-GS-MIB", "ansCCAUPIndex"),
    (0, "ANS-GS-MIB", "ansCCAUPVPI"),
    (0, "ANS-GS-MIB", "ansCCAUPVCI"),
)
if mibBuilder.loadTexts:
    ansCrossConnectEntry.setStatus("mandatory")
_AnsCCAUPSystemNode_Type = Integer32
_AnsCCAUPSystemNode_Object = MibTableColumn
ansCCAUPSystemNode = _AnsCCAUPSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 1),
    _AnsCCAUPSystemNode_Type()
)
ansCCAUPSystemNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansCCAUPSystemNode.setStatus("mandatory")
_AnsCCAUPSubrack_Type = Integer32
_AnsCCAUPSubrack_Object = MibTableColumn
ansCCAUPSubrack = _AnsCCAUPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 2),
    _AnsCCAUPSubrack_Type()
)
ansCCAUPSubrack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansCCAUPSubrack.setStatus("mandatory")
_AnsCCAUPPosition_Type = Integer32
_AnsCCAUPPosition_Object = MibTableColumn
ansCCAUPPosition = _AnsCCAUPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 3),
    _AnsCCAUPPosition_Type()
)
ansCCAUPPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansCCAUPPosition.setStatus("mandatory")
_AnsCCAUPIndex_Type = Integer32
_AnsCCAUPIndex_Object = MibTableColumn
ansCCAUPIndex = _AnsCCAUPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 4),
    _AnsCCAUPIndex_Type()
)
ansCCAUPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansCCAUPIndex.setStatus("mandatory")
_AnsCCAUPVPI_Type = Integer32
_AnsCCAUPVPI_Object = MibTableColumn
ansCCAUPVPI = _AnsCCAUPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 5),
    _AnsCCAUPVPI_Type()
)
ansCCAUPVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansCCAUPVPI.setStatus("mandatory")
_AnsCCAUPVCI_Type = Integer32
_AnsCCAUPVCI_Object = MibTableColumn
ansCCAUPVCI = _AnsCCAUPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 6),
    _AnsCCAUPVCI_Type()
)
ansCCAUPVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansCCAUPVCI.setStatus("mandatory")
_AnsCCASPSubrack_Type = Integer32
_AnsCCASPSubrack_Object = MibTableColumn
ansCCASPSubrack = _AnsCCASPSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 7),
    _AnsCCASPSubrack_Type()
)
ansCCASPSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCASPSubrack.setStatus("mandatory")
_AnsCCASPPosition_Type = Integer32
_AnsCCASPPosition_Object = MibTableColumn
ansCCASPPosition = _AnsCCASPPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 8),
    _AnsCCASPPosition_Type()
)
ansCCASPPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCASPPosition.setStatus("mandatory")
_AnsCCASPIndex_Type = Integer32
_AnsCCASPIndex_Object = MibTableColumn
ansCCASPIndex = _AnsCCASPIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 9),
    _AnsCCASPIndex_Type()
)
ansCCASPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCASPIndex.setStatus("mandatory")
_AnsCCASPVPI_Type = Integer32
_AnsCCASPVPI_Object = MibTableColumn
ansCCASPVPI = _AnsCCASPVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 10),
    _AnsCCASPVPI_Type()
)
ansCCASPVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCASPVPI.setStatus("mandatory")
_AnsCCASPVCI_Type = Integer32
_AnsCCASPVCI_Object = MibTableColumn
ansCCASPVCI = _AnsCCASPVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 11),
    _AnsCCASPVCI_Type()
)
ansCCASPVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCASPVCI.setStatus("mandatory")
_AnsCCType_Type = AnsCCType
_AnsCCType_Object = MibTableColumn
ansCCType = _AnsCCType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 12),
    _AnsCCType_Type()
)
ansCCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCType.setStatus("mandatory")
_AnsCCServiceClass_Type = AnsCCServiceClass
_AnsCCServiceClass_Object = MibTableColumn
ansCCServiceClass = _AnsCCServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 13),
    _AnsCCServiceClass_Type()
)
ansCCServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCServiceClass.setStatus("mandatory")
_AnsCCPcrAtoB_Type = Integer32
_AnsCCPcrAtoB_Object = MibTableColumn
ansCCPcrAtoB = _AnsCCPcrAtoB_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 14),
    _AnsCCPcrAtoB_Type()
)
ansCCPcrAtoB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCPcrAtoB.setStatus("mandatory")
_AnsCCPcrBtoA_Type = Integer32
_AnsCCPcrBtoA_Object = MibTableColumn
ansCCPcrBtoA = _AnsCCPcrBtoA_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 15),
    _AnsCCPcrBtoA_Type()
)
ansCCPcrBtoA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCPcrBtoA.setStatus("mandatory")
_AnsCCSourceType_Type = AnsCCSourceType
_AnsCCSourceType_Object = MibTableColumn
ansCCSourceType = _AnsCCSourceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 16),
    _AnsCCSourceType_Type()
)
ansCCSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCSourceType.setStatus("mandatory")


class _AnsCCServiceType_Type(Integer32):
    """Custom type ansCCServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("ce", 1),
          ("ethernet", 3))
    )


_AnsCCServiceType_Type.__name__ = "Integer32"
_AnsCCServiceType_Object = MibTableColumn
ansCCServiceType = _AnsCCServiceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 17),
    _AnsCCServiceType_Type()
)
ansCCServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCServiceType.setStatus("mandatory")


class _AnsCCOperStatus_Type(Integer32):
    """Custom type ansCCOperStatus based on Integer32"""
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


_AnsCCOperStatus_Type.__name__ = "Integer32"
_AnsCCOperStatus_Object = MibTableColumn
ansCCOperStatus = _AnsCCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 18),
    _AnsCCOperStatus_Type()
)
ansCCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCOperStatus.setStatus("mandatory")
_AnsCCLastOperStatusChange_Type = DateAndTime
_AnsCCLastOperStatusChange_Object = MibTableColumn
ansCCLastOperStatusChange = _AnsCCLastOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 19),
    _AnsCCLastOperStatusChange_Type()
)
ansCCLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCLastOperStatusChange.setStatus("mandatory")
_AnsCCAdminStatus_Type = AnsCCAdminStatus
_AnsCCAdminStatus_Object = MibTableColumn
ansCCAdminStatus = _AnsCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 20),
    _AnsCCAdminStatus_Type()
)
ansCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCCAdminStatus.setStatus("mandatory")
_AnsCCMulti_Type = AnsCCMulti
_AnsCCMulti_Object = MibTableColumn
ansCCMulti = _AnsCCMulti_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 21),
    _AnsCCMulti_Type()
)
ansCCMulti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansCCMulti.setStatus("mandatory")
_AnsCCRowStatus_Type = RowStatus
_AnsCCRowStatus_Object = MibTableColumn
ansCCRowStatus = _AnsCCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 8, 1, 1, 22),
    _AnsCCRowStatus_Type()
)
ansCCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansCCRowStatus.setStatus("mandatory")
_AnsApplData_ObjectIdentity = ObjectIdentity
ansApplData = _AnsApplData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9)
)
_AnsApplDataTable_Object = MibTable
ansApplDataTable = _AnsApplDataTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ansApplDataTable.setStatus("mandatory")
_AnsApplDataEntry_Object = MibTableRow
ansApplDataEntry = _AnsApplDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1)
)
ansApplDataEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansApplDataSystemNode"),
    (0, "ANS-GS-MIB", "ansApplDataSubrack"),
    (0, "ANS-GS-MIB", "ansApplDataPosition"),
    (0, "ANS-GS-MIB", "ansApplDataIndex"),
    (0, "ANS-GS-MIB", "ansApplDataVPI"),
    (0, "ANS-GS-MIB", "ansApplDataVCI"),
)
if mibBuilder.loadTexts:
    ansApplDataEntry.setStatus("mandatory")
_AnsApplDataSystemNode_Type = Integer32
_AnsApplDataSystemNode_Object = MibTableColumn
ansApplDataSystemNode = _AnsApplDataSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 1),
    _AnsApplDataSystemNode_Type()
)
ansApplDataSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataSystemNode.setStatus("mandatory")
_AnsApplDataSubrack_Type = Integer32
_AnsApplDataSubrack_Object = MibTableColumn
ansApplDataSubrack = _AnsApplDataSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 2),
    _AnsApplDataSubrack_Type()
)
ansApplDataSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataSubrack.setStatus("mandatory")
_AnsApplDataPosition_Type = Integer32
_AnsApplDataPosition_Object = MibTableColumn
ansApplDataPosition = _AnsApplDataPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 3),
    _AnsApplDataPosition_Type()
)
ansApplDataPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataPosition.setStatus("mandatory")
_AnsApplDataIndex_Type = Integer32
_AnsApplDataIndex_Object = MibTableColumn
ansApplDataIndex = _AnsApplDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 4),
    _AnsApplDataIndex_Type()
)
ansApplDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataIndex.setStatus("mandatory")
_AnsApplDataVPI_Type = Integer32
_AnsApplDataVPI_Object = MibTableColumn
ansApplDataVPI = _AnsApplDataVPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 5),
    _AnsApplDataVPI_Type()
)
ansApplDataVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataVPI.setStatus("mandatory")
_AnsApplDataVCI_Type = Integer32
_AnsApplDataVCI_Object = MibTableColumn
ansApplDataVCI = _AnsApplDataVCI_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 6),
    _AnsApplDataVCI_Type()
)
ansApplDataVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataVCI.setStatus("mandatory")


class _AnsApplDataOpState_Type(Integer32):
    """Custom type ansApplDataOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AnsApplDataOpState_Type.__name__ = "Integer32"
_AnsApplDataOpState_Object = MibTableColumn
ansApplDataOpState = _AnsApplDataOpState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 7),
    _AnsApplDataOpState_Type()
)
ansApplDataOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataOpState.setStatus("mandatory")


class _AnsApplDataAdminState_Type(Integer32):
    """Custom type ansApplDataAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AnsApplDataAdminState_Type.__name__ = "Integer32"
_AnsApplDataAdminState_Object = MibTableColumn
ansApplDataAdminState = _AnsApplDataAdminState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 8),
    _AnsApplDataAdminState_Type()
)
ansApplDataAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansApplDataAdminState.setStatus("mandatory")


class _AnsApplDataServiceParams_Type(Integer32):
    """Custom type ansApplDataServiceParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("ethernet", 2),
          ("undefined", -1))
    )


_AnsApplDataServiceParams_Type.__name__ = "Integer32"
_AnsApplDataServiceParams_Object = MibTableColumn
ansApplDataServiceParams = _AnsApplDataServiceParams_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 9, 1, 1, 9),
    _AnsApplDataServiceParams_Type()
)
ansApplDataServiceParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansApplDataServiceParams.setStatus("mandatory")
_AnsAal1Pars_ObjectIdentity = ObjectIdentity
ansAal1Pars = _AnsAal1Pars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10)
)
_AnsAal1ParsTable_Object = MibTable
ansAal1ParsTable = _AnsAal1ParsTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1)
)
if mibBuilder.loadTexts:
    ansAal1ParsTable.setStatus("mandatory")
_AnsAal1ParsEntry_Object = MibTableRow
ansAal1ParsEntry = _AnsAal1ParsEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1)
)
ansAal1ParsEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansApplDataSystemNode"),
    (0, "ANS-GS-MIB", "ansApplDataSubrack"),
    (0, "ANS-GS-MIB", "ansApplDataPosition"),
    (0, "ANS-GS-MIB", "ansApplDataIndex"),
    (0, "ANS-GS-MIB", "ansApplDataVPI"),
    (0, "ANS-GS-MIB", "ansApplDataVCI"),
)
if mibBuilder.loadTexts:
    ansAal1ParsEntry.setStatus("mandatory")
_AnsAal1ParsTimeSlot_Type = DisplayString
_AnsAal1ParsTimeSlot_Object = MibTableColumn
ansAal1ParsTimeSlot = _AnsAal1ParsTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 1),
    _AnsAal1ParsTimeSlot_Type()
)
ansAal1ParsTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsTimeSlot.setStatus("mandatory")


class _AnsAal1ParsType_Type(Integer32):
    """Custom type ansAal1ParsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("structured-contiguous", 2),
          ("structured-free", 3),
          ("undefined", -1),
          ("unstructured", 1))
    )


_AnsAal1ParsType_Type.__name__ = "Integer32"
_AnsAal1ParsType_Object = MibTableColumn
ansAal1ParsType = _AnsAal1ParsType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 2),
    _AnsAal1ParsType_Type()
)
ansAal1ParsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsType.setStatus("mandatory")
_AnsAal1ParsFillLevel_Type = Integer32
_AnsAal1ParsFillLevel_Object = MibTableColumn
ansAal1ParsFillLevel = _AnsAal1ParsFillLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 3),
    _AnsAal1ParsFillLevel_Type()
)
ansAal1ParsFillLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsFillLevel.setStatus("mandatory")
_AnsAal1ParsCdvt_Type = Integer32
_AnsAal1ParsCdvt_Object = MibTableColumn
ansAal1ParsCdvt = _AnsAal1ParsCdvt_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 4),
    _AnsAal1ParsCdvt_Type()
)
ansAal1ParsCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAal1ParsCdvt.setStatus("mandatory")
_AnsAal1ParsMaxBuffSize_Type = Integer32
_AnsAal1ParsMaxBuffSize_Object = MibTableColumn
ansAal1ParsMaxBuffSize = _AnsAal1ParsMaxBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 5),
    _AnsAal1ParsMaxBuffSize_Type()
)
ansAal1ParsMaxBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansAal1ParsMaxBuffSize.setStatus("mandatory")


class _AnsAal1ParsTcMode_Type(Integer32):
    """Custom type ansAal1ParsTcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleyed", 2),
          ("immediate", 1),
          ("undefined", -1))
    )


_AnsAal1ParsTcMode_Type.__name__ = "Integer32"
_AnsAal1ParsTcMode_Object = MibTableColumn
ansAal1ParsTcMode = _AnsAal1ParsTcMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 6),
    _AnsAal1ParsTcMode_Type()
)
ansAal1ParsTcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsTcMode.setStatus("mandatory")


class _AnsAal1ParsTcType_Type(Integer32):
    """Custom type ansAal1ParsTcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0ais", 2),
          ("service-specific", 1),
          ("undefined", -1))
    )


_AnsAal1ParsTcType_Type.__name__ = "Integer32"
_AnsAal1ParsTcType_Object = MibTableColumn
ansAal1ParsTcType = _AnsAal1ParsTcType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 7),
    _AnsAal1ParsTcType_Type()
)
ansAal1ParsTcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsTcType.setStatus("mandatory")
_AnsAal1ParsTcBtoA_Type = Integer32
_AnsAal1ParsTcBtoA_Object = MibTableColumn
ansAal1ParsTcBtoA = _AnsAal1ParsTcBtoA_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 8),
    _AnsAal1ParsTcBtoA_Type()
)
ansAal1ParsTcBtoA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsTcBtoA.setStatus("mandatory")
_AnsAal1ParsTcAtoB_Type = Integer32
_AnsAal1ParsTcAtoB_Object = MibTableColumn
ansAal1ParsTcAtoB = _AnsAal1ParsTcAtoB_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 10, 1, 1, 9),
    _AnsAal1ParsTcAtoB_Type()
)
ansAal1ParsTcAtoB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansAal1ParsTcAtoB.setStatus("mandatory")
_AnsEthPars_ObjectIdentity = ObjectIdentity
ansEthPars = _AnsEthPars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 11)
)
_AnsEthParsTable_Object = MibTable
ansEthParsTable = _AnsEthParsTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 11, 1)
)
if mibBuilder.loadTexts:
    ansEthParsTable.setStatus("mandatory")
_AnsEthParsEntry_Object = MibTableRow
ansEthParsEntry = _AnsEthParsEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 11, 1, 1)
)
ansEthParsEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansApplDataSystemNode"),
    (0, "ANS-GS-MIB", "ansApplDataSubrack"),
    (0, "ANS-GS-MIB", "ansApplDataPosition"),
    (0, "ANS-GS-MIB", "ansApplDataIndex"),
    (0, "ANS-GS-MIB", "ansApplDataVPI"),
    (0, "ANS-GS-MIB", "ansApplDataVCI"),
)
if mibBuilder.loadTexts:
    ansEthParsEntry.setStatus("mandatory")
_AnsEthParsPcrShaping_Type = Integer32
_AnsEthParsPcrShaping_Object = MibTableColumn
ansEthParsPcrShaping = _AnsEthParsPcrShaping_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 11, 1, 1, 1),
    _AnsEthParsPcrShaping_Type()
)
ansEthParsPcrShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansEthParsPcrShaping.setStatus("mandatory")
_EthernetPort_ObjectIdentity = ObjectIdentity
ethernetPort = _EthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12)
)
_EthernetPortTable_Object = MibTable
ethernetPortTable = _EthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1)
)
if mibBuilder.loadTexts:
    ethernetPortTable.setStatus("mandatory")
_EthernetPortEntry_Object = MibTableRow
ethernetPortEntry = _EthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1, 1)
)
ethernetPortEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAccessUserPortSystemNode"),
    (0, "ANS-GS-MIB", "ansAccessUserPortSubrack"),
    (0, "ANS-GS-MIB", "ansAccessUserPortPosition"),
    (0, "ANS-GS-MIB", "ansAccessUserPortIndex"),
)
if mibBuilder.loadTexts:
    ethernetPortEntry.setStatus("mandatory")


class _EthernetPortFcsEncapsulation_Type(Integer32):
    """Custom type ethernetPortFcsEncapsulation based on Integer32"""
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


_EthernetPortFcsEncapsulation_Type.__name__ = "Integer32"
_EthernetPortFcsEncapsulation_Object = MibTableColumn
ethernetPortFcsEncapsulation = _EthernetPortFcsEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1, 1, 1),
    _EthernetPortFcsEncapsulation_Type()
)
ethernetPortFcsEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPortFcsEncapsulation.setStatus("mandatory")


class _EthernetPortMuxOrEncapsulation_Type(Integer32):
    """Custom type ethernetPortMuxOrEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llcEncapsulation", 2),
          ("vcBasedMultiplexing", 1))
    )


_EthernetPortMuxOrEncapsulation_Type.__name__ = "Integer32"
_EthernetPortMuxOrEncapsulation_Object = MibTableColumn
ethernetPortMuxOrEncapsulation = _EthernetPortMuxOrEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1, 1, 2),
    _EthernetPortMuxOrEncapsulation_Type()
)
ethernetPortMuxOrEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPortMuxOrEncapsulation.setStatus("mandatory")
_EthernetPortIpAddress_Type = IpAddress
_EthernetPortIpAddress_Object = MibTableColumn
ethernetPortIpAddress = _EthernetPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1, 1, 3),
    _EthernetPortIpAddress_Type()
)
ethernetPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPortIpAddress.setStatus("mandatory")


class _EthernetPortType_Type(Integer32):
    """Custom type ethernetPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("base10", 1),
          ("base100", 2))
    )


_EthernetPortType_Type.__name__ = "Integer32"
_EthernetPortType_Object = MibTableColumn
ethernetPortType = _EthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1, 1, 4),
    _EthernetPortType_Type()
)
ethernetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPortType.setStatus("mandatory")


class _EthernetPortOperatingMode_Type(Integer32):
    """Custom type ethernetPortOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("base10", 1),
          ("base100", 2))
    )


_EthernetPortOperatingMode_Type.__name__ = "Integer32"
_EthernetPortOperatingMode_Object = MibTableColumn
ethernetPortOperatingMode = _EthernetPortOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 12, 1, 1, 5),
    _EthernetPortOperatingMode_Type()
)
ethernetPortOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPortOperatingMode.setStatus("mandatory")
_PdhPort_ObjectIdentity = ObjectIdentity
pdhPort = _PdhPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13)
)
_PdhPortTable_Object = MibTable
pdhPortTable = _PdhPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1)
)
if mibBuilder.loadTexts:
    pdhPortTable.setStatus("mandatory")
_PdhPortEntry_Object = MibTableRow
pdhPortEntry = _PdhPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1)
)
pdhPortEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
    (0, "ANS-GS-MIB", "pdhPortPort"),
)
if mibBuilder.loadTexts:
    pdhPortEntry.setStatus("mandatory")
_PdhPortPort_Type = Integer32
_PdhPortPort_Object = MibTableColumn
pdhPortPort = _PdhPortPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 1),
    _PdhPortPort_Type()
)
pdhPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhPortPort.setStatus("mandatory")
_PdhPortTsUsed_Type = DisplayString
_PdhPortTsUsed_Object = MibTableColumn
pdhPortTsUsed = _PdhPortTsUsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 2),
    _PdhPortTsUsed_Type()
)
pdhPortTsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhPortTsUsed.setStatus("mandatory")


class _PdhPortClockMode_Type(Integer32):
    """Custom type pdhPortClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 2),
          ("looped-asynchronous", 3),
          ("synchronous", 1))
    )


_PdhPortClockMode_Type.__name__ = "Integer32"
_PdhPortClockMode_Object = MibTableColumn
pdhPortClockMode = _PdhPortClockMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 3),
    _PdhPortClockMode_Type()
)
pdhPortClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortClockMode.setStatus("mandatory")


class _PdhPortHaulMode_Type(Integer32):
    """Custom type pdhPortHaulMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_PdhPortHaulMode_Type.__name__ = "Integer32"
_PdhPortHaulMode_Object = MibTableColumn
pdhPortHaulMode = _PdhPortHaulMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 4),
    _PdhPortHaulMode_Type()
)
pdhPortHaulMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortHaulMode.setStatus("mandatory")


class _PdhPortLineCode_Type(Integer32):
    """Custom type pdhPortLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 3),
          ("hdb3", 1))
    )


_PdhPortLineCode_Type.__name__ = "Integer32"
_PdhPortLineCode_Object = MibTableColumn
pdhPortLineCode = _PdhPortLineCode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 5),
    _PdhPortLineCode_Type()
)
pdhPortLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortLineCode.setStatus("mandatory")


class _PdhPortLoopback_Type(Integer32):
    """Custom type pdhPortLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("off", -1))
    )


_PdhPortLoopback_Type.__name__ = "Integer32"
_PdhPortLoopback_Object = MibTableColumn
pdhPortLoopback = _PdhPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 6),
    _PdhPortLoopback_Type()
)
pdhPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortLoopback.setStatus("mandatory")


class _PdhPortCas_Type(Integer32):
    """Custom type pdhPortCas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 2),
          ("cas", 1),
          ("not-used", -1))
    )


_PdhPortCas_Type.__name__ = "Integer32"
_PdhPortCas_Object = MibTableColumn
pdhPortCas = _PdhPortCas_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 7),
    _PdhPortCas_Type()
)
pdhPortCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortCas.setStatus("mandatory")


class _PdhPortFrameFormat_Type(Integer32):
    """Custom type pdhPortFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1-crc", 3),
          ("esf", 2),
          ("not-used", -1),
          ("sf", 1))
    )


_PdhPortFrameFormat_Type.__name__ = "Integer32"
_PdhPortFrameFormat_Object = MibTableColumn
pdhPortFrameFormat = _PdhPortFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 8),
    _PdhPortFrameFormat_Type()
)
pdhPortFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortFrameFormat.setStatus("mandatory")


class _PdhPortServiceType_Type(Integer32):
    """Custom type pdhPortServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 1),
          ("unstructured", 2))
    )


_PdhPortServiceType_Type.__name__ = "Integer32"
_PdhPortServiceType_Object = MibTableColumn
pdhPortServiceType = _PdhPortServiceType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 13, 1, 1, 9),
    _PdhPortServiceType_Type()
)
pdhPortServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhPortServiceType.setStatus("mandatory")
_TerminalId_ObjectIdentity = ObjectIdentity
terminalId = _TerminalId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14)
)
_AnsTerminalIdTable_Object = MibTable
ansTerminalIdTable = _AnsTerminalIdTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14, 1)
)
if mibBuilder.loadTexts:
    ansTerminalIdTable.setStatus("mandatory")
_AnsTerminalIdEntry_Object = MibTableRow
ansTerminalIdEntry = _AnsTerminalIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14, 1, 1)
)
ansTerminalIdEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansTerminalIdIdent"),
)
if mibBuilder.loadTexts:
    ansTerminalIdEntry.setStatus("mandatory")


class _AnsTerminalIdIdent_Type(DisplayString):
    """Custom type ansTerminalIdIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AnsTerminalIdIdent_Type.__name__ = "DisplayString"
_AnsTerminalIdIdent_Object = MibTableColumn
ansTerminalIdIdent = _AnsTerminalIdIdent_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14, 1, 1, 1),
    _AnsTerminalIdIdent_Type()
)
ansTerminalIdIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTerminalIdIdent.setStatus("mandatory")
_AnsTerminalIdSystemNode_Type = Integer32
_AnsTerminalIdSystemNode_Object = MibTableColumn
ansTerminalIdSystemNode = _AnsTerminalIdSystemNode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14, 1, 1, 2),
    _AnsTerminalIdSystemNode_Type()
)
ansTerminalIdSystemNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTerminalIdSystemNode.setStatus("mandatory")
_AnsTerminalIdSubrack_Type = Integer32
_AnsTerminalIdSubrack_Object = MibTableColumn
ansTerminalIdSubrack = _AnsTerminalIdSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14, 1, 1, 3),
    _AnsTerminalIdSubrack_Type()
)
ansTerminalIdSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTerminalIdSubrack.setStatus("mandatory")
_AnsTerminalIdPosition_Type = Integer32
_AnsTerminalIdPosition_Object = MibTableColumn
ansTerminalIdPosition = _AnsTerminalIdPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 4, 14, 1, 1, 4),
    _AnsTerminalIdPosition_Type()
)
ansTerminalIdPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTerminalIdPosition.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-GS-MIB",
    **{"AnsPortType": AnsPortType,
       "AnsCCType": AnsCCType,
       "AnsCCServiceClass": AnsCCServiceClass,
       "AnsCCSourceType": AnsCCSourceType,
       "AnsCCMulti": AnsCCMulti,
       "AnsCCAdminStatus": AnsCCAdminStatus,
       "AnsAal1ParsType": AnsAal1ParsType,
       "AnsAal1ParsTcMode": AnsAal1ParsTcMode,
       "AnsAal1ParsTcType": AnsAal1ParsTcType,
       "connections": connections,
       "accessUserPort": accessUserPort,
       "ansAccessUserPortTable": ansAccessUserPortTable,
       "ansAccessUserPortEntry": ansAccessUserPortEntry,
       "ansAccessUserPortSystemNode": ansAccessUserPortSystemNode,
       "ansAccessUserPortSubrack": ansAccessUserPortSubrack,
       "ansAccessUserPortPosition": ansAccessUserPortPosition,
       "ansAccessUserPortIndex": ansAccessUserPortIndex,
       "ansAccessUserPortType": ansAccessUserPortType,
       "ansAccessUserPortMaxBwDs": ansAccessUserPortMaxBwDs,
       "ansAccessUserPortMaxBwUs": ansAccessUserPortMaxBwUs,
       "ansAccessUserPortAvailBwDs": ansAccessUserPortAvailBwDs,
       "ansAccessUserPortAvailBwUs": ansAccessUserPortAvailBwUs,
       "ansAccessUserPortMinVpi": ansAccessUserPortMinVpi,
       "ansAccessUserPortMaxVpi": ansAccessUserPortMaxVpi,
       "ansAccessUserPortMinVci": ansAccessUserPortMinVci,
       "ansAccessUserPortMaxVci": ansAccessUserPortMaxVci,
       "ansAccessUserPortLabel": ansAccessUserPortLabel,
       "ansAccessUserPortOperStatus": ansAccessUserPortOperStatus,
       "ansAccessUserPortAdminStatus": ansAccessUserPortAdminStatus,
       "ansAccessUserPortUsageState": ansAccessUserPortUsageState,
       "ansAccessUserPortAtmFormat": ansAccessUserPortAtmFormat,
       "accessServicePort": accessServicePort,
       "ansAccessServicePortTable": ansAccessServicePortTable,
       "ansAccessServicePortEntry": ansAccessServicePortEntry,
       "ansAccessServicePortSystemNode": ansAccessServicePortSystemNode,
       "ansAccessServicePortSubrack": ansAccessServicePortSubrack,
       "ansAccessServicePortPosition": ansAccessServicePortPosition,
       "ansAccessServicePortIndex": ansAccessServicePortIndex,
       "ansAccessServicePortLabel": ansAccessServicePortLabel,
       "ansAccessServicePortMaxBwDs": ansAccessServicePortMaxBwDs,
       "ansAccessServicePortMaxBwUs": ansAccessServicePortMaxBwUs,
       "ansAccessServicePortAvailBwDs": ansAccessServicePortAvailBwDs,
       "ansAccessServicePortAvailBwUs": ansAccessServicePortAvailBwUs,
       "ansAccessServicePortMinVpi": ansAccessServicePortMinVpi,
       "ansAccessServicePortMaxVpi": ansAccessServicePortMaxVpi,
       "ansAccessServicePortMinVci": ansAccessServicePortMinVci,
       "ansAccessServicePortMaxVci": ansAccessServicePortMaxVci,
       "ansAccessServicePortOperStatus": ansAccessServicePortOperStatus,
       "ansAccessServicePortAdminStatus": ansAccessServicePortAdminStatus,
       "ansAccessServicePortUsageState": ansAccessServicePortUsageState,
       "ansAccessServicePortAtmFormat": ansAccessServicePortAtmFormat,
       "ansAccessServicePortType": ansAccessServicePortType,
       "accessServiceUserPort": accessServiceUserPort,
       "ansAccessServiceUserPortTable": ansAccessServiceUserPortTable,
       "ansAccessServiceUserPortEntry": ansAccessServiceUserPortEntry,
       "ansAccessServiceUserPortSystemNode": ansAccessServiceUserPortSystemNode,
       "ansAccessServiceUserPortSubrack": ansAccessServiceUserPortSubrack,
       "ansAccessServiceUserPortPosition": ansAccessServiceUserPortPosition,
       "ansAccessServiceUserPortIndex": ansAccessServiceUserPortIndex,
       "ansAccessServiceUserPortLabel": ansAccessServiceUserPortLabel,
       "ansAccessServiceUserPortMaxBwDs": ansAccessServiceUserPortMaxBwDs,
       "ansAccessServiceUserPortMaxBwUs": ansAccessServiceUserPortMaxBwUs,
       "ansAccessServiceUserPortAvailBwDs": ansAccessServiceUserPortAvailBwDs,
       "ansAccessServiceUserPortAvailBwUs": ansAccessServiceUserPortAvailBwUs,
       "ansAccessServiceUserPortMinVpi": ansAccessServiceUserPortMinVpi,
       "ansAccessServiceUserPortMaxVpi": ansAccessServiceUserPortMaxVpi,
       "ansAccessServiceUserPortMinVci": ansAccessServiceUserPortMinVci,
       "ansAccessServiceUserPortMaxVci": ansAccessServiceUserPortMaxVci,
       "ansAccessServiceUserPortOperStatus": ansAccessServiceUserPortOperStatus,
       "ansAccessServiceUserPortAdminStatus": ansAccessServiceUserPortAdminStatus,
       "ansAccessServiceUserPortUsageState": ansAccessServiceUserPortUsageState,
       "ansAccessServiceUserPortAtmFormat": ansAccessServiceUserPortAtmFormat,
       "ansAccessServiceUserPortType": ansAccessServiceUserPortType,
       "accessInternalPort": accessInternalPort,
       "ansAccessInternalPortTable": ansAccessInternalPortTable,
       "ansAccessInternalPortEntry": ansAccessInternalPortEntry,
       "ansAccessInternalPortSystemNode": ansAccessInternalPortSystemNode,
       "ansAccessInternalPortSubrack": ansAccessInternalPortSubrack,
       "ansAccessInternalPortPosition": ansAccessInternalPortPosition,
       "ansAccessInternalPortIndex": ansAccessInternalPortIndex,
       "ansAccessInternalPortLabel": ansAccessInternalPortLabel,
       "ansAccessInternalPortMaxBwDs": ansAccessInternalPortMaxBwDs,
       "ansAccessInternalPortMaxBwUs": ansAccessInternalPortMaxBwUs,
       "ansAccessInternalPortAvailBwDs": ansAccessInternalPortAvailBwDs,
       "ansAccessInternalPortAvailBwUs": ansAccessInternalPortAvailBwUs,
       "ansAccessInternalPortMinVpi": ansAccessInternalPortMinVpi,
       "ansAccessInternalPortMaxVpi": ansAccessInternalPortMaxVpi,
       "ansAccessInternalPortMinVci": ansAccessInternalPortMinVci,
       "ansAccessInternalPortMaxVci": ansAccessInternalPortMaxVci,
       "ansAccessInternalPortOperStatus": ansAccessInternalPortOperStatus,
       "ansAccessInternalPortAdminStatus": ansAccessInternalPortAdminStatus,
       "ansAccessInternalPortUsageState": ansAccessInternalPortUsageState,
       "ansAccessInternalPortAtmFormat": ansAccessInternalPortAtmFormat,
       "ansAccessInternalPortType": ansAccessInternalPortType,
       "ansAtmCreateCC": ansAtmCreateCC,
       "ansAtmCreateCCTable": ansAtmCreateCCTable,
       "ansAtmCreateCCEntry": ansAtmCreateCCEntry,
       "ansAtmCCAUPSystemNode": ansAtmCCAUPSystemNode,
       "ansAtmCCAUPSubrack": ansAtmCCAUPSubrack,
       "ansAtmCCAUPPosition": ansAtmCCAUPPosition,
       "ansAtmCCAUPIndex": ansAtmCCAUPIndex,
       "ansAtmCCAUPVPI": ansAtmCCAUPVPI,
       "ansAtmCCAUPVCI": ansAtmCCAUPVCI,
       "ansAtmCCASPSubrack": ansAtmCCASPSubrack,
       "ansAtmCCASPPosition": ansAtmCCASPPosition,
       "ansAtmCCASPIndex": ansAtmCCASPIndex,
       "ansAtmCCASPVPI": ansAtmCCASPVPI,
       "ansAtmCCASPVCI": ansAtmCCASPVCI,
       "ansAtmCCType": ansAtmCCType,
       "ansAtmCCServiceClass": ansAtmCCServiceClass,
       "ansAtmCCSourceType": ansAtmCCSourceType,
       "ansAtmCCServiceType": ansAtmCCServiceType,
       "ansAtmCCPcrAtoB": ansAtmCCPcrAtoB,
       "ansAtmCCPcrBtoA": ansAtmCCPcrBtoA,
       "ansAtmCCMulti": ansAtmCCMulti,
       "ansAtmCCAdminStatus": ansAtmCCAdminStatus,
       "ansAtmCCRowStatus": ansAtmCCRowStatus,
       "ansCeAtmCreateCC": ansCeAtmCreateCC,
       "ansCeAtmCreateCCTable": ansCeAtmCreateCCTable,
       "ansCeAtmCreateCCEntry": ansCeAtmCreateCCEntry,
       "ansCeAtmCCAUPSystemNode": ansCeAtmCCAUPSystemNode,
       "ansCeAtmCCAUPSubrack": ansCeAtmCCAUPSubrack,
       "ansCeAtmCCAUPPosition": ansCeAtmCCAUPPosition,
       "ansCeAtmCCAUPIndex": ansCeAtmCCAUPIndex,
       "ansCeAtmCCAUPVPI": ansCeAtmCCAUPVPI,
       "ansCeAtmCCAUPVCI": ansCeAtmCCAUPVCI,
       "ansCeAtmCCASPSubrack": ansCeAtmCCASPSubrack,
       "ansCeAtmCCASPPosition": ansCeAtmCCASPPosition,
       "ansCeAtmCCASPIndex": ansCeAtmCCASPIndex,
       "ansCeAtmCCASPVPI": ansCeAtmCCASPVPI,
       "ansCeAtmCCASPVCI": ansCeAtmCCASPVCI,
       "ansCeAtmCCType": ansCeAtmCCType,
       "ansCeAtmCCServiceClass": ansCeAtmCCServiceClass,
       "ansCeAtmCCSourceType": ansCeAtmCCSourceType,
       "ansCeAtmCCPcrAtoB": ansCeAtmCCPcrAtoB,
       "ansCeAtmCCPcrBtoA": ansCeAtmCCPcrBtoA,
       "ansCeAtmCCMulti": ansCeAtmCCMulti,
       "ansCeAtmCCAdminStatus": ansCeAtmCCAdminStatus,
       "ansCeAtmCCTimeSlotPa": ansCeAtmCCTimeSlotPa,
       "ansCeAtmCCTypePa": ansCeAtmCCTypePa,
       "ansCeAtmCCFillLevelPa": ansCeAtmCCFillLevelPa,
       "ansCeAtmCCCdvtPa": ansCeAtmCCCdvtPa,
       "ansCeAtmCCMaxBuffSizePa": ansCeAtmCCMaxBuffSizePa,
       "ansCeAtmCCTcModePa": ansCeAtmCCTcModePa,
       "ansCeAtmCCTcTypePa": ansCeAtmCCTcTypePa,
       "ansCeAtmCCTcBtoAPa": ansCeAtmCCTcBtoAPa,
       "ansCeAtmCCTcAtoBPa": ansCeAtmCCTcAtoBPa,
       "ansCeAtmCCRowStatus": ansCeAtmCCRowStatus,
       "ansCeCeCreateCC": ansCeCeCreateCC,
       "ansCeCeCreateCCTable": ansCeCeCreateCCTable,
       "ansCeCeCreateCCEntry": ansCeCeCreateCCEntry,
       "ansCeCeCCAUPSystemNode": ansCeCeCCAUPSystemNode,
       "ansCeCeCCAUPSubrack": ansCeCeCCAUPSubrack,
       "ansCeCeCCAUPPosition": ansCeCeCCAUPPosition,
       "ansCeCeCCAUPIndex": ansCeCeCCAUPIndex,
       "ansCeCeCCAUPVPI": ansCeCeCCAUPVPI,
       "ansCeCeCCAUPVCI": ansCeCeCCAUPVCI,
       "ansCeCeCCASPSubrack": ansCeCeCCASPSubrack,
       "ansCeCeCCASPPosition": ansCeCeCCASPPosition,
       "ansCeCeCCASPIndex": ansCeCeCCASPIndex,
       "ansCeCeCCASPVPI": ansCeCeCCASPVPI,
       "ansCeCeCCASPVCI": ansCeCeCCASPVCI,
       "ansCeCeCCType": ansCeCeCCType,
       "ansCeCeCCServiceClass": ansCeCeCCServiceClass,
       "ansCeCeCCSourceType": ansCeCeCCSourceType,
       "ansCeCeCCPcrAtoB": ansCeCeCCPcrAtoB,
       "ansCeCeCCPcrBtoA": ansCeCeCCPcrBtoA,
       "ansCeCeCCMulti": ansCeCeCCMulti,
       "ansCeCeCCAdminStatus": ansCeCeCCAdminStatus,
       "ansCeCeCCTimeSlotPa": ansCeCeCCTimeSlotPa,
       "ansCeCeCCTypePa": ansCeCeCCTypePa,
       "ansCeCeCCFillLevelPa": ansCeCeCCFillLevelPa,
       "ansCeCeCCCdvtPa": ansCeCeCCCdvtPa,
       "ansCeCeCCMaxBuffSizePa": ansCeCeCCMaxBuffSizePa,
       "ansCeCeCCTcModePa": ansCeCeCCTcModePa,
       "ansCeCeCCTcTypePa": ansCeCeCCTcTypePa,
       "ansCeCeCCTcBtoAPa": ansCeCeCCTcBtoAPa,
       "ansCeCeCCTcAtoBPa": ansCeCeCCTcAtoBPa,
       "ansCeCeCCTimeSlotPb": ansCeCeCCTimeSlotPb,
       "ansCeCeCCTypePb": ansCeCeCCTypePb,
       "ansCeCeCCFillLevelPb": ansCeCeCCFillLevelPb,
       "ansCeCeCCCdvtPb": ansCeCeCCCdvtPb,
       "ansCeCeCCMaxBuffSizePb": ansCeCeCCMaxBuffSizePb,
       "ansCeCeCCTcModePb": ansCeCeCCTcModePb,
       "ansCeCeCCTcTypePb": ansCeCeCCTcTypePb,
       "ansCeCeCCTcBtoAPb": ansCeCeCCTcBtoAPb,
       "ansCeCeCCTcAtoBPb": ansCeCeCCTcAtoBPb,
       "ansCeCeCCRowStatus": ansCeCeCCRowStatus,
       "ansCrossConnect": ansCrossConnect,
       "ansCrossConnectTable": ansCrossConnectTable,
       "ansCrossConnectEntry": ansCrossConnectEntry,
       "ansCCAUPSystemNode": ansCCAUPSystemNode,
       "ansCCAUPSubrack": ansCCAUPSubrack,
       "ansCCAUPPosition": ansCCAUPPosition,
       "ansCCAUPIndex": ansCCAUPIndex,
       "ansCCAUPVPI": ansCCAUPVPI,
       "ansCCAUPVCI": ansCCAUPVCI,
       "ansCCASPSubrack": ansCCASPSubrack,
       "ansCCASPPosition": ansCCASPPosition,
       "ansCCASPIndex": ansCCASPIndex,
       "ansCCASPVPI": ansCCASPVPI,
       "ansCCASPVCI": ansCCASPVCI,
       "ansCCType": ansCCType,
       "ansCCServiceClass": ansCCServiceClass,
       "ansCCPcrAtoB": ansCCPcrAtoB,
       "ansCCPcrBtoA": ansCCPcrBtoA,
       "ansCCSourceType": ansCCSourceType,
       "ansCCServiceType": ansCCServiceType,
       "ansCCOperStatus": ansCCOperStatus,
       "ansCCLastOperStatusChange": ansCCLastOperStatusChange,
       "ansCCAdminStatus": ansCCAdminStatus,
       "ansCCMulti": ansCCMulti,
       "ansCCRowStatus": ansCCRowStatus,
       "ansApplData": ansApplData,
       "ansApplDataTable": ansApplDataTable,
       "ansApplDataEntry": ansApplDataEntry,
       "ansApplDataSystemNode": ansApplDataSystemNode,
       "ansApplDataSubrack": ansApplDataSubrack,
       "ansApplDataPosition": ansApplDataPosition,
       "ansApplDataIndex": ansApplDataIndex,
       "ansApplDataVPI": ansApplDataVPI,
       "ansApplDataVCI": ansApplDataVCI,
       "ansApplDataOpState": ansApplDataOpState,
       "ansApplDataAdminState": ansApplDataAdminState,
       "ansApplDataServiceParams": ansApplDataServiceParams,
       "ansAal1Pars": ansAal1Pars,
       "ansAal1ParsTable": ansAal1ParsTable,
       "ansAal1ParsEntry": ansAal1ParsEntry,
       "ansAal1ParsTimeSlot": ansAal1ParsTimeSlot,
       "ansAal1ParsType": ansAal1ParsType,
       "ansAal1ParsFillLevel": ansAal1ParsFillLevel,
       "ansAal1ParsCdvt": ansAal1ParsCdvt,
       "ansAal1ParsMaxBuffSize": ansAal1ParsMaxBuffSize,
       "ansAal1ParsTcMode": ansAal1ParsTcMode,
       "ansAal1ParsTcType": ansAal1ParsTcType,
       "ansAal1ParsTcBtoA": ansAal1ParsTcBtoA,
       "ansAal1ParsTcAtoB": ansAal1ParsTcAtoB,
       "ansEthPars": ansEthPars,
       "ansEthParsTable": ansEthParsTable,
       "ansEthParsEntry": ansEthParsEntry,
       "ansEthParsPcrShaping": ansEthParsPcrShaping,
       "ethernetPort": ethernetPort,
       "ethernetPortTable": ethernetPortTable,
       "ethernetPortEntry": ethernetPortEntry,
       "ethernetPortFcsEncapsulation": ethernetPortFcsEncapsulation,
       "ethernetPortMuxOrEncapsulation": ethernetPortMuxOrEncapsulation,
       "ethernetPortIpAddress": ethernetPortIpAddress,
       "ethernetPortType": ethernetPortType,
       "ethernetPortOperatingMode": ethernetPortOperatingMode,
       "pdhPort": pdhPort,
       "pdhPortTable": pdhPortTable,
       "pdhPortEntry": pdhPortEntry,
       "pdhPortPort": pdhPortPort,
       "pdhPortTsUsed": pdhPortTsUsed,
       "pdhPortClockMode": pdhPortClockMode,
       "pdhPortHaulMode": pdhPortHaulMode,
       "pdhPortLineCode": pdhPortLineCode,
       "pdhPortLoopback": pdhPortLoopback,
       "pdhPortCas": pdhPortCas,
       "pdhPortFrameFormat": pdhPortFrameFormat,
       "pdhPortServiceType": pdhPortServiceType,
       "terminalId": terminalId,
       "ansTerminalIdTable": ansTerminalIdTable,
       "ansTerminalIdEntry": ansTerminalIdEntry,
       "ansTerminalIdIdent": ansTerminalIdIdent,
       "ansTerminalIdSystemNode": ansTerminalIdSystemNode,
       "ansTerminalIdSubrack": ansTerminalIdSubrack,
       "ansTerminalIdPosition": ansTerminalIdPosition}
)
