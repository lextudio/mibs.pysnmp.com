# SNMP MIB module (CYCLADES-ACS-CONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYCLADES-ACS-CONF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:23 2024
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

(cyACSMgmt,) = mibBuilder.importSymbols(
    "CYCLADES-ACS-MIB",
    "cyACSMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

cyACSConf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2)
)
cyACSConf.setRevisions(
        ("2005-08-29 00:00",
         "2003-06-30 00:00",
         "2003-01-17 00:00",
         "2002-10-20 00:00",
         "2002-09-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CyHostName_Type(DisplayString):
    """Custom type cyHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CyHostName_Type.__name__ = "DisplayString"
_CyHostName_Object = MibScalar
cyHostName = _CyHostName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 1),
    _CyHostName_Type()
)
cyHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyHostName.setStatus("current")


class _CyConsoleBanner_Type(DisplayString):
    """Custom type cyConsoleBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CyConsoleBanner_Type.__name__ = "DisplayString"
_CyConsoleBanner_Object = MibScalar
cyConsoleBanner = _CyConsoleBanner_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 2),
    _CyConsoleBanner_Type()
)
cyConsoleBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyConsoleBanner.setStatus("current")


class _CyMotd_Type(DisplayString):
    """Custom type cyMotd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyMotd_Type.__name__ = "DisplayString"
_CyMotd_Object = MibScalar
cyMotd = _CyMotd_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 3),
    _CyMotd_Type()
)
cyMotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyMotd.setStatus("current")
_CyEthItf_ObjectIdentity = ObjectIdentity
cyEthItf = _CyEthItf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4)
)
if mibBuilder.loadTexts:
    cyEthItf.setStatus("current")


class _CyEthDhcpc_Type(Integer32):
    """Custom type cyEthDhcpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0),
          ("restore", 2))
    )


_CyEthDhcpc_Type.__name__ = "Integer32"
_CyEthDhcpc_Object = MibScalar
cyEthDhcpc = _CyEthDhcpc_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 1),
    _CyEthDhcpc_Type()
)
cyEthDhcpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyEthDhcpc.setStatus("current")
_CyEthIPaddr_Type = IpAddress
_CyEthIPaddr_Object = MibScalar
cyEthIPaddr = _CyEthIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 2),
    _CyEthIPaddr_Type()
)
cyEthIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyEthIPaddr.setStatus("current")
_CyEthIPmask_Type = IpAddress
_CyEthIPmask_Object = MibScalar
cyEthIPmask = _CyEthIPmask_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 3),
    _CyEthIPmask_Type()
)
cyEthIPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyEthIPmask.setStatus("current")
_CyEthMTU_Type = Integer32
_CyEthMTU_Object = MibScalar
cyEthMTU = _CyEthMTU_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 4),
    _CyEthMTU_Type()
)
cyEthMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyEthMTU.setStatus("current")
_CyEthIPaddr2_Type = IpAddress
_CyEthIPaddr2_Object = MibScalar
cyEthIPaddr2 = _CyEthIPaddr2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 5),
    _CyEthIPaddr2_Type()
)
cyEthIPaddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyEthIPaddr2.setStatus("current")
_CyEthIPmask2_Type = IpAddress
_CyEthIPmask2_Object = MibScalar
cyEthIPmask2 = _CyEthIPmask2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 6),
    _CyEthIPmask2_Type()
)
cyEthIPmask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyEthIPmask2.setStatus("current")
_CyNameService_ObjectIdentity = ObjectIdentity
cyNameService = _CyNameService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5)
)
if mibBuilder.loadTexts:
    cyNameService.setStatus("current")


class _CyResolverOrder_Type(DisplayString):
    """Custom type cyResolverOrder based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CyResolverOrder_Type.__name__ = "DisplayString"
_CyResolverOrder_Object = MibScalar
cyResolverOrder = _CyResolverOrder_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 1),
    _CyResolverOrder_Type()
)
cyResolverOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyResolverOrder.setStatus("current")


class _CyMultipleIP_Type(DisplayString):
    """Custom type cyMultipleIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CyMultipleIP_Type.__name__ = "DisplayString"
_CyMultipleIP_Object = MibScalar
cyMultipleIP = _CyMultipleIP_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 2),
    _CyMultipleIP_Type()
)
cyMultipleIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyMultipleIP.setStatus("current")
_CyDNSserv_ObjectIdentity = ObjectIdentity
cyDNSserv = _CyDNSserv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cyDNSserv.setStatus("current")
_CyDNSpriserv_Type = IpAddress
_CyDNSpriserv_Object = MibScalar
cyDNSpriserv = _CyDNSpriserv_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3, 1),
    _CyDNSpriserv_Type()
)
cyDNSpriserv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyDNSpriserv.setStatus("current")
_CyDNSsecserv_Type = IpAddress
_CyDNSsecserv_Object = MibScalar
cyDNSsecserv = _CyDNSsecserv_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3, 2),
    _CyDNSsecserv_Type()
)
cyDNSsecserv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyDNSsecserv.setStatus("current")


class _CyDNSdomain_Type(DisplayString):
    """Custom type cyDNSdomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CyDNSdomain_Type.__name__ = "DisplayString"
_CyDNSdomain_Object = MibScalar
cyDNSdomain = _CyDNSdomain_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3, 3),
    _CyDNSdomain_Type()
)
cyDNSdomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyDNSdomain.setStatus("current")
_CySerialPortConf_ObjectIdentity = ObjectIdentity
cySerialPortConf = _CySerialPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6)
)
if mibBuilder.loadTexts:
    cySerialPortConf.setStatus("current")
_CySerialGlobal_ObjectIdentity = ObjectIdentity
cySerialGlobal = _CySerialGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cySerialGlobal.setStatus("current")


class _CySerialInclude_Type(DisplayString):
    """Custom type cySerialInclude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySerialInclude_Type.__name__ = "DisplayString"
_CySerialInclude_Object = MibScalar
cySerialInclude = _CySerialInclude_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 1),
    _CySerialInclude_Type()
)
cySerialInclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialInclude.setStatus("current")


class _CySerialNFS_Type(DisplayString):
    """Custom type cySerialNFS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CySerialNFS_Type.__name__ = "DisplayString"
_CySerialNFS_Object = MibScalar
cySerialNFS = _CySerialNFS_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 2),
    _CySerialNFS_Type()
)
cySerialNFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialNFS.setStatus("current")


class _CySerialLockDir_Type(DisplayString):
    """Custom type cySerialLockDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CySerialLockDir_Type.__name__ = "DisplayString"
_CySerialLockDir_Object = MibScalar
cySerialLockDir = _CySerialLockDir_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 3),
    _CySerialLockDir_Type()
)
cySerialLockDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialLockDir.setStatus("current")


class _CySerialRlogin_Type(DisplayString):
    """Custom type cySerialRlogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CySerialRlogin_Type.__name__ = "DisplayString"
_CySerialRlogin_Object = MibScalar
cySerialRlogin = _CySerialRlogin_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 4),
    _CySerialRlogin_Type()
)
cySerialRlogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialRlogin.setStatus("current")


class _CySerialPppd_Type(DisplayString):
    """Custom type cySerialPppd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CySerialPppd_Type.__name__ = "DisplayString"
_CySerialPppd_Object = MibScalar
cySerialPppd = _CySerialPppd_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 5),
    _CySerialPppd_Type()
)
cySerialPppd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialPppd.setStatus("current")


class _CySerialTelnet_Type(DisplayString):
    """Custom type cySerialTelnet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CySerialTelnet_Type.__name__ = "DisplayString"
_CySerialTelnet_Object = MibScalar
cySerialTelnet = _CySerialTelnet_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 6),
    _CySerialTelnet_Type()
)
cySerialTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialTelnet.setStatus("current")


class _CySerialSsh_Type(DisplayString):
    """Custom type cySerialSsh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CySerialSsh_Type.__name__ = "DisplayString"
_CySerialSsh_Object = MibScalar
cySerialSsh = _CySerialSsh_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 7),
    _CySerialSsh_Type()
)
cySerialSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialSsh.setStatus("current")


class _CySerialLocalLogins_Type(Integer32):
    """Custom type cySerialLocalLogins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CySerialLocalLogins_Type.__name__ = "Integer32"
_CySerialLocalLogins_Object = MibScalar
cySerialLocalLogins = _CySerialLocalLogins_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 8),
    _CySerialLocalLogins_Type()
)
cySerialLocalLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialLocalLogins.setStatus("current")
_CySerialFacility_Type = Integer32
_CySerialFacility_Object = MibScalar
cySerialFacility = _CySerialFacility_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 9),
    _CySerialFacility_Type()
)
cySerialFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialFacility.setStatus("current")
_CySerialDBFacility_Type = Integer32
_CySerialDBFacility_Object = MibScalar
cySerialDBFacility = _CySerialDBFacility_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 10),
    _CySerialDBFacility_Type()
)
cySerialDBFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySerialDBFacility.setStatus("current")
_CySerialGroupTable_Object = MibTable
cySerialGroupTable = _CySerialGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11)
)
if mibBuilder.loadTexts:
    cySerialGroupTable.setStatus("current")
_CygroupEntry_Object = MibTableRow
cygroupEntry = _CygroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1)
)
cygroupEntry.setIndexNames(
    (0, "CYCLADES-ACS-CONF-MIB", "cyGroupIndex"),
)
if mibBuilder.loadTexts:
    cygroupEntry.setStatus("current")
_CyGroupIndex_Type = InterfaceIndexOrZero
_CyGroupIndex_Object = MibTableColumn
cyGroupIndex = _CyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1, 1),
    _CyGroupIndex_Type()
)
cyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyGroupIndex.setStatus("current")


class _CyGroupName_Type(DisplayString):
    """Custom type cyGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CyGroupName_Type.__name__ = "DisplayString"
_CyGroupName_Object = MibTableColumn
cyGroupName = _CyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1, 2),
    _CyGroupName_Type()
)
cyGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyGroupName.setStatus("current")


class _CyGroupUsers_Type(DisplayString):
    """Custom type cyGroupUsers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyGroupUsers_Type.__name__ = "DisplayString"
_CyGroupUsers_Object = MibTableColumn
cyGroupUsers = _CyGroupUsers_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1, 3),
    _CyGroupUsers_Type()
)
cyGroupUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyGroupUsers.setStatus("current")
_CySerialSpec_ObjectIdentity = ObjectIdentity
cySerialSpec = _CySerialSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cySerialSpec.setStatus("current")
_CySerialPortTable_Object = MibTable
cySerialPortTable = _CySerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cySerialPortTable.setStatus("current")
_CysportEntry_Object = MibTableRow
cysportEntry = _CysportEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1)
)
cysportEntry.setIndexNames(
    (0, "CYCLADES-ACS-CONF-MIB", "cySPortNumber"),
)
if mibBuilder.loadTexts:
    cysportEntry.setStatus("current")
_CySPortNumber_Type = InterfaceIndexOrZero
_CySPortNumber_Object = MibTableColumn
cySPortNumber = _CySPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 1),
    _CySPortNumber_Type()
)
cySPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cySPortNumber.setStatus("current")


class _CySPortTty_Type(DisplayString):
    """Custom type cySPortTty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CySPortTty_Type.__name__ = "DisplayString"
_CySPortTty_Object = MibTableColumn
cySPortTty = _CySPortTty_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 2),
    _CySPortTty_Type()
)
cySPortTty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortTty.setStatus("current")


class _CySPortName_Type(DisplayString):
    """Custom type cySPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortName_Type.__name__ = "DisplayString"
_CySPortName_Object = MibTableColumn
cySPortName = _CySPortName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 3),
    _CySPortName_Type()
)
cySPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortName.setStatus("current")


class _CySPortSpeed_Type(Integer32):
    """Custom type cySPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              75,
              110,
              134,
              150,
              200,
              300,
              600,
              1200,
              1800,
              2400,
              4800,
              9600,
              14400,
              19200,
              28800,
              38400,
              57600,
              115200,
              230400,
              460800)
        )
    )
    namedValues = NamedValues(
        *(("s110bps", 110),
          ("s115200bps", 115200),
          ("s1200bps", 1200),
          ("s134bps", 134),
          ("s14400bps", 14400),
          ("s150bps", 150),
          ("s1800bps", 1800),
          ("s19200bps", 19200),
          ("s200bps", 200),
          ("s230400bps", 230400),
          ("s2400bps", 2400),
          ("s28800bps", 28800),
          ("s300bps", 300),
          ("s38400bps", 38400),
          ("s460800bps", 460800),
          ("s4800bps", 4800),
          ("s50bps", 50),
          ("s57600bps", 57600),
          ("s600bps", 600),
          ("s75bps", 75),
          ("s9600bps", 9600))
    )


_CySPortSpeed_Type.__name__ = "Integer32"
_CySPortSpeed_Object = MibTableColumn
cySPortSpeed = _CySPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 4),
    _CySPortSpeed_Type()
)
cySPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSpeed.setStatus("current")


class _CySPortDataSize_Type(Integer32):
    """Custom type cySPortDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_CySPortDataSize_Type.__name__ = "Integer32"
_CySPortDataSize_Object = MibTableColumn
cySPortDataSize = _CySPortDataSize_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 5),
    _CySPortDataSize_Type()
)
cySPortDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDataSize.setStatus("current")


class _CySPortStopBits_Type(Integer32):
    """Custom type cySPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CySPortStopBits_Type.__name__ = "Integer32"
_CySPortStopBits_Object = MibTableColumn
cySPortStopBits = _CySPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 6),
    _CySPortStopBits_Type()
)
cySPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortStopBits.setStatus("current")


class _CySPortParity_Type(DisplayString):
    """Custom type cySPortParity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CySPortParity_Type.__name__ = "DisplayString"
_CySPortParity_Object = MibTableColumn
cySPortParity = _CySPortParity_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 7),
    _CySPortParity_Type()
)
cySPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortParity.setStatus("current")


class _CySPortFlowCtrl_Type(DisplayString):
    """Custom type cySPortFlowCtrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CySPortFlowCtrl_Type.__name__ = "DisplayString"
_CySPortFlowCtrl_Object = MibTableColumn
cySPortFlowCtrl = _CySPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 8),
    _CySPortFlowCtrl_Type()
)
cySPortFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortFlowCtrl.setStatus("current")
_CySPortDTRdelay_Type = Integer32
_CySPortDTRdelay_Object = MibTableColumn
cySPortDTRdelay = _CySPortDTRdelay_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 9),
    _CySPortDTRdelay_Type()
)
cySPortDTRdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDTRdelay.setStatus("current")


class _CySPortDCDCtrl_Type(Integer32):
    """Custom type cySPortDCDCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("control", 1),
          ("notctrl", 0))
    )


_CySPortDCDCtrl_Type.__name__ = "Integer32"
_CySPortDCDCtrl_Object = MibTableColumn
cySPortDCDCtrl = _CySPortDCDCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 10),
    _CySPortDCDCtrl_Type()
)
cySPortDCDCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDCDCtrl.setStatus("current")


class _CySPortLogUtmp_Type(Integer32):
    """Custom type cySPortLogUtmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_CySPortLogUtmp_Type.__name__ = "Integer32"
_CySPortLogUtmp_Object = MibTableColumn
cySPortLogUtmp = _CySPortLogUtmp_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 11),
    _CySPortLogUtmp_Type()
)
cySPortLogUtmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortLogUtmp.setStatus("current")


class _CySPortLogWtmp_Type(Integer32):
    """Custom type cySPortLogWtmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_CySPortLogWtmp_Type.__name__ = "Integer32"
_CySPortLogWtmp_Object = MibTableColumn
cySPortLogWtmp = _CySPortLogWtmp_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 12),
    _CySPortLogWtmp_Type()
)
cySPortLogWtmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortLogWtmp.setStatus("current")


class _CySPortLogform_Type(DisplayString):
    """Custom type cySPortLogform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortLogform_Type.__name__ = "DisplayString"
_CySPortLogform_Object = MibTableColumn
cySPortLogform = _CySPortLogform_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 13),
    _CySPortLogform_Type()
)
cySPortLogform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortLogform.setStatus("current")


class _CySPortAuthtype_Type(DisplayString):
    """Custom type cySPortAuthtype based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CySPortAuthtype_Type.__name__ = "DisplayString"
_CySPortAuthtype_Object = MibTableColumn
cySPortAuthtype = _CySPortAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 14),
    _CySPortAuthtype_Type()
)
cySPortAuthtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthtype.setStatus("current")
_CySPortAuthSrv1_Type = IpAddress
_CySPortAuthSrv1_Object = MibTableColumn
cySPortAuthSrv1 = _CySPortAuthSrv1_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 15),
    _CySPortAuthSrv1_Type()
)
cySPortAuthSrv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthSrv1.setStatus("current")
_CySPortAccSrv1_Type = IpAddress
_CySPortAccSrv1_Object = MibTableColumn
cySPortAccSrv1 = _CySPortAccSrv1_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 16),
    _CySPortAccSrv1_Type()
)
cySPortAccSrv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAccSrv1.setStatus("current")
_CySPortAuthTmo_Type = Integer32
_CySPortAuthTmo_Object = MibTableColumn
cySPortAuthTmo = _CySPortAuthTmo_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 17),
    _CySPortAuthTmo_Type()
)
cySPortAuthTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthTmo.setStatus("current")
_CySPortAuthRetr_Type = Integer32
_CySPortAuthRetr_Object = MibTableColumn
cySPortAuthRetr = _CySPortAuthRetr_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 18),
    _CySPortAuthRetr_Type()
)
cySPortAuthRetr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthRetr.setStatus("current")
_CySPortAuthSrv2_Type = IpAddress
_CySPortAuthSrv2_Object = MibTableColumn
cySPortAuthSrv2 = _CySPortAuthSrv2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 19),
    _CySPortAuthSrv2_Type()
)
cySPortAuthSrv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthSrv2.setStatus("current")
_CySPortAccSrv2_Type = IpAddress
_CySPortAccSrv2_Object = MibTableColumn
cySPortAccSrv2 = _CySPortAccSrv2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 20),
    _CySPortAccSrv2_Type()
)
cySPortAccSrv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAccSrv2.setStatus("current")


class _CySPortAuthSecret_Type(DisplayString):
    """Custom type cySPortAuthSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortAuthSecret_Type.__name__ = "DisplayString"
_CySPortAuthSecret_Object = MibTableColumn
cySPortAuthSecret = _CySPortAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 21),
    _CySPortAuthSecret_Type()
)
cySPortAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthSecret.setStatus("current")


class _CySPortAuthRadP_Type(Integer32):
    """Custom type cySPortAuthRadP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_CySPortAuthRadP_Type.__name__ = "Integer32"
_CySPortAuthRadP_Object = MibTableColumn
cySPortAuthRadP = _CySPortAuthRadP_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 22),
    _CySPortAuthRadP_Type()
)
cySPortAuthRadP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthRadP.setStatus("current")


class _CySPortAuthAcc_Type(DisplayString):
    """Custom type cySPortAuthAcc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortAuthAcc_Type.__name__ = "DisplayString"
_CySPortAuthAcc_Object = MibTableColumn
cySPortAuthAcc = _CySPortAuthAcc_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 23),
    _CySPortAuthAcc_Type()
)
cySPortAuthAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAuthAcc.setStatus("current")


class _CySPortProtocol_Type(DisplayString):
    """Custom type cySPortProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortProtocol_Type.__name__ = "DisplayString"
_CySPortProtocol_Object = MibTableColumn
cySPortProtocol = _CySPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 24),
    _CySPortProtocol_Type()
)
cySPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortProtocol.setStatus("current")


class _CySPortRemoteIP_Type(DisplayString):
    """Custom type cySPortRemoteIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CySPortRemoteIP_Type.__name__ = "DisplayString"
_CySPortRemoteIP_Object = MibTableColumn
cySPortRemoteIP = _CySPortRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 25),
    _CySPortRemoteIP_Type()
)
cySPortRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortRemoteIP.setStatus("current")


class _CySPortSocketPort_Type(DisplayString):
    """Custom type cySPortSocketPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CySPortSocketPort_Type.__name__ = "DisplayString"
_CySPortSocketPort_Object = MibTableColumn
cySPortSocketPort = _CySPortSocketPort_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 26),
    _CySPortSocketPort_Type()
)
cySPortSocketPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSocketPort.setStatus("current")
_CySPortRemHost_Type = IpAddress
_CySPortRemHost_Object = MibTableColumn
cySPortRemHost = _CySPortRemHost_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 27),
    _CySPortRemHost_Type()
)
cySPortRemHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortRemHost.setStatus("current")


class _CySPortBanner_Type(DisplayString):
    """Custom type cySPortBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_CySPortBanner_Type.__name__ = "DisplayString"
_CySPortBanner_Object = MibTableColumn
cySPortBanner = _CySPortBanner_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 28),
    _CySPortBanner_Type()
)
cySPortBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortBanner.setStatus("current")


class _CySPortPrompt_Type(DisplayString):
    """Custom type cySPortPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_CySPortPrompt_Type.__name__ = "DisplayString"
_CySPortPrompt_Object = MibTableColumn
cySPortPrompt = _CySPortPrompt_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 29),
    _CySPortPrompt_Type()
)
cySPortPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPrompt.setStatus("current")


class _CySPortTermType_Type(DisplayString):
    """Custom type cySPortTermType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CySPortTermType_Type.__name__ = "DisplayString"
_CySPortTermType_Object = MibTableColumn
cySPortTermType = _CySPortTermType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 30),
    _CySPortTermType_Type()
)
cySPortTermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortTermType.setStatus("current")


class _CySPortAutomUsr_Type(DisplayString):
    """Custom type cySPortAutomUsr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortAutomUsr_Type.__name__ = "DisplayString"
_CySPortAutomUsr_Object = MibTableColumn
cySPortAutomUsr = _CySPortAutomUsr_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 31),
    _CySPortAutomUsr_Type()
)
cySPortAutomUsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAutomUsr.setStatus("current")
_CySPortNetMask_Type = IpAddress
_CySPortNetMask_Object = MibTableColumn
cySPortNetMask = _CySPortNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 32),
    _CySPortNetMask_Type()
)
cySPortNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortNetMask.setStatus("current")
_CySPortPppMtu_Type = Integer32
_CySPortPppMtu_Object = MibTableColumn
cySPortPppMtu = _CySPortPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 33),
    _CySPortPppMtu_Type()
)
cySPortPppMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPppMtu.setStatus("current")
_CySPortPppMru_Type = Integer32
_CySPortPppMru_Object = MibTableColumn
cySPortPppMru = _CySPortPppMru_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 34),
    _CySPortPppMru_Type()
)
cySPortPppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPppMru.setStatus("current")
_CySPortPppOptions_Type = DisplayString
_CySPortPppOptions_Object = MibTableColumn
cySPortPppOptions = _CySPortPppOptions_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 35),
    _CySPortPppOptions_Type()
)
cySPortPppOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPppOptions.setStatus("current")
_CySPortPppFoption_Type = DisplayString
_CySPortPppFoption_Object = MibTableColumn
cySPortPppFoption = _CySPortPppFoption_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 36),
    _CySPortPppFoption_Type()
)
cySPortPppFoption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPppFoption.setStatus("current")
_CySPortModemChat_Type = DisplayString
_CySPortModemChat_Object = MibTableColumn
cySPortModemChat = _CySPortModemChat_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 37),
    _CySPortModemChat_Type()
)
cySPortModemChat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortModemChat.setStatus("current")


class _CySPortSttyCmd_Type(DisplayString):
    """Custom type cySPortSttyCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_CySPortSttyCmd_Type.__name__ = "DisplayString"
_CySPortSttyCmd_Object = MibTableColumn
cySPortSttyCmd = _CySPortSttyCmd_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 38),
    _CySPortSttyCmd_Type()
)
cySPortSttyCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSttyCmd.setStatus("current")
_CySPortSockTx_Type = Integer32
_CySPortSockTx_Object = MibTableColumn
cySPortSockTx = _CySPortSockTx_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 39),
    _CySPortSockTx_Type()
)
cySPortSockTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSockTx.setStatus("current")
_CySPortSockPoll_Type = Integer32
_CySPortSockPoll_Object = MibTableColumn
cySPortSockPoll = _CySPortSockPoll_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 40),
    _CySPortSockPoll_Type()
)
cySPortSockPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSockPoll.setStatus("current")
_CySPortSockIdle_Type = Integer32
_CySPortSockIdle_Object = MibTableColumn
cySPortSockIdle = _CySPortSockIdle_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 41),
    _CySPortSockIdle_Type()
)
cySPortSockIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSockIdle.setStatus("current")
_CySPortDBsize_Type = Integer32
_CySPortDBsize_Object = MibTableColumn
cySPortDBsize = _CySPortDBsize_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 42),
    _CySPortDBsize_Type()
)
cySPortDBsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDBsize.setStatus("current")


class _CySPortDBtime_Type(Integer32):
    """Custom type cySPortDBtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_CySPortDBtime_Type.__name__ = "Integer32"
_CySPortDBtime_Object = MibTableColumn
cySPortDBtime = _CySPortDBtime_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 43),
    _CySPortDBtime_Type()
)
cySPortDBtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDBtime.setStatus("current")


class _CySPortDBmode_Type(DisplayString):
    """Custom type cySPortDBmode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CySPortDBmode_Type.__name__ = "DisplayString"
_CySPortDBmode_Object = MibTableColumn
cySPortDBmode = _CySPortDBmode_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 44),
    _CySPortDBmode_Type()
)
cySPortDBmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDBmode.setStatus("current")
_CySPortDBsyslog_Type = Integer32
_CySPortDBsyslog_Object = MibTableColumn
cySPortDBsyslog = _CySPortDBsyslog_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 45),
    _CySPortDBsyslog_Type()
)
cySPortDBsyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDBsyslog.setStatus("current")


class _CySPortDBmenu_Type(Integer32):
    """Custom type cySPortDBmenu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("displayDB", 2),
          ("displayMenu", 0),
          ("displayParc", 3),
          ("inactive", 1))
    )


_CySPortDBmenu_Type.__name__ = "Integer32"
_CySPortDBmenu_Object = MibTableColumn
cySPortDBmenu = _CySPortDBmenu_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 46),
    _CySPortDBmenu_Type()
)
cySPortDBmenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDBmenu.setStatus("current")


class _CySPortDBalarm_Type(Integer32):
    """Custom type cySPortDBalarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_CySPortDBalarm_Type.__name__ = "Integer32"
_CySPortDBalarm_Object = MibTableColumn
cySPortDBalarm = _CySPortDBalarm_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 47),
    _CySPortDBalarm_Type()
)
cySPortDBalarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortDBalarm.setStatus("current")


class _CySPortSSHbreak_Type(DisplayString):
    """Custom type cySPortSSHbreak based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CySPortSSHbreak_Type.__name__ = "DisplayString"
_CySPortSSHbreak_Object = MibTableColumn
cySPortSSHbreak = _CySPortSSHbreak_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 48),
    _CySPortSSHbreak_Type()
)
cySPortSSHbreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSSHbreak.setStatus("current")


class _CySPortSniffSess_Type(DisplayString):
    """Custom type cySPortSniffSess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CySPortSniffSess_Type.__name__ = "DisplayString"
_CySPortSniffSess_Object = MibTableColumn
cySPortSniffSess = _CySPortSniffSess_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 49),
    _CySPortSniffSess_Type()
)
cySPortSniffSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSniffSess.setStatus("current")


class _CySPortSniffAdm_Type(DisplayString):
    """Custom type cySPortSniffAdm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortSniffAdm_Type.__name__ = "DisplayString"
_CySPortSniffAdm_Object = MibTableColumn
cySPortSniffAdm = _CySPortSniffAdm_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 50),
    _CySPortSniffAdm_Type()
)
cySPortSniffAdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSniffAdm.setStatus("current")


class _CySPortSniffEsc_Type(DisplayString):
    """Custom type cySPortSniffEsc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CySPortSniffEsc_Type.__name__ = "DisplayString"
_CySPortSniffEsc_Object = MibTableColumn
cySPortSniffEsc = _CySPortSniffEsc_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 51),
    _CySPortSniffEsc_Type()
)
cySPortSniffEsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSniffEsc.setStatus("current")


class _CySPortSniffMsess_Type(DisplayString):
    """Custom type cySPortSniffMsess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CySPortSniffMsess_Type.__name__ = "DisplayString"
_CySPortSniffMsess_Object = MibTableColumn
cySPortSniffMsess = _CySPortSniffMsess_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 52),
    _CySPortSniffMsess_Type()
)
cySPortSniffMsess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSniffMsess.setStatus("current")


class _CySPortTelnetMode_Type(Integer32):
    """Custom type cySPortTelnetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("binary", 1),
          ("text", 0))
    )


_CySPortTelnetMode_Type.__name__ = "Integer32"
_CySPortTelnetMode_Object = MibTableColumn
cySPortTelnetMode = _CySPortTelnetMode_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 53),
    _CySPortTelnetMode_Type()
)
cySPortTelnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortTelnetMode.setStatus("current")


class _CySPortSysBufSess_Type(Integer32):
    """Custom type cySPortSysBufSess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_CySPortSysBufSess_Type.__name__ = "Integer32"
_CySPortSysBufSess_Object = MibTableColumn
cySPortSysBufSess = _CySPortSysBufSess_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 54),
    _CySPortSysBufSess_Type()
)
cySPortSysBufSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortSysBufSess.setStatus("current")


class _CySPortLFSuppress_Type(Integer32):
    """Custom type cySPortLFSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_CySPortLFSuppress_Type.__name__ = "Integer32"
_CySPortLFSuppress_Object = MibTableColumn
cySPortLFSuppress = _CySPortLFSuppress_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 55),
    _CySPortLFSuppress_Type()
)
cySPortLFSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortLFSuppress.setStatus("current")


class _CySPortAutoInput_Type(DisplayString):
    """Custom type cySPortAutoInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortAutoInput_Type.__name__ = "DisplayString"
_CySPortAutoInput_Object = MibTableColumn
cySPortAutoInput = _CySPortAutoInput_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 56),
    _CySPortAutoInput_Type()
)
cySPortAutoInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAutoInput.setStatus("current")


class _CySPortAutoOutput_Type(DisplayString):
    """Custom type cySPortAutoOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortAutoOutput_Type.__name__ = "DisplayString"
_CySPortAutoOutput_Object = MibTableColumn
cySPortAutoOutput = _CySPortAutoOutput_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 57),
    _CySPortAutoOutput_Type()
)
cySPortAutoOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortAutoOutput.setStatus("current")


class _CySPortPmType_Type(DisplayString):
    """Custom type cySPortPmType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CySPortPmType_Type.__name__ = "DisplayString"
_CySPortPmType_Object = MibTableColumn
cySPortPmType = _CySPortPmType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 58),
    _CySPortPmType_Type()
)
cySPortPmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPmType.setStatus("current")


class _CySPortPmUsers_Type(DisplayString):
    """Custom type cySPortPmUsers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortPmUsers_Type.__name__ = "DisplayString"
_CySPortPmUsers_Object = MibTableColumn
cySPortPmUsers = _CySPortPmUsers_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 59),
    _CySPortPmUsers_Type()
)
cySPortPmUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPmUsers.setStatus("current")


class _CySPortPmOutlet_Type(DisplayString):
    """Custom type cySPortPmOutlet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CySPortPmOutlet_Type.__name__ = "DisplayString"
_CySPortPmOutlet_Object = MibTableColumn
cySPortPmOutlet = _CySPortPmOutlet_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 60),
    _CySPortPmOutlet_Type()
)
cySPortPmOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPmOutlet.setStatus("current")


class _CySPortPmKey_Type(DisplayString):
    """Custom type cySPortPmKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CySPortPmKey_Type.__name__ = "DisplayString"
_CySPortPmKey_Object = MibTableColumn
cySPortPmKey = _CySPortPmKey_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 61),
    _CySPortPmKey_Type()
)
cySPortPmKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPmKey.setStatus("current")
_CySPortPmNOutlets_Type = Integer32
_CySPortPmNOutlets_Object = MibTableColumn
cySPortPmNOutlets = _CySPortPmNOutlets_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 62),
    _CySPortPmNOutlets_Type()
)
cySPortPmNOutlets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortPmNOutlets.setStatus("current")
_CySPortBreakInterval_Type = Integer32
_CySPortBreakInterval_Object = MibTableColumn
cySPortBreakInterval = _CySPortBreakInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 63),
    _CySPortBreakInterval_Type()
)
cySPortBreakInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cySPortBreakInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS-CONF-MIB",
    **{"cyACSConf": cyACSConf,
       "cyHostName": cyHostName,
       "cyConsoleBanner": cyConsoleBanner,
       "cyMotd": cyMotd,
       "cyEthItf": cyEthItf,
       "cyEthDhcpc": cyEthDhcpc,
       "cyEthIPaddr": cyEthIPaddr,
       "cyEthIPmask": cyEthIPmask,
       "cyEthMTU": cyEthMTU,
       "cyEthIPaddr2": cyEthIPaddr2,
       "cyEthIPmask2": cyEthIPmask2,
       "cyNameService": cyNameService,
       "cyResolverOrder": cyResolverOrder,
       "cyMultipleIP": cyMultipleIP,
       "cyDNSserv": cyDNSserv,
       "cyDNSpriserv": cyDNSpriserv,
       "cyDNSsecserv": cyDNSsecserv,
       "cyDNSdomain": cyDNSdomain,
       "cySerialPortConf": cySerialPortConf,
       "cySerialGlobal": cySerialGlobal,
       "cySerialInclude": cySerialInclude,
       "cySerialNFS": cySerialNFS,
       "cySerialLockDir": cySerialLockDir,
       "cySerialRlogin": cySerialRlogin,
       "cySerialPppd": cySerialPppd,
       "cySerialTelnet": cySerialTelnet,
       "cySerialSsh": cySerialSsh,
       "cySerialLocalLogins": cySerialLocalLogins,
       "cySerialFacility": cySerialFacility,
       "cySerialDBFacility": cySerialDBFacility,
       "cySerialGroupTable": cySerialGroupTable,
       "cygroupEntry": cygroupEntry,
       "cyGroupIndex": cyGroupIndex,
       "cyGroupName": cyGroupName,
       "cyGroupUsers": cyGroupUsers,
       "cySerialSpec": cySerialSpec,
       "cySerialPortTable": cySerialPortTable,
       "cysportEntry": cysportEntry,
       "cySPortNumber": cySPortNumber,
       "cySPortTty": cySPortTty,
       "cySPortName": cySPortName,
       "cySPortSpeed": cySPortSpeed,
       "cySPortDataSize": cySPortDataSize,
       "cySPortStopBits": cySPortStopBits,
       "cySPortParity": cySPortParity,
       "cySPortFlowCtrl": cySPortFlowCtrl,
       "cySPortDTRdelay": cySPortDTRdelay,
       "cySPortDCDCtrl": cySPortDCDCtrl,
       "cySPortLogUtmp": cySPortLogUtmp,
       "cySPortLogWtmp": cySPortLogWtmp,
       "cySPortLogform": cySPortLogform,
       "cySPortAuthtype": cySPortAuthtype,
       "cySPortAuthSrv1": cySPortAuthSrv1,
       "cySPortAccSrv1": cySPortAccSrv1,
       "cySPortAuthTmo": cySPortAuthTmo,
       "cySPortAuthRetr": cySPortAuthRetr,
       "cySPortAuthSrv2": cySPortAuthSrv2,
       "cySPortAccSrv2": cySPortAccSrv2,
       "cySPortAuthSecret": cySPortAuthSecret,
       "cySPortAuthRadP": cySPortAuthRadP,
       "cySPortAuthAcc": cySPortAuthAcc,
       "cySPortProtocol": cySPortProtocol,
       "cySPortRemoteIP": cySPortRemoteIP,
       "cySPortSocketPort": cySPortSocketPort,
       "cySPortRemHost": cySPortRemHost,
       "cySPortBanner": cySPortBanner,
       "cySPortPrompt": cySPortPrompt,
       "cySPortTermType": cySPortTermType,
       "cySPortAutomUsr": cySPortAutomUsr,
       "cySPortNetMask": cySPortNetMask,
       "cySPortPppMtu": cySPortPppMtu,
       "cySPortPppMru": cySPortPppMru,
       "cySPortPppOptions": cySPortPppOptions,
       "cySPortPppFoption": cySPortPppFoption,
       "cySPortModemChat": cySPortModemChat,
       "cySPortSttyCmd": cySPortSttyCmd,
       "cySPortSockTx": cySPortSockTx,
       "cySPortSockPoll": cySPortSockPoll,
       "cySPortSockIdle": cySPortSockIdle,
       "cySPortDBsize": cySPortDBsize,
       "cySPortDBtime": cySPortDBtime,
       "cySPortDBmode": cySPortDBmode,
       "cySPortDBsyslog": cySPortDBsyslog,
       "cySPortDBmenu": cySPortDBmenu,
       "cySPortDBalarm": cySPortDBalarm,
       "cySPortSSHbreak": cySPortSSHbreak,
       "cySPortSniffSess": cySPortSniffSess,
       "cySPortSniffAdm": cySPortSniffAdm,
       "cySPortSniffEsc": cySPortSniffEsc,
       "cySPortSniffMsess": cySPortSniffMsess,
       "cySPortTelnetMode": cySPortTelnetMode,
       "cySPortSysBufSess": cySPortSysBufSess,
       "cySPortLFSuppress": cySPortLFSuppress,
       "cySPortAutoInput": cySPortAutoInput,
       "cySPortAutoOutput": cySPortAutoOutput,
       "cySPortPmType": cySPortPmType,
       "cySPortPmUsers": cySPortPmUsers,
       "cySPortPmOutlet": cySPortPmOutlet,
       "cySPortPmKey": cySPortPmKey,
       "cySPortPmNOutlets": cySPortPmNOutlets,
       "cySPortBreakInterval": cySPortBreakInterval}
)
