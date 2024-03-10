"""SNMP MIB module (QB-PVC-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-PVC-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:33 2024
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

(AtmVpIdentifier,
 AtmVorXLastChange,
 atmNoClpNoScr,
 AtmServiceCategory,
 AtmVorXOperStatus,
 AtmAddr,
 AtmConnCastType,
 AtmTrafficDescrParamIndex,
 AtmConnKind,
 AtmVcIdentifier,
 AtmVorXAdminStatus) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVpIdentifier",
    "AtmVorXLastChange",
    "atmNoClpNoScr",
    "AtmServiceCategory",
    "AtmVorXOperStatus",
    "AtmAddr",
    "AtmConnCastType",
    "AtmTrafficDescrParamIndex",
    "AtmConnKind",
    "AtmVcIdentifier",
    "AtmVorXAdminStatus")

(InterfaceIndex,
 ifIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "InterfaceIndexOrZero")

(QbEnableStatus,
 QbPvcConnKind) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbEnableStatus",
    "QbPvcConnKind")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(NotificationGroup,
 ObjectGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ObjectGroup",
    "ModuleCompliance")

(Unsigned32,
 Integer32,
 TimeTicks,
 iso,
 IpAddress,
 Bits,
 ObjectIdentity,
 MibIdentifier,
 ModuleIdentity,
 Counter32,
 Gauge32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Counter64,
 NotificationType) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Unsigned32",
    "Integer32",
    "TimeTicks",
    "iso",
    "IpAddress",
    "Bits",
    "ObjectIdentity",
    "MibIdentifier",
    "ModuleIdentity",
    "Counter32",
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "NotificationType")

(TruthValue,
 RowStatus,
 DisplayString,
 TimeStamp,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TruthValue",
    "RowStatus",
    "DisplayString",
    "TimeStamp",
    "TextualConvention")


# MODULE-IDENTITY

qbPvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13)
)
qbPvcMIB.setLastUpdated("0107031255Z")
if mibBuilder.loadTexts:
    qbPvcMIB.setOrganization("""\
Quantum Bridge Communications, Inc.
""")
qbPvcMIB.setContactInfo("""\
support@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbPvcMIB.setDescription("""\
This module defines additional objects for the provisioning and management of
PVC in Quantum bridge devices.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class QbConnEndptType(TextualConvention, Integer32):
    status = "current"
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
        *(("esw", 2),
          ("gige", 4),
          ("iotEnet", 3),
          ("unknown", 1),
          ("vlan", 5))
    )

    if mibBuilder.loadTexts:
        description = """\
A data rate in Mbits/second.
"""


# MIB Managed Objects in the order of their OIDs

_QbPvcObjects_ObjectIdentity = ObjectIdentity
qbPvcObjects = _QbPvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1)
)
_QbEnetPvcGroup_ObjectIdentity = ObjectIdentity
qbEnetPvcGroup = _QbEnetPvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1)
)
_QbEnetPvcNumber_Type = Integer32
_QbEnetPvcNumber_Object = MibScalar
qbEnetPvcNumber = _QbEnetPvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 1),
    _QbEnetPvcNumber_Type()
)
qbEnetPvcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbEnetPvcNumber.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcNumber.setDescription("""\
The total number of provisioned Ethernet to ATM PVCs.
""")
_QbEnePvcLastTimeUpdate_Type = TimeTicks
_QbEnePvcLastTimeUpdate_Object = MibScalar
qbEnePvcLastTimeUpdate = _QbEnePvcLastTimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 2),
    _QbEnePvcLastTimeUpdate_Type()
)
qbEnePvcLastTimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbEnePvcLastTimeUpdate.setStatus("current")
if mibBuilder.loadTexts:
    qbEnePvcLastTimeUpdate.setDescription("""\
The value of sysUpTime at the time of the last creation, deletion or
modification of an entry in the qbAtmPvcTable. If the number of entries has
been unchanged since the last re-initialization of the agent, then this object
contains a zero value.
""")
_QbEnetPvcTable_Object = MibTable
qbEnetPvcTable = _QbEnetPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qbEnetPvcTable.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcTable.setDescription("""\
The Quantum Bridge Ethernet configuration table contains connections between
Ethernet interfaces (IOT and Ethernet Module) and corresponding VCL/AAL5 that
are configured at an ATM interface. An entry in the table may be created,
destroyed or modified. This table lists all Ethernet AAL5 PVCs within the
System that send/receive packet traffic to/from the ATM cloud.
""")
_QbEnetPvcEntry_Object = MibTableRow
qbEnetPvcEntry = _QbEnetPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1)
)
qbEnetPvcEntry.setIndexNames(
    (0, "QB-PVC-MIB", "qbEnetPvcIndex"),
)
if mibBuilder.loadTexts:
    qbEnetPvcEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcEntry.setDescription("""\
An entry in the qbEnetPvcTable. There is one entry in the table per Ethernet
interface. The creation of a row in this table causes a corresponding entry in
the atmVclTable of the ATM-MIB to be automatically created if an atmVclEntry
with qbEnetPvcVpi and qbEnetPvcVci values does not exist. This corresponding
entry can be removed only if the qbEnetPvcEntry is removed. The qbEnetPvcIndex
of this table is an ifIndex of the IOT or Module Ethernet interface from the
ifTable.
""")
_QbEnetPvcIndex_Type = Integer32
_QbEnetPvcIndex_Object = MibTableColumn
qbEnetPvcIndex = _QbEnetPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 1),
    _QbEnetPvcIndex_Type()
)
qbEnetPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbEnetPvcIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcIndex.setDescription("""\
The value of this object is equal to MIB II's ifIndex value of the IOT or
24-Port Enet Port interface.
""")
_QbEnetPvcAtmIndex_Type = InterfaceIndex
_QbEnetPvcAtmIndex_Object = MibTableColumn
qbEnetPvcAtmIndex = _QbEnetPvcAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 2),
    _QbEnetPvcAtmIndex_Type()
)
qbEnetPvcAtmIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcAtmIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcAtmIndex.setDescription("""\
The value of this object is equal to MIB II's ifIndex value of the ATM Port
interface mapped to an Ethernet interface.
""")
_QbEnetPvcVpi_Type = AtmVpIdentifier
_QbEnetPvcVpi_Object = MibTableColumn
qbEnetPvcVpi = _QbEnetPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 3),
    _QbEnetPvcVpi_Type()
)
qbEnetPvcVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcVpi.setDescription("""\
A VPI of the AAL5 bi-directional PVC that connects this interface to the ATM
cloud.
""")
_QbEnetPvcVci_Type = AtmVcIdentifier
_QbEnetPvcVci_Object = MibTableColumn
qbEnetPvcVci = _QbEnetPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 4),
    _QbEnetPvcVci_Type()
)
qbEnetPvcVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcVci.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcVci.setDescription("""\
A VCI of the AAL5 bi-directional PVC that connects this interface to the ATM
cloud.
""")


class _QbEnetPvcName_Type(DisplayString):
    """Custom type qbEnetPvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbEnetPvcName_Type.__name__ = "DisplayString"
_QbEnetPvcName_Object = MibTableColumn
qbEnetPvcName = _QbEnetPvcName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 5),
    _QbEnetPvcName_Type()
)
qbEnetPvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcName.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcName.setDescription("""\
The textual name of the connection(PVC) as specified by a user. It provides a
non-volatile handle for this PVC. The supplied name in the qbAtmPvcName is
associated with the same PVC for as long as that PVC/conection remains.
""")


class _QbEnetPvcRxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbEnetPvcRxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 3


_QbEnetPvcRxTrafficDescrIndex_Object = MibTableColumn
qbEnetPvcRxTrafficDescrIndex = _QbEnetPvcRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 6),
    _QbEnetPvcRxTrafficDescrIndex_Type()
)
qbEnetPvcRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row of the ATM Traffic Descriptor Table
which applies to the transmit direction of this VCL.
""")


class _QbEnetPvcTxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbEnetPvcTxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 3


_QbEnetPvcTxTrafficDescrIndex_Object = MibTableColumn
qbEnetPvcTxTrafficDescrIndex = _QbEnetPvcTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 7),
    _QbEnetPvcTxTrafficDescrIndex_Type()
)
qbEnetPvcTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VCL.
""")
_QbEnetPvcAdminStatus_Type = AtmVorXAdminStatus
_QbEnetPvcAdminStatus_Object = MibTableColumn
qbEnetPvcAdminStatus = _QbEnetPvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 8),
    _QbEnetPvcAdminStatus_Type()
)
qbEnetPvcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcAdminStatus.setDescription("""\
The desired administrative status of the Ethernet connection The up and down
states indicate that the traffic flow is enabled or disabled respectively
across the ATM cloud.
""")
_QbEnetPvcOperStatus_Type = AtmVorXOperStatus
_QbEnetPvcOperStatus_Object = MibTableColumn
qbEnetPvcOperStatus = _QbEnetPvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 9),
    _QbEnetPvcOperStatus_Type()
)
qbEnetPvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbEnetPvcOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcOperStatus.setDescription("""\
The current operational status of the connect.
""")
_QbEnetPvcLastChange_Type = AtmVorXLastChange
_QbEnetPvcLastChange_Object = MibTableColumn
qbEnetPvcLastChange = _QbEnetPvcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 10),
    _QbEnetPvcLastChange_Type()
)
qbEnetPvcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbEnetPvcLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcLastChange.setDescription("""\
The value of sysUpTime at the time this PVC entered its current operational
state.
""")


class _QbEnetPvcConnKind_Type(QbPvcConnKind):
    """Custom type qbEnetPvcConnKind based on QbPvcConnKind"""


_QbEnetPvcConnKind_Object = MibTableColumn
qbEnetPvcConnKind = _QbEnetPvcConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 11),
    _QbEnetPvcConnKind_Type()
)
qbEnetPvcConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcConnKind.setDescription("""\
The connection type. Two types of connection can be provisioned on the Enet
port (modEnetToAtm and iotEnetToAtm)
""")
_QbEnetPvcLoopback_Type = QbEnableStatus
_QbEnetPvcLoopback_Object = MibTableColumn
qbEnetPvcLoopback = _QbEnetPvcLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 12),
    _QbEnetPvcLoopback_Type()
)
qbEnetPvcLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcLoopback.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcLoopback.setDescription("""\
This object enables loopback on the ENET or ATM enedpoint.
""")


class _QbEnetPvcLoopbackSide_Type(Integer32):
    """Custom type qbEnetPvcLoopbackSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmEndpt", 2),
          ("enetEndpt", 1),
          ("none", 3))
    )


_QbEnetPvcLoopbackSide_Type.__name__ = "Integer32"
_QbEnetPvcLoopbackSide_Object = MibTableColumn
qbEnetPvcLoopbackSide = _QbEnetPvcLoopbackSide_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 13),
    _QbEnetPvcLoopbackSide_Type()
)
qbEnetPvcLoopbackSide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcLoopbackSide.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcLoopbackSide.setDescription("""\
This object enables loopback on the IOT ENET enedpoint.
""")
_QbEnetPvcRowStatus_Type = RowStatus
_QbEnetPvcRowStatus_Object = MibTableColumn
qbEnetPvcRowStatus = _QbEnetPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 1, 3, 1, 14),
    _QbEnetPvcRowStatus_Type()
)
qbEnetPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbEnetPvcRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcRowStatus.setDescription("""\
The status column for this IOT ENET interface. This OBJECT can be set to:
createAndGo(4) destroy(6) The following values may be read: active(1) This
object may only be set to createAndGo(4). Setting this object to active(1) when
its value is already active(1) is a no-op. Setting this object to
createAndGo(4) causes the agent to attempt to create and commit the row based
on the contents of the objects in the row. If all necessary information is
present in the row and the values are acceptable to the agent, the agent will
change the status to active(1). If any of the necessary objects are not
available, the agent will reject the creation request. Setting this object to
destroy(6) will remove the corresponding entry in this table, and disable data
traffic.
""")
_QbCrossConnPvcGroup_ObjectIdentity = ObjectIdentity
qbCrossConnPvcGroup = _QbCrossConnPvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2)
)
_QbCrossConnPvcNumber_Type = Integer32
_QbCrossConnPvcNumber_Object = MibScalar
qbCrossConnPvcNumber = _QbCrossConnPvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 1),
    _QbCrossConnPvcNumber_Type()
)
qbCrossConnPvcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCrossConnPvcNumber.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcNumber.setDescription("""\
The total number of provisioned Enet to Enet, DS1 to DS1, E1 to E1 PVCs.
""")
_QbCrossConnPvcLastTimeUpdate_Type = TimeTicks
_QbCrossConnPvcLastTimeUpdate_Object = MibScalar
qbCrossConnPvcLastTimeUpdate = _QbCrossConnPvcLastTimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 2),
    _QbCrossConnPvcLastTimeUpdate_Type()
)
qbCrossConnPvcLastTimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCrossConnPvcLastTimeUpdate.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcLastTimeUpdate.setDescription("""\
The value of sysUpTime at the time of the last creation, deletion or
modification of an entry in the qbAtmPvcTable. If the number of entries has
been unchanged since the last re-initialization of the agent, then this object
contains a zero value.
""")
_QbCrossConnPvcTable_Object = MibTable
qbCrossConnPvcTable = _QbCrossConnPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qbCrossConnPvcTable.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcTable.setDescription("""\
The Quantum Bridge Pvc cross-connection table. This table defines Enet, DS1, or
E1 port point-to-point cross-connections within a single OAS system. The
connection can be set between two Ethernet, two DS1 or two E1 ports. The table
has two indexes: the interface index of the first end-point and the interface
index of the second endpoint. Note: Connections that are listed in this table
are not reflected in the atmVclTable.
""")
_QbCrossConnPvcEntry_Object = MibTableRow
qbCrossConnPvcEntry = _QbCrossConnPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1)
)
qbCrossConnPvcEntry.setIndexNames(
    (0, "QB-PVC-MIB", "qbCrossConnPvcLowIfIndex"),
    (0, "QB-PVC-MIB", "qbCrossConnPvcHighIfIndex"),
)
if mibBuilder.loadTexts:
    qbCrossConnPvcEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcEntry.setDescription("""\
An entry in the Quantum Bridge qbCrossConnPvcTable two contains a connection
between the same port type of IOTs or Modules(Enet and DS1).
""")
_QbCrossConnPvcLowIfIndex_Type = InterfaceIndex
_QbCrossConnPvcLowIfIndex_Object = MibTableColumn
qbCrossConnPvcLowIfIndex = _QbCrossConnPvcLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 1),
    _QbCrossConnPvcLowIfIndex_Type()
)
qbCrossConnPvcLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbCrossConnPvcLowIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcLowIfIndex.setDescription("""\
The ifIndex of the first interface(lower index) for the configured PVC cross-
connect.
""")
_QbCrossConnPvcHighIfIndex_Type = InterfaceIndex
_QbCrossConnPvcHighIfIndex_Object = MibTableColumn
qbCrossConnPvcHighIfIndex = _QbCrossConnPvcHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 2),
    _QbCrossConnPvcHighIfIndex_Type()
)
qbCrossConnPvcHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbCrossConnPvcHighIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcHighIfIndex.setDescription("""\
The ifIndex of the second interface(higher index) for the configured PVC cross-
connect.
""")
_QbCrossConnPvcAdminStatus_Type = AtmVorXAdminStatus
_QbCrossConnPvcAdminStatus_Object = MibTableColumn
qbCrossConnPvcAdminStatus = _QbCrossConnPvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 3),
    _QbCrossConnPvcAdminStatus_Type()
)
qbCrossConnPvcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcAdminStatus.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VCL.
""")
_QbCrossConnPvcOperStatus_Type = AtmVorXOperStatus
_QbCrossConnPvcOperStatus_Object = MibTableColumn
qbCrossConnPvcOperStatus = _QbCrossConnPvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 4),
    _QbCrossConnPvcOperStatus_Type()
)
qbCrossConnPvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCrossConnPvcOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcOperStatus.setDescription("""\
The current operational status of the connection.
""")
_QbCrossConnPvcLastChange_Type = AtmVorXLastChange
_QbCrossConnPvcLastChange_Object = MibTableColumn
qbCrossConnPvcLastChange = _QbCrossConnPvcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 5),
    _QbCrossConnPvcLastChange_Type()
)
qbCrossConnPvcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCrossConnPvcLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcLastChange.setDescription("""\
The value of sysUpTime at the time this connection entered its current
operational state.
""")
_QbCrossConnPvcRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbCrossConnPvcRxTrafficDescrIndex_Object = MibTableColumn
qbCrossConnPvcRxTrafficDescrIndex = _QbCrossConnPvcRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 6),
    _QbCrossConnPvcRxTrafficDescrIndex_Type()
)
qbCrossConnPvcRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row of the ATM Traffic Descriptor Table
which applies to the transmit direction of this connection.
""")


class _QbCrossConnPvcTxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbCrossConnPvcTxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 3


_QbCrossConnPvcTxTrafficDescrIndex_Object = MibTableColumn
qbCrossConnPvcTxTrafficDescrIndex = _QbCrossConnPvcTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 7),
    _QbCrossConnPvcTxTrafficDescrIndex_Type()
)
qbCrossConnPvcTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this connection.
""")


class _QbCrossConnPvcName_Type(DisplayString):
    """Custom type qbCrossConnPvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbCrossConnPvcName_Type.__name__ = "DisplayString"
_QbCrossConnPvcName_Object = MibTableColumn
qbCrossConnPvcName = _QbCrossConnPvcName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 8),
    _QbCrossConnPvcName_Type()
)
qbCrossConnPvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcName.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcName.setDescription("""\
The textual name of the connection as specified by a user. It provides a non-
volatile handle for this connection. The supplied name in the qbIotPortConnName
is associated with the same connection for as long as that conection remains.
""")


class _QbCrossConnPvcConnKind_Type(QbPvcConnKind):
    """Custom type qbCrossConnPvcConnKind based on QbPvcConnKind"""


_QbCrossConnPvcConnKind_Object = MibTableColumn
qbCrossConnPvcConnKind = _QbCrossConnPvcConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 9),
    _QbCrossConnPvcConnKind_Type()
)
qbCrossConnPvcConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcConnKind.setDescription("""\
The connection type. The following connection types can be provisioned on the
Enet port iotDs1ToIotDs11, iotE1ToIotE1, iotEnetToIotEnet, iotEnetToModEnet,
modE1ToModE1, modDs1ToModDs1,iotEnetToModEnet, iotE1ToModE1, iotDs1ToModDs1.
""")


class _QbCrossConnPvcLoopback_Type(QbEnableStatus):
    """Custom type qbCrossConnPvcLoopback based on QbEnableStatus"""


_QbCrossConnPvcLoopback_Object = MibTableColumn
qbCrossConnPvcLoopback = _QbCrossConnPvcLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 10),
    _QbCrossConnPvcLoopback_Type()
)
qbCrossConnPvcLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcLoopback.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcLoopback.setDescription("""\
This object enables loopback on this IOT to IOT port enedpoint. The endpoint on
which loopback is enabled is defined by qbIotPortCrossConnLoopbackEndpt.
""")


class _QbCrossConnPvcLoopbackSide_Type(Integer32):
    """Custom type qbCrossConnPvcLoopbackSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highIfIndexSide", 2),
          ("lowIfIndexSide", 1),
          ("none", 3))
    )


_QbCrossConnPvcLoopbackSide_Type.__name__ = "Integer32"
_QbCrossConnPvcLoopbackSide_Object = MibTableColumn
qbCrossConnPvcLoopbackSide = _QbCrossConnPvcLoopbackSide_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 11),
    _QbCrossConnPvcLoopbackSide_Type()
)
qbCrossConnPvcLoopbackSide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcLoopbackSide.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcLoopbackSide.setDescription("""\
This object defines loopback on the selected endpoint.
""")
_QbCrossConnPvcRowStatus_Type = RowStatus
_QbCrossConnPvcRowStatus_Object = MibTableColumn
qbCrossConnPvcRowStatus = _QbCrossConnPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 2, 3, 1, 12),
    _QbCrossConnPvcRowStatus_Type()
)
qbCrossConnPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCrossConnPvcRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcRowStatus.setDescription("""\
The status of the port connect entry. Changing the value of this object from
'active' to 'destroy' will remove this entry from the database. It will disrupt
traffic between two IOT packet interfaces.
""")
_QbPvcConnGroup_ObjectIdentity = ObjectIdentity
qbPvcConnGroup = _QbPvcConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3)
)
_QbPvcConnNum_Type = Integer32
_QbPvcConnNum_Object = MibScalar
qbPvcConnNum = _QbPvcConnNum_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 1),
    _QbPvcConnNum_Type()
)
qbPvcConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbPvcConnNum.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnNum.setDescription("""\
The total number of provisioned Enet to Enet, DS1 to DS1, E1 to E1 PVCs.
""")
_QbPvcConnTableLastTimeUpdate_Type = TimeTicks
_QbPvcConnTableLastTimeUpdate_Object = MibScalar
qbPvcConnTableLastTimeUpdate = _QbPvcConnTableLastTimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 2),
    _QbPvcConnTableLastTimeUpdate_Type()
)
qbPvcConnTableLastTimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbPvcConnTableLastTimeUpdate.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnTableLastTimeUpdate.setDescription("""\
The value of sysUpTime at the time of the last creation, deletion or
modification of an entry in the qbPvcConnTable. If the number of entries has
been unchanged since the last re-initialization of the agent, then this object
contains a zero value.
""")
_QbPvcNextConnId_Type = Integer32
_QbPvcNextConnId_Object = MibScalar
qbPvcNextConnId = _QbPvcNextConnId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 3),
    _QbPvcNextConnId_Type()
)
qbPvcNextConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbPvcNextConnId.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcNextConnId.setDescription("""\
This object returns the lowest unused connection Id.
""")
_QbPvcConnTable_Object = MibTable
qbPvcConnTable = _QbPvcConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4)
)
if mibBuilder.loadTexts:
    qbPvcConnTable.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnTable.setDescription("""\
This table contains the generic data pertaining to connections. For R3.0 this
is limited to ethernet, VLAN, GigE and IOT Enet cross connects.
""")
_QbPvcConnEntry_Object = MibTableRow
qbPvcConnEntry = _QbPvcConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1)
)
qbPvcConnEntry.setIndexNames(
    (0, "QB-PVC-MIB", "qbPvcConnId"),
)
if mibBuilder.loadTexts:
    qbPvcConnEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEntry.setDescription("""\
Each row provides data for a single connection.
""")
_QbPvcConnId_Type = Unsigned32
_QbPvcConnId_Object = MibTableColumn
qbPvcConnId = _QbPvcConnId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 1),
    _QbPvcConnId_Type()
)
qbPvcConnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnId.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnId.setDescription("""\
This is a unique identifier for this connection.
""")
_QbPvcConnName_Type = DisplayString
_QbPvcConnName_Object = MibTableColumn
qbPvcConnName = _QbPvcConnName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 2),
    _QbPvcConnName_Type()
)
qbPvcConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnName.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnName.setDescription("""\
This is the connection name.
""")


class _QbPvcConnAdminStatus_Type(AtmVorXAdminStatus):
    """Custom type qbPvcConnAdminStatus based on AtmVorXAdminStatus"""


_QbPvcConnAdminStatus_Object = MibTableColumn
qbPvcConnAdminStatus = _QbPvcConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 3),
    _QbPvcConnAdminStatus_Type()
)
qbPvcConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnAdminStatus.setDescription("""\
This is the connection admin status.
""")
_QbPvcConnOperStatus_Type = AtmVorXOperStatus
_QbPvcConnOperStatus_Object = MibTableColumn
qbPvcConnOperStatus = _QbPvcConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 4),
    _QbPvcConnOperStatus_Type()
)
qbPvcConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbPvcConnOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnOperStatus.setDescription("""\
This is the connection oper status.
""")
_QbPvcConnTxTd_Type = Integer32
_QbPvcConnTxTd_Object = MibTableColumn
qbPvcConnTxTd = _QbPvcConnTxTd_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 5),
    _QbPvcConnTxTd_Type()
)
qbPvcConnTxTd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnTxTd.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnTxTd.setDescription("""\
This is the traffic descriptor for traffic going from endpoint 1 to endpoint 2.
""")
_QbPvcConnRxTd_Type = Integer32
_QbPvcConnRxTd_Object = MibTableColumn
qbPvcConnRxTd = _QbPvcConnRxTd_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 6),
    _QbPvcConnRxTd_Type()
)
qbPvcConnRxTd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnRxTd.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnRxTd.setDescription("""\
This is the traffic descriptor for traffic going from endpoint 2 to endpoint 1.
""")
_QbPvcConnEndpt1_Type = ObjectIdentifier
_QbPvcConnEndpt1_Object = MibTableColumn
qbPvcConnEndpt1 = _QbPvcConnEndpt1_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 7),
    _QbPvcConnEndpt1_Type()
)
qbPvcConnEndpt1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnEndpt1.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEndpt1.setDescription("""\
This is connection endpoint 1. The following are examples of using this object:
ATM endpoint 200.33.43 (ATM interface index of 200, VPI 33, VCI 43) Ethernet
endpoint 5002 (Ifindex of ethernet port) Vlan endpoint 23.2 (vlanindex of 23
and vlan port 2) GigE endpoint 201.25 (GigE ifindex of 201 and vlanid 25)
""")
_QbPvcConnEndpt2_Type = ObjectIdentifier
_QbPvcConnEndpt2_Object = MibTableColumn
qbPvcConnEndpt2 = _QbPvcConnEndpt2_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 8),
    _QbPvcConnEndpt2_Type()
)
qbPvcConnEndpt2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnEndpt2.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEndpt2.setDescription("""\
This is connection endpoint 2( See examples in qbPvcEndpt1).
""")
_QbPvcConnEndpt1Type_Type = QbConnEndptType
_QbPvcConnEndpt1Type_Object = MibTableColumn
qbPvcConnEndpt1Type = _QbPvcConnEndpt1Type_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 9),
    _QbPvcConnEndpt1Type_Type()
)
qbPvcConnEndpt1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnEndpt1Type.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEndpt1Type.setDescription("""\
This is the type for endpoint 1.
""")
_QbPvcConnEndpt2Type_Type = QbConnEndptType
_QbPvcConnEndpt2Type_Object = MibTableColumn
qbPvcConnEndpt2Type = _QbPvcConnEndpt2Type_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 10),
    _QbPvcConnEndpt2Type_Type()
)
qbPvcConnEndpt2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnEndpt2Type.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEndpt2Type.setDescription("""\
This is the type for endpoint 2.
""")


class _QbPvcConnEndpt1Loop_Type(Integer32):
    """Custom type qbPvcConnEndpt1Loop based on Integer32"""
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


_QbPvcConnEndpt1Loop_Type.__name__ = "Integer32"
_QbPvcConnEndpt1Loop_Object = MibTableColumn
qbPvcConnEndpt1Loop = _QbPvcConnEndpt1Loop_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 11),
    _QbPvcConnEndpt1Loop_Type()
)
qbPvcConnEndpt1Loop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnEndpt1Loop.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEndpt1Loop.setDescription("""\
This controls PVC loopbacks on endpoint 1.
""")


class _QbPvcConnEndpt2Loop_Type(Integer32):
    """Custom type qbPvcConnEndpt2Loop based on Integer32"""
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


_QbPvcConnEndpt2Loop_Type.__name__ = "Integer32"
_QbPvcConnEndpt2Loop_Object = MibTableColumn
qbPvcConnEndpt2Loop = _QbPvcConnEndpt2Loop_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 12),
    _QbPvcConnEndpt2Loop_Type()
)
qbPvcConnEndpt2Loop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnEndpt2Loop.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnEndpt2Loop.setDescription("""\
This controls PVC loopbacks on endpoint 2.
""")
_QbPvcConnType_Type = QbPvcConnKind
_QbPvcConnType_Object = MibTableColumn
qbPvcConnType = _QbPvcConnType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 13),
    _QbPvcConnType_Type()
)
qbPvcConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnType.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnType.setDescription("""\
This is the connection type.
""")
_QbPvcConnRowStatus_Type = RowStatus
_QbPvcConnRowStatus_Object = MibTableColumn
qbPvcConnRowStatus = _QbPvcConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 4, 1, 14),
    _QbPvcConnRowStatus_Type()
)
qbPvcConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbPvcConnRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnRowStatus.setDescription("""\
The row status column for this Vlan. This OBJECT can be set to: createAndGo(4)
destroy(6) The following values may be read: active(1) Setting this object to
createAndGo(4) causes the agent to attempt to create and commit the row based
on the contents of the objects in the row. If all necessary information is
present in the row and the values are acceptable to the agent, the agent will
change the status to active(1). If any of the necessary objects are not
available, the agent will reject the creation request. When a row is created in
this table, there will also be 2 corresponding rows created in the table
qbPvcMappingTable. Setting this object to destroy(6) will remove the
corresponding entry in this table, and disable data traffic. When this row is
deleted the 2 corresponding rows in the qbPvcMappingTable will also be deleted.
""")
_QbPvcConnMappingTable_Object = MibTable
qbPvcConnMappingTable = _QbPvcConnMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 5)
)
if mibBuilder.loadTexts:
    qbPvcConnMappingTable.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnMappingTable.setDescription("""\
This table contains the data to map from the first index of the connection
endpoint to connection ID.
""")
_QbPvcConnMappingEntry_Object = MibTableRow
qbPvcConnMappingEntry = _QbPvcConnMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 5, 1)
)
qbPvcConnMappingEntry.setIndexNames(
    (0, "QB-PVC-MIB", "qbPvcConnMappingType"),
    (0, "QB-PVC-MIB", "qbPvcConnMappingIndex"),
    (0, "QB-PVC-MIB", "qbPvcConnMappingId"),
)
if mibBuilder.loadTexts:
    qbPvcConnMappingEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnMappingEntry.setDescription("""\
Each row maps from an specific endpoint to a specific connection.
""")
_QbPvcConnMappingType_Type = QbConnEndptType
_QbPvcConnMappingType_Object = MibTableColumn
qbPvcConnMappingType = _QbPvcConnMappingType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 5, 1, 1),
    _QbPvcConnMappingType_Type()
)
qbPvcConnMappingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbPvcConnMappingType.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnMappingType.setDescription("""\
This is the type of endpoint that the next index refers to.
""")
_QbPvcConnMappingIndex_Type = Unsigned32
_QbPvcConnMappingIndex_Object = MibTableColumn
qbPvcConnMappingIndex = _QbPvcConnMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 5, 1, 2),
    _QbPvcConnMappingIndex_Type()
)
qbPvcConnMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbPvcConnMappingIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnMappingIndex.setDescription("""\
This is the first index for the connection endpoint. For most connection
endpoint this will be the ifIndex, however for VLAN endpoints, this will be the
VLAN index.
""")
_QbPvcConnMappingId_Type = Unsigned32
_QbPvcConnMappingId_Object = MibTableColumn
qbPvcConnMappingId = _QbPvcConnMappingId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 5, 1, 3),
    _QbPvcConnMappingId_Type()
)
qbPvcConnMappingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbPvcConnMappingId.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnMappingId.setDescription("""\
This is the connection Id for the connection this entry pertains to.
""")
_QbPvcConnMappingName_Type = DisplayString
_QbPvcConnMappingName_Object = MibTableColumn
qbPvcConnMappingName = _QbPvcConnMappingName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 1, 3, 5, 1, 4),
    _QbPvcConnMappingName_Type()
)
qbPvcConnMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbPvcConnMappingName.setStatus("current")
if mibBuilder.loadTexts:
    qbPvcConnMappingName.setDescription("""\
This is the connection name.
""")
_QbPvcNotifications_ObjectIdentity = ObjectIdentity
qbPvcNotifications = _QbPvcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 2)
)
_QbPvcNotificationPrefix_ObjectIdentity = ObjectIdentity
qbPvcNotificationPrefix = _QbPvcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 2, 0)
)
_QbPvcConformance_ObjectIdentity = ObjectIdentity
qbPvcConformance = _QbPvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 3)
)
_QbPvcCompliances_ObjectIdentity = ObjectIdentity
qbPvcCompliances = _QbPvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 3, 1)
)
_QbPvcGroups_ObjectIdentity = ObjectIdentity
qbPvcGroups = _QbPvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 3, 2)
)

# Managed Objects groups

qbEnetPvcGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 3, 2, 1)
)
qbEnetPvcGroupInfo.setObjects(
      *(("QB-PVC-MIB", "qbEnetPvcAtmIndex"),
        ("QB-PVC-MIB", "qbEnetPvcVpi"),
        ("QB-PVC-MIB", "qbEnetPvcVci"),
        ("QB-PVC-MIB", "qbEnetPvcName"),
        ("QB-PVC-MIB", "qbEnetPvcRxTrafficDescrIndex"),
        ("QB-PVC-MIB", "qbEnetPvcTxTrafficDescrIndex"),
        ("QB-PVC-MIB", "qbEnetPvcAdminStatus"),
        ("QB-PVC-MIB", "qbEnetPvcOperStatus"),
        ("QB-PVC-MIB", "qbEnetPvcLastChange"),
        ("QB-PVC-MIB", "qbEnetPvcConnKind"),
        ("QB-PVC-MIB", "qbEnetPvcLoopback"),
        ("QB-PVC-MIB", "qbEnetPvcLoopbackSide"),
        ("QB-PVC-MIB", "qbEnetPvcRowStatus"))
)
if mibBuilder.loadTexts:
    qbEnetPvcGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbEnetPvcGroupInfo.setDescription("""\
The set of all accessible objects in the ATM PVC Network Group of this MIB.
""")

qbCrossConnPvcGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 3, 2, 2)
)
qbCrossConnPvcGroupInfo.setObjects(
      *(("QB-PVC-MIB", "qbCrossConnPvcConnKind"),
        ("QB-PVC-MIB", "qbCrossConnPvcAdminStatus"),
        ("QB-PVC-MIB", "qbCrossConnPvcOperStatus"),
        ("QB-PVC-MIB", "qbCrossConnPvcLastChange"),
        ("QB-PVC-MIB", "qbCrossConnPvcRxTrafficDescrIndex"),
        ("QB-PVC-MIB", "qbCrossConnPvcTxTrafficDescrIndex"),
        ("QB-PVC-MIB", "qbCrossConnPvcName"),
        ("QB-PVC-MIB", "qbCrossConnPvcConnKind"),
        ("QB-PVC-MIB", "qbCrossConnPvcLoopback"),
        ("QB-PVC-MIB", "qbCrossConnPvcLoopbackSide"),
        ("QB-PVC-MIB", "qbCrossConnPvcRowStatus"))
)
if mibBuilder.loadTexts:
    qbCrossConnPvcGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbCrossConnPvcGroupInfo.setDescription("""\
The set of all accessible objects in the Cross-Connect PVC Group of this MIB.
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbPvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbPvcCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbPvcCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-PVC-MIB",
    **{"QbConnEndptType": QbConnEndptType,
       "qbPvcMIB": qbPvcMIB,
       "qbPvcObjects": qbPvcObjects,
       "qbEnetPvcGroup": qbEnetPvcGroup,
       "qbEnetPvcNumber": qbEnetPvcNumber,
       "qbEnePvcLastTimeUpdate": qbEnePvcLastTimeUpdate,
       "qbEnetPvcTable": qbEnetPvcTable,
       "qbEnetPvcEntry": qbEnetPvcEntry,
       "qbEnetPvcIndex": qbEnetPvcIndex,
       "qbEnetPvcAtmIndex": qbEnetPvcAtmIndex,
       "qbEnetPvcVpi": qbEnetPvcVpi,
       "qbEnetPvcVci": qbEnetPvcVci,
       "qbEnetPvcName": qbEnetPvcName,
       "qbEnetPvcRxTrafficDescrIndex": qbEnetPvcRxTrafficDescrIndex,
       "qbEnetPvcTxTrafficDescrIndex": qbEnetPvcTxTrafficDescrIndex,
       "qbEnetPvcAdminStatus": qbEnetPvcAdminStatus,
       "qbEnetPvcOperStatus": qbEnetPvcOperStatus,
       "qbEnetPvcLastChange": qbEnetPvcLastChange,
       "qbEnetPvcConnKind": qbEnetPvcConnKind,
       "qbEnetPvcLoopback": qbEnetPvcLoopback,
       "qbEnetPvcLoopbackSide": qbEnetPvcLoopbackSide,
       "qbEnetPvcRowStatus": qbEnetPvcRowStatus,
       "qbCrossConnPvcGroup": qbCrossConnPvcGroup,
       "qbCrossConnPvcNumber": qbCrossConnPvcNumber,
       "qbCrossConnPvcLastTimeUpdate": qbCrossConnPvcLastTimeUpdate,
       "qbCrossConnPvcTable": qbCrossConnPvcTable,
       "qbCrossConnPvcEntry": qbCrossConnPvcEntry,
       "qbCrossConnPvcLowIfIndex": qbCrossConnPvcLowIfIndex,
       "qbCrossConnPvcHighIfIndex": qbCrossConnPvcHighIfIndex,
       "qbCrossConnPvcAdminStatus": qbCrossConnPvcAdminStatus,
       "qbCrossConnPvcOperStatus": qbCrossConnPvcOperStatus,
       "qbCrossConnPvcLastChange": qbCrossConnPvcLastChange,
       "qbCrossConnPvcRxTrafficDescrIndex": qbCrossConnPvcRxTrafficDescrIndex,
       "qbCrossConnPvcTxTrafficDescrIndex": qbCrossConnPvcTxTrafficDescrIndex,
       "qbCrossConnPvcName": qbCrossConnPvcName,
       "qbCrossConnPvcConnKind": qbCrossConnPvcConnKind,
       "qbCrossConnPvcLoopback": qbCrossConnPvcLoopback,
       "qbCrossConnPvcLoopbackSide": qbCrossConnPvcLoopbackSide,
       "qbCrossConnPvcRowStatus": qbCrossConnPvcRowStatus,
       "qbPvcConnGroup": qbPvcConnGroup,
       "qbPvcConnNum": qbPvcConnNum,
       "qbPvcConnTableLastTimeUpdate": qbPvcConnTableLastTimeUpdate,
       "qbPvcNextConnId": qbPvcNextConnId,
       "qbPvcConnTable": qbPvcConnTable,
       "qbPvcConnEntry": qbPvcConnEntry,
       "qbPvcConnId": qbPvcConnId,
       "qbPvcConnName": qbPvcConnName,
       "qbPvcConnAdminStatus": qbPvcConnAdminStatus,
       "qbPvcConnOperStatus": qbPvcConnOperStatus,
       "qbPvcConnTxTd": qbPvcConnTxTd,
       "qbPvcConnRxTd": qbPvcConnRxTd,
       "qbPvcConnEndpt1": qbPvcConnEndpt1,
       "qbPvcConnEndpt2": qbPvcConnEndpt2,
       "qbPvcConnEndpt1Type": qbPvcConnEndpt1Type,
       "qbPvcConnEndpt2Type": qbPvcConnEndpt2Type,
       "qbPvcConnEndpt1Loop": qbPvcConnEndpt1Loop,
       "qbPvcConnEndpt2Loop": qbPvcConnEndpt2Loop,
       "qbPvcConnType": qbPvcConnType,
       "qbPvcConnRowStatus": qbPvcConnRowStatus,
       "qbPvcConnMappingTable": qbPvcConnMappingTable,
       "qbPvcConnMappingEntry": qbPvcConnMappingEntry,
       "qbPvcConnMappingType": qbPvcConnMappingType,
       "qbPvcConnMappingIndex": qbPvcConnMappingIndex,
       "qbPvcConnMappingId": qbPvcConnMappingId,
       "qbPvcConnMappingName": qbPvcConnMappingName,
       "qbPvcNotifications": qbPvcNotifications,
       "qbPvcNotificationPrefix": qbPvcNotificationPrefix,
       "qbPvcConformance": qbPvcConformance,
       "qbPvcCompliances": qbPvcCompliances,
       "qbPvcCompliance": qbPvcCompliance,
       "qbPvcGroups": qbPvcGroups,
       "qbEnetPvcGroupInfo": qbEnetPvcGroupInfo,
       "qbCrossConnPvcGroupInfo": qbCrossConnPvcGroupInfo}
)
