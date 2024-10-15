# SNMP MIB module (NMS-EPON-EOC-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-EOC-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:40 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponEocConfig_ObjectIdentity = ObjectIdentity
nmsEponEocConfig = _NmsEponEocConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32)
)
_NmsEponEocTftpOper_ObjectIdentity = ObjectIdentity
nmsEponEocTftpOper = _NmsEponEocTftpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1)
)
_TftpServerIpAddr_Type = IpAddress
_TftpServerIpAddr_Object = MibScalar
tftpServerIpAddr = _TftpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 1),
    _TftpServerIpAddr_Type()
)
tftpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIpAddr.setStatus("mandatory")
_TftpServerSourceFileName_Type = OctetString
_TftpServerSourceFileName_Object = MibScalar
tftpServerSourceFileName = _TftpServerSourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 2),
    _TftpServerSourceFileName_Type()
)
tftpServerSourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerSourceFileName.setStatus("mandatory")
_TftpServerDestFileName_Type = OctetString
_TftpServerDestFileName_Object = MibScalar
tftpServerDestFileName = _TftpServerDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 3),
    _TftpServerDestFileName_Type()
)
tftpServerDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerDestFileName.setStatus("mandatory")


class _TftpServerOper_Type(Integer32):
    """Custom type tftpServerOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download_from_onu", 2),
          ("no_operation", 0),
          ("upload_to_onu", 1))
    )


_TftpServerOper_Type.__name__ = "Integer32"
_TftpServerOper_Object = MibScalar
tftpServerOper = _TftpServerOper_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 4),
    _TftpServerOper_Type()
)
tftpServerOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerOper.setStatus("mandatory")
_NmsEponEocBlackWhiteListTable_Object = MibTable
nmsEponEocBlackWhiteListTable = _NmsEponEocBlackWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2)
)
if mibBuilder.loadTexts:
    nmsEponEocBlackWhiteListTable.setStatus("mandatory")
_NmsEponEocBlackWhiteListEntry_Object = MibTableRow
nmsEponEocBlackWhiteListEntry = _NmsEponEocBlackWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1)
)
nmsEponEocBlackWhiteListEntry.setIndexNames(
    (0, "NMS-EPON-EOC-CONF", "authMode"),
    (0, "NMS-EPON-EOC-CONF", "macAddr"),
)
if mibBuilder.loadTexts:
    nmsEponEocBlackWhiteListEntry.setStatus("mandatory")


class _AuthMode_Type(Integer32):
    """Custom type authMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("black_list", 1),
          ("white_list", 2))
    )


_AuthMode_Type.__name__ = "Integer32"
_AuthMode_Object = MibTableColumn
authMode = _AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1, 1),
    _AuthMode_Type()
)
authMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMode.setStatus("mandatory")
_MacAddr_Type = MacAddress
_MacAddr_Object = MibTableColumn
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1, 2),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddr.setStatus("mandatory")


class _ListOper_Type(Integer32):
    """Custom type listOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add_list", 1),
          ("delete_list", 2),
          ("no_action", 0))
    )


_ListOper_Type.__name__ = "Integer32"
_ListOper_Object = MibScalar
listOper = _ListOper_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1, 3),
    _ListOper_Type()
)
listOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listOper.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-EOC-CONF",
    **{"nmsEponEocConfig": nmsEponEocConfig,
       "nmsEponEocTftpOper": nmsEponEocTftpOper,
       "tftpServerIpAddr": tftpServerIpAddr,
       "tftpServerSourceFileName": tftpServerSourceFileName,
       "tftpServerDestFileName": tftpServerDestFileName,
       "tftpServerOper": tftpServerOper,
       "nmsEponEocBlackWhiteListTable": nmsEponEocBlackWhiteListTable,
       "nmsEponEocBlackWhiteListEntry": nmsEponEocBlackWhiteListEntry,
       "authMode": authMode,
       "macAddr": macAddr,
       "listOper": listOper}
)
