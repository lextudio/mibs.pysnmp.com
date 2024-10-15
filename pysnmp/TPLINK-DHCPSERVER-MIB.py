# SNMP MIB module (TPLINK-DHCPSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DHCPSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:56 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkDhcpServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38)
)
tplinkDhcpServerMIB.setRevisions(
        ("2012-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpServerMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpServerMIBObjects = _TplinkDhcpServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1)
)


class _TpDhcpServerEnable_Type(Integer32):
    """Custom type tpDhcpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpDhcpServerEnable_Type.__name__ = "Integer32"
_TpDhcpServerEnable_Object = MibScalar
tpDhcpServerEnable = _TpDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 1),
    _TpDhcpServerEnable_Type()
)
tpDhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerEnable.setStatus("current")


class _TpDhcpServerVendorClassId_Type(OctetString):
    """Custom type tpDhcpServerVendorClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TpDhcpServerVendorClassId_Type.__name__ = "OctetString"
_TpDhcpServerVendorClassId_Object = MibScalar
tpDhcpServerVendorClassId = _TpDhcpServerVendorClassId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 2),
    _TpDhcpServerVendorClassId_Type()
)
tpDhcpServerVendorClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerVendorClassId.setStatus("current")
_TpDhcpServerCapwapAcIp_Type = IpAddress
_TpDhcpServerCapwapAcIp_Object = MibScalar
tpDhcpServerCapwapAcIp = _TpDhcpServerCapwapAcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 3),
    _TpDhcpServerCapwapAcIp_Type()
)
tpDhcpServerCapwapAcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerCapwapAcIp.setStatus("current")
_TpDhcpServerUnusedIpTable_Object = MibTable
tpDhcpServerUnusedIpTable = _TpDhcpServerUnusedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4)
)
if mibBuilder.loadTexts:
    tpDhcpServerUnusedIpTable.setStatus("current")
_TpDhcpServerUnusedIpEntry_Object = MibTableRow
tpDhcpServerUnusedIpEntry = _TpDhcpServerUnusedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1)
)
tpDhcpServerUnusedIpEntry.setIndexNames(
    (0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerUnusedStartIp"),
)
if mibBuilder.loadTexts:
    tpDhcpServerUnusedIpEntry.setStatus("current")
_TpDhcpServerUnusedStartIp_Type = IpAddress
_TpDhcpServerUnusedStartIp_Object = MibTableColumn
tpDhcpServerUnusedStartIp = _TpDhcpServerUnusedStartIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 1),
    _TpDhcpServerUnusedStartIp_Type()
)
tpDhcpServerUnusedStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerUnusedStartIp.setStatus("current")
_TpDhcpServerUnusedEndIp_Type = IpAddress
_TpDhcpServerUnusedEndIp_Object = MibTableColumn
tpDhcpServerUnusedEndIp = _TpDhcpServerUnusedEndIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 2),
    _TpDhcpServerUnusedEndIp_Type()
)
tpDhcpServerUnusedEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerUnusedEndIp.setStatus("current")
_TpDhcpServerUnusedIpStatus_Type = TPRowStatus
_TpDhcpServerUnusedIpStatus_Object = MibTableColumn
tpDhcpServerUnusedIpStatus = _TpDhcpServerUnusedIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 3),
    _TpDhcpServerUnusedIpStatus_Type()
)
tpDhcpServerUnusedIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerUnusedIpStatus.setStatus("current")
_TpDhcpServerAddrPoolTable_Object = MibTable
tpDhcpServerAddrPoolTable = _TpDhcpServerAddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5)
)
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolTable.setStatus("current")
_TpDhcpServerAddrPoolEntry_Object = MibTableRow
tpDhcpServerAddrPoolEntry = _TpDhcpServerAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1)
)
tpDhcpServerAddrPoolEntry.setIndexNames(
    (0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerAddrPoolNetwork"),
)
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolEntry.setStatus("current")


class _TpDhcpServerAddrPoolName_Type(OctetString):
    """Custom type tpDhcpServerAddrPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TpDhcpServerAddrPoolName_Type.__name__ = "OctetString"
_TpDhcpServerAddrPoolName_Object = MibTableColumn
tpDhcpServerAddrPoolName = _TpDhcpServerAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 1),
    _TpDhcpServerAddrPoolName_Type()
)
tpDhcpServerAddrPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolName.setStatus("current")
_TpDhcpServerAddrPoolNetwork_Type = IpAddress
_TpDhcpServerAddrPoolNetwork_Object = MibTableColumn
tpDhcpServerAddrPoolNetwork = _TpDhcpServerAddrPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 2),
    _TpDhcpServerAddrPoolNetwork_Type()
)
tpDhcpServerAddrPoolNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNetwork.setStatus("current")
_TpDhcpServerAddrPoolSubnetMask_Type = IpAddress
_TpDhcpServerAddrPoolSubnetMask_Object = MibTableColumn
tpDhcpServerAddrPoolSubnetMask = _TpDhcpServerAddrPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 3),
    _TpDhcpServerAddrPoolSubnetMask_Type()
)
tpDhcpServerAddrPoolSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolSubnetMask.setStatus("current")
_TpDhcpServerAddrPoolRentTime_Type = Integer32
_TpDhcpServerAddrPoolRentTime_Object = MibTableColumn
tpDhcpServerAddrPoolRentTime = _TpDhcpServerAddrPoolRentTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 4),
    _TpDhcpServerAddrPoolRentTime_Type()
)
tpDhcpServerAddrPoolRentTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolRentTime.setStatus("current")
_TpDhcpServerAddrPoolGateWayA_Type = IpAddress
_TpDhcpServerAddrPoolGateWayA_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayA = _TpDhcpServerAddrPoolGateWayA_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 5),
    _TpDhcpServerAddrPoolGateWayA_Type()
)
tpDhcpServerAddrPoolGateWayA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayA.setStatus("current")
_TpDhcpServerAddrPoolGateWayB_Type = IpAddress
_TpDhcpServerAddrPoolGateWayB_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayB = _TpDhcpServerAddrPoolGateWayB_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 6),
    _TpDhcpServerAddrPoolGateWayB_Type()
)
tpDhcpServerAddrPoolGateWayB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayB.setStatus("current")
_TpDhcpServerAddrPoolGateWayC_Type = IpAddress
_TpDhcpServerAddrPoolGateWayC_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayC = _TpDhcpServerAddrPoolGateWayC_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 7),
    _TpDhcpServerAddrPoolGateWayC_Type()
)
tpDhcpServerAddrPoolGateWayC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayC.setStatus("current")
_TpDhcpServerAddrPoolGateWayD_Type = IpAddress
_TpDhcpServerAddrPoolGateWayD_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayD = _TpDhcpServerAddrPoolGateWayD_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 8),
    _TpDhcpServerAddrPoolGateWayD_Type()
)
tpDhcpServerAddrPoolGateWayD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayD.setStatus("current")
_TpDhcpServerAddrPoolGateWayE_Type = IpAddress
_TpDhcpServerAddrPoolGateWayE_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayE = _TpDhcpServerAddrPoolGateWayE_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 9),
    _TpDhcpServerAddrPoolGateWayE_Type()
)
tpDhcpServerAddrPoolGateWayE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayE.setStatus("current")
_TpDhcpServerAddrPoolGateWayF_Type = IpAddress
_TpDhcpServerAddrPoolGateWayF_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayF = _TpDhcpServerAddrPoolGateWayF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 10),
    _TpDhcpServerAddrPoolGateWayF_Type()
)
tpDhcpServerAddrPoolGateWayF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayF.setStatus("current")
_TpDhcpServerAddrPoolGateWayG_Type = IpAddress
_TpDhcpServerAddrPoolGateWayG_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayG = _TpDhcpServerAddrPoolGateWayG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 11),
    _TpDhcpServerAddrPoolGateWayG_Type()
)
tpDhcpServerAddrPoolGateWayG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayG.setStatus("current")
_TpDhcpServerAddrPoolGateWayH_Type = IpAddress
_TpDhcpServerAddrPoolGateWayH_Object = MibTableColumn
tpDhcpServerAddrPoolGateWayH = _TpDhcpServerAddrPoolGateWayH_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 12),
    _TpDhcpServerAddrPoolGateWayH_Type()
)
tpDhcpServerAddrPoolGateWayH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolGateWayH.setStatus("current")
_TpDhcpServerAddrPoolDnsA_Type = IpAddress
_TpDhcpServerAddrPoolDnsA_Object = MibTableColumn
tpDhcpServerAddrPoolDnsA = _TpDhcpServerAddrPoolDnsA_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 13),
    _TpDhcpServerAddrPoolDnsA_Type()
)
tpDhcpServerAddrPoolDnsA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsA.setStatus("current")
_TpDhcpServerAddrPoolDnsB_Type = IpAddress
_TpDhcpServerAddrPoolDnsB_Object = MibTableColumn
tpDhcpServerAddrPoolDnsB = _TpDhcpServerAddrPoolDnsB_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 14),
    _TpDhcpServerAddrPoolDnsB_Type()
)
tpDhcpServerAddrPoolDnsB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsB.setStatus("current")
_TpDhcpServerAddrPoolDnsC_Type = IpAddress
_TpDhcpServerAddrPoolDnsC_Object = MibTableColumn
tpDhcpServerAddrPoolDnsC = _TpDhcpServerAddrPoolDnsC_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 15),
    _TpDhcpServerAddrPoolDnsC_Type()
)
tpDhcpServerAddrPoolDnsC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsC.setStatus("current")
_TpDhcpServerAddrPoolDnsD_Type = IpAddress
_TpDhcpServerAddrPoolDnsD_Object = MibTableColumn
tpDhcpServerAddrPoolDnsD = _TpDhcpServerAddrPoolDnsD_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 16),
    _TpDhcpServerAddrPoolDnsD_Type()
)
tpDhcpServerAddrPoolDnsD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsD.setStatus("current")
_TpDhcpServerAddrPoolDnsE_Type = IpAddress
_TpDhcpServerAddrPoolDnsE_Object = MibTableColumn
tpDhcpServerAddrPoolDnsE = _TpDhcpServerAddrPoolDnsE_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 17),
    _TpDhcpServerAddrPoolDnsE_Type()
)
tpDhcpServerAddrPoolDnsE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsE.setStatus("current")
_TpDhcpServerAddrPoolDnsF_Type = IpAddress
_TpDhcpServerAddrPoolDnsF_Object = MibTableColumn
tpDhcpServerAddrPoolDnsF = _TpDhcpServerAddrPoolDnsF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 18),
    _TpDhcpServerAddrPoolDnsF_Type()
)
tpDhcpServerAddrPoolDnsF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsF.setStatus("current")
_TpDhcpServerAddrPoolDnsG_Type = IpAddress
_TpDhcpServerAddrPoolDnsG_Object = MibTableColumn
tpDhcpServerAddrPoolDnsG = _TpDhcpServerAddrPoolDnsG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 19),
    _TpDhcpServerAddrPoolDnsG_Type()
)
tpDhcpServerAddrPoolDnsG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsG.setStatus("current")
_TpDhcpServerAddrPoolDnsH_Type = IpAddress
_TpDhcpServerAddrPoolDnsH_Object = MibTableColumn
tpDhcpServerAddrPoolDnsH = _TpDhcpServerAddrPoolDnsH_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 20),
    _TpDhcpServerAddrPoolDnsH_Type()
)
tpDhcpServerAddrPoolDnsH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDnsH.setStatus("current")
_TpDhcpServerAddrPoolNBNServerA_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerA_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerA = _TpDhcpServerAddrPoolNBNServerA_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 21),
    _TpDhcpServerAddrPoolNBNServerA_Type()
)
tpDhcpServerAddrPoolNBNServerA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerA.setStatus("current")
_TpDhcpServerAddrPoolNBNServerB_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerB_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerB = _TpDhcpServerAddrPoolNBNServerB_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 22),
    _TpDhcpServerAddrPoolNBNServerB_Type()
)
tpDhcpServerAddrPoolNBNServerB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerB.setStatus("current")
_TpDhcpServerAddrPoolNBNServerC_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerC_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerC = _TpDhcpServerAddrPoolNBNServerC_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 23),
    _TpDhcpServerAddrPoolNBNServerC_Type()
)
tpDhcpServerAddrPoolNBNServerC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerC.setStatus("current")
_TpDhcpServerAddrPoolNBNServerD_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerD_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerD = _TpDhcpServerAddrPoolNBNServerD_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 24),
    _TpDhcpServerAddrPoolNBNServerD_Type()
)
tpDhcpServerAddrPoolNBNServerD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerD.setStatus("current")
_TpDhcpServerAddrPoolNBNServerE_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerE_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerE = _TpDhcpServerAddrPoolNBNServerE_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 25),
    _TpDhcpServerAddrPoolNBNServerE_Type()
)
tpDhcpServerAddrPoolNBNServerE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerE.setStatus("current")
_TpDhcpServerAddrPoolNBNServerF_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerF_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerF = _TpDhcpServerAddrPoolNBNServerF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 26),
    _TpDhcpServerAddrPoolNBNServerF_Type()
)
tpDhcpServerAddrPoolNBNServerF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerF.setStatus("current")
_TpDhcpServerAddrPoolNBNServerG_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerG_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerG = _TpDhcpServerAddrPoolNBNServerG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 27),
    _TpDhcpServerAddrPoolNBNServerG_Type()
)
tpDhcpServerAddrPoolNBNServerG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerG.setStatus("current")
_TpDhcpServerAddrPoolNBNServerH_Type = IpAddress
_TpDhcpServerAddrPoolNBNServerH_Object = MibTableColumn
tpDhcpServerAddrPoolNBNServerH = _TpDhcpServerAddrPoolNBNServerH_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 28),
    _TpDhcpServerAddrPoolNBNServerH_Type()
)
tpDhcpServerAddrPoolNBNServerH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNBNServerH.setStatus("current")


class _TpDhcpServerAddrPoolNetbiosNodeType_Type(Integer32):
    """Custom type tpDhcpServerAddrPoolNetbiosNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("hybrid", 8),
          ("mixed", 4),
          ("none", 0),
          ("peer-to-peer", 2))
    )


_TpDhcpServerAddrPoolNetbiosNodeType_Type.__name__ = "Integer32"
_TpDhcpServerAddrPoolNetbiosNodeType_Object = MibTableColumn
tpDhcpServerAddrPoolNetbiosNodeType = _TpDhcpServerAddrPoolNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 29),
    _TpDhcpServerAddrPoolNetbiosNodeType_Type()
)
tpDhcpServerAddrPoolNetbiosNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNetbiosNodeType.setStatus("current")
_TpDhcpServerAddrPoolNextServer_Type = IpAddress
_TpDhcpServerAddrPoolNextServer_Object = MibTableColumn
tpDhcpServerAddrPoolNextServer = _TpDhcpServerAddrPoolNextServer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 30),
    _TpDhcpServerAddrPoolNextServer_Type()
)
tpDhcpServerAddrPoolNextServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolNextServer.setStatus("current")


class _TpDhcpServerAddrPoolDomainName_Type(OctetString):
    """Custom type tpDhcpServerAddrPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TpDhcpServerAddrPoolDomainName_Type.__name__ = "OctetString"
_TpDhcpServerAddrPoolDomainName_Object = MibTableColumn
tpDhcpServerAddrPoolDomainName = _TpDhcpServerAddrPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 31),
    _TpDhcpServerAddrPoolDomainName_Type()
)
tpDhcpServerAddrPoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolDomainName.setStatus("current")


class _TpDhcpServerAddrPoolBootfile_Type(OctetString):
    """Custom type tpDhcpServerAddrPoolBootfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TpDhcpServerAddrPoolBootfile_Type.__name__ = "OctetString"
_TpDhcpServerAddrPoolBootfile_Object = MibTableColumn
tpDhcpServerAddrPoolBootfile = _TpDhcpServerAddrPoolBootfile_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 32),
    _TpDhcpServerAddrPoolBootfile_Type()
)
tpDhcpServerAddrPoolBootfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolBootfile.setStatus("current")
_TpDhcpServerAddrPoolStatus_Type = TPRowStatus
_TpDhcpServerAddrPoolStatus_Object = MibTableColumn
tpDhcpServerAddrPoolStatus = _TpDhcpServerAddrPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 33),
    _TpDhcpServerAddrPoolStatus_Type()
)
tpDhcpServerAddrPoolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerAddrPoolStatus.setStatus("current")
_TpDhcpServerStaticBindTable_Object = MibTable
tpDhcpServerStaticBindTable = _TpDhcpServerStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6)
)
if mibBuilder.loadTexts:
    tpDhcpServerStaticBindTable.setStatus("current")
_TpDhcpServerStaticBindEntry_Object = MibTableRow
tpDhcpServerStaticBindEntry = _TpDhcpServerStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1)
)
tpDhcpServerStaticBindEntry.setIndexNames(
    (0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerBindIpAddr"),
)
if mibBuilder.loadTexts:
    tpDhcpServerStaticBindEntry.setStatus("current")


class _TpDhcpServerStaticAddrPoolName_Type(OctetString):
    """Custom type tpDhcpServerStaticAddrPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TpDhcpServerStaticAddrPoolName_Type.__name__ = "OctetString"
_TpDhcpServerStaticAddrPoolName_Object = MibTableColumn
tpDhcpServerStaticAddrPoolName = _TpDhcpServerStaticAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 1),
    _TpDhcpServerStaticAddrPoolName_Type()
)
tpDhcpServerStaticAddrPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerStaticAddrPoolName.setStatus("current")
_TpDhcpServerBindIpAddr_Type = IpAddress
_TpDhcpServerBindIpAddr_Object = MibTableColumn
tpDhcpServerBindIpAddr = _TpDhcpServerBindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 2),
    _TpDhcpServerBindIpAddr_Type()
)
tpDhcpServerBindIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerBindIpAddr.setStatus("current")


class _TpDhcpServerStaticClientId_Type(OctetString):
    """Custom type tpDhcpServerStaticClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpDhcpServerStaticClientId_Type.__name__ = "OctetString"
_TpDhcpServerStaticClientId_Object = MibTableColumn
tpDhcpServerStaticClientId = _TpDhcpServerStaticClientId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 3),
    _TpDhcpServerStaticClientId_Type()
)
tpDhcpServerStaticClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerStaticClientId.setStatus("current")


class _TpDhcpServerMacAddr_Type(OctetString):
    """Custom type tpDhcpServerMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpDhcpServerMacAddr_Type.__name__ = "OctetString"
_TpDhcpServerMacAddr_Object = MibTableColumn
tpDhcpServerMacAddr = _TpDhcpServerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 4),
    _TpDhcpServerMacAddr_Type()
)
tpDhcpServerMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerMacAddr.setStatus("current")


class _TpDhcpServerHardwareType_Type(Integer32):
    """Custom type tpDhcpServerHardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ascii", -2),
          ("ethernet", 1),
          ("hex", -1),
          ("ieee802", 6))
    )


_TpDhcpServerHardwareType_Type.__name__ = "Integer32"
_TpDhcpServerHardwareType_Object = MibTableColumn
tpDhcpServerHardwareType = _TpDhcpServerHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 5),
    _TpDhcpServerHardwareType_Type()
)
tpDhcpServerHardwareType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerHardwareType.setStatus("current")
_TpDhcpServerStaticBindStatus_Type = TPRowStatus
_TpDhcpServerStaticBindStatus_Object = MibTableColumn
tpDhcpServerStaticBindStatus = _TpDhcpServerStaticBindStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 6),
    _TpDhcpServerStaticBindStatus_Type()
)
tpDhcpServerStaticBindStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerStaticBindStatus.setStatus("current")
_TpDhcpServerBindingTable_Object = MibTable
tpDhcpServerBindingTable = _TpDhcpServerBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7)
)
if mibBuilder.loadTexts:
    tpDhcpServerBindingTable.setStatus("current")
_TpDhcpServerBindingEntry_Object = MibTableRow
tpDhcpServerBindingEntry = _TpDhcpServerBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1)
)
tpDhcpServerBindingEntry.setIndexNames(
    (0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerBindingIp"),
)
if mibBuilder.loadTexts:
    tpDhcpServerBindingEntry.setStatus("current")
_TpDhcpServerBindingIp_Type = IpAddress
_TpDhcpServerBindingIp_Object = MibTableColumn
tpDhcpServerBindingIp = _TpDhcpServerBindingIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 1),
    _TpDhcpServerBindingIp_Type()
)
tpDhcpServerBindingIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerBindingIp.setStatus("current")


class _TpDhcpServerBindingClientId_Type(OctetString):
    """Custom type tpDhcpServerBindingClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TpDhcpServerBindingClientId_Type.__name__ = "OctetString"
_TpDhcpServerBindingClientId_Object = MibTableColumn
tpDhcpServerBindingClientId = _TpDhcpServerBindingClientId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 2),
    _TpDhcpServerBindingClientId_Type()
)
tpDhcpServerBindingClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerBindingClientId.setStatus("current")


class _TpDhcpServerBindingMac_Type(OctetString):
    """Custom type tpDhcpServerBindingMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpDhcpServerBindingMac_Type.__name__ = "OctetString"
_TpDhcpServerBindingMac_Object = MibTableColumn
tpDhcpServerBindingMac = _TpDhcpServerBindingMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 3),
    _TpDhcpServerBindingMac_Type()
)
tpDhcpServerBindingMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerBindingMac.setStatus("current")


class _TpDhcpServerBindingType_Type(Integer32):
    """Custom type tpDhcpServerBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_TpDhcpServerBindingType_Type.__name__ = "Integer32"
_TpDhcpServerBindingType_Object = MibTableColumn
tpDhcpServerBindingType = _TpDhcpServerBindingType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 4),
    _TpDhcpServerBindingType_Type()
)
tpDhcpServerBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerBindingType.setStatus("current")


class _TpDhcpServerBindingRemainTime_Type(OctetString):
    """Custom type tpDhcpServerBindingRemainTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpDhcpServerBindingRemainTime_Type.__name__ = "OctetString"
_TpDhcpServerBindingRemainTime_Object = MibTableColumn
tpDhcpServerBindingRemainTime = _TpDhcpServerBindingRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 5),
    _TpDhcpServerBindingRemainTime_Type()
)
tpDhcpServerBindingRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerBindingRemainTime.setStatus("current")
_TpDhcpServerBindingStatus_Type = TPRowStatus
_TpDhcpServerBindingStatus_Object = MibTableColumn
tpDhcpServerBindingStatus = _TpDhcpServerBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 6),
    _TpDhcpServerBindingStatus_Type()
)
tpDhcpServerBindingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDhcpServerBindingStatus.setStatus("current")


class _TpDhcpServerBindingClear_Type(Integer32):
    """Custom type tpDhcpServerBindingClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("remain", 0))
    )


_TpDhcpServerBindingClear_Type.__name__ = "Integer32"
_TpDhcpServerBindingClear_Object = MibScalar
tpDhcpServerBindingClear = _TpDhcpServerBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 8),
    _TpDhcpServerBindingClear_Type()
)
tpDhcpServerBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerBindingClear.setStatus("current")
_TpDhcpServerStatistics_ObjectIdentity = ObjectIdentity
tpDhcpServerStatistics = _TpDhcpServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9)
)
_TpDhcpServerStatisticsBootRequest_Type = Counter64
_TpDhcpServerStatisticsBootRequest_Object = MibScalar
tpDhcpServerStatisticsBootRequest = _TpDhcpServerStatisticsBootRequest_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 1),
    _TpDhcpServerStatisticsBootRequest_Type()
)
tpDhcpServerStatisticsBootRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsBootRequest.setStatus("current")
_TpDhcpServerStatisticsDiscover_Type = Counter64
_TpDhcpServerStatisticsDiscover_Object = MibScalar
tpDhcpServerStatisticsDiscover = _TpDhcpServerStatisticsDiscover_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 2),
    _TpDhcpServerStatisticsDiscover_Type()
)
tpDhcpServerStatisticsDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsDiscover.setStatus("current")
_TpDhcpServerStatisticsRequest_Type = Counter64
_TpDhcpServerStatisticsRequest_Object = MibScalar
tpDhcpServerStatisticsRequest = _TpDhcpServerStatisticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 3),
    _TpDhcpServerStatisticsRequest_Type()
)
tpDhcpServerStatisticsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsRequest.setStatus("current")
_TpDhcpServerStatisticsDecline_Type = Counter64
_TpDhcpServerStatisticsDecline_Object = MibScalar
tpDhcpServerStatisticsDecline = _TpDhcpServerStatisticsDecline_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 4),
    _TpDhcpServerStatisticsDecline_Type()
)
tpDhcpServerStatisticsDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsDecline.setStatus("current")
_TpDhcpServerStatisticsRelease_Type = Counter64
_TpDhcpServerStatisticsRelease_Object = MibScalar
tpDhcpServerStatisticsRelease = _TpDhcpServerStatisticsRelease_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 5),
    _TpDhcpServerStatisticsRelease_Type()
)
tpDhcpServerStatisticsRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsRelease.setStatus("current")
_TpDhcpServerStatisticsInform_Type = Counter64
_TpDhcpServerStatisticsInform_Object = MibScalar
tpDhcpServerStatisticsInform = _TpDhcpServerStatisticsInform_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 6),
    _TpDhcpServerStatisticsInform_Type()
)
tpDhcpServerStatisticsInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsInform.setStatus("current")
_TpDhcpServerStatisticsBootReply_Type = Counter64
_TpDhcpServerStatisticsBootReply_Object = MibScalar
tpDhcpServerStatisticsBootReply = _TpDhcpServerStatisticsBootReply_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 7),
    _TpDhcpServerStatisticsBootReply_Type()
)
tpDhcpServerStatisticsBootReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsBootReply.setStatus("current")
_TpDhcpServerStatisticsOffer_Type = Counter64
_TpDhcpServerStatisticsOffer_Object = MibScalar
tpDhcpServerStatisticsOffer = _TpDhcpServerStatisticsOffer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 8),
    _TpDhcpServerStatisticsOffer_Type()
)
tpDhcpServerStatisticsOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsOffer.setStatus("current")
_TpDhcpServerStatisticsAck_Type = Counter64
_TpDhcpServerStatisticsAck_Object = MibScalar
tpDhcpServerStatisticsAck = _TpDhcpServerStatisticsAck_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 9),
    _TpDhcpServerStatisticsAck_Type()
)
tpDhcpServerStatisticsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsAck.setStatus("current")
_TpDhcpServerStatisticsNak_Type = Counter64
_TpDhcpServerStatisticsNak_Object = MibScalar
tpDhcpServerStatisticsNak = _TpDhcpServerStatisticsNak_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 10),
    _TpDhcpServerStatisticsNak_Type()
)
tpDhcpServerStatisticsNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsNak.setStatus("current")


class _TpDhcpServerStatisticsClear_Type(Integer32):
    """Custom type tpDhcpServerStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("remain", 0))
    )


_TpDhcpServerStatisticsClear_Type.__name__ = "Integer32"
_TpDhcpServerStatisticsClear_Object = MibScalar
tpDhcpServerStatisticsClear = _TpDhcpServerStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 11),
    _TpDhcpServerStatisticsClear_Type()
)
tpDhcpServerStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerStatisticsClear.setStatus("current")


class _TpDhcpServerPingPackets_Type(Integer32):
    """Custom type tpDhcpServerPingPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TpDhcpServerPingPackets_Type.__name__ = "Integer32"
_TpDhcpServerPingPackets_Object = MibScalar
tpDhcpServerPingPackets = _TpDhcpServerPingPackets_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 10),
    _TpDhcpServerPingPackets_Type()
)
tpDhcpServerPingPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerPingPackets.setStatus("current")


class _TpDhcpServerPingTimeout_Type(Integer32):
    """Custom type tpDhcpServerPingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TpDhcpServerPingTimeout_Type.__name__ = "Integer32"
_TpDhcpServerPingTimeout_Object = MibScalar
tpDhcpServerPingTimeout = _TpDhcpServerPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 11),
    _TpDhcpServerPingTimeout_Type()
)
tpDhcpServerPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDhcpServerPingTimeout.setStatus("current")
_TplinkDhcpServerNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpServerNotifications = _TplinkDhcpServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 38, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPSERVER-MIB",
    **{"tplinkDhcpServerMIB": tplinkDhcpServerMIB,
       "tplinkDhcpServerMIBObjects": tplinkDhcpServerMIBObjects,
       "tpDhcpServerEnable": tpDhcpServerEnable,
       "tpDhcpServerVendorClassId": tpDhcpServerVendorClassId,
       "tpDhcpServerCapwapAcIp": tpDhcpServerCapwapAcIp,
       "tpDhcpServerUnusedIpTable": tpDhcpServerUnusedIpTable,
       "tpDhcpServerUnusedIpEntry": tpDhcpServerUnusedIpEntry,
       "tpDhcpServerUnusedStartIp": tpDhcpServerUnusedStartIp,
       "tpDhcpServerUnusedEndIp": tpDhcpServerUnusedEndIp,
       "tpDhcpServerUnusedIpStatus": tpDhcpServerUnusedIpStatus,
       "tpDhcpServerAddrPoolTable": tpDhcpServerAddrPoolTable,
       "tpDhcpServerAddrPoolEntry": tpDhcpServerAddrPoolEntry,
       "tpDhcpServerAddrPoolName": tpDhcpServerAddrPoolName,
       "tpDhcpServerAddrPoolNetwork": tpDhcpServerAddrPoolNetwork,
       "tpDhcpServerAddrPoolSubnetMask": tpDhcpServerAddrPoolSubnetMask,
       "tpDhcpServerAddrPoolRentTime": tpDhcpServerAddrPoolRentTime,
       "tpDhcpServerAddrPoolGateWayA": tpDhcpServerAddrPoolGateWayA,
       "tpDhcpServerAddrPoolGateWayB": tpDhcpServerAddrPoolGateWayB,
       "tpDhcpServerAddrPoolGateWayC": tpDhcpServerAddrPoolGateWayC,
       "tpDhcpServerAddrPoolGateWayD": tpDhcpServerAddrPoolGateWayD,
       "tpDhcpServerAddrPoolGateWayE": tpDhcpServerAddrPoolGateWayE,
       "tpDhcpServerAddrPoolGateWayF": tpDhcpServerAddrPoolGateWayF,
       "tpDhcpServerAddrPoolGateWayG": tpDhcpServerAddrPoolGateWayG,
       "tpDhcpServerAddrPoolGateWayH": tpDhcpServerAddrPoolGateWayH,
       "tpDhcpServerAddrPoolDnsA": tpDhcpServerAddrPoolDnsA,
       "tpDhcpServerAddrPoolDnsB": tpDhcpServerAddrPoolDnsB,
       "tpDhcpServerAddrPoolDnsC": tpDhcpServerAddrPoolDnsC,
       "tpDhcpServerAddrPoolDnsD": tpDhcpServerAddrPoolDnsD,
       "tpDhcpServerAddrPoolDnsE": tpDhcpServerAddrPoolDnsE,
       "tpDhcpServerAddrPoolDnsF": tpDhcpServerAddrPoolDnsF,
       "tpDhcpServerAddrPoolDnsG": tpDhcpServerAddrPoolDnsG,
       "tpDhcpServerAddrPoolDnsH": tpDhcpServerAddrPoolDnsH,
       "tpDhcpServerAddrPoolNBNServerA": tpDhcpServerAddrPoolNBNServerA,
       "tpDhcpServerAddrPoolNBNServerB": tpDhcpServerAddrPoolNBNServerB,
       "tpDhcpServerAddrPoolNBNServerC": tpDhcpServerAddrPoolNBNServerC,
       "tpDhcpServerAddrPoolNBNServerD": tpDhcpServerAddrPoolNBNServerD,
       "tpDhcpServerAddrPoolNBNServerE": tpDhcpServerAddrPoolNBNServerE,
       "tpDhcpServerAddrPoolNBNServerF": tpDhcpServerAddrPoolNBNServerF,
       "tpDhcpServerAddrPoolNBNServerG": tpDhcpServerAddrPoolNBNServerG,
       "tpDhcpServerAddrPoolNBNServerH": tpDhcpServerAddrPoolNBNServerH,
       "tpDhcpServerAddrPoolNetbiosNodeType": tpDhcpServerAddrPoolNetbiosNodeType,
       "tpDhcpServerAddrPoolNextServer": tpDhcpServerAddrPoolNextServer,
       "tpDhcpServerAddrPoolDomainName": tpDhcpServerAddrPoolDomainName,
       "tpDhcpServerAddrPoolBootfile": tpDhcpServerAddrPoolBootfile,
       "tpDhcpServerAddrPoolStatus": tpDhcpServerAddrPoolStatus,
       "tpDhcpServerStaticBindTable": tpDhcpServerStaticBindTable,
       "tpDhcpServerStaticBindEntry": tpDhcpServerStaticBindEntry,
       "tpDhcpServerStaticAddrPoolName": tpDhcpServerStaticAddrPoolName,
       "tpDhcpServerBindIpAddr": tpDhcpServerBindIpAddr,
       "tpDhcpServerStaticClientId": tpDhcpServerStaticClientId,
       "tpDhcpServerMacAddr": tpDhcpServerMacAddr,
       "tpDhcpServerHardwareType": tpDhcpServerHardwareType,
       "tpDhcpServerStaticBindStatus": tpDhcpServerStaticBindStatus,
       "tpDhcpServerBindingTable": tpDhcpServerBindingTable,
       "tpDhcpServerBindingEntry": tpDhcpServerBindingEntry,
       "tpDhcpServerBindingIp": tpDhcpServerBindingIp,
       "tpDhcpServerBindingClientId": tpDhcpServerBindingClientId,
       "tpDhcpServerBindingMac": tpDhcpServerBindingMac,
       "tpDhcpServerBindingType": tpDhcpServerBindingType,
       "tpDhcpServerBindingRemainTime": tpDhcpServerBindingRemainTime,
       "tpDhcpServerBindingStatus": tpDhcpServerBindingStatus,
       "tpDhcpServerBindingClear": tpDhcpServerBindingClear,
       "tpDhcpServerStatistics": tpDhcpServerStatistics,
       "tpDhcpServerStatisticsBootRequest": tpDhcpServerStatisticsBootRequest,
       "tpDhcpServerStatisticsDiscover": tpDhcpServerStatisticsDiscover,
       "tpDhcpServerStatisticsRequest": tpDhcpServerStatisticsRequest,
       "tpDhcpServerStatisticsDecline": tpDhcpServerStatisticsDecline,
       "tpDhcpServerStatisticsRelease": tpDhcpServerStatisticsRelease,
       "tpDhcpServerStatisticsInform": tpDhcpServerStatisticsInform,
       "tpDhcpServerStatisticsBootReply": tpDhcpServerStatisticsBootReply,
       "tpDhcpServerStatisticsOffer": tpDhcpServerStatisticsOffer,
       "tpDhcpServerStatisticsAck": tpDhcpServerStatisticsAck,
       "tpDhcpServerStatisticsNak": tpDhcpServerStatisticsNak,
       "tpDhcpServerStatisticsClear": tpDhcpServerStatisticsClear,
       "tpDhcpServerPingPackets": tpDhcpServerPingPackets,
       "tpDhcpServerPingTimeout": tpDhcpServerPingTimeout,
       "tplinkDhcpServerNotifications": tplinkDhcpServerNotifications}
)
