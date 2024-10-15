# SNMP MIB module (STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:57 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(HpSwitchPortType,
 VidList) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "HpSwitchPortType",
    "VidList")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class VlanID(Integer32):
    """Custom type VlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchStatistics_ObjectIdentity = ObjectIdentity
hpSwitchStatistics = _HpSwitchStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9)
)
_HpSwitchIpxStat_ObjectIdentity = ObjectIdentity
hpSwitchIpxStat = _HpSwitchIpxStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1)
)
_HpSwitchIpxStatTable_Object = MibTable
hpSwitchIpxStatTable = _HpSwitchIpxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchIpxStatTable.setStatus("mandatory")
_HpSwitchIpxStatEntry_Object = MibTableRow
hpSwitchIpxStatEntry = _HpSwitchIpxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1)
)
hpSwitchIpxStatEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchIpxStatIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchIpxStatEntry.setStatus("mandatory")
_HpSwitchIpxStatIndex_Type = VlanID
_HpSwitchIpxStatIndex_Object = MibTableColumn
hpSwitchIpxStatIndex = _HpSwitchIpxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 1),
    _HpSwitchIpxStatIndex_Type()
)
hpSwitchIpxStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpxStatIndex.setStatus("mandatory")
_HpSwitchIpxStatNodeAddr_Type = MacAddress
_HpSwitchIpxStatNodeAddr_Object = MibTableColumn
hpSwitchIpxStatNodeAddr = _HpSwitchIpxStatNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 2),
    _HpSwitchIpxStatNodeAddr_Type()
)
hpSwitchIpxStatNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpxStatNodeAddr.setStatus("mandatory")
_HpSwitchIpxStatGatewayAddr_Type = MacAddress
_HpSwitchIpxStatGatewayAddr_Object = MibTableColumn
hpSwitchIpxStatGatewayAddr = _HpSwitchIpxStatGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 3),
    _HpSwitchIpxStatGatewayAddr_Type()
)
hpSwitchIpxStatGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpxStatGatewayAddr.setStatus("mandatory")


class _HpSwitchIpxStatGatewayEncap_Type(Integer32):
    """Custom type hpSwitchIpxStatGatewayEncap based on Integer32"""
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
        *(("ethernetII", 1),
          ("ieee8022", 2),
          ("ieee8023Raw", 4),
          ("noGateway", 5),
          ("snap", 3))
    )


_HpSwitchIpxStatGatewayEncap_Type.__name__ = "Integer32"
_HpSwitchIpxStatGatewayEncap_Object = MibTableColumn
hpSwitchIpxStatGatewayEncap = _HpSwitchIpxStatGatewayEncap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 4),
    _HpSwitchIpxStatGatewayEncap_Type()
)
hpSwitchIpxStatGatewayEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpxStatGatewayEncap.setStatus("mandatory")


class _HpSwitchIpxStatAdminStatus_Type(Integer32):
    """Custom type hpSwitchIpxStatAdminStatus based on Integer32"""
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


_HpSwitchIpxStatAdminStatus_Type.__name__ = "Integer32"
_HpSwitchIpxStatAdminStatus_Object = MibTableColumn
hpSwitchIpxStatAdminStatus = _HpSwitchIpxStatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 5),
    _HpSwitchIpxStatAdminStatus_Type()
)
hpSwitchIpxStatAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpxStatAdminStatus.setStatus("mandatory")
_HpSwitchIpStat_ObjectIdentity = ObjectIdentity
hpSwitchIpStat = _HpSwitchIpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2)
)


class _HpSwitchIpStatTimepAdminStatus_Type(Integer32):
    """Custom type hpSwitchIpStatTimepAdminStatus based on Integer32"""
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


_HpSwitchIpStatTimepAdminStatus_Type.__name__ = "Integer32"
_HpSwitchIpStatTimepAdminStatus_Object = MibScalar
hpSwitchIpStatTimepAdminStatus = _HpSwitchIpStatTimepAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 1),
    _HpSwitchIpStatTimepAdminStatus_Type()
)
hpSwitchIpStatTimepAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatTimepAdminStatus.setStatus("obsolete")
_HpSwitchIpStatTimepServerAddr_Type = IpAddress
_HpSwitchIpStatTimepServerAddr_Object = MibScalar
hpSwitchIpStatTimepServerAddr = _HpSwitchIpStatTimepServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 2),
    _HpSwitchIpStatTimepServerAddr_Type()
)
hpSwitchIpStatTimepServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatTimepServerAddr.setStatus("obsolete")


class _HpSwitchIpStatTimepPollInterval_Type(Integer32):
    """Custom type hpSwitchIpStatTimepPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIpStatTimepPollInterval_Type.__name__ = "Integer32"
_HpSwitchIpStatTimepPollInterval_Object = MibScalar
hpSwitchIpStatTimepPollInterval = _HpSwitchIpStatTimepPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 3),
    _HpSwitchIpStatTimepPollInterval_Type()
)
hpSwitchIpStatTimepPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatTimepPollInterval.setStatus("obsolete")
_HpSwitchIpStatTable_Object = MibTable
hpSwitchIpStatTable = _HpSwitchIpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4)
)
if mibBuilder.loadTexts:
    hpSwitchIpStatTable.setStatus("obsolete")
_HpSwitchIpStatEntry_Object = MibTableRow
hpSwitchIpStatEntry = _HpSwitchIpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1)
)
hpSwitchIpStatEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchIpStatIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchIpStatEntry.setStatus("obsolete")
_HpSwitchIpStatIndex_Type = VlanID
_HpSwitchIpStatIndex_Object = MibTableColumn
hpSwitchIpStatIndex = _HpSwitchIpStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 1),
    _HpSwitchIpStatIndex_Type()
)
hpSwitchIpStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatIndex.setStatus("obsolete")
_HpSwitchIpStatAddr_Type = IpAddress
_HpSwitchIpStatAddr_Object = MibTableColumn
hpSwitchIpStatAddr = _HpSwitchIpStatAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 2),
    _HpSwitchIpStatAddr_Type()
)
hpSwitchIpStatAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatAddr.setStatus("obsolete")
_HpSwitchIpStatMask_Type = IpAddress
_HpSwitchIpStatMask_Object = MibTableColumn
hpSwitchIpStatMask = _HpSwitchIpStatMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 3),
    _HpSwitchIpStatMask_Type()
)
hpSwitchIpStatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatMask.setStatus("obsolete")
_HpSwitchIpStatGatewayAddr_Type = IpAddress
_HpSwitchIpStatGatewayAddr_Object = MibTableColumn
hpSwitchIpStatGatewayAddr = _HpSwitchIpStatGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 4),
    _HpSwitchIpStatGatewayAddr_Type()
)
hpSwitchIpStatGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatGatewayAddr.setStatus("obsolete")


class _HpSwitchIpStatAdminStatus_Type(Integer32):
    """Custom type hpSwitchIpStatAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 3),
          ("disable", 2),
          ("enable", 1))
    )


_HpSwitchIpStatAdminStatus_Type.__name__ = "Integer32"
_HpSwitchIpStatAdminStatus_Object = MibTableColumn
hpSwitchIpStatAdminStatus = _HpSwitchIpStatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 5),
    _HpSwitchIpStatAdminStatus_Type()
)
hpSwitchIpStatAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpStatAdminStatus.setStatus("obsolete")
_HpSwitchFdbInfo_ObjectIdentity = ObjectIdentity
hpSwitchFdbInfo = _HpSwitchFdbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4)
)
_HpSwitchVlanFdbAddrTable_Object = MibTable
hpSwitchVlanFdbAddrTable = _HpSwitchVlanFdbAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    hpSwitchVlanFdbAddrTable.setStatus("mandatory")
_HpSwitchVlanFdbAddrEntry_Object = MibTableRow
hpSwitchVlanFdbAddrEntry = _HpSwitchVlanFdbAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1)
)
hpSwitchVlanFdbAddrEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchVlanFdbId"),
    (0, "STATISTICS-MIB", "hpSwitchVlanFdbAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchVlanFdbAddrEntry.setStatus("mandatory")
_HpSwitchVlanFdbId_Type = VlanID
_HpSwitchVlanFdbId_Object = MibTableColumn
hpSwitchVlanFdbId = _HpSwitchVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1, 1),
    _HpSwitchVlanFdbId_Type()
)
hpSwitchVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchVlanFdbId.setStatus("mandatory")
_HpSwitchVlanFdbAddress_Type = MacAddress
_HpSwitchVlanFdbAddress_Object = MibTableColumn
hpSwitchVlanFdbAddress = _HpSwitchVlanFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1, 2),
    _HpSwitchVlanFdbAddress_Type()
)
hpSwitchVlanFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchVlanFdbAddress.setStatus("mandatory")
_HpSwitchVlanFdbPort_Type = Integer32
_HpSwitchVlanFdbPort_Object = MibTableColumn
hpSwitchVlanFdbPort = _HpSwitchVlanFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1, 3),
    _HpSwitchVlanFdbPort_Type()
)
hpSwitchVlanFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchVlanFdbPort.setStatus("mandatory")
_HpSwitchPortFdbAddrTable_Object = MibTable
hpSwitchPortFdbAddrTable = _HpSwitchPortFdbAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    hpSwitchPortFdbAddrTable.setStatus("mandatory")
_HpSwitchPortFdbAddrEntry_Object = MibTableRow
hpSwitchPortFdbAddrEntry = _HpSwitchPortFdbAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1)
)
hpSwitchPortFdbAddrEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchPortFdbId"),
    (0, "STATISTICS-MIB", "hpSwitchPortFdbAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchPortFdbAddrEntry.setStatus("mandatory")
_HpSwitchPortFdbId_Type = Integer32
_HpSwitchPortFdbId_Object = MibTableColumn
hpSwitchPortFdbId = _HpSwitchPortFdbId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1, 1),
    _HpSwitchPortFdbId_Type()
)
hpSwitchPortFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortFdbId.setStatus("mandatory")
_HpSwitchPortFdbAddress_Type = MacAddress
_HpSwitchPortFdbAddress_Object = MibTableColumn
hpSwitchPortFdbAddress = _HpSwitchPortFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1, 2),
    _HpSwitchPortFdbAddress_Type()
)
hpSwitchPortFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortFdbAddress.setStatus("mandatory")
_HpSwitchPortFdbVlanId_Type = VlanID
_HpSwitchPortFdbVlanId_Object = MibTableColumn
hpSwitchPortFdbVlanId = _HpSwitchPortFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1, 3),
    _HpSwitchPortFdbVlanId_Type()
)
hpSwitchPortFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortFdbVlanId.setStatus("deprecated")
_HpSwitchPortFdbVidList_Type = VidList
_HpSwitchPortFdbVidList_Object = MibTableColumn
hpSwitchPortFdbVidList = _HpSwitchPortFdbVidList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1, 4),
    _HpSwitchPortFdbVidList_Type()
)
hpSwitchPortFdbVidList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortFdbVidList.setStatus("mandatory")
_HpSwitchStpStat_ObjectIdentity = ObjectIdentity
hpSwitchStpStat = _HpSwitchStpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 5)
)


class _HpSwitchStpStatAdminStatus_Type(Integer32):
    """Custom type hpSwitchStpStatAdminStatus based on Integer32"""
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


_HpSwitchStpStatAdminStatus_Type.__name__ = "Integer32"
_HpSwitchStpStatAdminStatus_Object = MibScalar
hpSwitchStpStatAdminStatus = _HpSwitchStpStatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 5, 1),
    _HpSwitchStpStatAdminStatus_Type()
)
hpSwitchStpStatAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStpStatAdminStatus.setStatus("mandatory")
_HpSwitchMiscStat_ObjectIdentity = ObjectIdentity
hpSwitchMiscStat = _HpSwitchMiscStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 6)
)


class _HpSwitchCpuStat_Type(Integer32):
    """Custom type hpSwitchCpuStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchCpuStat_Type.__name__ = "Integer32"
_HpSwitchCpuStat_Object = MibScalar
hpSwitchCpuStat = _HpSwitchCpuStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 6, 1),
    _HpSwitchCpuStat_Type()
)
hpSwitchCpuStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCpuStat.setStatus("mandatory")
_HpSwitchFddiIpFragStat_ObjectIdentity = ObjectIdentity
hpSwitchFddiIpFragStat = _HpSwitchFddiIpFragStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7)
)
_HpSwitchFddiIpFragStatTable_Object = MibTable
hpSwitchFddiIpFragStatTable = _HpSwitchFddiIpFragStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragStatTable.setStatus("mandatory")
_HpSwitchFddiIpFragStatEntry_Object = MibTableRow
hpSwitchFddiIpFragStatEntry = _HpSwitchFddiIpFragStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1)
)
hpSwitchFddiIpFragStatEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchFddiIpFragStatIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragStatEntry.setStatus("mandatory")


class _HpSwitchFddiIpFragStatIndex_Type(Integer32):
    """Custom type hpSwitchFddiIpFragStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFddiIpFragStatIndex_Type.__name__ = "Integer32"
_HpSwitchFddiIpFragStatIndex_Object = MibTableColumn
hpSwitchFddiIpFragStatIndex = _HpSwitchFddiIpFragStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 1),
    _HpSwitchFddiIpFragStatIndex_Type()
)
hpSwitchFddiIpFragStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragStatIndex.setStatus("mandatory")
_HpSwitchFddiIpFragFramesFragmented_Type = Counter32
_HpSwitchFddiIpFragFramesFragmented_Object = MibTableColumn
hpSwitchFddiIpFragFramesFragmented = _HpSwitchFddiIpFragFramesFragmented_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 2),
    _HpSwitchFddiIpFragFramesFragmented_Type()
)
hpSwitchFddiIpFragFramesFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragFramesFragmented.setStatus("mandatory")
_HpSwitchFddiIpFragFramesCreated_Type = Counter32
_HpSwitchFddiIpFragFramesCreated_Object = MibTableColumn
hpSwitchFddiIpFragFramesCreated = _HpSwitchFddiIpFragFramesCreated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 3),
    _HpSwitchFddiIpFragFramesCreated_Type()
)
hpSwitchFddiIpFragFramesCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragFramesCreated.setStatus("mandatory")
_HpSwitchFddiIpFragFrameErrors_Type = Counter32
_HpSwitchFddiIpFragFrameErrors_Object = MibTableColumn
hpSwitchFddiIpFragFrameErrors = _HpSwitchFddiIpFragFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 4),
    _HpSwitchFddiIpFragFrameErrors_Type()
)
hpSwitchFddiIpFragFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragFrameErrors.setStatus("mandatory")
_HpSwitchFddiSystemStat_ObjectIdentity = ObjectIdentity
hpSwitchFddiSystemStat = _HpSwitchFddiSystemStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8)
)
_HpSwitchFddiSystemStatTable_Object = MibTable
hpSwitchFddiSystemStatTable = _HpSwitchFddiSystemStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFddiSystemStatTable.setStatus("mandatory")
_HpSwitchFddiSystemStatEntry_Object = MibTableRow
hpSwitchFddiSystemStatEntry = _HpSwitchFddiSystemStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1)
)
hpSwitchFddiSystemStatEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchFddiSystemStatIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFddiSystemStatEntry.setStatus("mandatory")


class _HpSwitchFddiSystemStatIndex_Type(Integer32):
    """Custom type hpSwitchFddiSystemStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFddiSystemStatIndex_Type.__name__ = "Integer32"
_HpSwitchFddiSystemStatIndex_Object = MibTableColumn
hpSwitchFddiSystemStatIndex = _HpSwitchFddiSystemStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 1),
    _HpSwitchFddiSystemStatIndex_Type()
)
hpSwitchFddiSystemStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemStatIndex.setStatus("mandatory")


class _HpSwitchFddiSystemOsVersion_Type(DisplayString):
    """Custom type hpSwitchFddiSystemOsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpSwitchFddiSystemOsVersion_Type.__name__ = "DisplayString"
_HpSwitchFddiSystemOsVersion_Object = MibTableColumn
hpSwitchFddiSystemOsVersion = _HpSwitchFddiSystemOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 2),
    _HpSwitchFddiSystemOsVersion_Type()
)
hpSwitchFddiSystemOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemOsVersion.setStatus("mandatory")


class _HpSwitchFddiSystemRomVersion_Type(DisplayString):
    """Custom type hpSwitchFddiSystemRomVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpSwitchFddiSystemRomVersion_Type.__name__ = "DisplayString"
_HpSwitchFddiSystemRomVersion_Object = MibTableColumn
hpSwitchFddiSystemRomVersion = _HpSwitchFddiSystemRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 3),
    _HpSwitchFddiSystemRomVersion_Type()
)
hpSwitchFddiSystemRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemRomVersion.setStatus("mandatory")
_HpSwitchFddiSystemMemoryTotal_Type = Integer32
_HpSwitchFddiSystemMemoryTotal_Object = MibTableColumn
hpSwitchFddiSystemMemoryTotal = _HpSwitchFddiSystemMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 4),
    _HpSwitchFddiSystemMemoryTotal_Type()
)
hpSwitchFddiSystemMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemMemoryTotal.setStatus("mandatory")
_HpSwitchFddiSystemMemoryFree_Type = Integer32
_HpSwitchFddiSystemMemoryFree_Object = MibTableColumn
hpSwitchFddiSystemMemoryFree = _HpSwitchFddiSystemMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 5),
    _HpSwitchFddiSystemMemoryFree_Type()
)
hpSwitchFddiSystemMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemMemoryFree.setStatus("mandatory")


class _HpSwitchFddiSystemCpuUtil_Type(Integer32):
    """Custom type hpSwitchFddiSystemCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchFddiSystemCpuUtil_Type.__name__ = "Integer32"
_HpSwitchFddiSystemCpuUtil_Object = MibTableColumn
hpSwitchFddiSystemCpuUtil = _HpSwitchFddiSystemCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 6),
    _HpSwitchFddiSystemCpuUtil_Type()
)
hpSwitchFddiSystemCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemCpuUtil.setStatus("mandatory")


class _HpSwitchFddiSystemBuildDirectory_Type(OctetString):
    """Custom type hpSwitchFddiSystemBuildDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_HpSwitchFddiSystemBuildDirectory_Type.__name__ = "OctetString"
_HpSwitchFddiSystemBuildDirectory_Object = MibTableColumn
hpSwitchFddiSystemBuildDirectory = _HpSwitchFddiSystemBuildDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 7),
    _HpSwitchFddiSystemBuildDirectory_Type()
)
hpSwitchFddiSystemBuildDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemBuildDirectory.setStatus("mandatory")


class _HpSwitchFddiSystemBuildDate_Type(OctetString):
    """Custom type hpSwitchFddiSystemBuildDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_HpSwitchFddiSystemBuildDate_Type.__name__ = "OctetString"
_HpSwitchFddiSystemBuildDate_Object = MibTableColumn
hpSwitchFddiSystemBuildDate = _HpSwitchFddiSystemBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 8),
    _HpSwitchFddiSystemBuildDate_Type()
)
hpSwitchFddiSystemBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemBuildDate.setStatus("mandatory")


class _HpSwitchFddiSystemBuildNumber_Type(OctetString):
    """Custom type hpSwitchFddiSystemBuildNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_HpSwitchFddiSystemBuildNumber_Type.__name__ = "OctetString"
_HpSwitchFddiSystemBuildNumber_Object = MibTableColumn
hpSwitchFddiSystemBuildNumber = _HpSwitchFddiSystemBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 9),
    _HpSwitchFddiSystemBuildNumber_Type()
)
hpSwitchFddiSystemBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiSystemBuildNumber.setStatus("mandatory")
_HpABCStats_ObjectIdentity = ObjectIdentity
hpABCStats = _HpABCStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9)
)
_HpABCStatsTable_Object = MibTable
hpABCStatsTable = _HpABCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1)
)
if mibBuilder.loadTexts:
    hpABCStatsTable.setStatus("mandatory")
_HpABCStatsEntry_Object = MibTableRow
hpABCStatsEntry = _HpABCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1)
)
hpABCStatsEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpABCStatsVlanIndex"),
    (0, "STATISTICS-MIB", "hpABCStatsPortIndex"),
)
if mibBuilder.loadTexts:
    hpABCStatsEntry.setStatus("mandatory")
_HpABCStatsVlanIndex_Type = VlanID
_HpABCStatsVlanIndex_Object = MibTableColumn
hpABCStatsVlanIndex = _HpABCStatsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 1),
    _HpABCStatsVlanIndex_Type()
)
hpABCStatsVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsVlanIndex.setStatus("mandatory")


class _HpABCStatsPortIndex_Type(Integer32):
    """Custom type hpABCStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpABCStatsPortIndex_Type.__name__ = "Integer32"
_HpABCStatsPortIndex_Object = MibTableColumn
hpABCStatsPortIndex = _HpABCStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 2),
    _HpABCStatsPortIndex_Type()
)
hpABCStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsPortIndex.setStatus("mandatory")
_HpABCStatsPortType_Type = HpSwitchPortType
_HpABCStatsPortType_Object = MibTableColumn
hpABCStatsPortType = _HpABCStatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 3),
    _HpABCStatsPortType_Type()
)
hpABCStatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsPortType.setStatus("mandatory")
_HpABCStatsArpReplies_Type = Counter32
_HpABCStatsArpReplies_Object = MibTableColumn
hpABCStatsArpReplies = _HpABCStatsArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 4),
    _HpABCStatsArpReplies_Type()
)
hpABCStatsArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsArpReplies.setStatus("mandatory")
_HpABCStatsIpxReplies_Type = Counter32
_HpABCStatsIpxReplies_Object = MibTableColumn
hpABCStatsIpxReplies = _HpABCStatsIpxReplies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 5),
    _HpABCStatsIpxReplies_Type()
)
hpABCStatsIpxReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsIpxReplies.setStatus("mandatory")


class _HpABCStatsIpRipControl_Type(Integer32):
    """Custom type hpABCStatsIpRipControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_HpABCStatsIpRipControl_Type.__name__ = "Integer32"
_HpABCStatsIpRipControl_Object = MibTableColumn
hpABCStatsIpRipControl = _HpABCStatsIpRipControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 6),
    _HpABCStatsIpRipControl_Type()
)
hpABCStatsIpRipControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsIpRipControl.setStatus("mandatory")


class _HpABCStatsIpxRipSapControl_Type(Integer32):
    """Custom type hpABCStatsIpxRipSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_HpABCStatsIpxRipSapControl_Type.__name__ = "Integer32"
_HpABCStatsIpxRipSapControl_Object = MibTableColumn
hpABCStatsIpxRipSapControl = _HpABCStatsIpxRipSapControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 7),
    _HpABCStatsIpxRipSapControl_Type()
)
hpABCStatsIpxRipSapControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpABCStatsIpxRipSapControl.setStatus("mandatory")
_HpIgmpStats_ObjectIdentity = ObjectIdentity
hpIgmpStats = _HpIgmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10)
)
_HpIgmpStatsTable_Object = MibTable
hpIgmpStatsTable = _HpIgmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1)
)
if mibBuilder.loadTexts:
    hpIgmpStatsTable.setStatus("mandatory")
_HpIgmpStatsEntry_Object = MibTableRow
hpIgmpStatsEntry = _HpIgmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1)
)
hpIgmpStatsEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpIgmpStatsVlanIndex"),
    (0, "STATISTICS-MIB", "hpIgmpStatsActiveGroupAddr"),
)
if mibBuilder.loadTexts:
    hpIgmpStatsEntry.setStatus("mandatory")
_HpIgmpStatsVlanIndex_Type = VlanID
_HpIgmpStatsVlanIndex_Object = MibTableColumn
hpIgmpStatsVlanIndex = _HpIgmpStatsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 1),
    _HpIgmpStatsVlanIndex_Type()
)
hpIgmpStatsVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsVlanIndex.setStatus("mandatory")
_HpIgmpStatsActiveGroupAddr_Type = IpAddress
_HpIgmpStatsActiveGroupAddr_Object = MibTableColumn
hpIgmpStatsActiveGroupAddr = _HpIgmpStatsActiveGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 2),
    _HpIgmpStatsActiveGroupAddr_Type()
)
hpIgmpStatsActiveGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsActiveGroupAddr.setStatus("mandatory")
_HpIgmpStatsReports_Type = Counter32
_HpIgmpStatsReports_Object = MibTableColumn
hpIgmpStatsReports = _HpIgmpStatsReports_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 3),
    _HpIgmpStatsReports_Type()
)
hpIgmpStatsReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsReports.setStatus("mandatory")
_HpIgmpStatsQueries_Type = Counter32
_HpIgmpStatsQueries_Object = MibTableColumn
hpIgmpStatsQueries = _HpIgmpStatsQueries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 4),
    _HpIgmpStatsQueries_Type()
)
hpIgmpStatsQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsQueries.setStatus("mandatory")
_HpIgmpStatsQuerierAccessPort_Type = Integer32
_HpIgmpStatsQuerierAccessPort_Object = MibTableColumn
hpIgmpStatsQuerierAccessPort = _HpIgmpStatsQuerierAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 5),
    _HpIgmpStatsQuerierAccessPort_Type()
)
hpIgmpStatsQuerierAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsQuerierAccessPort.setStatus("mandatory")
_HpIgmpStatsPortTable_Object = MibTable
hpIgmpStatsPortTable = _HpIgmpStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2)
)
if mibBuilder.loadTexts:
    hpIgmpStatsPortTable.setStatus("deprecated")
_HpIgmpStatsPortEntry_Object = MibTableRow
hpIgmpStatsPortEntry = _HpIgmpStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1)
)
hpIgmpStatsPortEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpIgmpStatsActiveGroupAddr"),
    (0, "STATISTICS-MIB", "hpIgmpStatsPortIndex"),
)
if mibBuilder.loadTexts:
    hpIgmpStatsPortEntry.setStatus("deprecated")


class _HpIgmpStatsPortIndex_Type(Integer32):
    """Custom type hpIgmpStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpIgmpStatsPortIndex_Type.__name__ = "Integer32"
_HpIgmpStatsPortIndex_Object = MibTableColumn
hpIgmpStatsPortIndex = _HpIgmpStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1, 1),
    _HpIgmpStatsPortIndex_Type()
)
hpIgmpStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortIndex.setStatus("deprecated")
_HpIgmpStatsPortType_Type = HpSwitchPortType
_HpIgmpStatsPortType_Object = MibTableColumn
hpIgmpStatsPortType = _HpIgmpStatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1, 2),
    _HpIgmpStatsPortType_Type()
)
hpIgmpStatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortType.setStatus("deprecated")


class _HpIgmpStatsPortAccess_Type(Integer32):
    """Custom type hpIgmpStatsPortAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("host-router", 3),
          ("router", 2))
    )


_HpIgmpStatsPortAccess_Type.__name__ = "Integer32"
_HpIgmpStatsPortAccess_Object = MibTableColumn
hpIgmpStatsPortAccess = _HpIgmpStatsPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1, 3),
    _HpIgmpStatsPortAccess_Type()
)
hpIgmpStatsPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortAccess.setStatus("deprecated")
_HpIgmpStatsPortTable2_Object = MibTable
hpIgmpStatsPortTable2 = _HpIgmpStatsPortTable2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3)
)
if mibBuilder.loadTexts:
    hpIgmpStatsPortTable2.setStatus("mandatory")
_HpIgmpStatsPortEntry2_Object = MibTableRow
hpIgmpStatsPortEntry2 = _HpIgmpStatsPortEntry2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1)
)
hpIgmpStatsPortEntry2.setIndexNames(
    (0, "STATISTICS-MIB", "hpIgmpStatsVlanIndex"),
    (0, "STATISTICS-MIB", "hpIgmpStatsActiveGroupAddr"),
    (0, "STATISTICS-MIB", "hpIgmpStatsPortIndex2"),
)
if mibBuilder.loadTexts:
    hpIgmpStatsPortEntry2.setStatus("mandatory")


class _HpIgmpStatsPortIndex2_Type(Integer32):
    """Custom type hpIgmpStatsPortIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpIgmpStatsPortIndex2_Type.__name__ = "Integer32"
_HpIgmpStatsPortIndex2_Object = MibTableColumn
hpIgmpStatsPortIndex2 = _HpIgmpStatsPortIndex2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 1),
    _HpIgmpStatsPortIndex2_Type()
)
hpIgmpStatsPortIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortIndex2.setStatus("mandatory")
_HpIgmpStatsPortType2_Type = HpSwitchPortType
_HpIgmpStatsPortType2_Object = MibTableColumn
hpIgmpStatsPortType2 = _HpIgmpStatsPortType2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 2),
    _HpIgmpStatsPortType2_Type()
)
hpIgmpStatsPortType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortType2.setStatus("mandatory")


class _HpIgmpStatsPortAccess2_Type(Integer32):
    """Custom type hpIgmpStatsPortAccess2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("host-router", 3),
          ("router", 2))
    )


_HpIgmpStatsPortAccess2_Type.__name__ = "Integer32"
_HpIgmpStatsPortAccess2_Object = MibTableColumn
hpIgmpStatsPortAccess2 = _HpIgmpStatsPortAccess2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 3),
    _HpIgmpStatsPortAccess2_Type()
)
hpIgmpStatsPortAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortAccess2.setStatus("mandatory")
_HpIgmpStatsPortAgeTimer2_Type = Integer32
_HpIgmpStatsPortAgeTimer2_Object = MibTableColumn
hpIgmpStatsPortAgeTimer2 = _HpIgmpStatsPortAgeTimer2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 4),
    _HpIgmpStatsPortAgeTimer2_Type()
)
hpIgmpStatsPortAgeTimer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortAgeTimer2.setStatus("mandatory")
_HpIgmpStatsPortLeaveTimer2_Type = Integer32
_HpIgmpStatsPortLeaveTimer2_Object = MibTableColumn
hpIgmpStatsPortLeaveTimer2 = _HpIgmpStatsPortLeaveTimer2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 5),
    _HpIgmpStatsPortLeaveTimer2_Type()
)
hpIgmpStatsPortLeaveTimer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIgmpStatsPortLeaveTimer2.setStatus("mandatory")
_HpLdbalStats_ObjectIdentity = ObjectIdentity
hpLdbalStats = _HpLdbalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11)
)
_HpLdbalStatsPortTable_Object = MibTable
hpLdbalStatsPortTable = _HpLdbalStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1)
)
if mibBuilder.loadTexts:
    hpLdbalStatsPortTable.setStatus("mandatory")
_HpLdbalStatsPortEntry_Object = MibTableRow
hpLdbalStatsPortEntry = _HpLdbalStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1)
)
hpLdbalStatsPortEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpLdbalStatsPortIndex"),
)
if mibBuilder.loadTexts:
    hpLdbalStatsPortEntry.setStatus("mandatory")


class _HpLdbalStatsPortIndex_Type(Integer32):
    """Custom type hpLdbalStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpLdbalStatsPortIndex_Type.__name__ = "Integer32"
_HpLdbalStatsPortIndex_Object = MibTableColumn
hpLdbalStatsPortIndex = _HpLdbalStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 1),
    _HpLdbalStatsPortIndex_Type()
)
hpLdbalStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLdbalStatsPortIndex.setStatus("mandatory")


class _HpLdbalStatsPortState_Type(Integer32):
    """Custom type hpLdbalStatsPortState based on Integer32"""
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
        *(("disabled", 1),
          ("error", 2),
          ("established", 5),
          ("initial", 3),
          ("notEstablished", 4),
          ("topologyError", 6))
    )


_HpLdbalStatsPortState_Type.__name__ = "Integer32"
_HpLdbalStatsPortState_Object = MibTableColumn
hpLdbalStatsPortState = _HpLdbalStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 2),
    _HpLdbalStatsPortState_Type()
)
hpLdbalStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLdbalStatsPortState.setStatus("mandatory")
_HpLdbalStatsAdjacentSwitch_Type = MacAddress
_HpLdbalStatsAdjacentSwitch_Object = MibTableColumn
hpLdbalStatsAdjacentSwitch = _HpLdbalStatsAdjacentSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 3),
    _HpLdbalStatsAdjacentSwitch_Type()
)
hpLdbalStatsAdjacentSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLdbalStatsAdjacentSwitch.setStatus("mandatory")
_HpLdbalStatsPeerPort_Type = MacAddress
_HpLdbalStatsPeerPort_Object = MibTableColumn
hpLdbalStatsPeerPort = _HpLdbalStatsPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 4),
    _HpLdbalStatsPeerPort_Type()
)
hpLdbalStatsPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLdbalStatsPeerPort.setStatus("mandatory")
_HpLdbalStatsAdjacentHost_Type = DisplayString
_HpLdbalStatsAdjacentHost_Object = MibTableColumn
hpLdbalStatsAdjacentHost = _HpLdbalStatsAdjacentHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 5),
    _HpLdbalStatsAdjacentHost_Type()
)
hpLdbalStatsAdjacentHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLdbalStatsAdjacentHost.setStatus("mandatory")


class _HpLdbalStatsMeshWarningStatus_Type(Integer32):
    """Custom type hpLdbalStatsMeshWarningStatus based on Integer32"""
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


_HpLdbalStatsMeshWarningStatus_Type.__name__ = "Integer32"
_HpLdbalStatsMeshWarningStatus_Object = MibTableColumn
hpLdbalStatsMeshWarningStatus = _HpLdbalStatsMeshWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 6),
    _HpLdbalStatsMeshWarningStatus_Type()
)
hpLdbalStatsMeshWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpLdbalStatsMeshWarningStatus.setStatus("mandatory")
_HpSwitchMacStats_ObjectIdentity = ObjectIdentity
hpSwitchMacStats = _HpSwitchMacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 12)
)


class _HpSwitchFdbAddressCount_Type(Integer32):
    """Custom type hpSwitchFdbAddressCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_HpSwitchFdbAddressCount_Type.__name__ = "Integer32"
_HpSwitchFdbAddressCount_Object = MibScalar
hpSwitchFdbAddressCount = _HpSwitchFdbAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 12, 1),
    _HpSwitchFdbAddressCount_Type()
)
hpSwitchFdbAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFdbAddressCount.setStatus("mandatory")
_HpSwitchFlowControlStatus_ObjectIdentity = ObjectIdentity
hpSwitchFlowControlStatus = _HpSwitchFlowControlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13)
)
_HpSwitchFlowControlStatusTable_Object = MibTable
hpSwitchFlowControlStatusTable = _HpSwitchFlowControlStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFlowControlStatusTable.setStatus("mandatory")
_HpSwitchFlowControlStatusEntry_Object = MibTableRow
hpSwitchFlowControlStatusEntry = _HpSwitchFlowControlStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1, 1)
)
hpSwitchFlowControlStatusEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchFlowControlStatusPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFlowControlStatusEntry.setStatus("mandatory")


class _HpSwitchFlowControlStatusPortIndex_Type(Integer32):
    """Custom type hpSwitchFlowControlStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFlowControlStatusPortIndex_Type.__name__ = "Integer32"
_HpSwitchFlowControlStatusPortIndex_Object = MibTableColumn
hpSwitchFlowControlStatusPortIndex = _HpSwitchFlowControlStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1, 1, 1),
    _HpSwitchFlowControlStatusPortIndex_Type()
)
hpSwitchFlowControlStatusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFlowControlStatusPortIndex.setStatus("mandatory")


class _HpSwitchFlowControlState_Type(Integer32):
    """Custom type hpSwitchFlowControlState based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("on-rx", 3),
          ("on-tx", 4))
    )


_HpSwitchFlowControlState_Type.__name__ = "Integer32"
_HpSwitchFlowControlState_Object = MibTableColumn
hpSwitchFlowControlState = _HpSwitchFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1, 1, 2),
    _HpSwitchFlowControlState_Type()
)
hpSwitchFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFlowControlState.setStatus("mandatory")
_HpFECStatsTrunk_ObjectIdentity = ObjectIdentity
hpFECStatsTrunk = _HpFECStatsTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14)
)
_HpFECStatsTrunkTable_Object = MibTable
hpFECStatsTrunkTable = _HpFECStatsTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1)
)
if mibBuilder.loadTexts:
    hpFECStatsTrunkTable.setStatus("mandatory")
_HpFECStatsTrunkEntry_Object = MibTableRow
hpFECStatsTrunkEntry = _HpFECStatsTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1)
)
hpFECStatsTrunkEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpFECStatsTrunkIndex"),
)
if mibBuilder.loadTexts:
    hpFECStatsTrunkEntry.setStatus("mandatory")


class _HpFECStatsTrunkIndex_Type(Integer32):
    """Custom type hpFECStatsTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpFECStatsTrunkIndex_Type.__name__ = "Integer32"
_HpFECStatsTrunkIndex_Object = MibTableColumn
hpFECStatsTrunkIndex = _HpFECStatsTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 1),
    _HpFECStatsTrunkIndex_Type()
)
hpFECStatsTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsTrunkIndex.setStatus("mandatory")
_HpFECStatsTrunkName_Type = DisplayString
_HpFECStatsTrunkName_Object = MibTableColumn
hpFECStatsTrunkName = _HpFECStatsTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 2),
    _HpFECStatsTrunkName_Type()
)
hpFECStatsTrunkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsTrunkName.setStatus("mandatory")


class _HpFECStatsTrunkNegotiationStatus_Type(Integer32):
    """Custom type hpFECStatsTrunkNegotiationStatus based on Integer32"""
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
          ("initialized", 3),
          ("successful", 1))
    )


_HpFECStatsTrunkNegotiationStatus_Type.__name__ = "Integer32"
_HpFECStatsTrunkNegotiationStatus_Object = MibTableColumn
hpFECStatsTrunkNegotiationStatus = _HpFECStatsTrunkNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 3),
    _HpFECStatsTrunkNegotiationStatus_Type()
)
hpFECStatsTrunkNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsTrunkNegotiationStatus.setStatus("mandatory")


class _HpFECStatsTrunkForwardingMode_Type(Integer32):
    """Custom type hpFECStatsTrunkForwardingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("sa-da", 2),
          ("sa-only", 1))
    )


_HpFECStatsTrunkForwardingMode_Type.__name__ = "Integer32"
_HpFECStatsTrunkForwardingMode_Object = MibTableColumn
hpFECStatsTrunkForwardingMode = _HpFECStatsTrunkForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 4),
    _HpFECStatsTrunkForwardingMode_Type()
)
hpFECStatsTrunkForwardingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsTrunkForwardingMode.setStatus("mandatory")
_HpFECStatsTrunkFlushPktsEchoed_Type = Counter32
_HpFECStatsTrunkFlushPktsEchoed_Object = MibTableColumn
hpFECStatsTrunkFlushPktsEchoed = _HpFECStatsTrunkFlushPktsEchoed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 5),
    _HpFECStatsTrunkFlushPktsEchoed_Type()
)
hpFECStatsTrunkFlushPktsEchoed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsTrunkFlushPktsEchoed.setStatus("mandatory")
_HpFECStatsPort_ObjectIdentity = ObjectIdentity
hpFECStatsPort = _HpFECStatsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15)
)
_HpFECStatsPortTable_Object = MibTable
hpFECStatsPortTable = _HpFECStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1)
)
if mibBuilder.loadTexts:
    hpFECStatsPortTable.setStatus("mandatory")
_HpFECStatsPortEntry_Object = MibTableRow
hpFECStatsPortEntry = _HpFECStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1)
)
hpFECStatsPortEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpFECStatsPortIndex"),
)
if mibBuilder.loadTexts:
    hpFECStatsPortEntry.setStatus("mandatory")


class _HpFECStatsPortIndex_Type(Integer32):
    """Custom type hpFECStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpFECStatsPortIndex_Type.__name__ = "Integer32"
_HpFECStatsPortIndex_Object = MibTableColumn
hpFECStatsPortIndex = _HpFECStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 1),
    _HpFECStatsPortIndex_Type()
)
hpFECStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortIndex.setStatus("mandatory")


class _HpFECStatsPortTrunkNumber_Type(Integer32):
    """Custom type hpFECStatsPortTrunkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpFECStatsPortTrunkNumber_Type.__name__ = "Integer32"
_HpFECStatsPortTrunkNumber_Object = MibTableColumn
hpFECStatsPortTrunkNumber = _HpFECStatsPortTrunkNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 2),
    _HpFECStatsPortTrunkNumber_Type()
)
hpFECStatsPortTrunkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortTrunkNumber.setStatus("mandatory")
_HpFECStatsPortTrunkName_Type = DisplayString
_HpFECStatsPortTrunkName_Object = MibTableColumn
hpFECStatsPortTrunkName = _HpFECStatsPortTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 3),
    _HpFECStatsPortTrunkName_Type()
)
hpFECStatsPortTrunkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortTrunkName.setStatus("mandatory")


class _HpFECStatsPortMode_Type(Integer32):
    """Custom type hpFECStatsPortMode based on Integer32"""
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
        *(("blocking", 3),
          ("down", 1),
          ("forwarding", 2),
          ("up", 4))
    )


_HpFECStatsPortMode_Type.__name__ = "Integer32"
_HpFECStatsPortMode_Object = MibTableColumn
hpFECStatsPortMode = _HpFECStatsPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 4),
    _HpFECStatsPortMode_Type()
)
hpFECStatsPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortMode.setStatus("mandatory")


class _HpFECStatsPortNegotiationStatus_Type(Integer32):
    """Custom type hpFECStatsPortNegotiationStatus based on Integer32"""
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
          ("initialized", 3),
          ("successful", 1))
    )


_HpFECStatsPortNegotiationStatus_Type.__name__ = "Integer32"
_HpFECStatsPortNegotiationStatus_Object = MibTableColumn
hpFECStatsPortNegotiationStatus = _HpFECStatsPortNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 5),
    _HpFECStatsPortNegotiationStatus_Type()
)
hpFECStatsPortNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortNegotiationStatus.setStatus("mandatory")
_HpFECStatsPortHellosSent_Type = Counter32
_HpFECStatsPortHellosSent_Object = MibTableColumn
hpFECStatsPortHellosSent = _HpFECStatsPortHellosSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 6),
    _HpFECStatsPortHellosSent_Type()
)
hpFECStatsPortHellosSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortHellosSent.setStatus("mandatory")
_HpFECStatsPortHellosReceived_Type = Counter32
_HpFECStatsPortHellosReceived_Object = MibTableColumn
hpFECStatsPortHellosReceived = _HpFECStatsPortHellosReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 7),
    _HpFECStatsPortHellosReceived_Type()
)
hpFECStatsPortHellosReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortHellosReceived.setStatus("mandatory")


class _HpFECStatsPortMySlowHello_Type(Integer32):
    """Custom type hpFECStatsPortMySlowHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("slow", 2))
    )


_HpFECStatsPortMySlowHello_Type.__name__ = "Integer32"
_HpFECStatsPortMySlowHello_Object = MibTableColumn
hpFECStatsPortMySlowHello = _HpFECStatsPortMySlowHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 8),
    _HpFECStatsPortMySlowHello_Type()
)
hpFECStatsPortMySlowHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortMySlowHello.setStatus("mandatory")


class _HpFECStatsPortMyAutoMode_Type(Integer32):
    """Custom type hpFECStatsPortMyAutoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("desirable", 1))
    )


_HpFECStatsPortMyAutoMode_Type.__name__ = "Integer32"
_HpFECStatsPortMyAutoMode_Object = MibTableColumn
hpFECStatsPortMyAutoMode = _HpFECStatsPortMyAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 9),
    _HpFECStatsPortMyAutoMode_Type()
)
hpFECStatsPortMyAutoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortMyAutoMode.setStatus("mandatory")
_HpFECStatsPortPartner_Type = MacAddress
_HpFECStatsPortPartner_Object = MibTableColumn
hpFECStatsPortPartner = _HpFECStatsPortPartner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 10),
    _HpFECStatsPortPartner_Type()
)
hpFECStatsPortPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortPartner.setStatus("mandatory")
_HpFECStatsPortFlushPktsEchoed_Type = Counter32
_HpFECStatsPortFlushPktsEchoed_Object = MibTableColumn
hpFECStatsPortFlushPktsEchoed = _HpFECStatsPortFlushPktsEchoed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 11),
    _HpFECStatsPortFlushPktsEchoed_Type()
)
hpFECStatsPortFlushPktsEchoed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFECStatsPortFlushPktsEchoed.setStatus("mandatory")
_HpGvrpStats_ObjectIdentity = ObjectIdentity
hpGvrpStats = _HpGvrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16)
)
_HpGvrpStatsTable_Object = MibTable
hpGvrpStatsTable = _HpGvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1)
)
if mibBuilder.loadTexts:
    hpGvrpStatsTable.setStatus("mandatory")
_HpGvrpStatsEntry_Object = MibTableRow
hpGvrpStatsEntry = _HpGvrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1)
)
hpGvrpStatsEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpGvrpStatsVlanIndex"),
    (0, "STATISTICS-MIB", "hpGvrpStatsPortIndex"),
)
if mibBuilder.loadTexts:
    hpGvrpStatsEntry.setStatus("mandatory")
_HpGvrpStatsVlanIndex_Type = VlanID
_HpGvrpStatsVlanIndex_Object = MibTableColumn
hpGvrpStatsVlanIndex = _HpGvrpStatsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 1),
    _HpGvrpStatsVlanIndex_Type()
)
hpGvrpStatsVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGvrpStatsVlanIndex.setStatus("mandatory")


class _HpGvrpStatsPortIndex_Type(Integer32):
    """Custom type hpGvrpStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpGvrpStatsPortIndex_Type.__name__ = "Integer32"
_HpGvrpStatsPortIndex_Object = MibTableColumn
hpGvrpStatsPortIndex = _HpGvrpStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 2),
    _HpGvrpStatsPortIndex_Type()
)
hpGvrpStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGvrpStatsPortIndex.setStatus("mandatory")


class _HpGvrpStatsPortVlanMember_Type(Integer32):
    """Custom type hpGvrpStatsPortVlanMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("pending", 1),
          ("yes", 2))
    )


_HpGvrpStatsPortVlanMember_Type.__name__ = "Integer32"
_HpGvrpStatsPortVlanMember_Object = MibTableColumn
hpGvrpStatsPortVlanMember = _HpGvrpStatsPortVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 3),
    _HpGvrpStatsPortVlanMember_Type()
)
hpGvrpStatsPortVlanMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGvrpStatsPortVlanMember.setStatus("mandatory")


class _HpGvrpPortIfOperStatus_Type(Integer32):
    """Custom type hpGvrpPortIfOperStatus based on Integer32"""
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


_HpGvrpPortIfOperStatus_Type.__name__ = "Integer32"
_HpGvrpPortIfOperStatus_Object = MibTableColumn
hpGvrpPortIfOperStatus = _HpGvrpPortIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 4),
    _HpGvrpPortIfOperStatus_Type()
)
hpGvrpPortIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGvrpPortIfOperStatus.setStatus("mandatory")


class _HpPortGvrpCtrlStatus_Type(Integer32):
    """Custom type hpPortGvrpCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("disable", 3),
          ("learn", 1))
    )


_HpPortGvrpCtrlStatus_Type.__name__ = "Integer32"
_HpPortGvrpCtrlStatus_Object = MibTableColumn
hpPortGvrpCtrlStatus = _HpPortGvrpCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 5),
    _HpPortGvrpCtrlStatus_Type()
)
hpPortGvrpCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPortGvrpCtrlStatus.setStatus("mandatory")
_HpSshStats_ObjectIdentity = ObjectIdentity
hpSshStats = _HpSshStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17)
)
_HpSshStatsTable_Object = MibTable
hpSshStatsTable = _HpSshStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1)
)
if mibBuilder.loadTexts:
    hpSshStatsTable.setStatus("mandatory")
_HpSshStatsEntry_Object = MibTableRow
hpSshStatsEntry = _HpSshStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1)
)
hpSshStatsEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSshStatsSesIndex"),
)
if mibBuilder.loadTexts:
    hpSshStatsEntry.setStatus("mandatory")


class _HpSshStatsSesIndex_Type(Integer32):
    """Custom type hpSshStatsSesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSshStatsSesIndex_Type.__name__ = "Integer32"
_HpSshStatsSesIndex_Object = MibTableColumn
hpSshStatsSesIndex = _HpSshStatsSesIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 1),
    _HpSshStatsSesIndex_Type()
)
hpSshStatsSesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSesIndex.setStatus("mandatory")


class _HpSshStatsSesType_Type(Integer32):
    """Custom type hpSshStatsSesType based on Integer32"""
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
        *(("console", 1),
          ("inactive", 4),
          ("ssh", 3),
          ("telnet", 2))
    )


_HpSshStatsSesType_Type.__name__ = "Integer32"
_HpSshStatsSesType_Object = MibTableColumn
hpSshStatsSesType = _HpSshStatsSesType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 2),
    _HpSshStatsSesType_Type()
)
hpSshStatsSesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSesType.setStatus("mandatory")


class _HpSshStatsSourceIpPort_Type(DisplayString):
    """Custom type hpSshStatsSourceIpPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_HpSshStatsSourceIpPort_Type.__name__ = "DisplayString"
_HpSshStatsSourceIpPort_Object = MibTableColumn
hpSshStatsSourceIpPort = _HpSshStatsSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 3),
    _HpSshStatsSourceIpPort_Type()
)
hpSshStatsSourceIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSourceIpPort.setStatus("deprecated")


class _HpSshStatsSesVersion_Type(Integer32):
    """Custom type hpSshStatsSesVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 255),
          ("version1", 1),
          ("version2", 2))
    )


_HpSshStatsSesVersion_Type.__name__ = "Integer32"
_HpSshStatsSesVersion_Object = MibTableColumn
hpSshStatsSesVersion = _HpSshStatsSesVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 4),
    _HpSshStatsSesVersion_Type()
)
hpSshStatsSesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSesVersion.setStatus("mandatory")
_HpSshStatsSourceIpType_Type = InetAddressType
_HpSshStatsSourceIpType_Object = MibTableColumn
hpSshStatsSourceIpType = _HpSshStatsSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 5),
    _HpSshStatsSourceIpType_Type()
)
hpSshStatsSourceIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSourceIpType.setStatus("mandatory")
_HpSshStatsSourceIpAddress_Type = InetAddress
_HpSshStatsSourceIpAddress_Object = MibTableColumn
hpSshStatsSourceIpAddress = _HpSshStatsSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 6),
    _HpSshStatsSourceIpAddress_Type()
)
hpSshStatsSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSourceIpAddress.setStatus("mandatory")
_HpSshStatsSourceIpPortNum_Type = InetPortNumber
_HpSshStatsSourceIpPortNum_Object = MibTableColumn
hpSshStatsSourceIpPortNum = _HpSshStatsSourceIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 7),
    _HpSshStatsSourceIpPortNum_Type()
)
hpSshStatsSourceIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSshStatsSourceIpPortNum.setStatus("mandatory")
_HpSwitchPhysicalPort_ObjectIdentity = ObjectIdentity
hpSwitchPhysicalPort = _HpSwitchPhysicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18)
)
_HpSwitchPhysicalPortTable_Object = MibTable
hpSwitchPhysicalPortTable = _HpSwitchPhysicalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1)
)
if mibBuilder.loadTexts:
    hpSwitchPhysicalPortTable.setStatus("mandatory")
_HpSwitchPhysicalPortEntry_Object = MibTableRow
hpSwitchPhysicalPortEntry = _HpSwitchPhysicalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1, 1)
)
hpSwitchPhysicalPortEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchPhysicalPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchPhysicalPortEntry.setStatus("mandatory")


class _HpSwitchPhysicalPortIndex_Type(Integer32):
    """Custom type hpSwitchPhysicalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchPhysicalPortIndex_Type.__name__ = "Integer32"
_HpSwitchPhysicalPortIndex_Object = MibTableColumn
hpSwitchPhysicalPortIndex = _HpSwitchPhysicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1, 1, 1),
    _HpSwitchPhysicalPortIndex_Type()
)
hpSwitchPhysicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPhysicalPortIndex.setStatus("mandatory")
_HpSwitchPhysicalPortType_Type = HpSwitchPortType
_HpSwitchPhysicalPortType_Object = MibTableColumn
hpSwitchPhysicalPortType = _HpSwitchPhysicalPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1, 1, 2),
    _HpSwitchPhysicalPortType_Type()
)
hpSwitchPhysicalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPhysicalPortType.setStatus("mandatory")
_HpSwitchCosStats_ObjectIdentity = ObjectIdentity
hpSwitchCosStats = _HpSwitchCosStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 19)
)
_HpSwitchQueueWatchStatsTable_Object = MibTable
hpSwitchQueueWatchStatsTable = _HpSwitchQueueWatchStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 19, 1)
)
if mibBuilder.loadTexts:
    hpSwitchQueueWatchStatsTable.setStatus("mandatory")
_HpSwitchQueueWatchStatsEntry_Object = MibTableRow
hpSwitchQueueWatchStatsEntry = _HpSwitchQueueWatchStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 19, 1, 1)
)
hpSwitchQueueWatchStatsEntry.setIndexNames(
    (0, "STATISTICS-MIB", "hpSwitchQueueWatchStatsPortIndex"),
    (0, "STATISTICS-MIB", "hpSwitchQueueWatchStatsQueueIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchQueueWatchStatsEntry.setStatus("mandatory")


class _HpSwitchQueueWatchStatsPortIndex_Type(Integer32):
    """Custom type hpSwitchQueueWatchStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchQueueWatchStatsPortIndex_Type.__name__ = "Integer32"
_HpSwitchQueueWatchStatsPortIndex_Object = MibTableColumn
hpSwitchQueueWatchStatsPortIndex = _HpSwitchQueueWatchStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 19, 1, 1, 1),
    _HpSwitchQueueWatchStatsPortIndex_Type()
)
hpSwitchQueueWatchStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchQueueWatchStatsPortIndex.setStatus("mandatory")


class _HpSwitchQueueWatchStatsQueueIndex_Type(Integer32):
    """Custom type hpSwitchQueueWatchStatsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchQueueWatchStatsQueueIndex_Type.__name__ = "Integer32"
_HpSwitchQueueWatchStatsQueueIndex_Object = MibTableColumn
hpSwitchQueueWatchStatsQueueIndex = _HpSwitchQueueWatchStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 19, 1, 1, 2),
    _HpSwitchQueueWatchStatsQueueIndex_Type()
)
hpSwitchQueueWatchStatsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchQueueWatchStatsQueueIndex.setStatus("mandatory")
_HpSwitchQueueWatchStatsQueueDrops_Type = Counter32
_HpSwitchQueueWatchStatsQueueDrops_Object = MibTableColumn
hpSwitchQueueWatchStatsQueueDrops = _HpSwitchQueueWatchStatsQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 19, 1, 1, 3),
    _HpSwitchQueueWatchStatsQueueDrops_Type()
)
hpSwitchQueueWatchStatsQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchQueueWatchStatsQueueDrops.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STATISTICS-MIB",
    **{"MacAddress": MacAddress,
       "VlanID": VlanID,
       "hpSwitchStatistics": hpSwitchStatistics,
       "hpSwitchIpxStat": hpSwitchIpxStat,
       "hpSwitchIpxStatTable": hpSwitchIpxStatTable,
       "hpSwitchIpxStatEntry": hpSwitchIpxStatEntry,
       "hpSwitchIpxStatIndex": hpSwitchIpxStatIndex,
       "hpSwitchIpxStatNodeAddr": hpSwitchIpxStatNodeAddr,
       "hpSwitchIpxStatGatewayAddr": hpSwitchIpxStatGatewayAddr,
       "hpSwitchIpxStatGatewayEncap": hpSwitchIpxStatGatewayEncap,
       "hpSwitchIpxStatAdminStatus": hpSwitchIpxStatAdminStatus,
       "hpSwitchIpStat": hpSwitchIpStat,
       "hpSwitchIpStatTimepAdminStatus": hpSwitchIpStatTimepAdminStatus,
       "hpSwitchIpStatTimepServerAddr": hpSwitchIpStatTimepServerAddr,
       "hpSwitchIpStatTimepPollInterval": hpSwitchIpStatTimepPollInterval,
       "hpSwitchIpStatTable": hpSwitchIpStatTable,
       "hpSwitchIpStatEntry": hpSwitchIpStatEntry,
       "hpSwitchIpStatIndex": hpSwitchIpStatIndex,
       "hpSwitchIpStatAddr": hpSwitchIpStatAddr,
       "hpSwitchIpStatMask": hpSwitchIpStatMask,
       "hpSwitchIpStatGatewayAddr": hpSwitchIpStatGatewayAddr,
       "hpSwitchIpStatAdminStatus": hpSwitchIpStatAdminStatus,
       "hpSwitchFdbInfo": hpSwitchFdbInfo,
       "hpSwitchVlanFdbAddrTable": hpSwitchVlanFdbAddrTable,
       "hpSwitchVlanFdbAddrEntry": hpSwitchVlanFdbAddrEntry,
       "hpSwitchVlanFdbId": hpSwitchVlanFdbId,
       "hpSwitchVlanFdbAddress": hpSwitchVlanFdbAddress,
       "hpSwitchVlanFdbPort": hpSwitchVlanFdbPort,
       "hpSwitchPortFdbAddrTable": hpSwitchPortFdbAddrTable,
       "hpSwitchPortFdbAddrEntry": hpSwitchPortFdbAddrEntry,
       "hpSwitchPortFdbId": hpSwitchPortFdbId,
       "hpSwitchPortFdbAddress": hpSwitchPortFdbAddress,
       "hpSwitchPortFdbVlanId": hpSwitchPortFdbVlanId,
       "hpSwitchPortFdbVidList": hpSwitchPortFdbVidList,
       "hpSwitchStpStat": hpSwitchStpStat,
       "hpSwitchStpStatAdminStatus": hpSwitchStpStatAdminStatus,
       "hpSwitchMiscStat": hpSwitchMiscStat,
       "hpSwitchCpuStat": hpSwitchCpuStat,
       "hpSwitchFddiIpFragStat": hpSwitchFddiIpFragStat,
       "hpSwitchFddiIpFragStatTable": hpSwitchFddiIpFragStatTable,
       "hpSwitchFddiIpFragStatEntry": hpSwitchFddiIpFragStatEntry,
       "hpSwitchFddiIpFragStatIndex": hpSwitchFddiIpFragStatIndex,
       "hpSwitchFddiIpFragFramesFragmented": hpSwitchFddiIpFragFramesFragmented,
       "hpSwitchFddiIpFragFramesCreated": hpSwitchFddiIpFragFramesCreated,
       "hpSwitchFddiIpFragFrameErrors": hpSwitchFddiIpFragFrameErrors,
       "hpSwitchFddiSystemStat": hpSwitchFddiSystemStat,
       "hpSwitchFddiSystemStatTable": hpSwitchFddiSystemStatTable,
       "hpSwitchFddiSystemStatEntry": hpSwitchFddiSystemStatEntry,
       "hpSwitchFddiSystemStatIndex": hpSwitchFddiSystemStatIndex,
       "hpSwitchFddiSystemOsVersion": hpSwitchFddiSystemOsVersion,
       "hpSwitchFddiSystemRomVersion": hpSwitchFddiSystemRomVersion,
       "hpSwitchFddiSystemMemoryTotal": hpSwitchFddiSystemMemoryTotal,
       "hpSwitchFddiSystemMemoryFree": hpSwitchFddiSystemMemoryFree,
       "hpSwitchFddiSystemCpuUtil": hpSwitchFddiSystemCpuUtil,
       "hpSwitchFddiSystemBuildDirectory": hpSwitchFddiSystemBuildDirectory,
       "hpSwitchFddiSystemBuildDate": hpSwitchFddiSystemBuildDate,
       "hpSwitchFddiSystemBuildNumber": hpSwitchFddiSystemBuildNumber,
       "hpABCStats": hpABCStats,
       "hpABCStatsTable": hpABCStatsTable,
       "hpABCStatsEntry": hpABCStatsEntry,
       "hpABCStatsVlanIndex": hpABCStatsVlanIndex,
       "hpABCStatsPortIndex": hpABCStatsPortIndex,
       "hpABCStatsPortType": hpABCStatsPortType,
       "hpABCStatsArpReplies": hpABCStatsArpReplies,
       "hpABCStatsIpxReplies": hpABCStatsIpxReplies,
       "hpABCStatsIpRipControl": hpABCStatsIpRipControl,
       "hpABCStatsIpxRipSapControl": hpABCStatsIpxRipSapControl,
       "hpIgmpStats": hpIgmpStats,
       "hpIgmpStatsTable": hpIgmpStatsTable,
       "hpIgmpStatsEntry": hpIgmpStatsEntry,
       "hpIgmpStatsVlanIndex": hpIgmpStatsVlanIndex,
       "hpIgmpStatsActiveGroupAddr": hpIgmpStatsActiveGroupAddr,
       "hpIgmpStatsReports": hpIgmpStatsReports,
       "hpIgmpStatsQueries": hpIgmpStatsQueries,
       "hpIgmpStatsQuerierAccessPort": hpIgmpStatsQuerierAccessPort,
       "hpIgmpStatsPortTable": hpIgmpStatsPortTable,
       "hpIgmpStatsPortEntry": hpIgmpStatsPortEntry,
       "hpIgmpStatsPortIndex": hpIgmpStatsPortIndex,
       "hpIgmpStatsPortType": hpIgmpStatsPortType,
       "hpIgmpStatsPortAccess": hpIgmpStatsPortAccess,
       "hpIgmpStatsPortTable2": hpIgmpStatsPortTable2,
       "hpIgmpStatsPortEntry2": hpIgmpStatsPortEntry2,
       "hpIgmpStatsPortIndex2": hpIgmpStatsPortIndex2,
       "hpIgmpStatsPortType2": hpIgmpStatsPortType2,
       "hpIgmpStatsPortAccess2": hpIgmpStatsPortAccess2,
       "hpIgmpStatsPortAgeTimer2": hpIgmpStatsPortAgeTimer2,
       "hpIgmpStatsPortLeaveTimer2": hpIgmpStatsPortLeaveTimer2,
       "hpLdbalStats": hpLdbalStats,
       "hpLdbalStatsPortTable": hpLdbalStatsPortTable,
       "hpLdbalStatsPortEntry": hpLdbalStatsPortEntry,
       "hpLdbalStatsPortIndex": hpLdbalStatsPortIndex,
       "hpLdbalStatsPortState": hpLdbalStatsPortState,
       "hpLdbalStatsAdjacentSwitch": hpLdbalStatsAdjacentSwitch,
       "hpLdbalStatsPeerPort": hpLdbalStatsPeerPort,
       "hpLdbalStatsAdjacentHost": hpLdbalStatsAdjacentHost,
       "hpLdbalStatsMeshWarningStatus": hpLdbalStatsMeshWarningStatus,
       "hpSwitchMacStats": hpSwitchMacStats,
       "hpSwitchFdbAddressCount": hpSwitchFdbAddressCount,
       "hpSwitchFlowControlStatus": hpSwitchFlowControlStatus,
       "hpSwitchFlowControlStatusTable": hpSwitchFlowControlStatusTable,
       "hpSwitchFlowControlStatusEntry": hpSwitchFlowControlStatusEntry,
       "hpSwitchFlowControlStatusPortIndex": hpSwitchFlowControlStatusPortIndex,
       "hpSwitchFlowControlState": hpSwitchFlowControlState,
       "hpFECStatsTrunk": hpFECStatsTrunk,
       "hpFECStatsTrunkTable": hpFECStatsTrunkTable,
       "hpFECStatsTrunkEntry": hpFECStatsTrunkEntry,
       "hpFECStatsTrunkIndex": hpFECStatsTrunkIndex,
       "hpFECStatsTrunkName": hpFECStatsTrunkName,
       "hpFECStatsTrunkNegotiationStatus": hpFECStatsTrunkNegotiationStatus,
       "hpFECStatsTrunkForwardingMode": hpFECStatsTrunkForwardingMode,
       "hpFECStatsTrunkFlushPktsEchoed": hpFECStatsTrunkFlushPktsEchoed,
       "hpFECStatsPort": hpFECStatsPort,
       "hpFECStatsPortTable": hpFECStatsPortTable,
       "hpFECStatsPortEntry": hpFECStatsPortEntry,
       "hpFECStatsPortIndex": hpFECStatsPortIndex,
       "hpFECStatsPortTrunkNumber": hpFECStatsPortTrunkNumber,
       "hpFECStatsPortTrunkName": hpFECStatsPortTrunkName,
       "hpFECStatsPortMode": hpFECStatsPortMode,
       "hpFECStatsPortNegotiationStatus": hpFECStatsPortNegotiationStatus,
       "hpFECStatsPortHellosSent": hpFECStatsPortHellosSent,
       "hpFECStatsPortHellosReceived": hpFECStatsPortHellosReceived,
       "hpFECStatsPortMySlowHello": hpFECStatsPortMySlowHello,
       "hpFECStatsPortMyAutoMode": hpFECStatsPortMyAutoMode,
       "hpFECStatsPortPartner": hpFECStatsPortPartner,
       "hpFECStatsPortFlushPktsEchoed": hpFECStatsPortFlushPktsEchoed,
       "hpGvrpStats": hpGvrpStats,
       "hpGvrpStatsTable": hpGvrpStatsTable,
       "hpGvrpStatsEntry": hpGvrpStatsEntry,
       "hpGvrpStatsVlanIndex": hpGvrpStatsVlanIndex,
       "hpGvrpStatsPortIndex": hpGvrpStatsPortIndex,
       "hpGvrpStatsPortVlanMember": hpGvrpStatsPortVlanMember,
       "hpGvrpPortIfOperStatus": hpGvrpPortIfOperStatus,
       "hpPortGvrpCtrlStatus": hpPortGvrpCtrlStatus,
       "hpSshStats": hpSshStats,
       "hpSshStatsTable": hpSshStatsTable,
       "hpSshStatsEntry": hpSshStatsEntry,
       "hpSshStatsSesIndex": hpSshStatsSesIndex,
       "hpSshStatsSesType": hpSshStatsSesType,
       "hpSshStatsSourceIpPort": hpSshStatsSourceIpPort,
       "hpSshStatsSesVersion": hpSshStatsSesVersion,
       "hpSshStatsSourceIpType": hpSshStatsSourceIpType,
       "hpSshStatsSourceIpAddress": hpSshStatsSourceIpAddress,
       "hpSshStatsSourceIpPortNum": hpSshStatsSourceIpPortNum,
       "hpSwitchPhysicalPort": hpSwitchPhysicalPort,
       "hpSwitchPhysicalPortTable": hpSwitchPhysicalPortTable,
       "hpSwitchPhysicalPortEntry": hpSwitchPhysicalPortEntry,
       "hpSwitchPhysicalPortIndex": hpSwitchPhysicalPortIndex,
       "hpSwitchPhysicalPortType": hpSwitchPhysicalPortType,
       "hpSwitchCosStats": hpSwitchCosStats,
       "hpSwitchQueueWatchStatsTable": hpSwitchQueueWatchStatsTable,
       "hpSwitchQueueWatchStatsEntry": hpSwitchQueueWatchStatsEntry,
       "hpSwitchQueueWatchStatsPortIndex": hpSwitchQueueWatchStatsPortIndex,
       "hpSwitchQueueWatchStatsQueueIndex": hpSwitchQueueWatchStatsQueueIndex,
       "hpSwitchQueueWatchStatsQueueDrops": hpSwitchQueueWatchStatsQueueDrops}
)
