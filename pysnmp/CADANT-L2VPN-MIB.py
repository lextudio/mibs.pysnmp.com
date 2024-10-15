# SNMP MIB module (CADANT-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-L2VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:02 2024
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

(cadL2vpn,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadL2vpn")

(DocsL2vpnIfList,
 clabProjDocsis) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "DocsL2vpnIfList",
    "clabProjDocsis")

(docsIfCmtsCmStatusIndex,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusIndex")

(DocsL2vpnIdentifier,
 DocsL2vpnIndex,
 DocsNsiEncapSubtype,
 docsL2vpnIdx) = mibBuilder.importSymbols(
    "DOCS-L2VPN-MIB",
    "DocsL2vpnIdentifier",
    "DocsL2vpnIndex",
    "DocsNsiEncapSubtype",
    "docsL2vpnIdx")

(docsQosPktClassId,
 docsQosServiceFlowId) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "docsQosPktClassId",
    "docsQosServiceFlowId")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadL2vpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1)
)
cadL2vpnMIB.setRevisions(
        ("2015-10-01 00:00",
         "2015-07-07 00:00",
         "2015-06-24 00:00",
         "2015-06-22 00:00",
         "2015-03-09 00:00",
         "2014-12-02 00:00",
         "2013-09-23 00:00",
         "2013-09-10 00:00",
         "2009-08-03 00:00",
         "2009-06-25 00:00",
         "2009-06-23 00:00",
         "2009-06-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadNsiEncapValue(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CadL2vpnMIBObjects_ObjectIdentity = ObjectIdentity
cadL2vpnMIBObjects = _CadL2vpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1)
)
_CadL2vpnParams_ObjectIdentity = ObjectIdentity
cadL2vpnParams = _CadL2vpnParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1)
)


class _CadL2vpnPrimaryNetworkIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadL2vpnPrimaryNetworkIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadL2vpnPrimaryNetworkIfIndex_Object = MibScalar
cadL2vpnPrimaryNetworkIfIndex = _CadL2vpnPrimaryNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 1),
    _CadL2vpnPrimaryNetworkIfIndex_Type()
)
cadL2vpnPrimaryNetworkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadL2vpnPrimaryNetworkIfIndex.setStatus("current")


class _CadL2vpnSecondaryNetworkIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadL2vpnSecondaryNetworkIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadL2vpnSecondaryNetworkIfIndex_Object = MibScalar
cadL2vpnSecondaryNetworkIfIndex = _CadL2vpnSecondaryNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 2),
    _CadL2vpnSecondaryNetworkIfIndex_Type()
)
cadL2vpnSecondaryNetworkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadL2vpnSecondaryNetworkIfIndex.setStatus("current")
_CadL2vpnActiveNetworkIfIndex_Type = InterfaceIndexOrZero
_CadL2vpnActiveNetworkIfIndex_Object = MibScalar
cadL2vpnActiveNetworkIfIndex = _CadL2vpnActiveNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 3),
    _CadL2vpnActiveNetworkIfIndex_Type()
)
cadL2vpnActiveNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnActiveNetworkIfIndex.setStatus("current")


class _CadL2vpnForwardingEnabled_Type(TruthValue):
    """Custom type cadL2vpnForwardingEnabled based on TruthValue"""


_CadL2vpnForwardingEnabled_Object = MibScalar
cadL2vpnForwardingEnabled = _CadL2vpnForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 4),
    _CadL2vpnForwardingEnabled_Type()
)
cadL2vpnForwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadL2vpnForwardingEnabled.setStatus("current")


class _CadL2vpnCmCapEsafeIdentRequired_Type(TruthValue):
    """Custom type cadL2vpnCmCapEsafeIdentRequired based on TruthValue"""


_CadL2vpnCmCapEsafeIdentRequired_Object = MibScalar
cadL2vpnCmCapEsafeIdentRequired = _CadL2vpnCmCapEsafeIdentRequired_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 5),
    _CadL2vpnCmCapEsafeIdentRequired_Type()
)
cadL2vpnCmCapEsafeIdentRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadL2vpnCmCapEsafeIdentRequired.setStatus("current")


class _CadL2vpnCmCapDutFilterRequired_Type(TruthValue):
    """Custom type cadL2vpnCmCapDutFilterRequired based on TruthValue"""


_CadL2vpnCmCapDutFilterRequired_Object = MibScalar
cadL2vpnCmCapDutFilterRequired = _CadL2vpnCmCapDutFilterRequired_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 6),
    _CadL2vpnCmCapDutFilterRequired_Type()
)
cadL2vpnCmCapDutFilterRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadL2vpnCmCapDutFilterRequired.setStatus("current")


class _CadL2vpnGlobalTpid_Type(Integer32):
    """Custom type cadL2vpnGlobalTpid based on Integer32"""
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
        *(("tpid8100", 1),
          ("tpid88a8", 2),
          ("tpid9100", 3))
    )


_CadL2vpnGlobalTpid_Type.__name__ = "Integer32"
_CadL2vpnGlobalTpid_Object = MibScalar
cadL2vpnGlobalTpid = _CadL2vpnGlobalTpid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 1, 7),
    _CadL2vpnGlobalTpid_Type()
)
cadL2vpnGlobalTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadL2vpnGlobalTpid.setStatus("current")
_CadL2vpnInterfaceTable_Object = MibTable
cadL2vpnInterfaceTable = _CadL2vpnInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cadL2vpnInterfaceTable.setStatus("current")
_CadL2vpnInterfaceEntry_Object = MibTableRow
cadL2vpnInterfaceEntry = _CadL2vpnInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1)
)
cadL2vpnInterfaceEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cadL2vpnInterfaceEntry.setStatus("current")
_CadL2vpnInterfaceIfIndex_Type = InterfaceIndex
_CadL2vpnInterfaceIfIndex_Object = MibTableColumn
cadL2vpnInterfaceIfIndex = _CadL2vpnInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1, 1),
    _CadL2vpnInterfaceIfIndex_Type()
)
cadL2vpnInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnInterfaceIfIndex.setStatus("current")


class _CadL2vpnInterfaceIpIgmpSnooping_Type(TruthValue):
    """Custom type cadL2vpnInterfaceIpIgmpSnooping based on TruthValue"""


_CadL2vpnInterfaceIpIgmpSnooping_Object = MibTableColumn
cadL2vpnInterfaceIpIgmpSnooping = _CadL2vpnInterfaceIpIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1, 2),
    _CadL2vpnInterfaceIpIgmpSnooping_Type()
)
cadL2vpnInterfaceIpIgmpSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnInterfaceIpIgmpSnooping.setStatus("current")
_CadL2vpnInterfaceRowStatus_Type = RowStatus
_CadL2vpnInterfaceRowStatus_Object = MibTableColumn
cadL2vpnInterfaceRowStatus = _CadL2vpnInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 2, 1, 3),
    _CadL2vpnInterfaceRowStatus_Type()
)
cadL2vpnInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnInterfaceRowStatus.setStatus("current")
_CadL2vpnVlanIdRangeTable_Object = MibTable
cadL2vpnVlanIdRangeTable = _CadL2vpnVlanIdRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cadL2vpnVlanIdRangeTable.setStatus("current")
_CadL2vpnVlanIdRangeEntry_Object = MibTableRow
cadL2vpnVlanIdRangeEntry = _CadL2vpnVlanIdRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1)
)
cadL2vpnVlanIdRangeEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnVlanIdRangeBegin"),
    (0, "CADANT-L2VPN-MIB", "cadL2vpnVlanIdRangeEnd"),
)
if mibBuilder.loadTexts:
    cadL2vpnVlanIdRangeEntry.setStatus("current")


class _CadL2vpnVlanIdRangeBegin_Type(Unsigned32):
    """Custom type cadL2vpnVlanIdRangeBegin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_CadL2vpnVlanIdRangeBegin_Type.__name__ = "Unsigned32"
_CadL2vpnVlanIdRangeBegin_Object = MibTableColumn
cadL2vpnVlanIdRangeBegin = _CadL2vpnVlanIdRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 1),
    _CadL2vpnVlanIdRangeBegin_Type()
)
cadL2vpnVlanIdRangeBegin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnVlanIdRangeBegin.setStatus("current")


class _CadL2vpnVlanIdRangeEnd_Type(Unsigned32):
    """Custom type cadL2vpnVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_CadL2vpnVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_CadL2vpnVlanIdRangeEnd_Object = MibTableColumn
cadL2vpnVlanIdRangeEnd = _CadL2vpnVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 2),
    _CadL2vpnVlanIdRangeEnd_Type()
)
cadL2vpnVlanIdRangeEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnVlanIdRangeEnd.setStatus("current")


class _CadL2vpnVlanIdRangeNsiEncapSubtype_Type(Integer32):
    """Custom type cadL2vpnVlanIdRangeNsiEncapSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual-qtag", 2),
          ("l3-vrf", 3),
          ("single-qtag", 1))
    )


_CadL2vpnVlanIdRangeNsiEncapSubtype_Type.__name__ = "Integer32"
_CadL2vpnVlanIdRangeNsiEncapSubtype_Object = MibTableColumn
cadL2vpnVlanIdRangeNsiEncapSubtype = _CadL2vpnVlanIdRangeNsiEncapSubtype_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 3),
    _CadL2vpnVlanIdRangeNsiEncapSubtype_Type()
)
cadL2vpnVlanIdRangeNsiEncapSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnVlanIdRangeNsiEncapSubtype.setStatus("current")
_CadL2vpnVlanIdRangeRowStatus_Type = RowStatus
_CadL2vpnVlanIdRangeRowStatus_Object = MibTableColumn
cadL2vpnVlanIdRangeRowStatus = _CadL2vpnVlanIdRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 3, 1, 4),
    _CadL2vpnVlanIdRangeRowStatus_Type()
)
cadL2vpnVlanIdRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnVlanIdRangeRowStatus.setStatus("current")
_CadL2vpnInstanceIdToCmTable_Object = MibTable
cadL2vpnInstanceIdToCmTable = _CadL2vpnInstanceIdToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cadL2vpnInstanceIdToCmTable.setStatus("current")
_CadL2vpnInstanceIdToCmEntry_Object = MibTableRow
cadL2vpnInstanceIdToCmEntry = _CadL2vpnInstanceIdToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1)
)
cadL2vpnInstanceIdToCmEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnInstanceId"),
)
if mibBuilder.loadTexts:
    cadL2vpnInstanceIdToCmEntry.setStatus("current")


class _CadL2vpnInstanceId_Type(Integer32):
    """Custom type cadL2vpnInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_CadL2vpnInstanceId_Type.__name__ = "Integer32"
_CadL2vpnInstanceId_Object = MibTableColumn
cadL2vpnInstanceId = _CadL2vpnInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 1),
    _CadL2vpnInstanceId_Type()
)
cadL2vpnInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnInstanceId.setStatus("current")


class _CadL2vpnInstanceIdVlanIdOuter_Type(Integer32):
    """Custom type cadL2vpnInstanceIdVlanIdOuter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_CadL2vpnInstanceIdVlanIdOuter_Type.__name__ = "Integer32"
_CadL2vpnInstanceIdVlanIdOuter_Object = MibTableColumn
cadL2vpnInstanceIdVlanIdOuter = _CadL2vpnInstanceIdVlanIdOuter_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 2),
    _CadL2vpnInstanceIdVlanIdOuter_Type()
)
cadL2vpnInstanceIdVlanIdOuter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnInstanceIdVlanIdOuter.setStatus("current")


class _CadL2vpnInstanceIdVlanIdInner_Type(Integer32):
    """Custom type cadL2vpnInstanceIdVlanIdInner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CadL2vpnInstanceIdVlanIdInner_Type.__name__ = "Integer32"
_CadL2vpnInstanceIdVlanIdInner_Object = MibTableColumn
cadL2vpnInstanceIdVlanIdInner = _CadL2vpnInstanceIdVlanIdInner_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 3),
    _CadL2vpnInstanceIdVlanIdInner_Type()
)
cadL2vpnInstanceIdVlanIdInner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnInstanceIdVlanIdInner.setStatus("current")
_CadL2vpnInstanceIdCmMac_Type = MacAddress
_CadL2vpnInstanceIdCmMac_Object = MibTableColumn
cadL2vpnInstanceIdCmMac = _CadL2vpnInstanceIdCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 4),
    _CadL2vpnInstanceIdCmMac_Type()
)
cadL2vpnInstanceIdCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnInstanceIdCmMac.setStatus("current")
_CadL2vpnInstanceIdVpnId_Type = DocsL2vpnIdentifier
_CadL2vpnInstanceIdVpnId_Object = MibTableColumn
cadL2vpnInstanceIdVpnId = _CadL2vpnInstanceIdVpnId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 4, 1, 5),
    _CadL2vpnInstanceIdVpnId_Type()
)
cadL2vpnInstanceIdVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnInstanceIdVpnId.setStatus("current")
_CadL2vpnIdxToCmVpnInstTable_Object = MibTable
cadL2vpnIdxToCmVpnInstTable = _CadL2vpnIdxToCmVpnInstTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cadL2vpnIdxToCmVpnInstTable.setStatus("current")
_CadL2vpnIdxToCmVpnInstEntry_Object = MibTableRow
cadL2vpnIdxToCmVpnInstEntry = _CadL2vpnIdxToCmVpnInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 6, 1)
)
cadL2vpnIdxToCmVpnInstEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnVpnIdx"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnInstanceId"),
)
if mibBuilder.loadTexts:
    cadL2vpnIdxToCmVpnInstEntry.setStatus("current")
_CadL2vpnVpnIdx_Type = DocsL2vpnIndex
_CadL2vpnVpnIdx_Object = MibTableColumn
cadL2vpnVpnIdx = _CadL2vpnVpnIdx_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 6, 1, 1),
    _CadL2vpnVpnIdx_Type()
)
cadL2vpnVpnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnVpnIdx.setStatus("current")
_CadL2vpnPktClassTable_Object = MibTable
cadL2vpnPktClassTable = _CadL2vpnPktClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cadL2vpnPktClassTable.setStatus("current")
_CadL2vpnPktClassEntry_Object = MibTableRow
cadL2vpnPktClassEntry = _CadL2vpnPktClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1)
)
cadL2vpnPktClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS3-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    cadL2vpnPktClassEntry.setStatus("current")
_CadL2vpnPktClassL2vpnId_Type = DocsL2vpnIdentifier
_CadL2vpnPktClassL2vpnId_Object = MibTableColumn
cadL2vpnPktClassL2vpnId = _CadL2vpnPktClassL2vpnId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 1),
    _CadL2vpnPktClassL2vpnId_Type()
)
cadL2vpnPktClassL2vpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnPktClassL2vpnId.setStatus("current")


class _CadL2vpnPktClassUserPriRangeLow_Type(Unsigned32):
    """Custom type cadL2vpnPktClassUserPriRangeLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CadL2vpnPktClassUserPriRangeLow_Type.__name__ = "Unsigned32"
_CadL2vpnPktClassUserPriRangeLow_Object = MibTableColumn
cadL2vpnPktClassUserPriRangeLow = _CadL2vpnPktClassUserPriRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 2),
    _CadL2vpnPktClassUserPriRangeLow_Type()
)
cadL2vpnPktClassUserPriRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnPktClassUserPriRangeLow.setStatus("current")


class _CadL2vpnPktClassUserPriRangeHigh_Type(Unsigned32):
    """Custom type cadL2vpnPktClassUserPriRangeHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CadL2vpnPktClassUserPriRangeHigh_Type.__name__ = "Unsigned32"
_CadL2vpnPktClassUserPriRangeHigh_Object = MibTableColumn
cadL2vpnPktClassUserPriRangeHigh = _CadL2vpnPktClassUserPriRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 3),
    _CadL2vpnPktClassUserPriRangeHigh_Type()
)
cadL2vpnPktClassUserPriRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnPktClassUserPriRangeHigh.setStatus("current")
_CadL2vpnPktClassCMIM_Type = DocsL2vpnIfList
_CadL2vpnPktClassCMIM_Object = MibTableColumn
cadL2vpnPktClassCMIM = _CadL2vpnPktClassCMIM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 4),
    _CadL2vpnPktClassCMIM_Type()
)
cadL2vpnPktClassCMIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnPktClassCMIM.setStatus("current")
_CadL2vpnPktClassVendorSpecific_Type = OctetString
_CadL2vpnPktClassVendorSpecific_Object = MibTableColumn
cadL2vpnPktClassVendorSpecific = _CadL2vpnPktClassVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 8, 1, 5),
    _CadL2vpnPktClassVendorSpecific_Type()
)
cadL2vpnPktClassVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadL2vpnPktClassVendorSpecific.setStatus("current")
_CadL2vpnDenyForwardingTable_Object = MibTable
cadL2vpnDenyForwardingTable = _CadL2vpnDenyForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingTable.setStatus("current")
_CadL2vpnDenyForwardingEntry_Object = MibTableRow
cadL2vpnDenyForwardingEntry = _CadL2vpnDenyForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1)
)
cadL2vpnDenyForwardingEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnDenyForwardingIndex"),
)
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingEntry.setStatus("current")
_CadL2vpnDenyForwardingIndex_Type = Unsigned32
_CadL2vpnDenyForwardingIndex_Object = MibTableColumn
cadL2vpnDenyForwardingIndex = _CadL2vpnDenyForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 1),
    _CadL2vpnDenyForwardingIndex_Type()
)
cadL2vpnDenyForwardingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingIndex.setStatus("current")


class _CadL2vpnDenyForwardingVpnId_Type(OctetString):
    """Custom type cadL2vpnDenyForwardingVpnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadL2vpnDenyForwardingVpnId_Type.__name__ = "OctetString"
_CadL2vpnDenyForwardingVpnId_Object = MibTableColumn
cadL2vpnDenyForwardingVpnId = _CadL2vpnDenyForwardingVpnId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 2),
    _CadL2vpnDenyForwardingVpnId_Type()
)
cadL2vpnDenyForwardingVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingVpnId.setStatus("current")


class _CadL2vpnDenyForwardingInstanceId_Type(Integer32):
    """Custom type cadL2vpnDenyForwardingInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CadL2vpnDenyForwardingInstanceId_Type.__name__ = "Integer32"
_CadL2vpnDenyForwardingInstanceId_Object = MibTableColumn
cadL2vpnDenyForwardingInstanceId = _CadL2vpnDenyForwardingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 3),
    _CadL2vpnDenyForwardingInstanceId_Type()
)
cadL2vpnDenyForwardingInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingInstanceId.setStatus("current")
_CadL2vpnDenyForwardingCmMac_Type = MacAddress
_CadL2vpnDenyForwardingCmMac_Object = MibTableColumn
cadL2vpnDenyForwardingCmMac = _CadL2vpnDenyForwardingCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 4),
    _CadL2vpnDenyForwardingCmMac_Type()
)
cadL2vpnDenyForwardingCmMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingCmMac.setStatus("current")
_CadL2vpnDenyForwardingRowStatus_Type = RowStatus
_CadL2vpnDenyForwardingRowStatus_Object = MibTableColumn
cadL2vpnDenyForwardingRowStatus = _CadL2vpnDenyForwardingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 5),
    _CadL2vpnDenyForwardingRowStatus_Type()
)
cadL2vpnDenyForwardingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingRowStatus.setStatus("current")
_CadL2vpnDenyForwardingMplsPeerIp_Type = InetAddress
_CadL2vpnDenyForwardingMplsPeerIp_Object = MibTableColumn
cadL2vpnDenyForwardingMplsPeerIp = _CadL2vpnDenyForwardingMplsPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 9, 1, 6),
    _CadL2vpnDenyForwardingMplsPeerIp_Type()
)
cadL2vpnDenyForwardingMplsPeerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnDenyForwardingMplsPeerIp.setStatus("current")
_CerL2vpnCmVpnIdTable_Object = MibTable
cerL2vpnCmVpnIdTable = _CerL2vpnCmVpnIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cerL2vpnCmVpnIdTable.setStatus("current")
_CerL2vpnCmVpnIdEntry_Object = MibTableRow
cerL2vpnCmVpnIdEntry = _CerL2vpnCmVpnIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1)
)
cerL2vpnCmVpnIdEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmVpnId"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmNsiEncapSubtype"),
)
if mibBuilder.loadTexts:
    cerL2vpnCmVpnIdEntry.setStatus("current")
_CerL2vpnCmMac_Type = MacAddress
_CerL2vpnCmMac_Object = MibTableColumn
cerL2vpnCmMac = _CerL2vpnCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 1),
    _CerL2vpnCmMac_Type()
)
cerL2vpnCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerL2vpnCmMac.setStatus("current")
_CerL2vpnCmVpnId_Type = DocsL2vpnIdentifier
_CerL2vpnCmVpnId_Object = MibTableColumn
cerL2vpnCmVpnId = _CerL2vpnCmVpnId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 2),
    _CerL2vpnCmVpnId_Type()
)
cerL2vpnCmVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmVpnId.setStatus("current")
_CerL2vpnCmNsiEncapSubtype_Type = DocsNsiEncapSubtype
_CerL2vpnCmNsiEncapSubtype_Object = MibTableColumn
cerL2vpnCmNsiEncapSubtype = _CerL2vpnCmNsiEncapSubtype_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 3),
    _CerL2vpnCmNsiEncapSubtype_Type()
)
cerL2vpnCmNsiEncapSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmNsiEncapSubtype.setStatus("current")
_CerL2vpnIdx_Type = DocsL2vpnIndex
_CerL2vpnIdx_Object = MibTableColumn
cerL2vpnIdx = _CerL2vpnIdx_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 4),
    _CerL2vpnIdx_Type()
)
cerL2vpnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnIdx.setStatus("current")
_CerL2vpnCmForwardingEnabled_Type = TruthValue
_CerL2vpnCmForwardingEnabled_Object = MibTableColumn
cerL2vpnCmForwardingEnabled = _CerL2vpnCmForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 5),
    _CerL2vpnCmForwardingEnabled_Type()
)
cerL2vpnCmForwardingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmForwardingEnabled.setStatus("current")


class _CerL2vpnInstanceId_Type(Integer32):
    """Custom type cerL2vpnInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CerL2vpnInstanceId_Type.__name__ = "Integer32"
_CerL2vpnInstanceId_Object = MibTableColumn
cerL2vpnInstanceId = _CerL2vpnInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 6),
    _CerL2vpnInstanceId_Type()
)
cerL2vpnInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerL2vpnInstanceId.setStatus("current")


class _CerL2vpnInstanceOuterVlanId_Type(Integer32):
    """Custom type cerL2vpnInstanceOuterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_CerL2vpnInstanceOuterVlanId_Type.__name__ = "Integer32"
_CerL2vpnInstanceOuterVlanId_Object = MibTableColumn
cerL2vpnInstanceOuterVlanId = _CerL2vpnInstanceOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 7),
    _CerL2vpnInstanceOuterVlanId_Type()
)
cerL2vpnInstanceOuterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnInstanceOuterVlanId.setStatus("current")


class _CerL2vpnInstanceInnerVlanId_Type(Integer32):
    """Custom type cerL2vpnInstanceInnerVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CerL2vpnInstanceInnerVlanId_Type.__name__ = "Integer32"
_CerL2vpnInstanceInnerVlanId_Object = MibTableColumn
cerL2vpnInstanceInnerVlanId = _CerL2vpnInstanceInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 8),
    _CerL2vpnInstanceInnerVlanId_Type()
)
cerL2vpnInstanceInnerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnInstanceInnerVlanId.setStatus("current")


class _CerL2vpnInstanceNsiEncapSubType_Type(Integer32):
    """Custom type cerL2vpnInstanceNsiEncapSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual-qtag", 2),
          ("not-applicable", 0),
          ("single-qtag", 1))
    )


_CerL2vpnInstanceNsiEncapSubType_Type.__name__ = "Integer32"
_CerL2vpnInstanceNsiEncapSubType_Object = MibTableColumn
cerL2vpnInstanceNsiEncapSubType = _CerL2vpnInstanceNsiEncapSubType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 9),
    _CerL2vpnInstanceNsiEncapSubType_Type()
)
cerL2vpnInstanceNsiEncapSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnInstanceNsiEncapSubType.setStatus("current")
_CerL2vpnCmCompliantCapability_Type = TruthValue
_CerL2vpnCmCompliantCapability_Object = MibTableColumn
cerL2vpnCmCompliantCapability = _CerL2vpnCmCompliantCapability_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 10),
    _CerL2vpnCmCompliantCapability_Type()
)
cerL2vpnCmCompliantCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmCompliantCapability.setStatus("current")
_CerL2vpnCmDutFilteringCapability_Type = TruthValue
_CerL2vpnCmDutFilteringCapability_Object = MibTableColumn
cerL2vpnCmDutFilteringCapability = _CerL2vpnCmDutFilteringCapability_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 11),
    _CerL2vpnCmDutFilteringCapability_Type()
)
cerL2vpnCmDutFilteringCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmDutFilteringCapability.setStatus("current")
_CerL2vpnCmDutCMIM_Type = DocsL2vpnIfList
_CerL2vpnCmDutCMIM_Object = MibTableColumn
cerL2vpnCmDutCMIM = _CerL2vpnCmDutCMIM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 12),
    _CerL2vpnCmDutCMIM_Type()
)
cerL2vpnCmDutCMIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmDutCMIM.setStatus("current")
_CerL2vpnCmDhcpSnooping_Type = DocsL2vpnIfList
_CerL2vpnCmDhcpSnooping_Object = MibTableColumn
cerL2vpnCmDhcpSnooping = _CerL2vpnCmDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 13),
    _CerL2vpnCmDhcpSnooping_Type()
)
cerL2vpnCmDhcpSnooping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmDhcpSnooping.setStatus("current")
_CerL2vpnVpnCmCMIM_Type = DocsL2vpnIfList
_CerL2vpnVpnCmCMIM_Object = MibTableColumn
cerL2vpnVpnCmCMIM = _CerL2vpnVpnCmCMIM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 14),
    _CerL2vpnVpnCmCMIM_Type()
)
cerL2vpnVpnCmCMIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnVpnCmCMIM.setStatus("current")


class _CerL2vpnVpnCmIndividualSAID_Type(Integer32):
    """Custom type cerL2vpnVpnCmIndividualSAID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CerL2vpnVpnCmIndividualSAID_Type.__name__ = "Integer32"
_CerL2vpnVpnCmIndividualSAID_Object = MibTableColumn
cerL2vpnVpnCmIndividualSAID = _CerL2vpnVpnCmIndividualSAID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 15),
    _CerL2vpnVpnCmIndividualSAID_Type()
)
cerL2vpnVpnCmIndividualSAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnVpnCmIndividualSAID.setStatus("current")
_CerL2vpnVpnCmVendorSpecific_Type = OctetString
_CerL2vpnVpnCmVendorSpecific_Object = MibTableColumn
cerL2vpnVpnCmVendorSpecific = _CerL2vpnVpnCmVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 16),
    _CerL2vpnVpnCmVendorSpecific_Type()
)
cerL2vpnVpnCmVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnVpnCmVendorSpecific.setStatus("current")
_CerL2vpnCmNsiEncapValue_Type = CadNsiEncapValue
_CerL2vpnCmNsiEncapValue_Object = MibTableColumn
cerL2vpnCmNsiEncapValue = _CerL2vpnCmNsiEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 17),
    _CerL2vpnCmNsiEncapValue_Type()
)
cerL2vpnCmNsiEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmNsiEncapValue.setStatus("current")


class _CerL2vpnMplsAcId_Type(Unsigned32):
    """Custom type cerL2vpnMplsAcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CerL2vpnMplsAcId_Type.__name__ = "Unsigned32"
_CerL2vpnMplsAcId_Object = MibTableColumn
cerL2vpnMplsAcId = _CerL2vpnMplsAcId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 18),
    _CerL2vpnMplsAcId_Type()
)
cerL2vpnMplsAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnMplsAcId.setStatus("current")


class _CerL2vpnCmMplsPwId_Type(Unsigned32):
    """Custom type cerL2vpnCmMplsPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CerL2vpnCmMplsPwId_Type.__name__ = "Unsigned32"
_CerL2vpnCmMplsPwId_Object = MibTableColumn
cerL2vpnCmMplsPwId = _CerL2vpnCmMplsPwId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 19),
    _CerL2vpnCmMplsPwId_Type()
)
cerL2vpnCmMplsPwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmMplsPwId.setStatus("current")
_CerL2vpnCmMplsPeerAddrType_Type = InetAddressType
_CerL2vpnCmMplsPeerAddrType_Object = MibTableColumn
cerL2vpnCmMplsPeerAddrType = _CerL2vpnCmMplsPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 20),
    _CerL2vpnCmMplsPeerAddrType_Type()
)
cerL2vpnCmMplsPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmMplsPeerAddrType.setStatus("current")
_CerL2vpnCmMplsPeerAddr_Type = InetAddress
_CerL2vpnCmMplsPeerAddr_Object = MibTableColumn
cerL2vpnCmMplsPeerAddr = _CerL2vpnCmMplsPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 21),
    _CerL2vpnCmMplsPeerAddr_Type()
)
cerL2vpnCmMplsPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmMplsPeerAddr.setStatus("current")


class _CerL2vpnCmBgpVpnId_Type(Unsigned32):
    """Custom type cerL2vpnCmBgpVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CerL2vpnCmBgpVpnId_Type.__name__ = "Unsigned32"
_CerL2vpnCmBgpVpnId_Object = MibTableColumn
cerL2vpnCmBgpVpnId = _CerL2vpnCmBgpVpnId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 22),
    _CerL2vpnCmBgpVpnId_Type()
)
cerL2vpnCmBgpVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmBgpVpnId.setStatus("current")


class _CerL2vpnCmBgpRd_Type(OctetString):
    """Custom type cerL2vpnCmBgpRd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CerL2vpnCmBgpRd_Type.__name__ = "OctetString"
_CerL2vpnCmBgpRd_Object = MibTableColumn
cerL2vpnCmBgpRd = _CerL2vpnCmBgpRd_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 23),
    _CerL2vpnCmBgpRd_Type()
)
cerL2vpnCmBgpRd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmBgpRd.setStatus("current")


class _CerL2vpnCmBgpRtImport_Type(OctetString):
    """Custom type cerL2vpnCmBgpRtImport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CerL2vpnCmBgpRtImport_Type.__name__ = "OctetString"
_CerL2vpnCmBgpRtImport_Object = MibTableColumn
cerL2vpnCmBgpRtImport = _CerL2vpnCmBgpRtImport_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 24),
    _CerL2vpnCmBgpRtImport_Type()
)
cerL2vpnCmBgpRtImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmBgpRtImport.setStatus("current")


class _CerL2vpnCmBgpRtExport_Type(OctetString):
    """Custom type cerL2vpnCmBgpRtExport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CerL2vpnCmBgpRtExport_Type.__name__ = "OctetString"
_CerL2vpnCmBgpRtExport_Object = MibTableColumn
cerL2vpnCmBgpRtExport = _CerL2vpnCmBgpRtExport_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 25),
    _CerL2vpnCmBgpRtExport_Type()
)
cerL2vpnCmBgpRtExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmBgpRtExport.setStatus("current")


class _CerL2vpnCmBgpCeVeId_Type(Unsigned32):
    """Custom type cerL2vpnCmBgpCeVeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CerL2vpnCmBgpCeVeId_Type.__name__ = "Unsigned32"
_CerL2vpnCmBgpCeVeId_Object = MibTableColumn
cerL2vpnCmBgpCeVeId = _CerL2vpnCmBgpCeVeId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 10, 1, 26),
    _CerL2vpnCmBgpCeVeId_Type()
)
cerL2vpnCmBgpCeVeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmBgpCeVeId.setStatus("current")
_CerL2vpnCmStatsTable_Object = MibTable
cerL2vpnCmStatsTable = _CerL2vpnCmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cerL2vpnCmStatsTable.setStatus("current")
_CerL2vpnCmStatsEntry_Object = MibTableRow
cerL2vpnCmStatsEntry = _CerL2vpnCmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1)
)
cerL2vpnCmStatsEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmVpnId"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmNsiEncapSubtype"),
)
if mibBuilder.loadTexts:
    cerL2vpnCmStatsEntry.setStatus("current")
_CerL2vpnCmStatsUpstreamPkts_Type = Counter32
_CerL2vpnCmStatsUpstreamPkts_Object = MibTableColumn
cerL2vpnCmStatsUpstreamPkts = _CerL2vpnCmStatsUpstreamPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 1),
    _CerL2vpnCmStatsUpstreamPkts_Type()
)
cerL2vpnCmStatsUpstreamPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmStatsUpstreamPkts.setStatus("current")
_CerL2vpnCmStatsUpstreamBytes_Type = Counter32
_CerL2vpnCmStatsUpstreamBytes_Object = MibTableColumn
cerL2vpnCmStatsUpstreamBytes = _CerL2vpnCmStatsUpstreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 2),
    _CerL2vpnCmStatsUpstreamBytes_Type()
)
cerL2vpnCmStatsUpstreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmStatsUpstreamBytes.setStatus("current")
_CerL2vpnCmStatsUpstreamDiscards_Type = Counter32
_CerL2vpnCmStatsUpstreamDiscards_Object = MibTableColumn
cerL2vpnCmStatsUpstreamDiscards = _CerL2vpnCmStatsUpstreamDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 3),
    _CerL2vpnCmStatsUpstreamDiscards_Type()
)
cerL2vpnCmStatsUpstreamDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmStatsUpstreamDiscards.setStatus("current")
_CerL2vpnCmStatsDownstreamPkts_Type = Counter32
_CerL2vpnCmStatsDownstreamPkts_Object = MibTableColumn
cerL2vpnCmStatsDownstreamPkts = _CerL2vpnCmStatsDownstreamPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 4),
    _CerL2vpnCmStatsDownstreamPkts_Type()
)
cerL2vpnCmStatsDownstreamPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmStatsDownstreamPkts.setStatus("current")
_CerL2vpnCmStatsDownstreamBytes_Type = Counter32
_CerL2vpnCmStatsDownstreamBytes_Object = MibTableColumn
cerL2vpnCmStatsDownstreamBytes = _CerL2vpnCmStatsDownstreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 5),
    _CerL2vpnCmStatsDownstreamBytes_Type()
)
cerL2vpnCmStatsDownstreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmStatsDownstreamBytes.setStatus("current")
_CerL2vpnCmStatsDownstreamDiscards_Type = Counter32
_CerL2vpnCmStatsDownstreamDiscards_Object = MibTableColumn
cerL2vpnCmStatsDownstreamDiscards = _CerL2vpnCmStatsDownstreamDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 11, 1, 6),
    _CerL2vpnCmStatsDownstreamDiscards_Type()
)
cerL2vpnCmStatsDownstreamDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmStatsDownstreamDiscards.setStatus("current")
_CadL2vpnMplsPeerIpToCmTable_Object = MibTable
cadL2vpnMplsPeerIpToCmTable = _CadL2vpnMplsPeerIpToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cadL2vpnMplsPeerIpToCmTable.setStatus("current")
_CadL2vpnMplsPeerIpToCmEntry_Object = MibTableRow
cadL2vpnMplsPeerIpToCmEntry = _CadL2vpnMplsPeerIpToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 12, 1)
)
cadL2vpnMplsPeerIpToCmEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMplsPeerAddrType"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMplsPeerIpAddress"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmMac"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmVpnId"),
    (0, "CADANT-L2VPN-MIB", "cerL2vpnCmNsiEncapSubtype"),
)
if mibBuilder.loadTexts:
    cadL2vpnMplsPeerIpToCmEntry.setStatus("current")
_CerL2vpnCmMplsPeerIpAddress_Type = InetAddress
_CerL2vpnCmMplsPeerIpAddress_Object = MibTableColumn
cerL2vpnCmMplsPeerIpAddress = _CerL2vpnCmMplsPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 12, 1, 2),
    _CerL2vpnCmMplsPeerIpAddress_Type()
)
cerL2vpnCmMplsPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerL2vpnCmMplsPeerIpAddress.setStatus("current")
_CadL2vpnProvisionedCmTable_Object = MibTable
cadL2vpnProvisionedCmTable = _CadL2vpnProvisionedCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmTable.setStatus("current")
_CadL2vpnProvisionedCmEntry_Object = MibTableRow
cadL2vpnProvisionedCmEntry = _CadL2vpnProvisionedCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1)
)
cadL2vpnProvisionedCmEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnProvisionedCmMacAddress"),
)
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmEntry.setStatus("current")
_CadL2vpnProvisionedCmMacAddress_Type = MacAddress
_CadL2vpnProvisionedCmMacAddress_Object = MibTableColumn
cadL2vpnProvisionedCmMacAddress = _CadL2vpnProvisionedCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 1),
    _CadL2vpnProvisionedCmMacAddress_Type()
)
cadL2vpnProvisionedCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmMacAddress.setStatus("current")
_CadL2vpnProvisionedCmL2vpnId_Type = DocsL2vpnIdentifier
_CadL2vpnProvisionedCmL2vpnId_Object = MibTableColumn
cadL2vpnProvisionedCmL2vpnId = _CadL2vpnProvisionedCmL2vpnId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 2),
    _CadL2vpnProvisionedCmL2vpnId_Type()
)
cadL2vpnProvisionedCmL2vpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmL2vpnId.setStatus("current")


class _CadL2vpnProvisionedCmOuterVlanId_Type(Integer32):
    """Custom type cadL2vpnProvisionedCmOuterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_CadL2vpnProvisionedCmOuterVlanId_Type.__name__ = "Integer32"
_CadL2vpnProvisionedCmOuterVlanId_Object = MibTableColumn
cadL2vpnProvisionedCmOuterVlanId = _CadL2vpnProvisionedCmOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 3),
    _CadL2vpnProvisionedCmOuterVlanId_Type()
)
cadL2vpnProvisionedCmOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmOuterVlanId.setStatus("current")


class _CadL2vpnProvisionedCmInnerVlanId_Type(Integer32):
    """Custom type cadL2vpnProvisionedCmInnerVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CadL2vpnProvisionedCmInnerVlanId_Type.__name__ = "Integer32"
_CadL2vpnProvisionedCmInnerVlanId_Object = MibTableColumn
cadL2vpnProvisionedCmInnerVlanId = _CadL2vpnProvisionedCmInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 4),
    _CadL2vpnProvisionedCmInnerVlanId_Type()
)
cadL2vpnProvisionedCmInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmInnerVlanId.setStatus("current")
_CadL2vpnProvisionedCmRowStatus_Type = RowStatus
_CadL2vpnProvisionedCmRowStatus_Object = MibTableColumn
cadL2vpnProvisionedCmRowStatus = _CadL2vpnProvisionedCmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 13, 1, 5),
    _CadL2vpnProvisionedCmRowStatus_Type()
)
cadL2vpnProvisionedCmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmRowStatus.setStatus("current")
_CadL2vpnProvisionedCmEsafeTable_Object = MibTable
cadL2vpnProvisionedCmEsafeTable = _CadL2vpnProvisionedCmEsafeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmEsafeTable.setStatus("current")
_CadL2vpnProvisionedCmEsafeEntry_Object = MibTableRow
cadL2vpnProvisionedCmEsafeEntry = _CadL2vpnProvisionedCmEsafeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1)
)
cadL2vpnProvisionedCmEsafeEntry.setIndexNames(
    (0, "CADANT-L2VPN-MIB", "cadL2vpnProvisionedCmMacAddress"),
    (0, "CADANT-L2VPN-MIB", "cadL2vpnProvisionedCmEsafeMacAddress"),
)
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmEsafeEntry.setStatus("current")
_CadL2vpnProvisionedCmEsafeMacAddress_Type = MacAddress
_CadL2vpnProvisionedCmEsafeMacAddress_Object = MibTableColumn
cadL2vpnProvisionedCmEsafeMacAddress = _CadL2vpnProvisionedCmEsafeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1, 1),
    _CadL2vpnProvisionedCmEsafeMacAddress_Type()
)
cadL2vpnProvisionedCmEsafeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmEsafeMacAddress.setStatus("current")


class _CadL2vpnProvisionedCmEsafeIfIndex_Type(Integer32):
    """Custom type cadL2vpnProvisionedCmEsafeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              19)
        )
    )
    namedValues = NamedValues(
        *(("mta", 16),
          ("stb", 17),
          ("tea", 19))
    )


_CadL2vpnProvisionedCmEsafeIfIndex_Type.__name__ = "Integer32"
_CadL2vpnProvisionedCmEsafeIfIndex_Object = MibTableColumn
cadL2vpnProvisionedCmEsafeIfIndex = _CadL2vpnProvisionedCmEsafeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1, 2),
    _CadL2vpnProvisionedCmEsafeIfIndex_Type()
)
cadL2vpnProvisionedCmEsafeIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmEsafeIfIndex.setStatus("current")
_CadL2vpnProvisionedCmEsafeRowStatus_Type = RowStatus
_CadL2vpnProvisionedCmEsafeRowStatus_Object = MibTableColumn
cadL2vpnProvisionedCmEsafeRowStatus = _CadL2vpnProvisionedCmEsafeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120, 1, 1, 14, 1, 3),
    _CadL2vpnProvisionedCmEsafeRowStatus_Type()
)
cadL2vpnProvisionedCmEsafeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadL2vpnProvisionedCmEsafeRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-L2VPN-MIB",
    **{"CadNsiEncapValue": CadNsiEncapValue,
       "cadL2vpnMIB": cadL2vpnMIB,
       "cadL2vpnMIBObjects": cadL2vpnMIBObjects,
       "cadL2vpnParams": cadL2vpnParams,
       "cadL2vpnPrimaryNetworkIfIndex": cadL2vpnPrimaryNetworkIfIndex,
       "cadL2vpnSecondaryNetworkIfIndex": cadL2vpnSecondaryNetworkIfIndex,
       "cadL2vpnActiveNetworkIfIndex": cadL2vpnActiveNetworkIfIndex,
       "cadL2vpnForwardingEnabled": cadL2vpnForwardingEnabled,
       "cadL2vpnCmCapEsafeIdentRequired": cadL2vpnCmCapEsafeIdentRequired,
       "cadL2vpnCmCapDutFilterRequired": cadL2vpnCmCapDutFilterRequired,
       "cadL2vpnGlobalTpid": cadL2vpnGlobalTpid,
       "cadL2vpnInterfaceTable": cadL2vpnInterfaceTable,
       "cadL2vpnInterfaceEntry": cadL2vpnInterfaceEntry,
       "cadL2vpnInterfaceIfIndex": cadL2vpnInterfaceIfIndex,
       "cadL2vpnInterfaceIpIgmpSnooping": cadL2vpnInterfaceIpIgmpSnooping,
       "cadL2vpnInterfaceRowStatus": cadL2vpnInterfaceRowStatus,
       "cadL2vpnVlanIdRangeTable": cadL2vpnVlanIdRangeTable,
       "cadL2vpnVlanIdRangeEntry": cadL2vpnVlanIdRangeEntry,
       "cadL2vpnVlanIdRangeBegin": cadL2vpnVlanIdRangeBegin,
       "cadL2vpnVlanIdRangeEnd": cadL2vpnVlanIdRangeEnd,
       "cadL2vpnVlanIdRangeNsiEncapSubtype": cadL2vpnVlanIdRangeNsiEncapSubtype,
       "cadL2vpnVlanIdRangeRowStatus": cadL2vpnVlanIdRangeRowStatus,
       "cadL2vpnInstanceIdToCmTable": cadL2vpnInstanceIdToCmTable,
       "cadL2vpnInstanceIdToCmEntry": cadL2vpnInstanceIdToCmEntry,
       "cadL2vpnInstanceId": cadL2vpnInstanceId,
       "cadL2vpnInstanceIdVlanIdOuter": cadL2vpnInstanceIdVlanIdOuter,
       "cadL2vpnInstanceIdVlanIdInner": cadL2vpnInstanceIdVlanIdInner,
       "cadL2vpnInstanceIdCmMac": cadL2vpnInstanceIdCmMac,
       "cadL2vpnInstanceIdVpnId": cadL2vpnInstanceIdVpnId,
       "cadL2vpnIdxToCmVpnInstTable": cadL2vpnIdxToCmVpnInstTable,
       "cadL2vpnIdxToCmVpnInstEntry": cadL2vpnIdxToCmVpnInstEntry,
       "cadL2vpnVpnIdx": cadL2vpnVpnIdx,
       "cadL2vpnPktClassTable": cadL2vpnPktClassTable,
       "cadL2vpnPktClassEntry": cadL2vpnPktClassEntry,
       "cadL2vpnPktClassL2vpnId": cadL2vpnPktClassL2vpnId,
       "cadL2vpnPktClassUserPriRangeLow": cadL2vpnPktClassUserPriRangeLow,
       "cadL2vpnPktClassUserPriRangeHigh": cadL2vpnPktClassUserPriRangeHigh,
       "cadL2vpnPktClassCMIM": cadL2vpnPktClassCMIM,
       "cadL2vpnPktClassVendorSpecific": cadL2vpnPktClassVendorSpecific,
       "cadL2vpnDenyForwardingTable": cadL2vpnDenyForwardingTable,
       "cadL2vpnDenyForwardingEntry": cadL2vpnDenyForwardingEntry,
       "cadL2vpnDenyForwardingIndex": cadL2vpnDenyForwardingIndex,
       "cadL2vpnDenyForwardingVpnId": cadL2vpnDenyForwardingVpnId,
       "cadL2vpnDenyForwardingInstanceId": cadL2vpnDenyForwardingInstanceId,
       "cadL2vpnDenyForwardingCmMac": cadL2vpnDenyForwardingCmMac,
       "cadL2vpnDenyForwardingRowStatus": cadL2vpnDenyForwardingRowStatus,
       "cadL2vpnDenyForwardingMplsPeerIp": cadL2vpnDenyForwardingMplsPeerIp,
       "cerL2vpnCmVpnIdTable": cerL2vpnCmVpnIdTable,
       "cerL2vpnCmVpnIdEntry": cerL2vpnCmVpnIdEntry,
       "cerL2vpnCmMac": cerL2vpnCmMac,
       "cerL2vpnCmVpnId": cerL2vpnCmVpnId,
       "cerL2vpnCmNsiEncapSubtype": cerL2vpnCmNsiEncapSubtype,
       "cerL2vpnIdx": cerL2vpnIdx,
       "cerL2vpnCmForwardingEnabled": cerL2vpnCmForwardingEnabled,
       "cerL2vpnInstanceId": cerL2vpnInstanceId,
       "cerL2vpnInstanceOuterVlanId": cerL2vpnInstanceOuterVlanId,
       "cerL2vpnInstanceInnerVlanId": cerL2vpnInstanceInnerVlanId,
       "cerL2vpnInstanceNsiEncapSubType": cerL2vpnInstanceNsiEncapSubType,
       "cerL2vpnCmCompliantCapability": cerL2vpnCmCompliantCapability,
       "cerL2vpnCmDutFilteringCapability": cerL2vpnCmDutFilteringCapability,
       "cerL2vpnCmDutCMIM": cerL2vpnCmDutCMIM,
       "cerL2vpnCmDhcpSnooping": cerL2vpnCmDhcpSnooping,
       "cerL2vpnVpnCmCMIM": cerL2vpnVpnCmCMIM,
       "cerL2vpnVpnCmIndividualSAID": cerL2vpnVpnCmIndividualSAID,
       "cerL2vpnVpnCmVendorSpecific": cerL2vpnVpnCmVendorSpecific,
       "cerL2vpnCmNsiEncapValue": cerL2vpnCmNsiEncapValue,
       "cerL2vpnMplsAcId": cerL2vpnMplsAcId,
       "cerL2vpnCmMplsPwId": cerL2vpnCmMplsPwId,
       "cerL2vpnCmMplsPeerAddrType": cerL2vpnCmMplsPeerAddrType,
       "cerL2vpnCmMplsPeerAddr": cerL2vpnCmMplsPeerAddr,
       "cerL2vpnCmBgpVpnId": cerL2vpnCmBgpVpnId,
       "cerL2vpnCmBgpRd": cerL2vpnCmBgpRd,
       "cerL2vpnCmBgpRtImport": cerL2vpnCmBgpRtImport,
       "cerL2vpnCmBgpRtExport": cerL2vpnCmBgpRtExport,
       "cerL2vpnCmBgpCeVeId": cerL2vpnCmBgpCeVeId,
       "cerL2vpnCmStatsTable": cerL2vpnCmStatsTable,
       "cerL2vpnCmStatsEntry": cerL2vpnCmStatsEntry,
       "cerL2vpnCmStatsUpstreamPkts": cerL2vpnCmStatsUpstreamPkts,
       "cerL2vpnCmStatsUpstreamBytes": cerL2vpnCmStatsUpstreamBytes,
       "cerL2vpnCmStatsUpstreamDiscards": cerL2vpnCmStatsUpstreamDiscards,
       "cerL2vpnCmStatsDownstreamPkts": cerL2vpnCmStatsDownstreamPkts,
       "cerL2vpnCmStatsDownstreamBytes": cerL2vpnCmStatsDownstreamBytes,
       "cerL2vpnCmStatsDownstreamDiscards": cerL2vpnCmStatsDownstreamDiscards,
       "cadL2vpnMplsPeerIpToCmTable": cadL2vpnMplsPeerIpToCmTable,
       "cadL2vpnMplsPeerIpToCmEntry": cadL2vpnMplsPeerIpToCmEntry,
       "cerL2vpnCmMplsPeerIpAddress": cerL2vpnCmMplsPeerIpAddress,
       "cadL2vpnProvisionedCmTable": cadL2vpnProvisionedCmTable,
       "cadL2vpnProvisionedCmEntry": cadL2vpnProvisionedCmEntry,
       "cadL2vpnProvisionedCmMacAddress": cadL2vpnProvisionedCmMacAddress,
       "cadL2vpnProvisionedCmL2vpnId": cadL2vpnProvisionedCmL2vpnId,
       "cadL2vpnProvisionedCmOuterVlanId": cadL2vpnProvisionedCmOuterVlanId,
       "cadL2vpnProvisionedCmInnerVlanId": cadL2vpnProvisionedCmInnerVlanId,
       "cadL2vpnProvisionedCmRowStatus": cadL2vpnProvisionedCmRowStatus,
       "cadL2vpnProvisionedCmEsafeTable": cadL2vpnProvisionedCmEsafeTable,
       "cadL2vpnProvisionedCmEsafeEntry": cadL2vpnProvisionedCmEsafeEntry,
       "cadL2vpnProvisionedCmEsafeMacAddress": cadL2vpnProvisionedCmEsafeMacAddress,
       "cadL2vpnProvisionedCmEsafeIfIndex": cadL2vpnProvisionedCmEsafeIfIndex,
       "cadL2vpnProvisionedCmEsafeRowStatus": cadL2vpnProvisionedCmEsafeRowStatus}
)
