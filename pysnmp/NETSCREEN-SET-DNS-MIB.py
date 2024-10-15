# SNMP MIB module (NETSCREEN-SET-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:55 2024
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

netscreenSetDnsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 3)
)
netscreenSetDnsMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetDNS_ObjectIdentity = ObjectIdentity
nsSetDNS = _NsSetDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3)
)
_NsConfigDnsPriSer_Type = IpAddress
_NsConfigDnsPriSer_Object = MibScalar
nsConfigDnsPriSer = _NsConfigDnsPriSer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 1),
    _NsConfigDnsPriSer_Type()
)
nsConfigDnsPriSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsPriSer.setStatus("current")
_NsConfigDnsSecSer_Type = IpAddress
_NsConfigDnsSecSer_Object = MibScalar
nsConfigDnsSecSer = _NsConfigDnsSecSer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 2),
    _NsConfigDnsSecSer_Type()
)
nsConfigDnsSecSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsSecSer.setStatus("current")


class _NsConfigDnsRefEnable_Type(Integer32):
    """Custom type nsConfigDnsRefEnable based on Integer32"""
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


_NsConfigDnsRefEnable_Type.__name__ = "Integer32"
_NsConfigDnsRefEnable_Object = MibScalar
nsConfigDnsRefEnable = _NsConfigDnsRefEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 3),
    _NsConfigDnsRefEnable_Type()
)
nsConfigDnsRefEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsRefEnable.setStatus("current")


class _NsConfigDnsRefTime_Type(DisplayString):
    """Custom type nsConfigDnsRefTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NsConfigDnsRefTime_Type.__name__ = "DisplayString"
_NsConfigDnsRefTime_Object = MibScalar
nsConfigDnsRefTime = _NsConfigDnsRefTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 4),
    _NsConfigDnsRefTime_Type()
)
nsConfigDnsRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsRefTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-DNS-MIB",
    **{"netscreenSetDnsMibModule": netscreenSetDnsMibModule,
       "nsSetDNS": nsSetDNS,
       "nsConfigDnsPriSer": nsConfigDnsPriSer,
       "nsConfigDnsSecSer": nsConfigDnsSecSer,
       "nsConfigDnsRefEnable": nsConfigDnsRefEnable,
       "nsConfigDnsRefTime": nsConfigDnsRefTime}
)
