# SNMP MIB module (IPAD-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPAD-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:44 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Verilink_ObjectIdentity = ObjectIdentity
verilink = _Verilink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321)
)
_Hbu_ObjectIdentity = ObjectIdentity
hbu = _Hbu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100)
)
_Ipad_ObjectIdentity = ObjectIdentity
ipad = _Ipad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1)
)
_IpadFrPort_ObjectIdentity = ObjectIdentity
ipadFrPort = _IpadFrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1)
)
_IpadService_ObjectIdentity = ObjectIdentity
ipadService = _IpadService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2)
)
_IpadChannel_ObjectIdentity = ObjectIdentity
ipadChannel = _IpadChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3)
)
_IpadDLCI_ObjectIdentity = ObjectIdentity
ipadDLCI = _IpadDLCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4)
)
_IpadEndpoint_ObjectIdentity = ObjectIdentity
ipadEndpoint = _IpadEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5)
)
_IpadUser_ObjectIdentity = ObjectIdentity
ipadUser = _IpadUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6)
)
_IpadPPP_ObjectIdentity = ObjectIdentity
ipadPPP = _IpadPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7)
)
_IpadModem_ObjectIdentity = ObjectIdentity
ipadModem = _IpadModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8)
)
_IpadSvcAware_ObjectIdentity = ObjectIdentity
ipadSvcAware = _IpadSvcAware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9)
)
_IpadPktSwitch_ObjectIdentity = ObjectIdentity
ipadPktSwitch = _IpadPktSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10)
)
_IpadTrapDest_ObjectIdentity = ObjectIdentity
ipadTrapDest = _IpadTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11)
)
_IpadMisc_ObjectIdentity = ObjectIdentity
ipadMisc = _IpadMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12)
)
_IpadRouter_ObjectIdentity = ObjectIdentity
ipadRouter = _IpadRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13)
)
_IpadCircuitParms_ObjectIdentity = ObjectIdentity
ipadCircuitParms = _IpadCircuitParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1)
)
_IpadCircuitTable_Object = MibTable
ipadCircuitTable = _IpadCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    ipadCircuitTable.setStatus("optional")
_IpadCircuitTableEntry_Object = MibTableRow
ipadCircuitTableEntry = _IpadCircuitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1)
)
ipadCircuitTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadCircuitIndex"),
)
if mibBuilder.loadTexts:
    ipadCircuitTableEntry.setStatus("mandatory")
_IpadCircuitIndex_Type = Integer32
_IpadCircuitIndex_Object = MibTableColumn
ipadCircuitIndex = _IpadCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 1),
    _IpadCircuitIndex_Type()
)
ipadCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadCircuitIndex.setStatus("mandatory")
_IpadCircuitEndpoint_Type = DisplayString
_IpadCircuitEndpoint_Object = MibTableColumn
ipadCircuitEndpoint = _IpadCircuitEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 2),
    _IpadCircuitEndpoint_Type()
)
ipadCircuitEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEndpoint.setStatus("mandatory")
_IpadCircuitIpAddress_Type = IpAddress
_IpadCircuitIpAddress_Object = MibTableColumn
ipadCircuitIpAddress = _IpadCircuitIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 3),
    _IpadCircuitIpAddress_Type()
)
ipadCircuitIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitIpAddress.setStatus("mandatory")
_IpadCircuitIpMask_Type = IpAddress
_IpadCircuitIpMask_Object = MibTableColumn
ipadCircuitIpMask = _IpadCircuitIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 4),
    _IpadCircuitIpMask_Type()
)
ipadCircuitIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitIpMask.setStatus("mandatory")


class _IpadCircuitMaxTransmitUnit_Type(Integer32):
    """Custom type ipadCircuitMaxTransmitUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadCircuitMaxTransmitUnit_Type.__name__ = "Integer32"
_IpadCircuitMaxTransmitUnit_Object = MibTableColumn
ipadCircuitMaxTransmitUnit = _IpadCircuitMaxTransmitUnit_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 5),
    _IpadCircuitMaxTransmitUnit_Type()
)
ipadCircuitMaxTransmitUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitMaxTransmitUnit.setStatus("mandatory")


class _IpadCircuitCost_Type(Integer32):
    """Custom type ipadCircuitCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadCircuitCost_Type.__name__ = "Integer32"
_IpadCircuitCost_Object = MibTableColumn
ipadCircuitCost = _IpadCircuitCost_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 6),
    _IpadCircuitCost_Type()
)
ipadCircuitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitCost.setStatus("mandatory")


class _IpadCircuitEnableRIP_Type(Integer32):
    """Custom type ipadCircuitEnableRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadCircuitEnableRIP_Type.__name__ = "Integer32"
_IpadCircuitEnableRIP_Object = MibTableColumn
ipadCircuitEnableRIP = _IpadCircuitEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 7),
    _IpadCircuitEnableRIP_Type()
)
ipadCircuitEnableRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEnableRIP.setStatus("mandatory")


class _IpadCircuitEnableOSPF_Type(Integer32):
    """Custom type ipadCircuitEnableOSPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadCircuitEnableOSPF_Type.__name__ = "Integer32"
_IpadCircuitEnableOSPF_Object = MibTableColumn
ipadCircuitEnableOSPF = _IpadCircuitEnableOSPF_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 8),
    _IpadCircuitEnableOSPF_Type()
)
ipadCircuitEnableOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEnableOSPF.setStatus("mandatory")


class _IpadCircuitEnableMulticast_Type(Integer32):
    """Custom type ipadCircuitEnableMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadCircuitEnableMulticast_Type.__name__ = "Integer32"
_IpadCircuitEnableMulticast_Object = MibTableColumn
ipadCircuitEnableMulticast = _IpadCircuitEnableMulticast_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 9),
    _IpadCircuitEnableMulticast_Type()
)
ipadCircuitEnableMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEnableMulticast.setStatus("mandatory")


class _IpadCircuitAdd_Type(Integer32):
    """Custom type ipadCircuitAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadCircuitAdd_Type.__name__ = "Integer32"
_IpadCircuitAdd_Object = MibScalar
ipadCircuitAdd = _IpadCircuitAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 2),
    _IpadCircuitAdd_Type()
)
ipadCircuitAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitAdd.setStatus("mandatory")
_IpadCircuitDelete_Type = Integer32
_IpadCircuitDelete_Object = MibScalar
ipadCircuitDelete = _IpadCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 3),
    _IpadCircuitDelete_Type()
)
ipadCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitDelete.setStatus("mandatory")
_IpadRIPParms_ObjectIdentity = ObjectIdentity
ipadRIPParms = _IpadRIPParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2)
)


class _IpadRIPEnable_Type(Integer32):
    """Custom type ipadRIPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadRIPEnable_Type.__name__ = "Integer32"
_IpadRIPEnable_Object = MibScalar
ipadRIPEnable = _IpadRIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 1),
    _IpadRIPEnable_Type()
)
ipadRIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPEnable.setStatus("mandatory")


class _IpadRIPTrustNeighbors_Type(Integer32):
    """Custom type ipadRIPTrustNeighbors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadRIPTrustNeighbors_Type.__name__ = "Integer32"
_IpadRIPTrustNeighbors_Object = MibScalar
ipadRIPTrustNeighbors = _IpadRIPTrustNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 2),
    _IpadRIPTrustNeighbors_Type()
)
ipadRIPTrustNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPTrustNeighbors.setStatus("mandatory")


class _IpadRIPInterval_Type(Integer32):
    """Custom type ipadRIPInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadRIPInterval_Type.__name__ = "Integer32"
_IpadRIPInterval_Object = MibScalar
ipadRIPInterval = _IpadRIPInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 3),
    _IpadRIPInterval_Type()
)
ipadRIPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPInterval.setStatus("mandatory")


class _IpadRIPDomain_Type(Integer32):
    """Custom type ipadRIPDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadRIPDomain_Type.__name__ = "Integer32"
_IpadRIPDomain_Object = MibScalar
ipadRIPDomain = _IpadRIPDomain_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 4),
    _IpadRIPDomain_Type()
)
ipadRIPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPDomain.setStatus("mandatory")
_IpadRIPStaticARPTable_Object = MibTable
ipadRIPStaticARPTable = _IpadRIPStaticARPTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5)
)
if mibBuilder.loadTexts:
    ipadRIPStaticARPTable.setStatus("optional")
_IpadRIPStaticARPTableEntry_Object = MibTableRow
ipadRIPStaticARPTableEntry = _IpadRIPStaticARPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1)
)
ipadRIPStaticARPTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadRIPStaticARPIndex"),
)
if mibBuilder.loadTexts:
    ipadRIPStaticARPTableEntry.setStatus("mandatory")
_IpadRIPStaticARPIndex_Type = Integer32
_IpadRIPStaticARPIndex_Object = MibTableColumn
ipadRIPStaticARPIndex = _IpadRIPStaticARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 1),
    _IpadRIPStaticARPIndex_Type()
)
ipadRIPStaticARPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPStaticARPIndex.setStatus("mandatory")
_IpadRIPStaticARPEndpoint_Type = DisplayString
_IpadRIPStaticARPEndpoint_Object = MibTableColumn
ipadRIPStaticARPEndpoint = _IpadRIPStaticARPEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 2),
    _IpadRIPStaticARPEndpoint_Type()
)
ipadRIPStaticARPEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPEndpoint.setStatus("mandatory")
_IpadRIPStaticARPIpAddress_Type = IpAddress
_IpadRIPStaticARPIpAddress_Object = MibTableColumn
ipadRIPStaticARPIpAddress = _IpadRIPStaticARPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 3),
    _IpadRIPStaticARPIpAddress_Type()
)
ipadRIPStaticARPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPIpAddress.setStatus("mandatory")
_IpadRIPStaticARPMacAddress_Type = DisplayString
_IpadRIPStaticARPMacAddress_Object = MibTableColumn
ipadRIPStaticARPMacAddress = _IpadRIPStaticARPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 4),
    _IpadRIPStaticARPMacAddress_Type()
)
ipadRIPStaticARPMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPMacAddress.setStatus("mandatory")
_IpadRIPStaticARPDLCIAddress_Type = Integer32
_IpadRIPStaticARPDLCIAddress_Object = MibTableColumn
ipadRIPStaticARPDLCIAddress = _IpadRIPStaticARPDLCIAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 5),
    _IpadRIPStaticARPDLCIAddress_Type()
)
ipadRIPStaticARPDLCIAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPDLCIAddress.setStatus("mandatory")


class _IpadRIPStaticARPEnableARP_Type(Integer32):
    """Custom type ipadRIPStaticARPEnableARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadRIPStaticARPEnableARP_Type.__name__ = "Integer32"
_IpadRIPStaticARPEnableARP_Object = MibTableColumn
ipadRIPStaticARPEnableARP = _IpadRIPStaticARPEnableARP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 6),
    _IpadRIPStaticARPEnableARP_Type()
)
ipadRIPStaticARPEnableARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPEnableARP.setStatus("mandatory")


class _IpadRIPStaticARPAdd_Type(Integer32):
    """Custom type ipadRIPStaticARPAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadRIPStaticARPAdd_Type.__name__ = "Integer32"
_IpadRIPStaticARPAdd_Object = MibScalar
ipadRIPStaticARPAdd = _IpadRIPStaticARPAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 6),
    _IpadRIPStaticARPAdd_Type()
)
ipadRIPStaticARPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPAdd.setStatus("mandatory")
_IpadRIPStaticARPDelete_Type = Integer32
_IpadRIPStaticARPDelete_Object = MibScalar
ipadRIPStaticARPDelete = _IpadRIPStaticARPDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 7),
    _IpadRIPStaticARPDelete_Type()
)
ipadRIPStaticARPDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPDelete.setStatus("mandatory")
_IpadRIPStaticRouteTable_Object = MibTable
ipadRIPStaticRouteTable = _IpadRIPStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8)
)
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTable.setStatus("optional")
_IpadRIPStaticRouteTableEntry_Object = MibTableRow
ipadRIPStaticRouteTableEntry = _IpadRIPStaticRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1)
)
ipadRIPStaticRouteTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadRIPStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTableEntry.setStatus("mandatory")
_IpadRIPStaticRouteIndex_Type = Integer32
_IpadRIPStaticRouteIndex_Object = MibTableColumn
ipadRIPStaticRouteIndex = _IpadRIPStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 1),
    _IpadRIPStaticRouteIndex_Type()
)
ipadRIPStaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteIndex.setStatus("mandatory")
_IpadRIPStaticRouteEndpoint_Type = DisplayString
_IpadRIPStaticRouteEndpoint_Object = MibTableColumn
ipadRIPStaticRouteEndpoint = _IpadRIPStaticRouteEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 2),
    _IpadRIPStaticRouteEndpoint_Type()
)
ipadRIPStaticRouteEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteEndpoint.setStatus("mandatory")
_IpadRIPStaticRouteTargetIpAddress_Type = IpAddress
_IpadRIPStaticRouteTargetIpAddress_Object = MibTableColumn
ipadRIPStaticRouteTargetIpAddress = _IpadRIPStaticRouteTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 3),
    _IpadRIPStaticRouteTargetIpAddress_Type()
)
ipadRIPStaticRouteTargetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTargetIpAddress.setStatus("mandatory")
_IpadRIPStaticRouteTargetIpMask_Type = IpAddress
_IpadRIPStaticRouteTargetIpMask_Object = MibTableColumn
ipadRIPStaticRouteTargetIpMask = _IpadRIPStaticRouteTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 4),
    _IpadRIPStaticRouteTargetIpMask_Type()
)
ipadRIPStaticRouteTargetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTargetIpMask.setStatus("mandatory")
_IpadRIPStaticRouteNextHopIpAddress_Type = IpAddress
_IpadRIPStaticRouteNextHopIpAddress_Object = MibTableColumn
ipadRIPStaticRouteNextHopIpAddress = _IpadRIPStaticRouteNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 5),
    _IpadRIPStaticRouteNextHopIpAddress_Type()
)
ipadRIPStaticRouteNextHopIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteNextHopIpAddress.setStatus("mandatory")


class _IpadRIPStaticRouteCost_Type(Integer32):
    """Custom type ipadRIPStaticRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadRIPStaticRouteCost_Type.__name__ = "Integer32"
_IpadRIPStaticRouteCost_Object = MibTableColumn
ipadRIPStaticRouteCost = _IpadRIPStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 6),
    _IpadRIPStaticRouteCost_Type()
)
ipadRIPStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteCost.setStatus("mandatory")


class _IpadRIPStaticRouteEnableRouter_Type(Integer32):
    """Custom type ipadRIPStaticRouteEnableRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpadRIPStaticRouteEnableRouter_Type.__name__ = "Integer32"
_IpadRIPStaticRouteEnableRouter_Object = MibTableColumn
ipadRIPStaticRouteEnableRouter = _IpadRIPStaticRouteEnableRouter_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 7),
    _IpadRIPStaticRouteEnableRouter_Type()
)
ipadRIPStaticRouteEnableRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteEnableRouter.setStatus("mandatory")


class _IpadRIPStaticRouteAdd_Type(Integer32):
    """Custom type ipadRIPStaticRouteAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadRIPStaticRouteAdd_Type.__name__ = "Integer32"
_IpadRIPStaticRouteAdd_Object = MibScalar
ipadRIPStaticRouteAdd = _IpadRIPStaticRouteAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 9),
    _IpadRIPStaticRouteAdd_Type()
)
ipadRIPStaticRouteAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteAdd.setStatus("mandatory")
_IpadRIPStaticRouteDelete_Type = Integer32
_IpadRIPStaticRouteDelete_Object = MibScalar
ipadRIPStaticRouteDelete = _IpadRIPStaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 10),
    _IpadRIPStaticRouteDelete_Type()
)
ipadRIPStaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteDelete.setStatus("mandatory")
_IpadRIPNeighborTable_Object = MibTable
ipadRIPNeighborTable = _IpadRIPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11)
)
if mibBuilder.loadTexts:
    ipadRIPNeighborTable.setStatus("optional")
_IpadRIPNeighborTableEntry_Object = MibTableRow
ipadRIPNeighborTableEntry = _IpadRIPNeighborTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1)
)
ipadRIPNeighborTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadRIPNeighborIndex"),
)
if mibBuilder.loadTexts:
    ipadRIPNeighborTableEntry.setStatus("mandatory")
_IpadRIPNeighborIndex_Type = Integer32
_IpadRIPNeighborIndex_Object = MibTableColumn
ipadRIPNeighborIndex = _IpadRIPNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 1),
    _IpadRIPNeighborIndex_Type()
)
ipadRIPNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPNeighborIndex.setStatus("mandatory")
_IpadRIPNeighborAddress_Type = IpAddress
_IpadRIPNeighborAddress_Object = MibTableColumn
ipadRIPNeighborAddress = _IpadRIPNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 2),
    _IpadRIPNeighborAddress_Type()
)
ipadRIPNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPNeighborAddress.setStatus("mandatory")
_IpadRIPNeighborAdd_Type = IpAddress
_IpadRIPNeighborAdd_Object = MibScalar
ipadRIPNeighborAdd = _IpadRIPNeighborAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 12),
    _IpadRIPNeighborAdd_Type()
)
ipadRIPNeighborAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPNeighborAdd.setStatus("mandatory")
_IpadRIPNeighborDelete_Type = IpAddress
_IpadRIPNeighborDelete_Object = MibScalar
ipadRIPNeighborDelete = _IpadRIPNeighborDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 13),
    _IpadRIPNeighborDelete_Type()
)
ipadRIPNeighborDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPNeighborDelete.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-ROUTER-MIB",
    **{"verilink": verilink,
       "hbu": hbu,
       "ipad": ipad,
       "ipadFrPort": ipadFrPort,
       "ipadService": ipadService,
       "ipadChannel": ipadChannel,
       "ipadDLCI": ipadDLCI,
       "ipadEndpoint": ipadEndpoint,
       "ipadUser": ipadUser,
       "ipadPPP": ipadPPP,
       "ipadModem": ipadModem,
       "ipadSvcAware": ipadSvcAware,
       "ipadPktSwitch": ipadPktSwitch,
       "ipadTrapDest": ipadTrapDest,
       "ipadMisc": ipadMisc,
       "ipadRouter": ipadRouter,
       "ipadCircuitParms": ipadCircuitParms,
       "ipadCircuitTable": ipadCircuitTable,
       "ipadCircuitTableEntry": ipadCircuitTableEntry,
       "ipadCircuitIndex": ipadCircuitIndex,
       "ipadCircuitEndpoint": ipadCircuitEndpoint,
       "ipadCircuitIpAddress": ipadCircuitIpAddress,
       "ipadCircuitIpMask": ipadCircuitIpMask,
       "ipadCircuitMaxTransmitUnit": ipadCircuitMaxTransmitUnit,
       "ipadCircuitCost": ipadCircuitCost,
       "ipadCircuitEnableRIP": ipadCircuitEnableRIP,
       "ipadCircuitEnableOSPF": ipadCircuitEnableOSPF,
       "ipadCircuitEnableMulticast": ipadCircuitEnableMulticast,
       "ipadCircuitAdd": ipadCircuitAdd,
       "ipadCircuitDelete": ipadCircuitDelete,
       "ipadRIPParms": ipadRIPParms,
       "ipadRIPEnable": ipadRIPEnable,
       "ipadRIPTrustNeighbors": ipadRIPTrustNeighbors,
       "ipadRIPInterval": ipadRIPInterval,
       "ipadRIPDomain": ipadRIPDomain,
       "ipadRIPStaticARPTable": ipadRIPStaticARPTable,
       "ipadRIPStaticARPTableEntry": ipadRIPStaticARPTableEntry,
       "ipadRIPStaticARPIndex": ipadRIPStaticARPIndex,
       "ipadRIPStaticARPEndpoint": ipadRIPStaticARPEndpoint,
       "ipadRIPStaticARPIpAddress": ipadRIPStaticARPIpAddress,
       "ipadRIPStaticARPMacAddress": ipadRIPStaticARPMacAddress,
       "ipadRIPStaticARPDLCIAddress": ipadRIPStaticARPDLCIAddress,
       "ipadRIPStaticARPEnableARP": ipadRIPStaticARPEnableARP,
       "ipadRIPStaticARPAdd": ipadRIPStaticARPAdd,
       "ipadRIPStaticARPDelete": ipadRIPStaticARPDelete,
       "ipadRIPStaticRouteTable": ipadRIPStaticRouteTable,
       "ipadRIPStaticRouteTableEntry": ipadRIPStaticRouteTableEntry,
       "ipadRIPStaticRouteIndex": ipadRIPStaticRouteIndex,
       "ipadRIPStaticRouteEndpoint": ipadRIPStaticRouteEndpoint,
       "ipadRIPStaticRouteTargetIpAddress": ipadRIPStaticRouteTargetIpAddress,
       "ipadRIPStaticRouteTargetIpMask": ipadRIPStaticRouteTargetIpMask,
       "ipadRIPStaticRouteNextHopIpAddress": ipadRIPStaticRouteNextHopIpAddress,
       "ipadRIPStaticRouteCost": ipadRIPStaticRouteCost,
       "ipadRIPStaticRouteEnableRouter": ipadRIPStaticRouteEnableRouter,
       "ipadRIPStaticRouteAdd": ipadRIPStaticRouteAdd,
       "ipadRIPStaticRouteDelete": ipadRIPStaticRouteDelete,
       "ipadRIPNeighborTable": ipadRIPNeighborTable,
       "ipadRIPNeighborTableEntry": ipadRIPNeighborTableEntry,
       "ipadRIPNeighborIndex": ipadRIPNeighborIndex,
       "ipadRIPNeighborAddress": ipadRIPNeighborAddress,
       "ipadRIPNeighborAdd": ipadRIPNeighborAdd,
       "ipadRIPNeighborDelete": ipadRIPNeighborDelete}
)
