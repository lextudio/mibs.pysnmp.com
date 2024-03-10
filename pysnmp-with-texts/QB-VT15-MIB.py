"""SNMP MIB module (QB-VT15-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-VT15-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:29 2024
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

(AtmVorXLastChange,
 AtmTrafficDescrParamIndex,
 AtmVorXAdminStatus,
 atmNoClpNoScr,
 AtmConnCastType,
 AtmServiceCategory,
 AtmConnKind,
 AtmVpIdentifier,
 AtmVorXOperStatus,
 AtmAddr,
 AtmVcIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVorXLastChange",
    "AtmTrafficDescrParamIndex",
    "AtmVorXAdminStatus",
    "atmNoClpNoScr",
    "AtmConnCastType",
    "AtmServiceCategory",
    "AtmConnKind",
    "AtmVpIdentifier",
    "AtmVorXOperStatus",
    "AtmAddr",
    "AtmVcIdentifier")

(InterfaceIndexOrZero,
 ifIndex,
 InterfaceIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex",
    "InterfaceIndex")

(QbEnableStatus,
 QbPvcConnKind) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbEnableStatus",
    "QbPvcConnKind")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ObjectGroup,
 NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "NotificationGroup",
    "ModuleCompliance")

(Bits,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Counter64,
 iso,
 ObjectIdentity,
 TimeTicks,
 IpAddress,
 Gauge32,
 NotificationType,
 Counter32,
 MibIdentifier,
 Integer32,
 ModuleIdentity,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "iso",
    "ObjectIdentity",
    "TimeTicks",
    "IpAddress",
    "Gauge32",
    "NotificationType",
    "Counter32",
    "MibIdentifier",
    "Integer32",
    "ModuleIdentity",
    "Unsigned32")

(DisplayString,
 TextualConvention,
 TruthValue,
 TimeStamp,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue",
    "TimeStamp",
    "RowStatus")


# MODULE-IDENTITY

qbVTVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9)
)
qbVTVCMIB.setLastUpdated("0012131255Z")
if mibBuilder.loadTexts:
    qbVTVCMIB.setOrganization("""\
Quantum Bridge Communications, Inc.
""")
qbVTVCMIB.setContactInfo("""\
support@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbVTVCMIB.setDescription("""\
This module defines additional objects for the provisioning of VT1.5/VC12 links
in Quantum Bridge devices.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class QbVT15Sts1(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )

    if mibBuilder.loadTexts:
        description = """\
The STS-1 number.
"""


class QbVT15VTGroup(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )

    if mibBuilder.loadTexts:
        description = """\
The VT1.5 group number.
"""


class QbVT15VTGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )

    if mibBuilder.loadTexts:
        description = """\
The VT1.5 group number.
"""


class QbVT15VTId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )

    if mibBuilder.loadTexts:
        description = """\
The VT Identifier number. The qbVT15VTId is determined by using the following
formula: (sts-1) * 28 + (vtgrp-1) * 4 + vtnum. sts-sonet path, vtgrp - sonet
path group, vt - VT number.
"""


class QbVC12Id(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )

    if mibBuilder.loadTexts:
        description = """\
The VC Identifier number.
"""


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
if mibBuilder.loadTexts:
    qbVTVCConnTable.setDescription("""\
The Quantum Bridge VT connection table contains a list of VT1.5 connections
that are provisioned at OAS SONET(STS-3) and SDH(STM-1) interfaces between
IOT(DS1/E1) ports and VTs/VCs, ATM PVCs and VTs/VCs, VTs/VCs and VTs/VCs ports.
The STS-3 interfaces are listed in the sonetMediumTable(RFC2558) as interfaces
with the 'sonetMediumType' object set to sonet(1) value. The STM-1 interfaces
are listed in the sonetMediumTable(RFC2558) as interfaces with the
'sonetMediumType' object set to sdh(1). The table has 2 indexes of the first
end-point: Sonet interface index, vt/vc identifier. Note: All connections
between ATM ports and VTs/VCs are listed in the atmVclTable.
""")
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
if mibBuilder.loadTexts:
    qbVTVCConnEntry.setDescription("""\
An entry in the Quantum Bridge qbVTVCConnTable table.
""")
_QbVTVCIfIndex_Type = InterfaceIndex
_QbVTVCIfIndex_Object = MibTableColumn
qbVTVCIfIndex = _QbVTVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 1),
    _QbVTVCIfIndex_Type()
)
qbVTVCIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCIfIndex.setDescription("""\
The STS-3/SDH-1 signal interface.
""")


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
if mibBuilder.loadTexts:
    qbVTVCConnId.setDescription("""\
The identifier of the specified VT (virtual tributary) or VC signal. The VT
identifier is determined by using the following formula: (sts-1) * 28 +
(vtgrp-1) * 4 + vtnum. sts-sonet path, vtgrp - sonet path group, vt - VT
number.The VC identifier has ranges from 1 to 63.
""")
_QbVTVCConnIotAtmIfIndex_Type = InterfaceIndexOrZero
_QbVTVCConnIotAtmIfIndex_Object = MibTableColumn
qbVTVCConnIotAtmIfIndex = _QbVTVCConnIotAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 3),
    _QbVTVCConnIotAtmIfIndex_Type()
)
qbVTVCConnIotAtmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnIotAtmIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnIotAtmIfIndex.setDescription("""\
An IOT interface index of the atm layer interface or DS1/E1 interface of the
connection between an ATM/IOT and a VT1.5/VC12 or VT1.5/VC12 and VT1.5/VC12.
The connection type is indicated by the qbVTVCConnKind object. If this object
is set to vt15ToAtm or vt15ToAtm the ATM layer interface is specified. When the
iotE1ToVt15, iotDs1ToVt15,iotE1ToVc12, iotDs1ToVc12 values are set the IOT
DS1/E1 interface is specified. For a VT to VT connection this object isn't
needed.
""")


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
if mibBuilder.loadTexts:
    qbVTVCConnName.setDescription("""\
The textual name of the VT1.5/VC12 connection as specified by a user. It
provides a non-volatile handle for this PVC.The supplied name in the
qbVTVCConnName is associated with the same connection for as long as that
connection remains.
""")
_QbVTVCConnAdminStatus_Type = AtmVorXAdminStatus
_QbVTVCConnAdminStatus_Object = MibTableColumn
qbVTVCConnAdminStatus = _QbVTVCConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 5),
    _QbVTVCConnAdminStatus_Type()
)
qbVTVCConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnAdminStatus.setDescription("""\
The desired administrative status of the connection The up and down states
indicate that the traffic flow is enabled or disabled respectively across the
specified connection.
""")
_QbVTVCConnOperStatus_Type = AtmVorXOperStatus
_QbVTVCConnOperStatus_Object = MibTableColumn
qbVTVCConnOperStatus = _QbVTVCConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 6),
    _QbVTVCConnOperStatus_Type()
)
qbVTVCConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCConnOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnOperStatus.setDescription("""\
The current operational status of the connection.
""")
_QbVTVCConnLastChange_Type = AtmVorXLastChange
_QbVTVCConnLastChange_Object = MibTableColumn
qbVTVCConnLastChange = _QbVTVCConnLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 7),
    _QbVTVCConnLastChange_Type()
)
qbVTVCConnLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCConnLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnLastChange.setDescription("""\
The value of sysUpTime at the time this connection entered its current
operational state.
""")
_QbVTVCConnAtmVpi_Type = AtmVpIdentifier
_QbVTVCConnAtmVpi_Object = MibTableColumn
qbVTVCConnAtmVpi = _QbVTVCConnAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 8),
    _QbVTVCConnAtmVpi_Type()
)
qbVTVCConnAtmVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnAtmVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnAtmVpi.setDescription("""\
The value of this object is equal to the VPI used by the ATM VCL mapped through
this connection to a VT. The value is irrelevant for a non-ATM connection.
(i.e., qbVTVCConnKind isn't set vt15ToAtm or vc12ToAtm value).
""")
_QbVTVCConnAtmVci_Type = AtmVcIdentifier
_QbVTVCConnAtmVci_Object = MibTableColumn
qbVTVCConnAtmVci = _QbVTVCConnAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 9),
    _QbVTVCConnAtmVci_Type()
)
qbVTVCConnAtmVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnAtmVci.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnAtmVci.setDescription("""\
The value of this object is equal to the VCI used by the ATM VCL mapped through
this connection to a VT. The value is irrelevant if a non-ATM connection.
(i.e., qbVTVCConnKind isn't set to vt15ToAtm or vc12ToAtm value).
""")


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
if mibBuilder.loadTexts:
    qbVTVCConnKind.setDescription("""\
The VT connection type. Two types of connection can be provisioned on the
VT/sonet port (IOT-VT and VT-ATM)
""")


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
if mibBuilder.loadTexts:
    qbVTVCCrossConnId.setDescription("""\
This object is instantiated only for a VT/VC which is cross-connected to
another VT/VC. Two entries that have the same value belong to a single entry of
qbVTVCCrossConnTable. The corresponding entry in qbVTVCCrossConnTable can be
found by sending getnext with qbVTVCIfIndex qbVTVCConnId instances. The value
is irrelevant for a non-VTtpVT connection (i.e., qbVTVCConnKind isn't set to
vt15Vt15 or vt12Vt12 value).
""")
_QbVTVCConnRowStatus_Type = RowStatus
_QbVTVCConnRowStatus_Object = MibTableColumn
qbVTVCConnRowStatus = _QbVTVCConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 1, 1, 12),
    _QbVTVCConnRowStatus_Type()
)
qbVTVCConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCConnRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCConnRowStatus.setDescription("""\
The status column for this IOT ENET interface. This OBJECT can be set to:
createAndGo(4) destroy(6) The following values may be read: active(1) This
object may only be set to createAndGo(4). Setting this object to active(1) when
its value is already active(1) is a no-op. Setting this object to
createAndGo(4) causes the agent to attempt to create and commit a row based on
the contents of the objects in the row. If all necessary information is present
in the row and the values are acceptable to the agent, the agent will change
the status to active(1). If any of the necessary objects are not available, the
agent will reject the creation request.
""")


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
if mibBuilder.loadTexts:
    qbVTVCConnLoopback.setDescription("""\
Activate a connection loopback for a PVC that has an endpoint on this VT. This
object, when read, returns one of the following results: enable(1): Loopback is
enabled on this VT disable(2): Loopback is disbaled on this VT Setting this
object to one of the acceptable values causes the following results depending
on the qbVTVCConnLoopbackEndpt value: enable(1): Enable loopback on this VT
trib when qbVTVCConnLoopbackEndpt is set to 'vtLoopback'. Enable loopback on
IOT or ATM port when qbVTVCConnLoopbackEndpt is set to nonVtloopback'. For VT
to VT connection this object activates loopback on this VT. disable(2): Disbale
activated loopback. The disabled endpoint is selected depending of the
qbVTVCConnLoopbackEndpt
""")


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
if mibBuilder.loadTexts:
    qbVTVCConnLoopbackEndpt.setDescription("""\
Define an endpoint on which loopback is activated or disabled. The object works
in conjunction with the qbVTVCConnLoopback.
""")
_QbVTVCCrossConnTable_Object = MibTable
qbVTVCCrossConnTable = _QbVTVCCrossConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    qbVTVCCrossConnTable.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCCrossConnTable.setDescription("""\
The Quantum Bridge VT cross-connection (VT to VT) table contains all point-to-
point cross-connections between various VTs that are provisoned at OAS STS-3
Sonet interfaces. The STS-3 interfaces are listed in the
sonetMediumTable(RFC2558) as interfaces with the 'sonetMediumType' object set
to sonet(1). The table is indexed by four indexes: low interface interface
index,low vt identifiers, high interface index, and high vt identifier. The
terms low and high are chosen to represent numerical ordering of two
interfaces/vt within VT cross-connect.
""")
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
if mibBuilder.loadTexts:
    qbVTVCCrossConnEntry.setDescription("""\
An entry in the Quantum Bridge QbVTVCCrossConnTable.
""")
_QbVTVCCrossConnIfIndexEndpt1_Type = InterfaceIndex
_QbVTVCCrossConnIfIndexEndpt1_Object = MibTableColumn
qbVTVCCrossConnIfIndexEndpt1 = _QbVTVCCrossConnIfIndexEndpt1_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 1),
    _QbVTVCCrossConnIfIndexEndpt1_Type()
)
qbVTVCCrossConnIfIndexEndpt1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIfIndexEndpt1.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIfIndexEndpt1.setDescription("""\
The STS-3/SDH-1 Sonet low interface index of the specified cross-connection.
""")


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
if mibBuilder.loadTexts:
    qbVTVCCrossConnVTIdEndpt1.setDescription("""\
The low VT/VC identifier of the specified VT/VC group of the first cross-
connect endpoint.
""")
_QbVTVCCrossConnIfIndexEndpt2_Type = InterfaceIndex
_QbVTVCCrossConnIfIndexEndpt2_Object = MibTableColumn
qbVTVCCrossConnIfIndexEndpt2 = _QbVTVCCrossConnIfIndexEndpt2_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 3),
    _QbVTVCCrossConnIfIndexEndpt2_Type()
)
qbVTVCCrossConnIfIndexEndpt2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIfIndexEndpt2.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCCrossConnIfIndexEndpt2.setDescription("""\
The high STS-3 Sonet interface of the specified cross-connection of the second
cross-connect endpoint.
""")


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
if mibBuilder.loadTexts:
    qbVTVCCrossConnVTIdEndpt2.setDescription("""\
The high VT/VC identifier of the specified VT group of the second cross-connect
endpoint.
""")


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
if mibBuilder.loadTexts:
    qbVTVCCrossConnIndex.setDescription("""\
A unique value to identify this VT to VT cross-connect. For each
qbVTVCConnEntry associated with this cross-connect, the agent reports this
cross-connect index value in the qbVTVCCrossConnId attribute of the
corresponding qbVTVCConnTable entries.
""")


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
if mibBuilder.loadTexts:
    qbVTVCCrossConnName.setDescription("""\
The textual name of the VT1.5 cross-connection as specified by a user. It
provides a non-volatile handle for this cross-connection. The supplied name in
the qbVTVCCrossName is associated with the same cross-connection for as long as
that cross-conection remains.
""")
_QbVTVCCrossConnAdminStatus_Type = AtmVorXAdminStatus
_QbVTVCCrossConnAdminStatus_Object = MibTableColumn
qbVTVCCrossConnAdminStatus = _QbVTVCCrossConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 7),
    _QbVTVCCrossConnAdminStatus_Type()
)
qbVTVCCrossConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCCrossConnAdminStatus.setDescription("""\
The desired administrative status of the specified cross-connection. The up and
down states indicate that the traffic flow is enabled or disabled across this
cross-connection.
""")
_QbVTVCCrossConnOperStatus_Type = AtmVorXOperStatus
_QbVTVCCrossConnOperStatus_Object = MibTableColumn
qbVTVCCrossConnOperStatus = _QbVTVCCrossConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 8),
    _QbVTVCCrossConnOperStatus_Type()
)
qbVTVCCrossConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVTVCCrossConnOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCCrossConnOperStatus.setDescription("""\
The current operational status of the connection.
""")


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
if mibBuilder.loadTexts:
    qbVTVCCrossConnKind.setDescription("""\
The VT connection type. Two types of connection can be provisioned on the VT-VT
and VC-VC.
""")
_QbVTVCCrossConnRowStatus_Type = RowStatus
_QbVTVCCrossConnRowStatus_Object = MibTableColumn
qbVTVCCrossConnRowStatus = _QbVTVCCrossConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 2, 1, 10),
    _QbVTVCCrossConnRowStatus_Type()
)
qbVTVCCrossConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbVTVCCrossConnRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbVTVCCrossConnRowStatus.setDescription("""\
The status column for this IOT ENET interface. This OBJECT can be set to:
createAndGo(4) destroy(6) The following values may be read: active(1) This
object may only be set to createAndGo(4). Setting this object to active(1) when
its value is already active(1) is a no-op. Setting this object to
createAndGo(4) causes the agent to attempt to create and commit a row based on
the contents of the objects in the row. If all necessary information is present
in the row and the values are acceptable to the agent, the agent will change
the status to active(1). If any of the necessary objects are not available, the
agent will reject the creation request. Setting this object to destroy(6) will
remove the corresponding entry in this table, and disable data traffic.
""")
_QbVTConfTable_Object = MibTable
qbVTConfTable = _QbVTConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    qbVTConfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbVTConfTable.setDescription("""\
The Quantum Bridge VT configuration table contains configuration parameters of
tributaries at OAS VT155 interfaces. The STS-3 interfaces of D155VT cards that
are listed in the sonetMediumTable(RFC2558) as interfaces with the
'sonetMediumType' object set to sonet(1). The table has two indexes: Sonet
interface index, and tributary identifier.
""")
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
if mibBuilder.loadTexts:
    qbVTConfEntry.setDescription("""\
An entry in the Quantum Bridge qbVTConfEntry. Every entry containes settings of
the tributary
""")
_QbVTConfIfIndex_Type = InterfaceIndex
_QbVTConfIfIndex_Object = MibTableColumn
qbVTConfIfIndex = _QbVTConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1, 1),
    _QbVTConfIfIndex_Type()
)
qbVTConfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTConfIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbVTConfIfIndex.setDescription("""\
The STS-3/SDH-1 Sonet interface of the specified tributary.
""")
_QbVTConfVTId_Type = QbVT15VTId
_QbVTConfVTId_Object = MibTableColumn
qbVTConfVTId = _QbVTConfVTId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 3, 1, 2),
    _QbVTConfVTId_Type()
)
qbVTConfVTId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVTConfVTId.setStatus("current")
if mibBuilder.loadTexts:
    qbVTConfVTId.setDescription("""\
The identifier of the specified tributary.
""")


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
if mibBuilder.loadTexts:
    qbVTConfClockMode.setDescription("""\
The object defines whether VT155 service clocking mode used for AAL1 recovery.
Applies only to D155VT interfaces that are configured for SONET format.
""")


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
if mibBuilder.loadTexts:
    qbVTConfAction.setDescription("""\
Indicates whether the clock mode is set for a single tributary or group of
tributaries. When set to 'singleVTAction(1)' a single selected tributary is set
to a desired clock mode. When set to 'stsVTAction(2)' all tributaries that
belongs to qbVTConfVTId's STS are set to a desired clock mode. When set to
'ifVTAction(3)' all qbVTConfIfIndex tributaries are set to a desired clock
mode. For this mode the value of qbVTConfVTId is irrelevant. Thus any valid
QbVT15VTId value can be used. When the value is set to 'noop', no operation is
performed. When read, this object always returns the value noop(4).
""")
_QbVtVcStatsTable_Object = MibTable
qbVtVcStatsTable = _QbVtVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    qbVtVcStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsTable.setDescription("""\
This table contains the stats for each VT/VC with a connection established. One
row in this table should exist for each VT/VC connection.
""")
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
if mibBuilder.loadTexts:
    qbVtVcStatsEntry.setDescription("""\
An entry in the Quantum Bridge qbVtVcStatsTable table.
""")
_QbVtVcStatsIfIndex_Type = InterfaceIndex
_QbVtVcStatsIfIndex_Object = MibTableColumn
qbVtVcStatsIfIndex = _QbVtVcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 1),
    _QbVtVcStatsIfIndex_Type()
)
qbVtVcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbVtVcStatsIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsIfIndex.setDescription("""\
The STS-3/SDH-1 signal interface.
""")


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
if mibBuilder.loadTexts:
    qbVtVcStatsConnId.setDescription("""\
The identifier of the specified VT (virtual tributary) or VC signal. The VT
identifier is determined by using the following formula: (sts-1) * 28 +
(vtgrp-1) * 4 + vtnum. sts-sonet path, vtgrp - sonet path group, vt - VT
number.The VC identifier has ranges from 1 to 63.
""")
_QbVtVcStatsRxCells_Type = Counter32
_QbVtVcStatsRxCells_Object = MibTableColumn
qbVtVcStatsRxCells = _QbVtVcStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 3),
    _QbVtVcStatsRxCells_Type()
)
qbVtVcStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsRxCells.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsRxCells.setDescription("""\
The number of received cells.
""")
_QbVtVcStatsTxCells_Type = Counter32
_QbVtVcStatsTxCells_Object = MibTableColumn
qbVtVcStatsTxCells = _QbVtVcStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 4),
    _QbVtVcStatsTxCells_Type()
)
qbVtVcStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsTxCells.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsTxCells.setDescription("""\
The number of transmitted cells.
""")
_QbVtVcStatsRxDroppedCells_Type = Counter32
_QbVtVcStatsRxDroppedCells_Object = MibTableColumn
qbVtVcStatsRxDroppedCells = _QbVtVcStatsRxDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 5),
    _QbVtVcStatsRxDroppedCells_Type()
)
qbVtVcStatsRxDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsRxDroppedCells.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsRxDroppedCells.setDescription("""\
The number of received cells that were dropped.
""")
_QbVtVcStatsTxConditionalCells_Type = Counter32
_QbVtVcStatsTxConditionalCells_Object = MibTableColumn
qbVtVcStatsTxConditionalCells = _QbVtVcStatsTxConditionalCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 6),
    _QbVtVcStatsTxConditionalCells_Type()
)
qbVtVcStatsTxConditionalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsTxConditionalCells.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsTxConditionalCells.setDescription("""\
The number of transmitted conditional cells.
""")
_QbVtVcStatsTxSuppressedCells_Type = Counter32
_QbVtVcStatsTxSuppressedCells_Object = MibTableColumn
qbVtVcStatsTxSuppressedCells = _QbVtVcStatsTxSuppressedCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 9, 1, 4, 1, 7),
    _QbVtVcStatsTxSuppressedCells_Type()
)
qbVtVcStatsTxSuppressedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbVtVcStatsTxSuppressedCells.setStatus("current")
if mibBuilder.loadTexts:
    qbVtVcStatsTxSuppressedCells.setDescription("""\
The number of transmitted supressed cells.
""")
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
if mibBuilder.loadTexts:
    qbVTVCConnInfo.setDescription("""\
The set of all accessible objects in this MIB.
""")

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
if mibBuilder.loadTexts:
    qbVTVCCrossConnInfo.setDescription("""\
The set of all accessible objects in this MIB.
""")


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
if mibBuilder.loadTexts:
    qbVTVCConnOperStatusChange.setDescription("""\
A notification indicates that a VT15 connection has chaged the operations
status. The notification is originated for every connection which is listed in
the qbVTVCConnTable when its the qbVTVCConnOperStatus object changed state.
""")

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
if mibBuilder.loadTexts:
    qbVTVCCrossConnOperStatusChange.setDescription("""\
A notification indicates that a VT15 cross-connection has chaged the operations
status. The notification is originated for every connection which is listed in
the qbVT15CrossConnTable when its the qbVTVCCrossConnOperStatus object changed
state.
""")


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
if mibBuilder.loadTexts:
    qbVTVCCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


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
