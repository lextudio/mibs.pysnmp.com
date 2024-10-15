# SNMP MIB module (NETSCREEN-SET-WEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-WEB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:59 2024
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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

netscreenSetWebMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 12)
)
netscreenSetWebMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-12 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetWebUI_ObjectIdentity = ObjectIdentity
nsSetWebUI = _NsSetWebUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12)
)
_NsSetWebUICfgTable_Object = MibTable
nsSetWebUICfgTable = _NsSetWebUICfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1)
)
if mibBuilder.loadTexts:
    nsSetWebUICfgTable.setStatus("current")
_NsSetWebUICfgEntry_Object = MibTableRow
nsSetWebUICfgEntry = _NsSetWebUICfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1)
)
nsSetWebUICfgEntry.setIndexNames(
    (0, "NETSCREEN-SET-WEB-MIB", "nsSetWebVsys"),
)
if mibBuilder.loadTexts:
    nsSetWebUICfgEntry.setStatus("current")


class _NsSetWebVsys_Type(Integer32):
    """Custom type nsSetWebVsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSetWebVsys_Type.__name__ = "Integer32"
_NsSetWebVsys_Object = MibTableColumn
nsSetWebVsys = _NsSetWebVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 1),
    _NsSetWebVsys_Type()
)
nsSetWebVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebVsys.setStatus("current")


class _NsSetWebIdleTimeout_Type(Integer32):
    """Custom type nsSetWebIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetWebIdleTimeout_Type.__name__ = "Integer32"
_NsSetWebIdleTimeout_Object = MibTableColumn
nsSetWebIdleTimeout = _NsSetWebIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 2),
    _NsSetWebIdleTimeout_Type()
)
nsSetWebIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebIdleTimeout.setStatus("current")
_NsSetWebTimeout_Type = Integer32
_NsSetWebTimeout_Object = MibTableColumn
nsSetWebTimeout = _NsSetWebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 3),
    _NsSetWebTimeout_Type()
)
nsSetWebTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebTimeout.setStatus("current")
_NsSetWebPort_Type = Integer32
_NsSetWebPort_Object = MibTableColumn
nsSetWebPort = _NsSetWebPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 4),
    _NsSetWebPort_Type()
)
nsSetWebPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebPort.setStatus("current")
_NsSetWebSSLPort_Type = Integer32
_NsSetWebSSLPort_Object = MibTableColumn
nsSetWebSSLPort = _NsSetWebSSLPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 5),
    _NsSetWebSSLPort_Type()
)
nsSetWebSSLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebSSLPort.setStatus("current")


class _NsSetWebSSLCertificate_Type(DisplayString):
    """Custom type nsSetWebSSLCertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetWebSSLCertificate_Type.__name__ = "DisplayString"
_NsSetWebSSLCertificate_Object = MibTableColumn
nsSetWebSSLCertificate = _NsSetWebSSLCertificate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 6),
    _NsSetWebSSLCertificate_Type()
)
nsSetWebSSLCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebSSLCertificate.setStatus("current")


class _NsSetWebSSLCipher_Type(Integer32):
    """Custom type nsSetWebSSLCipher based on Integer32"""
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
        *(("des-sha", 2),
          ("rc4-40-md5", 1),
          ("rc4-md5", 0),
          ("triple-des-sha", 3))
    )


_NsSetWebSSLCipher_Type.__name__ = "Integer32"
_NsSetWebSSLCipher_Object = MibTableColumn
nsSetWebSSLCipher = _NsSetWebSSLCipher_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 12, 1, 1, 7),
    _NsSetWebSSLCipher_Type()
)
nsSetWebSSLCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetWebSSLCipher.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-WEB-MIB",
    **{"netscreenSetWebMibModule": netscreenSetWebMibModule,
       "nsSetWebUI": nsSetWebUI,
       "nsSetWebUICfgTable": nsSetWebUICfgTable,
       "nsSetWebUICfgEntry": nsSetWebUICfgEntry,
       "nsSetWebVsys": nsSetWebVsys,
       "nsSetWebIdleTimeout": nsSetWebIdleTimeout,
       "nsSetWebTimeout": nsSetWebTimeout,
       "nsSetWebPort": nsSetWebPort,
       "nsSetWebSSLPort": nsSetWebSSLPort,
       "nsSetWebSSLCertificate": nsSetWebSSLCertificate,
       "nsSetWebSSLCipher": nsSetWebSSLCipher}
)
