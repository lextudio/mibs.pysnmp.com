"""SNMP MIB module (QB-DWS-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-DWS-MIB
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

(qbSysIotSerialNumber,
 qbSysModuleSlot) = mibBuilder.importSymbols(
    "QBSYS-SYSTEM-MIB",
    "qbSysIotSerialNumber",
    "qbSysModuleSlot")

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

(TimeStamp,
 DisplayString,
 RowStatus,
 TruthValue,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TimeStamp",
    "DisplayString",
    "RowStatus",
    "TruthValue",
    "TextualConvention")


# MODULE-IDENTITY

qbDwsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3)
)
qbDwsMIB.setLastUpdated("0107071255Z")
if mibBuilder.loadTexts:
    qbDwsMIB.setOrganization("""\
Quantum Bridge Communications, Inc.
""")
qbDwsMIB.setContactInfo("""\
support@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbDwsMIB.setDescription("""\
This module defines additional objects for the provisioning and management of
DWS links in Quantum bridge devices.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class QbPvcConnKind(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("atmPvcToPvc", 1),
          ("atmPvpToPvp", 2),
          ("atmToDs1", 24),
          ("atmToE1", 25),
          ("atmToEnet", 23),
          ("ds1ToDs1", 30),
          ("ds1ToM13", 29),
          ("ds1ToVc11", 28),
          ("ds1ToVt15", 26),
          ("e1ToE1", 31),
          ("e1ToVc12", 27),
          ("enetToEnet", 32),
          ("iotDs1ToAtm", 4),
          ("iotDs1ToDs1", 33),
          ("iotDs1ToIotDs1", 15),
          ("iotDs1ToM13", 21),
          ("iotDs1ToVc11", 18),
          ("iotDs1ToVc12", 13),
          ("iotDs1ToVt15", 11),
          ("iotE1ToAtm", 3),
          ("iotE1ToE1", 34),
          ("iotE1ToIotE1", 14),
          ("iotE1ToVc12", 12),
          ("iotE1ToVt15", 10),
          ("iotEnetToAtm", 5),
          ("iotEnetToEnet", 35),
          ("iotEnetToIotEnet", 16),
          ("m13ToAtm", 20),
          ("m13ToM13", 22),
          ("unknown", 0),
          ("vc11ToAtm", 17),
          ("vc11ToVc11", 19),
          ("vc12ToAtm", 7),
          ("vc12ToVc12", 9),
          ("vlanToAtm", 36),
          ("vlanToEnet", 39),
          ("vlanToGige", 37),
          ("vlanToIotEnet", 38),
          ("vt15ToAtm", 6),
          ("vt15Vt15", 8))
    )

    if mibBuilder.loadTexts:
        description = """\
A connection type that can be provisioned.
"""


class QbBitRate(TextualConvention, Gauge32):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
A data rate in bits/second.
"""


class QbSerialNum(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )

    if mibBuilder.loadTexts:
        description = """\
The IOT serial number.
"""


class QbDwsIfStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("ok", 1),
          ("rxFailure", 2),
          ("txFailure", 3),
          ("unknown", 4))
    )

    if mibBuilder.loadTexts:
        description = """\
The status of the DWS Interface
"""


class QbDwsSrvStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("almostFull", 3),
          ("avilable", 1),
          ("empty", 2),
          ("overflown", 4))
    )

    if mibBuilder.loadTexts:
        description = """\
The service status of the DWS Interface
"""


class QbAtmAal5EncapsType(TextualConvention, Integer32):
    status = "current"
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
        *(("qbBridgedPropEncaps", 4),
          ("qbBridgedProto8023EncapFcs", 2),
          ("qbBridgedProto8023EncapsNoFcs", 3),
          ("qbBridgedProtoLLCEncapsNoFcs", 5),
          ("qbRoutedEncapsNoHdrNoFcs", 6),
          ("qbVcMultiplexRoutedProto", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of data encapsulation used over the AAL5 layer.
"""


class QbEnableStatus(TextualConvention, Integer32):
    status = "current"
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

    if mibBuilder.loadTexts:
        description = """\
enable(1) or disable(1) operations.
"""


# MIB Managed Objects in the order of their OIDs

_QbDwsObjects_ObjectIdentity = ObjectIdentity
qbDwsObjects = _QbDwsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1)
)
_QbDwsNetGroup_ObjectIdentity = ObjectIdentity
qbDwsNetGroup = _QbDwsNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1)
)


class _QbDwsSysRangeMode_Type(Integer32):
    """Custom type qbDwsSysRangeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rangeAll", 2),
          ("ready", 1))
    )


_QbDwsSysRangeMode_Type.__name__ = "Integer32"
_QbDwsSysRangeMode_Object = MibScalar
qbDwsSysRangeMode = _QbDwsSysRangeMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 1),
    _QbDwsSysRangeMode_Type()
)
qbDwsSysRangeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDwsSysRangeMode.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsSysRangeMode.setDescription("""\
The object that indicates a system wide range mode. When read, this object
always returns the value 'ready(1)'. Setting this object to rangeAll(2) causes
ranging of all IOTs that connect to this OAS.
""")


class _QbSysIotRecoverMode_Type(Integer32):
    """Custom type qbSysIotRecoverMode based on Integer32"""
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


_QbSysIotRecoverMode_Type.__name__ = "Integer32"
_QbSysIotRecoverMode_Object = MibScalar
qbSysIotRecoverMode = _QbSysIotRecoverMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 2),
    _QbSysIotRecoverMode_Type()
)
qbSysIotRecoverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysIotRecoverMode.setStatus("current")
if mibBuilder.loadTexts:
    qbSysIotRecoverMode.setDescription("""\
The object allows to set the IOT auto-recovery feature on the IOAS. Auto-
recovery is global in scope, so when it is enabled, auto-recovery is attempted
for all IOTs that are attached to the IOAS.
""")
_QbDwsNetTable_Object = MibTable
qbDwsNetTable = _QbDwsNetTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qbDwsNetTable.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTable.setDescription("""\
The Quantum Bridge PON Interface Table contains extensions of the standard MIB
Interface Table, one entry per IOAS DWS interface. The table contains read-only
objects and shows MIB objects for every Network interface
""")
_QbDwsNetEntry_Object = MibTableRow
qbDwsNetEntry = _QbDwsNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1)
)
qbDwsNetEntry.setIndexNames(
    (0, "QB-DWS-MIB", "qbDwsNetIfIndex"),
)
if mibBuilder.loadTexts:
    qbDwsNetEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetEntry.setDescription("""\
An entry in the Quantum Bridge DWS Interface Table that contains the Network
interface's specific objects.
""")
_QbDwsNetIfIndex_Type = InterfaceIndex
_QbDwsNetIfIndex_Object = MibTableColumn
qbDwsNetIfIndex = _QbDwsNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 1),
    _QbDwsNetIfIndex_Type()
)
qbDwsNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetIfIndex.setDescription("""\
The value of this object is the same as the corresponding ifIndex of the
Network Interface in the ifTable.
""")
_QbDwsNetBw_Type = QbBitRate
_QbDwsNetBw_Object = MibTableColumn
qbDwsNetBw = _QbDwsNetBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 2),
    _QbDwsNetBw_Type()
)
qbDwsNetBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetBw.setUnits("Bits per second")
if mibBuilder.loadTexts:
    qbDwsNetBw.setDescription("""\
The object indicates the total bandwidth rate that is available for reservation
on this interface. This object is specified in Bits per second.
""")
_QbDwsNetAllocatedBw_Type = QbBitRate
_QbDwsNetAllocatedBw_Object = MibTableColumn
qbDwsNetAllocatedBw = _QbDwsNetAllocatedBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 3),
    _QbDwsNetAllocatedBw_Type()
)
qbDwsNetAllocatedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedBw.setUnits("Bits per second")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedBw.setDescription("""\
The object indicates the total bandwidth rate that is currently subscribed. The
subscribed bandwidth rate consists of the bandwidth rate allocated for all
provisoned connections. This object is specified in Bits per sec(Bps).
""")
_QbDwsNetAvailableBw_Type = QbBitRate
_QbDwsNetAvailableBw_Object = MibTableColumn
qbDwsNetAvailableBw = _QbDwsNetAvailableBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 4),
    _QbDwsNetAvailableBw_Type()
)
qbDwsNetAvailableBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetAvailableBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetAvailableBw.setUnits("Bits per second")
if mibBuilder.loadTexts:
    qbDwsNetAvailableBw.setDescription("""\
The portion of this interface's capacity in bits per sec that is available for
data traffic. This variable is adjusted for the allocated bandwidth. The
formula for calculating this value is qbDwsNetBw - qbDwsNetAllocatedBw This
object is specified in Bps.
""")
_QbDwsNetAllocatedUbrBw_Type = QbBitRate
_QbDwsNetAllocatedUbrBw_Object = MibTableColumn
qbDwsNetAllocatedUbrBw = _QbDwsNetAllocatedUbrBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 5),
    _QbDwsNetAllocatedUbrBw_Type()
)
qbDwsNetAllocatedUbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedUbrBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedUbrBw.setUnits("Bits per second")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedUbrBw.setDescription("""\
The object indicates the total number of bandwidth that are currently allocated
for packet/ubr traffic. This object is specified in Bps.
""")
_QbDwsNetAllocatedCbrBw_Type = QbBitRate
_QbDwsNetAllocatedCbrBw_Object = MibTableColumn
qbDwsNetAllocatedCbrBw = _QbDwsNetAllocatedCbrBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 6),
    _QbDwsNetAllocatedCbrBw_Type()
)
qbDwsNetAllocatedCbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedCbrBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedCbrBw.setUnits("Bits per second")
if mibBuilder.loadTexts:
    qbDwsNetAllocatedCbrBw.setDescription("""\
The object indicates the total number of bandwidth that is currently allocated
for CBR traffic. This object is specified in Bps.
""")
_QbDwsNetNumCbrConn_Type = Integer32
_QbDwsNetNumCbrConn_Object = MibTableColumn
qbDwsNetNumCbrConn = _QbDwsNetNumCbrConn_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 7),
    _QbDwsNetNumCbrConn_Type()
)
qbDwsNetNumCbrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetNumCbrConn.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetNumCbrConn.setDescription("""\
The object indicates the total number of inactive and in-service CBR
connections that are currently provisioned on this interface.
""")
_QbDwsNetNumUbrConn_Type = Integer32
_QbDwsNetNumUbrConn_Object = MibTableColumn
qbDwsNetNumUbrConn = _QbDwsNetNumUbrConn_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 8),
    _QbDwsNetNumUbrConn_Type()
)
qbDwsNetNumUbrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetNumUbrConn.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetNumUbrConn.setDescription("""\
The object indicates the total number of inactive and in-serice UBR connections
that are currently provisioned on this interface.
""")
_QbDwsNetNumIot_Type = Integer32
_QbDwsNetNumIot_Object = MibTableColumn
qbDwsNetNumIot = _QbDwsNetNumIot_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 9),
    _QbDwsNetNumIot_Type()
)
qbDwsNetNumIot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetNumIot.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetNumIot.setDescription("""\
The number of IOTs that are provisioned on the Network interface.
""")
_QbDwsNetTxStatus_Type = QbDwsIfStatus
_QbDwsNetTxStatus_Object = MibTableColumn
qbDwsNetTxStatus = _QbDwsNetTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 10),
    _QbDwsNetTxStatus_Type()
)
qbDwsNetTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetTxStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTxStatus.setDescription("""\
This objects indicates the status of the DWS transmitter. The trap is generated
by the SNMP agent when the IOAS DWS transmitter problem is detected. The trap
contains the DWS module interface index.
""")
_QbDwsNetTxStatusLastChange_Type = TimeStamp
_QbDwsNetTxStatusLastChange_Object = MibTableColumn
qbDwsNetTxStatusLastChange = _QbDwsNetTxStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 11),
    _QbDwsNetTxStatusLastChange_Type()
)
qbDwsNetTxStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetTxStatusLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTxStatusLastChange.setDescription("""\
The value of MIB II's sysUpTime object at the time this DWS Interface entered
its current status state.
""")
_QbDwsNetLosIotAddr_Type = Integer32
_QbDwsNetLosIotAddr_Object = MibTableColumn
qbDwsNetLosIotAddr = _QbDwsNetLosIotAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 12),
    _QbDwsNetLosIotAddr_Type()
)
qbDwsNetLosIotAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetLosIotAddr.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetLosIotAddr.setDescription("""\
The object contains the address of the IOT for which a Los condition is
detected. This indicates that no signal was detected within the expected time
slot window. Note: The Los indication at the IOAS DWS card is a signal that an
IOT is non-functioning.
""")
_QbDwsNetLosIotTime_Type = TimeStamp
_QbDwsNetLosIotTime_Object = MibTableColumn
qbDwsNetLosIotTime = _QbDwsNetLosIotTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 13),
    _QbDwsNetLosIotTime_Type()
)
qbDwsNetLosIotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetLosIotTime.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetLosIotTime.setDescription("""\
The value of MIB II's sysUpTime object at the time when the qbDwsNetIotLos
condition was detected.
""")
_QbDwsNetEncryptStatus_Type = TruthValue
_QbDwsNetEncryptStatus_Object = MibTableColumn
qbDwsNetEncryptStatus = _QbDwsNetEncryptStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 14),
    _QbDwsNetEncryptStatus_Type()
)
qbDwsNetEncryptStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDwsNetEncryptStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetEncryptStatus.setDescription("""\
The object that enables and disables encryption on this interface.
""")


class _QbDwsNetRangeMode_Type(Integer32):
    """Custom type qbDwsNetRangeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rangeAll", 2),
          ("ready", 1))
    )


_QbDwsNetRangeMode_Type.__name__ = "Integer32"
_QbDwsNetRangeMode_Object = MibTableColumn
qbDwsNetRangeMode = _QbDwsNetRangeMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 15),
    _QbDwsNetRangeMode_Type()
)
qbDwsNetRangeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDwsNetRangeMode.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetRangeMode.setDescription("""\
The object that indicates a range mode. When read, this object always returns
the value 'ready(1)'. Setting this object to rangeAll(2) causes ranging of all
IOTs connected to this interface.
""")
_QbDwsNetRxTsCount_Type = Counter32
_QbDwsNetRxTsCount_Object = MibTableColumn
qbDwsNetRxTsCount = _QbDwsNetRxTsCount_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 16),
    _QbDwsNetRxTsCount_Type()
)
qbDwsNetRxTsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetRxTsCount.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetRxTsCount.setDescription("""\
The total number of successfully received time slots.
""")
_QbDwsNetTxTsCount_Type = Counter32
_QbDwsNetTxTsCount_Object = MibTableColumn
qbDwsNetTxTsCount = _QbDwsNetTxTsCount_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 17),
    _QbDwsNetTxTsCount_Type()
)
qbDwsNetTxTsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetTxTsCount.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTxTsCount.setDescription("""\
The total number of successfully transmitted time slots.
""")
_QbDwsNetRxMissingTs_Type = Counter32
_QbDwsNetRxMissingTs_Object = MibTableColumn
qbDwsNetRxMissingTs = _QbDwsNetRxMissingTs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 18),
    _QbDwsNetRxMissingTs_Type()
)
qbDwsNetRxMissingTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetRxMissingTs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetRxMissingTs.setDescription("""\
The number received time slots that have been missed.
""")
_QbDwsNetRxIllegalTs_Type = Counter32
_QbDwsNetRxIllegalTs_Object = MibTableColumn
qbDwsNetRxIllegalTs = _QbDwsNetRxIllegalTs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 19),
    _QbDwsNetRxIllegalTs_Type()
)
qbDwsNetRxIllegalTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetRxIllegalTs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetRxIllegalTs.setDescription("""\
The number illegal received time slots that have been detected.
""")
_QbDwsNetTxJabberTs_Type = Counter32
_QbDwsNetTxJabberTs_Object = MibTableColumn
qbDwsNetTxJabberTs = _QbDwsNetTxJabberTs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 20),
    _QbDwsNetTxJabberTs_Type()
)
qbDwsNetTxJabberTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetTxJabberTs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTxJabberTs.setDescription("""\
The number jabber transmitted time slots that have been detected.
""")
_QbDwsNetTxOutOfFrameTs_Type = Counter32
_QbDwsNetTxOutOfFrameTs_Object = MibTableColumn
qbDwsNetTxOutOfFrameTs = _QbDwsNetTxOutOfFrameTs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 21),
    _QbDwsNetTxOutOfFrameTs_Type()
)
qbDwsNetTxOutOfFrameTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetTxOutOfFrameTs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTxOutOfFrameTs.setDescription("""\
The number out of frame transmitted timeslots that have been detected.
""")
_QbDwsNetTxHdrCrcTsErrs_Type = Counter32
_QbDwsNetTxHdrCrcTsErrs_Object = MibTableColumn
qbDwsNetTxHdrCrcTsErrs = _QbDwsNetTxHdrCrcTsErrs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 22),
    _QbDwsNetTxHdrCrcTsErrs_Type()
)
qbDwsNetTxHdrCrcTsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetTxHdrCrcTsErrs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetTxHdrCrcTsErrs.setDescription("""\
The number transmitted timeslots with the header protection error that have
been detected.
""")
_QbDwsNetOamRequests_Type = Counter32
_QbDwsNetOamRequests_Object = MibTableColumn
qbDwsNetOamRequests = _QbDwsNetOamRequests_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 23),
    _QbDwsNetOamRequests_Type()
)
qbDwsNetOamRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetOamRequests.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetOamRequests.setDescription("""\
The number of OAM requests. These OAM requests are originated by the IOAS and
sent to downstream IOTs.
""")
_QbDwsNetOamResponses_Type = Counter32
_QbDwsNetOamResponses_Object = MibTableColumn
qbDwsNetOamResponses = _QbDwsNetOamResponses_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 24),
    _QbDwsNetOamResponses_Type()
)
qbDwsNetOamResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetOamResponses.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetOamResponses.setDescription("""\
The number of OAM responses. These responses are generated by IOTs in response
to downstream requests.
""")
_QbDwsNetOamEvents_Type = Counter32
_QbDwsNetOamEvents_Object = MibTableColumn
qbDwsNetOamEvents = _QbDwsNetOamEvents_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 25),
    _QbDwsNetOamEvents_Type()
)
qbDwsNetOamEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetOamEvents.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetOamEvents.setDescription("""\
The number of OAM events. These events are originated by IOT devices to signal
abnormal conditions.
""")
_QbDwsNetOamBadMsgs_Type = Counter32
_QbDwsNetOamBadMsgs_Object = MibTableColumn
qbDwsNetOamBadMsgs = _QbDwsNetOamBadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 26),
    _QbDwsNetOamBadMsgs_Type()
)
qbDwsNetOamBadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsNetOamBadMsgs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetOamBadMsgs.setDescription("""\
The total number of bad OAM messages.
""")


class _QbDwsNetLoopBack_Type(Integer32):
    """Custom type qbDwsNetLoopBack based on Integer32"""
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


_QbDwsNetLoopBack_Type.__name__ = "Integer32"
_QbDwsNetLoopBack_Object = MibTableColumn
qbDwsNetLoopBack = _QbDwsNetLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 1, 3, 1, 27),
    _QbDwsNetLoopBack_Type()
)
qbDwsNetLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDwsNetLoopBack.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetLoopBack.setDescription("""\
The Loopback status of this DWS port. Writing configures the port to go into
the loopback mode. When placed in loopback mode the DWS port does a 'payload'
loopback.
""")
_QbDwsIotIfGroup_ObjectIdentity = ObjectIdentity
qbDwsIotIfGroup = _QbDwsIotIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2)
)
_QbDwsIotIfConfTable_Object = MibTable
qbDwsIotIfConfTable = _QbDwsIotIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qbDwsIotIfConfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfConfTable.setDescription("""\
The Quantum DWS interface table. One entry per each IOT's DWS interface.
""")
_QbDwsIotIfConfEntry_Object = MibTableRow
qbDwsIotIfConfEntry = _QbDwsIotIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1)
)
qbDwsIotIfConfEntry.setIndexNames(
    (0, "QB-DWS-MIB", "qbDwsIotIfIndex"),
)
if mibBuilder.loadTexts:
    qbDwsIotIfConfEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfConfEntry.setDescription("""\
An entry in the Quantum Bridge DWS Interface Table. The ifIndex is a DWS
interface index from ifTable.
""")
_QbDwsIotIfIndex_Type = InterfaceIndex
_QbDwsIotIfIndex_Object = MibTableColumn
qbDwsIotIfIndex = _QbDwsIotIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 1),
    _QbDwsIotIfIndex_Type()
)
qbDwsIotIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbDwsIotIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfIndex.setDescription("""\
The ifIndex of this interface in the ifTable.
""")
_QbDwsIotNetIfIndex_Type = InterfaceIndex
_QbDwsIotNetIfIndex_Object = MibTableColumn
qbDwsIotNetIfIndex = _QbDwsIotNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 2),
    _QbDwsIotNetIfIndex_Type()
)
qbDwsIotNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotNetIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotNetIfIndex.setDescription("""\
The ifIndex of this PON interface in the ifTable.
""")
_QbDwsIotIfAddr_Type = Integer32
_QbDwsIotIfAddr_Object = MibTableColumn
qbDwsIotIfAddr = _QbDwsIotIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 3),
    _QbDwsIotIfAddr_Type()
)
qbDwsIotIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfAddr.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfAddr.setDescription("""\
The IOT terminal address.
""")
_QbDwsIotIfConfPowerLevel_Type = Integer32
_QbDwsIotIfConfPowerLevel_Object = MibTableColumn
qbDwsIotIfConfPowerLevel = _QbDwsIotIfConfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 4),
    _QbDwsIotIfConfPowerLevel_Type()
)
qbDwsIotIfConfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfConfPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfConfPowerLevel.setDescription("""\
The DWS interface's power level.
""")
_QbDwsIotIfConfEqDelay_Type = TimeTicks
_QbDwsIotIfConfEqDelay_Object = MibTableColumn
qbDwsIotIfConfEqDelay = _QbDwsIotIfConfEqDelay_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 5),
    _QbDwsIotIfConfEqDelay_Type()
)
qbDwsIotIfConfEqDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfConfEqDelay.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfConfEqDelay.setDescription("""\
The equal Delay time (in hundredths of a second).
""")
_QbDwsIotIfConfWaveLength_Type = Integer32
_QbDwsIotIfConfWaveLength_Object = MibTableColumn
qbDwsIotIfConfWaveLength = _QbDwsIotIfConfWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 6),
    _QbDwsIotIfConfWaveLength_Type()
)
qbDwsIotIfConfWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfConfWaveLength.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfConfWaveLength.setDescription("""\
The wave length value for this DWS interface.
""")
_QbDwsIotIfUbrBw_Type = QbBitRate
_QbDwsIotIfUbrBw_Object = MibTableColumn
qbDwsIotIfUbrBw = _QbDwsIotIfUbrBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 7),
    _QbDwsIotIfUbrBw_Type()
)
qbDwsIotIfUbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfUbrBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfUbrBw.setDescription("""\
The object indicates the total UBR bandwidth rate that is reserved for a given
IOT interface. This object is specified in Bits per second.
""")
_QbDwsIotIfCbrBw_Type = QbBitRate
_QbDwsIotIfCbrBw_Object = MibTableColumn
qbDwsIotIfCbrBw = _QbDwsIotIfCbrBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 8),
    _QbDwsIotIfCbrBw_Type()
)
qbDwsIotIfCbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfCbrBw.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfCbrBw.setDescription("""\
The object indicates the total CBR bandwidth rate that is reserved for a given
IOT interface. This object is specified in Bits per second.
""")
_QbDwsIotIfTxStatus_Type = QbDwsIfStatus
_QbDwsIotIfTxStatus_Object = MibTableColumn
qbDwsIotIfTxStatus = _QbDwsIotIfTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 9),
    _QbDwsIotIfTxStatus_Type()
)
qbDwsIotIfTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfTxStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfTxStatus.setDescription("""\
This objects indicates the status of the IOT DWS Port. The txFailure(2) state
indicates that the laser transmitter failed. The rxFailure(3) state indicates
that no signal was detected within the expected timeslot window. It signals
that there is a problem with the DWS port receiver. When this object is
changed, the ifOperStatus and ifLastChnaged of this interface must also be
changed. Note: The trap is generated by the SNMP agent when the IOT DWS status
is changed. The trap contains the IOAS DWS card interface index and IOT
address.
""")
_QbDwsIotIfTxStatusLastChange_Type = TimeStamp
_QbDwsIotIfTxStatusLastChange_Object = MibTableColumn
qbDwsIotIfTxStatusLastChange = _QbDwsIotIfTxStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 10),
    _QbDwsIotIfTxStatusLastChange_Type()
)
qbDwsIotIfTxStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfTxStatusLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfTxStatusLastChange.setDescription("""\
The value of MIB II's sysUpTime object at the time this DWS Interface enters
its current status state.
""")
_QbDwsIotIfLastRangeTime_Type = TimeStamp
_QbDwsIotIfLastRangeTime_Object = MibTableColumn
qbDwsIotIfLastRangeTime = _QbDwsIotIfLastRangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 1, 1, 11),
    _QbDwsIotIfLastRangeTime_Type()
)
qbDwsIotIfLastRangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfLastRangeTime.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfLastRangeTime.setDescription("""\
The value of MIB II's sysUpTime object at the last time when this IOT is ranged
""")
_QbDwsIotIfStatsTable_Object = MibTable
qbDwsIotIfStatsTable = _QbDwsIotIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qbDwsIotIfStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsTable.setDescription("""\
The Quantum Bridge IOT's terminal table. One entry per each RT.
""")
_QbDwsIotIfStatsEntry_Object = MibTableRow
qbDwsIotIfStatsEntry = _QbDwsIotIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1)
)
qbDwsIotIfStatsEntry.setIndexNames(
    (0, "QB-DWS-MIB", "qbDwsIotIfIndex"),
)
if mibBuilder.loadTexts:
    qbDwsIotIfStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsEntry.setDescription("""\
An entry in the Quantum DWS Interface Statistics Table.
""")


class _QbDwsIotIfStatsUtil_Type(Integer32):
    """Custom type qbDwsIotIfStatsUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QbDwsIotIfStatsUtil_Type.__name__ = "Integer32"
_QbDwsIotIfStatsUtil_Object = MibTableColumn
qbDwsIotIfStatsUtil = _QbDwsIotIfStatsUtil_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 1),
    _QbDwsIotIfStatsUtil_Type()
)
qbDwsIotIfStatsUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsUtil.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsUtil.setUnits("percent")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsUtil.setDescription("""\
The object indicates the utilization of the Network Interface transmission rate
capacity by the IOT DWS interface. This object is specified in percents.
""")
_QbDwsIotIfStatsOamRequests_Type = Counter32
_QbDwsIotIfStatsOamRequests_Object = MibTableColumn
qbDwsIotIfStatsOamRequests = _QbDwsIotIfStatsOamRequests_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 2),
    _QbDwsIotIfStatsOamRequests_Type()
)
qbDwsIotIfStatsOamRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamRequests.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamRequests.setDescription("""\
The number of received downstream OAM request messages.
""")
_QbDwsIotIfStatsOamResponses_Type = Counter32
_QbDwsIotIfStatsOamResponses_Object = MibTableColumn
qbDwsIotIfStatsOamResponses = _QbDwsIotIfStatsOamResponses_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 3),
    _QbDwsIotIfStatsOamResponses_Type()
)
qbDwsIotIfStatsOamResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamResponses.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamResponses.setDescription("""\
The number of transmitted upstream OAM response messages.
""")
_QbDwsIotIfStatsOamEvents_Type = Counter32
_QbDwsIotIfStatsOamEvents_Object = MibTableColumn
qbDwsIotIfStatsOamEvents = _QbDwsIotIfStatsOamEvents_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 4),
    _QbDwsIotIfStatsOamEvents_Type()
)
qbDwsIotIfStatsOamEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamEvents.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamEvents.setDescription("""\
The number of OAM event messages originated by the interface.
""")
_QbDwsIotIfStatsOamBadMsgs_Type = Counter32
_QbDwsIotIfStatsOamBadMsgs_Object = MibTableColumn
qbDwsIotIfStatsOamBadMsgs = _QbDwsIotIfStatsOamBadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 5),
    _QbDwsIotIfStatsOamBadMsgs_Type()
)
qbDwsIotIfStatsOamBadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamBadMsgs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsOamBadMsgs.setDescription("""\
The number of wrong OAM messages received on this interface.
""")
_QbDwsIotIfStatsCrcErrs_Type = Counter32
_QbDwsIotIfStatsCrcErrs_Object = MibTableColumn
qbDwsIotIfStatsCrcErrs = _QbDwsIotIfStatsCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 6),
    _QbDwsIotIfStatsCrcErrs_Type()
)
qbDwsIotIfStatsCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsCrcErrs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsCrcErrs.setDescription("""\
The summary number of the IOT DWS CRC subframe and time slot header CRC errors.
""")
_QbDwsIotIfStatsTsHdrParityErrs_Type = Counter32
_QbDwsIotIfStatsTsHdrParityErrs_Object = MibTableColumn
qbDwsIotIfStatsTsHdrParityErrs = _QbDwsIotIfStatsTsHdrParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 7),
    _QbDwsIotIfStatsTsHdrParityErrs_Type()
)
qbDwsIotIfStatsTsHdrParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsTsHdrParityErrs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsTsHdrParityErrs.setDescription("""\
The number of Time Slot header parity errors that have been detected on the
interface.
""")
_QbDwsIotIfStatsFrameLossErrs_Type = Counter32
_QbDwsIotIfStatsFrameLossErrs_Object = MibTableColumn
qbDwsIotIfStatsFrameLossErrs = _QbDwsIotIfStatsFrameLossErrs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 8),
    _QbDwsIotIfStatsFrameLossErrs_Type()
)
qbDwsIotIfStatsFrameLossErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsFrameLossErrs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsFrameLossErrs.setDescription("""\
The number of Loss frame errors that have been detected on the interface.
""")
_QbDwsIotIfStatsSignalLossErrs_Type = Counter32
_QbDwsIotIfStatsSignalLossErrs_Object = MibTableColumn
qbDwsIotIfStatsSignalLossErrs = _QbDwsIotIfStatsSignalLossErrs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 9),
    _QbDwsIotIfStatsSignalLossErrs_Type()
)
qbDwsIotIfStatsSignalLossErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsSignalLossErrs.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsSignalLossErrs.setDescription("""\
The number of Loss signal errors that have been detected on the interface.
""")
_QbDwsIotIfStatsRxAal1Cells_Type = Counter32
_QbDwsIotIfStatsRxAal1Cells_Object = MibTableColumn
qbDwsIotIfStatsRxAal1Cells = _QbDwsIotIfStatsRxAal1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 10),
    _QbDwsIotIfStatsRxAal1Cells_Type()
)
qbDwsIotIfStatsRxAal1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsRxAal1Cells.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsRxAal1Cells.setDescription("""\
The number of received AAL1 ATM cells.
""")
_QbDwsIotIfStatsTxAal1Cells_Type = Counter32
_QbDwsIotIfStatsTxAal1Cells_Object = MibTableColumn
qbDwsIotIfStatsTxAal1Cells = _QbDwsIotIfStatsTxAal1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 2, 2, 1, 11),
    _QbDwsIotIfStatsTxAal1Cells_Type()
)
qbDwsIotIfStatsTxAal1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsTxAal1Cells.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotIfStatsTxAal1Cells.setDescription("""\
The number of transmitted ATM cells .
""")
_QbIotPktIfGroup_ObjectIdentity = ObjectIdentity
qbIotPktIfGroup = _QbIotPktIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3)
)
_QbIotPktIfConfTable_Object = MibTable
qbIotPktIfConfTable = _QbIotPktIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qbIotPktIfConfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfTable.setDescription("""\
The Quantum Bridge PKT configuration table contains cross-connections between
Ethernet interfaces and corresponding PVC/AAL5 that are configured at a WAN
port. An entry in the table may be created, destroyed or modified. This table
lists all PVCs within the System that send/receive packet traffic to/from the
ATM cloud.
""")
_QbIotPktIfConfEntry_Object = MibTableRow
qbIotPktIfConfEntry = _QbIotPktIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1)
)
qbIotPktIfConfEntry.setIndexNames(
    (0, "QB-DWS-MIB", "qbIotPktIfConfIndex"),
)
if mibBuilder.loadTexts:
    qbIotPktIfConfEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfEntry.setDescription("""\
An entry in the Quantum Bridge IP configuration table. For every IP traffic
flow, there is a corresponding row in this table which contains a DWS interface
index, and a VPI/VCI pair of PVC configured at a SONET port for a given DWS
interface. The creation of a row in this table causes a corresponding entry in
the atmVclTable of the ATM-MIB to be automatically created if an atmVclEntry
with qbPktIotIfConfVpi and qbPktIotIfConfVci values does not exist. This
corresponding entry can be removed only if the qbPktIotIfConfEntry is removed.
The qbPktIotIfConfIndex of this table is an ifIndex of the DWS interface from
the ifTable.
""")
_QbIotPktIfConfIndex_Type = InterfaceIndex
_QbIotPktIfConfIndex_Object = MibTableColumn
qbIotPktIfConfIndex = _QbIotPktIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 1),
    _QbIotPktIfConfIndex_Type()
)
qbIotPktIfConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbIotPktIfConfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfIndex.setDescription("""\
An interface index of the Ethernet port interface.
""")
_QbAtmIfIndex_Type = InterfaceIndex
_QbAtmIfIndex_Object = MibTableColumn
qbAtmIfIndex = _QbAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 2),
    _QbAtmIfIndex_Type()
)
qbAtmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmIfIndex.setDescription("""\
An interface index of the ATM interface that is stacked on top of the WAN/SONET
interface.
""")
_QbIotPktIfConfVpi_Type = AtmVpIdentifier
_QbIotPktIfConfVpi_Object = MibTableColumn
qbIotPktIfConfVpi = _QbIotPktIfConfVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 3),
    _QbIotPktIfConfVpi_Type()
)
qbIotPktIfConfVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfVpi.setDescription("""\
A VPI of the AAL5 PVC that connects this interface to the ATM cloud. This PVC
is automatically configured at the SONET port of the WAN card (atmVclTable).
""")
_QbIotPktIfConfVci_Type = AtmVcIdentifier
_QbIotPktIfConfVci_Object = MibTableColumn
qbIotPktIfConfVci = _QbIotPktIfConfVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 4),
    _QbIotPktIfConfVci_Type()
)
qbIotPktIfConfVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfVci.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfVci.setDescription("""\
A VCI of the AAL5 bi-directional PVC that connects this interface to the ATM
cloud. This PVC is automatically configured or removed at the SONET port of the
WAN card (atmVclTable).
""")


class _QbIotPktIfConfConnName_Type(DisplayString):
    """Custom type qbIotPktIfConfConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbIotPktIfConfConnName_Type.__name__ = "DisplayString"
_QbIotPktIfConfConnName_Object = MibTableColumn
qbIotPktIfConfConnName = _QbIotPktIfConfConnName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 5),
    _QbIotPktIfConfConnName_Type()
)
qbIotPktIfConfConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfConnName.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfConnName.setDescription("""\
The textual name of the connection(PVC) as specified by a user. It provides a
non-volatile handle for this PVC. The supplied name in the
qbPktIotIfConfPvcName is associated with the same PVC for as long as that
PVC/conection remains.
""")


class _QbIotPktIfConfRxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbIotPktIfConfRxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 3


_QbIotPktIfConfRxTrafficDescrIndex_Object = MibTableColumn
qbIotPktIfConfRxTrafficDescrIndex = _QbIotPktIfConfRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 6),
    _QbIotPktIfConfRxTrafficDescrIndex_Type()
)
qbIotPktIfConfRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row of the ATM Traffic Descriptor Table
which applies to the transmit direction of this VCL.
""")


class _QbIotPktIfConfTxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbIotPktIfConfTxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 3


_QbIotPktIfConfTxTrafficDescrIndex_Object = MibTableColumn
qbIotPktIfConfTxTrafficDescrIndex = _QbIotPktIfConfTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 7),
    _QbIotPktIfConfTxTrafficDescrIndex_Type()
)
qbIotPktIfConfTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VCL.
""")
_QbIotPktIfConfAdminStatus_Type = AtmVorXAdminStatus
_QbIotPktIfConfAdminStatus_Object = MibTableColumn
qbIotPktIfConfAdminStatus = _QbIotPktIfConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 8),
    _QbIotPktIfConfAdminStatus_Type()
)
qbIotPktIfConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfAdminStatus.setDescription("""\
The desired administrative status of the packet connection The up and down
states indicate that the traffic flow is enabled or disabled respectively
across the ATM cloud.
""")
_QbIotPktIfConfOperStatus_Type = AtmVorXOperStatus
_QbIotPktIfConfOperStatus_Object = MibTableColumn
qbIotPktIfConfOperStatus = _QbIotPktIfConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 9),
    _QbIotPktIfConfOperStatus_Type()
)
qbIotPktIfConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIotPktIfConfOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfOperStatus.setDescription("""\
The current operational status of the connect.
""")
_QbIotPktIfConfRowStatus_Type = RowStatus
_QbIotPktIfConfRowStatus_Object = MibTableColumn
qbIotPktIfConfRowStatus = _QbIotPktIfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 10),
    _QbIotPktIfConfRowStatus_Type()
)
qbIotPktIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfRowStatus.setDescription("""\
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
_QbIotPktIfConfLoopback_Type = QbEnableStatus
_QbIotPktIfConfLoopback_Object = MibTableColumn
qbIotPktIfConfLoopback = _QbIotPktIfConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 11),
    _QbIotPktIfConfLoopback_Type()
)
qbIotPktIfConfLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfLoopback.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfLoopback.setDescription("""\
This object enables loopback on the IOT ENET enedpoint.
""")
_QbIotPktIfConfConnKind_Type = QbPvcConnKind
_QbIotPktIfConfConnKind_Object = MibTableColumn
qbIotPktIfConfConnKind = _QbIotPktIfConfConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 3, 1, 1, 12),
    _QbIotPktIfConfConnKind_Type()
)
qbIotPktIfConfConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPktIfConfConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPktIfConfConnKind.setDescription("""\
The PVC connection type.
""")
_QbIotAddrGroup_ObjectIdentity = ObjectIdentity
qbIotAddrGroup = _QbIotAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 4)
)
_QbIotAddrTable_Object = MibTable
qbIotAddrTable = _QbIotAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qbIotAddrTable.setStatus("current")
if mibBuilder.loadTexts:
    qbIotAddrTable.setDescription("""\
The Quantum Bridge IOT address table. This table contains information to
convert an IOT's address into an IOT's serial number. This table has two
indexes: 1. Interface index of the IOAS interface to which a terminal connects.
The interface identified by a particular value of this index is the same as the
interface identified by the same value of ifIndex. 2. IOT terminal address. A
row exists in this table for each discovered IOT terminal. Whenever an IOT is
discovered a row is added to the table
""")
_QbIotAddrEntry_Object = MibTableRow
qbIotAddrEntry = _QbIotAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 4, 1, 1)
)
qbIotAddrEntry.setIndexNames(
    (0, "QB-DWS-MIB", "qbDwsNetIfIndex"),
    (0, "QB-DWS-MIB", "qbIotAddr"),
)
if mibBuilder.loadTexts:
    qbIotAddrEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbIotAddrEntry.setDescription("""\
For every IOT terminal there is a row in this table. This contains the IOT
address and serial number.
""")
_QbIotAddr_Type = Integer32
_QbIotAddr_Object = MibTableColumn
qbIotAddr = _QbIotAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 4, 1, 1, 1),
    _QbIotAddr_Type()
)
qbIotAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbIotAddr.setStatus("current")
if mibBuilder.loadTexts:
    qbIotAddr.setDescription("""\
The IOT's address.
""")
_QbIotSerialNum_Type = QbSerialNum
_QbIotSerialNum_Object = MibTableColumn
qbIotSerialNum = _QbIotSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 4, 1, 1, 2),
    _QbIotSerialNum_Type()
)
qbIotSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIotSerialNum.setStatus("current")
if mibBuilder.loadTexts:
    qbIotSerialNum.setDescription("""\
 The IOT's serial number.
""")
_QbIotPortCrossConnGroup_ObjectIdentity = ObjectIdentity
qbIotPortCrossConnGroup = _QbIotPortCrossConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5)
)
_QbIotPortCrossConnTable_Object = MibTable
qbIotPortCrossConnTable = _QbIotPortCrossConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    qbIotPortCrossConnTable.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnTable.setDescription("""\
The Quantum Bridge IOT port cross-connection table. This table defines all IOT
port point-to-point cross-connections within a single OAS system. The
connection can be set between two Ethernet, two DS1 or two E1 ports on
different IOTs. The table has two indexes: the interface index of the first
end-point and the interface index of the second endpoint. Note: Connections
that are listed in this table are not reflected in the atmVclTable.
""")
_QbIotPortCrossConnEntry_Object = MibTableRow
qbIotPortCrossConnEntry = _QbIotPortCrossConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1)
)
qbIotPortCrossConnEntry.setIndexNames(
    (0, "QB-DWS-MIB", "qbIotPortCrossConnEndpt1IfIndex"),
    (0, "QB-DWS-MIB", "qbIotPortCrossConnEndpt2IfIndex"),
)
if mibBuilder.loadTexts:
    qbIotPortCrossConnEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnEntry.setDescription("""\
An entry in the Quantum Bridge qbIotPortConnTable two contains a connection
between the same port type of different IOTs.
""")
_QbIotPortCrossConnEndpt1IfIndex_Type = InterfaceIndex
_QbIotPortCrossConnEndpt1IfIndex_Object = MibTableColumn
qbIotPortCrossConnEndpt1IfIndex = _QbIotPortCrossConnEndpt1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 1),
    _QbIotPortCrossConnEndpt1IfIndex_Type()
)
qbIotPortCrossConnEndpt1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbIotPortCrossConnEndpt1IfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnEndpt1IfIndex.setDescription("""\
The ifIndex of the first IOT port((end-point) for the configured IOT cross-
connect.
""")
_QbIotPortCrossConnEndpt2IfIndex_Type = InterfaceIndex
_QbIotPortCrossConnEndpt2IfIndex_Object = MibTableColumn
qbIotPortCrossConnEndpt2IfIndex = _QbIotPortCrossConnEndpt2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 2),
    _QbIotPortCrossConnEndpt2IfIndex_Type()
)
qbIotPortCrossConnEndpt2IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbIotPortCrossConnEndpt2IfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnEndpt2IfIndex.setDescription("""\
The ifIndex of the second IOT port(end-point) for the configured IOT cross-
connect.
""")
_QbIotPortCrossConnAdminStatus_Type = AtmVorXAdminStatus
_QbIotPortCrossConnAdminStatus_Object = MibTableColumn
qbIotPortCrossConnAdminStatus = _QbIotPortCrossConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 3),
    _QbIotPortCrossConnAdminStatus_Type()
)
qbIotPortCrossConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnAdminStatus.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VCL.
""")
_QbIotPortCrossConnOperStatus_Type = AtmVorXOperStatus
_QbIotPortCrossConnOperStatus_Object = MibTableColumn
qbIotPortCrossConnOperStatus = _QbIotPortCrossConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 4),
    _QbIotPortCrossConnOperStatus_Type()
)
qbIotPortCrossConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIotPortCrossConnOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnOperStatus.setDescription("""\
The current operational status of the connection.
""")
_QbIotPortCrossConnLastChange_Type = AtmVorXLastChange
_QbIotPortCrossConnLastChange_Object = MibTableColumn
qbIotPortCrossConnLastChange = _QbIotPortCrossConnLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 5),
    _QbIotPortCrossConnLastChange_Type()
)
qbIotPortCrossConnLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIotPortCrossConnLastChange.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnLastChange.setDescription("""\
The value of sysUpTime at the time this connection entered its current
operational state.
""")
_QbIotPortCrossConnRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_QbIotPortCrossConnRxTrafficDescrIndex_Object = MibTableColumn
qbIotPortCrossConnRxTrafficDescrIndex = _QbIotPortCrossConnRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 6),
    _QbIotPortCrossConnRxTrafficDescrIndex_Type()
)
qbIotPortCrossConnRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row of the ATM Traffic Descriptor Table
which applies to the transmit direction of this connection.
""")


class _QbIotPortCrossConnTxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbIotPortCrossConnTxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 3


_QbIotPortCrossConnTxTrafficDescrIndex_Object = MibTableColumn
qbIotPortCrossConnTxTrafficDescrIndex = _QbIotPortCrossConnTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 7),
    _QbIotPortCrossConnTxTrafficDescrIndex_Type()
)
qbIotPortCrossConnTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this connection.
""")


class _QbIotPortCrossConnName_Type(DisplayString):
    """Custom type qbIotPortCrossConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbIotPortCrossConnName_Type.__name__ = "DisplayString"
_QbIotPortCrossConnName_Object = MibTableColumn
qbIotPortCrossConnName = _QbIotPortCrossConnName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 8),
    _QbIotPortCrossConnName_Type()
)
qbIotPortCrossConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnName.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnName.setDescription("""\
The textual name of the connection as specified by a user. It provides a non-
volatile handle for this connection. The supplied name in the qbIotPortConnName
is associated with the same connection for as long as that conection remains.
""")
_QbIotPortCrossConnRowStatus_Type = RowStatus
_QbIotPortCrossConnRowStatus_Object = MibTableColumn
qbIotPortCrossConnRowStatus = _QbIotPortCrossConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 9),
    _QbIotPortCrossConnRowStatus_Type()
)
qbIotPortCrossConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnRowStatus.setDescription("""\
The status of the port connect entry. Changing the value of this object from
'active' to 'destroy' will remove this entry from the database. It will disrupt
traffic between two IOT packet interfaces.
""")


class _QbIotPortCrossConnLoopback_Type(QbEnableStatus):
    """Custom type qbIotPortCrossConnLoopback based on QbEnableStatus"""


_QbIotPortCrossConnLoopback_Object = MibTableColumn
qbIotPortCrossConnLoopback = _QbIotPortCrossConnLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 10),
    _QbIotPortCrossConnLoopback_Type()
)
qbIotPortCrossConnLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnLoopback.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnLoopback.setDescription("""\
This object enables loopback on this IOT to IOT port enedpoint. The endpoint on
which loopback is enabled is defined by qbIotPortCrossConnLoopbackEndpt.
""")


class _QbIotPortCrossConnLoopbackEndpt_Type(Integer32):
    """Custom type qbIotPortCrossConnLoopbackEndpt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endPt1", 1),
          ("endPt2", 2))
    )


_QbIotPortCrossConnLoopbackEndpt_Type.__name__ = "Integer32"
_QbIotPortCrossConnLoopbackEndpt_Object = MibTableColumn
qbIotPortCrossConnLoopbackEndpt = _QbIotPortCrossConnLoopbackEndpt_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 11),
    _QbIotPortCrossConnLoopbackEndpt_Type()
)
qbIotPortCrossConnLoopbackEndpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnLoopbackEndpt.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnLoopbackEndpt.setDescription("""\
This object defines loopback on the selected endpoint.
""")
_QbIotPortCrossConnKind_Type = QbPvcConnKind
_QbIotPortCrossConnKind_Object = MibTableColumn
qbIotPortCrossConnKind = _QbIotPortCrossConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 5, 1, 1, 12),
    _QbIotPortCrossConnKind_Type()
)
qbIotPortCrossConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbIotPortCrossConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbIotPortCrossConnKind.setDescription("""\
The VCL connection type.
""")
_QbTContGroup_ObjectIdentity = ObjectIdentity
qbTContGroup = _QbTContGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6)
)
_QbTContNumber_Type = Integer32
_QbTContNumber_Object = MibScalar
qbTContNumber = _QbTContNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 1),
    _QbTContNumber_Type()
)
qbTContNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbTContNumber.setStatus("current")
if mibBuilder.loadTexts:
    qbTContNumber.setDescription("""\
The total number of provisioned Ethernet to ATM PVCs.
""")
_QbNextFreeTContIndex_Type = Integer32
_QbNextFreeTContIndex_Object = MibScalar
qbNextFreeTContIndex = _QbNextFreeTContIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 2),
    _QbNextFreeTContIndex_Type()
)
qbNextFreeTContIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbNextFreeTContIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbNextFreeTContIndex.setDescription("""\
The next available Container index.
""")
_QbTContTable_Object = MibTable
qbTContTable = _QbTContTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    qbTContTable.setStatus("current")
if mibBuilder.loadTexts:
    qbTContTable.setDescription("""\
The Quantum Bridge Traffic Container table(TCons) contains traffic containers
of IOTs.
""")
_QbTContEntry_Object = MibTableRow
qbTContEntry = _QbTContEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1)
)
qbTContEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysIotSerialNumber"),
    (0, "QB-DWS-MIB", "qbTContIndex"),
)
if mibBuilder.loadTexts:
    qbTContEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbTContEntry.setDescription("""\
An entry in the qbTContTable. There is one entry in the table per IOT on the
PON for Release 3.0. The creation of a row in the qbSysIotTable causes a
corresponding entry in this table to be automatically created. The deletion of
a row in the qbSysIotTable causes a corresponding entry in this table to be
automatically removed.
""")
_QbTContIndex_Type = Integer32
_QbTContIndex_Object = MibTableColumn
qbTContIndex = _QbTContIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1, 1),
    _QbTContIndex_Type()
)
qbTContIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbTContIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbTContIndex.setDescription("""\
The value of this object identifies the row of the Traffic Container Table.
Note tht this value can be set to 1 only for Release 3.0.
""")


class _QbTContType_Type(Integer32):
    """Custom type qbTContType based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type4", 4),
          ("type5", 5))
    )


_QbTContType_Type.__name__ = "Integer32"
_QbTContType_Object = MibTableColumn
qbTContType = _QbTContType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1, 2),
    _QbTContType_Type()
)
qbTContType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTContType.setStatus("current")
if mibBuilder.loadTexts:
    qbTContType.setDescription("""\
The Traffic container type. Note that this object can be set to type1 for
Release 3.0
""")
_QbTContMaxBw_Type = Integer32
_QbTContMaxBw_Object = MibTableColumn
qbTContMaxBw = _QbTContMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1, 3),
    _QbTContMaxBw_Type()
)
qbTContMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTContMaxBw.setStatus("current")
if mibBuilder.loadTexts:
    qbTContMaxBw.setDescription("""\
The maximum bandwidth to be assigned to this TCONT. Note that the read-only
access is supported for Release 3.0
""")
_QbTContFixedBw_Type = Integer32
_QbTContFixedBw_Object = MibTableColumn
qbTContFixedBw = _QbTContFixedBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1, 4),
    _QbTContFixedBw_Type()
)
qbTContFixedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTContFixedBw.setStatus("current")
if mibBuilder.loadTexts:
    qbTContFixedBw.setDescription("""\
The lower limit of bandwidth for this TCONT.
""")
_QbTContAssuredBw_Type = Integer32
_QbTContAssuredBw_Object = MibTableColumn
qbTContAssuredBw = _QbTContAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1, 5),
    _QbTContAssuredBw_Type()
)
qbTContAssuredBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTContAssuredBw.setStatus("current")
if mibBuilder.loadTexts:
    qbTContAssuredBw.setDescription("""\
The guaranteed minimum bandwidth for this TCONT. TCONT. Note that the read-only
access is supported for Release 3.0
""")
_QbTContGrantNum_Type = Integer32
_QbTContGrantNum_Object = MibTableColumn
qbTContGrantNum = _QbTContGrantNum_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 1, 6, 3, 1, 6),
    _QbTContGrantNum_Type()
)
qbTContGrantNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTContGrantNum.setStatus("current")
if mibBuilder.loadTexts:
    qbTContGrantNum.setDescription("""\
FSAN grant number that is assigned to this TCONT. Note that the read-only
access is supported for Release 3.0
""")
_QbDwsNotifications_ObjectIdentity = ObjectIdentity
qbDwsNotifications = _QbDwsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 2)
)
_QbDwsNotificationPrefix_ObjectIdentity = ObjectIdentity
qbDwsNotificationPrefix = _QbDwsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 2, 0)
)
_QbDwsConformance_ObjectIdentity = ObjectIdentity
qbDwsConformance = _QbDwsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3)
)
_QbDwsCompliances_ObjectIdentity = ObjectIdentity
qbDwsCompliances = _QbDwsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 1)
)
_QbDwsGroups_ObjectIdentity = ObjectIdentity
qbDwsGroups = _QbDwsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 2)
)

# Managed Objects groups

qbDwsNetGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 2, 1)
)
qbDwsNetGroupInfo.setObjects(
      *(("QB-DWS-MIB", "qbSysIotRecoverMode"),
        ("QB-DWS-MIB", "qbDwsNetBw"),
        ("QB-DWS-MIB", "qbDwsNetAllocatedBw"),
        ("QB-DWS-MIB", "qbDwsNetAvailableBw"),
        ("QB-DWS-MIB", "qbDwsNetAllocatedUbrBw"),
        ("QB-DWS-MIB", "qbDwsNetAllocatedCbrBw"),
        ("QB-DWS-MIB", "qbDwsNetNumCbrConn"),
        ("QB-DWS-MIB", "qbDwsNetNumUbrConn"),
        ("QB-DWS-MIB", "qbDwsNetNumIot"),
        ("QB-DWS-MIB", "qbDwsNetTxStatus"),
        ("QB-DWS-MIB", "qbDwsNetTxStatusLastChange"),
        ("QB-DWS-MIB", "qbDwsNetLosIotAddr"),
        ("QB-DWS-MIB", "qbDwsNetLosIotTime"),
        ("QB-DWS-MIB", "qbDwsNetEncryptStatus"),
        ("QB-DWS-MIB", "qbDwsNetRangeMode"),
        ("QB-DWS-MIB", "qbDwsNetRxTsCount"),
        ("QB-DWS-MIB", "qbDwsNetTxTsCount"),
        ("QB-DWS-MIB", "qbDwsNetRxMissingTs"),
        ("QB-DWS-MIB", "qbDwsNetRxIllegalTs"),
        ("QB-DWS-MIB", "qbDwsNetTxJabberTs"),
        ("QB-DWS-MIB", "qbDwsNetTxOutOfFrameTs"),
        ("QB-DWS-MIB", "qbDwsNetTxHdrCrcTsErrs"),
        ("QB-DWS-MIB", "qbDwsNetOamRequests"),
        ("QB-DWS-MIB", "qbDwsNetOamResponses"),
        ("QB-DWS-MIB", "qbDwsNetOamEvents"),
        ("QB-DWS-MIB", "qbDwsNetOamBadMsgs"))
)
if mibBuilder.loadTexts:
    qbDwsNetGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsNetGroupInfo.setDescription("""\
The set of all accessible objects in the DWS Network Group of this MIB.
""")

qbDwsIotGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 2, 2)
)
qbDwsIotGroupInfo.setObjects(
      *(("QB-DWS-MIB", "qbDwsIotIfAddr"),
        ("QB-DWS-MIB", "qbDwsIotIfConfPowerLevel"),
        ("QB-DWS-MIB", "qbDwsIotIfConfEqDelay"),
        ("QB-DWS-MIB", "qbDwsIotIfConfWaveLength"),
        ("QB-DWS-MIB", "qbDwsIotIfUbrBw"),
        ("QB-DWS-MIB", "qbDwsIotIfCbrBw"),
        ("QB-DWS-MIB", "qbDwsIotIfTxStatus"),
        ("QB-DWS-MIB", "qbDwsIotIfTxStatusLastChange"),
        ("QB-DWS-MIB", "qbDwsIotIfLastRangeTime"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsUtil"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsOamRequests"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsOamResponses"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsOamEvents"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsOamBadMsgs"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsCrcErrs"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsTsHdrParityErrs"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsFrameLossErrs"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsSignalLossErrs"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsRxAal1Cells"),
        ("QB-DWS-MIB", "qbDwsIotIfStatsTxAal1Cells"))
)
if mibBuilder.loadTexts:
    qbDwsIotGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotGroupInfo.setDescription("""\
The set of all accessible objects in the IOT Group of this MIB.
""")

qbDwsPktGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 2, 3)
)
qbDwsPktGroupInfo.setObjects(
      *(("QB-DWS-MIB", "qbAtmIfIndex"),
        ("QB-DWS-MIB", "qbIotPktIfConfVpi"),
        ("QB-DWS-MIB", "qbIotPktIfConfVci"),
        ("QB-DWS-MIB", "qbIotPktIfConfConnName"),
        ("QB-DWS-MIB", "qbIotPktIfConfRowStatus"))
)
if mibBuilder.loadTexts:
    qbDwsPktGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsPktGroupInfo.setDescription("""\
The set of all accessible objects in the Packet Group ofthis MIB.
""")

qbDwsIotAddrGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 2, 4)
)
qbDwsIotAddrGroupInfo.setObjects(
    ("QB-DWS-MIB", "qbIotSerialNum")
)
if mibBuilder.loadTexts:
    qbDwsIotAddrGroupInfo.setStatus("current")
if mibBuilder.loadTexts:
    qbDwsIotAddrGroupInfo.setDescription("""\
The set of all accessible objects in the IOT address group of this MIB.
""")


# Notification objects

qbDwsIotRxLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 2, 0, 1)
)
qbDwsIotRxLos.setObjects(
      *(("QB-DWS-MIB", "qbDwsNetIfIndex"),
        ("QB-DWS-MIB", "qbDwsIotIfAddr"))
)
if mibBuilder.loadTexts:
    qbDwsIotRxLos.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbDwsIotRxLos.setDescription("""\
A qbDwsIotRxLos trap indicates Loss of Signal by the IOT's. This trap is
generated by an IOT when Analog DS1/E1 Analog or Digital Los occur.
""")

qbDwsRxIoasLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 2, 0, 2)
)
qbDwsRxIoasLos.setObjects(
      *(("QB-DWS-MIB", "qbDwsNetIfIndex"),
        ("QB-DWS-MIB", "qbDwsIotIfAddr"))
)
if mibBuilder.loadTexts:
    qbDwsRxIoasLos.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbDwsRxIoasLos.setDescription("""\
A qbDwsRxIoasLos trap indicates Loss of Signal by the IOAS's DWS receiver. This
trap is generated by an IOAS DWS card when no signal from an IOT is detected
within the timeslot window.
""")

qbDwsIoasTxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 2, 0, 3)
)
qbDwsIoasTxFailure.setObjects(
    ("QB-DWS-MIB", "qbDwsNetIfIndex")
)
if mibBuilder.loadTexts:
    qbDwsIoasTxFailure.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbDwsIoasTxFailure.setDescription("""\
A qbDwsTxFailure trap indicates that the IOAS card transmitter does not work.
The trap is generated by an IOAS card when the IOAS DWS card transmitter
problem is detected. The trap contains the DWS card interface index.
""")

qbDwsIotRangeTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 2, 0, 4)
)
qbDwsIotRangeTimeout.setObjects(
      *(("QB-DWS-MIB", "qbDwsNetIfIndex"),
        ("QB-DWS-MIB", "qbDwsIotIfAddr"))
)
if mibBuilder.loadTexts:
    qbDwsIotRangeTimeout.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbDwsIotRangeTimeout.setDescription("""\
A qbDwsTxFailure trap indicates that IOT not responding during the ranging
process.
""")


# Notifications groups


# Agent capabilities


# Module compliance

qbDwsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbDwsCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbDwsCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-DWS-MIB",
    **{"QbPvcConnKind": QbPvcConnKind,
       "QbBitRate": QbBitRate,
       "QbSerialNum": QbSerialNum,
       "QbDwsIfStatus": QbDwsIfStatus,
       "QbDwsSrvStatus": QbDwsSrvStatus,
       "QbAtmAal5EncapsType": QbAtmAal5EncapsType,
       "QbEnableStatus": QbEnableStatus,
       "qbDwsMIB": qbDwsMIB,
       "qbDwsObjects": qbDwsObjects,
       "qbDwsNetGroup": qbDwsNetGroup,
       "qbDwsSysRangeMode": qbDwsSysRangeMode,
       "qbSysIotRecoverMode": qbSysIotRecoverMode,
       "qbDwsNetTable": qbDwsNetTable,
       "qbDwsNetEntry": qbDwsNetEntry,
       "qbDwsNetIfIndex": qbDwsNetIfIndex,
       "qbDwsNetBw": qbDwsNetBw,
       "qbDwsNetAllocatedBw": qbDwsNetAllocatedBw,
       "qbDwsNetAvailableBw": qbDwsNetAvailableBw,
       "qbDwsNetAllocatedUbrBw": qbDwsNetAllocatedUbrBw,
       "qbDwsNetAllocatedCbrBw": qbDwsNetAllocatedCbrBw,
       "qbDwsNetNumCbrConn": qbDwsNetNumCbrConn,
       "qbDwsNetNumUbrConn": qbDwsNetNumUbrConn,
       "qbDwsNetNumIot": qbDwsNetNumIot,
       "qbDwsNetTxStatus": qbDwsNetTxStatus,
       "qbDwsNetTxStatusLastChange": qbDwsNetTxStatusLastChange,
       "qbDwsNetLosIotAddr": qbDwsNetLosIotAddr,
       "qbDwsNetLosIotTime": qbDwsNetLosIotTime,
       "qbDwsNetEncryptStatus": qbDwsNetEncryptStatus,
       "qbDwsNetRangeMode": qbDwsNetRangeMode,
       "qbDwsNetRxTsCount": qbDwsNetRxTsCount,
       "qbDwsNetTxTsCount": qbDwsNetTxTsCount,
       "qbDwsNetRxMissingTs": qbDwsNetRxMissingTs,
       "qbDwsNetRxIllegalTs": qbDwsNetRxIllegalTs,
       "qbDwsNetTxJabberTs": qbDwsNetTxJabberTs,
       "qbDwsNetTxOutOfFrameTs": qbDwsNetTxOutOfFrameTs,
       "qbDwsNetTxHdrCrcTsErrs": qbDwsNetTxHdrCrcTsErrs,
       "qbDwsNetOamRequests": qbDwsNetOamRequests,
       "qbDwsNetOamResponses": qbDwsNetOamResponses,
       "qbDwsNetOamEvents": qbDwsNetOamEvents,
       "qbDwsNetOamBadMsgs": qbDwsNetOamBadMsgs,
       "qbDwsNetLoopBack": qbDwsNetLoopBack,
       "qbDwsIotIfGroup": qbDwsIotIfGroup,
       "qbDwsIotIfConfTable": qbDwsIotIfConfTable,
       "qbDwsIotIfConfEntry": qbDwsIotIfConfEntry,
       "qbDwsIotIfIndex": qbDwsIotIfIndex,
       "qbDwsIotNetIfIndex": qbDwsIotNetIfIndex,
       "qbDwsIotIfAddr": qbDwsIotIfAddr,
       "qbDwsIotIfConfPowerLevel": qbDwsIotIfConfPowerLevel,
       "qbDwsIotIfConfEqDelay": qbDwsIotIfConfEqDelay,
       "qbDwsIotIfConfWaveLength": qbDwsIotIfConfWaveLength,
       "qbDwsIotIfUbrBw": qbDwsIotIfUbrBw,
       "qbDwsIotIfCbrBw": qbDwsIotIfCbrBw,
       "qbDwsIotIfTxStatus": qbDwsIotIfTxStatus,
       "qbDwsIotIfTxStatusLastChange": qbDwsIotIfTxStatusLastChange,
       "qbDwsIotIfLastRangeTime": qbDwsIotIfLastRangeTime,
       "qbDwsIotIfStatsTable": qbDwsIotIfStatsTable,
       "qbDwsIotIfStatsEntry": qbDwsIotIfStatsEntry,
       "qbDwsIotIfStatsUtil": qbDwsIotIfStatsUtil,
       "qbDwsIotIfStatsOamRequests": qbDwsIotIfStatsOamRequests,
       "qbDwsIotIfStatsOamResponses": qbDwsIotIfStatsOamResponses,
       "qbDwsIotIfStatsOamEvents": qbDwsIotIfStatsOamEvents,
       "qbDwsIotIfStatsOamBadMsgs": qbDwsIotIfStatsOamBadMsgs,
       "qbDwsIotIfStatsCrcErrs": qbDwsIotIfStatsCrcErrs,
       "qbDwsIotIfStatsTsHdrParityErrs": qbDwsIotIfStatsTsHdrParityErrs,
       "qbDwsIotIfStatsFrameLossErrs": qbDwsIotIfStatsFrameLossErrs,
       "qbDwsIotIfStatsSignalLossErrs": qbDwsIotIfStatsSignalLossErrs,
       "qbDwsIotIfStatsRxAal1Cells": qbDwsIotIfStatsRxAal1Cells,
       "qbDwsIotIfStatsTxAal1Cells": qbDwsIotIfStatsTxAal1Cells,
       "qbIotPktIfGroup": qbIotPktIfGroup,
       "qbIotPktIfConfTable": qbIotPktIfConfTable,
       "qbIotPktIfConfEntry": qbIotPktIfConfEntry,
       "qbIotPktIfConfIndex": qbIotPktIfConfIndex,
       "qbAtmIfIndex": qbAtmIfIndex,
       "qbIotPktIfConfVpi": qbIotPktIfConfVpi,
       "qbIotPktIfConfVci": qbIotPktIfConfVci,
       "qbIotPktIfConfConnName": qbIotPktIfConfConnName,
       "qbIotPktIfConfRxTrafficDescrIndex": qbIotPktIfConfRxTrafficDescrIndex,
       "qbIotPktIfConfTxTrafficDescrIndex": qbIotPktIfConfTxTrafficDescrIndex,
       "qbIotPktIfConfAdminStatus": qbIotPktIfConfAdminStatus,
       "qbIotPktIfConfOperStatus": qbIotPktIfConfOperStatus,
       "qbIotPktIfConfRowStatus": qbIotPktIfConfRowStatus,
       "qbIotPktIfConfLoopback": qbIotPktIfConfLoopback,
       "qbIotPktIfConfConnKind": qbIotPktIfConfConnKind,
       "qbIotAddrGroup": qbIotAddrGroup,
       "qbIotAddrTable": qbIotAddrTable,
       "qbIotAddrEntry": qbIotAddrEntry,
       "qbIotAddr": qbIotAddr,
       "qbIotSerialNum": qbIotSerialNum,
       "qbIotPortCrossConnGroup": qbIotPortCrossConnGroup,
       "qbIotPortCrossConnTable": qbIotPortCrossConnTable,
       "qbIotPortCrossConnEntry": qbIotPortCrossConnEntry,
       "qbIotPortCrossConnEndpt1IfIndex": qbIotPortCrossConnEndpt1IfIndex,
       "qbIotPortCrossConnEndpt2IfIndex": qbIotPortCrossConnEndpt2IfIndex,
       "qbIotPortCrossConnAdminStatus": qbIotPortCrossConnAdminStatus,
       "qbIotPortCrossConnOperStatus": qbIotPortCrossConnOperStatus,
       "qbIotPortCrossConnLastChange": qbIotPortCrossConnLastChange,
       "qbIotPortCrossConnRxTrafficDescrIndex": qbIotPortCrossConnRxTrafficDescrIndex,
       "qbIotPortCrossConnTxTrafficDescrIndex": qbIotPortCrossConnTxTrafficDescrIndex,
       "qbIotPortCrossConnName": qbIotPortCrossConnName,
       "qbIotPortCrossConnRowStatus": qbIotPortCrossConnRowStatus,
       "qbIotPortCrossConnLoopback": qbIotPortCrossConnLoopback,
       "qbIotPortCrossConnLoopbackEndpt": qbIotPortCrossConnLoopbackEndpt,
       "qbIotPortCrossConnKind": qbIotPortCrossConnKind,
       "qbTContGroup": qbTContGroup,
       "qbTContNumber": qbTContNumber,
       "qbNextFreeTContIndex": qbNextFreeTContIndex,
       "qbTContTable": qbTContTable,
       "qbTContEntry": qbTContEntry,
       "qbTContIndex": qbTContIndex,
       "qbTContType": qbTContType,
       "qbTContMaxBw": qbTContMaxBw,
       "qbTContFixedBw": qbTContFixedBw,
       "qbTContAssuredBw": qbTContAssuredBw,
       "qbTContGrantNum": qbTContGrantNum,
       "qbDwsNotifications": qbDwsNotifications,
       "qbDwsNotificationPrefix": qbDwsNotificationPrefix,
       "qbDwsIotRxLos": qbDwsIotRxLos,
       "qbDwsRxIoasLos": qbDwsRxIoasLos,
       "qbDwsIoasTxFailure": qbDwsIoasTxFailure,
       "qbDwsIotRangeTimeout": qbDwsIotRangeTimeout,
       "qbDwsConformance": qbDwsConformance,
       "qbDwsCompliances": qbDwsCompliances,
       "qbDwsCompliance": qbDwsCompliance,
       "qbDwsGroups": qbDwsGroups,
       "qbDwsNetGroupInfo": qbDwsNetGroupInfo,
       "qbDwsIotGroupInfo": qbDwsIotGroupInfo,
       "qbDwsPktGroupInfo": qbDwsPktGroupInfo,
       "qbDwsIotAddrGroupInfo": qbDwsIotAddrGroupInfo}
)
