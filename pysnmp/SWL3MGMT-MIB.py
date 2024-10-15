# SNMP MIB module (SWL3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWL3MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:27 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(AreaID,
 Metric,
 TOSType) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "Metric",
    "TOSType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(privateMgmt,) = mibBuilder.importSymbols(
    "SWPRIMGMT-MIB",
    "privateMgmt")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3)
)


# Types definitions



class NodeAddress(OctetString):
    """Custom type NodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class NetAddress(OctetString):
    """Custom type NetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwL3DevMgmt_ObjectIdentity = ObjectIdentity
swL3DevMgmt = _SwL3DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1)
)
_SwL3DevCtrl_ObjectIdentity = ObjectIdentity
swL3DevCtrl = _SwL3DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1)
)


class _SwL3DevCtrlRIPState_Type(Integer32):
    """Custom type swL3DevCtrlRIPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlRIPState_Type.__name__ = "Integer32"
_SwL3DevCtrlRIPState_Object = MibScalar
swL3DevCtrlRIPState = _SwL3DevCtrlRIPState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 1),
    _SwL3DevCtrlRIPState_Type()
)
swL3DevCtrlRIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlRIPState.setStatus("current")


class _SwL3DevCtrlOSPFState_Type(Integer32):
    """Custom type swL3DevCtrlOSPFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlOSPFState_Type.__name__ = "Integer32"
_SwL3DevCtrlOSPFState_Object = MibScalar
swL3DevCtrlOSPFState = _SwL3DevCtrlOSPFState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 2),
    _SwL3DevCtrlOSPFState_Type()
)
swL3DevCtrlOSPFState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlOSPFState.setStatus("current")


class _SwL3DevCtrlDVMRPState_Type(Integer32):
    """Custom type swL3DevCtrlDVMRPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlDVMRPState_Type.__name__ = "Integer32"
_SwL3DevCtrlDVMRPState_Object = MibScalar
swL3DevCtrlDVMRPState = _SwL3DevCtrlDVMRPState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 3),
    _SwL3DevCtrlDVMRPState_Type()
)
swL3DevCtrlDVMRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlDVMRPState.setStatus("current")


class _SwL3DevCtrlVRRPState_Type(Integer32):
    """Custom type swL3DevCtrlVRRPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlVRRPState_Type.__name__ = "Integer32"
_SwL3DevCtrlVRRPState_Object = MibScalar
swL3DevCtrlVRRPState = _SwL3DevCtrlVRRPState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 4),
    _SwL3DevCtrlVRRPState_Type()
)
swL3DevCtrlVRRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlVRRPState.setStatus("current")


class _SwL3DevCtrlVRRPPingVirtualAddrState_Type(Integer32):
    """Custom type swL3DevCtrlVRRPPingVirtualAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlVRRPPingVirtualAddrState_Type.__name__ = "Integer32"
_SwL3DevCtrlVRRPPingVirtualAddrState_Object = MibScalar
swL3DevCtrlVRRPPingVirtualAddrState = _SwL3DevCtrlVRRPPingVirtualAddrState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 5),
    _SwL3DevCtrlVRRPPingVirtualAddrState_Type()
)
swL3DevCtrlVRRPPingVirtualAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlVRRPPingVirtualAddrState.setStatus("current")
_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3IpCtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3IpCtrlEntry.setStatus("current")


class _SwL3IpCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3IpCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwL3IpCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3IpCtrlInterfaceName_Object = MibTableColumn
swL3IpCtrlInterfaceName = _SwL3IpCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 1),
    _SwL3IpCtrlInterfaceName_Type()
)
swL3IpCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlInterfaceName.setStatus("current")


class _SwL3IpCtrlIfIndex_Type(Integer32):
    """Custom type swL3IpCtrlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpCtrlIfIndex_Type.__name__ = "Integer32"
_SwL3IpCtrlIfIndex_Object = MibTableColumn
swL3IpCtrlIfIndex = _SwL3IpCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 4),
    _SwL3IpCtrlIpSubnetMask_Type()
)
swL3IpCtrlIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpSubnetMask.setStatus("current")


class _SwL3IpCtrlVlanName_Type(DisplayString):
    """Custom type swL3IpCtrlVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL3IpCtrlVlanName_Type.__name__ = "DisplayString"
_SwL3IpCtrlVlanName_Object = MibTableColumn
swL3IpCtrlVlanName = _SwL3IpCtrlVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 5),
    _SwL3IpCtrlVlanName_Type()
)
swL3IpCtrlVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlVlanName.setStatus("current")


class _SwL3IpCtrlMode_Type(Integer32):
    """Custom type swL3IpCtrlMode based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 4),
          ("manual", 2),
          ("other", 1))
    )


_SwL3IpCtrlMode_Type.__name__ = "Integer32"
_SwL3IpCtrlMode_Object = MibTableColumn
swL3IpCtrlMode = _SwL3IpCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 6),
    _SwL3IpCtrlMode_Type()
)
swL3IpCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlMode.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 7),
    _SwL3IpCtrlState_Type()
)
swL3IpCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlState.setStatus("current")


class _SwL3IpCtrlOperState_Type(Integer32):
    """Custom type swL3IpCtrlOperState based on Integer32"""
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


_SwL3IpCtrlOperState_Type.__name__ = "Integer32"
_SwL3IpCtrlOperState_Object = MibTableColumn
swL3IpCtrlOperState = _SwL3IpCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 8),
    _SwL3IpCtrlOperState_Type()
)
swL3IpCtrlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlOperState.setStatus("current")
_SwL3IpFdbMgmt_ObjectIdentity = ObjectIdentity
swL3IpFdbMgmt = _SwL3IpFdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2)
)
_SwL3IpFdbInfoTable_Object = MibTable
swL3IpFdbInfoTable = _SwL3IpFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoTable.setStatus("current")
_SwL3IpFdbInfoEntry_Object = MibTableRow
swL3IpFdbInfoEntry = _SwL3IpFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1)
)
swL3IpFdbInfoEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3IpFdbInfoIpAddr"),
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoEntry.setStatus("current")
_SwL3IpFdbInfoIpAddr_Type = IpAddress
_SwL3IpFdbInfoIpAddr_Object = MibTableColumn
swL3IpFdbInfoIpAddr = _SwL3IpFdbInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 1),
    _SwL3IpFdbInfoIpAddr_Type()
)
swL3IpFdbInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpAddr.setStatus("current")
_SwL3IpFdbInfoIpSubnetMask_Type = IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object = MibTableColumn
swL3IpFdbInfoIpSubnetMask = _SwL3IpFdbInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 2),
    _SwL3IpFdbInfoIpSubnetMask_Type()
)
swL3IpFdbInfoIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpSubnetMask.setStatus("current")


class _SwL3IpFdbInfoPort_Type(Integer32):
    """Custom type swL3IpFdbInfoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpFdbInfoPort_Type.__name__ = "Integer32"
_SwL3IpFdbInfoPort_Object = MibTableColumn
swL3IpFdbInfoPort = _SwL3IpFdbInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 3),
    _SwL3IpFdbInfoPort_Type()
)
swL3IpFdbInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoPort.setStatus("current")


class _SwL3IpFdbInfoType_Type(Integer32):
    """Custom type swL3IpFdbInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("other", 1),
          ("static", 2))
    )


_SwL3IpFdbInfoType_Type.__name__ = "Integer32"
_SwL3IpFdbInfoType_Object = MibTableColumn
swL3IpFdbInfoType = _SwL3IpFdbInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 4),
    _SwL3IpFdbInfoType_Type()
)
swL3IpFdbInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoType.setStatus("current")
_SwL3IpFilterMgmt_ObjectIdentity = ObjectIdentity
swL3IpFilterMgmt = _SwL3IpFilterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3)
)
_SwL3IpFilterAddrConfig_ObjectIdentity = ObjectIdentity
swL3IpFilterAddrConfig = _SwL3IpFilterAddrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1)
)


class _SwL3IpFilterAddrMaxSupportedEntries_Type(Integer32):
    """Custom type swL3IpFilterAddrMaxSupportedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpFilterAddrMaxSupportedEntries_Type.__name__ = "Integer32"
_SwL3IpFilterAddrMaxSupportedEntries_Object = MibScalar
swL3IpFilterAddrMaxSupportedEntries = _SwL3IpFilterAddrMaxSupportedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 1),
    _SwL3IpFilterAddrMaxSupportedEntries_Type()
)
swL3IpFilterAddrMaxSupportedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFilterAddrMaxSupportedEntries.setStatus("current")


class _SwL3IpFilterAddrCurrentTotalEntries_Type(Integer32):
    """Custom type swL3IpFilterAddrCurrentTotalEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpFilterAddrCurrentTotalEntries_Type.__name__ = "Integer32"
_SwL3IpFilterAddrCurrentTotalEntries_Object = MibScalar
swL3IpFilterAddrCurrentTotalEntries = _SwL3IpFilterAddrCurrentTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 2),
    _SwL3IpFilterAddrCurrentTotalEntries_Type()
)
swL3IpFilterAddrCurrentTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFilterAddrCurrentTotalEntries.setStatus("current")
_SwL3IpFilterAddrCtrlTable_Object = MibTable
swL3IpFilterAddrCtrlTable = _SwL3IpFilterAddrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpFilterAddrCtrlTable.setStatus("current")
_SwL3IpFilterAddrCtrlEntry_Object = MibTableRow
swL3IpFilterAddrCtrlEntry = _SwL3IpFilterAddrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3, 1)
)
swL3IpFilterAddrCtrlEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3IpFilterAddrIpAddr"),
)
if mibBuilder.loadTexts:
    swL3IpFilterAddrCtrlEntry.setStatus("current")
_SwL3IpFilterAddrIpAddr_Type = IpAddress
_SwL3IpFilterAddrIpAddr_Object = MibTableColumn
swL3IpFilterAddrIpAddr = _SwL3IpFilterAddrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3, 1, 1),
    _SwL3IpFilterAddrIpAddr_Type()
)
swL3IpFilterAddrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFilterAddrIpAddr.setStatus("current")


class _SwL3IpFilterAddrCtrlState_Type(Integer32):
    """Custom type swL3IpFilterAddrCtrlState based on Integer32"""
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
        *(("dst-addr", 2),
          ("dst-src-addr", 4),
          ("invalid", 5),
          ("other", 1),
          ("src-addr", 3))
    )


_SwL3IpFilterAddrCtrlState_Type.__name__ = "Integer32"
_SwL3IpFilterAddrCtrlState_Object = MibTableColumn
swL3IpFilterAddrCtrlState = _SwL3IpFilterAddrCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3, 1, 2),
    _SwL3IpFilterAddrCtrlState_Type()
)
swL3IpFilterAddrCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpFilterAddrCtrlState.setStatus("current")


class _SwL3IpArpAgingTime_Type(Integer32):
    """Custom type swL3IpArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpArpAgingTime_Type.__name__ = "Integer32"
_SwL3IpArpAgingTime_Object = MibScalar
swL3IpArpAgingTime = _SwL3IpArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 4),
    _SwL3IpArpAgingTime_Type()
)
swL3IpArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpAgingTime.setStatus("current")
_SwL3IpStaticRouteTable_Object = MibTable
swL3IpStaticRouteTable = _SwL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTable.setStatus("current")
_SwL3IpStaticRouteEntry_Object = MibTableRow
swL3IpStaticRouteEntry = _SwL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1)
)
swL3IpStaticRouteEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "SWL3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "SWL3MGMT-MIB", "swL3IpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteEntry.setStatus("current")
_SwL3IpStaticRouteDest_Type = IpAddress
_SwL3IpStaticRouteDest_Object = MibTableColumn
swL3IpStaticRouteDest = _SwL3IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 1),
    _SwL3IpStaticRouteDest_Type()
)
swL3IpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteDest.setStatus("current")
_SwL3IpStaticRouteMask_Type = IpAddress
_SwL3IpStaticRouteMask_Object = MibTableColumn
swL3IpStaticRouteMask = _SwL3IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 2),
    _SwL3IpStaticRouteMask_Type()
)
swL3IpStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteMask.setStatus("current")
_SwL3IpStaticRouteNextHop_Type = IpAddress
_SwL3IpStaticRouteNextHop_Object = MibTableColumn
swL3IpStaticRouteNextHop = _SwL3IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 3),
    _SwL3IpStaticRouteNextHop_Type()
)
swL3IpStaticRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteNextHop.setStatus("current")


class _SwL3IpStaticRouteMetric_Type(Integer32):
    """Custom type swL3IpStaticRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3IpStaticRouteMetric_Type.__name__ = "Integer32"
_SwL3IpStaticRouteMetric_Object = MibTableColumn
swL3IpStaticRouteMetric = _SwL3IpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 4),
    _SwL3IpStaticRouteMetric_Type()
)
swL3IpStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteMetric.setStatus("current")


class _SwL3IpStaticRouteStatus_Type(Integer32):
    """Custom type swL3IpStaticRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3IpStaticRouteStatus_Type.__name__ = "Integer32"
_SwL3IpStaticRouteStatus_Object = MibTableColumn
swL3IpStaticRouteStatus = _SwL3IpStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 5),
    _SwL3IpStaticRouteStatus_Type()
)
swL3IpStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteStatus.setStatus("current")
_SwL3IpArpTable_Object = MibTable
swL3IpArpTable = _SwL3IpArpTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    swL3IpArpTable.setStatus("current")
_SwL3IpArpEntry_Object = MibTableRow
swL3IpArpEntry = _SwL3IpArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1)
)
swL3IpArpEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3IpArpIfIndex"),
    (0, "SWL3MGMT-MIB", "swL3IpArpNetAddress"),
)
if mibBuilder.loadTexts:
    swL3IpArpEntry.setStatus("current")
_SwL3IpArpIfIndex_Type = Integer32
_SwL3IpArpIfIndex_Object = MibTableColumn
swL3IpArpIfIndex = _SwL3IpArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 1),
    _SwL3IpArpIfIndex_Type()
)
swL3IpArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpArpIfIndex.setStatus("current")
_SwL3IpArpNetAddress_Type = IpAddress
_SwL3IpArpNetAddress_Object = MibTableColumn
swL3IpArpNetAddress = _SwL3IpArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 2),
    _SwL3IpArpNetAddress_Type()
)
swL3IpArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpArpNetAddress.setStatus("current")
_SwL3IpArpPhysAddress_Type = MacAddress
_SwL3IpArpPhysAddress_Object = MibTableColumn
swL3IpArpPhysAddress = _SwL3IpArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 3),
    _SwL3IpArpPhysAddress_Type()
)
swL3IpArpPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpArpPhysAddress.setStatus("current")


class _SwL3IpArpType_Type(Integer32):
    """Custom type swL3IpArpType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("local", 5),
          ("local-broadcast", 6),
          ("other", 1),
          ("static", 4))
    )


_SwL3IpArpType_Type.__name__ = "Integer32"
_SwL3IpArpType_Object = MibTableColumn
swL3IpArpType = _SwL3IpArpType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 4),
    _SwL3IpArpType_Type()
)
swL3IpArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpArpType.setStatus("current")


class _SwL3IpArpDynamicAgingTime_Type(Integer32):
    """Custom type swL3IpArpDynamicAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpArpDynamicAgingTime_Type.__name__ = "Integer32"
_SwL3IpArpDynamicAgingTime_Object = MibTableColumn
swL3IpArpDynamicAgingTime = _SwL3IpArpDynamicAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 5),
    _SwL3IpArpDynamicAgingTime_Type()
)
swL3IpArpDynamicAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpArpDynamicAgingTime.setStatus("current")


class _SwL3IpArpReqRateLimitState_Type(Integer32):
    """Custom type swL3IpArpReqRateLimitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3IpArpReqRateLimitState_Type.__name__ = "Integer32"
_SwL3IpArpReqRateLimitState_Object = MibScalar
swL3IpArpReqRateLimitState = _SwL3IpArpReqRateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 7),
    _SwL3IpArpReqRateLimitState_Type()
)
swL3IpArpReqRateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpReqRateLimitState.setStatus("current")


class _SwL3IpArpReqRateLimitValue_Type(Integer32):
    """Custom type swL3IpArpReqRateLimitValue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SwL3IpArpReqRateLimitValue_Type.__name__ = "Integer32"
_SwL3IpArpReqRateLimitValue_Object = MibScalar
swL3IpArpReqRateLimitValue = _SwL3IpArpReqRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 8),
    _SwL3IpArpReqRateLimitValue_Type()
)
swL3IpArpReqRateLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpReqRateLimitValue.setStatus("current")
_SwL3RelayMgmt_ObjectIdentity = ObjectIdentity
swL3RelayMgmt = _SwL3RelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3)
)
_SwL3RelayBootpMgmt_ObjectIdentity = ObjectIdentity
swL3RelayBootpMgmt = _SwL3RelayBootpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1)
)


class _SwL3RelayBootpState_Type(Integer32):
    """Custom type swL3RelayBootpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayBootpState_Type.__name__ = "Integer32"
_SwL3RelayBootpState_Object = MibScalar
swL3RelayBootpState = _SwL3RelayBootpState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 1),
    _SwL3RelayBootpState_Type()
)
swL3RelayBootpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayBootpState.setStatus("current")


class _SwL3RelayBootpHopCount_Type(Integer32):
    """Custom type swL3RelayBootpHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3RelayBootpHopCount_Type.__name__ = "Integer32"
_SwL3RelayBootpHopCount_Object = MibScalar
swL3RelayBootpHopCount = _SwL3RelayBootpHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 2),
    _SwL3RelayBootpHopCount_Type()
)
swL3RelayBootpHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayBootpHopCount.setStatus("current")


class _SwL3RelayBootpTimeThreshold_Type(Integer32):
    """Custom type swL3RelayBootpTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3RelayBootpTimeThreshold_Type.__name__ = "Integer32"
_SwL3RelayBootpTimeThreshold_Object = MibScalar
swL3RelayBootpTimeThreshold = _SwL3RelayBootpTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 3),
    _SwL3RelayBootpTimeThreshold_Type()
)
swL3RelayBootpTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayBootpTimeThreshold.setStatus("current")
_SwL3RelayBootpCtrlTable_Object = MibTable
swL3RelayBootpCtrlTable = _SwL3RelayBootpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    swL3RelayBootpCtrlTable.setStatus("current")
_SwL3RelayBootpCtrlEntry_Object = MibTableRow
swL3RelayBootpCtrlEntry = _SwL3RelayBootpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1)
)
swL3RelayBootpCtrlEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3RelayBootpCtrlInterfaceName"),
    (0, "SWL3MGMT-MIB", "swL3RelayBootpCtrlServer"),
)
if mibBuilder.loadTexts:
    swL3RelayBootpCtrlEntry.setStatus("current")


class _SwL3RelayBootpCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3RelayBootpCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwL3RelayBootpCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3RelayBootpCtrlInterfaceName_Object = MibTableColumn
swL3RelayBootpCtrlInterfaceName = _SwL3RelayBootpCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1, 1),
    _SwL3RelayBootpCtrlInterfaceName_Type()
)
swL3RelayBootpCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayBootpCtrlInterfaceName.setStatus("current")
_SwL3RelayBootpCtrlServer_Type = IpAddress
_SwL3RelayBootpCtrlServer_Object = MibTableColumn
swL3RelayBootpCtrlServer = _SwL3RelayBootpCtrlServer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1, 2),
    _SwL3RelayBootpCtrlServer_Type()
)
swL3RelayBootpCtrlServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayBootpCtrlServer.setStatus("current")


class _SwL3RelayBootpCtrlState_Type(Integer32):
    """Custom type swL3RelayBootpCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3RelayBootpCtrlState_Type.__name__ = "Integer32"
_SwL3RelayBootpCtrlState_Object = MibTableColumn
swL3RelayBootpCtrlState = _SwL3RelayBootpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1, 3),
    _SwL3RelayBootpCtrlState_Type()
)
swL3RelayBootpCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayBootpCtrlState.setStatus("current")
_SwL3RelayDnsMgmt_ObjectIdentity = ObjectIdentity
swL3RelayDnsMgmt = _SwL3RelayDnsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2)
)


class _SwL3RelayDnsState_Type(Integer32):
    """Custom type swL3RelayDnsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayDnsState_Type.__name__ = "Integer32"
_SwL3RelayDnsState_Object = MibScalar
swL3RelayDnsState = _SwL3RelayDnsState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 1),
    _SwL3RelayDnsState_Type()
)
swL3RelayDnsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsState.setStatus("current")
_SwL3RelayDnsPrimaryServer_Type = IpAddress
_SwL3RelayDnsPrimaryServer_Object = MibScalar
swL3RelayDnsPrimaryServer = _SwL3RelayDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 2),
    _SwL3RelayDnsPrimaryServer_Type()
)
swL3RelayDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsPrimaryServer.setStatus("current")
_SwL3RelayDnsSecondaryServer_Type = IpAddress
_SwL3RelayDnsSecondaryServer_Object = MibScalar
swL3RelayDnsSecondaryServer = _SwL3RelayDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 3),
    _SwL3RelayDnsSecondaryServer_Type()
)
swL3RelayDnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsSecondaryServer.setStatus("current")


class _SwL3RelayDnsCacheState_Type(Integer32):
    """Custom type swL3RelayDnsCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayDnsCacheState_Type.__name__ = "Integer32"
_SwL3RelayDnsCacheState_Object = MibScalar
swL3RelayDnsCacheState = _SwL3RelayDnsCacheState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 4),
    _SwL3RelayDnsCacheState_Type()
)
swL3RelayDnsCacheState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCacheState.setStatus("current")


class _SwL3RelayDnsStaticTableState_Type(Integer32):
    """Custom type swL3RelayDnsStaticTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayDnsStaticTableState_Type.__name__ = "Integer32"
_SwL3RelayDnsStaticTableState_Object = MibScalar
swL3RelayDnsStaticTableState = _SwL3RelayDnsStaticTableState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 5),
    _SwL3RelayDnsStaticTableState_Type()
)
swL3RelayDnsStaticTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsStaticTableState.setStatus("current")
_SwL3RelayDnsCtrlTable_Object = MibTable
swL3RelayDnsCtrlTable = _SwL3RelayDnsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlTable.setStatus("current")
_SwL3RelayDnsCtrlEntry_Object = MibTableRow
swL3RelayDnsCtrlEntry = _SwL3RelayDnsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1)
)
swL3RelayDnsCtrlEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3RelayDnsCtrlDomainName"),
    (0, "SWL3MGMT-MIB", "swL3RelayDnsCtrlIpAddr"),
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlEntry.setStatus("current")


class _SwL3RelayDnsCtrlDomainName_Type(DisplayString):
    """Custom type swL3RelayDnsCtrlDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwL3RelayDnsCtrlDomainName_Type.__name__ = "DisplayString"
_SwL3RelayDnsCtrlDomainName_Object = MibTableColumn
swL3RelayDnsCtrlDomainName = _SwL3RelayDnsCtrlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1, 1),
    _SwL3RelayDnsCtrlDomainName_Type()
)
swL3RelayDnsCtrlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlDomainName.setStatus("current")
_SwL3RelayDnsCtrlIpAddr_Type = IpAddress
_SwL3RelayDnsCtrlIpAddr_Object = MibTableColumn
swL3RelayDnsCtrlIpAddr = _SwL3RelayDnsCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1, 2),
    _SwL3RelayDnsCtrlIpAddr_Type()
)
swL3RelayDnsCtrlIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlIpAddr.setStatus("current")


class _SwL3RelayDnsCtrlState_Type(Integer32):
    """Custom type swL3RelayDnsCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3RelayDnsCtrlState_Type.__name__ = "Integer32"
_SwL3RelayDnsCtrlState_Object = MibTableColumn
swL3RelayDnsCtrlState = _SwL3RelayDnsCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1, 3),
    _SwL3RelayDnsCtrlState_Type()
)
swL3RelayDnsCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlState.setStatus("current")
_SwL3Md5Table_Object = MibTable
swL3Md5Table = _SwL3Md5Table_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4)
)
if mibBuilder.loadTexts:
    swL3Md5Table.setStatus("current")
_SwL3Md5Entry_Object = MibTableRow
swL3Md5Entry = _SwL3Md5Entry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1)
)
swL3Md5Entry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3Md5KeyId"),
)
if mibBuilder.loadTexts:
    swL3Md5Entry.setStatus("current")


class _SwL3Md5KeyId_Type(Integer32):
    """Custom type swL3Md5KeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL3Md5KeyId_Type.__name__ = "Integer32"
_SwL3Md5KeyId_Object = MibTableColumn
swL3Md5KeyId = _SwL3Md5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1, 1),
    _SwL3Md5KeyId_Type()
)
swL3Md5KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Md5KeyId.setStatus("current")


class _SwL3Md5Key_Type(DisplayString):
    """Custom type swL3Md5Key based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwL3Md5Key_Type.__name__ = "DisplayString"
_SwL3Md5Key_Object = MibTableColumn
swL3Md5Key = _SwL3Md5Key_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1, 2),
    _SwL3Md5Key_Type()
)
swL3Md5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Md5Key.setStatus("current")


class _SwL3Md5State_Type(Integer32):
    """Custom type swL3Md5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3Md5State_Type.__name__ = "Integer32"
_SwL3Md5State_Object = MibTableColumn
swL3Md5State = _SwL3Md5State_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1, 3),
    _SwL3Md5State_Type()
)
swL3Md5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Md5State.setStatus("current")
_SwL3RouteRedistriTable_Object = MibTable
swL3RouteRedistriTable = _SwL3RouteRedistriTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5)
)
if mibBuilder.loadTexts:
    swL3RouteRedistriTable.setStatus("current")
_SwL3RouteRedistriEntry_Object = MibTableRow
swL3RouteRedistriEntry = _SwL3RouteRedistriEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1)
)
swL3RouteRedistriEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3RouteRedistriSrcProtocol"),
    (0, "SWL3MGMT-MIB", "swL3RouteRedistriDstProtocol"),
)
if mibBuilder.loadTexts:
    swL3RouteRedistriEntry.setStatus("current")


class _SwL3RouteRedistriSrcProtocol_Type(Integer32):
    """Custom type swL3RouteRedistriSrcProtocol based on Integer32"""
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
        *(("local", 5),
          ("ospf", 3),
          ("other", 1),
          ("rip", 2),
          ("static", 4))
    )


_SwL3RouteRedistriSrcProtocol_Type.__name__ = "Integer32"
_SwL3RouteRedistriSrcProtocol_Object = MibTableColumn
swL3RouteRedistriSrcProtocol = _SwL3RouteRedistriSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 1),
    _SwL3RouteRedistriSrcProtocol_Type()
)
swL3RouteRedistriSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RouteRedistriSrcProtocol.setStatus("current")


class _SwL3RouteRedistriDstProtocol_Type(Integer32):
    """Custom type swL3RouteRedistriDstProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospf", 3),
          ("other", 1),
          ("rip", 2))
    )


_SwL3RouteRedistriDstProtocol_Type.__name__ = "Integer32"
_SwL3RouteRedistriDstProtocol_Object = MibTableColumn
swL3RouteRedistriDstProtocol = _SwL3RouteRedistriDstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 2),
    _SwL3RouteRedistriDstProtocol_Type()
)
swL3RouteRedistriDstProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RouteRedistriDstProtocol.setStatus("current")


class _SwL3RouteRedistriType_Type(Integer32):
    """Custom type swL3RouteRedistriType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("extType1", 9),
          ("extType2", 10),
          ("external", 6),
          ("inter-E1", 7),
          ("inter-E2", 8),
          ("internal", 5),
          ("other", 1),
          ("type-1", 3),
          ("type-2", 4))
    )


_SwL3RouteRedistriType_Type.__name__ = "Integer32"
_SwL3RouteRedistriType_Object = MibTableColumn
swL3RouteRedistriType = _SwL3RouteRedistriType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 3),
    _SwL3RouteRedistriType_Type()
)
swL3RouteRedistriType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RouteRedistriType.setStatus("current")


class _SwL3RouteRedistriMetric_Type(Integer32):
    """Custom type swL3RouteRedistriMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_SwL3RouteRedistriMetric_Type.__name__ = "Integer32"
_SwL3RouteRedistriMetric_Object = MibTableColumn
swL3RouteRedistriMetric = _SwL3RouteRedistriMetric_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 4),
    _SwL3RouteRedistriMetric_Type()
)
swL3RouteRedistriMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RouteRedistriMetric.setStatus("current")


class _SwL3RouteRedistriState_Type(Integer32):
    """Custom type swL3RouteRedistriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3RouteRedistriState_Type.__name__ = "Integer32"
_SwL3RouteRedistriState_Object = MibTableColumn
swL3RouteRedistriState = _SwL3RouteRedistriState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 5),
    _SwL3RouteRedistriState_Type()
)
swL3RouteRedistriState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RouteRedistriState.setStatus("current")
_SwL3OspfHostTable_Object = MibTable
swL3OspfHostTable = _SwL3OspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6)
)
if mibBuilder.loadTexts:
    swL3OspfHostTable.setStatus("current")
_SwL3OspfHostEntry_Object = MibTableRow
swL3OspfHostEntry = _SwL3OspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1)
)
swL3OspfHostEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3OspfHostIpAddress"),
    (0, "SWL3MGMT-MIB", "swL3OspfHostTOS"),
)
if mibBuilder.loadTexts:
    swL3OspfHostEntry.setStatus("current")
_SwL3OspfHostIpAddress_Type = IpAddress
_SwL3OspfHostIpAddress_Object = MibTableColumn
swL3OspfHostIpAddress = _SwL3OspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 1),
    _SwL3OspfHostIpAddress_Type()
)
swL3OspfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfHostIpAddress.setStatus("current")
_SwL3OspfHostTOS_Type = TOSType
_SwL3OspfHostTOS_Object = MibTableColumn
swL3OspfHostTOS = _SwL3OspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 2),
    _SwL3OspfHostTOS_Type()
)
swL3OspfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfHostTOS.setStatus("current")
_SwL3OspfHostMetric_Type = Metric
_SwL3OspfHostMetric_Object = MibTableColumn
swL3OspfHostMetric = _SwL3OspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 3),
    _SwL3OspfHostMetric_Type()
)
swL3OspfHostMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfHostMetric.setStatus("current")
_SwL3OspfHostStatus_Type = RowStatus
_SwL3OspfHostStatus_Object = MibTableColumn
swL3OspfHostStatus = _SwL3OspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 4),
    _SwL3OspfHostStatus_Type()
)
swL3OspfHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfHostStatus.setStatus("current")
_SwL3OspfHostAreaID_Type = AreaID
_SwL3OspfHostAreaID_Object = MibTableColumn
swL3OspfHostAreaID = _SwL3OspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 5),
    _SwL3OspfHostAreaID_Type()
)
swL3OspfHostAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfHostAreaID.setStatus("current")
_SwL3VrrpMgmt_ObjectIdentity = ObjectIdentity
swL3VrrpMgmt = _SwL3VrrpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7)
)
_SwL3VrrpOperTable_Object = MibTable
swL3VrrpOperTable = _SwL3VrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    swL3VrrpOperTable.setStatus("current")
_SwL3VrrpOperEntry_Object = MibTableRow
swL3VrrpOperEntry = _SwL3VrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1)
)
swL3VrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SWL3MGMT-MIB", "swL3VrrpOperVrId"),
)
if mibBuilder.loadTexts:
    swL3VrrpOperEntry.setStatus("current")


class _SwL3VrrpOperVrId_Type(Integer32):
    """Custom type swL3VrrpOperVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL3VrrpOperVrId_Type.__name__ = "Integer32"
_SwL3VrrpOperVrId_Object = MibTableColumn
swL3VrrpOperVrId = _SwL3VrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 1),
    _SwL3VrrpOperVrId_Type()
)
swL3VrrpOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL3VrrpOperVrId.setStatus("current")
_SwL3VrrpOperCriticalIpAddr_Type = IpAddress
_SwL3VrrpOperCriticalIpAddr_Object = MibTableColumn
swL3VrrpOperCriticalIpAddr = _SwL3VrrpOperCriticalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 2),
    _SwL3VrrpOperCriticalIpAddr_Type()
)
swL3VrrpOperCriticalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3VrrpOperCriticalIpAddr.setStatus("current")


class _SwL3VrrpOperCriticalIpState_Type(Integer32):
    """Custom type swL3VrrpOperCriticalIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3VrrpOperCriticalIpState_Type.__name__ = "Integer32"
_SwL3VrrpOperCriticalIpState_Object = MibTableColumn
swL3VrrpOperCriticalIpState = _SwL3VrrpOperCriticalIpState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 3),
    _SwL3VrrpOperCriticalIpState_Type()
)
swL3VrrpOperCriticalIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3VrrpOperCriticalIpState.setStatus("current")


class _SwL3VrrpOperHoldDownTimer_Type(Integer32):
    """Custom type swL3VrrpOperHoldDownTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21600),
    )


_SwL3VrrpOperHoldDownTimer_Type.__name__ = "Integer32"
_SwL3VrrpOperHoldDownTimer_Object = MibTableColumn
swL3VrrpOperHoldDownTimer = _SwL3VrrpOperHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 4),
    _SwL3VrrpOperHoldDownTimer_Type()
)
swL3VrrpOperHoldDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3VrrpOperHoldDownTimer.setStatus("current")
_SwL3RoutePrefTable_Object = MibTable
swL3RoutePrefTable = _SwL3RoutePrefTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8)
)
if mibBuilder.loadTexts:
    swL3RoutePrefTable.setStatus("current")
_SwL3RoutePrefEntry_Object = MibTableRow
swL3RoutePrefEntry = _SwL3RoutePrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8, 1)
)
swL3RoutePrefEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3RoutePrefProtocol"),
)
if mibBuilder.loadTexts:
    swL3RoutePrefEntry.setStatus("current")


class _SwL3RoutePrefProtocol_Type(Integer32):
    """Custom type swL3RoutePrefProtocol based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 6),
          ("isis", 1),
          ("local", 5),
          ("ospfExternal", 9),
          ("ospfExternal1", 10),
          ("ospfExternal2", 11),
          ("ospfInter", 8),
          ("ospfIntra", 3),
          ("ospfNssa1", 12),
          ("ospfNssa2", 13),
          ("rip", 2),
          ("static", 4),
          ("staticLow", 7))
    )


_SwL3RoutePrefProtocol_Type.__name__ = "Integer32"
_SwL3RoutePrefProtocol_Object = MibTableColumn
swL3RoutePrefProtocol = _SwL3RoutePrefProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8, 1, 1),
    _SwL3RoutePrefProtocol_Type()
)
swL3RoutePrefProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RoutePrefProtocol.setStatus("current")


class _SwL3RoutePrefValue_Type(Integer32):
    """Custom type swL3RoutePrefValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_SwL3RoutePrefValue_Type.__name__ = "Integer32"
_SwL3RoutePrefValue_Object = MibTableColumn
swL3RoutePrefValue = _SwL3RoutePrefValue_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8, 1, 2),
    _SwL3RoutePrefValue_Type()
)
swL3RoutePrefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePrefValue.setStatus("current")
_SwL3DvmrpInterfaceTable_Object = MibTable
swL3DvmrpInterfaceTable = _SwL3DvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9)
)
if mibBuilder.loadTexts:
    swL3DvmrpInterfaceTable.setStatus("current")
_SwL3DvmrpInterfaceEntry_Object = MibTableRow
swL3DvmrpInterfaceEntry = _SwL3DvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1)
)
swL3DvmrpInterfaceEntry.setIndexNames(
    (0, "SWL3MGMT-MIB", "swL3DvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    swL3DvmrpInterfaceEntry.setStatus("current")


class _SwL3DvmrpInterfaceIfIndex_Type(Integer32):
    """Custom type swL3DvmrpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3DvmrpInterfaceIfIndex_Type.__name__ = "Integer32"
_SwL3DvmrpInterfaceIfIndex_Object = MibTableColumn
swL3DvmrpInterfaceIfIndex = _SwL3DvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1, 1),
    _SwL3DvmrpInterfaceIfIndex_Type()
)
swL3DvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL3DvmrpInterfaceIfIndex.setStatus("current")


class _SwL3DvmrpInterfaceNeighborTimeout_Type(Integer32):
    """Custom type swL3DvmrpInterfaceNeighborTimeout based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3DvmrpInterfaceNeighborTimeout_Type.__name__ = "Integer32"
_SwL3DvmrpInterfaceNeighborTimeout_Object = MibTableColumn
swL3DvmrpInterfaceNeighborTimeout = _SwL3DvmrpInterfaceNeighborTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1, 2),
    _SwL3DvmrpInterfaceNeighborTimeout_Type()
)
swL3DvmrpInterfaceNeighborTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DvmrpInterfaceNeighborTimeout.setStatus("current")


class _SwL3DvmrpInterfaceProbe_Type(Integer32):
    """Custom type swL3DvmrpInterfaceProbe based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3DvmrpInterfaceProbe_Type.__name__ = "Integer32"
_SwL3DvmrpInterfaceProbe_Object = MibTableColumn
swL3DvmrpInterfaceProbe = _SwL3DvmrpInterfaceProbe_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1, 3),
    _SwL3DvmrpInterfaceProbe_Type()
)
swL3DvmrpInterfaceProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DvmrpInterfaceProbe.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWL3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
       "swL3MgmtMIB": swL3MgmtMIB,
       "swL3DevMgmt": swL3DevMgmt,
       "swL3DevCtrl": swL3DevCtrl,
       "swL3DevCtrlRIPState": swL3DevCtrlRIPState,
       "swL3DevCtrlOSPFState": swL3DevCtrlOSPFState,
       "swL3DevCtrlDVMRPState": swL3DevCtrlDVMRPState,
       "swL3DevCtrlVRRPState": swL3DevCtrlVRRPState,
       "swL3DevCtrlVRRPPingVirtualAddrState": swL3DevCtrlVRRPPingVirtualAddrState,
       "swL3IpMgmt": swL3IpMgmt,
       "swL3IpCtrlMgmt": swL3IpCtrlMgmt,
       "swL3IpCtrlTable": swL3IpCtrlTable,
       "swL3IpCtrlEntry": swL3IpCtrlEntry,
       "swL3IpCtrlInterfaceName": swL3IpCtrlInterfaceName,
       "swL3IpCtrlIfIndex": swL3IpCtrlIfIndex,
       "swL3IpCtrlIpAddr": swL3IpCtrlIpAddr,
       "swL3IpCtrlIpSubnetMask": swL3IpCtrlIpSubnetMask,
       "swL3IpCtrlVlanName": swL3IpCtrlVlanName,
       "swL3IpCtrlMode": swL3IpCtrlMode,
       "swL3IpCtrlState": swL3IpCtrlState,
       "swL3IpCtrlOperState": swL3IpCtrlOperState,
       "swL3IpFdbMgmt": swL3IpFdbMgmt,
       "swL3IpFdbInfoTable": swL3IpFdbInfoTable,
       "swL3IpFdbInfoEntry": swL3IpFdbInfoEntry,
       "swL3IpFdbInfoIpAddr": swL3IpFdbInfoIpAddr,
       "swL3IpFdbInfoIpSubnetMask": swL3IpFdbInfoIpSubnetMask,
       "swL3IpFdbInfoPort": swL3IpFdbInfoPort,
       "swL3IpFdbInfoType": swL3IpFdbInfoType,
       "swL3IpFilterMgmt": swL3IpFilterMgmt,
       "swL3IpFilterAddrConfig": swL3IpFilterAddrConfig,
       "swL3IpFilterAddrMaxSupportedEntries": swL3IpFilterAddrMaxSupportedEntries,
       "swL3IpFilterAddrCurrentTotalEntries": swL3IpFilterAddrCurrentTotalEntries,
       "swL3IpFilterAddrCtrlTable": swL3IpFilterAddrCtrlTable,
       "swL3IpFilterAddrCtrlEntry": swL3IpFilterAddrCtrlEntry,
       "swL3IpFilterAddrIpAddr": swL3IpFilterAddrIpAddr,
       "swL3IpFilterAddrCtrlState": swL3IpFilterAddrCtrlState,
       "swL3IpArpAgingTime": swL3IpArpAgingTime,
       "swL3IpStaticRouteTable": swL3IpStaticRouteTable,
       "swL3IpStaticRouteEntry": swL3IpStaticRouteEntry,
       "swL3IpStaticRouteDest": swL3IpStaticRouteDest,
       "swL3IpStaticRouteMask": swL3IpStaticRouteMask,
       "swL3IpStaticRouteNextHop": swL3IpStaticRouteNextHop,
       "swL3IpStaticRouteMetric": swL3IpStaticRouteMetric,
       "swL3IpStaticRouteStatus": swL3IpStaticRouteStatus,
       "swL3IpArpTable": swL3IpArpTable,
       "swL3IpArpEntry": swL3IpArpEntry,
       "swL3IpArpIfIndex": swL3IpArpIfIndex,
       "swL3IpArpNetAddress": swL3IpArpNetAddress,
       "swL3IpArpPhysAddress": swL3IpArpPhysAddress,
       "swL3IpArpType": swL3IpArpType,
       "swL3IpArpDynamicAgingTime": swL3IpArpDynamicAgingTime,
       "swL3IpArpReqRateLimitState": swL3IpArpReqRateLimitState,
       "swL3IpArpReqRateLimitValue": swL3IpArpReqRateLimitValue,
       "swL3RelayMgmt": swL3RelayMgmt,
       "swL3RelayBootpMgmt": swL3RelayBootpMgmt,
       "swL3RelayBootpState": swL3RelayBootpState,
       "swL3RelayBootpHopCount": swL3RelayBootpHopCount,
       "swL3RelayBootpTimeThreshold": swL3RelayBootpTimeThreshold,
       "swL3RelayBootpCtrlTable": swL3RelayBootpCtrlTable,
       "swL3RelayBootpCtrlEntry": swL3RelayBootpCtrlEntry,
       "swL3RelayBootpCtrlInterfaceName": swL3RelayBootpCtrlInterfaceName,
       "swL3RelayBootpCtrlServer": swL3RelayBootpCtrlServer,
       "swL3RelayBootpCtrlState": swL3RelayBootpCtrlState,
       "swL3RelayDnsMgmt": swL3RelayDnsMgmt,
       "swL3RelayDnsState": swL3RelayDnsState,
       "swL3RelayDnsPrimaryServer": swL3RelayDnsPrimaryServer,
       "swL3RelayDnsSecondaryServer": swL3RelayDnsSecondaryServer,
       "swL3RelayDnsCacheState": swL3RelayDnsCacheState,
       "swL3RelayDnsStaticTableState": swL3RelayDnsStaticTableState,
       "swL3RelayDnsCtrlTable": swL3RelayDnsCtrlTable,
       "swL3RelayDnsCtrlEntry": swL3RelayDnsCtrlEntry,
       "swL3RelayDnsCtrlDomainName": swL3RelayDnsCtrlDomainName,
       "swL3RelayDnsCtrlIpAddr": swL3RelayDnsCtrlIpAddr,
       "swL3RelayDnsCtrlState": swL3RelayDnsCtrlState,
       "swL3Md5Table": swL3Md5Table,
       "swL3Md5Entry": swL3Md5Entry,
       "swL3Md5KeyId": swL3Md5KeyId,
       "swL3Md5Key": swL3Md5Key,
       "swL3Md5State": swL3Md5State,
       "swL3RouteRedistriTable": swL3RouteRedistriTable,
       "swL3RouteRedistriEntry": swL3RouteRedistriEntry,
       "swL3RouteRedistriSrcProtocol": swL3RouteRedistriSrcProtocol,
       "swL3RouteRedistriDstProtocol": swL3RouteRedistriDstProtocol,
       "swL3RouteRedistriType": swL3RouteRedistriType,
       "swL3RouteRedistriMetric": swL3RouteRedistriMetric,
       "swL3RouteRedistriState": swL3RouteRedistriState,
       "swL3OspfHostTable": swL3OspfHostTable,
       "swL3OspfHostEntry": swL3OspfHostEntry,
       "swL3OspfHostIpAddress": swL3OspfHostIpAddress,
       "swL3OspfHostTOS": swL3OspfHostTOS,
       "swL3OspfHostMetric": swL3OspfHostMetric,
       "swL3OspfHostStatus": swL3OspfHostStatus,
       "swL3OspfHostAreaID": swL3OspfHostAreaID,
       "swL3VrrpMgmt": swL3VrrpMgmt,
       "swL3VrrpOperTable": swL3VrrpOperTable,
       "swL3VrrpOperEntry": swL3VrrpOperEntry,
       "swL3VrrpOperVrId": swL3VrrpOperVrId,
       "swL3VrrpOperCriticalIpAddr": swL3VrrpOperCriticalIpAddr,
       "swL3VrrpOperCriticalIpState": swL3VrrpOperCriticalIpState,
       "swL3VrrpOperHoldDownTimer": swL3VrrpOperHoldDownTimer,
       "swL3RoutePrefTable": swL3RoutePrefTable,
       "swL3RoutePrefEntry": swL3RoutePrefEntry,
       "swL3RoutePrefProtocol": swL3RoutePrefProtocol,
       "swL3RoutePrefValue": swL3RoutePrefValue,
       "swL3DvmrpInterfaceTable": swL3DvmrpInterfaceTable,
       "swL3DvmrpInterfaceEntry": swL3DvmrpInterfaceEntry,
       "swL3DvmrpInterfaceIfIndex": swL3DvmrpInterfaceIfIndex,
       "swL3DvmrpInterfaceNeighborTimeout": swL3DvmrpInterfaceNeighborTimeout,
       "swL3DvmrpInterfaceProbe": swL3DvmrpInterfaceProbe}
)
