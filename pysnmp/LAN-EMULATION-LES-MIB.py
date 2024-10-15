# SNMP MIB module (LAN-EMULATION-LES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LAN-EMULATION-LES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:07 2024
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

(LeArpTableEntryType,
 VciInteger,
 VpiInteger,
 atmfLanEmulation) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "LeArpTableEntryType",
    "VciInteger",
    "VpiInteger",
    "atmfLanEmulation")

(AtmLaneMask,
 IfIndexOrZero,
 Integer,
 TIMESTAMP) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "AtmLaneMask",
    "IfIndexOrZero",
    "Integer",
    "TIMESTAMP")

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




class AtmLaneAddress(OctetString):
    """Custom type AtmLaneAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class LesLecDataFrameFormat(Integer32):
    """Custom type LesLecDataFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3))
    )





class LesLecDataFrameSize(Integer32):
    """Custom type LesLecDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("max1516", 2),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LesMIB_ObjectIdentity = ObjectIdentity
lesMIB = _LesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3)
)
_LesConfGroup_ObjectIdentity = ObjectIdentity
lesConfGroup = _LesConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1)
)
_LesConfNextId_Type = Integer32
_LesConfNextId_Object = MibScalar
lesConfNextId = _LesConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 1),
    _LesConfNextId_Type()
)
lesConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesConfNextId.setStatus("mandatory")
_LesConfTable_Object = MibTable
lesConfTable = _LesConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lesConfTable.setStatus("mandatory")
_LesConfEntry_Object = MibTableRow
lesConfEntry = _LesConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1)
)
lesConfEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    lesConfEntry.setStatus("mandatory")
_LesConfIndex_Type = Integer32
_LesConfIndex_Object = MibTableColumn
lesConfIndex = _LesConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 1),
    _LesConfIndex_Type()
)
lesConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesConfIndex.setStatus("mandatory")
_LesAtmAddrSpec_Type = AtmLaneAddress
_LesAtmAddrSpec_Object = MibTableColumn
lesAtmAddrSpec = _LesAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 2),
    _LesAtmAddrSpec_Type()
)
lesAtmAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesAtmAddrSpec.setStatus("mandatory")


class _LesAtmAddrMask_Type(AtmLaneMask):
    """Custom type lesAtmAddrMask based on AtmLaneMask"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"


_LesAtmAddrMask_Object = MibTableColumn
lesAtmAddrMask = _LesAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 3),
    _LesAtmAddrMask_Type()
)
lesAtmAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesAtmAddrMask.setStatus("mandatory")
_LesAtmAddrActual_Type = AtmLaneAddress
_LesAtmAddrActual_Object = MibTableColumn
lesAtmAddrActual = _LesAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 4),
    _LesAtmAddrActual_Type()
)
lesAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesAtmAddrActual.setStatus("mandatory")


class _LesElanName_Type(DisplayString):
    """Custom type lesElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LesElanName_Type.__name__ = "DisplayString"
_LesElanName_Object = MibTableColumn
lesElanName = _LesElanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 5),
    _LesElanName_Type()
)
lesElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesElanName.setStatus("mandatory")
_LesLanType_Type = LesLecDataFrameFormat
_LesLanType_Object = MibTableColumn
lesLanType = _LesLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 6),
    _LesLanType_Type()
)
lesLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLanType.setStatus("mandatory")
_LesLastChange_Type = TIMESTAMP
_LesLastChange_Object = MibTableColumn
lesLastChange = _LesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 7),
    _LesLastChange_Type()
)
lesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLastChange.setStatus("mandatory")
_LesMaxFrameSize_Type = LesLecDataFrameSize
_LesMaxFrameSize_Object = MibTableColumn
lesMaxFrameSize = _LesMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 8),
    _LesMaxFrameSize_Type()
)
lesMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesMaxFrameSize.setStatus("mandatory")


class _LesControlTimeOut_Type(Integer32):
    """Custom type lesControlTimeOut based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LesControlTimeOut_Type.__name__ = "Integer32"
_LesControlTimeOut_Object = MibTableColumn
lesControlTimeOut = _LesControlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 9),
    _LesControlTimeOut_Type()
)
lesControlTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesControlTimeOut.setStatus("mandatory")


class _LesOperStatus_Type(Integer32):
    """Custom type lesOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_LesOperStatus_Type.__name__ = "Integer32"
_LesOperStatus_Object = MibTableColumn
lesOperStatus = _LesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 11),
    _LesOperStatus_Type()
)
lesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOperStatus.setStatus("mandatory")


class _LesAdminStatus_Type(Integer32):
    """Custom type lesAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_LesAdminStatus_Type.__name__ = "Integer32"
_LesAdminStatus_Object = MibTableColumn
lesAdminStatus = _LesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 12),
    _LesAdminStatus_Type()
)
lesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesAdminStatus.setStatus("mandatory")
_LesRowStatus_Type = RowStatus
_LesRowStatus_Object = MibTableColumn
lesRowStatus = _LesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 13),
    _LesRowStatus_Type()
)
lesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesRowStatus.setStatus("mandatory")
_LesVccTable_Object = MibTable
lesVccTable = _LesVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lesVccTable.setStatus("mandatory")
_LesVccEntry_Object = MibTableRow
lesVccEntry = _LesVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1)
)
lesVccEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesVccAtmIfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesVccCtlDistVpi"),
    (0, "LAN-EMULATION-LES-MIB", "lesVccCtlDistVci"),
)
if mibBuilder.loadTexts:
    lesVccEntry.setStatus("mandatory")
_LesVccAtmIfIndex_Type = IfIndexOrZero
_LesVccAtmIfIndex_Object = MibTableColumn
lesVccAtmIfIndex = _LesVccAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 1),
    _LesVccAtmIfIndex_Type()
)
lesVccAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesVccAtmIfIndex.setStatus("mandatory")
_LesVccCtlDistVpi_Type = VpiInteger
_LesVccCtlDistVpi_Object = MibTableColumn
lesVccCtlDistVpi = _LesVccCtlDistVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 2),
    _LesVccCtlDistVpi_Type()
)
lesVccCtlDistVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesVccCtlDistVpi.setStatus("mandatory")
_LesVccCtlDistVci_Type = VciInteger
_LesVccCtlDistVci_Object = MibTableColumn
lesVccCtlDistVci = _LesVccCtlDistVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 3),
    _LesVccCtlDistVci_Type()
)
lesVccCtlDistVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesVccCtlDistVci.setStatus("mandatory")
_LesVccRowStatus_Type = RowStatus
_LesVccRowStatus_Object = MibTableColumn
lesVccRowStatus = _LesVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 4),
    _LesVccRowStatus_Type()
)
lesVccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesVccRowStatus.setStatus("mandatory")
_LesBusTable_Object = MibTable
lesBusTable = _LesBusTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    lesBusTable.setStatus("mandatory")
_LesBusEntry_Object = MibTableRow
lesBusEntry = _LesBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4, 1)
)
lesBusEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesBusConfIndex"),
)
if mibBuilder.loadTexts:
    lesBusEntry.setStatus("mandatory")
_LesBusConfIndex_Type = Integer32
_LesBusConfIndex_Object = MibTableColumn
lesBusConfIndex = _LesBusConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4, 1, 1),
    _LesBusConfIndex_Type()
)
lesBusConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesBusConfIndex.setStatus("mandatory")
_LesBusAddress_Type = AtmLaneAddress
_LesBusAddress_Object = MibTableColumn
lesBusAddress = _LesBusAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4, 1, 2),
    _LesBusAddress_Type()
)
lesBusAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesBusAddress.setStatus("mandatory")
_LesLeArpMacTable_Object = MibTable
lesLeArpMacTable = _LesLeArpMacTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    lesLeArpMacTable.setStatus("mandatory")
_LesLeArpMacEntry_Object = MibTableRow
lesLeArpMacEntry = _LesLeArpMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1)
)
lesLeArpMacEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLeArpMacAddr"),
)
if mibBuilder.loadTexts:
    lesLeArpMacEntry.setStatus("mandatory")
_LesLeArpMacAddr_Type = MacAddress
_LesLeArpMacAddr_Object = MibTableColumn
lesLeArpMacAddr = _LesLeArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 1),
    _LesLeArpMacAddr_Type()
)
lesLeArpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLeArpMacAddr.setStatus("mandatory")


class _LesLeArpLecId_Type(Integer32):
    """Custom type lesLeArpLecId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_LesLeArpLecId_Type.__name__ = "Integer32"
_LesLeArpLecId_Object = MibTableColumn
lesLeArpLecId = _LesLeArpLecId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 2),
    _LesLeArpLecId_Type()
)
lesLeArpLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeArpLecId.setStatus("mandatory")
_LesLeArpAtmAddr_Type = AtmLaneAddress
_LesLeArpAtmAddr_Object = MibTableColumn
lesLeArpAtmAddr = _LesLeArpAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 3),
    _LesLeArpAtmAddr_Type()
)
lesLeArpAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeArpAtmAddr.setStatus("mandatory")


class _LesLeArpEntryType_Type(LeArpTableEntryType):
    """Custom type lesLeArpEntryType based on LeArpTableEntryType"""


_LesLeArpEntryType_Object = MibTableColumn
lesLeArpEntryType = _LesLeArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 4),
    _LesLeArpEntryType_Type()
)
lesLeArpEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeArpEntryType.setStatus("mandatory")
_LesLeArpRowStatus_Type = RowStatus
_LesLeArpRowStatus_Object = MibTableColumn
lesLeArpRowStatus = _LesLeArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 5),
    _LesLeArpRowStatus_Type()
)
lesLeArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeArpRowStatus.setStatus("mandatory")
_LesLeArpRdTable_Object = MibTable
lesLeArpRdTable = _LesLeArpRdTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6)
)
if mibBuilder.loadTexts:
    lesLeArpRdTable.setStatus("mandatory")
_LesLeArpRdEntry_Object = MibTableRow
lesLeArpRdEntry = _LesLeArpRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1)
)
lesLeArpRdEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLeArpRdSegId"),
    (0, "LAN-EMULATION-LES-MIB", "lesLeArpRdBridgeNum"),
)
if mibBuilder.loadTexts:
    lesLeArpRdEntry.setStatus("mandatory")


class _LesLeArpRdSegId_Type(Integer32):
    """Custom type lesLeArpRdSegId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LesLeArpRdSegId_Type.__name__ = "Integer32"
_LesLeArpRdSegId_Object = MibTableColumn
lesLeArpRdSegId = _LesLeArpRdSegId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 1),
    _LesLeArpRdSegId_Type()
)
lesLeArpRdSegId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLeArpRdSegId.setStatus("mandatory")


class _LesLeArpRdBridgeNum_Type(Integer32):
    """Custom type lesLeArpRdBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LesLeArpRdBridgeNum_Type.__name__ = "Integer32"
_LesLeArpRdBridgeNum_Object = MibTableColumn
lesLeArpRdBridgeNum = _LesLeArpRdBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 2),
    _LesLeArpRdBridgeNum_Type()
)
lesLeArpRdBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLeArpRdBridgeNum.setStatus("mandatory")


class _LesLeArpRdLecId_Type(Integer32):
    """Custom type lesLeArpRdLecId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_LesLeArpRdLecId_Type.__name__ = "Integer32"
_LesLeArpRdLecId_Object = MibTableColumn
lesLeArpRdLecId = _LesLeArpRdLecId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 3),
    _LesLeArpRdLecId_Type()
)
lesLeArpRdLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeArpRdLecId.setStatus("mandatory")
_LesLeArpRdAtmAddr_Type = AtmLaneAddress
_LesLeArpRdAtmAddr_Object = MibTableColumn
lesLeArpRdAtmAddr = _LesLeArpRdAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 4),
    _LesLeArpRdAtmAddr_Type()
)
lesLeArpRdAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeArpRdAtmAddr.setStatus("mandatory")


class _LesLeArpRdEntryType_Type(LeArpTableEntryType):
    """Custom type lesLeArpRdEntryType based on LeArpTableEntryType"""


_LesLeArpRdEntryType_Object = MibTableColumn
lesLeArpRdEntryType = _LesLeArpRdEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 5),
    _LesLeArpRdEntryType_Type()
)
lesLeArpRdEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeArpRdEntryType.setStatus("mandatory")
_LesLeArpRdRowStatus_Type = RowStatus
_LesLeArpRdRowStatus_Object = MibTableColumn
lesLeArpRdRowStatus = _LesLeArpRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 6),
    _LesLeArpRdRowStatus_Type()
)
lesLeArpRdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLeArpRdRowStatus.setStatus("mandatory")
_LesLecTableLastChange_Type = TIMESTAMP
_LesLecTableLastChange_Object = MibScalar
lesLecTableLastChange = _LesLecTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 7),
    _LesLecTableLastChange_Type()
)
lesLecTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecTableLastChange.setStatus("mandatory")
_LesLecTable_Object = MibTable
lesLecTable = _LesLecTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8)
)
if mibBuilder.loadTexts:
    lesLecTable.setStatus("mandatory")
_LesLecEntry_Object = MibTableRow
lesLecEntry = _LesLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1)
)
lesLecEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLecIndex"),
)
if mibBuilder.loadTexts:
    lesLecEntry.setStatus("mandatory")


class _LesLecIndex_Type(Integer32):
    """Custom type lesLecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LesLecIndex_Type.__name__ = "Integer32"
_LesLecIndex_Object = MibTableColumn
lesLecIndex = _LesLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 1),
    _LesLecIndex_Type()
)
lesLecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLecIndex.setStatus("mandatory")
_LesLecAtmAddr_Type = AtmLaneAddress
_LesLecAtmAddr_Object = MibTableColumn
lesLecAtmAddr = _LesLecAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 2),
    _LesLecAtmAddr_Type()
)
lesLecAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecAtmAddr.setStatus("mandatory")


class _LesLecProxy_Type(TruthValue):
    """Custom type lesLecProxy based on TruthValue"""


_LesLecProxy_Object = MibTableColumn
lesLecProxy = _LesLecProxy_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 3),
    _LesLecProxy_Type()
)
lesLecProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecProxy.setStatus("mandatory")


class _LesLecId_Type(Integer32):
    """Custom type lesLecId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_LesLecId_Type.__name__ = "Integer32"
_LesLecId_Object = MibTableColumn
lesLecId = _LesLecId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 4),
    _LesLecId_Type()
)
lesLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecId.setStatus("mandatory")
_LesLecAtmIfIndex_Type = IfIndexOrZero
_LesLecAtmIfIndex_Object = MibTableColumn
lesLecAtmIfIndex = _LesLecAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 5),
    _LesLecAtmIfIndex_Type()
)
lesLecAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecAtmIfIndex.setStatus("mandatory")
_LesLecCtlDirectVpi_Type = VpiInteger
_LesLecCtlDirectVpi_Object = MibTableColumn
lesLecCtlDirectVpi = _LesLecCtlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 6),
    _LesLecCtlDirectVpi_Type()
)
lesLecCtlDirectVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecCtlDirectVpi.setStatus("mandatory")
_LesLecCtlDirectVci_Type = VciInteger
_LesLecCtlDirectVci_Object = MibTableColumn
lesLecCtlDirectVci = _LesLecCtlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 7),
    _LesLecCtlDirectVci_Type()
)
lesLecCtlDirectVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecCtlDirectVci.setStatus("mandatory")
_LesLecLastChange_Type = TIMESTAMP
_LesLecLastChange_Object = MibTableColumn
lesLecLastChange = _LesLecLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 8),
    _LesLecLastChange_Type()
)
lesLecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecLastChange.setStatus("mandatory")


class _LesLecState_Type(Integer32):
    """Custom type lesLecState based on Integer32"""
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
        *(("addLec", 5),
          ("joinedLes", 6),
          ("joining", 4),
          ("lesConnect", 3),
          ("noLesConnect", 2),
          ("other", 1))
    )


_LesLecState_Type.__name__ = "Integer32"
_LesLecState_Object = MibTableColumn
lesLecState = _LesLecState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 9),
    _LesLecState_Type()
)
lesLecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecState.setStatus("mandatory")
_LesLecRowStatus_Type = RowStatus
_LesLecRowStatus_Object = MibTableColumn
lesLecRowStatus = _LesLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 10),
    _LesLecRowStatus_Type()
)
lesLecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecRowStatus.setStatus("mandatory")
_LesStatGroup_ObjectIdentity = ObjectIdentity
lesStatGroup = _LesStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2)
)
_LesStatTable_Object = MibTable
lesStatTable = _LesStatTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lesStatTable.setStatus("mandatory")
_LesStatEntry_Object = MibTableRow
lesStatEntry = _LesStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1)
)
lesStatEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    lesStatEntry.setStatus("mandatory")
_LesStatJoinOk_Type = Counter32
_LesStatJoinOk_Object = MibTableColumn
lesStatJoinOk = _LesStatJoinOk_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 1),
    _LesStatJoinOk_Type()
)
lesStatJoinOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatJoinOk.setStatus("mandatory")
_LesStatVerNotSup_Type = Counter32
_LesStatVerNotSup_Object = MibTableColumn
lesStatVerNotSup = _LesStatVerNotSup_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 2),
    _LesStatVerNotSup_Type()
)
lesStatVerNotSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatVerNotSup.setStatus("mandatory")
_LesStatInvalidReqParam_Type = Counter32
_LesStatInvalidReqParam_Object = MibTableColumn
lesStatInvalidReqParam = _LesStatInvalidReqParam_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 3),
    _LesStatInvalidReqParam_Type()
)
lesStatInvalidReqParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidReqParam.setStatus("mandatory")
_LesStatDupLanDest_Type = Counter32
_LesStatDupLanDest_Object = MibTableColumn
lesStatDupLanDest = _LesStatDupLanDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 4),
    _LesStatDupLanDest_Type()
)
lesStatDupLanDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatDupLanDest.setStatus("mandatory")
_LesStatDupAtmAddr_Type = Counter32
_LesStatDupAtmAddr_Object = MibTableColumn
lesStatDupAtmAddr = _LesStatDupAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 5),
    _LesStatDupAtmAddr_Type()
)
lesStatDupAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatDupAtmAddr.setStatus("mandatory")
_LesStatInsRes_Type = Counter32
_LesStatInsRes_Object = MibTableColumn
lesStatInsRes = _LesStatInsRes_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 6),
    _LesStatInsRes_Type()
)
lesStatInsRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInsRes.setStatus("mandatory")
_LesStatAccDenied_Type = Counter32
_LesStatAccDenied_Object = MibTableColumn
lesStatAccDenied = _LesStatAccDenied_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 7),
    _LesStatAccDenied_Type()
)
lesStatAccDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatAccDenied.setStatus("mandatory")
_LesStatInvalidReqId_Type = Counter32
_LesStatInvalidReqId_Object = MibTableColumn
lesStatInvalidReqId = _LesStatInvalidReqId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 8),
    _LesStatInvalidReqId_Type()
)
lesStatInvalidReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidReqId.setStatus("mandatory")
_LesStatInvalidLanDest_Type = Counter32
_LesStatInvalidLanDest_Object = MibTableColumn
lesStatInvalidLanDest = _LesStatInvalidLanDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 9),
    _LesStatInvalidLanDest_Type()
)
lesStatInvalidLanDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidLanDest.setStatus("mandatory")
_LesStatInvalidAtmAddr_Type = Counter32
_LesStatInvalidAtmAddr_Object = MibTableColumn
lesStatInvalidAtmAddr = _LesStatInvalidAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 10),
    _LesStatInvalidAtmAddr_Type()
)
lesStatInvalidAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidAtmAddr.setStatus("mandatory")
_LesStatInBadPkts_Type = Counter32
_LesStatInBadPkts_Object = MibTableColumn
lesStatInBadPkts = _LesStatInBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 11),
    _LesStatInBadPkts_Type()
)
lesStatInBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInBadPkts.setStatus("mandatory")
_LesStatOutRegFails_Type = Counter32
_LesStatOutRegFails_Object = MibTableColumn
lesStatOutRegFails = _LesStatOutRegFails_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 12),
    _LesStatOutRegFails_Type()
)
lesStatOutRegFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatOutRegFails.setStatus("mandatory")
_LesStatLeArpIn_Type = Counter32
_LesStatLeArpIn_Object = MibTableColumn
lesStatLeArpIn = _LesStatLeArpIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 13),
    _LesStatLeArpIn_Type()
)
lesStatLeArpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatLeArpIn.setStatus("mandatory")
_LesStatLeArpFwd_Type = Counter32
_LesStatLeArpFwd_Object = MibTableColumn
lesStatLeArpFwd = _LesStatLeArpFwd_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 14),
    _LesStatLeArpFwd_Type()
)
lesStatLeArpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatLeArpFwd.setStatus("mandatory")
_LesLecStatGroup_ObjectIdentity = ObjectIdentity
lesLecStatGroup = _LesLecStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3)
)
_LesLecStatTable_Object = MibTable
lesLecStatTable = _LesLecStatTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lesLecStatTable.setStatus("mandatory")
_LesLecStatEntry_Object = MibTableRow
lesLecStatEntry = _LesLecStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1)
)
lesLecStatEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLecIndex"),
)
if mibBuilder.loadTexts:
    lesLecStatEntry.setStatus("mandatory")
_LesLecRecvs_Type = Counter32
_LesLecRecvs_Object = MibTableColumn
lesLecRecvs = _LesLecRecvs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 1),
    _LesLecRecvs_Type()
)
lesLecRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecRecvs.setStatus("mandatory")
_LesLecSends_Type = Counter32
_LesLecSends_Object = MibTableColumn
lesLecSends = _LesLecSends_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 3),
    _LesLecSends_Type()
)
lesLecSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecSends.setStatus("mandatory")
_LesLecInRegReq_Type = Counter32
_LesLecInRegReq_Object = MibTableColumn
lesLecInRegReq = _LesLecInRegReq_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 4),
    _LesLecInRegReq_Type()
)
lesLecInRegReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInRegReq.setStatus("mandatory")
_LesLecInUnReg_Type = Counter32
_LesLecInUnReg_Object = MibTableColumn
lesLecInUnReg = _LesLecInUnReg_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 5),
    _LesLecInUnReg_Type()
)
lesLecInUnReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInUnReg.setStatus("mandatory")
_LesLecInLeArpUcast_Type = Counter32
_LesLecInLeArpUcast_Object = MibTableColumn
lesLecInLeArpUcast = _LesLecInLeArpUcast_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 6),
    _LesLecInLeArpUcast_Type()
)
lesLecInLeArpUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInLeArpUcast.setStatus("mandatory")
_LesLecInLeArpBcast_Type = Counter32
_LesLecInLeArpBcast_Object = MibTableColumn
lesLecInLeArpBcast = _LesLecInLeArpBcast_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 7),
    _LesLecInLeArpBcast_Type()
)
lesLecInLeArpBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInLeArpBcast.setStatus("mandatory")
_LesLecInLeArpResp_Type = Counter32
_LesLecInLeArpResp_Object = MibTableColumn
lesLecInLeArpResp = _LesLecInLeArpResp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 8),
    _LesLecInLeArpResp_Type()
)
lesLecInLeArpResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInLeArpResp.setStatus("mandatory")
_LesLecInNArp_Type = Counter32
_LesLecInNArp_Object = MibTableColumn
lesLecInNArp = _LesLecInNArp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 10),
    _LesLecInNArp_Type()
)
lesLecInNArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInNArp.setStatus("mandatory")
_LesFaultGroup_ObjectIdentity = ObjectIdentity
lesFaultGroup = _LesFaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4)
)
_LesErrCtlTable_Object = MibTable
lesErrCtlTable = _LesErrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lesErrCtlTable.setStatus("mandatory")
_LesErrCtlEntry_Object = MibTableRow
lesErrCtlEntry = _LesErrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1)
)
lesErrCtlEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    lesErrCtlEntry.setStatus("mandatory")


class _LesErrCtlAdminStatus_Type(Integer32):
    """Custom type lesErrCtlAdminStatus based on Integer32"""
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


_LesErrCtlAdminStatus_Type.__name__ = "Integer32"
_LesErrCtlAdminStatus_Object = MibTableColumn
lesErrCtlAdminStatus = _LesErrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 1),
    _LesErrCtlAdminStatus_Type()
)
lesErrCtlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesErrCtlAdminStatus.setStatus("mandatory")


class _LesErrCtlOperStatus_Type(Integer32):
    """Custom type lesErrCtlOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 5),
          ("failed", 4),
          ("other", 1),
          ("outOfRes", 3))
    )


_LesErrCtlOperStatus_Type.__name__ = "Integer32"
_LesErrCtlOperStatus_Object = MibTableColumn
lesErrCtlOperStatus = _LesErrCtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 2),
    _LesErrCtlOperStatus_Type()
)
lesErrCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrCtlOperStatus.setStatus("mandatory")


class _LesErrCtlClearLog_Type(Integer32):
    """Custom type lesErrCtlClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noOp", 1))
    )


_LesErrCtlClearLog_Type.__name__ = "Integer32"
_LesErrCtlClearLog_Object = MibTableColumn
lesErrCtlClearLog = _LesErrCtlClearLog_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 3),
    _LesErrCtlClearLog_Type()
)
lesErrCtlClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesErrCtlClearLog.setStatus("mandatory")


class _LesErrCtlMaxEntries_Type(Integer32):
    """Custom type lesErrCtlMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LesErrCtlMaxEntries_Type.__name__ = "Integer32"
_LesErrCtlMaxEntries_Object = MibTableColumn
lesErrCtlMaxEntries = _LesErrCtlMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 4),
    _LesErrCtlMaxEntries_Type()
)
lesErrCtlMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrCtlMaxEntries.setStatus("mandatory")


class _LesErrCtlLastEntry_Type(Integer32):
    """Custom type lesErrCtlLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LesErrCtlLastEntry_Type.__name__ = "Integer32"
_LesErrCtlLastEntry_Object = MibTableColumn
lesErrCtlLastEntry = _LesErrCtlLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 5),
    _LesErrCtlLastEntry_Type()
)
lesErrCtlLastEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesErrCtlLastEntry.setStatus("mandatory")
_LesErrLogTable_Object = MibTable
lesErrLogTable = _LesErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    lesErrLogTable.setStatus("mandatory")
_LesErrLogEntry_Object = MibTableRow
lesErrLogEntry = _LesErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1)
)
lesErrLogEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesErrLogIndex"),
)
if mibBuilder.loadTexts:
    lesErrLogEntry.setStatus("mandatory")


class _LesErrLogIndex_Type(Integer32):
    """Custom type lesErrLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LesErrLogIndex_Type.__name__ = "Integer32"
_LesErrLogIndex_Object = MibTableColumn
lesErrLogIndex = _LesErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 1),
    _LesErrLogIndex_Type()
)
lesErrLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesErrLogIndex.setStatus("mandatory")
_LesErrLogAtmAddr_Type = AtmLaneAddress
_LesErrLogAtmAddr_Object = MibTableColumn
lesErrLogAtmAddr = _LesErrLogAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 2),
    _LesErrLogAtmAddr_Type()
)
lesErrLogAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrLogAtmAddr.setStatus("mandatory")


class _LesErrLogErrCode_Type(Integer32):
    """Custom type lesErrLogErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_LesErrLogErrCode_Type.__name__ = "Integer32"
_LesErrLogErrCode_Object = MibTableColumn
lesErrLogErrCode = _LesErrLogErrCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 3),
    _LesErrLogErrCode_Type()
)
lesErrLogErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrLogErrCode.setStatus("mandatory")
_LesErrLogTime_Type = TIMESTAMP
_LesErrLogTime_Object = MibTableColumn
lesErrLogTime = _LesErrLogTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 4),
    _LesErrLogTime_Type()
)
lesErrLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrLogTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-EMULATION-LES-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "AtmLaneAddress": AtmLaneAddress,
       "MacAddress": MacAddress,
       "LesLecDataFrameFormat": LesLecDataFrameFormat,
       "LesLecDataFrameSize": LesLecDataFrameSize,
       "lesMIB": lesMIB,
       "lesConfGroup": lesConfGroup,
       "lesConfNextId": lesConfNextId,
       "lesConfTable": lesConfTable,
       "lesConfEntry": lesConfEntry,
       "lesConfIndex": lesConfIndex,
       "lesAtmAddrSpec": lesAtmAddrSpec,
       "lesAtmAddrMask": lesAtmAddrMask,
       "lesAtmAddrActual": lesAtmAddrActual,
       "lesElanName": lesElanName,
       "lesLanType": lesLanType,
       "lesLastChange": lesLastChange,
       "lesMaxFrameSize": lesMaxFrameSize,
       "lesControlTimeOut": lesControlTimeOut,
       "lesOperStatus": lesOperStatus,
       "lesAdminStatus": lesAdminStatus,
       "lesRowStatus": lesRowStatus,
       "lesVccTable": lesVccTable,
       "lesVccEntry": lesVccEntry,
       "lesVccAtmIfIndex": lesVccAtmIfIndex,
       "lesVccCtlDistVpi": lesVccCtlDistVpi,
       "lesVccCtlDistVci": lesVccCtlDistVci,
       "lesVccRowStatus": lesVccRowStatus,
       "lesBusTable": lesBusTable,
       "lesBusEntry": lesBusEntry,
       "lesBusConfIndex": lesBusConfIndex,
       "lesBusAddress": lesBusAddress,
       "lesLeArpMacTable": lesLeArpMacTable,
       "lesLeArpMacEntry": lesLeArpMacEntry,
       "lesLeArpMacAddr": lesLeArpMacAddr,
       "lesLeArpLecId": lesLeArpLecId,
       "lesLeArpAtmAddr": lesLeArpAtmAddr,
       "lesLeArpEntryType": lesLeArpEntryType,
       "lesLeArpRowStatus": lesLeArpRowStatus,
       "lesLeArpRdTable": lesLeArpRdTable,
       "lesLeArpRdEntry": lesLeArpRdEntry,
       "lesLeArpRdSegId": lesLeArpRdSegId,
       "lesLeArpRdBridgeNum": lesLeArpRdBridgeNum,
       "lesLeArpRdLecId": lesLeArpRdLecId,
       "lesLeArpRdAtmAddr": lesLeArpRdAtmAddr,
       "lesLeArpRdEntryType": lesLeArpRdEntryType,
       "lesLeArpRdRowStatus": lesLeArpRdRowStatus,
       "lesLecTableLastChange": lesLecTableLastChange,
       "lesLecTable": lesLecTable,
       "lesLecEntry": lesLecEntry,
       "lesLecIndex": lesLecIndex,
       "lesLecAtmAddr": lesLecAtmAddr,
       "lesLecProxy": lesLecProxy,
       "lesLecId": lesLecId,
       "lesLecAtmIfIndex": lesLecAtmIfIndex,
       "lesLecCtlDirectVpi": lesLecCtlDirectVpi,
       "lesLecCtlDirectVci": lesLecCtlDirectVci,
       "lesLecLastChange": lesLecLastChange,
       "lesLecState": lesLecState,
       "lesLecRowStatus": lesLecRowStatus,
       "lesStatGroup": lesStatGroup,
       "lesStatTable": lesStatTable,
       "lesStatEntry": lesStatEntry,
       "lesStatJoinOk": lesStatJoinOk,
       "lesStatVerNotSup": lesStatVerNotSup,
       "lesStatInvalidReqParam": lesStatInvalidReqParam,
       "lesStatDupLanDest": lesStatDupLanDest,
       "lesStatDupAtmAddr": lesStatDupAtmAddr,
       "lesStatInsRes": lesStatInsRes,
       "lesStatAccDenied": lesStatAccDenied,
       "lesStatInvalidReqId": lesStatInvalidReqId,
       "lesStatInvalidLanDest": lesStatInvalidLanDest,
       "lesStatInvalidAtmAddr": lesStatInvalidAtmAddr,
       "lesStatInBadPkts": lesStatInBadPkts,
       "lesStatOutRegFails": lesStatOutRegFails,
       "lesStatLeArpIn": lesStatLeArpIn,
       "lesStatLeArpFwd": lesStatLeArpFwd,
       "lesLecStatGroup": lesLecStatGroup,
       "lesLecStatTable": lesLecStatTable,
       "lesLecStatEntry": lesLecStatEntry,
       "lesLecRecvs": lesLecRecvs,
       "lesLecSends": lesLecSends,
       "lesLecInRegReq": lesLecInRegReq,
       "lesLecInUnReg": lesLecInUnReg,
       "lesLecInLeArpUcast": lesLecInLeArpUcast,
       "lesLecInLeArpBcast": lesLecInLeArpBcast,
       "lesLecInLeArpResp": lesLecInLeArpResp,
       "lesLecInNArp": lesLecInNArp,
       "lesFaultGroup": lesFaultGroup,
       "lesErrCtlTable": lesErrCtlTable,
       "lesErrCtlEntry": lesErrCtlEntry,
       "lesErrCtlAdminStatus": lesErrCtlAdminStatus,
       "lesErrCtlOperStatus": lesErrCtlOperStatus,
       "lesErrCtlClearLog": lesErrCtlClearLog,
       "lesErrCtlMaxEntries": lesErrCtlMaxEntries,
       "lesErrCtlLastEntry": lesErrCtlLastEntry,
       "lesErrLogTable": lesErrLogTable,
       "lesErrLogEntry": lesErrLogEntry,
       "lesErrLogIndex": lesErrLogIndex,
       "lesErrLogAtmAddr": lesErrLogAtmAddr,
       "lesErrLogErrCode": lesErrLogErrCode,
       "lesErrLogTime": lesErrLogTime}
)
