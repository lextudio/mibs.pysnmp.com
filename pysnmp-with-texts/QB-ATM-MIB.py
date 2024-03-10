"""SNMP MIB module (QB-ATM-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-ATM-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:27 2024
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

(atmTrafficDescrParamEntry,
 atmVclEntry,
 atmVcCrossConnectEntry,
 atmVplEntry,
 atmInterfaceConfEntry,
 atmVpCrossConnectEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry",
    "atmVclEntry",
    "atmVcCrossConnectEntry",
    "atmVplEntry",
    "atmInterfaceConfEntry",
    "atmVpCrossConnectEntry")

(AtmConnKind,
 AtmVcIdentifier,
 AtmVpIdentifier,
 atmNoClpNoScr,
 AtmVorXLastChange,
 AtmServiceCategory,
 AtmAddr,
 AtmTrafficDescrParamIndex,
 AtmVorXOperStatus,
 AtmVorXAdminStatus,
 AtmConnCastType) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmConnKind",
    "AtmVcIdentifier",
    "AtmVpIdentifier",
    "atmNoClpNoScr",
    "AtmVorXLastChange",
    "AtmServiceCategory",
    "AtmAddr",
    "AtmTrafficDescrParamIndex",
    "AtmVorXOperStatus",
    "AtmVorXAdminStatus",
    "AtmConnCastType")

(InterfaceIndexOrZero,
 InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "InterfaceIndex",
    "ifIndex")

(QbPvcConnKind,
 QbEnableStatus) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbPvcConnKind",
    "QbEnableStatus")

(TimeStamp,) = mibBuilder.importSymbols(
    "QBSYS-SYSTEM-MIB",
    "TimeStamp")

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

(Counter64,
 ObjectIdentity,
 IpAddress,
 Gauge32,
 NotificationType,
 Bits,
 TimeTicks,
 ModuleIdentity,
 Counter32,
 Unsigned32,
 Integer32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 iso,
 MibIdentifier) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter64",
    "ObjectIdentity",
    "IpAddress",
    "Gauge32",
    "NotificationType",
    "Bits",
    "TimeTicks",
    "ModuleIdentity",
    "Counter32",
    "Unsigned32",
    "Integer32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "iso",
    "MibIdentifier")

(DisplayString,
 TruthValue,
 TextualConvention,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TruthValue",
    "TextualConvention",
    "RowStatus")


# MODULE-IDENTITY

qbAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7)
)
qbAtmMIB.setLastUpdated("0101022155Z")
if mibBuilder.loadTexts:
    qbAtmMIB.setOrganization("""\
Quantum Bridge Inc.
""")
qbAtmMIB.setContactInfo("""\
mvaysman@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbAtmMIB.setDescription("""\
This module defines additional objects for management of ATM links in Quantum
Bridge devices, above and beyond what is defined in the standard ATM mib, and
proposed drafts.
""")


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

    if mibBuilder.loadTexts:
        description = """\
The ATM administrative weight of the ATM interface used by the PNNI Routing
Control
"""


class QbAtmPnniNodeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )

    if mibBuilder.loadTexts:
        description = """\
Global PNNI Node Id used in the QB PNNI system.
"""


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

    if mibBuilder.loadTexts:
        description = """\
The ATM interface signalling spec.
"""


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

    if mibBuilder.loadTexts:
        description = """\
The state of an instance of the PNNI Hello State machine.
"""


class QbAtmPnniAtmAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )

    if mibBuilder.loadTexts:
        description = """\
The ATM address used by the network entity. The address types are: no address
(0 octets), and NSAP (20 octets).
"""


class QbAtmPnniNodeIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )

    if mibBuilder.loadTexts:
        description = """\
An index that identifies a logical PNNI entity within the managed system. The
distinguished value zero indicates the null instance or no instance in the
qbAtmPnniNodeCfgParentNodeIndex. In all other cases, the distinguished value
zero indicates a logical entity within the switching system that manages routes
only over non-PNNI interfaces. By default, only the node identified by node
index one is created, and all PNNI interfaces are associated with that node.
"""


class QbAtmPnniPeerGroupId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )

    if mibBuilder.loadTexts:
        description = """\
A PNNI peer group ID.
"""


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

    if mibBuilder.loadTexts:
        description = """\
in-progress(1) or success(2) or timeout(3).
"""


class QbF4F5Status(TextualConvention, Bits):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
Definition of F4/F5 OperStatus
"""


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfTable.setDescription("""\
The Quantum Bridge ATM Interface Configuration Table contains extensions to the
ATM Interface Configuration Table, one entry per ATM interface.
""")
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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfEntry.setDescription("""\
An entry in the Quantum ATM Interface Configuration Table. Every ATM interface
contains a corresponding entry in the table.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfPolicingStatus.setDescription("""\
If this object is set to 'enable' the policing is enabled on this interface. If
the object set to 'disable,' the policing is disabled. Note: policing can be
set on the S622 and 155 cards only.
""")
_QbAtmInterfaceConfMaxPvcVpi_Type = Integer32
_QbAtmInterfaceConfMaxPvcVpi_Object = MibTableColumn
qbAtmInterfaceConfMaxPvcVpi = _QbAtmInterfaceConfMaxPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 2),
    _QbAtmInterfaceConfMaxPvcVpi_Type()
)
qbAtmInterfaceConfMaxPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvcVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvcVpi.setDescription("""\
This object indicates the maximum value of VPI that can be used to create a VC
on a given ATM native interface.
""")
_QbAtmInterfaceConfMinPvcVpi_Type = Integer32
_QbAtmInterfaceConfMinPvcVpi_Object = MibTableColumn
qbAtmInterfaceConfMinPvcVpi = _QbAtmInterfaceConfMinPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 3),
    _QbAtmInterfaceConfMinPvcVpi_Type()
)
qbAtmInterfaceConfMinPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvcVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvcVpi.setDescription("""\
This object indicates the minimum value of VPI that can be used to create a VC
on a given ATM native interface.
""")
_QbAtmInterfaceConfMaxPvcVci_Type = Integer32
_QbAtmInterfaceConfMaxPvcVci_Object = MibTableColumn
qbAtmInterfaceConfMaxPvcVci = _QbAtmInterfaceConfMaxPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 4),
    _QbAtmInterfaceConfMaxPvcVci_Type()
)
qbAtmInterfaceConfMaxPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvcVci.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvcVci.setDescription("""\
This object indicates the maximum value of VCI that can be used to create a VC
on a given ATM native interface.
""")
_QbAtmInterfaceConfMinPvcVci_Type = Integer32
_QbAtmInterfaceConfMinPvcVci_Object = MibTableColumn
qbAtmInterfaceConfMinPvcVci = _QbAtmInterfaceConfMinPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 5),
    _QbAtmInterfaceConfMinPvcVci_Type()
)
qbAtmInterfaceConfMinPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvcVci.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvcVci.setDescription("""\
This object indicates the minimum value of VCI that can be used to create a VC
on a given ATM native interface.
""")
_QbAtmInterfaceConfMaxPvpVpi_Type = Integer32
_QbAtmInterfaceConfMaxPvpVpi_Object = MibTableColumn
qbAtmInterfaceConfMaxPvpVpi = _QbAtmInterfaceConfMaxPvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 6),
    _QbAtmInterfaceConfMaxPvpVpi_Type()
)
qbAtmInterfaceConfMaxPvpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvpVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMaxPvpVpi.setDescription("""\
This object indicates the maximum value of VPI that can be used to create a VP
on a given ATM native interface.
""")
_QbAtmInterfaceConfMinPvpVpi_Type = Integer32
_QbAtmInterfaceConfMinPvpVpi_Object = MibTableColumn
qbAtmInterfaceConfMinPvpVpi = _QbAtmInterfaceConfMinPvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 1, 1, 7),
    _QbAtmInterfaceConfMinPvpVpi_Type()
)
qbAtmInterfaceConfMinPvpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvpVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfMinPvpVpi.setDescription("""\
This object indicates the minimum value of VPI that can be used to create a VP
on a given ATM native interface.
""")
_QbAtmTrafficDescrParamTable_Object = MibTable
qbAtmTrafficDescrParamTable = _QbAtmTrafficDescrParamTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamTable.setDescription("""\
The Quantum Bridge ATM Traffic Descriptor Table contains extensions to the ATM
Traffic Descriptor Table.
""")
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
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamEntry.setDescription("""\
An entry in the Quantum Bridge ATM Traffic Descriptor Table.
""")


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
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamName.setDescription("""\
A textual description of the traffic descriptor.
""")


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
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamDefault.setDescription("""\
The object indicates whether or not this is a default traffic descriptor.
Traffic descriptor with indexes from 1 to 20 are default traffic descriptors
and cannot be deleted.
""")
_QbAtmVclTable_Object = MibTable
qbAtmVclTable = _QbAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    qbAtmVclTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclTable.setDescription("""\
The Quantum Bridge Table contains an extension to the atmVclConnectTable, An
entry in this table models VCLs.
""")
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
if mibBuilder.loadTexts:
    qbAtmVclEntry.setDescription("""\
An entry in the QB ATM atmVclConnectTable.
""")


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
if mibBuilder.loadTexts:
    qbAtmVclLoopback.setDescription("""\
Enable loopback on this ATM VCL
""")


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
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackInsert.setDescription("""\
This is a loopback Insert object for LLID. Start loopback Insert by setting
this to an LLID value.
""")
_QbAtmVclF4F5LoopbackStatus_Type = QbF4F5LoopbackStatus
_QbAtmVclF4F5LoopbackStatus_Object = MibTableColumn
qbAtmVclF4F5LoopbackStatus = _QbAtmVclF4F5LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 3),
    _QbAtmVclF4F5LoopbackStatus_Type()
)
qbAtmVclF4F5LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackStatus.setDescription("""\
Status of loopback Insert command: in-progress, success, timeout.
""")
_QbAtmVclF4F5LoopbackTimestamp_Type = TimeStamp
_QbAtmVclF4F5LoopbackTimestamp_Object = MibTableColumn
qbAtmVclF4F5LoopbackTimestamp = _QbAtmVclF4F5LoopbackTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 4),
    _QbAtmVclF4F5LoopbackTimestamp_Type()
)
qbAtmVclF4F5LoopbackTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclF4F5LoopbackTimestamp.setDescription("""\
Value of sysUptime when last Insert completed.
""")
_QbAtmVclMgmtIpAddr_Type = IpAddress
_QbAtmVclMgmtIpAddr_Object = MibTableColumn
qbAtmVclMgmtIpAddr = _QbAtmVclMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 5),
    _QbAtmVclMgmtIpAddr_Type()
)
qbAtmVclMgmtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclMgmtIpAddr.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclMgmtIpAddr.setDescription("""\
Active IP Address for in-band Management SNMP of this chassis.
""")
_QbAtmVclMgmtIpMask_Type = IpAddress
_QbAtmVclMgmtIpMask_Object = MibTableColumn
qbAtmVclMgmtIpMask = _QbAtmVclMgmtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 6),
    _QbAtmVclMgmtIpMask_Type()
)
qbAtmVclMgmtIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclMgmtIpMask.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclMgmtIpMask.setDescription("""\
This is the IP network mask associated with the in-band Management interface.
""")
_QbAtmVclMgmtNeighborIP_Type = IpAddress
_QbAtmVclMgmtNeighborIP_Object = MibTableColumn
qbAtmVclMgmtNeighborIP = _QbAtmVclMgmtNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 7),
    _QbAtmVclMgmtNeighborIP_Type()
)
qbAtmVclMgmtNeighborIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmVclMgmtNeighborIP.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclMgmtNeighborIP.setDescription("""\
This is the neighbor IP address associated with the in-band Management
interface.
""")
_QbAtmVclConnKind_Type = QbPvcConnKind
_QbAtmVclConnKind_Object = MibTableColumn
qbAtmVclConnKind = _QbAtmVclConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 8),
    _QbAtmVclConnKind_Type()
)
qbAtmVclConnKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclConnKind.setDescription("""\
The VCL connection type.
""")
_QbAtmVclF4F5TxStatus_Type = QbF4F5Status
_QbAtmVclF4F5TxStatus_Object = MibTableColumn
qbAtmVclF4F5TxStatus = _QbAtmVclF4F5TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 9),
    _QbAtmVclF4F5TxStatus_Type()
)
qbAtmVclF4F5TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5TxStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclF4F5TxStatus.setDescription("""\
The transmitted OAM status for the PVC.
""")
_QbAtmVclF4F5TxLastChange_Type = TimeStamp
_QbAtmVclF4F5TxLastChange_Object = MibTableColumn
qbAtmVclF4F5TxLastChange = _QbAtmVclF4F5TxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 10),
    _QbAtmVclF4F5TxLastChange_Type()
)
qbAtmVclF4F5TxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5TxLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclF4F5TxLastChange.setDescription("""\
The value of sysUPtime when qbAtmVclF4F5TxStatus last changed.
""")
_QbAtmVclF4F5RxStatus_Type = QbF4F5Status
_QbAtmVclF4F5RxStatus_Object = MibTableColumn
qbAtmVclF4F5RxStatus = _QbAtmVclF4F5RxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 11),
    _QbAtmVclF4F5RxStatus_Type()
)
qbAtmVclF4F5RxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5RxStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclF4F5RxStatus.setDescription("""\
The received OAM status of the PVC.
""")
_QbAtmVclF4F5RxLastChange_Type = TimeStamp
_QbAtmVclF4F5RxLastChange_Object = MibTableColumn
qbAtmVclF4F5RxLastChange = _QbAtmVclF4F5RxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 3, 1, 12),
    _QbAtmVclF4F5RxLastChange_Type()
)
qbAtmVclF4F5RxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVclF4F5RxLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVclF4F5RxLastChange.setDescription("""\
The value of sysUPtime when qbAtmVclF4F5TxStatus last changed.
""")
_QbAtmVplTable_Object = MibTable
qbAtmVplTable = _QbAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    qbAtmVplTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplTable.setDescription("""\
The Quantum Bridge Table contains an extension to the atmVclConnectTable, An
entry in this table models VPLs.
""")
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
if mibBuilder.loadTexts:
    qbAtmVplEntry.setDescription("""\
An entry in the QB ATM qbAtmVpTable.
""")


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
if mibBuilder.loadTexts:
    qbAtmVplLoopback.setDescription("""\
Enable loopback on this ATM VPL
""")


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
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackInsert.setDescription("""\
This is a loopback Insert object for LLID. Start loopback Insert by setting
this to an LLID value.
""")
_QbAtmVplF4F5LoopbackStatus_Type = QbF4F5LoopbackStatus
_QbAtmVplF4F5LoopbackStatus_Object = MibTableColumn
qbAtmVplF4F5LoopbackStatus = _QbAtmVplF4F5LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 3),
    _QbAtmVplF4F5LoopbackStatus_Type()
)
qbAtmVplF4F5LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackStatus.setDescription("""\
Status of loopback Insert command: in-progress, success, timeout.
""")
_QbAtmVplF4F5LoopbackTimestamp_Type = TimeStamp
_QbAtmVplF4F5LoopbackTimestamp_Object = MibTableColumn
qbAtmVplF4F5LoopbackTimestamp = _QbAtmVplF4F5LoopbackTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 4),
    _QbAtmVplF4F5LoopbackTimestamp_Type()
)
qbAtmVplF4F5LoopbackTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplF4F5LoopbackTimestamp.setDescription("""\
Value of sysUptime when last Insert completed.
""")
_QbAtmVplF4F5TxStatus_Type = QbF4F5Status
_QbAtmVplF4F5TxStatus_Object = MibTableColumn
qbAtmVplF4F5TxStatus = _QbAtmVplF4F5TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 5),
    _QbAtmVplF4F5TxStatus_Type()
)
qbAtmVplF4F5TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5TxStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplF4F5TxStatus.setDescription("""\
The transmitted OAM status for the PVP.
""")
_QbAtmVplF4F5TxLastChange_Type = TimeStamp
_QbAtmVplF4F5TxLastChange_Object = MibTableColumn
qbAtmVplF4F5TxLastChange = _QbAtmVplF4F5TxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 6),
    _QbAtmVplF4F5TxLastChange_Type()
)
qbAtmVplF4F5TxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5TxLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplF4F5TxLastChange.setDescription("""\
The value of sysUPtime when qbAtmVclF4F5TxStatus last changed.
""")
_QbAtmVplF4F5RxStatus_Type = QbF4F5Status
_QbAtmVplF4F5RxStatus_Object = MibTableColumn
qbAtmVplF4F5RxStatus = _QbAtmVplF4F5RxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 7),
    _QbAtmVplF4F5RxStatus_Type()
)
qbAtmVplF4F5RxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5RxStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplF4F5RxStatus.setDescription("""\
The received OAM status of the PVP.
""")
_QbAtmVplF4F5RxLastChange_Type = TimeStamp
_QbAtmVplF4F5RxLastChange_Object = MibTableColumn
qbAtmVplF4F5RxLastChange = _QbAtmVplF4F5RxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 4, 1, 8),
    _QbAtmVplF4F5RxLastChange_Type()
)
qbAtmVplF4F5RxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmVplF4F5RxLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVplF4F5RxLastChange.setDescription("""\
The value of sysUPtime when qbAtmVclF4F5TxStatus last changed.
""")
_QbAtmVcCrossConnectTable_Object = MibTable
qbAtmVcCrossConnectTable = _QbAtmVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5)
)
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectTable.setDescription("""\
The Quantum Bridge Table contains an extension to the atmVcCrossConnectTable,
An entry in this table models two cross-connected VCLs.
""")
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
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectEntry.setDescription("""\
An entry in the QB ATM atmVcCrossConnectTable.
""")


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
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectName.setDescription("""\
A textual description for the cross connect.
""")
_QbAtmVcCrossConnectRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVcCrossConnectRxTrafficDescrIndex_Object = MibTableColumn
qbAtmVcCrossConnectRxTrafficDescrIndex = _QbAtmVcCrossConnectRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5, 1, 2),
    _QbAtmVcCrossConnectRxTrafficDescrIndex_Type()
)
qbAtmVcCrossConnectRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VCLs cross-connect.
""")
_QbAtmVcCrossConnectTxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVcCrossConnectTxTrafficDescrIndex_Object = MibTableColumn
qbAtmVcCrossConnectTxTrafficDescrIndex = _QbAtmVcCrossConnectTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 5, 1, 3),
    _QbAtmVcCrossConnectTxTrafficDescrIndex_Type()
)
qbAtmVcCrossConnectTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row of the ATM Traffic Descriptor Table
which applies to the transmit direction of this VCLs cross-connect
""")
_QbAtmVpCrossConnectTable_Object = MibTable
qbAtmVpCrossConnectTable = _QbAtmVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectTable.setDescription("""\
The Quantum Bridge Table contains an extension to the atmVpCrossConnectTable,
An entry in this table models two cross-connected VPLs.
""")
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
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectEntry.setDescription("""\
An entry in the QB ATM atmVpCrossConnectTable.
""")


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
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectName.setDescription("""\
A textual description for the cross connect.
""")
_QbAtmVpCrossConnectRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVpCrossConnectRxTrafficDescrIndex_Object = MibTableColumn
qbAtmVpCrossConnectRxTrafficDescrIndex = _QbAtmVpCrossConnectRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6, 1, 2),
    _QbAtmVpCrossConnectRxTrafficDescrIndex_Type()
)
qbAtmVpCrossConnectRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VPLs cross-connect.
""")
_QbAtmVpCrossConnectTxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbAtmVpCrossConnectTxTrafficDescrIndex_Object = MibTableColumn
qbAtmVpCrossConnectTxTrafficDescrIndex = _QbAtmVpCrossConnectTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 6, 1, 3),
    _QbAtmVpCrossConnectTxTrafficDescrIndex_Type()
)
qbAtmVpCrossConnectTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row of the ATM Traffic Descriptor Table
which applies to the transmit direction of this VPLs cross-connect
""")
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
if mibBuilder.loadTexts:
    qbAtmPnniNodeTable.setDescription("""\
The QbAtmpnniNodeTable contains attributes that affect the operation of a PNNI
logical node. There is a single row in this table for each PNNI peer group that
the managed system is expected or eligible to become a member of.
""")
_QbAtmPnniNodeEntry_Object = MibTableRow
qbAtmPnniNodeEntry = _QbAtmPnniNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1)
)
qbAtmPnniNodeEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmPnniNodeIndex"),
)
if mibBuilder.loadTexts:
    qbAtmPnniNodeEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeEntry.setDescription("""\
An entry in the table, containing information about a PNNI logical node in this
switching system.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeIndex.setDescription("""\
A value assigned to a node in this switching system that uniquely identifies it
in the MIB.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeNetAddrPrefix.setDescription("""\
Indicates the Network Prefix to use for the ATM End System Address. The value
is 13 bytes long, and is specified in the hexadecimal format. If less than 13
bytes(26 chars) are received, the agent appends trailing zero's. The object can
be set to ''h, if PNNI protocol is desirable on all interfaces.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeEndSysId.setDescription("""\
Indicates the End System Identifier for ATM End System Address. The value is 7
bytes long, and is specified in the hexadecimal format. The object can be set
to ''h, if PNNI protocol is desirable on all interfaces.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeLevel.setDescription("""\
The level of PNNI hierarchy at which this node exists. This attribute is used
to determine the default node ID and the default peer group ID for this node.
This object may only be written when pnniNodeAdminStatus has the value down.
""")
_QbAtmPnniNodeRowStatus_Type = RowStatus
_QbAtmPnniNodeRowStatus_Object = MibTableColumn
qbAtmPnniNodeRowStatus = _QbAtmPnniNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 5),
    _QbAtmPnniNodeRowStatus_Type()
)
qbAtmPnniNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeRowStatus.setDescription("""\
To create, delete, activate and de-activate a Node. Setting this object to
createAndGo(4) causes the corresponding row to be created. Setting this object
to destroy(6) causes the corresponding row to be deleted. Note that --
currently-- only a single instance of a row can be created in this table.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeOperStatus.setDescription("""\
Indicates the Operational Status of the PNNI Node. For Logical Group Nodes, the
Operational Status will be up only if the child becomes the PGL.
""")
_QbAtmPnniNodeAtmAddress_Type = QbAtmPnniAtmAddr
_QbAtmPnniNodeAtmAddress_Object = MibTableColumn
qbAtmPnniNodeAtmAddress = _QbAtmPnniNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 7),
    _QbAtmPnniNodeAtmAddress_Type()
)
qbAtmPnniNodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAtmAddress.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAtmAddress.setReference("""\
ATM Forum PNNI 1.0 Section 5.2.2
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAtmAddress.setDescription("""\
This node's ATM End System Address. Remote systems wishing to exchange PNNI
protocol packets with this node should direct packets or calls to this address.
The current Qb implementation does not support writing this value.
""")
_QbAtmPnniNodePeerGroupId_Type = QbAtmPnniPeerGroupId
_QbAtmPnniNodePeerGroupId_Object = MibTableColumn
qbAtmPnniNodePeerGroupId = _QbAtmPnniNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 1, 1, 8),
    _QbAtmPnniNodePeerGroupId_Type()
)
qbAtmPnniNodePeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupId.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupId.setReference("""\
ATM Forum PNNI 1.0 Section 5.3.2, Annex F
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupId.setDescription("""\
The Peer Group Identifier of the peer group that the given node is to become a
member of.
""")
_QbAtmPnniIfTable_Object = MibTable
qbAtmPnniIfTable = _QbAtmPnniIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2)
)
if mibBuilder.loadTexts:
    qbAtmPnniIfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniIfTable.setDescription("""\
The qbAtmPnniIfTable contains the attributes necessary to configure a physical
interface on a switching system capable of being used for PNNI routing. An
ifIndex is used as the instance ID to uniquely identify the interface on the
local switching system. This index has the same value as the ifIndex object
defined in RFC 1573 for the same interface, since this table correlates with
the ifTable in RFC 1573. One row in this table is created by the managed system
for each row in the ifTable that has an ifType of atm(37) or atmLogical(80).
""")
_QbAtmPnniIfEntry_Object = MibTableRow
qbAtmPnniIfEntry = _QbAtmPnniIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 2, 1)
)
qbAtmPnniIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbAtmPnniIfEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniIfEntry.setDescription("""\
An entry in the table, containing PNNI specific interface information in this
switching system.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfNodeIndex.setDescription("""\
Identifies the node within the switching system that the interface is directly
attached to. Note: For this release this value can be set only to 1.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightCbr.setDescription("""\
The administrative weight of this interface for the constant bit rate service
category.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightRtVbr.setDescription("""\
The administrative weight of this interface for the real-time variable bit rate
service category.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightNrtVbr.setDescription("""\
The administrative weight of this interface for the non-real-time variable bit
rate service category.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightAbr.setDescription("""\
The administrative weight of this interface for the available bit rate service
category.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfAdmWeightUbr.setDescription("""\
The administrative weight of this interface for the unspecified bit rate
service category.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfRccServiceCategory.setDescription("""\
The service category used for the PNNI routing control channel (VCI=18) on this
interface.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfRccTrafficDescrIndex.setDescription("""\
The traffic descriptor index referring to the entry in the
atmTrafficDescrParamTable defined in RFC 1695 that specifies the traffic
allocation for the PNNI routing control channel (VCI=18) on this interface.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniIfPolicingStatus.setDescription("""\
If this object is set to enable, the policing is enabled on this interface. If
the object is set to 'disable' the policing is disabled.
""")
_QbAtmPnniRouteAddrTable_Object = MibTable
qbAtmPnniRouteAddrTable = _QbAtmPnniRouteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3)
)
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrTable.setDescription("""\
A table containing all the attributes necessary to determine what the PNNI
entity believes is reachable in terms of ATM End System Addresses, and to
determine which nodes are advertising this reachability. This table is also
used to configure static routes to reachable address prefixes. The local node
index that receives the reachability information, reachable address, address
prefix length, and an index that distinguishes between multiple listings of
connectivity to a given address prefix from a given local node are combined to
form an instance ID for this object.
""")
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
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrEntry.setDescription("""\
An entry in the table, containing information about a reachable address prefix.
""")
_QbAtmPnniRouteAddrIfIndex_Type = InterfaceIndex
_QbAtmPnniRouteAddrIfIndex_Object = MibTableColumn
qbAtmPnniRouteAddrIfIndex = _QbAtmPnniRouteAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 1),
    _QbAtmPnniRouteAddrIfIndex_Type()
)
qbAtmPnniRouteAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrIfIndex.setDescription("""\
The local interface over which the reachable address can be reached.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrAddress.setDescription("""\
The value of the ATM End System Address prefix.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrPrefixLength.setDescription("""\
Indicates the number of bits to be applied to the ATM End System Address
prefix.
""")
_QbAtmPnniRouteAddrRowStatus_Type = RowStatus
_QbAtmPnniRouteAddrRowStatus_Object = MibTableColumn
qbAtmPnniRouteAddrRowStatus = _QbAtmPnniRouteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 3, 1, 4),
    _QbAtmPnniRouteAddrRowStatus_Type()
)
qbAtmPnniRouteAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrRowStatus.setDescription("""\
To create, delete, activate and de-activate a reachable address prefix.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrProto.setDescription("""\
This object indicates the Routing mechanism through which the connectivity from
the advertising node to the reachable address prefix was learned.
""")
_QbAtmInterfaceConfSigTable_Object = MibTable
qbAtmInterfaceConfSigTable = _QbAtmInterfaceConfSigTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4)
)
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigTable.setDescription("""\
This table contains ATM local interface configuration parameters, one entry per
ATM interface port.
""")
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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigEntry.setDescription("""\
 This list contains additonal ATM interface configuration parameters and state
variables.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigMode.setDescription("""\
The type of ATM interface which is either a UNI (User to Network), PNNI or
IISP. To modify the qbAtmInterfaceConfSignType, ifAdminStatus has to be down.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSide.setDescription("""\
The side of ATM interface which is either a user or network side. NotApplicable
value implies that qbAtmInterfaceConfSignType is other than uni or iisp.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigParseMode.setDescription("""\
Indicates to the signalling stack to use strict parsing of the INformation
Elements (IEs) within signalling messages. This parameter is set to 'on' for
conformance testing. For systems that do not test conformance it is recommended
to set the object to 'off'.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigAdminStatus.setDescription("""\
Enable/Disable signalling/sscop on this interface. To modify the
qbAtmInterfaceConfSignAdminStatus, ifAdminStatus has to be down.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMinVci.setDescription("""\
The minimum value of SVC connection for vci.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMaxVci.setDescription("""\
The maximum value of SVC connection for vci.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMinVpi.setDescription("""\
The minimum value of SVC connection for vpi.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvcMaxVpi.setDescription("""\
The maximum value of SVC connection for vpi.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvpMinVpi.setDescription("""\
The minimum value of SVP connection for vpi.
""")


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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigSvpMaxVpi.setDescription("""\
The maximum value of SVP connection for vpi.
""")
_QbAtmInterfaceConfSigLastChange_Type = AtmVorXLastChange
_QbAtmInterfaceConfSigLastChange_Object = MibTableColumn
qbAtmInterfaceConfSigLastChange = _QbAtmInterfaceConfSigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 11),
    _QbAtmInterfaceConfSigLastChange_Type()
)
qbAtmInterfaceConfSigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigLastChange.setDescription("""\
The value of sysUpTime at the time this interface changed its current
administrative state.
""")
_QbAtmInterfaceConfSigIlmiEnable_Type = Boolean
_QbAtmInterfaceConfSigIlmiEnable_Object = MibTableColumn
qbAtmInterfaceConfSigIlmiEnable = _QbAtmInterfaceConfSigIlmiEnable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 4, 1, 12),
    _QbAtmInterfaceConfSigIlmiEnable_Type()
)
qbAtmInterfaceConfSigIlmiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigIlmiEnable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigIlmiEnable.setDescription("""\
Can be enabled only if signaling is configured. ILMI is enabled by default when
signaling is configured on the system and the user may enter the disable option
.
""")
_QbAtmPnniNbrPeerTable_Object = MibTable
qbAtmPnniNbrPeerTable = _QbAtmPnniNbrPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5)
)
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerTable.setReference("""\
ATM Forum PNNI 1.0 Sections 5.7, 5.8
""")
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerTable.setDescription("""\
The qbAtmPnniNbrPeer Object contains all the attributes necessary to describe
the relationship a node in this switching system has with a neighboring node
within the same peer group. A concatenation of the Node Identifier of the node
within the local switching system and the neighboring peer's Node Identifier is
used to form the instance ID for this object. The entire qbAtmPnniNbrPeer
object is read-only, reflecting the fact that neighboring peers are discovered
dynamically by the PNNI protocol rather than configured.
""")
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
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerEntry.setReference("""\
ATM Forum PNNI 1.0 Sections 5.7, 5.8
""")
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerEntry.setDescription("""\
An entry in the table, containing information about this node's relationship
with a neighboring peer node.
""")
_QbAtmPnniPeerRemoteNodeId_Type = QbAtmPnniNodeId
_QbAtmPnniPeerRemoteNodeId_Object = MibTableColumn
qbAtmPnniPeerRemoteNodeId = _QbAtmPnniPeerRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 1),
    _QbAtmPnniPeerRemoteNodeId_Type()
)
qbAtmPnniPeerRemoteNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRemoteNodeId.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRemoteNodeId.setDescription("""\
The Node Identifier of the neighboring peer node.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniPeerState.setReference("""\
ATM Forum PNNI 1.0 Section 5.7.2
""")
if mibBuilder.loadTexts:
    qbAtmPnniPeerState.setDescription("""\
Indicates the state of this node's Neighboring Peer State Machine associated
with qbAtmPnniPeerRemoteNodeId.
""")
_QbAtmPnniPeerSvccRccIndex_Type = Integer32
_QbAtmPnniPeerSvccRccIndex_Object = MibTableColumn
qbAtmPnniPeerSvccRccIndex = _QbAtmPnniPeerSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 3),
    _QbAtmPnniPeerSvccRccIndex_Type()
)
qbAtmPnniPeerSvccRccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerSvccRccIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerSvccRccIndex.setDescription("""\
Identifies the SVCC-based RCC being used to communicate with the neighboring
peer if one exists. If both the local node and the neighboring peer node are
lowest-level nodes, this attribute is set to zero.
""")
_QbAtmPnniPeerPortCount_Type = Integer32
_QbAtmPnniPeerPortCount_Object = MibTableColumn
qbAtmPnniPeerPortCount = _QbAtmPnniPeerPortCount_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 4),
    _QbAtmPnniPeerPortCount_Type()
)
qbAtmPnniPeerPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerPortCount.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerPortCount.setDescription("""\
A count of the total number of ports that connect to the neighboring peer. If
the neighboring peer only communicates via an SVCC-based RCC, the value of this
attribute is set to zero. Otherwise it is set to the total number of ports to
the neighboring peer in the Hello state 2-WayInside.
""")
_QbAtmPnniPeerRcvDbSums_Type = Counter32
_QbAtmPnniPeerRcvDbSums_Object = MibTableColumn
qbAtmPnniPeerRcvDbSums = _QbAtmPnniPeerRcvDbSums_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 5),
    _QbAtmPnniPeerRcvDbSums_Type()
)
qbAtmPnniPeerRcvDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvDbSums.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvDbSums.setDescription("""\
A count of the number of Database Summary Packets received from the neighboring
peer.
""")
_QbAtmPnniPeerXmtDbSums_Type = Counter32
_QbAtmPnniPeerXmtDbSums_Object = MibTableColumn
qbAtmPnniPeerXmtDbSums = _QbAtmPnniPeerXmtDbSums_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 6),
    _QbAtmPnniPeerXmtDbSums_Type()
)
qbAtmPnniPeerXmtDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtDbSums.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtDbSums.setDescription("""\
A count of the number of Database Summary Packets transmitted to the
neighboring peer.
""")
_QbAtmPnniPeerRcvPtsps_Type = Counter32
_QbAtmPnniPeerRcvPtsps_Object = MibTableColumn
qbAtmPnniPeerRcvPtsps = _QbAtmPnniPeerRcvPtsps_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 7),
    _QbAtmPnniPeerRcvPtsps_Type()
)
qbAtmPnniPeerRcvPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtsps.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtsps.setDescription("""\
A count of the number of PTSPs received from the neighboring peer.
""")
_QbAtmPnniPeerXmtPtsps_Type = Counter32
_QbAtmPnniPeerXmtPtsps_Object = MibTableColumn
qbAtmPnniPeerXmtPtsps = _QbAtmPnniPeerXmtPtsps_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 8),
    _QbAtmPnniPeerXmtPtsps_Type()
)
qbAtmPnniPeerXmtPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtsps.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtsps.setDescription("""\
A count of the number of PTSPs (re)transmitted to the neighboring peer.
""")
_QbAtmPnniPeerRcvPtseReqs_Type = Counter32
_QbAtmPnniPeerRcvPtseReqs_Object = MibTableColumn
qbAtmPnniPeerRcvPtseReqs = _QbAtmPnniPeerRcvPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 9),
    _QbAtmPnniPeerRcvPtseReqs_Type()
)
qbAtmPnniPeerRcvPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtseReqs.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtseReqs.setDescription("""\
A count of the number of PTSE Request packets received from the neighboring
peer.
""")
_QbAtmPnniPeerXmtPtseReqs_Type = Counter32
_QbAtmPnniPeerXmtPtseReqs_Object = MibTableColumn
qbAtmPnniPeerXmtPtseReqs = _QbAtmPnniPeerXmtPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 10),
    _QbAtmPnniPeerXmtPtseReqs_Type()
)
qbAtmPnniPeerXmtPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtseReqs.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtseReqs.setDescription("""\
A count of the number of PTSE Request packets transmitted to the neighboring
peer.
""")
_QbAtmPnniPeerRcvPtseAcks_Type = Counter32
_QbAtmPnniPeerRcvPtseAcks_Object = MibTableColumn
qbAtmPnniPeerRcvPtseAcks = _QbAtmPnniPeerRcvPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 11),
    _QbAtmPnniPeerRcvPtseAcks_Type()
)
qbAtmPnniPeerRcvPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtseAcks.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerRcvPtseAcks.setDescription("""\
A count of the number of PTSE Ack packets received from the neighboring peer.
""")
_QbAtmPnniPeerXmtPtseAcks_Type = Counter32
_QbAtmPnniPeerXmtPtseAcks_Object = MibTableColumn
qbAtmPnniPeerXmtPtseAcks = _QbAtmPnniPeerXmtPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 5, 1, 12),
    _QbAtmPnniPeerXmtPtseAcks_Type()
)
qbAtmPnniPeerXmtPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtseAcks.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniPeerXmtPtseAcks.setDescription("""\
A count of the number of PTSE Ack packets transmitted to the neighboring peer.
""")
_QbAtmPnniNodePglTable_Object = MibTable
qbAtmPnniNodePglTable = _QbAtmPnniNodePglTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6)
)
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTable.setReference("""\
ATM Forum PNNI 1.0 Section 5.10.1
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTable.setDescription("""\
Peer group leader election information for a PNNI node in this switching
system.
""")
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
if mibBuilder.loadTexts:
    qbAtmPnniNodePglEntry.setReference("""\
ATM Forum PNNI 1.0 Section 5.10.1
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglEntry.setDescription("""\
An entry in the table, containing PGL election information of a PNNI logical
node in this switching system.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePglLeadershipPriority.setReference("""\
ATM Forum PNNI 1.0 Section 5.10.1.2
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglLeadershipPriority.setDescription("""\
The Leadership priority value this node should advertise in its nodal
information group for the given peer group. Only the value zero can be used
with nodes that are not PGL/LGN capable. If there is no configured parent node
index or no corresponding entry in the pnniNodeTable, then the advertised
leadership priority is zero regardless of this value.
""")
_QbAtmPnniNodeCfgParentNodeIndex_Type = Integer32
_QbAtmPnniNodeCfgParentNodeIndex_Object = MibTableColumn
qbAtmPnniNodeCfgParentNodeIndex = _QbAtmPnniNodeCfgParentNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 2),
    _QbAtmPnniNodeCfgParentNodeIndex_Type()
)
qbAtmPnniNodeCfgParentNodeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCfgParentNodeIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCfgParentNodeIndex.setReference("""\
ATM Forum PNNI 1.0 Annex F
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCfgParentNodeIndex.setDescription("""\
The local node index used to identify the node that will represent this peer
group at the next higher level of hierarchy, if this node becomes peer group
leader. The value 0 indicates that there is no parent node.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePglInitTime.setReference("""\
ATM Forum PNNI 1.0 Annex G PGLInitTime
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglInitTime.setDescription("""\
The amount of time in seconds this node will delay advertising its choice of
preferred PGL after having initialized operation and reached the full state
with at least one neighbor in the peer group.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePglOverrideDelay.setReference("""\
ATM Forum PNNI 1.0 Annex G OverrideDelay
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglOverrideDelay.setDescription("""\
The amount of time in seconds a node will wait for itself to be declared the
preferred PGL by unanimous agreement among its peers. In the absence of
unanimous agreement this will be the amount of time that will pass before this
node considers a two thirds majority as sufficient agreement to declare itself
peer group leader, abandoning the attempt to get unanimous agreement.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePglReelectTime.setReference("""\
ATM Forum PNNI 1.0 Annex G ReElectionInterval
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglReelectTime.setDescription("""\
The amount of time in seconds after losing connectivity to the current peer
group leader, that this node will wait before re-starting the process of
electing a new peer group leader.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePglState.setReference("""\
ATM Forum PNNI 1.0 Section 5.10.1.1.2
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglState.setDescription("""\
Indicates the state that this node is in with respect to the Peer Group Leader
election that takes place in the node's peer group. The values are enumerated
in the Peer Group Leader State Machine.
""")
_QbAtmPnniNodePreferredPgl_Type = QbAtmPnniNodeId
_QbAtmPnniNodePreferredPgl_Object = MibTableColumn
qbAtmPnniNodePreferredPgl = _QbAtmPnniNodePreferredPgl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 7),
    _QbAtmPnniNodePreferredPgl_Type()
)
qbAtmPnniNodePreferredPgl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePreferredPgl.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePreferredPgl.setReference("""\
ATM Forum PNNI 1.0 Section 5.10.1.1.6
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePreferredPgl.setDescription("""\
The Node ID of the node which the local node believes should be or become the
peer group leader. This is also the value the local node is currently
advertising in the `Preferred Peer Group Leader Node ID' field of its nodal
information group within the given peer group. If a Preferred PGL has not been
chosen, this attribute's value is set to (all) zero(s).
""")
_QbAtmPnniNodePeerGroupLeader_Type = QbAtmPnniNodeId
_QbAtmPnniNodePeerGroupLeader_Object = MibTableColumn
qbAtmPnniNodePeerGroupLeader = _QbAtmPnniNodePeerGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 8),
    _QbAtmPnniNodePeerGroupLeader_Type()
)
qbAtmPnniNodePeerGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupLeader.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerGroupLeader.setDescription("""\
The Node Identifier of the node which is currently operating as peer group
leader of the peer group this node belongs to. If a PGL has not been elected,
this attribute's value is set to (all) zero(s).
""")
_QbAtmPnniNodePglTimeStamp_Type = TimeStamp
_QbAtmPnniNodePglTimeStamp_Object = MibTableColumn
qbAtmPnniNodePglTimeStamp = _QbAtmPnniNodePglTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 9),
    _QbAtmPnniNodePglTimeStamp_Type()
)
qbAtmPnniNodePglTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodePglTimeStamp.setDescription("""\
The time at which the current Peer Group Leader established itself.
""")
_QbAtmPnniNodeActiveParentNodeId_Type = QbAtmPnniNodeId
_QbAtmPnniNodeActiveParentNodeId_Object = MibTableColumn
qbAtmPnniNodeActiveParentNodeId = _QbAtmPnniNodeActiveParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 6, 1, 10),
    _QbAtmPnniNodeActiveParentNodeId_Type()
)
qbAtmPnniNodeActiveParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniNodeActiveParentNodeId.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeActiveParentNodeId.setDescription("""\
The Node Identifier value being used by the Peer Group Leader to represent this
peer group at the next higher level of the hierarchy. If this node is at the
highest level of the hierarchy or if no PGL has yet been elected the PNNI
Protocol Entity sets the value of this attribute to (all) zero(s).
""")
_QbAtmPnniNodeTimerTable_Object = MibTable
qbAtmPnniNodeTimerTable = _QbAtmPnniNodeTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 7)
)
if mibBuilder.loadTexts:
    qbAtmPnniNodeTimerTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniNodeTimerTable.setDescription("""\
A table of initial PNNI timer values and significant change thresholds.
""")
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
if mibBuilder.loadTexts:
    qbAtmPnniNodeTimerEntry.setDescription("""\
An entry in the table, containing initial PNNI timer values and significant
change thresholds of a PNNI logical node in this switching system.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseHolddown.setReference("""\
ATM Forum PNNI 1.0 Annex G MinPTSEInterval
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseHolddown.setDescription("""\
The initial value for the PTSE hold down timer that will be used by the given
node to limit the rate at which it can re-originate PTSEs. It must be a
positive non-zero number.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloHolddown.setReference("""\
ATM Forum PNNI 1.0 Annex G MinHelloInterval
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloHolddown.setDescription("""\
The initial value for the Hello hold down timer that will be used by the given
node to limit the rate at which it sends Hellos. It must be a positive non-zero
number.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInterval.setReference("""\
ATM Forum PNNI 1.0 Annex G HelloInterval
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInterval.setDescription("""\
The initial value for the Hello Timer. In the absence of triggered Hellos, this
node will send one Hello packet on each of its ports on this interval.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInactivityFactor.setReference("""\
ATM Forum PNNI 1.0 Annex G InactivityFactor
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHelloInactivityFactor.setDescription("""\
The value for the Hello Inactivity factor that this node will use to determine
when a neighbor has gone down.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeHlinkInact.setReference("""\
ATM Forum PNNI 1.0 Annex G HorizontalLinkInactivityTime
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeHlinkInact.setDescription("""\
The amount of time a node will continue to advertise a horizontal (logical)
link for which it has not received and processed a LGN Horizontal Link
information group.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseRefreshInterval.setReference("""\
ATM Forum PNNI 1.0 Annex G PTSERefreshInterval
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseRefreshInterval.setDescription("""\
The initial value for the Refresh timer that this node will use to drive
(re-)origination of PTSEs in the absence of triggered updates.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseLifetimeFactor.setReference("""\
ATM Forum PNNI 1.0 Annex G PTSELifetimeFactor
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePtseLifetimeFactor.setDescription("""\
The value for the lifetime multiplier, expressed as a percentage. The result of
multiplying the qbAtmPnniNodePtseRefreshInterval attribute value by this
attribute value is used as the initial lifetime that this node places into
self-originated PTSEs.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeRxmtInterval.setReference("""\
ATM Forum PNNI 1.0 Annex G DSRxmtInterval, RequestRxmtInterval,
PTSERetransmissionInterval
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeRxmtInterval.setDescription("""\
The period between retransmissions of unacknowledged Database Summary packets,
PTSE Request packets, and PTSPs.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerDelayedAckInterval.setReference("""\
ATM Forum PNNI 1.0 Annex G PeerDelayedAckInterval, Appendix G
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodePeerDelayedAckInterval.setDescription("""\
The minimum amount of time between transmissions of delayed PTSE
acknowledgement packets.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrPm.setReference("""\
ATM Forum PNNI 1.0 Section 5.8.5.2.5.4, Annex G AvCR_PM
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrPm.setDescription("""\
The proportional multiplier used in the algorithms that determine significant
change for AvCR parameters, expressed as a percentage.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrMt.setReference("""\
ATM Forum PNNI 1.0 Section 5.8.5.2.5.4, Annex G AvCR_mT
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeAvcrMt.setDescription("""\
The minimum threshold used in the algorithms that determine significant change
for AvCR parameters, expressed as a percentage.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeCdvPm.setReference("""\
ATM Forum PNNI 1.0 Section 5.8.5.2.5.6, Annex G CDV_PM
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCdvPm.setDescription("""\
The proportional multiplier used in the algorithms that determine significant
change for CDV metrics, expressed as a percentage.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniNodeCtdPm.setReference("""\
ATM Forum PNNI 1.0 Section 5.8.5.2.5.5, Annex G maxCTD_PM
""")
if mibBuilder.loadTexts:
    qbAtmPnniNodeCtdPm.setDescription("""\
The proportional multiplier used in the algorithms that determine significant
change for CTD metrics, expressed as a percentage.
""")
_QbAtmPnniLinkTable_Object = MibTable
qbAtmPnniLinkTable = _QbAtmPnniLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8)
)
if mibBuilder.loadTexts:
    qbAtmPnniLinkTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniLinkTable.setReference("""\
ATM Forum PNNI 1.0 Section 5.6
""")
if mibBuilder.loadTexts:
    qbAtmPnniLinkTable.setDescription("""\
This table contains the attributes necessary to describe the operation of
logical links attached to the local switching system and the relationship with
the neighbor nodes on the other end of the links. Links are attached to a
specific node within the switching system. A concatenation of the Node Index of
the node within the local switching system and the port ID are used as the
instance ID to uniquely identify the link. Links may represent horizontal links
between lowest level neighboring peers, outside links, uplinks, or horizontal
links to/from LGNs. The entire qbAtmPnniLink object is read-only, reflecting
the fact that this information is discovered dynamically by the PNNI protocol
rather than configured.
""")
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
if mibBuilder.loadTexts:
    qbAtmPnniLinkEntry.setReference("""\
ATM Forum PNNI 1.0 Section 5.6
""")
if mibBuilder.loadTexts:
    qbAtmPnniLinkEntry.setDescription("""\
An entry in the table, containing information about a link attached to a PNNI
logical node in this switching system.
""")
_QbAtmPnniLinkPortId_Type = Integer32
_QbAtmPnniLinkPortId_Object = MibTableColumn
qbAtmPnniLinkPortId = _QbAtmPnniLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8, 1, 1),
    _QbAtmPnniLinkPortId_Type()
)
qbAtmPnniLinkPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmPnniLinkPortId.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniLinkPortId.setDescription("""\
The Port Identifier of the link as selected by the local node. This value has
meaning only within the context of the node to which the port is attached.
""")


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
if mibBuilder.loadTexts:
    qbAtmPnniLinkType.setDescription("""\
Indicates the type of link being described.
""")
_QbAtmPnniLinkHelloState_Type = QbAtmPnniHelloState
_QbAtmPnniLinkHelloState_Object = MibTableColumn
qbAtmPnniLinkHelloState = _QbAtmPnniLinkHelloState_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 7, 8, 1, 3),
    _QbAtmPnniLinkHelloState_Type()
)
qbAtmPnniLinkHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmPnniLinkHelloState.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniLinkHelloState.setReference("""\
ATM Forum PNNI 1.0 Section 5.6.2.1.2
""")
if mibBuilder.loadTexts:
    qbAtmPnniLinkHelloState.setDescription("""\
For horizontal and outside links between lowest-level nodes and for links of
unknown type, this attribute indicates the state of the Hello protocol exchange
over this link. For links to/from LGNs, this attribute indicates the state of
the corresponding LGN Horizontal Link Hello State Machine. For uplinks (where
the port ID is not also used for the underlying outside link), this attribute
is set to notApplicable.
""")
_QbAtmHiddenVclTable_Object = MibTable
qbAtmHiddenVclTable = _QbAtmHiddenVclTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8)
)
if mibBuilder.loadTexts:
    qbAtmHiddenVclTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmHiddenVclTable.setDescription("""\
The QB table with extensions to atmVclTable
""")
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
if mibBuilder.loadTexts:
    qbAtmHiddenVclEntry.setDescription("""\
Entry in qbAtmHiddenVclTable
""")


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
if mibBuilder.loadTexts:
    qbAtmHiddenVclName.setDescription("""\
A textual description for the SPVC name.
""")


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
if mibBuilder.loadTexts:
    qbAtmHiddenVclType.setDescription("""\
Value for the interface type. Native ATM - Q155, S622; non-native - E1, DS1,
ENET, VT
""")
_QbAtmHiddenVclIfIndex_Type = InterfaceIndex
_QbAtmHiddenVclIfIndex_Object = MibTableColumn
qbAtmHiddenVclIfIndex = _QbAtmHiddenVclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1, 3),
    _QbAtmHiddenVclIfIndex_Type()
)
qbAtmHiddenVclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmHiddenVclIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmHiddenVclIfIndex.setDescription("""\
ifIndex value for IOT interface. This value is not used for native ATM
interfaces.
""")
_QbAtmHiddenVclVtIndex_Type = Integer32
_QbAtmHiddenVclVtIndex_Object = MibTableColumn
qbAtmHiddenVclVtIndex = _QbAtmHiddenVclVtIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 8, 1, 4),
    _QbAtmHiddenVclVtIndex_Type()
)
qbAtmHiddenVclVtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmHiddenVclVtIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmHiddenVclVtIndex.setDescription("""\
Address information for a VT card. This value is used for VT cards only.
""")
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
if mibBuilder.loadTexts:
    qbAtmStatsBuffOverCells.setDescription("""\
This object gives the number of cells discarded due to buffer overflows.
""")
_QbAtmStatsInvalidCells_Type = Counter32
_QbAtmStatsInvalidCells_Object = MibScalar
qbAtmStatsInvalidCells = _QbAtmStatsInvalidCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 9, 2),
    _QbAtmStatsInvalidCells_Type()
)
qbAtmStatsInvalidCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmStatsInvalidCells.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmStatsInvalidCells.setDescription("""\
This object gives the number of cells discarded due to unknown VPI/VCI.
""")
_QbAtmStatsInvUpdateCells_Type = Counter32
_QbAtmStatsInvUpdateCells_Object = MibScalar
qbAtmStatsInvUpdateCells = _QbAtmStatsInvUpdateCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 9, 3),
    _QbAtmStatsInvUpdateCells_Type()
)
qbAtmStatsInvUpdateCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmStatsInvUpdateCells.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmStatsInvUpdateCells.setDescription("""\
This object gives the number of cells discarded due to internal switch errors.
""")
_QbAtmInterfaceStatTable_Object = MibTable
qbAtmInterfaceStatTable = _QbAtmInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10)
)
if mibBuilder.loadTexts:
    qbAtmInterfaceStatTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatTable.setDescription("""\
The Quantum Bridge ATM Interface Statistic Table contains ATM layer statistics
for each ATM interface.
""")
_QbAtmInterfaceStatEntry_Object = MibTableRow
qbAtmInterfaceStatEntry = _QbAtmInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10, 1)
)
qbAtmInterfaceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbAtmInterfaceStatEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatEntry.setDescription("""\
An entry in the Quantum ATM Interface Table. Every ATM interface contains a
corresponding entry in the table.
""")
_QbAtmInterfaceStatTxOAMCells_Type = Counter32
_QbAtmInterfaceStatTxOAMCells_Object = MibTableColumn
qbAtmInterfaceStatTxOAMCells = _QbAtmInterfaceStatTxOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10, 1, 1),
    _QbAtmInterfaceStatTxOAMCells_Type()
)
qbAtmInterfaceStatTxOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatTxOAMCells.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatTxOAMCells.setDescription("""\
The total number of valid OAM cells transmitted by this atm layer interface.
""")
_QbAtmInterfaceStatRxOAMCells_Type = Counter32
_QbAtmInterfaceStatRxOAMCells_Object = MibTableColumn
qbAtmInterfaceStatRxOAMCells = _QbAtmInterfaceStatRxOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 10, 1, 2),
    _QbAtmInterfaceStatRxOAMCells_Type()
)
qbAtmInterfaceStatRxOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatRxOAMCells.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInterfaceStatRxOAMCells.setDescription("""\
The total number of OAS ATM cells received by this atm layer interface.
""")
_QbAtmInBandMgtTable_Object = MibTable
qbAtmInBandMgtTable = _QbAtmInBandMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11)
)
if mibBuilder.loadTexts:
    qbAtmInBandMgtTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTable.setDescription("""\
The QbAtmInBandMgtTable defines in-band Management IP channels for use by ATM
connections.
""")
_QbAtmInBandMgtEntry_Object = MibTableRow
qbAtmInBandMgtEntry = _QbAtmInBandMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1)
)
qbAtmInBandMgtEntry.setIndexNames(
    (0, "QB-ATM-MIB", "qbAtmInBandMgtIpAddr"),
)
if mibBuilder.loadTexts:
    qbAtmInBandMgtEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtEntry.setDescription("""\
An entry in the table, containing information about an in-band Management
channel.
""")
_QbAtmInBandMgtIpAddr_Type = IpAddress
_QbAtmInBandMgtIpAddr_Object = MibTableColumn
qbAtmInBandMgtIpAddr = _QbAtmInBandMgtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 1),
    _QbAtmInBandMgtIpAddr_Type()
)
qbAtmInBandMgtIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpAddr.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpAddr.setDescription("""\
An IP Address for in-band SNMP Management of this chassis.
""")
_QbAtmInBandMgtIpMask_Type = IpAddress
_QbAtmInBandMgtIpMask_Object = MibTableColumn
qbAtmInBandMgtIpMask = _QbAtmInBandMgtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 2),
    _QbAtmInBandMgtIpMask_Type()
)
qbAtmInBandMgtIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpMask.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpMask.setDescription("""\
The IP Network Mask associated with this in-band SNMP Management IP Address.
""")
_QbAtmInBandMgtIpIfIndex_Type = InterfaceIndex
_QbAtmInBandMgtIpIfIndex_Object = MibTableColumn
qbAtmInBandMgtIpIfIndex = _QbAtmInBandMgtIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 3),
    _QbAtmInBandMgtIpIfIndex_Type()
)
qbAtmInBandMgtIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIpIfIndex.setDescription("""\
The Interface associated with this in-band management address.
""")
_QbAtmInBandMgtNeighborIp_Type = IpAddress
_QbAtmInBandMgtNeighborIp_Object = MibTableColumn
qbAtmInBandMgtNeighborIp = _QbAtmInBandMgtNeighborIp_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 4),
    _QbAtmInBandMgtNeighborIp_Type()
)
qbAtmInBandMgtNeighborIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtNeighborIp.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtNeighborIp.setDescription("""\
This is the neighbor IP address associated with the in-band Management
Interface. If the qbAtmInBandMgtConnKind is any value other than pvc(1), this
object is non-applicable.
""")
_QbAtmInBandMgtIfIndex_Type = InterfaceIndex
_QbAtmInBandMgtIfIndex_Object = MibTableColumn
qbAtmInBandMgtIfIndex = _QbAtmInBandMgtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 5),
    _QbAtmInBandMgtIfIndex_Type()
)
qbAtmInBandMgtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtIfIndex.setDescription("""\
This is the interface index associated with the in-band Management connection.
If the qbAtmInBandMgtConnKind is any value other than pvc(1), this object is
non-applicable.
""")
_QbAtmInBandMgtVpi_Type = AtmVpIdentifier
_QbAtmInBandMgtVpi_Object = MibTableColumn
qbAtmInBandMgtVpi = _QbAtmInBandMgtVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 6),
    _QbAtmInBandMgtVpi_Type()
)
qbAtmInBandMgtVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtVpi.setDescription("""\
If the value of qbAtmInBandMgtConnKind is pvc(1), this is the VPI associated
with this in-band management connection. If the value of qbAtmInBandMgtConnKind
is spvcInitiator(4), this object is target VPI. In all other cases, the value
of this object is non-applicable.
""")
_QbAtmInBandMgtVci_Type = AtmVcIdentifier
_QbAtmInBandMgtVci_Object = MibTableColumn
qbAtmInBandMgtVci = _QbAtmInBandMgtVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 7),
    _QbAtmInBandMgtVci_Type()
)
qbAtmInBandMgtVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtVci.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtVci.setDescription("""\
If the value of qbAtmInBandMgtConnKind is pvc(1), this is the VCI associated
with this in-band management connection. If the value of qbAtmInBandMgtConnKind
is spvcInitiator(4), this object is target VCI. In all other cases, the value
of this object is non-applicable.
""")
_QbAtmInBandMgtConnKind_Type = AtmConnKind
_QbAtmInBandMgtConnKind_Object = MibTableColumn
qbAtmInBandMgtConnKind = _QbAtmInBandMgtConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 8),
    _QbAtmInBandMgtConnKind_Type()
)
qbAtmInBandMgtConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtConnKind.setDescription("""\
This is the connection type associated with the in-band Management connection.
The currently accepted types are pvc(1), spvcInitiator(4) and spvcTarget(5).
""")
_QbAtmInBandMgtTxTd_Type = AtmTrafficDescrParamIndex
_QbAtmInBandMgtTxTd_Object = MibTableColumn
qbAtmInBandMgtTxTd = _QbAtmInBandMgtTxTd_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 9),
    _QbAtmInBandMgtTxTd_Type()
)
qbAtmInBandMgtTxTd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTxTd.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTxTd.setDescription("""\
The Transmit traffic descriptor associated with this in-band management
channel.
""")
_QbAtmInBandMgtRxTd_Type = AtmTrafficDescrParamIndex
_QbAtmInBandMgtRxTd_Object = MibTableColumn
qbAtmInBandMgtRxTd = _QbAtmInBandMgtRxTd_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 10),
    _QbAtmInBandMgtRxTd_Type()
)
qbAtmInBandMgtRxTd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtRxTd.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtRxTd.setDescription("""\
The Receive traffic descriptor associated with this in-band management channel.
""")
_QbAtmInBandMgtTargetNsapAddr_Type = AtmAddr
_QbAtmInBandMgtTargetNsapAddr_Object = MibTableColumn
qbAtmInBandMgtTargetNsapAddr = _QbAtmInBandMgtTargetNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 11),
    _QbAtmInBandMgtTargetNsapAddr_Type()
)
qbAtmInBandMgtTargetNsapAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTargetNsapAddr.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtTargetNsapAddr.setDescription("""\
If the value of qbAtmInBandMgtConnKind is spvcInitiator(4) this object
represetns the Target NSAP Address of the connection. In all other cases, the
value of this object is non-applicable.
""")
_QbAtmInBandMgtRowStatus_Type = RowStatus
_QbAtmInBandMgtRowStatus_Object = MibTableColumn
qbAtmInBandMgtRowStatus = _QbAtmInBandMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 1, 11, 1, 12),
    _QbAtmInBandMgtRowStatus_Type()
)
qbAtmInBandMgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmInBandMgtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmInBandMgtRowStatus.setDescription("""\
To create, or delete an Entry in this table. Setting this object to
createAndGo(4) causes the corresponding row to be created. Setting this object
to destroy(6) causes the corresponding row to be deleted. Note that --
currently-- only a single instance of a row can be created in this table.
""")
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
if mibBuilder.loadTexts:
    qbAtmPkt.setDescription("""\
This traffic descriptor type is to define a connection with an Ethernet
endpoint, and it is for a user that does not want to use ATM parameters
directly. The EtherNet bandwidth will be converted to a nrtVbr traffic
descriptor. The conversion from Ethernet bandwidth to ATM cell rate must add an
ATM cell tax. This is defined using the pcbe (packet-to-cell bandwidth
expansion) factor. If this is not defined for the traffic descriptor, then the
system default (qbAtmDefaultPCBE)should be used. The use of the parameter
vector for this type: Parameter 1: minbw, the minimum guarnteed bandwidth fo
rthe connection. This is defined in Mb/sec. (0-100). Parameter 2: maxbw, the
maximum bursting capability of the connection. This is defined in Mb/sec
(1-100). It is default to minbw. Parameter 3: bw, indicates the bandwidth for
the PON segment. Vaules are expressed in Mb, and may take interger value
between 1 and 100. (only apply to 155Mb PON). It is default to minbw. Parameter
4: pcbe, it defines the packed-to-cell bandwidth expansion. This is the
percentage overhead that is used to convert Ethernet bandwidth to ATM cell
rates. It is default to qbAtmDefaultPCBE. Parameter 5: not used.
""")
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
if mibBuilder.loadTexts:
    qbAtmF4F5LLID.setDescription("""\
This object stores Loopback Location ID (LLID).
""")


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
if mibBuilder.loadTexts:
    qbAtmDefaultPCBE.setDescription("""\
This object stores the default atm cell tax to be used by the system.
""")

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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfGroupInfo.setDescription("""\
The set of all accessible objects in the Interface group of this MIB.
""")

qbAtmTrafficDescrParamGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 2)
)
qbAtmTrafficDescrParamGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmTrafficDescrParamName"),
        ("QB-ATM-MIB", "qbAtmTrafficDescrParamDefault"))
)
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmTrafficDescrParamGroupInfo.setDescription("""\
The set of all accessible objects in the Traffic group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmVclGroupInfo.setDescription("""\
The set of all accessible objects in the VCL group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmVplGroupInfo.setDescription("""\
The set of all accessible objects in the VPL group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmVcCrossConnectGroupInfo.setDescription("""\
The set of all accessible objects in the VPL group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmVpCrossConnectGroupInfo.setDescription("""\
The set of all accessible objects in the VPL group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmPnniNodeGroupInfo.setDescription("""\
The set of all accessible objects in the VPL group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmPnniIfGroupInfo.setDescription("""\
The set of all accessible objects in the PNNI interface group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmPnniRouteAddrGroupInfo.setDescription("""\
The set of all accessible objects in the Route group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmInterfaceConfSigGroupInfo.setDescription("""\
The set of all accessible objects in the Route group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmPnniNbrPeerGroupInfo.setDescription("""\
The set of all accessible objects in the PNNI Peer Nbr group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmPnniPglGroupInfo.setDescription("""\
The set of all accessible objects in the PGL group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmPnniTimerGroupInfo.setDescription("""\
The set of all accessible objects in the PNNI Timer group of this MIB.
""")

qbAtmPnniLinkGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 7, 2, 2, 14)
)
qbAtmPnniLinkGroupInfo.setObjects(
      *(("QB-ATM-MIB", "qbAtmPnniLinkType"),
        ("QB-ATM-MIB", "qbAtmPnniLinkHelloState"))
)
if mibBuilder.loadTexts:
    qbAtmPnniLinkGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmPnniLinkGroupInfo.setDescription("""\
The set of all accessible objects in the PNNI Link group of this MIB.
""")

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
if mibBuilder.loadTexts:
    qbAtmInBandMgtGroupInfo.setDescription("""\
The set of all accessible objects in the in-band management group of this MIB.
""")


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
if mibBuilder.loadTexts:
    qbAtmCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


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
