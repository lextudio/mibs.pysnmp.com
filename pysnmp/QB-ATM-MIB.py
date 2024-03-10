"""SNMP MIB module (QB-ATM-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-ATM-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 05:35:09 2024
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

(atmVpCrossConnectEntry,
 atmInterfaceConfEntry,
 atmVclEntry,
 atmVplEntry,
 atmVcCrossConnectEntry,
 atmTrafficDescrParamEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVpCrossConnectEntry",
    "atmInterfaceConfEntry",
    "atmVclEntry",
    "atmVplEntry",
    "atmVcCrossConnectEntry",
    "atmTrafficDescrParamEntry")

(AtmTrafficDescrParamIndex,
 AtmConnKind,
 AtmVpIdentifier,
 AtmVorXLastChange,
 AtmVorXOperStatus,
 AtmConnCastType,
 atmNoClpNoScr,
 AtmAddr,
 AtmVcIdentifier,
 AtmVorXAdminStatus,
 AtmServiceCategory) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmTrafficDescrParamIndex",
    "AtmConnKind",
    "AtmVpIdentifier",
    "AtmVorXLastChange",
    "AtmVorXOperStatus",
    "AtmConnCastType",
    "atmNoClpNoScr",
    "AtmAddr",
    "AtmVcIdentifier",
    "AtmVorXAdminStatus",
    "AtmServiceCategory")

(InterfaceIndexOrZero,
 InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "InterfaceIndex",
    "ifIndex")

(QbEnableStatus,
 QbPvcConnKind) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbEnableStatus",
    "QbPvcConnKind")

(TimeStamp,) = mibBuilder.importSymbols(
    "QBSYS-SYSTEM-MIB",
    "TimeStamp")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ObjectGroup,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "ModuleCompliance",
    "NotificationGroup")

(MibIdentifier,
 NotificationType,
 Counter32,
 Bits,
 ModuleIdentity,
 Counter64,
 IpAddress,
 iso,
 ObjectIdentity,
 TimeTicks,
 Gauge32,
 Integer32,
 Unsigned32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "MibIdentifier",
    "NotificationType",
    "Counter32",
    "Bits",
    "ModuleIdentity",
    "Counter64",
    "IpAddress",
    "iso",
    "ObjectIdentity",
    "TimeTicks",
    "Gauge32",
    "Integer32",
    "Unsigned32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

(RowStatus,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "RowStatus",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qbAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7)
)


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
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




# TEXTUAL-CONVENTIONS



class QbAtmPnniWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )



class QbAtmPnniNodeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )



class QbAtmSigSpec(TextualConvention, Integer32):
    status = "current"
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
        *(("aini", 8),
          ("iisp30", 6),
          ("iisp31", 7),
          ("other", 1),
          ("pnni", 5),
          ("uni30", 2),
          ("uni31", 3),
          ("uni40", 4))
    )



class QbAtmPnniHelloState(TextualConvention, Integer32):
    status = "current"
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
        *(("attempt", 3),
          ("commonOutside", 8),
          ("down", 2),
          ("notApplicable", 1),
          ("oneWayInside", 4),
          ("oneWayOutside", 6),
          ("twoWayInside", 5),
          ("twoWayOutside", 7))
    )



class QbAtmPnniAtmAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )



class QbAtmPnniNodeIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class QbAtmPnniPeerGroupId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )



class QbF4F5LoopbackStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-progress", 1),
          ("success", 2),
          ("timeout", 3))
    )



class QbF4F5Status(TextualConvention, Bits):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_QbAtmObjects_ObjectIdentity = ObjectIdentity
qbAtmObjects = _QbAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1)
)
_QbAtmInterfaceConfTable_Object = MibTable
qbAtmInterfaceConfTable = _QbAtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    qbAtmInterfaceConfTable.setStatus("current")
_QbAtmInterfaceConfEntry_Object = MibTableRow
qbAtmInterfaceConfEntry = _QbAtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1)
)
atmInterfaceConfEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmInterfaceConfEntry")
)
qbAtmInterfaceConfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmInterfaceConfEntry.setStatus("current")


class _QbAtmInterfaceConfPolicingStatus_Type(Integer32):
    """Custom type qbAtmInterfaceConfPolicingStatus based on Integer32"""
    defaultValue = 2

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


_QbAtmInterfaceConfPolicingStatus_Type.__name__ = "Integer32"
_QbAtmInterfaceConfPolicingStatus_Object = MibTableColumn
qbAtmInterfaceConfPolicingStatus = _QbAtmInterfaceConfPolicingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 1),
    _QbAtmInterfaceConfPolicingStatus_Type()
)
qbAtmInterfaceConfPolicingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfPolicingStatus.setStatus("current")
_QbAtmInterfaceConfMaxPvcVpi_Type = Integer32
_QbAtmInterfaceConfMaxPvcVpi_Object = MibTableColumn
qbAtmInterfaceConfMaxPvcVpi = _QbAtmInterfaceConfMaxPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 2),
    _QbAtmInterfaceConfMaxPvcVpi_Type()
)
qbAtmInterfaceConfMaxPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvcVpi.setStatus("current")
_QbAtmInterfaceConfMinPvcVpi_Type = Integer32
_QbAtmInterfaceConfMinPvcVpi_Object = MibTableColumn
qbAtmInterfaceConfMinPvcVpi = _QbAtmInterfaceConfMinPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 3),
    _QbAtmInterfaceConfMinPvcVpi_Type()
)
qbAtmInterfaceConfMinPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvcVpi.setStatus("current")
_QbAtmInterfaceConfMaxPvcVci_Type = Integer32
_QbAtmInterfaceConfMaxPvcVci_Object = MibTableColumn
qbAtmInterfaceConfMaxPvcVci = _QbAtmInterfaceConfMaxPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 4),
    _QbAtmInterfaceConfMaxPvcVci_Type()
)
qbAtmInterfaceConfMaxPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvcVci.setStatus("current")
_QbAtmInterfaceConfMinPvcVci_Type = Integer32
_QbAtmInterfaceConfMinPvcVci_Object = MibTableColumn
qbAtmInterfaceConfMinPvcVci = _QbAtmInterfaceConfMinPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 5),
    _QbAtmInterfaceConfMinPvcVci_Type()
)
qbAtmInterfaceConfMinPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvcVci.setStatus("current")
_QbAtmInterfaceConfMaxPvpVpi_Type = Integer32
_QbAtmInterfaceConfMaxPvpVpi_Object = MibTableColumn
qbAtmInterfaceConfMaxPvpVpi = _QbAtmInterfaceConfMaxPvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 6),
    _QbAtmInterfaceConfMaxPvpVpi_Type()
)
qbAtmInterfaceConfMaxPvpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvpVpi.setStatus("current")
_QbAtmInterfaceConfMinPvpVpi_Type = Integer32
_QbAtmInterfaceConfMinPvpVpi_Object = MibTableColumn
qbAtmInterfaceConfMinPvpVpi = _QbAtmInterfaceConfMinPvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 7),
    _QbAtmInterfaceConfMinPvpVpi_Type()
)
qbAtmInterfaceConfMinPvpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvpVpi.setStatus("current")
_QbAtmTrafficDescrParamTable_Object = MibTable
qbAtmTrafficDescrParamTable = _QbAtmTrafficDescrParamTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamTable.setStatus("current")
_QbAtmTrafficDescrParamEntry_Object = MibTableRow
qbAtmTrafficDescrParamEntry = _QbAtmTrafficDescrParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 2, 1)
)
atmTrafficDescrParamEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmTrafficDescrParamEntry")
)
qbAtmTrafficDescrParamEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamEntry.setStatus("current")


class _QbAtmTrafficDescrParamName_Type(DisplayString):
    """Custom type qbAtmTrafficDescrParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbAtmTrafficDescrParamName_Type.__name__ = "DisplayString"
_QbAtmTrafficDescrParamName_Object = MibTableColumn
qbAtmTrafficDescrParamName = _QbAtmTrafficDescrParamName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 2, 1, 1),
    _QbAtmTrafficDescrParamName_Type()
)
qbAtmTrafficDescrParamName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamName.setStatus("current")


class _QbAtmTrafficDescrParamDefault_Type(Boolean):
    """Custom type qbAtmTrafficDescrParamDefault based on Boolean"""


_QbAtmTrafficDescrParamDefault_Object = MibTableColumn
qbAtmTrafficDescrParamDefault = _QbAtmTrafficDescrParamDefault_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 2, 1, 2),
    _QbAtmTrafficDescrParamDefault_Type()
)
qbAtmTrafficDescrParamDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamDefault.setStatus("current")
_QbAtmVclTable_Object = MibTable
qbAtmVclTable = _QbAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    qbAtmVclTable.setStatus("current")
_QbAtmVclEntry_Object = MibTableRow
qbAtmVclEntry = _QbAtmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1)
)
atmVclEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmVclEntry")
)
qbAtmVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmVclEntry.setStatus("current")


class _QbAtmVclLoopback_Type(QbEnableStatus):
    """Custom type qbAtmVclLoopback based on QbEnableStatus"""


_QbAtmVclLoopback_Object = MibTableColumn
qbAtmVclLoopback = _QbAtmVclLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 1),
    _QbAtmVclLoopback_Type()
)
qbAtmVclLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclLoopback.setStatus("current")


class _QbAtmVclF4F5LoopbackInsert_Type(OctetString):
    """Custom type qbAtmVclF4F5LoopbackInsert based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_QbAtmVclF4F5LoopbackInsert_Type.__name__ = "OctetString"
_QbAtmVclF4F5LoopbackInsert_Object = MibTableColumn
qbAtmVclF4F5LoopbackInsert = _QbAtmVclF4F5LoopbackInsert_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 2),
    _QbAtmVclF4F5LoopbackInsert_Type()
)
qbAtmVclF4F5LoopbackInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackInsert.setStatus("current")
_QbAtmVclF4F5LoopbackStatus_Type = QbF4F5LoopbackStatus
_QbAtmVclF4F5LoopbackStatus_Object = MibTableColumn
qbAtmVclF4F5LoopbackStatus = _QbAtmVclF4F5LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 3),
    _QbAtmVclF4F5LoopbackStatus_Type()
)
qbAtmVclF4F5LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackStatus.setStatus("current")
_QbAtmVclF4F5LoopbackTimestamp_Type = TimeStamp
_QbAtmVclF4F5LoopbackTimestamp_Object = MibTableColumn
qbAtmVclF4F5LoopbackTimestamp = _QbAtmVclF4F5LoopbackTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 4),
    _QbAtmVclF4F5LoopbackTimestamp_Type()
)
qbAtmVclF4F5LoopbackTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackTimestamp.setStatus("current")
_QbAtmVclMgmtIpAddr_Type = IpAddress
_QbAtmVclMgmtIpAddr_Object = MibTableColumn
qbAtmVclMgmtIpAddr = _QbAtmVclMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 5),
    _QbAtmVclMgmtIpAddr_Type()
)
qbAtmVclMgmtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclMgmtIpAddr.setStatus("current")
_QbAtmVclMgmtIpMask_Type = IpAddress
_QbAtmVclMgmtIpMask_Object = MibTableColumn
qbAtmVclMgmtIpMask = _QbAtmVclMgmtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 6),
    _QbAtmVclMgmtIpMask_Type()
)
qbAtmVclMgmtIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclMgmtIpMask.setStatus("current")
_QbAtmVclMgmtNeighborIP_Type = IpAddress
_QbAtmVclMgmtNeighborIP_Object = MibTableColumn
qbAtmVclMgmtNeighborIP = _QbAtmVclMgmtNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 7),
    _QbAtmVclMgmtNeighborIP_Type()
)
qbAtmVclMgmtNeighborIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclMgmtNeighborIP.setStatus("current")
_QbAtmVclConnKind_Type = QbPvcConnKind
_QbAtmVclConnKind_Object = MibTableColumn
qbAtmVclConnKind = _QbAtmVclConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 8),
    _QbAtmVclConnKind_Type()
)
qbAtmVclConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclConnKind.setStatus("current")
_QbAtmVclF4F5TxStatus_Type = QbF4F5Status
_QbAtmVclF4F5TxStatus_Object = MibTableColumn
qbAtmVclF4F5TxStatus = _QbAtmVclF4F5TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 9),
    _QbAtmVclF4F5TxStatus_Type()
)
qbAtmVclF4F5TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5TxStatus.setStatus("current")
_QbAtmVclF4F5TxLastChange_Type = TimeStamp
_QbAtmVclF4F5TxLastChange_Object = MibTableColumn
qbAtmVclF4F5TxLastChange = _QbAtmVclF4F5TxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 10),
    _QbAtmVclF4F5TxLastChange_Type()
)
qbAtmVclF4F5TxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5TxLastChange.setStatus("current")
_QbAtmVclF4F5RxStatus_Type = QbF4F5Status
_QbAtmVclF4F5RxStatus_Object = MibTableColumn
qbAtmVclF4F5RxStatus = _QbAtmVclF4F5RxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 11),
    _QbAtmVclF4F5RxStatus_Type()
)
qbAtmVclF4F5RxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5RxStatus.setStatus("current")
_QbAtmVclF4F5RxLastChange_Type = TimeStamp
_QbAtmVclF4F5RxLastChange_Object = MibTableColumn
qbAtmVclF4F5RxLastChange = _QbAtmVclF4F5RxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 12),
    _QbAtmVclF4F5RxLastChange_Type()
)
qbAtmVclF4F5RxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5RxLastChange.setStatus("current")
_QbAtmVplTable_Object = MibTable
qbAtmVplTable = _QbAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    qbAtmVplTable.setStatus("current")
_QbAtmVplEntry_Object = MibTableRow
qbAtmVplEntry = _QbAtmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1)
)
atmVplEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmVplEntry")
)
qbAtmVplEntry.setIndexNames(*atmVplEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmVplEntry.setStatus("current")


class _QbAtmVplLoopback_Type(QbEnableStatus):
    """Custom type qbAtmVplLoopback based on QbEnableStatus"""


_QbAtmVplLoopback_Object = MibTableColumn
qbAtmVplLoopback = _QbAtmVplLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 1),
    _QbAtmVplLoopback_Type()
)
qbAtmVplLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVplLoopback.setStatus("current")


class _QbAtmVplF4F5LoopbackInsert_Type(OctetString):
    """Custom type qbAtmVplF4F5LoopbackInsert based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_QbAtmVplF4F5LoopbackInsert_Type.__name__ = "OctetString"
_QbAtmVplF4F5LoopbackInsert_Object = MibTableColumn
qbAtmVplF4F5LoopbackInsert = _QbAtmVplF4F5LoopbackInsert_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 2),
    _QbAtmVplF4F5LoopbackInsert_Type()
)
qbAtmVplF4F5LoopbackInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackInsert.setStatus("current")
_QbAtmVplF4F5LoopbackStatus_Type = QbF4F5LoopbackStatus
_QbAtmVplF4F5LoopbackStatus_Object = MibTableColumn
qbAtmVplF4F5LoopbackStatus = _QbAtmVplF4F5LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 3),
    _QbAtmVplF4F5LoopbackStatus_Type()
)
qbAtmVplF4F5LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackStatus.setStatus("current")
_QbAtmVplF4F5LoopbackTimestamp_Type = TimeStamp
_QbAtmVplF4F5LoopbackTimestamp_Object = MibTableColumn
qbAtmVplF4F5LoopbackTimestamp = _QbAtmVplF4F5LoopbackTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 4),
    _QbAtmVplF4F5LoopbackTimestamp_Type()
)
qbAtmVplF4F5LoopbackTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackTimestamp.setStatus("current")
_QbAtmVplF4F5TxStatus_Type = QbF4F5Status
_QbAtmVplF4F5TxStatus_Object = MibTableColumn
qbAtmVplF4F5TxStatus = _QbAtmVplF4F5TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 5),
    _QbAtmVplF4F5TxStatus_Type()
)
qbAtmVplF4F5TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5TxStatus.setStatus("current")
_QbAtmVplF4F5TxLastChange_Type = TimeStamp
_QbAtmVplF4F5TxLastChange_Object = MibTableColumn
qbAtmVplF4F5TxLastChange = _QbAtmVplF4F5TxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 6),
    _QbAtmVplF4F5TxLastChange_Type()
)
qbAtmVplF4F5TxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5TxLastChange.setStatus("current")
_QbAtmVplF4F5RxStatus_Type = QbF4F5Status
_QbAtmVplF4F5RxStatus_Object = MibTableColumn
qbAtmVplF4F5RxStatus = _QbAtmVplF4F5RxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 7),
    _QbAtmVplF4F5RxStatus_Type()
)
qbAtmVplF4F5RxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5RxStatus.setStatus("current")
_QbAtmVplF4F5RxLastChange_Type = TimeStamp
_QbAtmVplF4F5RxLastChange_Object = MibTableColumn
qbAtmVplF4F5RxLastChange = _QbAtmVplF4F5RxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 8),
    _QbAtmVplF4F5RxLastChange_Type()
)
qbAtmVplF4F5RxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5RxLastChange.setStatus("current")
_QbAtmVcCrossConnectTable_Object = MibTable
qbAtmVcCrossConnectTable = _QbAtmVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5)
)
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectTable.setStatus("current")
_QbAtmVcCrossConnectEntry_Object = MibTableRow
qbAtmVcCrossConnectEntry = _QbAtmVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5, 1)
)
atmVcCrossConnectEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmVcCrossConnectEntry")
)
qbAtmVcCrossConnectEntry.setIndexNames(*atmVcCrossConnectEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectEntry.setStatus("current")


class _QbAtmVcCrossConnectName_Type(DisplayString):
    """Custom type qbAtmVcCrossConnectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbAtmVcCrossConnectName_Type.__name__ = "DisplayString"
_QbAtmVcCrossConnectName_Object = MibTableColumn
qbAtmVcCrossConnectName = _QbAtmVcCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5, 1, 1),
    _QbAtmVcCrossConnectName_Type()
)
qbAtmVcCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectName.setStatus("current")
_QbAtmVcCrossConnectRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVcCrossConnectRxTrafficDescrIndex_Object = MibTableColumn
qbAtmVcCrossConnectRxTrafficDescrIndex = _QbAtmVcCrossConnectRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5, 1, 2),
    _QbAtmVcCrossConnectRxTrafficDescrIndex_Type()
)
qbAtmVcCrossConnectRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectRxTrafficDescrIndex.setStatus("current")
_QbAtmVcCrossConnectTxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVcCrossConnectTxTrafficDescrIndex_Object = MibTableColumn
qbAtmVcCrossConnectTxTrafficDescrIndex = _QbAtmVcCrossConnectTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5, 1, 3),
    _QbAtmVcCrossConnectTxTrafficDescrIndex_Type()
)
qbAtmVcCrossConnectTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectTxTrafficDescrIndex.setStatus("current")
_QbAtmVpCrossConnectTable_Object = MibTable
qbAtmVpCrossConnectTable = _QbAtmVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectTable.setStatus("current")
_QbAtmVpCrossConnectEntry_Object = MibTableRow
qbAtmVpCrossConnectEntry = _QbAtmVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6, 1)
)
atmVpCrossConnectEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmVpCrossConnectEntry")
)
qbAtmVpCrossConnectEntry.setIndexNames(*atmVpCrossConnectEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectEntry.setStatus("current")


class _QbAtmVpCrossConnectName_Type(DisplayString):
    """Custom type qbAtmVpCrossConnectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbAtmVpCrossConnectName_Type.__name__ = "DisplayString"
_QbAtmVpCrossConnectName_Object = MibTableColumn
qbAtmVpCrossConnectName = _QbAtmVpCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6, 1, 1),
    _QbAtmVpCrossConnectName_Type()
)
qbAtmVpCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectName.setStatus("current")
_QbAtmVpCrossConnectRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVpCrossConnectRxTrafficDescrIndex_Object = MibTableColumn
qbAtmVpCrossConnectRxTrafficDescrIndex = _QbAtmVpCrossConnectRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6, 1, 2),
    _QbAtmVpCrossConnectRxTrafficDescrIndex_Type()
)
qbAtmVpCrossConnectRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectRxTrafficDescrIndex.setStatus("current")
_QbAtmVpCrossConnectTxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVpCrossConnectTxTrafficDescrIndex_Object = MibTableColumn
qbAtmVpCrossConnectTxTrafficDescrIndex = _QbAtmVpCrossConnectTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6, 1, 3),
    _QbAtmVpCrossConnectTxTrafficDescrIndex_Type()
)
qbAtmVpCrossConnectTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectTxTrafficDescrIndex.setStatus("current")
_QbAtmSigGroup_ObjectIdentity = ObjectIdentity
qbAtmSigGroup = _QbAtmSigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7)
)
_QbAtmPnniNodeTable_Object = MibTable
qbAtmPnniNodeTable = _QbAtmPnniNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    qbAtmPnniNodeTable.setStatus("current")
_QbAtmPnniNodeEntry_Object = MibTableRow
qbAtmPnniNodeEntry = _QbAtmPnniNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1)
)
qbAtmPnniNodeEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmPnniNodeIndex"),
)
if mibBuilder.loadTexts:
    qbAtmPnniNodeEntry.setStatus("current")


class _QbAtmPnniNodeIndex_Type(Integer32):
    """Custom type qbAtmPnniNodeIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QbAtmPnniNodeIndex_Type.__name__ = "Integer32"
_QbAtmPnniNodeIndex_Object = MibTableColumn
qbAtmPnniNodeIndex = _QbAtmPnniNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 1),
    _QbAtmPnniNodeIndex_Type()
)
qbAtmPnniNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniNodeIndex.setStatus("current")


class _QbAtmPnniNodeNetAddrPrefix_Type(OctetString):
    """Custom type qbAtmPnniNodeNetAddrPrefix based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_QbAtmPnniNodeNetAddrPrefix_Type.__name__ = "OctetString"
_QbAtmPnniNodeNetAddrPrefix_Object = MibTableColumn
qbAtmPnniNodeNetAddrPrefix = _QbAtmPnniNodeNetAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 2),
    _QbAtmPnniNodeNetAddrPrefix_Type()
)
qbAtmPnniNodeNetAddrPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeNetAddrPrefix.setStatus("current")


class _QbAtmPnniNodeEndSysId_Type(OctetString):
    """Custom type qbAtmPnniNodeEndSysId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_QbAtmPnniNodeEndSysId_Type.__name__ = "OctetString"
_QbAtmPnniNodeEndSysId_Object = MibTableColumn
qbAtmPnniNodeEndSysId = _QbAtmPnniNodeEndSysId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 3),
    _QbAtmPnniNodeEndSysId_Type()
)
qbAtmPnniNodeEndSysId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeEndSysId.setStatus("current")


class _QbAtmPnniNodeLevel_Type(Integer32):
    """Custom type qbAtmPnniNodeLevel based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104),
    )


_QbAtmPnniNodeLevel_Type.__name__ = "Integer32"
_QbAtmPnniNodeLevel_Object = MibTableColumn
qbAtmPnniNodeLevel = _QbAtmPnniNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 4),
    _QbAtmPnniNodeLevel_Type()
)
qbAtmPnniNodeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeLevel.setStatus("current")
_QbAtmPnniNodeRowStatus_Type = RowStatus
_QbAtmPnniNodeRowStatus_Object = MibTableColumn
qbAtmPnniNodeRowStatus = _QbAtmPnniNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 5),
    _QbAtmPnniNodeRowStatus_Type()
)
qbAtmPnniNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeRowStatus.setStatus("current")


class _QbAtmPnniNodeOperStatus_Type(Integer32):
    """Custom type qbAtmPnniNodeOperStatus based on Integer32"""
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


_QbAtmPnniNodeOperStatus_Type.__name__ = "Integer32"
_QbAtmPnniNodeOperStatus_Object = MibTableColumn
qbAtmPnniNodeOperStatus = _QbAtmPnniNodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 6),
    _QbAtmPnniNodeOperStatus_Type()
)
qbAtmPnniNodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodeOperStatus.setStatus("current")
_QbAtmPnniNodeAtmAddress_Type = QbAtmPnniAtmAddr
_QbAtmPnniNodeAtmAddress_Object = MibTableColumn
qbAtmPnniNodeAtmAddress = _QbAtmPnniNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 7),
    _QbAtmPnniNodeAtmAddress_Type()
)
qbAtmPnniNodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAtmAddress.setStatus("current")
_QbAtmPnniNodePeerGroupId_Type = QbAtmPnniPeerGroupId
_QbAtmPnniNodePeerGroupId_Object = MibTableColumn
qbAtmPnniNodePeerGroupId = _QbAtmPnniNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 8),
    _QbAtmPnniNodePeerGroupId_Type()
)
qbAtmPnniNodePeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupId.setStatus("current")
_QbAtmPnniIfTable_Object = MibTable
qbAtmPnniIfTable = _QbAtmPnniIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2)
)
if mibBuilder.loadTexts:
    qbAtmPnniIfTable.setStatus("current")
_QbAtmPnniIfEntry_Object = MibTableRow
qbAtmPnniIfEntry = _QbAtmPnniIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1)
)
qbAtmPnniIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbAtmPnniIfEntry.setStatus("current")


class _QbAtmPnniIfNodeIndex_Type(Integer32):
    """Custom type qbAtmPnniIfNodeIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_QbAtmPnniIfNodeIndex_Type.__name__ = "Integer32"
_QbAtmPnniIfNodeIndex_Object = MibTableColumn
qbAtmPnniIfNodeIndex = _QbAtmPnniIfNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 1),
    _QbAtmPnniIfNodeIndex_Type()
)
qbAtmPnniIfNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfNodeIndex.setStatus("current")


class _QbAtmPnniIfAdmWeightCbr_Type(QbAtmPnniWeight):
    """Custom type qbAtmPnniIfAdmWeightCbr based on QbAtmPnniWeight"""
    defaultValue = 5040


_QbAtmPnniIfAdmWeightCbr_Object = MibTableColumn
qbAtmPnniIfAdmWeightCbr = _QbAtmPnniIfAdmWeightCbr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 2),
    _QbAtmPnniIfAdmWeightCbr_Type()
)
qbAtmPnniIfAdmWeightCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightCbr.setStatus("current")


class _QbAtmPnniIfAdmWeightRtVbr_Type(QbAtmPnniWeight):
    """Custom type qbAtmPnniIfAdmWeightRtVbr based on QbAtmPnniWeight"""
    defaultValue = 5040


_QbAtmPnniIfAdmWeightRtVbr_Object = MibTableColumn
qbAtmPnniIfAdmWeightRtVbr = _QbAtmPnniIfAdmWeightRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 3),
    _QbAtmPnniIfAdmWeightRtVbr_Type()
)
qbAtmPnniIfAdmWeightRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightRtVbr.setStatus("current")


class _QbAtmPnniIfAdmWeightNrtVbr_Type(QbAtmPnniWeight):
    """Custom type qbAtmPnniIfAdmWeightNrtVbr based on QbAtmPnniWeight"""
    defaultValue = 5040


_QbAtmPnniIfAdmWeightNrtVbr_Object = MibTableColumn
qbAtmPnniIfAdmWeightNrtVbr = _QbAtmPnniIfAdmWeightNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 4),
    _QbAtmPnniIfAdmWeightNrtVbr_Type()
)
qbAtmPnniIfAdmWeightNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightNrtVbr.setStatus("current")


class _QbAtmPnniIfAdmWeightAbr_Type(QbAtmPnniWeight):
    """Custom type qbAtmPnniIfAdmWeightAbr based on QbAtmPnniWeight"""
    defaultValue = 5040


_QbAtmPnniIfAdmWeightAbr_Object = MibTableColumn
qbAtmPnniIfAdmWeightAbr = _QbAtmPnniIfAdmWeightAbr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 5),
    _QbAtmPnniIfAdmWeightAbr_Type()
)
qbAtmPnniIfAdmWeightAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightAbr.setStatus("current")


class _QbAtmPnniIfAdmWeightUbr_Type(QbAtmPnniWeight):
    """Custom type qbAtmPnniIfAdmWeightUbr based on QbAtmPnniWeight"""
    defaultValue = 5040


_QbAtmPnniIfAdmWeightUbr_Object = MibTableColumn
qbAtmPnniIfAdmWeightUbr = _QbAtmPnniIfAdmWeightUbr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 6),
    _QbAtmPnniIfAdmWeightUbr_Type()
)
qbAtmPnniIfAdmWeightUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightUbr.setStatus("current")


class _QbAtmPnniIfRccServiceCategory_Type(AtmServiceCategory):
    """Custom type qbAtmPnniIfRccServiceCategory based on AtmServiceCategory"""
    defaultValue = 4


_QbAtmPnniIfRccServiceCategory_Object = MibTableColumn
qbAtmPnniIfRccServiceCategory = _QbAtmPnniIfRccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 7),
    _QbAtmPnniIfRccServiceCategory_Type()
)
qbAtmPnniIfRccServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfRccServiceCategory.setStatus("current")


class _QbAtmPnniIfRccTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbAtmPnniIfRccTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 7


_QbAtmPnniIfRccTrafficDescrIndex_Object = MibTableColumn
qbAtmPnniIfRccTrafficDescrIndex = _QbAtmPnniIfRccTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 8),
    _QbAtmPnniIfRccTrafficDescrIndex_Type()
)
qbAtmPnniIfRccTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfRccTrafficDescrIndex.setStatus("current")


class _QbAtmPnniIfPolicingStatus_Type(Integer32):
    """Custom type qbAtmPnniIfPolicingStatus based on Integer32"""
    defaultValue = 2

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


_QbAtmPnniIfPolicingStatus_Type.__name__ = "Integer32"
_QbAtmPnniIfPolicingStatus_Object = MibTableColumn
qbAtmPnniIfPolicingStatus = _QbAtmPnniIfPolicingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1, 9),
    _QbAtmPnniIfPolicingStatus_Type()
)
qbAtmPnniIfPolicingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmPnniIfPolicingStatus.setStatus("deprecated")
_QbAtmPnniRouteAddrTable_Object = MibTable
qbAtmPnniRouteAddrTable = _QbAtmPnniRouteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3)
)
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrTable.setStatus("current")
_QbAtmPnniRouteAddrEntry_Object = MibTableRow
qbAtmPnniRouteAddrEntry = _QbAtmPnniRouteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1)
)
qbAtmPnniRouteAddrEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmPnniNodeIndex"),
    (0, "QB-ATM-MIB", "qbAtmPnniRouteAddrIfIndex"),
    (0, "QB-ATM-MIB", "qbAtmPnniRouteAddrAddress"),
)
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrEntry.setStatus("current")
_QbAtmPnniRouteAddrIfIndex_Type = InterfaceIndex
_QbAtmPnniRouteAddrIfIndex_Object = MibTableColumn
qbAtmPnniRouteAddrIfIndex = _QbAtmPnniRouteAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 1),
    _QbAtmPnniRouteAddrIfIndex_Type()
)
qbAtmPnniRouteAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrIfIndex.setStatus("current")


class _QbAtmPnniRouteAddrAddress_Type(OctetString):
    """Custom type qbAtmPnniRouteAddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_QbAtmPnniRouteAddrAddress_Type.__name__ = "OctetString"
_QbAtmPnniRouteAddrAddress_Object = MibTableColumn
qbAtmPnniRouteAddrAddress = _QbAtmPnniRouteAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 2),
    _QbAtmPnniRouteAddrAddress_Type()
)
qbAtmPnniRouteAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrAddress.setStatus("current")


class _QbAtmPnniRouteAddrPrefixLength_Type(Integer32):
    """Custom type qbAtmPnniRouteAddrPrefixLength based on Integer32"""
    defaultValue = 104

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 152),
    )


_QbAtmPnniRouteAddrPrefixLength_Type.__name__ = "Integer32"
_QbAtmPnniRouteAddrPrefixLength_Object = MibTableColumn
qbAtmPnniRouteAddrPrefixLength = _QbAtmPnniRouteAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 3),
    _QbAtmPnniRouteAddrPrefixLength_Type()
)
qbAtmPnniRouteAddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrPrefixLength.setStatus("current")
_QbAtmPnniRouteAddrRowStatus_Type = RowStatus
_QbAtmPnniRouteAddrRowStatus_Object = MibTableColumn
qbAtmPnniRouteAddrRowStatus = _QbAtmPnniRouteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 4),
    _QbAtmPnniRouteAddrRowStatus_Type()
)
qbAtmPnniRouteAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrRowStatus.setStatus("current")


class _QbAtmPnniRouteAddrProto_Type(Integer32):
    """Custom type qbAtmPnniRouteAddrProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 1),
          ("pnni", 2))
    )


_QbAtmPnniRouteAddrProto_Type.__name__ = "Integer32"
_QbAtmPnniRouteAddrProto_Object = MibTableColumn
qbAtmPnniRouteAddrProto = _QbAtmPnniRouteAddrProto_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 5),
    _QbAtmPnniRouteAddrProto_Type()
)
qbAtmPnniRouteAddrProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrProto.setStatus("current")
_QbAtmInterfaceConfSigTable_Object = MibTable
qbAtmInterfaceConfSigTable = _QbAtmInterfaceConfSigTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4)
)
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigTable.setStatus("current")
_QbAtmInterfaceConfSigEntry_Object = MibTableRow
qbAtmInterfaceConfSigEntry = _QbAtmInterfaceConfSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1)
)
atmInterfaceConfEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmInterfaceConfSigEntry")
)
qbAtmInterfaceConfSigEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigEntry.setStatus("current")


class _QbAtmInterfaceConfSigMode_Type(QbAtmSigSpec):
    """Custom type qbAtmInterfaceConfSigMode based on QbAtmSigSpec"""


_QbAtmInterfaceConfSigMode_Object = MibTableColumn
qbAtmInterfaceConfSigMode = _QbAtmInterfaceConfSigMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 1),
    _QbAtmInterfaceConfSigMode_Type()
)
qbAtmInterfaceConfSigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigMode.setStatus("current")


class _QbAtmInterfaceConfSigSide_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSide based on Integer32"""
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
        *(("network", 2),
          ("notApplicable", 3),
          ("user", 1))
    )


_QbAtmInterfaceConfSigSide_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSide_Object = MibTableColumn
qbAtmInterfaceConfSigSide = _QbAtmInterfaceConfSigSide_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 2),
    _QbAtmInterfaceConfSigSide_Type()
)
qbAtmInterfaceConfSigSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSide.setStatus("current")


class _QbAtmInterfaceConfSigParseMode_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigParseMode based on Integer32"""
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


_QbAtmInterfaceConfSigParseMode_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigParseMode_Object = MibTableColumn
qbAtmInterfaceConfSigParseMode = _QbAtmInterfaceConfSigParseMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 3),
    _QbAtmInterfaceConfSigParseMode_Type()
)
qbAtmInterfaceConfSigParseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigParseMode.setStatus("current")


class _QbAtmInterfaceConfSigAdminStatus_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigAdminStatus based on Integer32"""
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


_QbAtmInterfaceConfSigAdminStatus_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigAdminStatus_Object = MibTableColumn
qbAtmInterfaceConfSigAdminStatus = _QbAtmInterfaceConfSigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 4),
    _QbAtmInterfaceConfSigAdminStatus_Type()
)
qbAtmInterfaceConfSigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigAdminStatus.setStatus("current")


class _QbAtmInterfaceConfSigSvcMinVci_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSvcMinVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 16383),
    )


_QbAtmInterfaceConfSigSvcMinVci_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSvcMinVci_Object = MibTableColumn
qbAtmInterfaceConfSigSvcMinVci = _QbAtmInterfaceConfSigSvcMinVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 5),
    _QbAtmInterfaceConfSigSvcMinVci_Type()
)
qbAtmInterfaceConfSigSvcMinVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMinVci.setStatus("current")


class _QbAtmInterfaceConfSigSvcMaxVci_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSvcMaxVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 16383),
    )


_QbAtmInterfaceConfSigSvcMaxVci_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSvcMaxVci_Object = MibTableColumn
qbAtmInterfaceConfSigSvcMaxVci = _QbAtmInterfaceConfSigSvcMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 6),
    _QbAtmInterfaceConfSigSvcMaxVci_Type()
)
qbAtmInterfaceConfSigSvcMaxVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMaxVci.setStatus("current")


class _QbAtmInterfaceConfSigSvcMinVpi_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSvcMinVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbAtmInterfaceConfSigSvcMinVpi_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSvcMinVpi_Object = MibTableColumn
qbAtmInterfaceConfSigSvcMinVpi = _QbAtmInterfaceConfSigSvcMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 7),
    _QbAtmInterfaceConfSigSvcMinVpi_Type()
)
qbAtmInterfaceConfSigSvcMinVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMinVpi.setStatus("current")


class _QbAtmInterfaceConfSigSvcMaxVpi_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSvcMaxVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbAtmInterfaceConfSigSvcMaxVpi_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSvcMaxVpi_Object = MibTableColumn
qbAtmInterfaceConfSigSvcMaxVpi = _QbAtmInterfaceConfSigSvcMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 8),
    _QbAtmInterfaceConfSigSvcMaxVpi_Type()
)
qbAtmInterfaceConfSigSvcMaxVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMaxVpi.setStatus("current")


class _QbAtmInterfaceConfSigSvpMinVpi_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSvpMinVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbAtmInterfaceConfSigSvpMinVpi_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSvpMinVpi_Object = MibTableColumn
qbAtmInterfaceConfSigSvpMinVpi = _QbAtmInterfaceConfSigSvpMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 9),
    _QbAtmInterfaceConfSigSvpMinVpi_Type()
)
qbAtmInterfaceConfSigSvpMinVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvpMinVpi.setStatus("current")


class _QbAtmInterfaceConfSigSvpMaxVpi_Type(Integer32):
    """Custom type qbAtmInterfaceConfSigSvpMaxVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbAtmInterfaceConfSigSvpMaxVpi_Type.__name__ = "Integer32"
_QbAtmInterfaceConfSigSvpMaxVpi_Object = MibTableColumn
qbAtmInterfaceConfSigSvpMaxVpi = _QbAtmInterfaceConfSigSvpMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 10),
    _QbAtmInterfaceConfSigSvpMaxVpi_Type()
)
qbAtmInterfaceConfSigSvpMaxVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvpMaxVpi.setStatus("current")
_QbAtmInterfaceConfSigLastChange_Type = AtmVorXLastChange
_QbAtmInterfaceConfSigLastChange_Object = MibTableColumn
qbAtmInterfaceConfSigLastChange = _QbAtmInterfaceConfSigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 11),
    _QbAtmInterfaceConfSigLastChange_Type()
)
qbAtmInterfaceConfSigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigLastChange.setStatus("current")
_QbAtmInterfaceConfSigIlmiEnable_Type = Boolean
_QbAtmInterfaceConfSigIlmiEnable_Object = MibTableColumn
qbAtmInterfaceConfSigIlmiEnable = _QbAtmInterfaceConfSigIlmiEnable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 12),
    _QbAtmInterfaceConfSigIlmiEnable_Type()
)
qbAtmInterfaceConfSigIlmiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigIlmiEnable.setStatus("current")
_QbAtmPnniNbrPeerTable_Object = MibTable
qbAtmPnniNbrPeerTable = _QbAtmPnniNbrPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5)
)
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerTable.setStatus("current")
_QbAtmPnniNbrPeerEntry_Object = MibTableRow
qbAtmPnniNbrPeerEntry = _QbAtmPnniNbrPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1)
)
qbAtmPnniNbrPeerEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmPnniNodeIndex"),
    (0, "QB-ATM-MIB", "qbAtmPnniPeerRemoteNodeId"),
)
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerEntry.setStatus("current")
_QbAtmPnniPeerRemoteNodeId_Type = QbAtmPnniNodeId
_QbAtmPnniPeerRemoteNodeId_Object = MibTableColumn
qbAtmPnniPeerRemoteNodeId = _QbAtmPnniPeerRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 1),
    _QbAtmPnniPeerRemoteNodeId_Type()
)
qbAtmPnniPeerRemoteNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRemoteNodeId.setStatus("current")


class _QbAtmPnniPeerState_Type(Integer32):
    """Custom type qbAtmPnniPeerState based on Integer32"""
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
        *(("exchanging", 3),
          ("full", 5),
          ("loading", 4),
          ("negotiating", 2),
          ("npdown", 1))
    )


_QbAtmPnniPeerState_Type.__name__ = "Integer32"
_QbAtmPnniPeerState_Object = MibTableColumn
qbAtmPnniPeerState = _QbAtmPnniPeerState_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 2),
    _QbAtmPnniPeerState_Type()
)
qbAtmPnniPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerState.setStatus("current")
_QbAtmPnniPeerSvccRccIndex_Type = Integer32
_QbAtmPnniPeerSvccRccIndex_Object = MibTableColumn
qbAtmPnniPeerSvccRccIndex = _QbAtmPnniPeerSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 3),
    _QbAtmPnniPeerSvccRccIndex_Type()
)
qbAtmPnniPeerSvccRccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerSvccRccIndex.setStatus("current")
_QbAtmPnniPeerPortCount_Type = Integer32
_QbAtmPnniPeerPortCount_Object = MibTableColumn
qbAtmPnniPeerPortCount = _QbAtmPnniPeerPortCount_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 4),
    _QbAtmPnniPeerPortCount_Type()
)
qbAtmPnniPeerPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerPortCount.setStatus("current")
_QbAtmPnniPeerRcvDbSums_Type = Counter32
_QbAtmPnniPeerRcvDbSums_Object = MibTableColumn
qbAtmPnniPeerRcvDbSums = _QbAtmPnniPeerRcvDbSums_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 5),
    _QbAtmPnniPeerRcvDbSums_Type()
)
qbAtmPnniPeerRcvDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvDbSums.setStatus("current")
_QbAtmPnniPeerXmtDbSums_Type = Counter32
_QbAtmPnniPeerXmtDbSums_Object = MibTableColumn
qbAtmPnniPeerXmtDbSums = _QbAtmPnniPeerXmtDbSums_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 6),
    _QbAtmPnniPeerXmtDbSums_Type()
)
qbAtmPnniPeerXmtDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtDbSums.setStatus("current")
_QbAtmPnniPeerRcvPtsps_Type = Counter32
_QbAtmPnniPeerRcvPtsps_Object = MibTableColumn
qbAtmPnniPeerRcvPtsps = _QbAtmPnniPeerRcvPtsps_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 7),
    _QbAtmPnniPeerRcvPtsps_Type()
)
qbAtmPnniPeerRcvPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtsps.setStatus("current")
_QbAtmPnniPeerXmtPtsps_Type = Counter32
_QbAtmPnniPeerXmtPtsps_Object = MibTableColumn
qbAtmPnniPeerXmtPtsps = _QbAtmPnniPeerXmtPtsps_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 8),
    _QbAtmPnniPeerXmtPtsps_Type()
)
qbAtmPnniPeerXmtPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtsps.setStatus("current")
_QbAtmPnniPeerRcvPtseReqs_Type = Counter32
_QbAtmPnniPeerRcvPtseReqs_Object = MibTableColumn
qbAtmPnniPeerRcvPtseReqs = _QbAtmPnniPeerRcvPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 9),
    _QbAtmPnniPeerRcvPtseReqs_Type()
)
qbAtmPnniPeerRcvPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtseReqs.setStatus("current")
_QbAtmPnniPeerXmtPtseReqs_Type = Counter32
_QbAtmPnniPeerXmtPtseReqs_Object = MibTableColumn
qbAtmPnniPeerXmtPtseReqs = _QbAtmPnniPeerXmtPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 10),
    _QbAtmPnniPeerXmtPtseReqs_Type()
)
qbAtmPnniPeerXmtPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtseReqs.setStatus("current")
_QbAtmPnniPeerRcvPtseAcks_Type = Counter32
_QbAtmPnniPeerRcvPtseAcks_Object = MibTableColumn
qbAtmPnniPeerRcvPtseAcks = _QbAtmPnniPeerRcvPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 11),
    _QbAtmPnniPeerRcvPtseAcks_Type()
)
qbAtmPnniPeerRcvPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtseAcks.setStatus("current")
_QbAtmPnniPeerXmtPtseAcks_Type = Counter32
_QbAtmPnniPeerXmtPtseAcks_Object = MibTableColumn
qbAtmPnniPeerXmtPtseAcks = _QbAtmPnniPeerXmtPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 12),
    _QbAtmPnniPeerXmtPtseAcks_Type()
)
qbAtmPnniPeerXmtPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtseAcks.setStatus("current")
_QbAtmPnniNodePglTable_Object = MibTable
qbAtmPnniNodePglTable = _QbAtmPnniNodePglTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6)
)
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTable.setStatus("current")
_QbAtmPnniNodePglEntry_Object = MibTableRow
qbAtmPnniNodePglEntry = _QbAtmPnniNodePglEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1)
)
qbAtmPnniNodeEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmPnniNodePglEntry")
)
qbAtmPnniNodePglEntry.setIndexNames(*qbAtmPnniNodeEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmPnniNodePglEntry.setStatus("current")


class _QbAtmPnniNodePglLeadershipPriority_Type(Integer32):
    """Custom type qbAtmPnniNodePglLeadershipPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 205),
    )


_QbAtmPnniNodePglLeadershipPriority_Type.__name__ = "Integer32"
_QbAtmPnniNodePglLeadershipPriority_Object = MibTableColumn
qbAtmPnniNodePglLeadershipPriority = _QbAtmPnniNodePglLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 1),
    _QbAtmPnniNodePglLeadershipPriority_Type()
)
qbAtmPnniNodePglLeadershipPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglLeadershipPriority.setStatus("current")
_QbAtmPnniNodeCfgParentNodeIndex_Type = Integer32
_QbAtmPnniNodeCfgParentNodeIndex_Object = MibTableColumn
qbAtmPnniNodeCfgParentNodeIndex = _QbAtmPnniNodeCfgParentNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 2),
    _QbAtmPnniNodeCfgParentNodeIndex_Type()
)
qbAtmPnniNodeCfgParentNodeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCfgParentNodeIndex.setStatus("current")


class _QbAtmPnniNodePglInitTime_Type(Integer32):
    """Custom type qbAtmPnniNodePglInitTime based on Integer32"""
    defaultValue = 15


_QbAtmPnniNodePglInitTime_Object = MibTableColumn
qbAtmPnniNodePglInitTime = _QbAtmPnniNodePglInitTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 3),
    _QbAtmPnniNodePglInitTime_Type()
)
qbAtmPnniNodePglInitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglInitTime.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglInitTime.setUnits("seconds")


class _QbAtmPnniNodePglOverrideDelay_Type(Integer32):
    """Custom type qbAtmPnniNodePglOverrideDelay based on Integer32"""
    defaultValue = 30


_QbAtmPnniNodePglOverrideDelay_Object = MibTableColumn
qbAtmPnniNodePglOverrideDelay = _QbAtmPnniNodePglOverrideDelay_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 4),
    _QbAtmPnniNodePglOverrideDelay_Type()
)
qbAtmPnniNodePglOverrideDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglOverrideDelay.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglOverrideDelay.setUnits("seconds")


class _QbAtmPnniNodePglReelectTime_Type(Integer32):
    """Custom type qbAtmPnniNodePglReelectTime based on Integer32"""
    defaultValue = 15


_QbAtmPnniNodePglReelectTime_Object = MibTableColumn
qbAtmPnniNodePglReelectTime = _QbAtmPnniNodePglReelectTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 5),
    _QbAtmPnniNodePglReelectTime_Type()
)
qbAtmPnniNodePglReelectTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglReelectTime.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglReelectTime.setUnits("seconds")


class _QbAtmPnniNodePglState_Type(Integer32):
    """Custom type qbAtmPnniNodePglState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("awaitReElection", 10),
          ("awaitUnanimity", 6),
          ("awaiting", 2),
          ("awaitingFull", 3),
          ("calculating", 5),
          ("hungElection", 9),
          ("initialDelay", 4),
          ("operNotPgl", 8),
          ("operPgl", 7),
          ("other", 11),
          ("starting", 1))
    )


_QbAtmPnniNodePglState_Type.__name__ = "Integer32"
_QbAtmPnniNodePglState_Object = MibTableColumn
qbAtmPnniNodePglState = _QbAtmPnniNodePglState_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 6),
    _QbAtmPnniNodePglState_Type()
)
qbAtmPnniNodePglState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglState.setStatus("current")
_QbAtmPnniNodePreferredPgl_Type = QbAtmPnniNodeId
_QbAtmPnniNodePreferredPgl_Object = MibTableColumn
qbAtmPnniNodePreferredPgl = _QbAtmPnniNodePreferredPgl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 7),
    _QbAtmPnniNodePreferredPgl_Type()
)
qbAtmPnniNodePreferredPgl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePreferredPgl.setStatus("current")
_QbAtmPnniNodePeerGroupLeader_Type = QbAtmPnniNodeId
_QbAtmPnniNodePeerGroupLeader_Object = MibTableColumn
qbAtmPnniNodePeerGroupLeader = _QbAtmPnniNodePeerGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 8),
    _QbAtmPnniNodePeerGroupLeader_Type()
)
qbAtmPnniNodePeerGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupLeader.setStatus("current")
_QbAtmPnniNodePglTimeStamp_Type = TimeStamp
_QbAtmPnniNodePglTimeStamp_Object = MibTableColumn
qbAtmPnniNodePglTimeStamp = _QbAtmPnniNodePglTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 9),
    _QbAtmPnniNodePglTimeStamp_Type()
)
qbAtmPnniNodePglTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTimeStamp.setStatus("current")
_QbAtmPnniNodeActiveParentNodeId_Type = QbAtmPnniNodeId
_QbAtmPnniNodeActiveParentNodeId_Object = MibTableColumn
qbAtmPnniNodeActiveParentNodeId = _QbAtmPnniNodeActiveParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 10),
    _QbAtmPnniNodeActiveParentNodeId_Type()
)
qbAtmPnniNodeActiveParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodeActiveParentNodeId.setStatus("current")
_QbAtmPnniNodeTimerTable_Object = MibTable
qbAtmPnniNodeTimerTable = _QbAtmPnniNodeTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7)
)
if mibBuilder.loadTexts:
    qbAtmPnniNodeTimerTable.setStatus("current")
_QbAtmPnniNodeTimerEntry_Object = MibTableRow
qbAtmPnniNodeTimerEntry = _QbAtmPnniNodeTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1)
)
qbAtmPnniNodeEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmPnniNodeTimerEntry")
)
qbAtmPnniNodeTimerEntry.setIndexNames(*qbAtmPnniNodeEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmPnniNodeTimerEntry.setStatus("current")


class _QbAtmPnniNodePtseHolddown_Type(Integer32):
    """Custom type qbAtmPnniNodePtseHolddown based on Integer32"""
    defaultValue = 10


_QbAtmPnniNodePtseHolddown_Object = MibTableColumn
qbAtmPnniNodePtseHolddown = _QbAtmPnniNodePtseHolddown_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 1),
    _QbAtmPnniNodePtseHolddown_Type()
)
qbAtmPnniNodePtseHolddown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseHolddown.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseHolddown.setUnits("100 milliseconds")


class _QbAtmPnniNodeHelloHolddown_Type(Integer32):
    """Custom type qbAtmPnniNodeHelloHolddown based on Integer32"""
    defaultValue = 10


_QbAtmPnniNodeHelloHolddown_Object = MibTableColumn
qbAtmPnniNodeHelloHolddown = _QbAtmPnniNodeHelloHolddown_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 2),
    _QbAtmPnniNodeHelloHolddown_Type()
)
qbAtmPnniNodeHelloHolddown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloHolddown.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloHolddown.setUnits("100 milliseconds")


class _QbAtmPnniNodeHelloInterval_Type(Integer32):
    """Custom type qbAtmPnniNodeHelloInterval based on Integer32"""
    defaultValue = 15


_QbAtmPnniNodeHelloInterval_Object = MibTableColumn
qbAtmPnniNodeHelloInterval = _QbAtmPnniNodeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 3),
    _QbAtmPnniNodeHelloInterval_Type()
)
qbAtmPnniNodeHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInterval.setUnits("seconds")


class _QbAtmPnniNodeHelloInactivityFactor_Type(Integer32):
    """Custom type qbAtmPnniNodeHelloInactivityFactor based on Integer32"""
    defaultValue = 5


_QbAtmPnniNodeHelloInactivityFactor_Object = MibTableColumn
qbAtmPnniNodeHelloInactivityFactor = _QbAtmPnniNodeHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 4),
    _QbAtmPnniNodeHelloInactivityFactor_Type()
)
qbAtmPnniNodeHelloInactivityFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInactivityFactor.setStatus("current")


class _QbAtmPnniNodeHlinkInact_Type(Integer32):
    """Custom type qbAtmPnniNodeHlinkInact based on Integer32"""
    defaultValue = 120


_QbAtmPnniNodeHlinkInact_Object = MibTableColumn
qbAtmPnniNodeHlinkInact = _QbAtmPnniNodeHlinkInact_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 5),
    _QbAtmPnniNodeHlinkInact_Type()
)
qbAtmPnniNodeHlinkInact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHlinkInact.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHlinkInact.setUnits("seconds")


class _QbAtmPnniNodePtseRefreshInterval_Type(Integer32):
    """Custom type qbAtmPnniNodePtseRefreshInterval based on Integer32"""
    defaultValue = 1800


_QbAtmPnniNodePtseRefreshInterval_Object = MibTableColumn
qbAtmPnniNodePtseRefreshInterval = _QbAtmPnniNodePtseRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 6),
    _QbAtmPnniNodePtseRefreshInterval_Type()
)
qbAtmPnniNodePtseRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseRefreshInterval.setUnits("seconds")


class _QbAtmPnniNodePtseLifetimeFactor_Type(Integer32):
    """Custom type qbAtmPnniNodePtseLifetimeFactor based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1000),
    )


_QbAtmPnniNodePtseLifetimeFactor_Type.__name__ = "Integer32"
_QbAtmPnniNodePtseLifetimeFactor_Object = MibTableColumn
qbAtmPnniNodePtseLifetimeFactor = _QbAtmPnniNodePtseLifetimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 7),
    _QbAtmPnniNodePtseLifetimeFactor_Type()
)
qbAtmPnniNodePtseLifetimeFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseLifetimeFactor.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseLifetimeFactor.setUnits("percent")


class _QbAtmPnniNodeRxmtInterval_Type(Integer32):
    """Custom type qbAtmPnniNodeRxmtInterval based on Integer32"""
    defaultValue = 5


_QbAtmPnniNodeRxmtInterval_Object = MibTableColumn
qbAtmPnniNodeRxmtInterval = _QbAtmPnniNodeRxmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 8),
    _QbAtmPnniNodeRxmtInterval_Type()
)
qbAtmPnniNodeRxmtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeRxmtInterval.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeRxmtInterval.setUnits("seconds")


class _QbAtmPnniNodePeerDelayedAckInterval_Type(Integer32):
    """Custom type qbAtmPnniNodePeerDelayedAckInterval based on Integer32"""
    defaultValue = 10


_QbAtmPnniNodePeerDelayedAckInterval_Object = MibTableColumn
qbAtmPnniNodePeerDelayedAckInterval = _QbAtmPnniNodePeerDelayedAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 9),
    _QbAtmPnniNodePeerDelayedAckInterval_Type()
)
qbAtmPnniNodePeerDelayedAckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerDelayedAckInterval.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerDelayedAckInterval.setUnits("100 milliseconds")


class _QbAtmPnniNodeAvcrPm_Type(Integer32):
    """Custom type qbAtmPnniNodeAvcrPm based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_QbAtmPnniNodeAvcrPm_Type.__name__ = "Integer32"
_QbAtmPnniNodeAvcrPm_Object = MibTableColumn
qbAtmPnniNodeAvcrPm = _QbAtmPnniNodeAvcrPm_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 10),
    _QbAtmPnniNodeAvcrPm_Type()
)
qbAtmPnniNodeAvcrPm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrPm.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrPm.setUnits("percent")


class _QbAtmPnniNodeAvcrMt_Type(Integer32):
    """Custom type qbAtmPnniNodeAvcrMt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_QbAtmPnniNodeAvcrMt_Type.__name__ = "Integer32"
_QbAtmPnniNodeAvcrMt_Object = MibTableColumn
qbAtmPnniNodeAvcrMt = _QbAtmPnniNodeAvcrMt_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 11),
    _QbAtmPnniNodeAvcrMt_Type()
)
qbAtmPnniNodeAvcrMt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrMt.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrMt.setUnits("percent")


class _QbAtmPnniNodeCdvPm_Type(Integer32):
    """Custom type qbAtmPnniNodeCdvPm based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_QbAtmPnniNodeCdvPm_Type.__name__ = "Integer32"
_QbAtmPnniNodeCdvPm_Object = MibTableColumn
qbAtmPnniNodeCdvPm = _QbAtmPnniNodeCdvPm_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 12),
    _QbAtmPnniNodeCdvPm_Type()
)
qbAtmPnniNodeCdvPm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCdvPm.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCdvPm.setUnits("percent")


class _QbAtmPnniNodeCtdPm_Type(Integer32):
    """Custom type qbAtmPnniNodeCtdPm based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_QbAtmPnniNodeCtdPm_Type.__name__ = "Integer32"
_QbAtmPnniNodeCtdPm_Object = MibTableColumn
qbAtmPnniNodeCtdPm = _QbAtmPnniNodeCtdPm_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7, 1, 13),
    _QbAtmPnniNodeCtdPm_Type()
)
qbAtmPnniNodeCtdPm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCtdPm.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCtdPm.setUnits("percent")
_QbAtmPnniLinkTable_Object = MibTable
qbAtmPnniLinkTable = _QbAtmPnniLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8)
)
if mibBuilder.loadTexts:
    qbAtmPnniLinkTable.setStatus("current")
_QbAtmPnniLinkEntry_Object = MibTableRow
qbAtmPnniLinkEntry = _QbAtmPnniLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8, 1)
)
qbAtmPnniLinkEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmPnniNodeIndex"),
    (0, "QB-ATM-MIB", "qbAtmPnniLinkPortId"),
)
if mibBuilder.loadTexts:
    qbAtmPnniLinkEntry.setStatus("current")
_QbAtmPnniLinkPortId_Type = Integer32
_QbAtmPnniLinkPortId_Object = MibTableColumn
qbAtmPnniLinkPortId = _QbAtmPnniLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8, 1, 1),
    _QbAtmPnniLinkPortId_Type()
)
qbAtmPnniLinkPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniLinkPortId.setStatus("current")


class _QbAtmPnniLinkType_Type(Integer32):
    """Custom type qbAtmPnniLinkType based on Integer32"""
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
        *(("horizontalLinkToFromLgn", 3),
          ("lowestLevelHorizontalLink", 2),
          ("lowestLevelOutsideLink", 4),
          ("outsideLinkAndUplink", 6),
          ("unknown", 1),
          ("uplink", 5))
    )


_QbAtmPnniLinkType_Type.__name__ = "Integer32"
_QbAtmPnniLinkType_Object = MibTableColumn
qbAtmPnniLinkType = _QbAtmPnniLinkType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8, 1, 2),
    _QbAtmPnniLinkType_Type()
)
qbAtmPnniLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniLinkType.setStatus("current")
_QbAtmPnniLinkHelloState_Type = QbAtmPnniHelloState
_QbAtmPnniLinkHelloState_Object = MibTableColumn
qbAtmPnniLinkHelloState = _QbAtmPnniLinkHelloState_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8, 1, 3),
    _QbAtmPnniLinkHelloState_Type()
)
qbAtmPnniLinkHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniLinkHelloState.setStatus("current")
_QbAtmHiddenVclTable_Object = MibTable
qbAtmHiddenVclTable = _QbAtmHiddenVclTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8)
)
if mibBuilder.loadTexts:
    qbAtmHiddenVclTable.setStatus("current")
_QbAtmHiddenVclEntry_Object = MibTableRow
qbAtmHiddenVclEntry = _QbAtmHiddenVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1)
)
atmVclEntry.registerAugmentions(
    ("QB-ATM-MIB",
     "qbAtmHiddenVclEntry")
)
qbAtmHiddenVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmHiddenVclEntry.setStatus("current")


class _QbAtmHiddenVclName_Type(DisplayString):
    """Custom type qbAtmHiddenVclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbAtmHiddenVclName_Type.__name__ = "DisplayString"
_QbAtmHiddenVclName_Object = MibTableColumn
qbAtmHiddenVclName = _QbAtmHiddenVclName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1, 1),
    _QbAtmHiddenVclName_Type()
)
qbAtmHiddenVclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmHiddenVclName.setStatus("current")


class _QbAtmHiddenVclType_Type(Integer32):
    """Custom type qbAtmHiddenVclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("native", 1),
          ("non-native", 2))
    )


_QbAtmHiddenVclType_Type.__name__ = "Integer32"
_QbAtmHiddenVclType_Object = MibTableColumn
qbAtmHiddenVclType = _QbAtmHiddenVclType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1, 2),
    _QbAtmHiddenVclType_Type()
)
qbAtmHiddenVclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmHiddenVclType.setStatus("current")
_QbAtmHiddenVclIfIndex_Type = InterfaceIndex
_QbAtmHiddenVclIfIndex_Object = MibTableColumn
qbAtmHiddenVclIfIndex = _QbAtmHiddenVclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1, 3),
    _QbAtmHiddenVclIfIndex_Type()
)
qbAtmHiddenVclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmHiddenVclIfIndex.setStatus("current")
_QbAtmHiddenVclVtIndex_Type = Integer32
_QbAtmHiddenVclVtIndex_Object = MibTableColumn
qbAtmHiddenVclVtIndex = _QbAtmHiddenVclVtIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1, 4),
    _QbAtmHiddenVclVtIndex_Type()
)
qbAtmHiddenVclVtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmHiddenVclVtIndex.setStatus("current")
_QbAtmSwitchModuleGroup_ObjectIdentity = ObjectIdentity
qbAtmSwitchModuleGroup = _QbAtmSwitchModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 9)
)
_QbAtmStatsBuffOverCells_Type = Counter32
_QbAtmStatsBuffOverCells_Object = MibScalar
qbAtmStatsBuffOverCells = _QbAtmStatsBuffOverCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 9, 1),
    _QbAtmStatsBuffOverCells_Type()
)
qbAtmStatsBuffOverCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmStatsBuffOverCells.setStatus("current")
_QbAtmStatsInvalidCells_Type = Counter32
_QbAtmStatsInvalidCells_Object = MibScalar
qbAtmStatsInvalidCells = _QbAtmStatsInvalidCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 9, 2),
    _QbAtmStatsInvalidCells_Type()
)
qbAtmStatsInvalidCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmStatsInvalidCells.setStatus("current")
_QbAtmStatsInvUpdateCells_Type = Counter32
_QbAtmStatsInvUpdateCells_Object = MibScalar
qbAtmStatsInvUpdateCells = _QbAtmStatsInvUpdateCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 9, 3),
    _QbAtmStatsInvUpdateCells_Type()
)
qbAtmStatsInvUpdateCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmStatsInvUpdateCells.setStatus("current")
_QbAtmInterfaceStatTable_Object = MibTable
qbAtmInterfaceStatTable = _QbAtmInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10)
)
if mibBuilder.loadTexts:
    qbAtmInterfaceStatTable.setStatus("current")
_QbAtmInterfaceStatEntry_Object = MibTableRow
qbAtmInterfaceStatEntry = _QbAtmInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10, 1)
)
qbAtmInterfaceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbAtmInterfaceStatEntry.setStatus("current")
_QbAtmInterfaceStatTxOAMCells_Type = Counter32
_QbAtmInterfaceStatTxOAMCells_Object = MibTableColumn
qbAtmInterfaceStatTxOAMCells = _QbAtmInterfaceStatTxOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10, 1, 1),
    _QbAtmInterfaceStatTxOAMCells_Type()
)
qbAtmInterfaceStatTxOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatTxOAMCells.setStatus("current")
_QbAtmInterfaceStatRxOAMCells_Type = Counter32
_QbAtmInterfaceStatRxOAMCells_Object = MibTableColumn
qbAtmInterfaceStatRxOAMCells = _QbAtmInterfaceStatRxOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10, 1, 2),
    _QbAtmInterfaceStatRxOAMCells_Type()
)
qbAtmInterfaceStatRxOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatRxOAMCells.setStatus("current")
_QbAtmInBandMgtTable_Object = MibTable
qbAtmInBandMgtTable = _QbAtmInBandMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11)
)
if mibBuilder.loadTexts:
    qbAtmInBandMgtTable.setStatus("current")
_QbAtmInBandMgtEntry_Object = MibTableRow
qbAtmInBandMgtEntry = _QbAtmInBandMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1)
)
qbAtmInBandMgtEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmInBandMgtIpAddr"),
)
if mibBuilder.loadTexts:
    qbAtmInBandMgtEntry.setStatus("current")
_QbAtmInBandMgtIpAddr_Type = IpAddress
_QbAtmInBandMgtIpAddr_Object = MibTableColumn
qbAtmInBandMgtIpAddr = _QbAtmInBandMgtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 1),
    _QbAtmInBandMgtIpAddr_Type()
)
qbAtmInBandMgtIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpAddr.setStatus("current")
_QbAtmInBandMgtIpMask_Type = IpAddress
_QbAtmInBandMgtIpMask_Object = MibTableColumn
qbAtmInBandMgtIpMask = _QbAtmInBandMgtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 2),
    _QbAtmInBandMgtIpMask_Type()
)
qbAtmInBandMgtIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpMask.setStatus("current")
_QbAtmInBandMgtIpIfIndex_Type = InterfaceIndex
_QbAtmInBandMgtIpIfIndex_Object = MibTableColumn
qbAtmInBandMgtIpIfIndex = _QbAtmInBandMgtIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 3),
    _QbAtmInBandMgtIpIfIndex_Type()
)
qbAtmInBandMgtIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpIfIndex.setStatus("current")
_QbAtmInBandMgtNeighborIp_Type = IpAddress
_QbAtmInBandMgtNeighborIp_Object = MibTableColumn
qbAtmInBandMgtNeighborIp = _QbAtmInBandMgtNeighborIp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 4),
    _QbAtmInBandMgtNeighborIp_Type()
)
qbAtmInBandMgtNeighborIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtNeighborIp.setStatus("current")
_QbAtmInBandMgtIfIndex_Type = InterfaceIndex
_QbAtmInBandMgtIfIndex_Object = MibTableColumn
qbAtmInBandMgtIfIndex = _QbAtmInBandMgtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 5),
    _QbAtmInBandMgtIfIndex_Type()
)
qbAtmInBandMgtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIfIndex.setStatus("current")
_QbAtmInBandMgtVpi_Type = AtmVpIdentifier
_QbAtmInBandMgtVpi_Object = MibTableColumn
qbAtmInBandMgtVpi = _QbAtmInBandMgtVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 6),
    _QbAtmInBandMgtVpi_Type()
)
qbAtmInBandMgtVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtVpi.setStatus("current")
_QbAtmInBandMgtVci_Type = AtmVcIdentifier
_QbAtmInBandMgtVci_Object = MibTableColumn
qbAtmInBandMgtVci = _QbAtmInBandMgtVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 7),
    _QbAtmInBandMgtVci_Type()
)
qbAtmInBandMgtVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtVci.setStatus("current")
_QbAtmInBandMgtConnKind_Type = AtmConnKind
_QbAtmInBandMgtConnKind_Object = MibTableColumn
qbAtmInBandMgtConnKind = _QbAtmInBandMgtConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 8),
    _QbAtmInBandMgtConnKind_Type()
)
qbAtmInBandMgtConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtConnKind.setStatus("current")
_QbAtmInBandMgtTxTd_Type = AtmTrafficDescrParamIndex
_QbAtmInBandMgtTxTd_Object = MibTableColumn
qbAtmInBandMgtTxTd = _QbAtmInBandMgtTxTd_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 9),
    _QbAtmInBandMgtTxTd_Type()
)
qbAtmInBandMgtTxTd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTxTd.setStatus("current")
_QbAtmInBandMgtRxTd_Type = AtmTrafficDescrParamIndex
_QbAtmInBandMgtRxTd_Object = MibTableColumn
qbAtmInBandMgtRxTd = _QbAtmInBandMgtRxTd_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 10),
    _QbAtmInBandMgtRxTd_Type()
)
qbAtmInBandMgtRxTd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtRxTd.setStatus("current")
_QbAtmInBandMgtTargetNsapAddr_Type = AtmAddr
_QbAtmInBandMgtTargetNsapAddr_Object = MibTableColumn
qbAtmInBandMgtTargetNsapAddr = _QbAtmInBandMgtTargetNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 11),
    _QbAtmInBandMgtTargetNsapAddr_Type()
)
qbAtmInBandMgtTargetNsapAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTargetNsapAddr.setStatus("current")
_QbAtmInBandMgtRowStatus_Type = RowStatus
_QbAtmInBandMgtRowStatus_Object = MibTableColumn
qbAtmInBandMgtRowStatus = _QbAtmInBandMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 12),
    _QbAtmInBandMgtRowStatus_Type()
)
qbAtmInBandMgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtRowStatus.setStatus("current")
_QbAtmTrafficDescriptorTypes_ObjectIdentity = ObjectIdentity
qbAtmTrafficDescriptorTypes = _QbAtmTrafficDescriptorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 12)
)
_QbAtmPkt_ObjectIdentity = ObjectIdentity
qbAtmPkt = _QbAtmPkt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    qbAtmPkt.setStatus("current")
_QbAtmConformance_ObjectIdentity = ObjectIdentity
qbAtmConformance = _QbAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2)
)
_QbAtmCompliances_ObjectIdentity = ObjectIdentity
qbAtmCompliances = _QbAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 1)
)
_QbAtmGroups_ObjectIdentity = ObjectIdentity
qbAtmGroups = _QbAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2)
)
_QbAtmBaseGroup_ObjectIdentity = ObjectIdentity
qbAtmBaseGroup = _QbAtmBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 3)
)


class _QbAtmF4F5LLID_Type(OctetString):
    """Custom type qbAtmF4F5LLID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_QbAtmF4F5LLID_Type.__name__ = "OctetString"
_QbAtmF4F5LLID_Object = MibScalar
qbAtmF4F5LLID = _QbAtmF4F5LLID_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 3, 1),
    _QbAtmF4F5LLID_Type()
)
qbAtmF4F5LLID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmF4F5LLID.setStatus("current")


class _QbAtmDefaultPCBE_Type(Integer32):
    """Custom type qbAtmDefaultPCBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 70),
    )


_QbAtmDefaultPCBE_Type.__name__ = "Integer32"
_QbAtmDefaultPCBE_Object = MibScalar
qbAtmDefaultPCBE = _QbAtmDefaultPCBE_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 3, 2),
    _QbAtmDefaultPCBE_Type()
)
qbAtmDefaultPCBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmDefaultPCBE.setStatus("current")

# Managed Objects groups

qbAtmInterfaceConfGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 1)
)
qbAtmInterfaceConfGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmInterfaceConfPolicingStatus"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfMaxPvcVci"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfMinPvcVci"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfMaxPvcVpi"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfMinPvcVci"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfMaxPvpVpi"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfMinPvpVpi"))
)
if mibBuilder.loadTexts:
    qbAtmInterfaceConfGroupInfo.setStatus("current")

qbAtmTrafficDescrParamGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 2)
)
qbAtmTrafficDescrParamGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmTrafficDescrParamName"),
        ("QB-ATM-MIB", "qbAtmTrafficDescrParamDefault"))
)
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamGroupInfo.setStatus("current")

qbAtmVclGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 3)
)
qbAtmVclGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmVclLoopback"),
        ("QB-ATM-MIB", "qbAtmVclLoopback"),
        ("QB-ATM-MIB", "qbAtmVclF4F5LoopbackInsert"),
        ("QB-ATM-MIB", "qbAtmVclF4F5LoopbackStatus"),
        ("QB-ATM-MIB", "qbAtmVclF4F5LoopbackTimestamp"),
        ("QB-ATM-MIB", "qbAtmVclMgmtIpAddr"),
        ("QB-ATM-MIB", "qbAtmVclMgmtIpMask"),
        ("QB-ATM-MIB", "qbAtmVclMgmtNeighborIP"),
        ("QB-ATM-MIB", "qbAtmVclConnKind"))
)
if mibBuilder.loadTexts:
    qbAtmVclGroupInfo.setStatus("current")

qbAtmVplGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 4)
)
qbAtmVplGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmVplLoopback"),
        ("QB-ATM-MIB", "qbAtmVplF4F5LoopbackInsert"),
        ("QB-ATM-MIB", "qbAtmVplF4F5LoopbackStatus"),
        ("QB-ATM-MIB", "qbAtmVplF4F5LoopbackTimestamp"))
)
if mibBuilder.loadTexts:
    qbAtmVplGroupInfo.setStatus("current")

qbAtmVcCrossConnectGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 5)
)
qbAtmVcCrossConnectGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmVcCrossConnectName"),
        ("QB-ATM-MIB", "qbAtmVcCrossConnectRxTrafficDescrIndex"),
        ("QB-ATM-MIB", "qbAtmVcCrossConnectTxTrafficDescrIndex"))
)
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectGroupInfo.setStatus("current")

qbAtmVpCrossConnectGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 6)
)
qbAtmVpCrossConnectGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmVpCrossConnectName"),
        ("QB-ATM-MIB", "qbAtmVpCrossConnectRxTrafficDescrIndex"),
        ("QB-ATM-MIB", "qbAtmVpCrossConnectTxTrafficDescrIndex"))
)
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectGroupInfo.setStatus("current")

qbAtmPnniNodeGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 7)
)
qbAtmPnniNodeGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniNodeNetAddrPrefix"),
        ("QB-ATM-MIB", "qbAtmPnniNodeEndSysId"),
        ("QB-ATM-MIB", "qbAtmPnniNodeLevel"),
        ("QB-ATM-MIB", "qbAtmPnniNodeRowStatus"),
        ("QB-ATM-MIB", "qbAtmPnniNodeOperStatus"),
        ("QB-ATM-MIB", "qbAtmPnniNodeAtmAddress"),
        ("QB-ATM-MIB", "qbAtmPnniNodePeerGroupId"))
)
if mibBuilder.loadTexts:
    qbAtmPnniNodeGroupInfo.setStatus("current")

qbAtmPnniIfGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 8)
)
qbAtmPnniIfGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniRouteAddrPrefixLength"),
        ("QB-ATM-MIB", "qbAtmPnniRouteAddrRowStatus"),
        ("QB-ATM-MIB", "qbAtmPnniRouteAddrProto"))
)
if mibBuilder.loadTexts:
    qbAtmPnniIfGroupInfo.setStatus("current")

qbAtmPnniRouteAddrGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 9)
)
qbAtmPnniRouteAddrGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniIfAdmWeightCbr"),
        ("QB-ATM-MIB", "qbAtmPnniIfAdmWeightRtVbr"),
        ("QB-ATM-MIB", "qbAtmPnniIfAdmWeightNrtVbr"),
        ("QB-ATM-MIB", "qbAtmPnniIfAdmWeightAbr"),
        ("QB-ATM-MIB", "qbAtmPnniIfAdmWeightUbr"),
        ("QB-ATM-MIB", "qbAtmPnniIfRccServiceCategory"),
        ("QB-ATM-MIB", "qbAtmPnniIfRccTrafficDescrIndex"))
)
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrGroupInfo.setStatus("current")

qbAtmInterfaceConfSigGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 10)
)
qbAtmInterfaceConfSigGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmInterfaceConfSigMode"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSide"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigParseMode"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigAdminStatus"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSvcMinVci"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSvcMaxVci"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSvcMinVpi"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSvcMaxVpi"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSvpMinVpi"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigSvpMaxVpi"),
        ("QB-ATM-MIB", "qbAtmInterfaceConfSigLastChange"))
)
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigGroupInfo.setStatus("current")

qbAtmPnniNbrPeerGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 11)
)
qbAtmPnniNbrPeerGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniPeerState"),
        ("QB-ATM-MIB", "qbAtmPnniPeerSvccRccIndex"),
        ("QB-ATM-MIB", "qbAtmPnniPeerPortCount"),
        ("QB-ATM-MIB", "qbAtmPnniPeerRcvDbSums"),
        ("QB-ATM-MIB", "qbAtmPnniPeerXmtDbSums"),
        ("QB-ATM-MIB", "qbAtmPnniPeerRcvPtsps"),
        ("QB-ATM-MIB", "qbAtmPnniPeerXmtPtsps"),
        ("QB-ATM-MIB", "qbAtmPnniPeerRcvPtseReqs"),
        ("QB-ATM-MIB", "qbAtmPnniPeerXmtPtseReqs"),
        ("QB-ATM-MIB", "qbAtmPnniPeerRcvPtseAcks"),
        ("QB-ATM-MIB", "qbAtmPnniPeerXmtPtseAcks"))
)
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerGroupInfo.setStatus("current")

qbAtmPnniPglGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 12)
)
qbAtmPnniPglGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniNodePglLeadershipPriority"),
        ("QB-ATM-MIB", "qbAtmPnniNodeCfgParentNodeIndex"),
        ("QB-ATM-MIB", "qbAtmPnniNodePglInitTime"),
        ("QB-ATM-MIB", "qbAtmPnniNodePglOverrideDelay"),
        ("QB-ATM-MIB", "qbAtmPnniNodePglReelectTime"),
        ("QB-ATM-MIB", "qbAtmPnniNodePglState"),
        ("QB-ATM-MIB", "qbAtmPnniNodePreferredPgl"),
        ("QB-ATM-MIB", "qbAtmPnniNodePeerGroupLeader"),
        ("QB-ATM-MIB", "qbAtmPnniNodePglTimeStamp"),
        ("QB-ATM-MIB", "qbAtmPnniNodeActiveParentNodeId"))
)
if mibBuilder.loadTexts:
    qbAtmPnniPglGroupInfo.setStatus("current")

qbAtmPnniTimerGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 13)
)
qbAtmPnniTimerGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniNodePtseHolddown"),
        ("QB-ATM-MIB", "qbAtmPnniNodeHelloHolddown"),
        ("QB-ATM-MIB", "qbAtmPnniNodeHelloInterval"),
        ("QB-ATM-MIB", "qbAtmPnniNodeHelloInactivityFactor"),
        ("QB-ATM-MIB", "qbAtmPnniNodeHlinkInact"),
        ("QB-ATM-MIB", "qbAtmPnniNodePtseRefreshInterval"),
        ("QB-ATM-MIB", "qbAtmPnniNodePtseLifetimeFactor"),
        ("QB-ATM-MIB", "qbAtmPnniNodeRxmtInterval"),
        ("QB-ATM-MIB", "qbAtmPnniNodePeerDelayedAckInterval"),
        ("QB-ATM-MIB", "qbAtmPnniNodeAvcrPm"),
        ("QB-ATM-MIB", "qbAtmPnniNodeAvcrMt"),
        ("QB-ATM-MIB", "qbAtmPnniNodeCdvPm"),
        ("QB-ATM-MIB", "qbAtmPnniNodeCtdPm"))
)
if mibBuilder.loadTexts:
    qbAtmPnniTimerGroupInfo.setStatus("current")

qbAtmPnniLinkGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 14)
)
qbAtmPnniLinkGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniLinkType"),
        ("QB-ATM-MIB", "qbAtmPnniLinkHelloState"))
)
if mibBuilder.loadTexts:
    qbAtmPnniLinkGroupInfo.setStatus("current")

qbAtmInBandMgtGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 15)
)
qbAtmInBandMgtGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmInBandMgtIpMask"),
        ("QB-ATM-MIB", "qbAtmInBandMgtIpIfIndex"),
        ("QB-ATM-MIB", "qbAtmInBandMgtNeighborIp"),
        ("QB-ATM-MIB", "qbAtmInBandMgtIfIndex"),
        ("QB-ATM-MIB", "qbAtmInBandMgtVpi"),
        ("QB-ATM-MIB", "qbAtmInBandMgtVci"),
        ("QB-ATM-MIB", "qbAtmInBandMgtConnKind"),
        ("QB-ATM-MIB", "qbAtmInBandMgtTxTd"),
        ("QB-ATM-MIB", "qbAtmInBandMgtRxTd"),
        ("QB-ATM-MIB", "qbAtmInBandMgtTargetNsapAddr"),
        ("QB-ATM-MIB", "qbAtmInBandMgtRowStatus"))
)
if mibBuilder.loadTexts:
    qbAtmInBandMgtGroupInfo.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qbAtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-ATM-MIB",
    **{"QbAtmPnniWeight": QbAtmPnniWeight,
       "QbAtmPnniNodeId": QbAtmPnniNodeId,
       "QbAtmSigSpec": QbAtmSigSpec,
       "QbAtmPnniHelloState": QbAtmPnniHelloState,
       "QbAtmPnniAtmAddr": QbAtmPnniAtmAddr,
       "QbAtmPnniNodeIndex": QbAtmPnniNodeIndex,
       "QbAtmPnniPeerGroupId": QbAtmPnniPeerGroupId,
       "QbF4F5LoopbackStatus": QbF4F5LoopbackStatus,
       "QbF4F5Status": QbF4F5Status,
       "qbAtmMIB": qbAtmMIB,
       "qbAtmObjects": qbAtmObjects,
       "qbAtmInterfaceConfTable": qbAtmInterfaceConfTable,
       "qbAtmInterfaceConfEntry": qbAtmInterfaceConfEntry,
       "qbAtmInterfaceConfPolicingStatus": qbAtmInterfaceConfPolicingStatus,
       "qbAtmInterfaceConfMaxPvcVpi": qbAtmInterfaceConfMaxPvcVpi,
       "qbAtmInterfaceConfMinPvcVpi": qbAtmInterfaceConfMinPvcVpi,
       "qbAtmInterfaceConfMaxPvcVci": qbAtmInterfaceConfMaxPvcVci,
       "qbAtmInterfaceConfMinPvcVci": qbAtmInterfaceConfMinPvcVci,
       "qbAtmInterfaceConfMaxPvpVpi": qbAtmInterfaceConfMaxPvpVpi,
       "qbAtmInterfaceConfMinPvpVpi": qbAtmInterfaceConfMinPvpVpi,
       "qbAtmTrafficDescrParamTable": qbAtmTrafficDescrParamTable,
       "qbAtmTrafficDescrParamEntry": qbAtmTrafficDescrParamEntry,
       "qbAtmTrafficDescrParamName": qbAtmTrafficDescrParamName,
       "qbAtmTrafficDescrParamDefault": qbAtmTrafficDescrParamDefault,
       "qbAtmVclTable": qbAtmVclTable,
       "qbAtmVclEntry": qbAtmVclEntry,
       "qbAtmVclLoopback": qbAtmVclLoopback,
       "qbAtmVclF4F5LoopbackInsert": qbAtmVclF4F5LoopbackInsert,
       "qbAtmVclF4F5LoopbackStatus": qbAtmVclF4F5LoopbackStatus,
       "qbAtmVclF4F5LoopbackTimestamp": qbAtmVclF4F5LoopbackTimestamp,
       "qbAtmVclMgmtIpAddr": qbAtmVclMgmtIpAddr,
       "qbAtmVclMgmtIpMask": qbAtmVclMgmtIpMask,
       "qbAtmVclMgmtNeighborIP": qbAtmVclMgmtNeighborIP,
       "qbAtmVclConnKind": qbAtmVclConnKind,
       "qbAtmVclF4F5TxStatus": qbAtmVclF4F5TxStatus,
       "qbAtmVclF4F5TxLastChange": qbAtmVclF4F5TxLastChange,
       "qbAtmVclF4F5RxStatus": qbAtmVclF4F5RxStatus,
       "qbAtmVclF4F5RxLastChange": qbAtmVclF4F5RxLastChange,
       "qbAtmVplTable": qbAtmVplTable,
       "qbAtmVplEntry": qbAtmVplEntry,
       "qbAtmVplLoopback": qbAtmVplLoopback,
       "qbAtmVplF4F5LoopbackInsert": qbAtmVplF4F5LoopbackInsert,
       "qbAtmVplF4F5LoopbackStatus": qbAtmVplF4F5LoopbackStatus,
       "qbAtmVplF4F5LoopbackTimestamp": qbAtmVplF4F5LoopbackTimestamp,
       "qbAtmVplF4F5TxStatus": qbAtmVplF4F5TxStatus,
       "qbAtmVplF4F5TxLastChange": qbAtmVplF4F5TxLastChange,
       "qbAtmVplF4F5RxStatus": qbAtmVplF4F5RxStatus,
       "qbAtmVplF4F5RxLastChange": qbAtmVplF4F5RxLastChange,
       "qbAtmVcCrossConnectTable": qbAtmVcCrossConnectTable,
       "qbAtmVcCrossConnectEntry": qbAtmVcCrossConnectEntry,
       "qbAtmVcCrossConnectName": qbAtmVcCrossConnectName,
       "qbAtmVcCrossConnectRxTrafficDescrIndex": qbAtmVcCrossConnectRxTrafficDescrIndex,
       "qbAtmVcCrossConnectTxTrafficDescrIndex": qbAtmVcCrossConnectTxTrafficDescrIndex,
       "qbAtmVpCrossConnectTable": qbAtmVpCrossConnectTable,
       "qbAtmVpCrossConnectEntry": qbAtmVpCrossConnectEntry,
       "qbAtmVpCrossConnectName": qbAtmVpCrossConnectName,
       "qbAtmVpCrossConnectRxTrafficDescrIndex": qbAtmVpCrossConnectRxTrafficDescrIndex,
       "qbAtmVpCrossConnectTxTrafficDescrIndex": qbAtmVpCrossConnectTxTrafficDescrIndex,
       "qbAtmSigGroup": qbAtmSigGroup,
       "qbAtmPnniNodeTable": qbAtmPnniNodeTable,
       "qbAtmPnniNodeEntry": qbAtmPnniNodeEntry,
       "qbAtmPnniNodeIndex": qbAtmPnniNodeIndex,
       "qbAtmPnniNodeNetAddrPrefix": qbAtmPnniNodeNetAddrPrefix,
       "qbAtmPnniNodeEndSysId": qbAtmPnniNodeEndSysId,
       "qbAtmPnniNodeLevel": qbAtmPnniNodeLevel,
       "qbAtmPnniNodeRowStatus": qbAtmPnniNodeRowStatus,
       "qbAtmPnniNodeOperStatus": qbAtmPnniNodeOperStatus,
       "qbAtmPnniNodeAtmAddress": qbAtmPnniNodeAtmAddress,
       "qbAtmPnniNodePeerGroupId": qbAtmPnniNodePeerGroupId,
       "qbAtmPnniIfTable": qbAtmPnniIfTable,
       "qbAtmPnniIfEntry": qbAtmPnniIfEntry,
       "qbAtmPnniIfNodeIndex": qbAtmPnniIfNodeIndex,
       "qbAtmPnniIfAdmWeightCbr": qbAtmPnniIfAdmWeightCbr,
       "qbAtmPnniIfAdmWeightRtVbr": qbAtmPnniIfAdmWeightRtVbr,
       "qbAtmPnniIfAdmWeightNrtVbr": qbAtmPnniIfAdmWeightNrtVbr,
       "qbAtmPnniIfAdmWeightAbr": qbAtmPnniIfAdmWeightAbr,
       "qbAtmPnniIfAdmWeightUbr": qbAtmPnniIfAdmWeightUbr,
       "qbAtmPnniIfRccServiceCategory": qbAtmPnniIfRccServiceCategory,
       "qbAtmPnniIfRccTrafficDescrIndex": qbAtmPnniIfRccTrafficDescrIndex,
       "qbAtmPnniIfPolicingStatus": qbAtmPnniIfPolicingStatus,
       "qbAtmPnniRouteAddrTable": qbAtmPnniRouteAddrTable,
       "qbAtmPnniRouteAddrEntry": qbAtmPnniRouteAddrEntry,
       "qbAtmPnniRouteAddrIfIndex": qbAtmPnniRouteAddrIfIndex,
       "qbAtmPnniRouteAddrAddress": qbAtmPnniRouteAddrAddress,
       "qbAtmPnniRouteAddrPrefixLength": qbAtmPnniRouteAddrPrefixLength,
       "qbAtmPnniRouteAddrRowStatus": qbAtmPnniRouteAddrRowStatus,
       "qbAtmPnniRouteAddrProto": qbAtmPnniRouteAddrProto,
       "qbAtmInterfaceConfSigTable": qbAtmInterfaceConfSigTable,
       "qbAtmInterfaceConfSigEntry": qbAtmInterfaceConfSigEntry,
       "qbAtmInterfaceConfSigMode": qbAtmInterfaceConfSigMode,
       "qbAtmInterfaceConfSigSide": qbAtmInterfaceConfSigSide,
       "qbAtmInterfaceConfSigParseMode": qbAtmInterfaceConfSigParseMode,
       "qbAtmInterfaceConfSigAdminStatus": qbAtmInterfaceConfSigAdminStatus,
       "qbAtmInterfaceConfSigSvcMinVci": qbAtmInterfaceConfSigSvcMinVci,
       "qbAtmInterfaceConfSigSvcMaxVci": qbAtmInterfaceConfSigSvcMaxVci,
       "qbAtmInterfaceConfSigSvcMinVpi": qbAtmInterfaceConfSigSvcMinVpi,
       "qbAtmInterfaceConfSigSvcMaxVpi": qbAtmInterfaceConfSigSvcMaxVpi,
       "qbAtmInterfaceConfSigSvpMinVpi": qbAtmInterfaceConfSigSvpMinVpi,
       "qbAtmInterfaceConfSigSvpMaxVpi": qbAtmInterfaceConfSigSvpMaxVpi,
       "qbAtmInterfaceConfSigLastChange": qbAtmInterfaceConfSigLastChange,
       "qbAtmInterfaceConfSigIlmiEnable": qbAtmInterfaceConfSigIlmiEnable,
       "qbAtmPnniNbrPeerTable": qbAtmPnniNbrPeerTable,
       "qbAtmPnniNbrPeerEntry": qbAtmPnniNbrPeerEntry,
       "qbAtmPnniPeerRemoteNodeId": qbAtmPnniPeerRemoteNodeId,
       "qbAtmPnniPeerState": qbAtmPnniPeerState,
       "qbAtmPnniPeerSvccRccIndex": qbAtmPnniPeerSvccRccIndex,
       "qbAtmPnniPeerPortCount": qbAtmPnniPeerPortCount,
       "qbAtmPnniPeerRcvDbSums": qbAtmPnniPeerRcvDbSums,
       "qbAtmPnniPeerXmtDbSums": qbAtmPnniPeerXmtDbSums,
       "qbAtmPnniPeerRcvPtsps": qbAtmPnniPeerRcvPtsps,
       "qbAtmPnniPeerXmtPtsps": qbAtmPnniPeerXmtPtsps,
       "qbAtmPnniPeerRcvPtseReqs": qbAtmPnniPeerRcvPtseReqs,
       "qbAtmPnniPeerXmtPtseReqs": qbAtmPnniPeerXmtPtseReqs,
       "qbAtmPnniPeerRcvPtseAcks": qbAtmPnniPeerRcvPtseAcks,
       "qbAtmPnniPeerXmtPtseAcks": qbAtmPnniPeerXmtPtseAcks,
       "qbAtmPnniNodePglTable": qbAtmPnniNodePglTable,
       "qbAtmPnniNodePglEntry": qbAtmPnniNodePglEntry,
       "qbAtmPnniNodePglLeadershipPriority": qbAtmPnniNodePglLeadershipPriority,
       "qbAtmPnniNodeCfgParentNodeIndex": qbAtmPnniNodeCfgParentNodeIndex,
       "qbAtmPnniNodePglInitTime": qbAtmPnniNodePglInitTime,
       "qbAtmPnniNodePglOverrideDelay": qbAtmPnniNodePglOverrideDelay,
       "qbAtmPnniNodePglReelectTime": qbAtmPnniNodePglReelectTime,
       "qbAtmPnniNodePglState": qbAtmPnniNodePglState,
       "qbAtmPnniNodePreferredPgl": qbAtmPnniNodePreferredPgl,
       "qbAtmPnniNodePeerGroupLeader": qbAtmPnniNodePeerGroupLeader,
       "qbAtmPnniNodePglTimeStamp": qbAtmPnniNodePglTimeStamp,
       "qbAtmPnniNodeActiveParentNodeId": qbAtmPnniNodeActiveParentNodeId,
       "qbAtmPnniNodeTimerTable": qbAtmPnniNodeTimerTable,
       "qbAtmPnniNodeTimerEntry": qbAtmPnniNodeTimerEntry,
       "qbAtmPnniNodePtseHolddown": qbAtmPnniNodePtseHolddown,
       "qbAtmPnniNodeHelloHolddown": qbAtmPnniNodeHelloHolddown,
       "qbAtmPnniNodeHelloInterval": qbAtmPnniNodeHelloInterval,
       "qbAtmPnniNodeHelloInactivityFactor": qbAtmPnniNodeHelloInactivityFactor,
       "qbAtmPnniNodeHlinkInact": qbAtmPnniNodeHlinkInact,
       "qbAtmPnniNodePtseRefreshInterval": qbAtmPnniNodePtseRefreshInterval,
       "qbAtmPnniNodePtseLifetimeFactor": qbAtmPnniNodePtseLifetimeFactor,
       "qbAtmPnniNodeRxmtInterval": qbAtmPnniNodeRxmtInterval,
       "qbAtmPnniNodePeerDelayedAckInterval": qbAtmPnniNodePeerDelayedAckInterval,
       "qbAtmPnniNodeAvcrPm": qbAtmPnniNodeAvcrPm,
       "qbAtmPnniNodeAvcrMt": qbAtmPnniNodeAvcrMt,
       "qbAtmPnniNodeCdvPm": qbAtmPnniNodeCdvPm,
       "qbAtmPnniNodeCtdPm": qbAtmPnniNodeCtdPm,
       "qbAtmPnniLinkTable": qbAtmPnniLinkTable,
       "qbAtmPnniLinkEntry": qbAtmPnniLinkEntry,
       "qbAtmPnniLinkPortId": qbAtmPnniLinkPortId,
       "qbAtmPnniLinkType": qbAtmPnniLinkType,
       "qbAtmPnniLinkHelloState": qbAtmPnniLinkHelloState,
       "qbAtmHiddenVclTable": qbAtmHiddenVclTable,
       "qbAtmHiddenVclEntry": qbAtmHiddenVclEntry,
       "qbAtmHiddenVclName": qbAtmHiddenVclName,
       "qbAtmHiddenVclType": qbAtmHiddenVclType,
       "qbAtmHiddenVclIfIndex": qbAtmHiddenVclIfIndex,
       "qbAtmHiddenVclVtIndex": qbAtmHiddenVclVtIndex,
       "qbAtmSwitchModuleGroup": qbAtmSwitchModuleGroup,
       "qbAtmStatsBuffOverCells": qbAtmStatsBuffOverCells,
       "qbAtmStatsInvalidCells": qbAtmStatsInvalidCells,
       "qbAtmStatsInvUpdateCells": qbAtmStatsInvUpdateCells,
       "qbAtmInterfaceStatTable": qbAtmInterfaceStatTable,
       "qbAtmInterfaceStatEntry": qbAtmInterfaceStatEntry,
       "qbAtmInterfaceStatTxOAMCells": qbAtmInterfaceStatTxOAMCells,
       "qbAtmInterfaceStatRxOAMCells": qbAtmInterfaceStatRxOAMCells,
       "qbAtmInBandMgtTable": qbAtmInBandMgtTable,
       "qbAtmInBandMgtEntry": qbAtmInBandMgtEntry,
       "qbAtmInBandMgtIpAddr": qbAtmInBandMgtIpAddr,
       "qbAtmInBandMgtIpMask": qbAtmInBandMgtIpMask,
       "qbAtmInBandMgtIpIfIndex": qbAtmInBandMgtIpIfIndex,
       "qbAtmInBandMgtNeighborIp": qbAtmInBandMgtNeighborIp,
       "qbAtmInBandMgtIfIndex": qbAtmInBandMgtIfIndex,
       "qbAtmInBandMgtVpi": qbAtmInBandMgtVpi,
       "qbAtmInBandMgtVci": qbAtmInBandMgtVci,
       "qbAtmInBandMgtConnKind": qbAtmInBandMgtConnKind,
       "qbAtmInBandMgtTxTd": qbAtmInBandMgtTxTd,
       "qbAtmInBandMgtRxTd": qbAtmInBandMgtRxTd,
       "qbAtmInBandMgtTargetNsapAddr": qbAtmInBandMgtTargetNsapAddr,
       "qbAtmInBandMgtRowStatus": qbAtmInBandMgtRowStatus,
       "qbAtmTrafficDescriptorTypes": qbAtmTrafficDescriptorTypes,
       "qbAtmPkt": qbAtmPkt,
       "qbAtmConformance": qbAtmConformance,
       "qbAtmCompliances": qbAtmCompliances,
       "qbAtmCompliance": qbAtmCompliance,
       "qbAtmGroups": qbAtmGroups,
       "qbAtmInterfaceConfGroupInfo": qbAtmInterfaceConfGroupInfo,
       "qbAtmTrafficDescrParamGroupInfo": qbAtmTrafficDescrParamGroupInfo,
       "qbAtmVclGroupInfo": qbAtmVclGroupInfo,
       "qbAtmVplGroupInfo": qbAtmVplGroupInfo,
       "qbAtmVcCrossConnectGroupInfo": qbAtmVcCrossConnectGroupInfo,
       "qbAtmVpCrossConnectGroupInfo": qbAtmVpCrossConnectGroupInfo,
       "qbAtmPnniNodeGroupInfo": qbAtmPnniNodeGroupInfo,
       "qbAtmPnniIfGroupInfo": qbAtmPnniIfGroupInfo,
       "qbAtmPnniRouteAddrGroupInfo": qbAtmPnniRouteAddrGroupInfo,
       "qbAtmInterfaceConfSigGroupInfo": qbAtmInterfaceConfSigGroupInfo,
       "qbAtmPnniNbrPeerGroupInfo": qbAtmPnniNbrPeerGroupInfo,
       "qbAtmPnniPglGroupInfo": qbAtmPnniPglGroupInfo,
       "qbAtmPnniTimerGroupInfo": qbAtmPnniTimerGroupInfo,
       "qbAtmPnniLinkGroupInfo": qbAtmPnniLinkGroupInfo,
       "qbAtmInBandMgtGroupInfo": qbAtmInBandMgtGroupInfo,
       "qbAtmBaseGroup": qbAtmBaseGroup,
       "qbAtmF4F5LLID": qbAtmF4F5LLID,
       "qbAtmDefaultPCBE": qbAtmDefaultPCBE}
)
