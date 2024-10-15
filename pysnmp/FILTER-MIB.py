# SNMP MIB module (FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:55 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwFilterDhcp_ObjectIdentity = ObjectIdentity
swFilterDhcp = _SwFilterDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1)
)
_SwFilterDhcpPermitTable_Object = MibTable
swFilterDhcpPermitTable = _SwFilterDhcpPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1)
)
if mibBuilder.loadTexts:
    swFilterDhcpPermitTable.setStatus("current")
_SwFilterDhcpPermitEntry_Object = MibTableRow
swFilterDhcpPermitEntry = _SwFilterDhcpPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1)
)
swFilterDhcpPermitEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterDhcpServerIP"),
    (0, "FILTER-MIB", "swFilterDhcpClientMac"),
)
if mibBuilder.loadTexts:
    swFilterDhcpPermitEntry.setStatus("current")
_SwFilterDhcpServerIP_Type = IpAddress
_SwFilterDhcpServerIP_Object = MibTableColumn
swFilterDhcpServerIP = _SwFilterDhcpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 1),
    _SwFilterDhcpServerIP_Type()
)
swFilterDhcpServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterDhcpServerIP.setStatus("current")
_SwFilterDhcpClientMac_Type = MacAddress
_SwFilterDhcpClientMac_Object = MibTableColumn
swFilterDhcpClientMac = _SwFilterDhcpClientMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 2),
    _SwFilterDhcpClientMac_Type()
)
swFilterDhcpClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterDhcpClientMac.setStatus("current")
_SwFilterDhcpPorts_Type = PortList
_SwFilterDhcpPorts_Object = MibTableColumn
swFilterDhcpPorts = _SwFilterDhcpPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 3),
    _SwFilterDhcpPorts_Type()
)
swFilterDhcpPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swFilterDhcpPorts.setStatus("current")
_SwFilterDhcpStatus_Type = RowStatus
_SwFilterDhcpStatus_Object = MibTableColumn
swFilterDhcpStatus = _SwFilterDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 4),
    _SwFilterDhcpStatus_Type()
)
swFilterDhcpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swFilterDhcpStatus.setStatus("current")
_SwFilterDhcpPortTable_Object = MibTable
swFilterDhcpPortTable = _SwFilterDhcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2)
)
if mibBuilder.loadTexts:
    swFilterDhcpPortTable.setStatus("current")
_SwFilterDhcpPortEntry_Object = MibTableRow
swFilterDhcpPortEntry = _SwFilterDhcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2, 1)
)
swFilterDhcpPortEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterDhcpPortIndex"),
)
if mibBuilder.loadTexts:
    swFilterDhcpPortEntry.setStatus("current")


class _SwFilterDhcpPortIndex_Type(Integer32):
    """Custom type swFilterDhcpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwFilterDhcpPortIndex_Type.__name__ = "Integer32"
_SwFilterDhcpPortIndex_Object = MibTableColumn
swFilterDhcpPortIndex = _SwFilterDhcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2, 1, 1),
    _SwFilterDhcpPortIndex_Type()
)
swFilterDhcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterDhcpPortIndex.setStatus("current")


class _SwFilterDhcpPortState_Type(Integer32):
    """Custom type swFilterDhcpPortState based on Integer32"""
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


_SwFilterDhcpPortState_Type.__name__ = "Integer32"
_SwFilterDhcpPortState_Object = MibTableColumn
swFilterDhcpPortState = _SwFilterDhcpPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2, 1, 2),
    _SwFilterDhcpPortState_Type()
)
swFilterDhcpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpPortState.setStatus("current")


class _SwFilterDhcpServerIllegalSerLogSuppressDuration_Type(Integer32):
    """Custom type swFilterDhcpServerIllegalSerLogSuppressDuration based on Integer32"""
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
        *(("duration_1min", 1),
          ("duration_30min", 3),
          ("duration_5min", 2))
    )


_SwFilterDhcpServerIllegalSerLogSuppressDuration_Type.__name__ = "Integer32"
_SwFilterDhcpServerIllegalSerLogSuppressDuration_Object = MibScalar
swFilterDhcpServerIllegalSerLogSuppressDuration = _SwFilterDhcpServerIllegalSerLogSuppressDuration_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 3),
    _SwFilterDhcpServerIllegalSerLogSuppressDuration_Type()
)
swFilterDhcpServerIllegalSerLogSuppressDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpServerIllegalSerLogSuppressDuration.setStatus("current")


class _SwFilterDhcpServerTrapLogState_Type(Integer32):
    """Custom type swFilterDhcpServerTrapLogState based on Integer32"""
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


_SwFilterDhcpServerTrapLogState_Type.__name__ = "Integer32"
_SwFilterDhcpServerTrapLogState_Object = MibScalar
swFilterDhcpServerTrapLogState = _SwFilterDhcpServerTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 4),
    _SwFilterDhcpServerTrapLogState_Type()
)
swFilterDhcpServerTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpServerTrapLogState.setStatus("current")
_SwFilterNetbios_ObjectIdentity = ObjectIdentity
swFilterNetbios = _SwFilterNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 2)
)
_SwFilterNetbiosTable_Object = MibTable
swFilterNetbiosTable = _SwFilterNetbiosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 2, 1)
)
if mibBuilder.loadTexts:
    swFilterNetbiosTable.setStatus("current")
_SwFilterNetbiosEntry_Object = MibTableRow
swFilterNetbiosEntry = _SwFilterNetbiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 2, 1, 1)
)
swFilterNetbiosEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterNetbiosPortIndex"),
)
if mibBuilder.loadTexts:
    swFilterNetbiosEntry.setStatus("current")


class _SwFilterNetbiosPortIndex_Type(Integer32):
    """Custom type swFilterNetbiosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwFilterNetbiosPortIndex_Type.__name__ = "Integer32"
_SwFilterNetbiosPortIndex_Object = MibTableColumn
swFilterNetbiosPortIndex = _SwFilterNetbiosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 2, 1, 1, 1),
    _SwFilterNetbiosPortIndex_Type()
)
swFilterNetbiosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterNetbiosPortIndex.setStatus("current")


class _SwFilterNetbiosState_Type(Integer32):
    """Custom type swFilterNetbiosState based on Integer32"""
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


_SwFilterNetbiosState_Type.__name__ = "Integer32"
_SwFilterNetbiosState_Object = MibTableColumn
swFilterNetbiosState = _SwFilterNetbiosState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 2, 1, 1, 2),
    _SwFilterNetbiosState_Type()
)
swFilterNetbiosState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterNetbiosState.setStatus("current")
_SwFilterExtNetbios_ObjectIdentity = ObjectIdentity
swFilterExtNetbios = _SwFilterExtNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 3)
)
_SwFilterExtNetbiosTable_Object = MibTable
swFilterExtNetbiosTable = _SwFilterExtNetbiosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 3, 1)
)
if mibBuilder.loadTexts:
    swFilterExtNetbiosTable.setStatus("current")
_SwFilterExtNetbiosEntry_Object = MibTableRow
swFilterExtNetbiosEntry = _SwFilterExtNetbiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 3, 1, 1)
)
swFilterExtNetbiosEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterExtNetbiosPortIndex"),
)
if mibBuilder.loadTexts:
    swFilterExtNetbiosEntry.setStatus("current")


class _SwFilterExtNetbiosPortIndex_Type(Integer32):
    """Custom type swFilterExtNetbiosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwFilterExtNetbiosPortIndex_Type.__name__ = "Integer32"
_SwFilterExtNetbiosPortIndex_Object = MibTableColumn
swFilterExtNetbiosPortIndex = _SwFilterExtNetbiosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 3, 1, 1, 1),
    _SwFilterExtNetbiosPortIndex_Type()
)
swFilterExtNetbiosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterExtNetbiosPortIndex.setStatus("current")


class _SwFilterExtNetbiosState_Type(Integer32):
    """Custom type swFilterExtNetbiosState based on Integer32"""
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


_SwFilterExtNetbiosState_Type.__name__ = "Integer32"
_SwFilterExtNetbiosState_Object = MibTableColumn
swFilterExtNetbiosState = _SwFilterExtNetbiosState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 3, 1, 1, 2),
    _SwFilterExtNetbiosState_Type()
)
swFilterExtNetbiosState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterExtNetbiosState.setStatus("current")
_SwFilterCPU_ObjectIdentity = ObjectIdentity
swFilterCPU = _SwFilterCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4)
)
_SwFilterCPUL3CtrlPktTable_Object = MibTable
swFilterCPUL3CtrlPktTable = _SwFilterCPUL3CtrlPktTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1)
)
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktTable.setStatus("current")
_SwFilterCPUL3CtrlPktEntry_Object = MibTableRow
swFilterCPUL3CtrlPktEntry = _SwFilterCPUL3CtrlPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1)
)
swFilterCPUL3CtrlPktEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterCPUL3CtrlPktPortIndex"),
)
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktEntry.setStatus("current")


class _SwFilterCPUL3CtrlPktPortIndex_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwFilterCPUL3CtrlPktPortIndex_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktPortIndex_Object = MibTableColumn
swFilterCPUL3CtrlPktPortIndex = _SwFilterCPUL3CtrlPktPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 1),
    _SwFilterCPUL3CtrlPktPortIndex_Type()
)
swFilterCPUL3CtrlPktPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktPortIndex.setStatus("current")


class _SwFilterCPUL3CtrlPktRIPState_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktRIPState based on Integer32"""
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


_SwFilterCPUL3CtrlPktRIPState_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktRIPState_Object = MibTableColumn
swFilterCPUL3CtrlPktRIPState = _SwFilterCPUL3CtrlPktRIPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 2),
    _SwFilterCPUL3CtrlPktRIPState_Type()
)
swFilterCPUL3CtrlPktRIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktRIPState.setStatus("current")


class _SwFilterCPUL3CtrlPktOSPFState_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktOSPFState based on Integer32"""
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


_SwFilterCPUL3CtrlPktOSPFState_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktOSPFState_Object = MibTableColumn
swFilterCPUL3CtrlPktOSPFState = _SwFilterCPUL3CtrlPktOSPFState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 3),
    _SwFilterCPUL3CtrlPktOSPFState_Type()
)
swFilterCPUL3CtrlPktOSPFState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktOSPFState.setStatus("current")


class _SwFilterCPUL3CtrlPktVRRPState_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktVRRPState based on Integer32"""
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


_SwFilterCPUL3CtrlPktVRRPState_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktVRRPState_Object = MibTableColumn
swFilterCPUL3CtrlPktVRRPState = _SwFilterCPUL3CtrlPktVRRPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 4),
    _SwFilterCPUL3CtrlPktVRRPState_Type()
)
swFilterCPUL3CtrlPktVRRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktVRRPState.setStatus("current")


class _SwFilterCPUL3CtrlPktPIMState_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktPIMState based on Integer32"""
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


_SwFilterCPUL3CtrlPktPIMState_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktPIMState_Object = MibTableColumn
swFilterCPUL3CtrlPktPIMState = _SwFilterCPUL3CtrlPktPIMState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 5),
    _SwFilterCPUL3CtrlPktPIMState_Type()
)
swFilterCPUL3CtrlPktPIMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktPIMState.setStatus("current")


class _SwFilterCPUL3CtrlPktDVMRPState_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktDVMRPState based on Integer32"""
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


_SwFilterCPUL3CtrlPktDVMRPState_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktDVMRPState_Object = MibTableColumn
swFilterCPUL3CtrlPktDVMRPState = _SwFilterCPUL3CtrlPktDVMRPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 6),
    _SwFilterCPUL3CtrlPktDVMRPState_Type()
)
swFilterCPUL3CtrlPktDVMRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktDVMRPState.setStatus("current")


class _SwFilterCPUL3CtrlPktIGMPQueryState_Type(Integer32):
    """Custom type swFilterCPUL3CtrlPktIGMPQueryState based on Integer32"""
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


_SwFilterCPUL3CtrlPktIGMPQueryState_Type.__name__ = "Integer32"
_SwFilterCPUL3CtrlPktIGMPQueryState_Object = MibTableColumn
swFilterCPUL3CtrlPktIGMPQueryState = _SwFilterCPUL3CtrlPktIGMPQueryState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 4, 1, 1, 7),
    _SwFilterCPUL3CtrlPktIGMPQueryState_Type()
)
swFilterCPUL3CtrlPktIGMPQueryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterCPUL3CtrlPktIGMPQueryState.setStatus("current")
_SwFilterEgress_ObjectIdentity = ObjectIdentity
swFilterEgress = _SwFilterEgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 5)
)
_SwPktEgressFilterCtrlTable_Object = MibTable
swPktEgressFilterCtrlTable = _SwPktEgressFilterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 5, 1)
)
if mibBuilder.loadTexts:
    swPktEgressFilterCtrlTable.setStatus("current")
_SwPktEgressFilterCtrlEntry_Object = MibTableRow
swPktEgressFilterCtrlEntry = _SwPktEgressFilterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 5, 1, 1)
)
swPktEgressFilterCtrlEntry.setIndexNames(
    (0, "FILTER-MIB", "swPktEgressFilterPortIndex"),
)
if mibBuilder.loadTexts:
    swPktEgressFilterCtrlEntry.setStatus("current")


class _SwPktEgressFilterPortIndex_Type(Integer32):
    """Custom type swPktEgressFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPktEgressFilterPortIndex_Type.__name__ = "Integer32"
_SwPktEgressFilterPortIndex_Object = MibTableColumn
swPktEgressFilterPortIndex = _SwPktEgressFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 5, 1, 1, 1),
    _SwPktEgressFilterPortIndex_Type()
)
swPktEgressFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPktEgressFilterPortIndex.setStatus("current")


class _SwPktEgressFilterUnknownUnicastStatus_Type(Integer32):
    """Custom type swPktEgressFilterUnknownUnicastStatus based on Integer32"""
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


_SwPktEgressFilterUnknownUnicastStatus_Type.__name__ = "Integer32"
_SwPktEgressFilterUnknownUnicastStatus_Object = MibTableColumn
swPktEgressFilterUnknownUnicastStatus = _SwPktEgressFilterUnknownUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 5, 1, 1, 2),
    _SwPktEgressFilterUnknownUnicastStatus_Type()
)
swPktEgressFilterUnknownUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktEgressFilterUnknownUnicastStatus.setStatus("current")


class _SwPktEgressFilterUnknownMulticastStatus_Type(Integer32):
    """Custom type swPktEgressFilterUnknownMulticastStatus based on Integer32"""
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


_SwPktEgressFilterUnknownMulticastStatus_Type.__name__ = "Integer32"
_SwPktEgressFilterUnknownMulticastStatus_Object = MibTableColumn
swPktEgressFilterUnknownMulticastStatus = _SwPktEgressFilterUnknownMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 5, 1, 1, 3),
    _SwPktEgressFilterUnknownMulticastStatus_Type()
)
swPktEgressFilterUnknownMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPktEgressFilterUnknownMulticastStatus.setStatus("current")
_SwFilterNotify_ObjectIdentity = ObjectIdentity
swFilterNotify = _SwFilterNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100)
)
_SwFilterNotifyPrefix_ObjectIdentity = ObjectIdentity
swFilterNotifyPrefix = _SwFilterNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 0)
)
_SwFilterNotificationBindings_ObjectIdentity = ObjectIdentity
swFilterNotificationBindings = _SwFilterNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 2)
)
_SwFilterDetectedIP_Type = IpAddress
_SwFilterDetectedIP_Object = MibScalar
swFilterDetectedIP = _SwFilterDetectedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 2, 1),
    _SwFilterDetectedIP_Type()
)
swFilterDetectedIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swFilterDetectedIP.setStatus("current")
_SwFilterDetectedport_Type = Integer32
_SwFilterDetectedport_Object = MibScalar
swFilterDetectedport = _SwFilterDetectedport_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 2, 2),
    _SwFilterDetectedport_Type()
)
swFilterDetectedport.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swFilterDetectedport.setStatus("current")

# Managed Objects groups


# Notification objects

swFilterDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 0, 1)
)
swFilterDetectedTrap.setObjects(
      *(("FILTER-MIB", "swFilterDetectedIP"),
        ("FILTER-MIB", "swFilterDetectedport"))
)
if mibBuilder.loadTexts:
    swFilterDetectedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FILTER-MIB",
    **{"PortList": PortList,
       "swFilterMIB": swFilterMIB,
       "swFilterDhcp": swFilterDhcp,
       "swFilterDhcpPermitTable": swFilterDhcpPermitTable,
       "swFilterDhcpPermitEntry": swFilterDhcpPermitEntry,
       "swFilterDhcpServerIP": swFilterDhcpServerIP,
       "swFilterDhcpClientMac": swFilterDhcpClientMac,
       "swFilterDhcpPorts": swFilterDhcpPorts,
       "swFilterDhcpStatus": swFilterDhcpStatus,
       "swFilterDhcpPortTable": swFilterDhcpPortTable,
       "swFilterDhcpPortEntry": swFilterDhcpPortEntry,
       "swFilterDhcpPortIndex": swFilterDhcpPortIndex,
       "swFilterDhcpPortState": swFilterDhcpPortState,
       "swFilterDhcpServerIllegalSerLogSuppressDuration": swFilterDhcpServerIllegalSerLogSuppressDuration,
       "swFilterDhcpServerTrapLogState": swFilterDhcpServerTrapLogState,
       "swFilterNetbios": swFilterNetbios,
       "swFilterNetbiosTable": swFilterNetbiosTable,
       "swFilterNetbiosEntry": swFilterNetbiosEntry,
       "swFilterNetbiosPortIndex": swFilterNetbiosPortIndex,
       "swFilterNetbiosState": swFilterNetbiosState,
       "swFilterExtNetbios": swFilterExtNetbios,
       "swFilterExtNetbiosTable": swFilterExtNetbiosTable,
       "swFilterExtNetbiosEntry": swFilterExtNetbiosEntry,
       "swFilterExtNetbiosPortIndex": swFilterExtNetbiosPortIndex,
       "swFilterExtNetbiosState": swFilterExtNetbiosState,
       "swFilterCPU": swFilterCPU,
       "swFilterCPUL3CtrlPktTable": swFilterCPUL3CtrlPktTable,
       "swFilterCPUL3CtrlPktEntry": swFilterCPUL3CtrlPktEntry,
       "swFilterCPUL3CtrlPktPortIndex": swFilterCPUL3CtrlPktPortIndex,
       "swFilterCPUL3CtrlPktRIPState": swFilterCPUL3CtrlPktRIPState,
       "swFilterCPUL3CtrlPktOSPFState": swFilterCPUL3CtrlPktOSPFState,
       "swFilterCPUL3CtrlPktVRRPState": swFilterCPUL3CtrlPktVRRPState,
       "swFilterCPUL3CtrlPktPIMState": swFilterCPUL3CtrlPktPIMState,
       "swFilterCPUL3CtrlPktDVMRPState": swFilterCPUL3CtrlPktDVMRPState,
       "swFilterCPUL3CtrlPktIGMPQueryState": swFilterCPUL3CtrlPktIGMPQueryState,
       "swFilterEgress": swFilterEgress,
       "swPktEgressFilterCtrlTable": swPktEgressFilterCtrlTable,
       "swPktEgressFilterCtrlEntry": swPktEgressFilterCtrlEntry,
       "swPktEgressFilterPortIndex": swPktEgressFilterPortIndex,
       "swPktEgressFilterUnknownUnicastStatus": swPktEgressFilterUnknownUnicastStatus,
       "swPktEgressFilterUnknownMulticastStatus": swPktEgressFilterUnknownMulticastStatus,
       "swFilterNotify": swFilterNotify,
       "swFilterNotifyPrefix": swFilterNotifyPrefix,
       "swFilterDetectedTrap": swFilterDetectedTrap,
       "swFilterNotificationBindings": swFilterNotificationBindings,
       "swFilterDetectedIP": swFilterDetectedIP,
       "swFilterDetectedport": swFilterDetectedport}
)
