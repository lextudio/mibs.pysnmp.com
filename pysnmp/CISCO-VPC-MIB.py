# SNMP MIB module (CISCO-VPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:33 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807)
)
ciscoVpcMIB.setRevisions(
        ("2013-05-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVpcMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVpcMIBNotifs = _CiscoVpcMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 0)
)
_CiscoVpcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVpcMIBObjects = _CiscoVpcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1)
)
_CVpcPeerKeepAlive_ObjectIdentity = ObjectIdentity
cVpcPeerKeepAlive = _CVpcPeerKeepAlive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1)
)
_CVpcPeerKeepAliveConfigTable_Object = MibTable
cVpcPeerKeepAliveConfigTable = _CVpcPeerKeepAliveConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveConfigTable.setStatus("current")
_CVpcPeerKeepAliveConfigEntry_Object = MibTableRow
cVpcPeerKeepAliveConfigEntry = _CVpcPeerKeepAliveConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1)
)
cVpcPeerKeepAliveConfigEntry.setIndexNames(
    (0, "CISCO-VPC-MIB", "cVpcPeerKeepAliveConfigDomainID"),
)
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveConfigEntry.setStatus("current")
_CVpcPeerKeepAliveConfigDomainID_Type = Unsigned32
_CVpcPeerKeepAliveConfigDomainID_Object = MibTableColumn
cVpcPeerKeepAliveConfigDomainID = _CVpcPeerKeepAliveConfigDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 1),
    _CVpcPeerKeepAliveConfigDomainID_Type()
)
cVpcPeerKeepAliveConfigDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveConfigDomainID.setStatus("current")
_CVpcPeerKeepAliveDestAddrType_Type = InetAddressType
_CVpcPeerKeepAliveDestAddrType_Object = MibTableColumn
cVpcPeerKeepAliveDestAddrType = _CVpcPeerKeepAliveDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 2),
    _CVpcPeerKeepAliveDestAddrType_Type()
)
cVpcPeerKeepAliveDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveDestAddrType.setStatus("current")
_CVpcPeerKeepAliveDestAddr_Type = InetAddress
_CVpcPeerKeepAliveDestAddr_Object = MibTableColumn
cVpcPeerKeepAliveDestAddr = _CVpcPeerKeepAliveDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 3),
    _CVpcPeerKeepAliveDestAddr_Type()
)
cVpcPeerKeepAliveDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveDestAddr.setStatus("current")
_CVpcPeerKeepAliveSourceAddrType_Type = InetAddressType
_CVpcPeerKeepAliveSourceAddrType_Object = MibTableColumn
cVpcPeerKeepAliveSourceAddrType = _CVpcPeerKeepAliveSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 4),
    _CVpcPeerKeepAliveSourceAddrType_Type()
)
cVpcPeerKeepAliveSourceAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveSourceAddrType.setStatus("current")
_CVpcPeerKeepAliveSourceAddr_Type = InetAddress
_CVpcPeerKeepAliveSourceAddr_Object = MibTableColumn
cVpcPeerKeepAliveSourceAddr = _CVpcPeerKeepAliveSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 5),
    _CVpcPeerKeepAliveSourceAddr_Type()
)
cVpcPeerKeepAliveSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveSourceAddr.setStatus("current")


class _CVpcPeerKeepAliveUdpPort_Type(InetPortNumber):
    """Custom type cVpcPeerKeepAliveUdpPort based on InetPortNumber"""
    defaultValue = 3200


_CVpcPeerKeepAliveUdpPort_Object = MibTableColumn
cVpcPeerKeepAliveUdpPort = _CVpcPeerKeepAliveUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 6),
    _CVpcPeerKeepAliveUdpPort_Type()
)
cVpcPeerKeepAliveUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveUdpPort.setStatus("current")


class _CVpcPeerKeepAliveInterval_Type(Unsigned32):
    """Custom type cVpcPeerKeepAliveInterval based on Unsigned32"""
    defaultValue = 1000


_CVpcPeerKeepAliveInterval_Object = MibTableColumn
cVpcPeerKeepAliveInterval = _CVpcPeerKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 7),
    _CVpcPeerKeepAliveInterval_Type()
)
cVpcPeerKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveInterval.setUnits("milli-seconds")


class _CVpcPeerKeepAliveTimeout_Type(Unsigned32):
    """Custom type cVpcPeerKeepAliveTimeout based on Unsigned32"""
    defaultValue = 5


_CVpcPeerKeepAliveTimeout_Object = MibTableColumn
cVpcPeerKeepAliveTimeout = _CVpcPeerKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 8),
    _CVpcPeerKeepAliveTimeout_Type()
)
cVpcPeerKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTimeout.setUnits("seconds")


class _CVpcPeerKeepAliveHoldTimeout_Type(Unsigned32):
    """Custom type cVpcPeerKeepAliveHoldTimeout based on Unsigned32"""
    defaultValue = 3


_CVpcPeerKeepAliveHoldTimeout_Object = MibTableColumn
cVpcPeerKeepAliveHoldTimeout = _CVpcPeerKeepAliveHoldTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 9),
    _CVpcPeerKeepAliveHoldTimeout_Type()
)
cVpcPeerKeepAliveHoldTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveHoldTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveHoldTimeout.setUnits("seconds")


class _CVpcPeerKeepAliveTos_Type(Unsigned32):
    """Custom type cVpcPeerKeepAliveTos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CVpcPeerKeepAliveTos_Type.__name__ = "Unsigned32"
_CVpcPeerKeepAliveTos_Object = MibTableColumn
cVpcPeerKeepAliveTos = _CVpcPeerKeepAliveTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 10),
    _CVpcPeerKeepAliveTos_Type()
)
cVpcPeerKeepAliveTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTos.setStatus("current")


class _CVpcPeerKeepAlivePrecedence_Type(Unsigned32):
    """Custom type cVpcPeerKeepAlivePrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CVpcPeerKeepAlivePrecedence_Type.__name__ = "Unsigned32"
_CVpcPeerKeepAlivePrecedence_Object = MibTableColumn
cVpcPeerKeepAlivePrecedence = _CVpcPeerKeepAlivePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 11),
    _CVpcPeerKeepAlivePrecedence_Type()
)
cVpcPeerKeepAlivePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAlivePrecedence.setStatus("current")


class _CVpcPeerKeepAliveTosByte_Type(Unsigned32):
    """Custom type cVpcPeerKeepAliveTosByte based on Unsigned32"""
    defaultValue = 192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CVpcPeerKeepAliveTosByte_Type.__name__ = "Unsigned32"
_CVpcPeerKeepAliveTosByte_Object = MibTableColumn
cVpcPeerKeepAliveTosByte = _CVpcPeerKeepAliveTosByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 12),
    _CVpcPeerKeepAliveTosByte_Type()
)
cVpcPeerKeepAliveTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTosByte.setStatus("current")


class _CVpcPeerKeepAliveVrfName_Type(SnmpAdminString):
    """Custom type cVpcPeerKeepAliveVrfName based on SnmpAdminString"""
    defaultValue = OctetString("management")


_CVpcPeerKeepAliveVrfName_Object = MibTableColumn
cVpcPeerKeepAliveVrfName = _CVpcPeerKeepAliveVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 1, 1, 13),
    _CVpcPeerKeepAliveVrfName_Type()
)
cVpcPeerKeepAliveVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveVrfName.setStatus("current")
_CVpcPeerKeepAliveTable_Object = MibTable
cVpcPeerKeepAliveTable = _CVpcPeerKeepAliveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTable.setStatus("current")
_CVpcPeerKeepAliveEntry_Object = MibTableRow
cVpcPeerKeepAliveEntry = _CVpcPeerKeepAliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1)
)
cVpcPeerKeepAliveEntry.setIndexNames(
    (0, "CISCO-VPC-MIB", "cVpcPeerKeepAliveDomainID"),
)
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveEntry.setStatus("current")
_CVpcPeerKeepAliveDomainID_Type = Unsigned32
_CVpcPeerKeepAliveDomainID_Object = MibTableColumn
cVpcPeerKeepAliveDomainID = _CVpcPeerKeepAliveDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 1),
    _CVpcPeerKeepAliveDomainID_Type()
)
cVpcPeerKeepAliveDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveDomainID.setStatus("current")


class _CVpcPeerKeepAliveStatus_Type(Integer32):
    """Custom type cVpcPeerKeepAliveStatus based on Integer32"""
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
        *(("alive", 2),
          ("aliveButDomainIdDismatch", 4),
          ("disabled", 1),
          ("misconfigured", 8),
          ("peerUnreachable", 3),
          ("suspendedAsDestIPUnreachable", 6),
          ("suspendedAsISSU", 5),
          ("suspendedAsVRFUnusable", 7))
    )


_CVpcPeerKeepAliveStatus_Type.__name__ = "Integer32"
_CVpcPeerKeepAliveStatus_Object = MibTableColumn
cVpcPeerKeepAliveStatus = _CVpcPeerKeepAliveStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 2),
    _CVpcPeerKeepAliveStatus_Type()
)
cVpcPeerKeepAliveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveStatus.setStatus("current")
_CVpcPeerKeepAliveTime_Type = CounterBasedGauge64
_CVpcPeerKeepAliveTime_Object = MibTableColumn
cVpcPeerKeepAliveTime = _CVpcPeerKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 3),
    _CVpcPeerKeepAliveTime_Type()
)
cVpcPeerKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveTime.setUnits("milli-seconds")


class _CVpcPeerKeepAliveMsgSendStatus_Type(Integer32):
    """Custom type cVpcPeerKeepAliveMsgSendStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_CVpcPeerKeepAliveMsgSendStatus_Type.__name__ = "Integer32"
_CVpcPeerKeepAliveMsgSendStatus_Object = MibTableColumn
cVpcPeerKeepAliveMsgSendStatus = _CVpcPeerKeepAliveMsgSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 4),
    _CVpcPeerKeepAliveMsgSendStatus_Type()
)
cVpcPeerKeepAliveMsgSendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveMsgSendStatus.setStatus("current")
_CVpcPeerKeepAliveMsgLastSendTime_Type = DateAndTime
_CVpcPeerKeepAliveMsgLastSendTime_Object = MibTableColumn
cVpcPeerKeepAliveMsgLastSendTime = _CVpcPeerKeepAliveMsgLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 5),
    _CVpcPeerKeepAliveMsgLastSendTime_Type()
)
cVpcPeerKeepAliveMsgLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveMsgLastSendTime.setStatus("current")
_CVpcPeerKeepAliveMsgSendInterface_Type = InterfaceIndexOrZero
_CVpcPeerKeepAliveMsgSendInterface_Object = MibTableColumn
cVpcPeerKeepAliveMsgSendInterface = _CVpcPeerKeepAliveMsgSendInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 6),
    _CVpcPeerKeepAliveMsgSendInterface_Type()
)
cVpcPeerKeepAliveMsgSendInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveMsgSendInterface.setStatus("current")


class _CVpcPeerKeepAliveMsgRcvrStatus_Type(Integer32):
    """Custom type cVpcPeerKeepAliveMsgRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_CVpcPeerKeepAliveMsgRcvrStatus_Type.__name__ = "Integer32"
_CVpcPeerKeepAliveMsgRcvrStatus_Object = MibTableColumn
cVpcPeerKeepAliveMsgRcvrStatus = _CVpcPeerKeepAliveMsgRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 7),
    _CVpcPeerKeepAliveMsgRcvrStatus_Type()
)
cVpcPeerKeepAliveMsgRcvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveMsgRcvrStatus.setStatus("current")
_CVpcPeerKeepAliveMsgLastReceiveTime_Type = DateAndTime
_CVpcPeerKeepAliveMsgLastReceiveTime_Object = MibTableColumn
cVpcPeerKeepAliveMsgLastReceiveTime = _CVpcPeerKeepAliveMsgLastReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 8),
    _CVpcPeerKeepAliveMsgLastReceiveTime_Type()
)
cVpcPeerKeepAliveMsgLastReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveMsgLastReceiveTime.setStatus("current")
_CVpcPeerKeepAliveMsgReceiveInterface_Type = InterfaceIndexOrZero
_CVpcPeerKeepAliveMsgReceiveInterface_Object = MibTableColumn
cVpcPeerKeepAliveMsgReceiveInterface = _CVpcPeerKeepAliveMsgReceiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 1, 2, 1, 9),
    _CVpcPeerKeepAliveMsgReceiveInterface_Type()
)
cVpcPeerKeepAliveMsgReceiveInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveMsgReceiveInterface.setStatus("current")
_CVpcRole_ObjectIdentity = ObjectIdentity
cVpcRole = _CVpcRole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2)
)
_CVpcRoleTable_Object = MibTable
cVpcRoleTable = _CVpcRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cVpcRoleTable.setStatus("current")
_CVpcRoleEntry_Object = MibTableRow
cVpcRoleEntry = _CVpcRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1)
)
cVpcRoleEntry.setIndexNames(
    (0, "CISCO-VPC-MIB", "cVpcRoleDomainID"),
)
if mibBuilder.loadTexts:
    cVpcRoleEntry.setStatus("current")
_CVpcRoleDomainID_Type = Unsigned32
_CVpcRoleDomainID_Object = MibTableColumn
cVpcRoleDomainID = _CVpcRoleDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 1),
    _CVpcRoleDomainID_Type()
)
cVpcRoleDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcRoleDomainID.setStatus("current")


class _CVpcRoleStatus_Type(Integer32):
    """Custom type cVpcRoleStatus based on Integer32"""
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
        *(("noneEstablished", 5),
          ("primary", 2),
          ("primarySecondary", 1),
          ("secondary", 4),
          ("secondaryPrimary", 3))
    )


_CVpcRoleStatus_Type.__name__ = "Integer32"
_CVpcRoleStatus_Object = MibTableColumn
cVpcRoleStatus = _CVpcRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 2),
    _CVpcRoleStatus_Type()
)
cVpcRoleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcRoleStatus.setStatus("current")
_CVpcDualActiveDetectionStatus_Type = TruthValue
_CVpcDualActiveDetectionStatus_Object = MibTableColumn
cVpcDualActiveDetectionStatus = _CVpcDualActiveDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 3),
    _CVpcDualActiveDetectionStatus_Type()
)
cVpcDualActiveDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcDualActiveDetectionStatus.setStatus("current")
_CVpcSystemAdminMacAddress_Type = MacAddress
_CVpcSystemAdminMacAddress_Object = MibTableColumn
cVpcSystemAdminMacAddress = _CVpcSystemAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 4),
    _CVpcSystemAdminMacAddress_Type()
)
cVpcSystemAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcSystemAdminMacAddress.setStatus("current")
_CVpcSystemOperMacAddress_Type = MacAddress
_CVpcSystemOperMacAddress_Object = MibTableColumn
cVpcSystemOperMacAddress = _CVpcSystemOperMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 5),
    _CVpcSystemOperMacAddress_Type()
)
cVpcSystemOperMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcSystemOperMacAddress.setStatus("current")
_CVpcLocalOperMacAddress_Type = MacAddress
_CVpcLocalOperMacAddress_Object = MibTableColumn
cVpcLocalOperMacAddress = _CVpcLocalOperMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 6),
    _CVpcLocalOperMacAddress_Type()
)
cVpcLocalOperMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcLocalOperMacAddress.setStatus("current")
_CVpcSystemAdminPriority_Type = Unsigned32
_CVpcSystemAdminPriority_Object = MibTableColumn
cVpcSystemAdminPriority = _CVpcSystemAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 7),
    _CVpcSystemAdminPriority_Type()
)
cVpcSystemAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcSystemAdminPriority.setStatus("current")
_CVpcSystemOperPriority_Type = Unsigned32
_CVpcSystemOperPriority_Object = MibTableColumn
cVpcSystemOperPriority = _CVpcSystemOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 8),
    _CVpcSystemOperPriority_Type()
)
cVpcSystemOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcSystemOperPriority.setStatus("current")
_CVpcLocalRoleAdminPriority_Type = Unsigned32
_CVpcLocalRoleAdminPriority_Object = MibTableColumn
cVpcLocalRoleAdminPriority = _CVpcLocalRoleAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 9),
    _CVpcLocalRoleAdminPriority_Type()
)
cVpcLocalRoleAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVpcLocalRoleAdminPriority.setStatus("current")
_CVpcLocalRoleOperPriority_Type = Unsigned32
_CVpcLocalRoleOperPriority_Object = MibTableColumn
cVpcLocalRoleOperPriority = _CVpcLocalRoleOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 2, 1, 1, 10),
    _CVpcLocalRoleOperPriority_Type()
)
cVpcLocalRoleOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcLocalRoleOperPriority.setStatus("current")
_CVpcStatistics_ObjectIdentity = ObjectIdentity
cVpcStatistics = _CVpcStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3)
)
_CVpcStatsPeerKeepAliveTable_Object = MibTable
cVpcStatsPeerKeepAliveTable = _CVpcStatsPeerKeepAliveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveTable.setStatus("current")
_CVpcStatsPeerKeepAliveEntry_Object = MibTableRow
cVpcStatsPeerKeepAliveEntry = _CVpcStatsPeerKeepAliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1, 1)
)
cVpcStatsPeerKeepAliveEntry.setIndexNames(
    (0, "CISCO-VPC-MIB", "cVpcStatsPeerKeepAliveDomainID"),
)
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveEntry.setStatus("current")
_CVpcStatsPeerKeepAliveDomainID_Type = Unsigned32
_CVpcStatsPeerKeepAliveDomainID_Object = MibTableColumn
cVpcStatsPeerKeepAliveDomainID = _CVpcStatsPeerKeepAliveDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1, 1, 1),
    _CVpcStatsPeerKeepAliveDomainID_Type()
)
cVpcStatsPeerKeepAliveDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveDomainID.setStatus("current")
_CVpcStatsPeerKeepAliveMsgsSent_Type = Counter32
_CVpcStatsPeerKeepAliveMsgsSent_Object = MibTableColumn
cVpcStatsPeerKeepAliveMsgsSent = _CVpcStatsPeerKeepAliveMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1, 1, 2),
    _CVpcStatsPeerKeepAliveMsgsSent_Type()
)
cVpcStatsPeerKeepAliveMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveMsgsSent.setStatus("current")
_CVpcStatsPeerKeepAliveMsgsRcved_Type = Counter32
_CVpcStatsPeerKeepAliveMsgsRcved_Object = MibTableColumn
cVpcStatsPeerKeepAliveMsgsRcved = _CVpcStatsPeerKeepAliveMsgsRcved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1, 1, 3),
    _CVpcStatsPeerKeepAliveMsgsRcved_Type()
)
cVpcStatsPeerKeepAliveMsgsRcved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveMsgsRcved.setStatus("current")
_CVpcStatsPeerKeepAliveAvgInterval_Type = Unsigned32
_CVpcStatsPeerKeepAliveAvgInterval_Object = MibTableColumn
cVpcStatsPeerKeepAliveAvgInterval = _CVpcStatsPeerKeepAliveAvgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1, 1, 4),
    _CVpcStatsPeerKeepAliveAvgInterval_Type()
)
cVpcStatsPeerKeepAliveAvgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveAvgInterval.setStatus("current")
if mibBuilder.loadTexts:
    cVpcStatsPeerKeepAliveAvgInterval.setUnits("seconds")
_CVpcStatsPeerStatusChangeCount_Type = Counter32
_CVpcStatsPeerStatusChangeCount_Object = MibTableColumn
cVpcStatsPeerStatusChangeCount = _CVpcStatsPeerStatusChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 3, 1, 1, 5),
    _CVpcStatsPeerStatusChangeCount_Type()
)
cVpcStatsPeerStatusChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatsPeerStatusChangeCount.setStatus("current")
_CVpcStatus_ObjectIdentity = ObjectIdentity
cVpcStatus = _CVpcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4)
)
_CVpcStatusPeerLinkTable_Object = MibTable
cVpcStatusPeerLinkTable = _CVpcStatusPeerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cVpcStatusPeerLinkTable.setStatus("current")
_CVpcStatusPeerLinkEntry_Object = MibTableRow
cVpcStatusPeerLinkEntry = _CVpcStatusPeerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 1, 1)
)
cVpcStatusPeerLinkEntry.setIndexNames(
    (0, "CISCO-VPC-MIB", "cVpcStatusPeerLinkDomainID"),
)
if mibBuilder.loadTexts:
    cVpcStatusPeerLinkEntry.setStatus("current")
_CVpcStatusPeerLinkDomainID_Type = Unsigned32
_CVpcStatusPeerLinkDomainID_Object = MibTableColumn
cVpcStatusPeerLinkDomainID = _CVpcStatusPeerLinkDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 1, 1, 1),
    _CVpcStatusPeerLinkDomainID_Type()
)
cVpcStatusPeerLinkDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcStatusPeerLinkDomainID.setStatus("current")
_CVpcStatusPeerLinkIfIndex_Type = InterfaceIndex
_CVpcStatusPeerLinkIfIndex_Object = MibTableColumn
cVpcStatusPeerLinkIfIndex = _CVpcStatusPeerLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 1, 1, 2),
    _CVpcStatusPeerLinkIfIndex_Type()
)
cVpcStatusPeerLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatusPeerLinkIfIndex.setStatus("current")
_CVpcStatusHostLinkTable_Object = MibTable
cVpcStatusHostLinkTable = _CVpcStatusHostLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cVpcStatusHostLinkTable.setStatus("current")
_CVpcStatusHostLinkEntry_Object = MibTableRow
cVpcStatusHostLinkEntry = _CVpcStatusHostLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1)
)
cVpcStatusHostLinkEntry.setIndexNames(
    (0, "CISCO-VPC-MIB", "cVpcStatusHostLinkDomainID"),
    (0, "CISCO-VPC-MIB", "cVpcStatusHostLinkVpcID"),
)
if mibBuilder.loadTexts:
    cVpcStatusHostLinkEntry.setStatus("current")
_CVpcStatusHostLinkDomainID_Type = Unsigned32
_CVpcStatusHostLinkDomainID_Object = MibTableColumn
cVpcStatusHostLinkDomainID = _CVpcStatusHostLinkDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1, 1),
    _CVpcStatusHostLinkDomainID_Type()
)
cVpcStatusHostLinkDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcStatusHostLinkDomainID.setStatus("current")
_CVpcStatusHostLinkVpcID_Type = Unsigned32
_CVpcStatusHostLinkVpcID_Object = MibTableColumn
cVpcStatusHostLinkVpcID = _CVpcStatusHostLinkVpcID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1, 2),
    _CVpcStatusHostLinkVpcID_Type()
)
cVpcStatusHostLinkVpcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVpcStatusHostLinkVpcID.setStatus("current")
_CVpcStatusHostLinkIfIndex_Type = InterfaceIndexOrZero
_CVpcStatusHostLinkIfIndex_Object = MibTableColumn
cVpcStatusHostLinkIfIndex = _CVpcStatusHostLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1, 3),
    _CVpcStatusHostLinkIfIndex_Type()
)
cVpcStatusHostLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatusHostLinkIfIndex.setStatus("current")


class _CVpcStatusHostLinkStatus_Type(Integer32):
    """Custom type cVpcStatusHostLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("downStar", 2),
          ("up", 3))
    )


_CVpcStatusHostLinkStatus_Type.__name__ = "Integer32"
_CVpcStatusHostLinkStatus_Object = MibTableColumn
cVpcStatusHostLinkStatus = _CVpcStatusHostLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1, 4),
    _CVpcStatusHostLinkStatus_Type()
)
cVpcStatusHostLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatusHostLinkStatus.setStatus("current")


class _CVpcStatusHostLinkConsistencyStatus_Type(Integer32):
    """Custom type cVpcStatusHostLinkConsistencyStatus based on Integer32"""
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
          ("notApplicable", 3),
          ("success", 1))
    )


_CVpcStatusHostLinkConsistencyStatus_Type.__name__ = "Integer32"
_CVpcStatusHostLinkConsistencyStatus_Object = MibTableColumn
cVpcStatusHostLinkConsistencyStatus = _CVpcStatusHostLinkConsistencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1, 5),
    _CVpcStatusHostLinkConsistencyStatus_Type()
)
cVpcStatusHostLinkConsistencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatusHostLinkConsistencyStatus.setStatus("current")
_CVpcStatusHostLinkConsistencyDetail_Type = SnmpAdminString
_CVpcStatusHostLinkConsistencyDetail_Object = MibTableColumn
cVpcStatusHostLinkConsistencyDetail = _CVpcStatusHostLinkConsistencyDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 1, 4, 2, 1, 6),
    _CVpcStatusHostLinkConsistencyDetail_Type()
)
cVpcStatusHostLinkConsistencyDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVpcStatusHostLinkConsistencyDetail.setStatus("current")
_CiscoVpcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVpcMIBConformance = _CiscoVpcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2)
)
_CiscoVpcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVpcMIBCompliances = _CiscoVpcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 1)
)
_CiscoVpcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVpcMIBGroups = _CiscoVpcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2)
)

# Managed Objects groups

cVpcPeerKeepAliveConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2, 1)
)
cVpcPeerKeepAliveConfigInfoGroup.setObjects(
      *(("CISCO-VPC-MIB", "cVpcPeerKeepAliveDestAddrType"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveDestAddr"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveSourceAddrType"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveSourceAddr"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveUdpPort"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveInterval"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveTimeout"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveHoldTimeout"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveTos"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAlivePrecedence"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveTosByte"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveVrfName"))
)
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveConfigInfoGroup.setStatus("current")

cVpcPeerKeepAliveStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2, 2)
)
cVpcPeerKeepAliveStatusInfoGroup.setObjects(
      *(("CISCO-VPC-MIB", "cVpcPeerKeepAliveStatus"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveTime"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveMsgSendStatus"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveMsgLastSendTime"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveMsgSendInterface"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveMsgRcvrStatus"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveMsgLastReceiveTime"),
        ("CISCO-VPC-MIB", "cVpcPeerKeepAliveMsgReceiveInterface"))
)
if mibBuilder.loadTexts:
    cVpcPeerKeepAliveStatusInfoGroup.setStatus("current")

cVpcMIBRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2, 3)
)
cVpcMIBRoleGroup.setObjects(
      *(("CISCO-VPC-MIB", "cVpcRoleStatus"),
        ("CISCO-VPC-MIB", "cVpcDualActiveDetectionStatus"),
        ("CISCO-VPC-MIB", "cVpcSystemAdminMacAddress"),
        ("CISCO-VPC-MIB", "cVpcSystemOperMacAddress"),
        ("CISCO-VPC-MIB", "cVpcLocalOperMacAddress"),
        ("CISCO-VPC-MIB", "cVpcSystemAdminPriority"),
        ("CISCO-VPC-MIB", "cVpcSystemOperPriority"),
        ("CISCO-VPC-MIB", "cVpcLocalRoleAdminPriority"),
        ("CISCO-VPC-MIB", "cVpcLocalRoleOperPriority"))
)
if mibBuilder.loadTexts:
    cVpcMIBRoleGroup.setStatus("current")

cVpcMIBStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2, 4)
)
cVpcMIBStatisticsGroup.setObjects(
      *(("CISCO-VPC-MIB", "cVpcStatsPeerKeepAliveMsgsSent"),
        ("CISCO-VPC-MIB", "cVpcStatsPeerKeepAliveMsgsRcved"),
        ("CISCO-VPC-MIB", "cVpcStatsPeerKeepAliveAvgInterval"),
        ("CISCO-VPC-MIB", "cVpcStatsPeerStatusChangeCount"))
)
if mibBuilder.loadTexts:
    cVpcMIBStatisticsGroup.setStatus("current")

cVpcMIBPeerLinkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2, 5)
)
cVpcMIBPeerLinkStatusGroup.setObjects(
    ("CISCO-VPC-MIB", "cVpcStatusPeerLinkIfIndex")
)
if mibBuilder.loadTexts:
    cVpcMIBPeerLinkStatusGroup.setStatus("current")

cVpcMIBHostLinkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 2, 6)
)
cVpcMIBHostLinkStatusGroup.setObjects(
      *(("CISCO-VPC-MIB", "cVpcStatusHostLinkIfIndex"),
        ("CISCO-VPC-MIB", "cVpcStatusHostLinkStatus"),
        ("CISCO-VPC-MIB", "cVpcStatusHostLinkConsistencyStatus"),
        ("CISCO-VPC-MIB", "cVpcStatusHostLinkConsistencyDetail"))
)
if mibBuilder.loadTexts:
    cVpcMIBHostLinkStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVpcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 807, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVpcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VPC-MIB",
    **{"ciscoVpcMIB": ciscoVpcMIB,
       "ciscoVpcMIBNotifs": ciscoVpcMIBNotifs,
       "ciscoVpcMIBObjects": ciscoVpcMIBObjects,
       "cVpcPeerKeepAlive": cVpcPeerKeepAlive,
       "cVpcPeerKeepAliveConfigTable": cVpcPeerKeepAliveConfigTable,
       "cVpcPeerKeepAliveConfigEntry": cVpcPeerKeepAliveConfigEntry,
       "cVpcPeerKeepAliveConfigDomainID": cVpcPeerKeepAliveConfigDomainID,
       "cVpcPeerKeepAliveDestAddrType": cVpcPeerKeepAliveDestAddrType,
       "cVpcPeerKeepAliveDestAddr": cVpcPeerKeepAliveDestAddr,
       "cVpcPeerKeepAliveSourceAddrType": cVpcPeerKeepAliveSourceAddrType,
       "cVpcPeerKeepAliveSourceAddr": cVpcPeerKeepAliveSourceAddr,
       "cVpcPeerKeepAliveUdpPort": cVpcPeerKeepAliveUdpPort,
       "cVpcPeerKeepAliveInterval": cVpcPeerKeepAliveInterval,
       "cVpcPeerKeepAliveTimeout": cVpcPeerKeepAliveTimeout,
       "cVpcPeerKeepAliveHoldTimeout": cVpcPeerKeepAliveHoldTimeout,
       "cVpcPeerKeepAliveTos": cVpcPeerKeepAliveTos,
       "cVpcPeerKeepAlivePrecedence": cVpcPeerKeepAlivePrecedence,
       "cVpcPeerKeepAliveTosByte": cVpcPeerKeepAliveTosByte,
       "cVpcPeerKeepAliveVrfName": cVpcPeerKeepAliveVrfName,
       "cVpcPeerKeepAliveTable": cVpcPeerKeepAliveTable,
       "cVpcPeerKeepAliveEntry": cVpcPeerKeepAliveEntry,
       "cVpcPeerKeepAliveDomainID": cVpcPeerKeepAliveDomainID,
       "cVpcPeerKeepAliveStatus": cVpcPeerKeepAliveStatus,
       "cVpcPeerKeepAliveTime": cVpcPeerKeepAliveTime,
       "cVpcPeerKeepAliveMsgSendStatus": cVpcPeerKeepAliveMsgSendStatus,
       "cVpcPeerKeepAliveMsgLastSendTime": cVpcPeerKeepAliveMsgLastSendTime,
       "cVpcPeerKeepAliveMsgSendInterface": cVpcPeerKeepAliveMsgSendInterface,
       "cVpcPeerKeepAliveMsgRcvrStatus": cVpcPeerKeepAliveMsgRcvrStatus,
       "cVpcPeerKeepAliveMsgLastReceiveTime": cVpcPeerKeepAliveMsgLastReceiveTime,
       "cVpcPeerKeepAliveMsgReceiveInterface": cVpcPeerKeepAliveMsgReceiveInterface,
       "cVpcRole": cVpcRole,
       "cVpcRoleTable": cVpcRoleTable,
       "cVpcRoleEntry": cVpcRoleEntry,
       "cVpcRoleDomainID": cVpcRoleDomainID,
       "cVpcRoleStatus": cVpcRoleStatus,
       "cVpcDualActiveDetectionStatus": cVpcDualActiveDetectionStatus,
       "cVpcSystemAdminMacAddress": cVpcSystemAdminMacAddress,
       "cVpcSystemOperMacAddress": cVpcSystemOperMacAddress,
       "cVpcLocalOperMacAddress": cVpcLocalOperMacAddress,
       "cVpcSystemAdminPriority": cVpcSystemAdminPriority,
       "cVpcSystemOperPriority": cVpcSystemOperPriority,
       "cVpcLocalRoleAdminPriority": cVpcLocalRoleAdminPriority,
       "cVpcLocalRoleOperPriority": cVpcLocalRoleOperPriority,
       "cVpcStatistics": cVpcStatistics,
       "cVpcStatsPeerKeepAliveTable": cVpcStatsPeerKeepAliveTable,
       "cVpcStatsPeerKeepAliveEntry": cVpcStatsPeerKeepAliveEntry,
       "cVpcStatsPeerKeepAliveDomainID": cVpcStatsPeerKeepAliveDomainID,
       "cVpcStatsPeerKeepAliveMsgsSent": cVpcStatsPeerKeepAliveMsgsSent,
       "cVpcStatsPeerKeepAliveMsgsRcved": cVpcStatsPeerKeepAliveMsgsRcved,
       "cVpcStatsPeerKeepAliveAvgInterval": cVpcStatsPeerKeepAliveAvgInterval,
       "cVpcStatsPeerStatusChangeCount": cVpcStatsPeerStatusChangeCount,
       "cVpcStatus": cVpcStatus,
       "cVpcStatusPeerLinkTable": cVpcStatusPeerLinkTable,
       "cVpcStatusPeerLinkEntry": cVpcStatusPeerLinkEntry,
       "cVpcStatusPeerLinkDomainID": cVpcStatusPeerLinkDomainID,
       "cVpcStatusPeerLinkIfIndex": cVpcStatusPeerLinkIfIndex,
       "cVpcStatusHostLinkTable": cVpcStatusHostLinkTable,
       "cVpcStatusHostLinkEntry": cVpcStatusHostLinkEntry,
       "cVpcStatusHostLinkDomainID": cVpcStatusHostLinkDomainID,
       "cVpcStatusHostLinkVpcID": cVpcStatusHostLinkVpcID,
       "cVpcStatusHostLinkIfIndex": cVpcStatusHostLinkIfIndex,
       "cVpcStatusHostLinkStatus": cVpcStatusHostLinkStatus,
       "cVpcStatusHostLinkConsistencyStatus": cVpcStatusHostLinkConsistencyStatus,
       "cVpcStatusHostLinkConsistencyDetail": cVpcStatusHostLinkConsistencyDetail,
       "ciscoVpcMIBConformance": ciscoVpcMIBConformance,
       "ciscoVpcMIBCompliances": ciscoVpcMIBCompliances,
       "ciscoVpcMIBCompliance": ciscoVpcMIBCompliance,
       "ciscoVpcMIBGroups": ciscoVpcMIBGroups,
       "cVpcPeerKeepAliveConfigInfoGroup": cVpcPeerKeepAliveConfigInfoGroup,
       "cVpcPeerKeepAliveStatusInfoGroup": cVpcPeerKeepAliveStatusInfoGroup,
       "cVpcMIBRoleGroup": cVpcMIBRoleGroup,
       "cVpcMIBStatisticsGroup": cVpcMIBStatisticsGroup,
       "cVpcMIBPeerLinkStatusGroup": cVpcMIBPeerLinkStatusGroup,
       "cVpcMIBHostLinkStatusGroup": cVpcMIBHostLinkStatusGroup}
)
