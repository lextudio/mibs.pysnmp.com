# SNMP MIB module (ACC-DHCP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-DHCP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:03 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccDHCP_ObjectIdentity = ObjectIdentity
accDHCP = _AccDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55)
)
_AccDHCPSrvTable_Object = MibTable
accDHCPSrvTable = _AccDHCPSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1)
)
if mibBuilder.loadTexts:
    accDHCPSrvTable.setStatus("mandatory")
_AccDHCPSrvEntry_Object = MibTableRow
accDHCPSrvEntry = _AccDHCPSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1)
)
accDHCPSrvEntry.setIndexNames(
    (0, "ACC-DHCP", "accDhcpSrvIfIndex"),
)
if mibBuilder.loadTexts:
    accDHCPSrvEntry.setStatus("mandatory")
_AccDhcpSrvIfIndex_Type = Integer32
_AccDhcpSrvIfIndex_Object = MibTableColumn
accDhcpSrvIfIndex = _AccDhcpSrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 1),
    _AccDhcpSrvIfIndex_Type()
)
accDhcpSrvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvIfIndex.setStatus("mandatory")


class _AccDhcpSrvAdmStatus_Type(Integer32):
    """Custom type accDhcpSrvAdmStatus based on Integer32"""
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


_AccDhcpSrvAdmStatus_Type.__name__ = "Integer32"
_AccDhcpSrvAdmStatus_Object = MibTableColumn
accDhcpSrvAdmStatus = _AccDhcpSrvAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 2),
    _AccDhcpSrvAdmStatus_Type()
)
accDhcpSrvAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvAdmStatus.setStatus("mandatory")


class _AccDhcpSrvOpStatus_Type(Integer32):
    """Custom type accDhcpSrvOpStatus based on Integer32"""
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


_AccDhcpSrvOpStatus_Type.__name__ = "Integer32"
_AccDhcpSrvOpStatus_Object = MibTableColumn
accDhcpSrvOpStatus = _AccDhcpSrvOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 3),
    _AccDhcpSrvOpStatus_Type()
)
accDhcpSrvOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvOpStatus.setStatus("mandatory")
_AccDhcpSrvStartIpAddr_Type = IpAddress
_AccDhcpSrvStartIpAddr_Object = MibTableColumn
accDhcpSrvStartIpAddr = _AccDhcpSrvStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 4),
    _AccDhcpSrvStartIpAddr_Type()
)
accDhcpSrvStartIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvStartIpAddr.setStatus("mandatory")
_AccDhcpSrvEndIpAddr_Type = IpAddress
_AccDhcpSrvEndIpAddr_Object = MibTableColumn
accDhcpSrvEndIpAddr = _AccDhcpSrvEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 5),
    _AccDhcpSrvEndIpAddr_Type()
)
accDhcpSrvEndIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvEndIpAddr.setStatus("mandatory")
_AccDhcpSrvLeaseLen_Type = TimeTicks
_AccDhcpSrvLeaseLen_Object = MibTableColumn
accDhcpSrvLeaseLen = _AccDhcpSrvLeaseLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 6),
    _AccDhcpSrvLeaseLen_Type()
)
accDhcpSrvLeaseLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvLeaseLen.setStatus("mandatory")
_AccDhcpSrvLeaseCnt_Type = Gauge32
_AccDhcpSrvLeaseCnt_Object = MibTableColumn
accDhcpSrvLeaseCnt = _AccDhcpSrvLeaseCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 7),
    _AccDhcpSrvLeaseCnt_Type()
)
accDhcpSrvLeaseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvLeaseCnt.setStatus("mandatory")
_AccDhcpSrvRenewals_Type = Counter32
_AccDhcpSrvRenewals_Object = MibTableColumn
accDhcpSrvRenewals = _AccDhcpSrvRenewals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 8),
    _AccDhcpSrvRenewals_Type()
)
accDhcpSrvRenewals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvRenewals.setStatus("mandatory")
_AccDhcpSrvRefusals_Type = Counter32
_AccDhcpSrvRefusals_Object = MibTableColumn
accDhcpSrvRefusals = _AccDhcpSrvRefusals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 9),
    _AccDhcpSrvRefusals_Type()
)
accDhcpSrvRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvRefusals.setStatus("mandatory")
_AccDhcpSrvUnknowns_Type = Counter32
_AccDhcpSrvUnknowns_Object = MibTableColumn
accDhcpSrvUnknowns = _AccDhcpSrvUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 10),
    _AccDhcpSrvUnknowns_Type()
)
accDhcpSrvUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvUnknowns.setStatus("mandatory")
_AccDhcpSrvInforms_Type = Counter32
_AccDhcpSrvInforms_Object = MibTableColumn
accDhcpSrvInforms = _AccDhcpSrvInforms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 11),
    _AccDhcpSrvInforms_Type()
)
accDhcpSrvInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvInforms.setStatus("mandatory")
_AccDhcpSrvDiscovers_Type = Counter32
_AccDhcpSrvDiscovers_Object = MibTableColumn
accDhcpSrvDiscovers = _AccDhcpSrvDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 12),
    _AccDhcpSrvDiscovers_Type()
)
accDhcpSrvDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvDiscovers.setStatus("mandatory")
_AccDhcpSrvRequests_Type = Counter32
_AccDhcpSrvRequests_Object = MibTableColumn
accDhcpSrvRequests = _AccDhcpSrvRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 13),
    _AccDhcpSrvRequests_Type()
)
accDhcpSrvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvRequests.setStatus("mandatory")
_AccDhcpSrvReleases_Type = Counter32
_AccDhcpSrvReleases_Object = MibTableColumn
accDhcpSrvReleases = _AccDhcpSrvReleases_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 14),
    _AccDhcpSrvReleases_Type()
)
accDhcpSrvReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvReleases.setStatus("mandatory")
_AccDhcpSrvDeclines_Type = Counter32
_AccDhcpSrvDeclines_Object = MibTableColumn
accDhcpSrvDeclines = _AccDhcpSrvDeclines_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 15),
    _AccDhcpSrvDeclines_Type()
)
accDhcpSrvDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvDeclines.setStatus("mandatory")
_AccDhcpSrvReclaimeds_Type = Counter32
_AccDhcpSrvReclaimeds_Object = MibTableColumn
accDhcpSrvReclaimeds = _AccDhcpSrvReclaimeds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 16),
    _AccDhcpSrvReclaimeds_Type()
)
accDhcpSrvReclaimeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvReclaimeds.setStatus("mandatory")
_AccDhcpSrvExpireds_Type = Counter32
_AccDhcpSrvExpireds_Object = MibTableColumn
accDhcpSrvExpireds = _AccDhcpSrvExpireds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 17),
    _AccDhcpSrvExpireds_Type()
)
accDhcpSrvExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvExpireds.setStatus("mandatory")
_AccDhcpSrvAcks_Type = Counter32
_AccDhcpSrvAcks_Object = MibTableColumn
accDhcpSrvAcks = _AccDhcpSrvAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 18),
    _AccDhcpSrvAcks_Type()
)
accDhcpSrvAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvAcks.setStatus("mandatory")
_AccDhcpSrvNacks_Type = Counter32
_AccDhcpSrvNacks_Object = MibTableColumn
accDhcpSrvNacks = _AccDhcpSrvNacks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 19),
    _AccDhcpSrvNacks_Type()
)
accDhcpSrvNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvNacks.setStatus("mandatory")
_AccDhcpSrvOffers_Type = Counter32
_AccDhcpSrvOffers_Object = MibTableColumn
accDhcpSrvOffers = _AccDhcpSrvOffers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 20),
    _AccDhcpSrvOffers_Type()
)
accDhcpSrvOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvOffers.setStatus("mandatory")
_AccDhcpSrvDomainName_Type = OctetString
_AccDhcpSrvDomainName_Object = MibTableColumn
accDhcpSrvDomainName = _AccDhcpSrvDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 21),
    _AccDhcpSrvDomainName_Type()
)
accDhcpSrvDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvDomainName.setStatus("mandatory")
_AccDhcpSrvDomainServer_Type = IpAddress
_AccDhcpSrvDomainServer_Object = MibTableColumn
accDhcpSrvDomainServer = _AccDhcpSrvDomainServer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 22),
    _AccDhcpSrvDomainServer_Type()
)
accDhcpSrvDomainServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvDomainServer.setStatus("mandatory")


class _AccDhcpSrvMessageLevel_Type(Integer32):
    """Custom type accDhcpSrvMessageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccDhcpSrvMessageLevel_Type.__name__ = "Integer32"
_AccDhcpSrvMessageLevel_Object = MibTableColumn
accDhcpSrvMessageLevel = _AccDhcpSrvMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 23),
    _AccDhcpSrvMessageLevel_Type()
)
accDhcpSrvMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvMessageLevel.setStatus("mandatory")
_AccDhcpSrvDomainServer1_Type = IpAddress
_AccDhcpSrvDomainServer1_Object = MibTableColumn
accDhcpSrvDomainServer1 = _AccDhcpSrvDomainServer1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 24),
    _AccDhcpSrvDomainServer1_Type()
)
accDhcpSrvDomainServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvDomainServer1.setStatus("mandatory")
_AccDhcpSrvDomainServer2_Type = IpAddress
_AccDhcpSrvDomainServer2_Object = MibTableColumn
accDhcpSrvDomainServer2 = _AccDhcpSrvDomainServer2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 25),
    _AccDhcpSrvDomainServer2_Type()
)
accDhcpSrvDomainServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvDomainServer2.setStatus("mandatory")
_AccDhcpSrvDomainServer3_Type = IpAddress
_AccDhcpSrvDomainServer3_Object = MibTableColumn
accDhcpSrvDomainServer3 = _AccDhcpSrvDomainServer3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 26),
    _AccDhcpSrvDomainServer3_Type()
)
accDhcpSrvDomainServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvDomainServer3.setStatus("mandatory")
_AccDhcpSrvDomainServer4_Type = IpAddress
_AccDhcpSrvDomainServer4_Object = MibTableColumn
accDhcpSrvDomainServer4 = _AccDhcpSrvDomainServer4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 27),
    _AccDhcpSrvDomainServer4_Type()
)
accDhcpSrvDomainServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvDomainServer4.setStatus("mandatory")
_AccDhcpSrvNetBiosServer1_Type = IpAddress
_AccDhcpSrvNetBiosServer1_Object = MibTableColumn
accDhcpSrvNetBiosServer1 = _AccDhcpSrvNetBiosServer1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 28),
    _AccDhcpSrvNetBiosServer1_Type()
)
accDhcpSrvNetBiosServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvNetBiosServer1.setStatus("mandatory")
_AccDhcpSrvNetBiosServer2_Type = IpAddress
_AccDhcpSrvNetBiosServer2_Object = MibTableColumn
accDhcpSrvNetBiosServer2 = _AccDhcpSrvNetBiosServer2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 29),
    _AccDhcpSrvNetBiosServer2_Type()
)
accDhcpSrvNetBiosServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvNetBiosServer2.setStatus("mandatory")
_AccDhcpSrvNetBiosServer3_Type = IpAddress
_AccDhcpSrvNetBiosServer3_Object = MibTableColumn
accDhcpSrvNetBiosServer3 = _AccDhcpSrvNetBiosServer3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 30),
    _AccDhcpSrvNetBiosServer3_Type()
)
accDhcpSrvNetBiosServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvNetBiosServer3.setStatus("mandatory")
_AccDhcpSrvNetBiosServer4_Type = IpAddress
_AccDhcpSrvNetBiosServer4_Object = MibTableColumn
accDhcpSrvNetBiosServer4 = _AccDhcpSrvNetBiosServer4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 31),
    _AccDhcpSrvNetBiosServer4_Type()
)
accDhcpSrvNetBiosServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvNetBiosServer4.setStatus("mandatory")
_AccDhcpSrvAutoDialPort_Type = Integer32
_AccDhcpSrvAutoDialPort_Object = MibTableColumn
accDhcpSrvAutoDialPort = _AccDhcpSrvAutoDialPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 32),
    _AccDhcpSrvAutoDialPort_Type()
)
accDhcpSrvAutoDialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDhcpSrvAutoDialPort.setStatus("mandatory")
_AccDhcpSrvAutoDns1_Type = IpAddress
_AccDhcpSrvAutoDns1_Object = MibTableColumn
accDhcpSrvAutoDns1 = _AccDhcpSrvAutoDns1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 33),
    _AccDhcpSrvAutoDns1_Type()
)
accDhcpSrvAutoDns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvAutoDns1.setStatus("mandatory")
_AccDhcpSrvAutoDns2_Type = IpAddress
_AccDhcpSrvAutoDns2_Object = MibTableColumn
accDhcpSrvAutoDns2 = _AccDhcpSrvAutoDns2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 34),
    _AccDhcpSrvAutoDns2_Type()
)
accDhcpSrvAutoDns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvAutoDns2.setStatus("mandatory")
_AccDhcpSrvAutoNbns1_Type = IpAddress
_AccDhcpSrvAutoNbns1_Object = MibTableColumn
accDhcpSrvAutoNbns1 = _AccDhcpSrvAutoNbns1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 35),
    _AccDhcpSrvAutoNbns1_Type()
)
accDhcpSrvAutoNbns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvAutoNbns1.setStatus("mandatory")
_AccDhcpSrvAutoNbns2_Type = IpAddress
_AccDhcpSrvAutoNbns2_Object = MibTableColumn
accDhcpSrvAutoNbns2 = _AccDhcpSrvAutoNbns2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 1, 1, 36),
    _AccDhcpSrvAutoNbns2_Type()
)
accDhcpSrvAutoNbns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvAutoNbns2.setStatus("mandatory")
_AccDHCPSrvLeaseTable_Object = MibTable
accDHCPSrvLeaseTable = _AccDHCPSrvLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 2)
)
if mibBuilder.loadTexts:
    accDHCPSrvLeaseTable.setStatus("mandatory")
_AccDHCPSrvLeaseEntry_Object = MibTableRow
accDHCPSrvLeaseEntry = _AccDHCPSrvLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 2, 1)
)
accDHCPSrvLeaseEntry.setIndexNames(
    (0, "ACC-DHCP", "accDhcpSrvLeaseTblIndex"),
)
if mibBuilder.loadTexts:
    accDHCPSrvLeaseEntry.setStatus("mandatory")
_AccDhcpSrvLeaseTblAddr_Type = IpAddress
_AccDhcpSrvLeaseTblAddr_Object = MibTableColumn
accDhcpSrvLeaseTblAddr = _AccDhcpSrvLeaseTblAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 2, 1, 1),
    _AccDhcpSrvLeaseTblAddr_Type()
)
accDhcpSrvLeaseTblAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvLeaseTblAddr.setStatus("mandatory")
_AccDhcpSrvLeaseTblIndex_Type = Integer32
_AccDhcpSrvLeaseTblIndex_Object = MibTableColumn
accDhcpSrvLeaseTblIndex = _AccDhcpSrvLeaseTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 2, 1, 2),
    _AccDhcpSrvLeaseTblIndex_Type()
)
accDhcpSrvLeaseTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvLeaseTblIndex.setStatus("mandatory")
_AccDhcpSrvLeaseTblClient_Type = OctetString
_AccDhcpSrvLeaseTblClient_Object = MibTableColumn
accDhcpSrvLeaseTblClient = _AccDhcpSrvLeaseTblClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 2, 1, 3),
    _AccDhcpSrvLeaseTblClient_Type()
)
accDhcpSrvLeaseTblClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvLeaseTblClient.setStatus("mandatory")
_AccDhcpSrvLeaseTblTime_Type = TimeTicks
_AccDhcpSrvLeaseTblTime_Object = MibTableColumn
accDhcpSrvLeaseTblTime = _AccDhcpSrvLeaseTblTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 55, 2, 1, 4),
    _AccDhcpSrvLeaseTblTime_Type()
)
accDhcpSrvLeaseTblTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDhcpSrvLeaseTblTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-DHCP",
    **{"accDHCP": accDHCP,
       "accDHCPSrvTable": accDHCPSrvTable,
       "accDHCPSrvEntry": accDHCPSrvEntry,
       "accDhcpSrvIfIndex": accDhcpSrvIfIndex,
       "accDhcpSrvAdmStatus": accDhcpSrvAdmStatus,
       "accDhcpSrvOpStatus": accDhcpSrvOpStatus,
       "accDhcpSrvStartIpAddr": accDhcpSrvStartIpAddr,
       "accDhcpSrvEndIpAddr": accDhcpSrvEndIpAddr,
       "accDhcpSrvLeaseLen": accDhcpSrvLeaseLen,
       "accDhcpSrvLeaseCnt": accDhcpSrvLeaseCnt,
       "accDhcpSrvRenewals": accDhcpSrvRenewals,
       "accDhcpSrvRefusals": accDhcpSrvRefusals,
       "accDhcpSrvUnknowns": accDhcpSrvUnknowns,
       "accDhcpSrvInforms": accDhcpSrvInforms,
       "accDhcpSrvDiscovers": accDhcpSrvDiscovers,
       "accDhcpSrvRequests": accDhcpSrvRequests,
       "accDhcpSrvReleases": accDhcpSrvReleases,
       "accDhcpSrvDeclines": accDhcpSrvDeclines,
       "accDhcpSrvReclaimeds": accDhcpSrvReclaimeds,
       "accDhcpSrvExpireds": accDhcpSrvExpireds,
       "accDhcpSrvAcks": accDhcpSrvAcks,
       "accDhcpSrvNacks": accDhcpSrvNacks,
       "accDhcpSrvOffers": accDhcpSrvOffers,
       "accDhcpSrvDomainName": accDhcpSrvDomainName,
       "accDhcpSrvDomainServer": accDhcpSrvDomainServer,
       "accDhcpSrvMessageLevel": accDhcpSrvMessageLevel,
       "accDhcpSrvDomainServer1": accDhcpSrvDomainServer1,
       "accDhcpSrvDomainServer2": accDhcpSrvDomainServer2,
       "accDhcpSrvDomainServer3": accDhcpSrvDomainServer3,
       "accDhcpSrvDomainServer4": accDhcpSrvDomainServer4,
       "accDhcpSrvNetBiosServer1": accDhcpSrvNetBiosServer1,
       "accDhcpSrvNetBiosServer2": accDhcpSrvNetBiosServer2,
       "accDhcpSrvNetBiosServer3": accDhcpSrvNetBiosServer3,
       "accDhcpSrvNetBiosServer4": accDhcpSrvNetBiosServer4,
       "accDhcpSrvAutoDialPort": accDhcpSrvAutoDialPort,
       "accDhcpSrvAutoDns1": accDhcpSrvAutoDns1,
       "accDhcpSrvAutoDns2": accDhcpSrvAutoDns2,
       "accDhcpSrvAutoNbns1": accDhcpSrvAutoNbns1,
       "accDhcpSrvAutoNbns2": accDhcpSrvAutoNbns2,
       "accDHCPSrvLeaseTable": accDHCPSrvLeaseTable,
       "accDHCPSrvLeaseEntry": accDHCPSrvLeaseEntry,
       "accDhcpSrvLeaseTblAddr": accDhcpSrvLeaseTblAddr,
       "accDhcpSrvLeaseTblIndex": accDhcpSrvLeaseTblIndex,
       "accDhcpSrvLeaseTblClient": accDhcpSrvLeaseTblClient,
       "accDhcpSrvLeaseTblTime": accDhcpSrvLeaseTblTime}
)
