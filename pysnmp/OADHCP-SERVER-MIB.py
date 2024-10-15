# SNMP MIB module (OADHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OADHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:33 2024
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
 NotificationType,
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
    "NotificationType",
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



class HostName(DisplayString):
    """Custom type HostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insert", 3),
          ("invalid", 2),
          ("valid", 1))
    )





class ObjectStatus(Integer32):
    """Custom type ObjectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("other", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaDhcp_ObjectIdentity = ObjectIdentity
oaDhcp = _OaDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11)
)
_OaDhcpServer_ObjectIdentity = ObjectIdentity
oaDhcpServer = _OaDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1)
)
_OaDhcpServerGeneral_ObjectIdentity = ObjectIdentity
oaDhcpServerGeneral = _OaDhcpServerGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1)
)
_OaDhcpServerStatus_Type = ObjectStatus
_OaDhcpServerStatus_Object = MibScalar
oaDhcpServerStatus = _OaDhcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 1),
    _OaDhcpServerStatus_Type()
)
oaDhcpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpServerStatus.setStatus("mandatory")


class _OaDhcpNetbiosNodeType_Type(Integer32):
    """Custom type oaDhcpNetbiosNodeType based on Integer32"""
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
        *(("B-node", 2),
          ("H-node", 5),
          ("M-node", 4),
          ("P-node", 3),
          ("other", 1))
    )


_OaDhcpNetbiosNodeType_Type.__name__ = "Integer32"
_OaDhcpNetbiosNodeType_Object = MibScalar
oaDhcpNetbiosNodeType = _OaDhcpNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 2),
    _OaDhcpNetbiosNodeType_Type()
)
oaDhcpNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpNetbiosNodeType.setStatus("mandatory")
_OaDhcpDomainName_Type = HostName
_OaDhcpDomainName_Object = MibScalar
oaDhcpDomainName = _OaDhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 3),
    _OaDhcpDomainName_Type()
)
oaDhcpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpDomainName.setStatus("mandatory")
_OaDhcpDefaultLeaseTime_Type = Integer32
_OaDhcpDefaultLeaseTime_Object = MibScalar
oaDhcpDefaultLeaseTime = _OaDhcpDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 4),
    _OaDhcpDefaultLeaseTime_Type()
)
oaDhcpDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpDefaultLeaseTime.setStatus("mandatory")
_OaDhcpMaxLeaseTime_Type = Integer32
_OaDhcpMaxLeaseTime_Object = MibScalar
oaDhcpMaxLeaseTime = _OaDhcpMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 5),
    _OaDhcpMaxLeaseTime_Type()
)
oaDhcpMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpMaxLeaseTime.setStatus("mandatory")
_OaDhcpDNSTable_Object = MibTable
oaDhcpDNSTable = _OaDhcpDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    oaDhcpDNSTable.setStatus("mandatory")
_OaDhcpDNSEntry_Object = MibTableRow
oaDhcpDNSEntry = _OaDhcpDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1)
)
oaDhcpDNSEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpDNSNum"),
)
if mibBuilder.loadTexts:
    oaDhcpDNSEntry.setStatus("mandatory")
_OaDhcpDNSNum_Type = Integer32
_OaDhcpDNSNum_Object = MibTableColumn
oaDhcpDNSNum = _OaDhcpDNSNum_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1, 1),
    _OaDhcpDNSNum_Type()
)
oaDhcpDNSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpDNSNum.setStatus("mandatory")
_OaDhcpDNSIp_Type = IpAddress
_OaDhcpDNSIp_Object = MibTableColumn
oaDhcpDNSIp = _OaDhcpDNSIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1, 2),
    _OaDhcpDNSIp_Type()
)
oaDhcpDNSIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpDNSIp.setStatus("mandatory")
_OaDhcpDNSStatus_Type = EntryStatus
_OaDhcpDNSStatus_Object = MibTableColumn
oaDhcpDNSStatus = _OaDhcpDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1, 3),
    _OaDhcpDNSStatus_Type()
)
oaDhcpDNSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpDNSStatus.setStatus("mandatory")
_OaDhcpNetbiosServersTable_Object = MibTable
oaDhcpNetbiosServersTable = _OaDhcpNetbiosServersTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    oaDhcpNetbiosServersTable.setStatus("mandatory")
_OaDhcpNetbiosServersEntry_Object = MibTableRow
oaDhcpNetbiosServersEntry = _OaDhcpNetbiosServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1)
)
oaDhcpNetbiosServersEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpNetbiosServerNum"),
)
if mibBuilder.loadTexts:
    oaDhcpNetbiosServersEntry.setStatus("mandatory")
_OaDhcpNetbiosServerNum_Type = Integer32
_OaDhcpNetbiosServerNum_Object = MibTableColumn
oaDhcpNetbiosServerNum = _OaDhcpNetbiosServerNum_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1, 1),
    _OaDhcpNetbiosServerNum_Type()
)
oaDhcpNetbiosServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpNetbiosServerNum.setStatus("mandatory")
_OaDhcpNetbiosServerIp_Type = IpAddress
_OaDhcpNetbiosServerIp_Object = MibTableColumn
oaDhcpNetbiosServerIp = _OaDhcpNetbiosServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1, 2),
    _OaDhcpNetbiosServerIp_Type()
)
oaDhcpNetbiosServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpNetbiosServerIp.setStatus("mandatory")
_OaDhcpNetbiosServerStatus_Type = EntryStatus
_OaDhcpNetbiosServerStatus_Object = MibTableColumn
oaDhcpNetbiosServerStatus = _OaDhcpNetbiosServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1, 3),
    _OaDhcpNetbiosServerStatus_Type()
)
oaDhcpNetbiosServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpNetbiosServerStatus.setStatus("mandatory")
_OaDhcpSubnetConfigTable_Object = MibTable
oaDhcpSubnetConfigTable = _OaDhcpSubnetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4)
)
if mibBuilder.loadTexts:
    oaDhcpSubnetConfigTable.setStatus("mandatory")
_OaDhcpSubnetConfigEntry_Object = MibTableRow
oaDhcpSubnetConfigEntry = _OaDhcpSubnetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1)
)
oaDhcpSubnetConfigEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpInterfaceName"),
    (0, "OADHCP-SERVER-MIB", "oaDhcpSubnetIp"),
    (0, "OADHCP-SERVER-MIB", "oaDhcpSubnetMask"),
)
if mibBuilder.loadTexts:
    oaDhcpSubnetConfigEntry.setStatus("mandatory")
_OaDhcpInterfaceName_Type = DisplayString
_OaDhcpInterfaceName_Object = MibTableColumn
oaDhcpInterfaceName = _OaDhcpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 1),
    _OaDhcpInterfaceName_Type()
)
oaDhcpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpInterfaceName.setStatus("mandatory")
_OaDhcpSubnetIp_Type = IpAddress
_OaDhcpSubnetIp_Object = MibTableColumn
oaDhcpSubnetIp = _OaDhcpSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 2),
    _OaDhcpSubnetIp_Type()
)
oaDhcpSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpSubnetIp.setStatus("mandatory")
_OaDhcpSubnetMask_Type = IpAddress
_OaDhcpSubnetMask_Object = MibTableColumn
oaDhcpSubnetMask = _OaDhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 3),
    _OaDhcpSubnetMask_Type()
)
oaDhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpSubnetMask.setStatus("mandatory")
_OaDhcpOptionSubnetMask_Type = IpAddress
_OaDhcpOptionSubnetMask_Object = MibTableColumn
oaDhcpOptionSubnetMask = _OaDhcpOptionSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 4),
    _OaDhcpOptionSubnetMask_Type()
)
oaDhcpOptionSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpOptionSubnetMask.setStatus("mandatory")
_OaDhcpIsOptionMask_Type = ObjectStatus
_OaDhcpIsOptionMask_Object = MibTableColumn
oaDhcpIsOptionMask = _OaDhcpIsOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 5),
    _OaDhcpIsOptionMask_Type()
)
oaDhcpIsOptionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpIsOptionMask.setStatus("mandatory")
_OaDhcpSubnetConfigStatus_Type = EntryStatus
_OaDhcpSubnetConfigStatus_Object = MibTableColumn
oaDhcpSubnetConfigStatus = _OaDhcpSubnetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 6),
    _OaDhcpSubnetConfigStatus_Type()
)
oaDhcpSubnetConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpSubnetConfigStatus.setStatus("mandatory")
_OaDhcpIpRangeTable_Object = MibTable
oaDhcpIpRangeTable = _OaDhcpIpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5)
)
if mibBuilder.loadTexts:
    oaDhcpIpRangeTable.setStatus("mandatory")
_OaDhcpIpRangeEntry_Object = MibTableRow
oaDhcpIpRangeEntry = _OaDhcpIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1)
)
oaDhcpIpRangeEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpIpRangeSubnetIp"),
    (0, "OADHCP-SERVER-MIB", "oaDhcpIpRangeSubnetMask"),
    (0, "OADHCP-SERVER-MIB", "oaDhcpIpRangeStart"),
)
if mibBuilder.loadTexts:
    oaDhcpIpRangeEntry.setStatus("mandatory")
_OaDhcpIpRangeSubnetIp_Type = IpAddress
_OaDhcpIpRangeSubnetIp_Object = MibTableColumn
oaDhcpIpRangeSubnetIp = _OaDhcpIpRangeSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 1),
    _OaDhcpIpRangeSubnetIp_Type()
)
oaDhcpIpRangeSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpIpRangeSubnetIp.setStatus("mandatory")
_OaDhcpIpRangeSubnetMask_Type = IpAddress
_OaDhcpIpRangeSubnetMask_Object = MibTableColumn
oaDhcpIpRangeSubnetMask = _OaDhcpIpRangeSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 2),
    _OaDhcpIpRangeSubnetMask_Type()
)
oaDhcpIpRangeSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpIpRangeSubnetMask.setStatus("mandatory")
_OaDhcpIpRangeStart_Type = IpAddress
_OaDhcpIpRangeStart_Object = MibTableColumn
oaDhcpIpRangeStart = _OaDhcpIpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 3),
    _OaDhcpIpRangeStart_Type()
)
oaDhcpIpRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpIpRangeStart.setStatus("mandatory")
_OaDhcpIpRangeEnd_Type = IpAddress
_OaDhcpIpRangeEnd_Object = MibTableColumn
oaDhcpIpRangeEnd = _OaDhcpIpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 4),
    _OaDhcpIpRangeEnd_Type()
)
oaDhcpIpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpIpRangeEnd.setStatus("mandatory")
_OaDhcpIpRangeStatus_Type = EntryStatus
_OaDhcpIpRangeStatus_Object = MibTableColumn
oaDhcpIpRangeStatus = _OaDhcpIpRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 5),
    _OaDhcpIpRangeStatus_Type()
)
oaDhcpIpRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpIpRangeStatus.setStatus("mandatory")
_OaDhcpDefaultGWTable_Object = MibTable
oaDhcpDefaultGWTable = _OaDhcpDefaultGWTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6)
)
if mibBuilder.loadTexts:
    oaDhcpDefaultGWTable.setStatus("mandatory")
_OaDhcpDefaultGWEntry_Object = MibTableRow
oaDhcpDefaultGWEntry = _OaDhcpDefaultGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1)
)
oaDhcpDefaultGWEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpDefaultGWSubnetIp"),
    (0, "OADHCP-SERVER-MIB", "oaDhcpDefaultGWSubnetMask"),
    (0, "OADHCP-SERVER-MIB", "oaDhcpDefaultGWIp"),
)
if mibBuilder.loadTexts:
    oaDhcpDefaultGWEntry.setStatus("mandatory")
_OaDhcpDefaultGWSubnetIp_Type = IpAddress
_OaDhcpDefaultGWSubnetIp_Object = MibTableColumn
oaDhcpDefaultGWSubnetIp = _OaDhcpDefaultGWSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 1),
    _OaDhcpDefaultGWSubnetIp_Type()
)
oaDhcpDefaultGWSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpDefaultGWSubnetIp.setStatus("mandatory")
_OaDhcpDefaultGWSubnetMask_Type = IpAddress
_OaDhcpDefaultGWSubnetMask_Object = MibTableColumn
oaDhcpDefaultGWSubnetMask = _OaDhcpDefaultGWSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 2),
    _OaDhcpDefaultGWSubnetMask_Type()
)
oaDhcpDefaultGWSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpDefaultGWSubnetMask.setStatus("mandatory")
_OaDhcpDefaultGWIp_Type = IpAddress
_OaDhcpDefaultGWIp_Object = MibTableColumn
oaDhcpDefaultGWIp = _OaDhcpDefaultGWIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 3),
    _OaDhcpDefaultGWIp_Type()
)
oaDhcpDefaultGWIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpDefaultGWIp.setStatus("mandatory")
_OaDhcpDefaultGWStatus_Type = EntryStatus
_OaDhcpDefaultGWStatus_Object = MibTableColumn
oaDhcpDefaultGWStatus = _OaDhcpDefaultGWStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 4),
    _OaDhcpDefaultGWStatus_Type()
)
oaDhcpDefaultGWStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpDefaultGWStatus.setStatus("mandatory")
_OaDhcpRelay_ObjectIdentity = ObjectIdentity
oaDhcpRelay = _OaDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2)
)
_OaDhcpRelayGeneral_ObjectIdentity = ObjectIdentity
oaDhcpRelayGeneral = _OaDhcpRelayGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 1)
)
_OaDhcpRelayStatus_Type = ObjectStatus
_OaDhcpRelayStatus_Object = MibScalar
oaDhcpRelayStatus = _OaDhcpRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 1, 1),
    _OaDhcpRelayStatus_Type()
)
oaDhcpRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpRelayStatus.setStatus("mandatory")


class _OaDhcpRelayClearConfig_Type(Integer32):
    """Custom type oaDhcpRelayClearConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("None", 1),
          ("ResetConfig", 2))
    )


_OaDhcpRelayClearConfig_Type.__name__ = "Integer32"
_OaDhcpRelayClearConfig_Object = MibScalar
oaDhcpRelayClearConfig = _OaDhcpRelayClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 1, 2),
    _OaDhcpRelayClearConfig_Type()
)
oaDhcpRelayClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpRelayClearConfig.setStatus("mandatory")
_OaDhcpRelayServerTable_Object = MibTable
oaDhcpRelayServerTable = _OaDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    oaDhcpRelayServerTable.setStatus("mandatory")
_OaDhcpRelayServerEntry_Object = MibTableRow
oaDhcpRelayServerEntry = _OaDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2, 1)
)
oaDhcpRelayServerEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpRelayServerIp"),
)
if mibBuilder.loadTexts:
    oaDhcpRelayServerEntry.setStatus("mandatory")
_OaDhcpRelayServerIp_Type = IpAddress
_OaDhcpRelayServerIp_Object = MibTableColumn
oaDhcpRelayServerIp = _OaDhcpRelayServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2, 1, 1),
    _OaDhcpRelayServerIp_Type()
)
oaDhcpRelayServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpRelayServerIp.setStatus("mandatory")
_OaDhcpRelayServerStatus_Type = EntryStatus
_OaDhcpRelayServerStatus_Object = MibTableColumn
oaDhcpRelayServerStatus = _OaDhcpRelayServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2, 1, 2),
    _OaDhcpRelayServerStatus_Type()
)
oaDhcpRelayServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpRelayServerStatus.setStatus("mandatory")
_OaDhcpRelayInterfaceTable_Object = MibTable
oaDhcpRelayInterfaceTable = _OaDhcpRelayInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3)
)
if mibBuilder.loadTexts:
    oaDhcpRelayInterfaceTable.setStatus("mandatory")
_OaDhcpRelayInterfaceEntry_Object = MibTableRow
oaDhcpRelayInterfaceEntry = _OaDhcpRelayInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3, 1)
)
oaDhcpRelayInterfaceEntry.setIndexNames(
    (0, "OADHCP-SERVER-MIB", "oaDhcpRelayIfName"),
)
if mibBuilder.loadTexts:
    oaDhcpRelayInterfaceEntry.setStatus("mandatory")
_OaDhcpRelayIfName_Type = DisplayString
_OaDhcpRelayIfName_Object = MibTableColumn
oaDhcpRelayIfName = _OaDhcpRelayIfName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3, 1, 1),
    _OaDhcpRelayIfName_Type()
)
oaDhcpRelayIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDhcpRelayIfName.setStatus("mandatory")
_OaDhcpRelayIfStatus_Type = EntryStatus
_OaDhcpRelayIfStatus_Object = MibTableColumn
oaDhcpRelayIfStatus = _OaDhcpRelayIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3, 1, 2),
    _OaDhcpRelayIfStatus_Type()
)
oaDhcpRelayIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDhcpRelayIfStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OADHCP-SERVER-MIB",
    **{"HostName": HostName,
       "EntryStatus": EntryStatus,
       "ObjectStatus": ObjectStatus,
       "oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaDhcp": oaDhcp,
       "oaDhcpServer": oaDhcpServer,
       "oaDhcpServerGeneral": oaDhcpServerGeneral,
       "oaDhcpServerStatus": oaDhcpServerStatus,
       "oaDhcpNetbiosNodeType": oaDhcpNetbiosNodeType,
       "oaDhcpDomainName": oaDhcpDomainName,
       "oaDhcpDefaultLeaseTime": oaDhcpDefaultLeaseTime,
       "oaDhcpMaxLeaseTime": oaDhcpMaxLeaseTime,
       "oaDhcpDNSTable": oaDhcpDNSTable,
       "oaDhcpDNSEntry": oaDhcpDNSEntry,
       "oaDhcpDNSNum": oaDhcpDNSNum,
       "oaDhcpDNSIp": oaDhcpDNSIp,
       "oaDhcpDNSStatus": oaDhcpDNSStatus,
       "oaDhcpNetbiosServersTable": oaDhcpNetbiosServersTable,
       "oaDhcpNetbiosServersEntry": oaDhcpNetbiosServersEntry,
       "oaDhcpNetbiosServerNum": oaDhcpNetbiosServerNum,
       "oaDhcpNetbiosServerIp": oaDhcpNetbiosServerIp,
       "oaDhcpNetbiosServerStatus": oaDhcpNetbiosServerStatus,
       "oaDhcpSubnetConfigTable": oaDhcpSubnetConfigTable,
       "oaDhcpSubnetConfigEntry": oaDhcpSubnetConfigEntry,
       "oaDhcpInterfaceName": oaDhcpInterfaceName,
       "oaDhcpSubnetIp": oaDhcpSubnetIp,
       "oaDhcpSubnetMask": oaDhcpSubnetMask,
       "oaDhcpOptionSubnetMask": oaDhcpOptionSubnetMask,
       "oaDhcpIsOptionMask": oaDhcpIsOptionMask,
       "oaDhcpSubnetConfigStatus": oaDhcpSubnetConfigStatus,
       "oaDhcpIpRangeTable": oaDhcpIpRangeTable,
       "oaDhcpIpRangeEntry": oaDhcpIpRangeEntry,
       "oaDhcpIpRangeSubnetIp": oaDhcpIpRangeSubnetIp,
       "oaDhcpIpRangeSubnetMask": oaDhcpIpRangeSubnetMask,
       "oaDhcpIpRangeStart": oaDhcpIpRangeStart,
       "oaDhcpIpRangeEnd": oaDhcpIpRangeEnd,
       "oaDhcpIpRangeStatus": oaDhcpIpRangeStatus,
       "oaDhcpDefaultGWTable": oaDhcpDefaultGWTable,
       "oaDhcpDefaultGWEntry": oaDhcpDefaultGWEntry,
       "oaDhcpDefaultGWSubnetIp": oaDhcpDefaultGWSubnetIp,
       "oaDhcpDefaultGWSubnetMask": oaDhcpDefaultGWSubnetMask,
       "oaDhcpDefaultGWIp": oaDhcpDefaultGWIp,
       "oaDhcpDefaultGWStatus": oaDhcpDefaultGWStatus,
       "oaDhcpRelay": oaDhcpRelay,
       "oaDhcpRelayGeneral": oaDhcpRelayGeneral,
       "oaDhcpRelayStatus": oaDhcpRelayStatus,
       "oaDhcpRelayClearConfig": oaDhcpRelayClearConfig,
       "oaDhcpRelayServerTable": oaDhcpRelayServerTable,
       "oaDhcpRelayServerEntry": oaDhcpRelayServerEntry,
       "oaDhcpRelayServerIp": oaDhcpRelayServerIp,
       "oaDhcpRelayServerStatus": oaDhcpRelayServerStatus,
       "oaDhcpRelayInterfaceTable": oaDhcpRelayInterfaceTable,
       "oaDhcpRelayInterfaceEntry": oaDhcpRelayInterfaceEntry,
       "oaDhcpRelayIfName": oaDhcpRelayIfName,
       "oaDhcpRelayIfStatus": oaDhcpRelayIfStatus}
)
