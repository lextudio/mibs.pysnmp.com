# SNMP MIB module (HP-ICF-DHCP-SNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DHCP-SNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:16 2024
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

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfIpDhcpSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34)
)
hpicfIpDhcpSnoop.setRevisions(
        ("2016-06-01 00:00",
         "2016-01-29 00:00",
         "2015-06-12 00:00",
         "2013-06-12 00:00",
         "2013-05-02 00:00",
         "2013-02-10 00:00",
         "2007-08-24 00:00",
         "2006-07-06 00:38",
         "2006-03-18 00:38")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDhcpSnoopNotifications_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopNotifications = _HpicfDhcpSnoopNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 0)
)
_HpicfIpDhcpSnoopObjects_ObjectIdentity = ObjectIdentity
hpicfIpDhcpSnoopObjects = _HpicfIpDhcpSnoopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1)
)
_HpicfIpDhcpSnoopConfig_ObjectIdentity = ObjectIdentity
hpicfIpDhcpSnoopConfig = _HpicfIpDhcpSnoopConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1)
)
_HpicfDhcpSnoopGlobalCfg_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopGlobalCfg = _HpicfDhcpSnoopGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1)
)
_HpicfDhcpSnoopEnable_Type = TruthValue
_HpicfDhcpSnoopEnable_Object = MibScalar
hpicfDhcpSnoopEnable = _HpicfDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 1),
    _HpicfDhcpSnoopEnable_Type()
)
hpicfDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopEnable.setStatus("current")


class _HpicfDhcpSnoopVlanEnable_Type(OctetString):
    """Custom type hpicfDhcpSnoopVlanEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_HpicfDhcpSnoopVlanEnable_Type.__name__ = "OctetString"
_HpicfDhcpSnoopVlanEnable_Object = MibScalar
hpicfDhcpSnoopVlanEnable = _HpicfDhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 2),
    _HpicfDhcpSnoopVlanEnable_Type()
)
hpicfDhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopVlanEnable.setStatus("current")
_HpicfDhcpSnoopVerifyMac_Type = TruthValue
_HpicfDhcpSnoopVerifyMac_Object = MibScalar
hpicfDhcpSnoopVerifyMac = _HpicfDhcpSnoopVerifyMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 3),
    _HpicfDhcpSnoopVerifyMac_Type()
)
hpicfDhcpSnoopVerifyMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopVerifyMac.setStatus("current")
_HpicfDhcpSnoopDatabaseFile_Type = SnmpAdminString
_HpicfDhcpSnoopDatabaseFile_Object = MibScalar
hpicfDhcpSnoopDatabaseFile = _HpicfDhcpSnoopDatabaseFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 4),
    _HpicfDhcpSnoopDatabaseFile_Type()
)
hpicfDhcpSnoopDatabaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseFile.setStatus("current")


class _HpicfDhcpSnoopDatabaseWriteDelay_Type(Unsigned32):
    """Custom type hpicfDhcpSnoopDatabaseWriteDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_HpicfDhcpSnoopDatabaseWriteDelay_Type.__name__ = "Unsigned32"
_HpicfDhcpSnoopDatabaseWriteDelay_Object = MibScalar
hpicfDhcpSnoopDatabaseWriteDelay = _HpicfDhcpSnoopDatabaseWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 5),
    _HpicfDhcpSnoopDatabaseWriteDelay_Type()
)
hpicfDhcpSnoopDatabaseWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseWriteDelay.setStatus("current")


class _HpicfDhcpSnoopDatabaseWriteTimeout_Type(Unsigned32):
    """Custom type hpicfDhcpSnoopDatabaseWriteTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HpicfDhcpSnoopDatabaseWriteTimeout_Type.__name__ = "Unsigned32"
_HpicfDhcpSnoopDatabaseWriteTimeout_Object = MibScalar
hpicfDhcpSnoopDatabaseWriteTimeout = _HpicfDhcpSnoopDatabaseWriteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 6),
    _HpicfDhcpSnoopDatabaseWriteTimeout_Type()
)
hpicfDhcpSnoopDatabaseWriteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseWriteTimeout.setStatus("current")
_HpicfDhcpSnoopOpt82Insert_Type = TruthValue
_HpicfDhcpSnoopOpt82Insert_Object = MibScalar
hpicfDhcpSnoopOpt82Insert = _HpicfDhcpSnoopOpt82Insert_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 7),
    _HpicfDhcpSnoopOpt82Insert_Type()
)
hpicfDhcpSnoopOpt82Insert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopOpt82Insert.setStatus("current")


class _HpicfDhcpSnoopOpt82Policy_Type(Integer32):
    """Custom type hpicfDhcpSnoopOpt82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("keep", 1),
          ("replace", 2))
    )


_HpicfDhcpSnoopOpt82Policy_Type.__name__ = "Integer32"
_HpicfDhcpSnoopOpt82Policy_Object = MibScalar
hpicfDhcpSnoopOpt82Policy = _HpicfDhcpSnoopOpt82Policy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 8),
    _HpicfDhcpSnoopOpt82Policy_Type()
)
hpicfDhcpSnoopOpt82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopOpt82Policy.setStatus("current")


class _HpicfDhcpSnoopOpt82RemoteId_Type(Integer32):
    """Custom type hpicfDhcpSnoopOpt82RemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("mgmtIP", 3),
          ("subnetIP", 2))
    )


_HpicfDhcpSnoopOpt82RemoteId_Type.__name__ = "Integer32"
_HpicfDhcpSnoopOpt82RemoteId_Object = MibScalar
hpicfDhcpSnoopOpt82RemoteId = _HpicfDhcpSnoopOpt82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 9),
    _HpicfDhcpSnoopOpt82RemoteId_Type()
)
hpicfDhcpSnoopOpt82RemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopOpt82RemoteId.setStatus("current")


class _HpicfDhcpSnoopErrantReplyEnable_Type(Integer32):
    """Custom type hpicfDhcpSnoopErrantReplyEnable based on Integer32"""
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


_HpicfDhcpSnoopErrantReplyEnable_Type.__name__ = "Integer32"
_HpicfDhcpSnoopErrantReplyEnable_Object = MibScalar
hpicfDhcpSnoopErrantReplyEnable = _HpicfDhcpSnoopErrantReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 10),
    _HpicfDhcpSnoopErrantReplyEnable_Type()
)
hpicfDhcpSnoopErrantReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopErrantReplyEnable.setStatus("current")


class _HpicfDhcpSnoopDatabaseFTPort_Type(Unsigned32):
    """Custom type hpicfDhcpSnoopDatabaseFTPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfDhcpSnoopDatabaseFTPort_Type.__name__ = "Unsigned32"
_HpicfDhcpSnoopDatabaseFTPort_Object = MibScalar
hpicfDhcpSnoopDatabaseFTPort = _HpicfDhcpSnoopDatabaseFTPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 11),
    _HpicfDhcpSnoopDatabaseFTPort_Type()
)
hpicfDhcpSnoopDatabaseFTPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseFTPort.setStatus("current")
_HpicfDhcpSnoopDatabaseSFTPUsername_Type = SnmpAdminString
_HpicfDhcpSnoopDatabaseSFTPUsername_Object = MibScalar
hpicfDhcpSnoopDatabaseSFTPUsername = _HpicfDhcpSnoopDatabaseSFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 12),
    _HpicfDhcpSnoopDatabaseSFTPUsername_Type()
)
hpicfDhcpSnoopDatabaseSFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseSFTPUsername.setStatus("current")
_HpicfDhcpSnoopDatabaseSFTPPassword_Type = SnmpAdminString
_HpicfDhcpSnoopDatabaseSFTPPassword_Object = MibScalar
hpicfDhcpSnoopDatabaseSFTPPassword = _HpicfDhcpSnoopDatabaseSFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 13),
    _HpicfDhcpSnoopDatabaseSFTPPassword_Type()
)
hpicfDhcpSnoopDatabaseSFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseSFTPPassword.setStatus("current")


class _HpicfDhcpSnoopDatabaseValidateSFTPServer_Type(Integer32):
    """Custom type hpicfDhcpSnoopDatabaseValidateSFTPServer based on Integer32"""
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


_HpicfDhcpSnoopDatabaseValidateSFTPServer_Type.__name__ = "Integer32"
_HpicfDhcpSnoopDatabaseValidateSFTPServer_Object = MibScalar
hpicfDhcpSnoopDatabaseValidateSFTPServer = _HpicfDhcpSnoopDatabaseValidateSFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 14),
    _HpicfDhcpSnoopDatabaseValidateSFTPServer_Type()
)
hpicfDhcpSnoopDatabaseValidateSFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDatabaseValidateSFTPServer.setStatus("current")


class _HpicfDhcpSnoopAllowOverwriteBinding_Type(TruthValue):
    """Custom type hpicfDhcpSnoopAllowOverwriteBinding based on TruthValue"""


_HpicfDhcpSnoopAllowOverwriteBinding_Object = MibScalar
hpicfDhcpSnoopAllowOverwriteBinding = _HpicfDhcpSnoopAllowOverwriteBinding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 1, 15),
    _HpicfDhcpSnoopAllowOverwriteBinding_Type()
)
hpicfDhcpSnoopAllowOverwriteBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopAllowOverwriteBinding.setStatus("current")
_HpicfDhcpSnoopPortTable_Object = MibTable
hpicfDhcpSnoopPortTable = _HpicfDhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPortTable.setStatus("current")
_HpicfDhcpSnoopPortEntry_Object = MibTableRow
hpicfDhcpSnoopPortEntry = _HpicfDhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 2, 1)
)
hpicfDhcpSnoopPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPortEntry.setStatus("current")
_HpicfDhcpSnoopPortTrust_Type = TruthValue
_HpicfDhcpSnoopPortTrust_Object = MibTableColumn
hpicfDhcpSnoopPortTrust = _HpicfDhcpSnoopPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 2, 1, 1),
    _HpicfDhcpSnoopPortTrust_Type()
)
hpicfDhcpSnoopPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPortTrust.setStatus("current")


class _HpicfDhcpSnoopPortMaxbind_Type(Unsigned32):
    """Custom type hpicfDhcpSnoopPortMaxbind based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_HpicfDhcpSnoopPortMaxbind_Type.__name__ = "Unsigned32"
_HpicfDhcpSnoopPortMaxbind_Object = MibTableColumn
hpicfDhcpSnoopPortMaxbind = _HpicfDhcpSnoopPortMaxbind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 2, 1, 2),
    _HpicfDhcpSnoopPortMaxbind_Type()
)
hpicfDhcpSnoopPortMaxbind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPortMaxbind.setStatus("current")


class _HpicfDhcpSnoopPortStaticBinding_Type(Unsigned32):
    """Custom type hpicfDhcpSnoopPortStaticBinding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_HpicfDhcpSnoopPortStaticBinding_Type.__name__ = "Unsigned32"
_HpicfDhcpSnoopPortStaticBinding_Object = MibTableColumn
hpicfDhcpSnoopPortStaticBinding = _HpicfDhcpSnoopPortStaticBinding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 2, 1, 3),
    _HpicfDhcpSnoopPortStaticBinding_Type()
)
hpicfDhcpSnoopPortStaticBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPortStaticBinding.setStatus("current")


class _HpicfDhcpSnoopPortDynamicBinding_Type(Unsigned32):
    """Custom type hpicfDhcpSnoopPortDynamicBinding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_HpicfDhcpSnoopPortDynamicBinding_Type.__name__ = "Unsigned32"
_HpicfDhcpSnoopPortDynamicBinding_Object = MibTableColumn
hpicfDhcpSnoopPortDynamicBinding = _HpicfDhcpSnoopPortDynamicBinding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 2, 1, 4),
    _HpicfDhcpSnoopPortDynamicBinding_Type()
)
hpicfDhcpSnoopPortDynamicBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPortDynamicBinding.setStatus("current")
_HpicfDhcpSnoopServerTable_Object = MibTable
hpicfDhcpSnoopServerTable = _HpicfDhcpSnoopServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopServerTable.setStatus("current")
_HpicfDhcpSnoopServerEntry_Object = MibTableRow
hpicfDhcpSnoopServerEntry = _HpicfDhcpSnoopServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 3, 1)
)
hpicfDhcpSnoopServerEntry.setIndexNames(
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopServerAddrType"),
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopServerEntry.setStatus("current")
_HpicfDhcpSnoopServerAddrType_Type = InetAddressType
_HpicfDhcpSnoopServerAddrType_Object = MibTableColumn
hpicfDhcpSnoopServerAddrType = _HpicfDhcpSnoopServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 3, 1, 1),
    _HpicfDhcpSnoopServerAddrType_Type()
)
hpicfDhcpSnoopServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopServerAddrType.setStatus("current")
_HpicfDhcpSnoopServerAddress_Type = InetAddress
_HpicfDhcpSnoopServerAddress_Object = MibTableColumn
hpicfDhcpSnoopServerAddress = _HpicfDhcpSnoopServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 3, 1, 2),
    _HpicfDhcpSnoopServerAddress_Type()
)
hpicfDhcpSnoopServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopServerAddress.setStatus("current")
_HpicfDhcpSnoopServerStatus_Type = RowStatus
_HpicfDhcpSnoopServerStatus_Object = MibTableColumn
hpicfDhcpSnoopServerStatus = _HpicfDhcpSnoopServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 3, 1, 3),
    _HpicfDhcpSnoopServerStatus_Type()
)
hpicfDhcpSnoopServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopServerStatus.setStatus("current")
_HpicfIpStaticBindingsTable_Object = MibTable
hpicfIpStaticBindingsTable = _HpicfIpStaticBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsTable.setStatus("current")
_HpicfIpStaticBindingsEntry_Object = MibTableRow
hpicfIpStaticBindingsEntry = _HpicfIpStaticBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1)
)
hpicfIpStaticBindingsEntry.setIndexNames(
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfIpStaticBindingsVlan"),
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfIpStaticBindingsAddrType"),
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfIpStaticBindingsAddress"),
)
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsEntry.setStatus("current")


class _HpicfIpStaticBindingsVlan_Type(VlanIndex):
    """Custom type hpicfIpStaticBindingsVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HpicfIpStaticBindingsVlan_Type.__name__ = "VlanIndex"
_HpicfIpStaticBindingsVlan_Object = MibTableColumn
hpicfIpStaticBindingsVlan = _HpicfIpStaticBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1, 1),
    _HpicfIpStaticBindingsVlan_Type()
)
hpicfIpStaticBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsVlan.setStatus("current")
_HpicfIpStaticBindingsAddrType_Type = InetAddressType
_HpicfIpStaticBindingsAddrType_Object = MibTableColumn
hpicfIpStaticBindingsAddrType = _HpicfIpStaticBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1, 2),
    _HpicfIpStaticBindingsAddrType_Type()
)
hpicfIpStaticBindingsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsAddrType.setStatus("current")
_HpicfIpStaticBindingsAddress_Type = InetAddress
_HpicfIpStaticBindingsAddress_Object = MibTableColumn
hpicfIpStaticBindingsAddress = _HpicfIpStaticBindingsAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1, 3),
    _HpicfIpStaticBindingsAddress_Type()
)
hpicfIpStaticBindingsAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsAddress.setStatus("current")
_HpicfIpStaticBindingsMacAddress_Type = MacAddress
_HpicfIpStaticBindingsMacAddress_Object = MibTableColumn
hpicfIpStaticBindingsMacAddress = _HpicfIpStaticBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1, 4),
    _HpicfIpStaticBindingsMacAddress_Type()
)
hpicfIpStaticBindingsMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsMacAddress.setStatus("current")
_HpicfIpStaticBindingsInterface_Type = InterfaceIndex
_HpicfIpStaticBindingsInterface_Object = MibTableColumn
hpicfIpStaticBindingsInterface = _HpicfIpStaticBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1, 5),
    _HpicfIpStaticBindingsInterface_Type()
)
hpicfIpStaticBindingsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsInterface.setStatus("current")
_HpicfIpStaticBindingsStatus_Type = RowStatus
_HpicfIpStaticBindingsStatus_Object = MibTableColumn
hpicfIpStaticBindingsStatus = _HpicfIpStaticBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 1, 4, 1, 6),
    _HpicfIpStaticBindingsStatus_Type()
)
hpicfIpStaticBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticBindingsStatus.setStatus("current")
_HpicfIpDhcpSnoopStatus_ObjectIdentity = ObjectIdentity
hpicfIpDhcpSnoopStatus = _HpicfIpDhcpSnoopStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2)
)
_HpicfDhcpSnoopGlobalStats_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopGlobalStats = _HpicfDhcpSnoopGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1)
)
_HpicfDhcpSnoopCSForwards_Type = Counter32
_HpicfDhcpSnoopCSForwards_Object = MibScalar
hpicfDhcpSnoopCSForwards = _HpicfDhcpSnoopCSForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 1),
    _HpicfDhcpSnoopCSForwards_Type()
)
hpicfDhcpSnoopCSForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCSForwards.setStatus("current")
_HpicfDhcpSnoopCSMACMismatches_Type = Counter32
_HpicfDhcpSnoopCSMACMismatches_Object = MibScalar
hpicfDhcpSnoopCSMACMismatches = _HpicfDhcpSnoopCSMACMismatches_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 2),
    _HpicfDhcpSnoopCSMACMismatches_Type()
)
hpicfDhcpSnoopCSMACMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCSMACMismatches.setStatus("current")
_HpicfDhcpSnoopCSUntrustedOpt82s_Type = Counter32
_HpicfDhcpSnoopCSUntrustedOpt82s_Object = MibScalar
hpicfDhcpSnoopCSUntrustedOpt82s = _HpicfDhcpSnoopCSUntrustedOpt82s_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 3),
    _HpicfDhcpSnoopCSUntrustedOpt82s_Type()
)
hpicfDhcpSnoopCSUntrustedOpt82s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCSUntrustedOpt82s.setStatus("current")
_HpicfDhcpSnoopCSBadReleases_Type = Counter32
_HpicfDhcpSnoopCSBadReleases_Object = MibScalar
hpicfDhcpSnoopCSBadReleases = _HpicfDhcpSnoopCSBadReleases_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 4),
    _HpicfDhcpSnoopCSBadReleases_Type()
)
hpicfDhcpSnoopCSBadReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCSBadReleases.setStatus("current")
_HpicfDhcpSnoopCSUntrustedDestPorts_Type = Counter32
_HpicfDhcpSnoopCSUntrustedDestPorts_Object = MibScalar
hpicfDhcpSnoopCSUntrustedDestPorts = _HpicfDhcpSnoopCSUntrustedDestPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 5),
    _HpicfDhcpSnoopCSUntrustedDestPorts_Type()
)
hpicfDhcpSnoopCSUntrustedDestPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCSUntrustedDestPorts.setStatus("current")
_HpicfDhcpSnoopSCForwards_Type = Counter32
_HpicfDhcpSnoopSCForwards_Object = MibScalar
hpicfDhcpSnoopSCForwards = _HpicfDhcpSnoopSCForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 6),
    _HpicfDhcpSnoopSCForwards_Type()
)
hpicfDhcpSnoopSCForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopSCForwards.setStatus("current")
_HpicfDhcpSnoopSCUntrustedPorts_Type = Counter32
_HpicfDhcpSnoopSCUntrustedPorts_Object = MibScalar
hpicfDhcpSnoopSCUntrustedPorts = _HpicfDhcpSnoopSCUntrustedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 7),
    _HpicfDhcpSnoopSCUntrustedPorts_Type()
)
hpicfDhcpSnoopSCUntrustedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopSCUntrustedPorts.setStatus("current")
_HpicfDhcpSnoopSCUntrustedServers_Type = Counter32
_HpicfDhcpSnoopSCUntrustedServers_Object = MibScalar
hpicfDhcpSnoopSCUntrustedServers = _HpicfDhcpSnoopSCUntrustedServers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 8),
    _HpicfDhcpSnoopSCUntrustedServers_Type()
)
hpicfDhcpSnoopSCUntrustedServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopSCUntrustedServers.setStatus("current")
_HpicfDhcpSnoopSCOpt82Failures_Type = Counter32
_HpicfDhcpSnoopSCOpt82Failures_Object = MibScalar
hpicfDhcpSnoopSCOpt82Failures = _HpicfDhcpSnoopSCOpt82Failures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 9),
    _HpicfDhcpSnoopSCOpt82Failures_Type()
)
hpicfDhcpSnoopSCOpt82Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopSCOpt82Failures.setStatus("current")
_HpicfDhcpSnoopDBFileWriteAttempts_Type = Counter32
_HpicfDhcpSnoopDBFileWriteAttempts_Object = MibScalar
hpicfDhcpSnoopDBFileWriteAttempts = _HpicfDhcpSnoopDBFileWriteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 10),
    _HpicfDhcpSnoopDBFileWriteAttempts_Type()
)
hpicfDhcpSnoopDBFileWriteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDBFileWriteAttempts.setStatus("current")
_HpicfDhcpSnoopDBFileWriteFailures_Type = Counter32
_HpicfDhcpSnoopDBFileWriteFailures_Object = MibScalar
hpicfDhcpSnoopDBFileWriteFailures = _HpicfDhcpSnoopDBFileWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 11),
    _HpicfDhcpSnoopDBFileWriteFailures_Type()
)
hpicfDhcpSnoopDBFileWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDBFileWriteFailures.setStatus("current")


class _HpicfDhcpSnoopDBFileReadStatus_Type(Integer32):
    """Custom type hpicfDhcpSnoopDBFileReadStatus based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("notConfigured", 1),
          ("succeeded", 3))
    )


_HpicfDhcpSnoopDBFileReadStatus_Type.__name__ = "Integer32"
_HpicfDhcpSnoopDBFileReadStatus_Object = MibScalar
hpicfDhcpSnoopDBFileReadStatus = _HpicfDhcpSnoopDBFileReadStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 12),
    _HpicfDhcpSnoopDBFileReadStatus_Type()
)
hpicfDhcpSnoopDBFileReadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDBFileReadStatus.setStatus("current")


class _HpicfDhcpSnoopDBFileWriteStatus_Type(Integer32):
    """Custom type hpicfDhcpSnoopDBFileWriteStatus based on Integer32"""
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
        *(("delaying", 2),
          ("failed", 5),
          ("inProgress", 3),
          ("notConfigured", 1),
          ("succeeded", 4))
    )


_HpicfDhcpSnoopDBFileWriteStatus_Type.__name__ = "Integer32"
_HpicfDhcpSnoopDBFileWriteStatus_Object = MibScalar
hpicfDhcpSnoopDBFileWriteStatus = _HpicfDhcpSnoopDBFileWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 13),
    _HpicfDhcpSnoopDBFileWriteStatus_Type()
)
hpicfDhcpSnoopDBFileWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDBFileWriteStatus.setStatus("current")
_HpicfDhcpSnoopDBFileLastWriteTime_Type = DateAndTime
_HpicfDhcpSnoopDBFileLastWriteTime_Object = MibScalar
hpicfDhcpSnoopDBFileLastWriteTime = _HpicfDhcpSnoopDBFileLastWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 14),
    _HpicfDhcpSnoopDBFileLastWriteTime_Type()
)
hpicfDhcpSnoopDBFileLastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDBFileLastWriteTime.setStatus("current")
_HpicfDhcpSnoopPktsSent_Type = Counter32
_HpicfDhcpSnoopPktsSent_Object = MibScalar
hpicfDhcpSnoopPktsSent = _HpicfDhcpSnoopPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 15),
    _HpicfDhcpSnoopPktsSent_Type()
)
hpicfDhcpSnoopPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPktsSent.setStatus("current")
_HpicfDhcpSnoopPktsReceived_Type = Counter32
_HpicfDhcpSnoopPktsReceived_Object = MibScalar
hpicfDhcpSnoopPktsReceived = _HpicfDhcpSnoopPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 16),
    _HpicfDhcpSnoopPktsReceived_Type()
)
hpicfDhcpSnoopPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPktsReceived.setStatus("current")
_HpicfDhcpSnoopPktsDropped_Type = Counter32
_HpicfDhcpSnoopPktsDropped_Object = MibScalar
hpicfDhcpSnoopPktsDropped = _HpicfDhcpSnoopPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 17),
    _HpicfDhcpSnoopPktsDropped_Type()
)
hpicfDhcpSnoopPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPktsDropped.setStatus("current")
_HpicfDhcpSnoopMaxbindPktsDropped_Type = Counter32
_HpicfDhcpSnoopMaxbindPktsDropped_Object = MibScalar
hpicfDhcpSnoopMaxbindPktsDropped = _HpicfDhcpSnoopMaxbindPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 1, 18),
    _HpicfDhcpSnoopMaxbindPktsDropped_Type()
)
hpicfDhcpSnoopMaxbindPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopMaxbindPktsDropped.setStatus("current")
_HpicfDhcpSnoopBindingsTable_Object = MibTable
hpicfDhcpSnoopBindingsTable = _HpicfDhcpSnoopBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsTable.setStatus("current")
_HpicfDhcpSnoopBindingsEntry_Object = MibTableRow
hpicfDhcpSnoopBindingsEntry = _HpicfDhcpSnoopBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1)
)
hpicfDhcpSnoopBindingsEntry.setIndexNames(
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsVlan"),
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsMacAddress"),
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsAddrType"),
    (0, "HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsAddress"),
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsEntry.setStatus("current")


class _HpicfDhcpSnoopBindingsVlan_Type(VlanIndex):
    """Custom type hpicfDhcpSnoopBindingsVlan based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HpicfDhcpSnoopBindingsVlan_Type.__name__ = "VlanIndex"
_HpicfDhcpSnoopBindingsVlan_Object = MibTableColumn
hpicfDhcpSnoopBindingsVlan = _HpicfDhcpSnoopBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 1),
    _HpicfDhcpSnoopBindingsVlan_Type()
)
hpicfDhcpSnoopBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsVlan.setStatus("current")
_HpicfDhcpSnoopBindingsMacAddress_Type = MacAddress
_HpicfDhcpSnoopBindingsMacAddress_Object = MibTableColumn
hpicfDhcpSnoopBindingsMacAddress = _HpicfDhcpSnoopBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 2),
    _HpicfDhcpSnoopBindingsMacAddress_Type()
)
hpicfDhcpSnoopBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsMacAddress.setStatus("current")
_HpicfDhcpSnoopBindingsAddrType_Type = InetAddressType
_HpicfDhcpSnoopBindingsAddrType_Object = MibTableColumn
hpicfDhcpSnoopBindingsAddrType = _HpicfDhcpSnoopBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 3),
    _HpicfDhcpSnoopBindingsAddrType_Type()
)
hpicfDhcpSnoopBindingsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsAddrType.setStatus("current")
_HpicfDhcpSnoopBindingsAddress_Type = InetAddress
_HpicfDhcpSnoopBindingsAddress_Object = MibTableColumn
hpicfDhcpSnoopBindingsAddress = _HpicfDhcpSnoopBindingsAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 4),
    _HpicfDhcpSnoopBindingsAddress_Type()
)
hpicfDhcpSnoopBindingsAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsAddress.setStatus("current")
_HpicfDhcpSnoopBindingsInterface_Type = InterfaceIndex
_HpicfDhcpSnoopBindingsInterface_Object = MibTableColumn
hpicfDhcpSnoopBindingsInterface = _HpicfDhcpSnoopBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 5),
    _HpicfDhcpSnoopBindingsInterface_Type()
)
hpicfDhcpSnoopBindingsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsInterface.setStatus("current")
_HpicfDhcpSnoopBindingsLeaseTime_Type = Unsigned32
_HpicfDhcpSnoopBindingsLeaseTime_Object = MibTableColumn
hpicfDhcpSnoopBindingsLeaseTime = _HpicfDhcpSnoopBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 6),
    _HpicfDhcpSnoopBindingsLeaseTime_Type()
)
hpicfDhcpSnoopBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsLeaseTime.setStatus("current")


class _HpicfDhcpSnoopBindingsType_Type(Integer32):
    """Custom type hpicfDhcpSnoopBindingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_HpicfDhcpSnoopBindingsType_Type.__name__ = "Integer32"
_HpicfDhcpSnoopBindingsType_Object = MibTableColumn
hpicfDhcpSnoopBindingsType = _HpicfDhcpSnoopBindingsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 7),
    _HpicfDhcpSnoopBindingsType_Type()
)
hpicfDhcpSnoopBindingsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsType.setStatus("current")
_HpicfDhcpSnoopBindingsSecVlan_Type = Unsigned32
_HpicfDhcpSnoopBindingsSecVlan_Object = MibTableColumn
hpicfDhcpSnoopBindingsSecVlan = _HpicfDhcpSnoopBindingsSecVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 2, 2, 1, 8),
    _HpicfDhcpSnoopBindingsSecVlan_Type()
)
hpicfDhcpSnoopBindingsSecVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsSecVlan.setStatus("current")
_HpicfDhcpSnoopNotifyObjects_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopNotifyObjects = _HpicfDhcpSnoopNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 3)
)
_HpicfDhcpSnoopNotifyCount_Type = Counter32
_HpicfDhcpSnoopNotifyCount_Object = MibScalar
hpicfDhcpSnoopNotifyCount = _HpicfDhcpSnoopNotifyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 3, 1),
    _HpicfDhcpSnoopNotifyCount_Type()
)
hpicfDhcpSnoopNotifyCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopNotifyCount.setStatus("current")
_HpicfDhcpSnoopErrantSrcMAC_Type = MacAddress
_HpicfDhcpSnoopErrantSrcMAC_Object = MibScalar
hpicfDhcpSnoopErrantSrcMAC = _HpicfDhcpSnoopErrantSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 3, 2),
    _HpicfDhcpSnoopErrantSrcMAC_Type()
)
hpicfDhcpSnoopErrantSrcMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopErrantSrcMAC.setStatus("current")
_HpicfDhcpSnoopErrantSrcIPType_Type = InetAddressType
_HpicfDhcpSnoopErrantSrcIPType_Object = MibScalar
hpicfDhcpSnoopErrantSrcIPType = _HpicfDhcpSnoopErrantSrcIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 3, 3),
    _HpicfDhcpSnoopErrantSrcIPType_Type()
)
hpicfDhcpSnoopErrantSrcIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopErrantSrcIPType.setStatus("current")
_HpicfDhcpSnoopErrantSrcIP_Type = InetAddress
_HpicfDhcpSnoopErrantSrcIP_Object = MibScalar
hpicfDhcpSnoopErrantSrcIP = _HpicfDhcpSnoopErrantSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 3, 4),
    _HpicfDhcpSnoopErrantSrcIP_Type()
)
hpicfDhcpSnoopErrantSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopErrantSrcIP.setStatus("current")
_HpicfDhcpSnoopClearStatsOptions_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopClearStatsOptions = _HpicfDhcpSnoopClearStatsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 4)
)
_HpicfDhcpSnoopClearStats_Type = TruthValue
_HpicfDhcpSnoopClearStats_Object = MibScalar
hpicfDhcpSnoopClearStats = _HpicfDhcpSnoopClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 4, 1),
    _HpicfDhcpSnoopClearStats_Type()
)
hpicfDhcpSnoopClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearStats.setStatus("current")
_HpicfDhcpSnoopClearBindingsOptions_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopClearBindingsOptions = _HpicfDhcpSnoopClearBindingsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 5)
)
_HpicfDhcpSnoopClearBindings_Type = TruthValue
_HpicfDhcpSnoopClearBindings_Object = MibScalar
hpicfDhcpSnoopClearBindings = _HpicfDhcpSnoopClearBindings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 5, 1),
    _HpicfDhcpSnoopClearBindings_Type()
)
hpicfDhcpSnoopClearBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearBindings.setStatus("current")
_HpicfDhcpSnoopClearBindingsIpType_Type = InetAddressType
_HpicfDhcpSnoopClearBindingsIpType_Object = MibScalar
hpicfDhcpSnoopClearBindingsIpType = _HpicfDhcpSnoopClearBindingsIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 5, 2),
    _HpicfDhcpSnoopClearBindingsIpType_Type()
)
hpicfDhcpSnoopClearBindingsIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearBindingsIpType.setStatus("current")
_HpicfDhcpSnoopClearBindingsIpAddr_Type = InetAddress
_HpicfDhcpSnoopClearBindingsIpAddr_Object = MibScalar
hpicfDhcpSnoopClearBindingsIpAddr = _HpicfDhcpSnoopClearBindingsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 5, 3),
    _HpicfDhcpSnoopClearBindingsIpAddr_Type()
)
hpicfDhcpSnoopClearBindingsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearBindingsIpAddr.setStatus("current")
_HpicfDhcpSnoopClearBindingsPort_Type = InterfaceIndexOrZero
_HpicfDhcpSnoopClearBindingsPort_Object = MibScalar
hpicfDhcpSnoopClearBindingsPort = _HpicfDhcpSnoopClearBindingsPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 5, 4),
    _HpicfDhcpSnoopClearBindingsPort_Type()
)
hpicfDhcpSnoopClearBindingsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearBindingsPort.setStatus("current")
_HpicfDhcpSnoopClearBindingsVlan_Type = InterfaceIndexOrZero
_HpicfDhcpSnoopClearBindingsVlan_Object = MibScalar
hpicfDhcpSnoopClearBindingsVlan = _HpicfDhcpSnoopClearBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 1, 5, 5),
    _HpicfDhcpSnoopClearBindingsVlan_Type()
)
hpicfDhcpSnoopClearBindingsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearBindingsVlan.setStatus("current")
_HpicfDhcpSnoopConformance_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopConformance = _HpicfDhcpSnoopConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2)
)
_HpicfIpDhcpSnoopGroups_ObjectIdentity = ObjectIdentity
hpicfIpDhcpSnoopGroups = _HpicfIpDhcpSnoopGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1)
)
_HpicfDhcpSnoopCompliances_ObjectIdentity = ObjectIdentity
hpicfDhcpSnoopCompliances = _HpicfDhcpSnoopCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2)
)

# Managed Objects groups

hpicfDhcpSnoopBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 1)
)
hpicfDhcpSnoopBaseGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopEnable"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopVlanEnable"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopVerifyMac"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPortTrust"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopCSForwards"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopCSMACMismatches"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopCSBadReleases"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopCSUntrustedDestPorts"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopSCForwards"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopSCUntrustedPorts"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBaseGroup.setStatus("current")

hpicfDhcpSnoopOpt82Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 2)
)
hpicfDhcpSnoopOpt82Group.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopOpt82Insert"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopOpt82Policy"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopOpt82RemoteId"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopCSUntrustedOpt82s"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopSCOpt82Failures"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopOpt82Group.setStatus("current")

hpicfDhcpSnoopServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 3)
)
hpicfDhcpSnoopServersGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopServerStatus"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopSCUntrustedServers"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopServersGroup.setStatus("current")

hpicfDhcpSnoopDbaseFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 4)
)
hpicfDhcpSnoopDbaseFileGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseFile"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseWriteDelay"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseWriteTimeout"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileWriteAttempts"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileWriteFailures"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileReadStatus"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileWriteStatus"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileLastWriteTime"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDbaseFileGroup.setStatus("deprecated")

hpicfDhcpSnoopBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 5)
)
hpicfDhcpSnoopBindingsGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsInterface"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsLeaseTime"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsType"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsSecVlan"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopBindingsGroup.setStatus("current")

hpicfDhcpSnoopStaticBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 6)
)
hpicfDhcpSnoopStaticBindingsGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfIpStaticBindingsMacAddress"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfIpStaticBindingsInterface"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfIpStaticBindingsStatus"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopBindingsType"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopStaticBindingsGroup.setStatus("current")

hpicfDhcpSnoopNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 7)
)
hpicfDhcpSnoopNotifyObjsGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopNotifyCount"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantSrcMAC"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantSrcIPType"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantSrcIP"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantReplyEnable"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopNotifyObjsGroup.setStatus("current")

hpicfDhcpSnoopPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 9)
)
hpicfDhcpSnoopPktsGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPktsSent"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPktsReceived"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPktsDropped"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPktsGroup.setStatus("current")

hpicfDhcpSnoopClearStatsOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 10)
)
hpicfDhcpSnoopClearStatsOptionsGroup.setObjects(
    ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopClearStats")
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearStatsOptionsGroup.setStatus("current")

hpicfDhcpSnoopMaxbindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 11)
)
hpicfDhcpSnoopMaxbindingGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPortMaxbind"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPortStaticBinding"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPortDynamicBinding"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopMaxbindingGroup.setStatus("current")

hpicfDhcpSnoopPktsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 12)
)
hpicfDhcpSnoopPktsGroup1.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPktsSent"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPktsReceived"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopPktsDropped"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopMaxbindPktsDropped"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopPktsGroup1.setStatus("current")

hpicfDhcpSnoopDbaseFileGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 13)
)
hpicfDhcpSnoopDbaseFileGroup1.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseFile"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseWriteDelay"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseWriteTimeout"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileWriteAttempts"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileWriteFailures"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileReadStatus"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileWriteStatus"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDBFileLastWriteTime"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseFTPort"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseSFTPUsername"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseSFTPPassword"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopDatabaseValidateSFTPServer"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopDbaseFileGroup1.setStatus("current")

hpicfDhcpSnoopAllowOverwriteBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 14)
)
hpicfDhcpSnoopAllowOverwriteBindingGroup.setObjects(
    ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopAllowOverwriteBinding")
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopAllowOverwriteBindingGroup.setStatus("current")

hpicfDhcpSnoopClearBindingsOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 15)
)
hpicfDhcpSnoopClearBindingsOptionsGroup.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopClearBindings"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopClearBindingsIpType"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopClearBindingsIpAddr"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopClearBindingsPort"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopClearBindingsVlan"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearBindingsOptionsGroup.setStatus("current")


# Notification objects

hpicfDhcpSnoopErrantReply = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 0, 1)
)
hpicfDhcpSnoopErrantReply.setObjects(
      *(("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopNotifyCount"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantSrcMAC"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantSrcIPType"),
        ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantSrcIP"))
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopErrantReply.setStatus(
        "current"
    )


# Notifications groups

hpicfDhcpSnoopNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 1, 8)
)
hpicfDhcpSnoopNotificationGroup.setObjects(
    ("HP-ICF-DHCP-SNOOP-MIB", "hpicfDhcpSnoopErrantReply")
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfDhcpSnoopCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance.setStatus(
        "deprecated"
    )

hpicfDhcpSnoopCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance2.setStatus(
        "current"
    )

hpicfDhcpSnoopCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance3.setStatus(
        "current"
    )

hpicfDhcpSnoopCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance4.setStatus(
        "current"
    )

hpicfDhcpSnoopClearStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopClearStatsCompliance.setStatus(
        "current"
    )

hpicfDhcpSnoopCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance6.setStatus(
        "deprecated"
    )

hpicfDhcpSnoopCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance7.setStatus(
        "current"
    )

hpicfDhcpSnoopCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance8.setStatus(
        "current"
    )

hpicfDhcpSnoopCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance9.setStatus(
        "current"
    )

hpicfDhcpSnoopCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34, 2, 2, 10)
)
if mibBuilder.loadTexts:
    hpicfDhcpSnoopCompliance10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DHCP-SNOOP-MIB",
    **{"hpicfIpDhcpSnoop": hpicfIpDhcpSnoop,
       "hpicfDhcpSnoopNotifications": hpicfDhcpSnoopNotifications,
       "hpicfDhcpSnoopErrantReply": hpicfDhcpSnoopErrantReply,
       "hpicfIpDhcpSnoopObjects": hpicfIpDhcpSnoopObjects,
       "hpicfIpDhcpSnoopConfig": hpicfIpDhcpSnoopConfig,
       "hpicfDhcpSnoopGlobalCfg": hpicfDhcpSnoopGlobalCfg,
       "hpicfDhcpSnoopEnable": hpicfDhcpSnoopEnable,
       "hpicfDhcpSnoopVlanEnable": hpicfDhcpSnoopVlanEnable,
       "hpicfDhcpSnoopVerifyMac": hpicfDhcpSnoopVerifyMac,
       "hpicfDhcpSnoopDatabaseFile": hpicfDhcpSnoopDatabaseFile,
       "hpicfDhcpSnoopDatabaseWriteDelay": hpicfDhcpSnoopDatabaseWriteDelay,
       "hpicfDhcpSnoopDatabaseWriteTimeout": hpicfDhcpSnoopDatabaseWriteTimeout,
       "hpicfDhcpSnoopOpt82Insert": hpicfDhcpSnoopOpt82Insert,
       "hpicfDhcpSnoopOpt82Policy": hpicfDhcpSnoopOpt82Policy,
       "hpicfDhcpSnoopOpt82RemoteId": hpicfDhcpSnoopOpt82RemoteId,
       "hpicfDhcpSnoopErrantReplyEnable": hpicfDhcpSnoopErrantReplyEnable,
       "hpicfDhcpSnoopDatabaseFTPort": hpicfDhcpSnoopDatabaseFTPort,
       "hpicfDhcpSnoopDatabaseSFTPUsername": hpicfDhcpSnoopDatabaseSFTPUsername,
       "hpicfDhcpSnoopDatabaseSFTPPassword": hpicfDhcpSnoopDatabaseSFTPPassword,
       "hpicfDhcpSnoopDatabaseValidateSFTPServer": hpicfDhcpSnoopDatabaseValidateSFTPServer,
       "hpicfDhcpSnoopAllowOverwriteBinding": hpicfDhcpSnoopAllowOverwriteBinding,
       "hpicfDhcpSnoopPortTable": hpicfDhcpSnoopPortTable,
       "hpicfDhcpSnoopPortEntry": hpicfDhcpSnoopPortEntry,
       "hpicfDhcpSnoopPortTrust": hpicfDhcpSnoopPortTrust,
       "hpicfDhcpSnoopPortMaxbind": hpicfDhcpSnoopPortMaxbind,
       "hpicfDhcpSnoopPortStaticBinding": hpicfDhcpSnoopPortStaticBinding,
       "hpicfDhcpSnoopPortDynamicBinding": hpicfDhcpSnoopPortDynamicBinding,
       "hpicfDhcpSnoopServerTable": hpicfDhcpSnoopServerTable,
       "hpicfDhcpSnoopServerEntry": hpicfDhcpSnoopServerEntry,
       "hpicfDhcpSnoopServerAddrType": hpicfDhcpSnoopServerAddrType,
       "hpicfDhcpSnoopServerAddress": hpicfDhcpSnoopServerAddress,
       "hpicfDhcpSnoopServerStatus": hpicfDhcpSnoopServerStatus,
       "hpicfIpStaticBindingsTable": hpicfIpStaticBindingsTable,
       "hpicfIpStaticBindingsEntry": hpicfIpStaticBindingsEntry,
       "hpicfIpStaticBindingsVlan": hpicfIpStaticBindingsVlan,
       "hpicfIpStaticBindingsAddrType": hpicfIpStaticBindingsAddrType,
       "hpicfIpStaticBindingsAddress": hpicfIpStaticBindingsAddress,
       "hpicfIpStaticBindingsMacAddress": hpicfIpStaticBindingsMacAddress,
       "hpicfIpStaticBindingsInterface": hpicfIpStaticBindingsInterface,
       "hpicfIpStaticBindingsStatus": hpicfIpStaticBindingsStatus,
       "hpicfIpDhcpSnoopStatus": hpicfIpDhcpSnoopStatus,
       "hpicfDhcpSnoopGlobalStats": hpicfDhcpSnoopGlobalStats,
       "hpicfDhcpSnoopCSForwards": hpicfDhcpSnoopCSForwards,
       "hpicfDhcpSnoopCSMACMismatches": hpicfDhcpSnoopCSMACMismatches,
       "hpicfDhcpSnoopCSUntrustedOpt82s": hpicfDhcpSnoopCSUntrustedOpt82s,
       "hpicfDhcpSnoopCSBadReleases": hpicfDhcpSnoopCSBadReleases,
       "hpicfDhcpSnoopCSUntrustedDestPorts": hpicfDhcpSnoopCSUntrustedDestPorts,
       "hpicfDhcpSnoopSCForwards": hpicfDhcpSnoopSCForwards,
       "hpicfDhcpSnoopSCUntrustedPorts": hpicfDhcpSnoopSCUntrustedPorts,
       "hpicfDhcpSnoopSCUntrustedServers": hpicfDhcpSnoopSCUntrustedServers,
       "hpicfDhcpSnoopSCOpt82Failures": hpicfDhcpSnoopSCOpt82Failures,
       "hpicfDhcpSnoopDBFileWriteAttempts": hpicfDhcpSnoopDBFileWriteAttempts,
       "hpicfDhcpSnoopDBFileWriteFailures": hpicfDhcpSnoopDBFileWriteFailures,
       "hpicfDhcpSnoopDBFileReadStatus": hpicfDhcpSnoopDBFileReadStatus,
       "hpicfDhcpSnoopDBFileWriteStatus": hpicfDhcpSnoopDBFileWriteStatus,
       "hpicfDhcpSnoopDBFileLastWriteTime": hpicfDhcpSnoopDBFileLastWriteTime,
       "hpicfDhcpSnoopPktsSent": hpicfDhcpSnoopPktsSent,
       "hpicfDhcpSnoopPktsReceived": hpicfDhcpSnoopPktsReceived,
       "hpicfDhcpSnoopPktsDropped": hpicfDhcpSnoopPktsDropped,
       "hpicfDhcpSnoopMaxbindPktsDropped": hpicfDhcpSnoopMaxbindPktsDropped,
       "hpicfDhcpSnoopBindingsTable": hpicfDhcpSnoopBindingsTable,
       "hpicfDhcpSnoopBindingsEntry": hpicfDhcpSnoopBindingsEntry,
       "hpicfDhcpSnoopBindingsVlan": hpicfDhcpSnoopBindingsVlan,
       "hpicfDhcpSnoopBindingsMacAddress": hpicfDhcpSnoopBindingsMacAddress,
       "hpicfDhcpSnoopBindingsAddrType": hpicfDhcpSnoopBindingsAddrType,
       "hpicfDhcpSnoopBindingsAddress": hpicfDhcpSnoopBindingsAddress,
       "hpicfDhcpSnoopBindingsInterface": hpicfDhcpSnoopBindingsInterface,
       "hpicfDhcpSnoopBindingsLeaseTime": hpicfDhcpSnoopBindingsLeaseTime,
       "hpicfDhcpSnoopBindingsType": hpicfDhcpSnoopBindingsType,
       "hpicfDhcpSnoopBindingsSecVlan": hpicfDhcpSnoopBindingsSecVlan,
       "hpicfDhcpSnoopNotifyObjects": hpicfDhcpSnoopNotifyObjects,
       "hpicfDhcpSnoopNotifyCount": hpicfDhcpSnoopNotifyCount,
       "hpicfDhcpSnoopErrantSrcMAC": hpicfDhcpSnoopErrantSrcMAC,
       "hpicfDhcpSnoopErrantSrcIPType": hpicfDhcpSnoopErrantSrcIPType,
       "hpicfDhcpSnoopErrantSrcIP": hpicfDhcpSnoopErrantSrcIP,
       "hpicfDhcpSnoopClearStatsOptions": hpicfDhcpSnoopClearStatsOptions,
       "hpicfDhcpSnoopClearStats": hpicfDhcpSnoopClearStats,
       "hpicfDhcpSnoopClearBindingsOptions": hpicfDhcpSnoopClearBindingsOptions,
       "hpicfDhcpSnoopClearBindings": hpicfDhcpSnoopClearBindings,
       "hpicfDhcpSnoopClearBindingsIpType": hpicfDhcpSnoopClearBindingsIpType,
       "hpicfDhcpSnoopClearBindingsIpAddr": hpicfDhcpSnoopClearBindingsIpAddr,
       "hpicfDhcpSnoopClearBindingsPort": hpicfDhcpSnoopClearBindingsPort,
       "hpicfDhcpSnoopClearBindingsVlan": hpicfDhcpSnoopClearBindingsVlan,
       "hpicfDhcpSnoopConformance": hpicfDhcpSnoopConformance,
       "hpicfIpDhcpSnoopGroups": hpicfIpDhcpSnoopGroups,
       "hpicfDhcpSnoopBaseGroup": hpicfDhcpSnoopBaseGroup,
       "hpicfDhcpSnoopOpt82Group": hpicfDhcpSnoopOpt82Group,
       "hpicfDhcpSnoopServersGroup": hpicfDhcpSnoopServersGroup,
       "hpicfDhcpSnoopDbaseFileGroup": hpicfDhcpSnoopDbaseFileGroup,
       "hpicfDhcpSnoopBindingsGroup": hpicfDhcpSnoopBindingsGroup,
       "hpicfDhcpSnoopStaticBindingsGroup": hpicfDhcpSnoopStaticBindingsGroup,
       "hpicfDhcpSnoopNotifyObjsGroup": hpicfDhcpSnoopNotifyObjsGroup,
       "hpicfDhcpSnoopNotificationGroup": hpicfDhcpSnoopNotificationGroup,
       "hpicfDhcpSnoopPktsGroup": hpicfDhcpSnoopPktsGroup,
       "hpicfDhcpSnoopClearStatsOptionsGroup": hpicfDhcpSnoopClearStatsOptionsGroup,
       "hpicfDhcpSnoopMaxbindingGroup": hpicfDhcpSnoopMaxbindingGroup,
       "hpicfDhcpSnoopPktsGroup1": hpicfDhcpSnoopPktsGroup1,
       "hpicfDhcpSnoopDbaseFileGroup1": hpicfDhcpSnoopDbaseFileGroup1,
       "hpicfDhcpSnoopAllowOverwriteBindingGroup": hpicfDhcpSnoopAllowOverwriteBindingGroup,
       "hpicfDhcpSnoopClearBindingsOptionsGroup": hpicfDhcpSnoopClearBindingsOptionsGroup,
       "hpicfDhcpSnoopCompliances": hpicfDhcpSnoopCompliances,
       "hpicfDhcpSnoopCompliance": hpicfDhcpSnoopCompliance,
       "hpicfDhcpSnoopCompliance2": hpicfDhcpSnoopCompliance2,
       "hpicfDhcpSnoopCompliance3": hpicfDhcpSnoopCompliance3,
       "hpicfDhcpSnoopCompliance4": hpicfDhcpSnoopCompliance4,
       "hpicfDhcpSnoopClearStatsCompliance": hpicfDhcpSnoopClearStatsCompliance,
       "hpicfDhcpSnoopCompliance6": hpicfDhcpSnoopCompliance6,
       "hpicfDhcpSnoopCompliance7": hpicfDhcpSnoopCompliance7,
       "hpicfDhcpSnoopCompliance8": hpicfDhcpSnoopCompliance8,
       "hpicfDhcpSnoopCompliance9": hpicfDhcpSnoopCompliance9,
       "hpicfDhcpSnoopCompliance10": hpicfDhcpSnoopCompliance10}
)
