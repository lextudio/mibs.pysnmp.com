# SNMP MIB module (HUAWEI-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:22 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwNATCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SessionType(Integer32, TextualConvention):
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("dnsSession", 1),
          ("finrstSession", 2),
          ("fragSession", 3),
          ("ftpDataSession", 5),
          ("ftpSession", 4),
          ("greSesion", 34),
          ("h225Session", 6),
          ("h245Session", 7),
          ("h323rtcpSession", 8),
          ("h323rtpSession", 9),
          ("h323t120Session", 10),
          ("httpSession", 11),
          ("hwccSession", 12),
          ("icmpSession", 13),
          ("ilsSession", 14),
          ("msnSession", 29),
          ("netbiosSession", 17),
          ("netbiosdataSession", 15),
          ("netbiosnameSession", 16),
          ("pptpSession", 26),
          ("qqSession", 28),
          ("rasSession", 18),
          ("rtcpSession", 19),
          ("rtpSession", 20),
          ("rtspSession", 21),
          ("sipSession", 31),
          ("siprtpSession", 32),
          ("siptrcpSession", 33),
          ("smtpSession", 22),
          ("synSession", 23),
          ("tcpSession", 24),
          ("telnetSession", 25),
          ("udpSession", 27),
          ("userdefineSession", 30))
    )



class AlgType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dnsAlg", 2),
          ("ftpAlg", 5),
          ("h323Alg", 1),
          ("hwccAlg", 8),
          ("icmpAlg", 6),
          ("ilsAlg", 4),
          ("msnAlg", 10),
          ("netbiosAlg", 3),
          ("pptpAlg", 7),
          ("qqAlg", 9),
          ("userdefineAlg", 11))
    )



class NatType(Integer32, TextualConvention):
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
        *(("easyIP", 3),
          ("nat", 1),
          ("pat", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwNAT_ObjectIdentity = ObjectIdentity
hwNAT = _HwNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7)
)
_HwNatMibObjects_ObjectIdentity = ObjectIdentity
hwNatMibObjects = _HwNatMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1)
)
_HwNatAddressGroupInfoTable_Object = MibTable
hwNatAddressGroupInfoTable = _HwNatAddressGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwNatAddressGroupInfoTable.setStatus("current")
_HwNatAddressGroupInfoEntry_Object = MibTableRow
hwNatAddressGroupInfoEntry = _HwNatAddressGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1)
)
hwNatAddressGroupInfoEntry.setIndexNames(
    (0, "HUAWEI-NAT-MIB", "hwNatAddrGrpIndex"),
)
if mibBuilder.loadTexts:
    hwNatAddressGroupInfoEntry.setStatus("current")


class _HwNatAddrGrpIndex_Type(Integer32):
    """Custom type hwNatAddrGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwNatAddrGrpIndex_Type.__name__ = "Integer32"
_HwNatAddrGrpIndex_Object = MibTableColumn
hwNatAddrGrpIndex = _HwNatAddrGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 1),
    _HwNatAddrGrpIndex_Type()
)
hwNatAddrGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrGrpIndex.setStatus("current")
_HwNatAddrGrpBeginningIpAddr_Type = IpAddress
_HwNatAddrGrpBeginningIpAddr_Object = MibTableColumn
hwNatAddrGrpBeginningIpAddr = _HwNatAddrGrpBeginningIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 2),
    _HwNatAddrGrpBeginningIpAddr_Type()
)
hwNatAddrGrpBeginningIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpBeginningIpAddr.setStatus("current")
_HwNatAddrGrpEndingIpAddr_Type = IpAddress
_HwNatAddrGrpEndingIpAddr_Object = MibTableColumn
hwNatAddrGrpEndingIpAddr = _HwNatAddrGrpEndingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 3),
    _HwNatAddrGrpEndingIpAddr_Type()
)
hwNatAddrGrpEndingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpEndingIpAddr.setStatus("current")
_HwNatAddrGrpRefCount_Type = Integer32
_HwNatAddrGrpRefCount_Object = MibTableColumn
hwNatAddrGrpRefCount = _HwNatAddrGrpRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 4),
    _HwNatAddrGrpRefCount_Type()
)
hwNatAddrGrpRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrGrpRefCount.setStatus("current")
_HwNatAddrGrpRowstatus_Type = RowStatus
_HwNatAddrGrpRowstatus_Object = MibTableColumn
hwNatAddrGrpRowstatus = _HwNatAddrGrpRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 5),
    _HwNatAddrGrpRowstatus_Type()
)
hwNatAddrGrpRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpRowstatus.setStatus("current")


class _HwNatAddrGrpVrrpID_Type(Integer32):
    """Custom type hwNatAddrGrpVrrpID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwNatAddrGrpVrrpID_Type.__name__ = "Integer32"
_HwNatAddrGrpVrrpID_Object = MibTableColumn
hwNatAddrGrpVrrpID = _HwNatAddrGrpVrrpID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 6),
    _HwNatAddrGrpVrrpID_Type()
)
hwNatAddrGrpVrrpID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpVrrpID.setStatus("current")


class _HwNatAddrGrpVrfName_Type(OctetString):
    """Custom type hwNatAddrGrpVrfName based on OctetString"""
    defaultValue = OctetString("--")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwNatAddrGrpVrfName_Type.__name__ = "OctetString"
_HwNatAddrGrpVrfName_Object = MibTableColumn
hwNatAddrGrpVrfName = _HwNatAddrGrpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 1, 1, 7),
    _HwNatAddrGrpVrfName_Type()
)
hwNatAddrGrpVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpVrfName.setStatus("current")
_HwNatInternalServerTable_Object = MibTable
hwNatInternalServerTable = _HwNatInternalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwNatInternalServerTable.setStatus("current")
_HwNatInternalServerEntry_Object = MibTableRow
hwNatInternalServerEntry = _HwNatInternalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1)
)
hwNatInternalServerEntry.setIndexNames(
    (0, "HUAWEI-NAT-MIB", "hwNatServerIndex"),
)
if mibBuilder.loadTexts:
    hwNatInternalServerEntry.setStatus("current")


class _HwNatServerIndex_Type(Integer32):
    """Custom type hwNatServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwNatServerIndex_Type.__name__ = "Integer32"
_HwNatServerIndex_Object = MibTableColumn
hwNatServerIndex = _HwNatServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 1),
    _HwNatServerIndex_Type()
)
hwNatServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatServerIndex.setStatus("current")


class _HwNatServerProtocol_Type(Integer32):
    """Custom type hwNatServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwNatServerProtocol_Type.__name__ = "Integer32"
_HwNatServerProtocol_Object = MibTableColumn
hwNatServerProtocol = _HwNatServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 2),
    _HwNatServerProtocol_Type()
)
hwNatServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerProtocol.setStatus("current")
_HwNatServerInsideBeginIpAddr_Type = IpAddress
_HwNatServerInsideBeginIpAddr_Object = MibTableColumn
hwNatServerInsideBeginIpAddr = _HwNatServerInsideBeginIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 3),
    _HwNatServerInsideBeginIpAddr_Type()
)
hwNatServerInsideBeginIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerInsideBeginIpAddr.setStatus("current")
_HwNatServerInsideEndIpAddr_Type = IpAddress
_HwNatServerInsideEndIpAddr_Object = MibTableColumn
hwNatServerInsideEndIpAddr = _HwNatServerInsideEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 4),
    _HwNatServerInsideEndIpAddr_Type()
)
hwNatServerInsideEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerInsideEndIpAddr.setStatus("current")


class _HwNatServerInsidePort_Type(Integer32):
    """Custom type hwNatServerInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNatServerInsidePort_Type.__name__ = "Integer32"
_HwNatServerInsidePort_Object = MibTableColumn
hwNatServerInsidePort = _HwNatServerInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 5),
    _HwNatServerInsidePort_Type()
)
hwNatServerInsidePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerInsidePort.setStatus("current")
_HwNatServerOutsideIpAddr_Type = IpAddress
_HwNatServerOutsideIpAddr_Object = MibTableColumn
hwNatServerOutsideIpAddr = _HwNatServerOutsideIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 6),
    _HwNatServerOutsideIpAddr_Type()
)
hwNatServerOutsideIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerOutsideIpAddr.setStatus("current")


class _HwNatServerOutsideBeginPort_Type(Integer32):
    """Custom type hwNatServerOutsideBeginPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNatServerOutsideBeginPort_Type.__name__ = "Integer32"
_HwNatServerOutsideBeginPort_Object = MibTableColumn
hwNatServerOutsideBeginPort = _HwNatServerOutsideBeginPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 7),
    _HwNatServerOutsideBeginPort_Type()
)
hwNatServerOutsideBeginPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerOutsideBeginPort.setStatus("current")


class _HwNatServerOutsideEndPort_Type(Integer32):
    """Custom type hwNatServerOutsideEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNatServerOutsideEndPort_Type.__name__ = "Integer32"
_HwNatServerOutsideEndPort_Object = MibTableColumn
hwNatServerOutsideEndPort = _HwNatServerOutsideEndPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 8),
    _HwNatServerOutsideEndPort_Type()
)
hwNatServerOutsideEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerOutsideEndPort.setStatus("current")
_HwNatServerRowStatus_Type = RowStatus
_HwNatServerRowStatus_Object = MibTableColumn
hwNatServerRowStatus = _HwNatServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 9),
    _HwNatServerRowStatus_Type()
)
hwNatServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerRowStatus.setStatus("current")


class _HwNatServerVrrpID_Type(Integer32):
    """Custom type hwNatServerVrrpID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwNatServerVrrpID_Type.__name__ = "Integer32"
_HwNatServerVrrpID_Object = MibTableColumn
hwNatServerVrrpID = _HwNatServerVrrpID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 10),
    _HwNatServerVrrpID_Type()
)
hwNatServerVrrpID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerVrrpID.setStatus("current")


class _HwNatServerVrfName_Type(OctetString):
    """Custom type hwNatServerVrfName based on OctetString"""
    defaultValue = OctetString("--")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNatServerVrfName_Type.__name__ = "OctetString"
_HwNatServerVrfName_Object = MibTableColumn
hwNatServerVrfName = _HwNatServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 2, 1, 11),
    _HwNatServerVrfName_Type()
)
hwNatServerVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatServerVrfName.setStatus("current")
_HwNatTimeoutTable_Object = MibTable
hwNatTimeoutTable = _HwNatTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwNatTimeoutTable.setStatus("current")
_HwNatTimeoutEntry_Object = MibTableRow
hwNatTimeoutEntry = _HwNatTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 3, 1)
)
hwNatTimeoutEntry.setIndexNames(
    (0, "HUAWEI-NAT-MIB", "hwNatTimeoutSessionType"),
)
if mibBuilder.loadTexts:
    hwNatTimeoutEntry.setStatus("current")
_HwNatTimeoutSessionType_Type = SessionType
_HwNatTimeoutSessionType_Object = MibTableColumn
hwNatTimeoutSessionType = _HwNatTimeoutSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 3, 1, 1),
    _HwNatTimeoutSessionType_Type()
)
hwNatTimeoutSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatTimeoutSessionType.setStatus("current")


class _HwNatTimeoutValue_Type(Integer32):
    """Custom type hwNatTimeoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwNatTimeoutValue_Type.__name__ = "Integer32"
_HwNatTimeoutValue_Object = MibTableColumn
hwNatTimeoutValue = _HwNatTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 3, 1, 2),
    _HwNatTimeoutValue_Type()
)
hwNatTimeoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNatTimeoutValue.setStatus("current")
_HwNatAlgEnableTable_Object = MibTable
hwNatAlgEnableTable = _HwNatAlgEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwNatAlgEnableTable.setStatus("current")
_HwNatAlgEnableEntry_Object = MibTableRow
hwNatAlgEnableEntry = _HwNatAlgEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 4, 1)
)
hwNatAlgEnableEntry.setIndexNames(
    (0, "HUAWEI-NAT-MIB", "hwNatAlgEnableProtocol"),
)
if mibBuilder.loadTexts:
    hwNatAlgEnableEntry.setStatus("current")
_HwNatAlgEnableProtocol_Type = AlgType
_HwNatAlgEnableProtocol_Object = MibTableColumn
hwNatAlgEnableProtocol = _HwNatAlgEnableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 4, 1, 1),
    _HwNatAlgEnableProtocol_Type()
)
hwNatAlgEnableProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAlgEnableProtocol.setStatus("current")
_HwNatAlgEnableFlag_Type = TruthValue
_HwNatAlgEnableFlag_Object = MibTableColumn
hwNatAlgEnableFlag = _HwNatAlgEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 1, 4, 1, 2),
    _HwNatAlgEnableFlag_Type()
)
hwNatAlgEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNatAlgEnableFlag.setStatus("current")
_HwNatMonitorObjects_ObjectIdentity = ObjectIdentity
hwNatMonitorObjects = _HwNatMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2)
)
_HwNatMonitorGlobalHash_ObjectIdentity = ObjectIdentity
hwNatMonitorGlobalHash = _HwNatMonitorGlobalHash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 1)
)
_HwNatHashStatPatCount_Type = Counter32
_HwNatHashStatPatCount_Object = MibScalar
hwNatHashStatPatCount = _HwNatHashStatPatCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 1, 1),
    _HwNatHashStatPatCount_Type()
)
hwNatHashStatPatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatHashStatPatCount.setStatus("current")
_HwNatHashStatNoPatCount_Type = Counter32
_HwNatHashStatNoPatCount_Object = MibScalar
hwNatHashStatNoPatCount = _HwNatHashStatNoPatCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 1, 2),
    _HwNatHashStatNoPatCount_Type()
)
hwNatHashStatNoPatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatHashStatNoPatCount.setStatus("current")
_HwNatHashStatServerHashCount_Type = Counter32
_HwNatHashStatServerHashCount_Object = MibScalar
hwNatHashStatServerHashCount = _HwNatHashStatServerHashCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 1, 3),
    _HwNatHashStatServerHashCount_Type()
)
hwNatHashStatServerHashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatHashStatServerHashCount.setStatus("current")
_HwNatHashStatFragHashCount_Type = Counter32
_HwNatHashStatFragHashCount_Object = MibScalar
hwNatHashStatFragHashCount = _HwNatHashStatFragHashCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 1, 4),
    _HwNatHashStatFragHashCount_Type()
)
hwNatHashStatFragHashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatHashStatFragHashCount.setStatus("current")
_HwNatMonitorGlobalPkts_ObjectIdentity = ObjectIdentity
hwNatMonitorGlobalPkts = _HwNatMonitorGlobalPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 2)
)
_HwNatStatPktsCount_Type = Counter64
_HwNatStatPktsCount_Object = MibScalar
hwNatStatPktsCount = _HwNatStatPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 2, 1),
    _HwNatStatPktsCount_Type()
)
hwNatStatPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStatPktsCount.setStatus("current")
_HwNatStatFailedPktsCount_Type = Counter64
_HwNatStatFailedPktsCount_Object = MibScalar
hwNatStatFailedPktsCount = _HwNatStatFailedPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 2, 2),
    _HwNatStatFailedPktsCount_Type()
)
hwNatStatFailedPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStatFailedPktsCount.setStatus("current")
_HwNatStatTCPPktsCount_Type = Counter64
_HwNatStatTCPPktsCount_Object = MibScalar
hwNatStatTCPPktsCount = _HwNatStatTCPPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 2, 3),
    _HwNatStatTCPPktsCount_Type()
)
hwNatStatTCPPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStatTCPPktsCount.setStatus("current")
_HwNatStatUDPPktsCount_Type = Counter64
_HwNatStatUDPPktsCount_Object = MibScalar
hwNatStatUDPPktsCount = _HwNatStatUDPPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 2, 4),
    _HwNatStatUDPPktsCount_Type()
)
hwNatStatUDPPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStatUDPPktsCount.setStatus("current")
_HwNatStatICMPPktsCount_Type = Counter64
_HwNatStatICMPPktsCount_Object = MibScalar
hwNatStatICMPPktsCount = _HwNatStatICMPPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 2, 2, 5),
    _HwNatStatICMPPktsCount_Type()
)
hwNatStatICMPPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStatICMPPktsCount.setStatus("current")
_HwNatConformance_ObjectIdentity = ObjectIdentity
hwNatConformance = _HwNatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 3)
)
_HwNatMibGroups_ObjectIdentity = ObjectIdentity
hwNatMibGroups = _HwNatMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 3, 1)
)

# Managed Objects groups

hwNatCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 3, 1, 1)
)
hwNatCfgGroup.setObjects(
      *(("HUAWEI-NAT-MIB", "hwNatAddrGrpBeginningIpAddr"),
        ("HUAWEI-NAT-MIB", "hwNatAddrGrpEndingIpAddr"),
        ("HUAWEI-NAT-MIB", "hwNatAddrGrpRowstatus"),
        ("HUAWEI-NAT-MIB", "hwNatAddrGrpVrrpID"),
        ("HUAWEI-NAT-MIB", "hwNatAddrGrpVrfName"),
        ("HUAWEI-NAT-MIB", "hwNatServerProtocol"),
        ("HUAWEI-NAT-MIB", "hwNatServerInsideBeginIpAddr"),
        ("HUAWEI-NAT-MIB", "hwNatServerInsideEndIpAddr"),
        ("HUAWEI-NAT-MIB", "hwNatServerInsidePort"),
        ("HUAWEI-NAT-MIB", "hwNatServerRowStatus"),
        ("HUAWEI-NAT-MIB", "hwNatTimeoutValue"),
        ("HUAWEI-NAT-MIB", "hwNatAlgEnableFlag"),
        ("HUAWEI-NAT-MIB", "hwNatAddrGrpRefCount"),
        ("HUAWEI-NAT-MIB", "hwNatServerOutsideIpAddr"),
        ("HUAWEI-NAT-MIB", "hwNatServerOutsideBeginPort"),
        ("HUAWEI-NAT-MIB", "hwNatServerOutsideEndPort"),
        ("HUAWEI-NAT-MIB", "hwNatServerVrrpID"),
        ("HUAWEI-NAT-MIB", "hwNatServerVrfName"))
)
if mibBuilder.loadTexts:
    hwNatCfgGroup.setStatus("current")

hwNatMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 1, 3, 1, 2)
)
hwNatMonitorGroup.setObjects(
      *(("HUAWEI-NAT-MIB", "hwNatHashStatPatCount"),
        ("HUAWEI-NAT-MIB", "hwNatHashStatNoPatCount"),
        ("HUAWEI-NAT-MIB", "hwNatHashStatServerHashCount"),
        ("HUAWEI-NAT-MIB", "hwNatHashStatFragHashCount"),
        ("HUAWEI-NAT-MIB", "hwNatStatPktsCount"),
        ("HUAWEI-NAT-MIB", "hwNatStatFailedPktsCount"),
        ("HUAWEI-NAT-MIB", "hwNatStatTCPPktsCount"),
        ("HUAWEI-NAT-MIB", "hwNatStatUDPPktsCount"),
        ("HUAWEI-NAT-MIB", "hwNatStatICMPPktsCount"))
)
if mibBuilder.loadTexts:
    hwNatMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-NAT-MIB",
    **{"SessionType": SessionType,
       "AlgType": AlgType,
       "NatType": NatType,
       "hwNAT": hwNAT,
       "hwNATCommon": hwNATCommon,
       "hwNatMibObjects": hwNatMibObjects,
       "hwNatAddressGroupInfoTable": hwNatAddressGroupInfoTable,
       "hwNatAddressGroupInfoEntry": hwNatAddressGroupInfoEntry,
       "hwNatAddrGrpIndex": hwNatAddrGrpIndex,
       "hwNatAddrGrpBeginningIpAddr": hwNatAddrGrpBeginningIpAddr,
       "hwNatAddrGrpEndingIpAddr": hwNatAddrGrpEndingIpAddr,
       "hwNatAddrGrpRefCount": hwNatAddrGrpRefCount,
       "hwNatAddrGrpRowstatus": hwNatAddrGrpRowstatus,
       "hwNatAddrGrpVrrpID": hwNatAddrGrpVrrpID,
       "hwNatAddrGrpVrfName": hwNatAddrGrpVrfName,
       "hwNatInternalServerTable": hwNatInternalServerTable,
       "hwNatInternalServerEntry": hwNatInternalServerEntry,
       "hwNatServerIndex": hwNatServerIndex,
       "hwNatServerProtocol": hwNatServerProtocol,
       "hwNatServerInsideBeginIpAddr": hwNatServerInsideBeginIpAddr,
       "hwNatServerInsideEndIpAddr": hwNatServerInsideEndIpAddr,
       "hwNatServerInsidePort": hwNatServerInsidePort,
       "hwNatServerOutsideIpAddr": hwNatServerOutsideIpAddr,
       "hwNatServerOutsideBeginPort": hwNatServerOutsideBeginPort,
       "hwNatServerOutsideEndPort": hwNatServerOutsideEndPort,
       "hwNatServerRowStatus": hwNatServerRowStatus,
       "hwNatServerVrrpID": hwNatServerVrrpID,
       "hwNatServerVrfName": hwNatServerVrfName,
       "hwNatTimeoutTable": hwNatTimeoutTable,
       "hwNatTimeoutEntry": hwNatTimeoutEntry,
       "hwNatTimeoutSessionType": hwNatTimeoutSessionType,
       "hwNatTimeoutValue": hwNatTimeoutValue,
       "hwNatAlgEnableTable": hwNatAlgEnableTable,
       "hwNatAlgEnableEntry": hwNatAlgEnableEntry,
       "hwNatAlgEnableProtocol": hwNatAlgEnableProtocol,
       "hwNatAlgEnableFlag": hwNatAlgEnableFlag,
       "hwNatMonitorObjects": hwNatMonitorObjects,
       "hwNatMonitorGlobalHash": hwNatMonitorGlobalHash,
       "hwNatHashStatPatCount": hwNatHashStatPatCount,
       "hwNatHashStatNoPatCount": hwNatHashStatNoPatCount,
       "hwNatHashStatServerHashCount": hwNatHashStatServerHashCount,
       "hwNatHashStatFragHashCount": hwNatHashStatFragHashCount,
       "hwNatMonitorGlobalPkts": hwNatMonitorGlobalPkts,
       "hwNatStatPktsCount": hwNatStatPktsCount,
       "hwNatStatFailedPktsCount": hwNatStatFailedPktsCount,
       "hwNatStatTCPPktsCount": hwNatStatTCPPktsCount,
       "hwNatStatUDPPktsCount": hwNatStatUDPPktsCount,
       "hwNatStatICMPPktsCount": hwNatStatICMPPktsCount,
       "hwNatConformance": hwNatConformance,
       "hwNatMibGroups": hwNatMibGroups,
       "hwNatCfgGroup": hwNatCfgGroup,
       "hwNatMonitorGroup": hwNatMonitorGroup}
)
