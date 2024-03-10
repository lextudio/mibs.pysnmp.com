"""SNMP MIB module (QB-VT15-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-VT15-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 05:35:11 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(AtmServiceCategory,
 atmNoClpNoScr,
 AtmTrafficDescrParamIndex,
 AtmVorXAdminStatus,
 AtmVorXLastChange,
 AtmAddr,
 AtmVorXOperStatus,
 AtmConnCastType,
 AtmVcIdentifier,
 AtmVpIdentifier,
 AtmConnKind) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory",
    "atmNoClpNoScr",
    "AtmTrafficDescrParamIndex",
    "AtmVorXAdminStatus",
    "AtmVorXLastChange",
    "AtmAddr",
    "AtmVorXOperStatus",
    "AtmConnCastType",
    "AtmVcIdentifier",
    "AtmVpIdentifier",
    "AtmConnKind")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(QbPvcConnKind,
 QbEnableStatus) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbPvcConnKind",
    "QbEnableStatus")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Unsigned32,
 Counter32,
 NotificationType,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ObjectIdentity,
 Bits,
 MibIdentifier,
 ModuleIdentity,
 TimeTicks,
 IpAddress,
 Gauge32,
 Counter64,
 Integer32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Unsigned32",
    "Counter32",
    "NotificationType",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ObjectIdentity",
    "Bits",
    "MibIdentifier",
    "ModuleIdentity",
    "TimeTicks",
    "IpAddress",
    "Gauge32",
    "Counter64",
    "Integer32",
    "iso")

(DisplayString,
 TruthValue,
 TextualConvention,
 RowStatus,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TruthValue",
    "TextualConvention",
    "RowStatus",
    "TimeStamp")


# MODULE-IDENTITY

qbVTVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QbVT15Sts1(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class QbVT15VTGroup(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )



class QbVT15VTGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class QbVT15VTId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )



class QbVC12Id(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )



# MIB Managed Objects in the order of their OIDs

_QbVTVCTables_ObjectIdentity = ObjectIdentity
qbVTVCTables = _QbVTVCTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1)
)
_QbVTVCConnTable_Object = MibTable
qbVTVCConnTable = _QbVTVCConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    qbVTVCConnTable.setStatus("current")
_QbVTVCConnEntry_Object = MibTableRow
qbVTVCConnEntry = _QbVTVCConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1)
)
qbVTVCConnEntry.setIndexNames(
    (0, "QB-VT15-MIB", "qbVTVCIfIndex"),
    (0, "QB-VT15-MIB", "qbVTVCConnId"),
)
if mibBuilder.loadTexts:
    qbVTVCConnEntry.setStatus("current")
_QbVTVCIfIndex_Type = InterfaceIndex
_QbVTVCIfIndex_Object = MibTableColumn
qbVTVCIfIndex = _QbVTVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 1),
    _QbVTVCIfIndex_Type()
)
qbVTVCIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCIfIndex.setStatus("current")


class _QbVTVCConnId_Type(Integer32):
    """Custom type qbVTVCConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_QbVTVCConnId_Type.__name__ = "Integer32"
_QbVTVCConnId_Object = MibTableColumn
qbVTVCConnId = _QbVTVCConnId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 2),
    _QbVTVCConnId_Type()
)
qbVTVCConnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCConnId.setStatus("current")
_QbVTVCConnIotAtmIfIndex_Type = InterfaceIndexOrZero
_QbVTVCConnIotAtmIfIndex_Object = MibTableColumn
qbVTVCConnIotAtmIfIndex = _QbVTVCConnIotAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 3),
    _QbVTVCConnIotAtmIfIndex_Type()
)
qbVTVCConnIotAtmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnIotAtmIfIndex.setStatus("current")


class _QbVTVCConnName_Type(DisplayString):
    """Custom type qbVTVCConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbVTVCConnName_Type.__name__ = "DisplayString"
_QbVTVCConnName_Object = MibTableColumn
qbVTVCConnName = _QbVTVCConnName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 4),
    _QbVTVCConnName_Type()
)
qbVTVCConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnName.setStatus("current")
_QbVTVCConnAdminStatus_Type = AtmVorXAdminStatus
_QbVTVCConnAdminStatus_Object = MibTableColumn
qbVTVCConnAdminStatus = _QbVTVCConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 5),
    _QbVTVCConnAdminStatus_Type()
)
qbVTVCConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnAdminStatus.setStatus("current")
_QbVTVCConnOperStatus_Type = AtmVorXOperStatus
_QbVTVCConnOperStatus_Object = MibTableColumn
qbVTVCConnOperStatus = _QbVTVCConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 6),
    _QbVTVCConnOperStatus_Type()
)
qbVTVCConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCConnOperStatus.setStatus("current")
_QbVTVCConnLastChange_Type = AtmVorXLastChange
_QbVTVCConnLastChange_Object = MibTableColumn
qbVTVCConnLastChange = _QbVTVCConnLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 7),
    _QbVTVCConnLastChange_Type()
)
qbVTVCConnLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCConnLastChange.setStatus("current")
_QbVTVCConnAtmVpi_Type = AtmVpIdentifier
_QbVTVCConnAtmVpi_Object = MibTableColumn
qbVTVCConnAtmVpi = _QbVTVCConnAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 8),
    _QbVTVCConnAtmVpi_Type()
)
qbVTVCConnAtmVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnAtmVpi.setStatus("current")
_QbVTVCConnAtmVci_Type = AtmVcIdentifier
_QbVTVCConnAtmVci_Object = MibTableColumn
qbVTVCConnAtmVci = _QbVTVCConnAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 9),
    _QbVTVCConnAtmVci_Type()
)
qbVTVCConnAtmVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnAtmVci.setStatus("current")


class _QbVTVCConnKind_Type(QbPvcConnKind):
    """Custom type qbVTVCConnKind based on QbPvcConnKind"""


_QbVTVCConnKind_Object = MibTableColumn
qbVTVCConnKind = _QbVTVCConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 10),
    _QbVTVCConnKind_Type()
)
qbVTVCConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnKind.setStatus("current")


class _QbVTVCCrossConnId_Type(Integer32):
    """Custom type qbVTVCCrossConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QbVTVCCrossConnId_Type.__name__ = "Integer32"
_QbVTVCCrossConnId_Object = MibTableColumn
qbVTVCCrossConnId = _QbVTVCCrossConnId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 11),
    _QbVTVCCrossConnId_Type()
)
qbVTVCCrossConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCCrossConnId.setStatus("current")
_QbVTVCConnRowStatus_Type = RowStatus
_QbVTVCConnRowStatus_Object = MibTableColumn
qbVTVCConnRowStatus = _QbVTVCConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 12),
    _QbVTVCConnRowStatus_Type()
)
qbVTVCConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnRowStatus.setStatus("current")


class _QbVTVCConnLoopback_Type(QbEnableStatus):
    """Custom type qbVTVCConnLoopback based on QbEnableStatus"""


_QbVTVCConnLoopback_Object = MibTableColumn
qbVTVCConnLoopback = _QbVTVCConnLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 13),
    _QbVTVCConnLoopback_Type()
)
qbVTVCConnLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnLoopback.setStatus("current")


class _QbVTVCConnLoopbackEndpt_Type(Integer32):
    """Custom type qbVTVCConnLoopbackEndpt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonVtLoopback", 2),
          ("vtLoopback", 1))
    )


_QbVTVCConnLoopbackEndpt_Type.__name__ = "Integer32"
_QbVTVCConnLoopbackEndpt_Object = MibTableColumn
qbVTVCConnLoopbackEndpt = _QbVTVCConnLoopbackEndpt_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 14),
    _QbVTVCConnLoopbackEndpt_Type()
)
qbVTVCConnLoopbackEndpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnLoopbackEndpt.setStatus("current")
_QbVTVCCrossConnTable_Object = MibTable
qbVTVCCrossConnTable = _QbVTVCCrossConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    qbVTVCCrossConnTable.setStatus("current")
_QbVTVCCrossConnEntry_Object = MibTableRow
qbVTVCCrossConnEntry = _QbVTVCCrossConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1)
)
qbVTVCCrossConnEntry.setIndexNames(
    (0, "QB-VT15-MIB", "qbVTVCCrossConnIfIndexEndpt1"),
    (0, "QB-VT15-MIB", "qbVTVCCrossConnVTIdEndpt1"),
    (0, "QB-VT15-MIB", "qbVTVCCrossConnIfIndexEndpt2"),
    (0, "QB-VT15-MIB", "qbVTVCCrossConnVTIdEndpt2"),
)
if mibBuilder.loadTexts:
    qbVTVCCrossConnEntry.setStatus("current")
_QbVTVCCrossConnIfIndexEndpt1_Type = InterfaceIndex
_QbVTVCCrossConnIfIndexEndpt1_Object = MibTableColumn
qbVTVCCrossConnIfIndexEndpt1 = _QbVTVCCrossConnIfIndexEndpt1_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 1),
    _QbVTVCCrossConnIfIndexEndpt1_Type()
)
qbVTVCCrossConnIfIndexEndpt1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIfIndexEndpt1.setStatus("current")


class _QbVTVCCrossConnVTIdEndpt1_Type(Integer32):
    """Custom type qbVTVCCrossConnVTIdEndpt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_QbVTVCCrossConnVTIdEndpt1_Type.__name__ = "Integer32"
_QbVTVCCrossConnVTIdEndpt1_Object = MibTableColumn
qbVTVCCrossConnVTIdEndpt1 = _QbVTVCCrossConnVTIdEndpt1_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 2),
    _QbVTVCCrossConnVTIdEndpt1_Type()
)
qbVTVCCrossConnVTIdEndpt1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCCrossConnVTIdEndpt1.setStatus("current")
_QbVTVCCrossConnIfIndexEndpt2_Type = InterfaceIndex
_QbVTVCCrossConnIfIndexEndpt2_Object = MibTableColumn
qbVTVCCrossConnIfIndexEndpt2 = _QbVTVCCrossConnIfIndexEndpt2_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 3),
    _QbVTVCCrossConnIfIndexEndpt2_Type()
)
qbVTVCCrossConnIfIndexEndpt2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIfIndexEndpt2.setStatus("current")


class _QbVTVCCrossConnVTIdEndpt2_Type(Integer32):
    """Custom type qbVTVCCrossConnVTIdEndpt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_QbVTVCCrossConnVTIdEndpt2_Type.__name__ = "Integer32"
_QbVTVCCrossConnVTIdEndpt2_Object = MibTableColumn
qbVTVCCrossConnVTIdEndpt2 = _QbVTVCCrossConnVTIdEndpt2_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 4),
    _QbVTVCCrossConnVTIdEndpt2_Type()
)
qbVTVCCrossConnVTIdEndpt2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCCrossConnVTIdEndpt2.setStatus("current")


class _QbVTVCCrossConnIndex_Type(Integer32):
    """Custom type qbVTVCCrossConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QbVTVCCrossConnIndex_Type.__name__ = "Integer32"
_QbVTVCCrossConnIndex_Object = MibTableColumn
qbVTVCCrossConnIndex = _QbVTVCCrossConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 5),
    _QbVTVCCrossConnIndex_Type()
)
qbVTVCCrossConnIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIndex.setStatus("current")


class _QbVTVCCrossConnName_Type(DisplayString):
    """Custom type qbVTVCCrossConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbVTVCCrossConnName_Type.__name__ = "DisplayString"
_QbVTVCCrossConnName_Object = MibTableColumn
qbVTVCCrossConnName = _QbVTVCCrossConnName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 6),
    _QbVTVCCrossConnName_Type()
)
qbVTVCCrossConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnName.setStatus("current")
_QbVTVCCrossConnAdminStatus_Type = AtmVorXAdminStatus
_QbVTVCCrossConnAdminStatus_Object = MibTableColumn
qbVTVCCrossConnAdminStatus = _QbVTVCCrossConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 7),
    _QbVTVCCrossConnAdminStatus_Type()
)
qbVTVCCrossConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnAdminStatus.setStatus("current")
_QbVTVCCrossConnOperStatus_Type = AtmVorXOperStatus
_QbVTVCCrossConnOperStatus_Object = MibTableColumn
qbVTVCCrossConnOperStatus = _QbVTVCCrossConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 8),
    _QbVTVCCrossConnOperStatus_Type()
)
qbVTVCCrossConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCCrossConnOperStatus.setStatus("current")


class _QbVTVCCrossConnKind_Type(QbPvcConnKind):
    """Custom type qbVTVCCrossConnKind based on QbPvcConnKind"""


_QbVTVCCrossConnKind_Object = MibTableColumn
qbVTVCCrossConnKind = _QbVTVCCrossConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 9),
    _QbVTVCCrossConnKind_Type()
)
qbVTVCCrossConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnKind.setStatus("current")
_QbVTVCCrossConnRowStatus_Type = RowStatus
_QbVTVCCrossConnRowStatus_Object = MibTableColumn
qbVTVCCrossConnRowStatus = _QbVTVCCrossConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 10),
    _QbVTVCCrossConnRowStatus_Type()
)
qbVTVCCrossConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnRowStatus.setStatus("current")
_QbVTConfTable_Object = MibTable
qbVTConfTable = _QbVTConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    qbVTConfTable.setStatus("current")
_QbVTConfEntry_Object = MibTableRow
qbVTConfEntry = _QbVTConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1)
)
qbVTConfEntry.setIndexNames(
    (0, "QB-VT15-MIB", "qbVTConfIfIndex"),
    (0, "QB-VT15-MIB", "qbVTConfVTId"),
)
if mibBuilder.loadTexts:
    qbVTConfEntry.setStatus("current")
_QbVTConfIfIndex_Type = InterfaceIndex
_QbVTConfIfIndex_Object = MibTableColumn
qbVTConfIfIndex = _QbVTConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1, 1),
    _QbVTConfIfIndex_Type()
)
qbVTConfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTConfIfIndex.setStatus("current")
_QbVTConfVTId_Type = QbVT15VTId
_QbVTConfVTId_Object = MibTableColumn
qbVTConfVTId = _QbVTConfVTId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1, 2),
    _QbVTConfVTId_Type()
)
qbVTConfVTId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTConfVTId.setStatus("current")


class _QbVTConfClockMode_Type(Integer32):
    """Custom type qbVTConfClockMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("srts", 1))
    )


_QbVTConfClockMode_Type.__name__ = "Integer32"
_QbVTConfClockMode_Object = MibTableColumn
qbVTConfClockMode = _QbVTConfClockMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1, 3),
    _QbVTConfClockMode_Type()
)
qbVTConfClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbVTConfClockMode.setStatus("current")


class _QbVTConfAction_Type(Integer32):
    """Custom type qbVTConfAction based on Integer32"""
    defaultValue = 1

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
        *(("ifVTAction", 3),
          ("noop", 4),
          ("singleVTAction", 1),
          ("stsVTAction", 2))
    )


_QbVTConfAction_Type.__name__ = "Integer32"
_QbVTConfAction_Object = MibTableColumn
qbVTConfAction = _QbVTConfAction_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1, 4),
    _QbVTConfAction_Type()
)
qbVTConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbVTConfAction.setStatus("current")
_QbVtVcStatsTable_Object = MibTable
qbVtVcStatsTable = _QbVtVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    qbVtVcStatsTable.setStatus("current")
_QbVtVcStatsEntry_Object = MibTableRow
qbVtVcStatsEntry = _QbVtVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1)
)
qbVtVcStatsEntry.setIndexNames(
    (0, "QB-VT15-MIB", "qbVtVcStatsIfIndex"),
    (0, "QB-VT15-MIB", "qbVtVcStatsConnId"),
)
if mibBuilder.loadTexts:
    qbVtVcStatsEntry.setStatus("current")
_QbVtVcStatsIfIndex_Type = InterfaceIndex
_QbVtVcStatsIfIndex_Object = MibTableColumn
qbVtVcStatsIfIndex = _QbVtVcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 1),
    _QbVtVcStatsIfIndex_Type()
)
qbVtVcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVtVcStatsIfIndex.setStatus("current")


class _QbVtVcStatsConnId_Type(Integer32):
    """Custom type qbVtVcStatsConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_QbVtVcStatsConnId_Type.__name__ = "Integer32"
_QbVtVcStatsConnId_Object = MibTableColumn
qbVtVcStatsConnId = _QbVtVcStatsConnId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 2),
    _QbVtVcStatsConnId_Type()
)
qbVtVcStatsConnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVtVcStatsConnId.setStatus("current")
_QbVtVcStatsRxCells_Type = Counter32
_QbVtVcStatsRxCells_Object = MibTableColumn
qbVtVcStatsRxCells = _QbVtVcStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 3),
    _QbVtVcStatsRxCells_Type()
)
qbVtVcStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsRxCells.setStatus("current")
_QbVtVcStatsTxCells_Type = Counter32
_QbVtVcStatsTxCells_Object = MibTableColumn
qbVtVcStatsTxCells = _QbVtVcStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 4),
    _QbVtVcStatsTxCells_Type()
)
qbVtVcStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsTxCells.setStatus("current")
_QbVtVcStatsRxDroppedCells_Type = Counter32
_QbVtVcStatsRxDroppedCells_Object = MibTableColumn
qbVtVcStatsRxDroppedCells = _QbVtVcStatsRxDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 5),
    _QbVtVcStatsRxDroppedCells_Type()
)
qbVtVcStatsRxDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsRxDroppedCells.setStatus("current")
_QbVtVcStatsTxConditionalCells_Type = Counter32
_QbVtVcStatsTxConditionalCells_Object = MibTableColumn
qbVtVcStatsTxConditionalCells = _QbVtVcStatsTxConditionalCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 6),
    _QbVtVcStatsTxConditionalCells_Type()
)
qbVtVcStatsTxConditionalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsTxConditionalCells.setStatus("current")
_QbVtVcStatsTxSuppressedCells_Type = Counter32
_QbVtVcStatsTxSuppressedCells_Object = MibTableColumn
qbVtVcStatsTxSuppressedCells = _QbVtVcStatsTxSuppressedCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 7),
    _QbVtVcStatsTxSuppressedCells_Type()
)
qbVtVcStatsTxSuppressedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsTxSuppressedCells.setStatus("current")
_QbVTVCNotifications_ObjectIdentity = ObjectIdentity
qbVTVCNotifications = _QbVTVCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 2)
)
_QbVTVCNotificationPrefix_ObjectIdentity = ObjectIdentity
qbVTVCNotificationPrefix = _QbVTVCNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 2, 0)
)
_QbVTVCConformance_ObjectIdentity = ObjectIdentity
qbVTVCConformance = _QbVTVCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 3)
)
_QbVTVCCompliances_ObjectIdentity = ObjectIdentity
qbVTVCCompliances = _QbVTVCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 3, 1)
)
_QbVTVCGroups_ObjectIdentity = ObjectIdentity
qbVTVCGroups = _QbVTVCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 3, 2)
)

# Managed Objects groups

qbVTVCConnInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 3, 2, 1)
)
qbVTVCConnInfo.setObjects(
      *(("QB-VT15-MIB", "qbVTVCConnIotAtmIfIndex"),
        ("QB-VT15-MIB", "qbVTVCConnName"),
        ("QB-VT15-MIB", "qbVTVCConnAdminStatus"),
        ("QB-VT15-MIB", "qbVTVCConnOperStatus"),
        ("QB-VT15-MIB", "qbVTVCConnAtmVpi"),
        ("QB-VT15-MIB", "qbVTVCConnAtmVci"),
        ("QB-VT15-MIB", "qbVTVCConnKind"),
        ("QB-VT15-MIB", "qbVTVCConnRowStatus"))
)
if mibBuilder.loadTexts:
    qbVTVCConnInfo.setStatus("current")

qbVTVCCrossConnInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 3, 2, 2)
)
qbVTVCCrossConnInfo.setObjects(
      *(("QB-VT15-MIB", "qbVTVCCrossConnName"),
        ("QB-VT15-MIB", "qbVTVCCrossConnAdminStatus"),
        ("QB-VT15-MIB", "qbVTVCCrossConnOperStatus"),
        ("QB-VT15-MIB", "qbVTVCCrossConnRowStatus"))
)
if mibBuilder.loadTexts:
    qbVTVCCrossConnInfo.setStatus("current")


# Notification objects

qbVTVCConnOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 2, 0, 1)
)
qbVTVCConnOperStatusChange.setObjects(
      *(("QB-VT15-MIB", "qbVTVCConnOperStatus"),
        ("QB-VT15-MIB", "qbVTVCConnKind"))
)
if mibBuilder.loadTexts:
    qbVTVCConnOperStatusChange.setStatus(
        "current"
    )

qbVTVCCrossConnOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 2, 0, 2)
)
qbVTVCCrossConnOperStatusChange.setObjects(
      *(("QB-VT15-MIB", "qbVTVCCrossConnOperStatus"),
        ("QB-VT15-MIB", "qbVTVCCrossConnKind"))
)
if mibBuilder.loadTexts:
    qbVTVCCrossConnOperStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qbVTVCCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbVTVCCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-VT15-MIB",
    **{"QbVT15Sts1": QbVT15Sts1,
       "QbVT15VTGroup": QbVT15VTGroup,
       "QbVT15VTGroupId": QbVT15VTGroupId,
       "QbVT15VTId": QbVT15VTId,
       "QbVC12Id": QbVC12Id,
       "qbVTVCMIB": qbVTVCMIB,
       "qbVTVCTables": qbVTVCTables,
       "qbVTVCConnTable": qbVTVCConnTable,
       "qbVTVCConnEntry": qbVTVCConnEntry,
       "qbVTVCIfIndex": qbVTVCIfIndex,
       "qbVTVCConnId": qbVTVCConnId,
       "qbVTVCConnIotAtmIfIndex": qbVTVCConnIotAtmIfIndex,
       "qbVTVCConnName": qbVTVCConnName,
       "qbVTVCConnAdminStatus": qbVTVCConnAdminStatus,
       "qbVTVCConnOperStatus": qbVTVCConnOperStatus,
       "qbVTVCConnLastChange": qbVTVCConnLastChange,
       "qbVTVCConnAtmVpi": qbVTVCConnAtmVpi,
       "qbVTVCConnAtmVci": qbVTVCConnAtmVci,
       "qbVTVCConnKind": qbVTVCConnKind,
       "qbVTVCCrossConnId": qbVTVCCrossConnId,
       "qbVTVCConnRowStatus": qbVTVCConnRowStatus,
       "qbVTVCConnLoopback": qbVTVCConnLoopback,
       "qbVTVCConnLoopbackEndpt": qbVTVCConnLoopbackEndpt,
       "qbVTVCCrossConnTable": qbVTVCCrossConnTable,
       "qbVTVCCrossConnEntry": qbVTVCCrossConnEntry,
       "qbVTVCCrossConnIfIndexEndpt1": qbVTVCCrossConnIfIndexEndpt1,
       "qbVTVCCrossConnVTIdEndpt1": qbVTVCCrossConnVTIdEndpt1,
       "qbVTVCCrossConnIfIndexEndpt2": qbVTVCCrossConnIfIndexEndpt2,
       "qbVTVCCrossConnVTIdEndpt2": qbVTVCCrossConnVTIdEndpt2,
       "qbVTVCCrossConnIndex": qbVTVCCrossConnIndex,
       "qbVTVCCrossConnName": qbVTVCCrossConnName,
       "qbVTVCCrossConnAdminStatus": qbVTVCCrossConnAdminStatus,
       "qbVTVCCrossConnOperStatus": qbVTVCCrossConnOperStatus,
       "qbVTVCCrossConnKind": qbVTVCCrossConnKind,
       "qbVTVCCrossConnRowStatus": qbVTVCCrossConnRowStatus,
       "qbVTConfTable": qbVTConfTable,
       "qbVTConfEntry": qbVTConfEntry,
       "qbVTConfIfIndex": qbVTConfIfIndex,
       "qbVTConfVTId": qbVTConfVTId,
       "qbVTConfClockMode": qbVTConfClockMode,
       "qbVTConfAction": qbVTConfAction,
       "qbVtVcStatsTable": qbVtVcStatsTable,
       "qbVtVcStatsEntry": qbVtVcStatsEntry,
       "qbVtVcStatsIfIndex": qbVtVcStatsIfIndex,
       "qbVtVcStatsConnId": qbVtVcStatsConnId,
       "qbVtVcStatsRxCells": qbVtVcStatsRxCells,
       "qbVtVcStatsTxCells": qbVtVcStatsTxCells,
       "qbVtVcStatsRxDroppedCells": qbVtVcStatsRxDroppedCells,
       "qbVtVcStatsTxConditionalCells": qbVtVcStatsTxConditionalCells,
       "qbVtVcStatsTxSuppressedCells": qbVtVcStatsTxSuppressedCells,
       "qbVTVCNotifications": qbVTVCNotifications,
       "qbVTVCNotificationPrefix": qbVTVCNotificationPrefix,
       "qbVTVCConnOperStatusChange": qbVTVCConnOperStatusChange,
       "qbVTVCCrossConnOperStatusChange": qbVTVCCrossConnOperStatusChange,
       "qbVTVCConformance": qbVTVCConformance,
       "qbVTVCCompliances": qbVTVCCompliances,
       "qbVTVCCompliance": qbVTVCCompliance,
       "qbVTVCGroups": qbVTVCGroups,
       "qbVTVCConnInfo": qbVTVCConnInfo,
       "qbVTVCCrossConnInfo": qbVTVCCrossConnInfo}
)
